#!/usr/bin/env python3
"""Docs 2.0 converter (Spike 1): Bforartists manual .odt -> Markdown pages + image library.

Pipeline per source file
  1. odt_unwrap.py   unwrap banner tables so headings survive
  2. pandoc -t json  syntax tree + extracted media
  3. this script     clean -> section tree -> page assembly -> doc kit tags -> Markdown

Page layout comes from pages.json (which source sections go to which page).
Writes into OUT (content/, snippets/, images/) and a stats JSON for the report.
"""
import json, os, re, subprocess, sys, hashlib, shutil, collections, copy
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
STATS = collections.Counter()
IMAGE_INDEX = {}          # sha -> record
SNIPPETS = {}
DROPPED = collections.Counter()   # words removed on purpose: generated contents lists, file title lines
WARN = []

# ---------------------------------------------------------------- inline helpers

def stringify(inls):
    out = []
    for x in inls:
        t = x["t"]
        if t == "Str": out.append(x["c"])
        elif t in ("Space", "SoftBreak", "LineBreak"): out.append(" ")
        elif t in ("Emph", "Strong", "Underline", "Strikeout", "SmallCaps", "Superscript", "Subscript"):
            out.append(stringify(x["c"]))
        elif t == "Span": out.append(stringify(x["c"][1]))
        elif t == "Quoted": out.append('"' + stringify(x["c"][1]) + '"')
        elif t == "Code": out.append(x["c"][1])
        elif t == "Link": out.append(stringify(x["c"][1]))
    return "".join(out)


def clean_inlines(inls):
    """Unwrap spans/underline, drop empty anchors, merge bold fragments."""
    out = []
    for x in inls:
        t = x["t"]
        if t == "Span":
            inner = clean_inlines(x["c"][1])
            if x["c"][1] and x["c"][1][0]["t"] in ("Space", "SoftBreak"): out.append({"t": "Space"})
            out.extend(inner)
            last = x["c"][1][-1] if x["c"][1] else None
            if last and (last["t"] in ("Space", "SoftBreak") or (last["t"] in ("Strong", "Emph") and last["c"] and last["c"][-1]["t"] == "Space")):
                out.append({"t": "Space"})
        elif t in ("Underline", "SmallCaps"):
            out.extend(clean_inlines(x["c"]))
        elif t in ("Emph", "Strong", "Strikeout", "Superscript", "Subscript"):
            lead = bool(x["c"]) and x["c"][0]["t"] in ("Space", "SoftBreak")
            trail = bool(x["c"]) and (x["c"][-1]["t"] in ("Space", "SoftBreak") or
                                      (x["c"][-1]["t"] == "Str" and x["c"][-1]["c"].endswith(" ")))
            inner = clean_inlines(x["c"])
            if inner and inner[-1]["t"] == "Str" and inner[-1]["c"].endswith(" "):
                inner[-1] = {"t": "Str", "c": inner[-1]["c"].rstrip()}; trail = True
            if stringify(inner).strip():
                if lead: out.append({"t": "Space"})
                out.append({"t": t, "c": inner})
                if trail: out.append({"t": "Space"})
            else:
                out.extend(inner)
        elif t == "Link":
            out.append({"t": "Link", "c": [x["c"][0], clean_inlines(x["c"][1]), x["c"][2]]})
        else:
            out.append(x)
    # collapse runs of spaces
    res = []
    for x in out:
        if x["t"] in ("Space", "SoftBreak") and res and res[-1]["t"] in ("Space", "SoftBreak"):
            continue
        res.append(x)
    while res and res[0]["t"] in ("Space", "SoftBreak", "LineBreak"): res.pop(0)
    while res and res[-1]["t"] in ("Space", "SoftBreak", "LineBreak"): res.pop()
    return res


def words(s):
    return len(re.findall(r"[A-Za-z0-9][\w'’-]*", s))


def slug(s):
    s = s.lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "x"


def cm(v):
    if not v: return None
    m = re.match(r"([\d.]+)\s*(cm|in|mm|px)?", v)
    if not m: return None
    n = float(m.group(1)); u = m.group(2) or "cm"
    return {"cm": n, "mm": n / 10, "in": n * 2.54, "px": n / 37.8}[u]

# ---------------------------------------------------------------- section tree

class Node:
    def __init__(self, level, title, images=None):
        self.level, self.title = level, title
        self.images = images or []   # images found inside the heading
        self.blocks, self.children = [], []
        self.parent = None
        self.src = None

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()

    def text_words(self):
        return sum(block_words(b) for b in self.blocks) + sum(c.text_words() + words(c.title) for c in self.children)


def block_words(b):
    t = b["t"]
    if t in ("Para", "Plain"): return words(stringify(b["c"]))
    if t == "BulletList": return sum(block_words(x) for it in b["c"] for x in it)
    if t == "OrderedList": return sum(block_words(x) for it in b["c"][1] for x in it)
    if t == "RawBlock": return words(re.sub(r"[:{}\[\]=#|*-]", " ", b["c"][1]))
    if t == "Div": return sum(block_words(x) for x in b["c"][1])
    if t == "Table": return words(json.dumps(b))  // 3
    return 0


def is_empty_block(b):
    if b["t"] in ("Para", "Plain"):
        return not b["c"] or (not stringify(b["c"]).strip() and not any(i["t"] == "Image" for i in b["c"]))
    if b["t"] == "HorizontalRule": return True
    return False


def heading_split(inls):
    imgs = [i for i in inls if i["t"] == "Image"]
    rest = [i for i in inls if i["t"] != "Image"]
    title = re.sub(r"\s+", " ", stringify(clean_inlines(rest))).strip()
    return title, imgs


TITLE_NUM = re.compile(r"^\d+(\.\d+)*\s*(-\s*)?")
DROP_TITLES = re.compile(r"^((detailed )?table of contents?|available content)$", re.I)


def has_header(blocks):
    for b in blocks:
        if b["t"] == "Header":
            return True
        if b["t"] == "BulletList" and any(has_header(it) for it in b["c"]):
            return True
        if b["t"] == "OrderedList" and any(has_header(it) for it in b["c"][1]):
            return True
        if b["t"] in ("Div", "BlockQuote") and has_header(b["c"][1] if b["t"] == "Div" else b["c"]):
            return True
    return False


def unlist_headers(blocks):
    """Some .odt chapters put headings inside list items. Lift those lists out so each heading
    becomes a real section (otherwise its images and anchors are left raw)."""
    out = []
    for b in blocks:
        items = b["c"] if b["t"] == "BulletList" else b["c"][1] if b["t"] == "OrderedList" else None
        if items is not None and any(has_header(it) for it in items):
            STATS["lists_with_headings_lifted"] += 1
            for it in items:
                out.extend(unlist_headers(it))
        else:
            out.append(b)
    return out


def build_tree(blocks, srcname):
    blocks = unlist_headers(blocks)
    root = Node(0, "")
    root.src = srcname
    stack = [root]
    for b in blocks:
        if b["t"] == "Header":
            lvl = b["c"][0]
            title, imgs = heading_split(b["c"][2])
            if not title:
                STATS["empty_headings"] += 1
                # keep its images as content of the current section
                for im in imgs:
                    stack[-1].blocks.append({"t": "Para", "c": [im]})
                continue
            n = Node(lvl, title, imgs)
            n.src = srcname
            while stack[-1].level >= lvl: stack.pop()
            n.parent = stack[-1]; stack[-1].children.append(n); stack.append(n)
        elif is_empty_block(b):
            continue
        else:
            stack[-1].blocks.append(b)
    # first H1 = file title (numbered) -> lift its content to root
    for c in list(root.children):
        if c.level == 1 and TITLE_NUM.match(c.title) and re.match(r"^\d", c.title):
            STATS["file_titles"] += 1
            DROPPED[srcname] += words(c.title)
            root.title_icon = c.images[:1]
            idx = root.children.index(c)
            root.children[idx:idx + 1] = c.children
            root.blocks = c.blocks + root.blocks
            for ch in c.children: ch.parent = root
    # drop table-of-contents sections
    def prune(n):
        keep = []
        for c in n.children:
            if DROP_TITLES.match(c.title):
                STATS["toc_sections_dropped"] += 1
                DROPPED[srcname] += words(c.title) + c.text_words()
                continue
            prune(c); keep.append(c)
        n.children = keep
    prune(root)
    return root


def find(root, title_re):
    rx = re.compile(title_re, re.I)
    for n in root.walk():
        if n is not root and rx.search(n.title):
            return n
    raise KeyError(f"{title_re} not found in {root.src}")

# ---------------------------------------------------------------- images

def png_size(data):
    import struct
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    return (0, 0)


class Library:
    def __init__(self, out):
        self.out = out

    def add(self, media_root, src, place, hint):
        if src.startswith(("http://", "https://")):
            STATS["remote_images"] += 1
            return src
        fp = os.path.join(media_root, src)
        if not os.path.exists(fp):
            WARN.append(f"missing image {src}"); return None
        data = open(fp, "rb").read()
        sha = hashlib.sha256(data).hexdigest()
        rec = IMAGE_INDEX.get(sha)
        if rec:
            rec["uses"] += 1; STATS["image_dupes_reused"] += 1
            if place not in rec["places"]: rec["places"].append(place)
            return rec["path"]
        ext = os.path.splitext(src)[1].lower().replace(".jpeg", ".jpg")
        base = f"/images/{place}/{slug(hint)[:48]}"
        path = base + ext; i = 2
        while any(r["path"] == path for r in IMAGE_INDEX.values()):
            path = f"{base}-{i}{ext}"; i += 1
        os.makedirs(os.path.dirname(os.path.join(self.out, path.lstrip("/"))), exist_ok=True)
        shutil.copyfile(fp, os.path.join(self.out, path.lstrip("/")))
        try:
            w, h = Image.open(fp).size
        except Exception:
            w, h = png_size(data)
            WARN.append(f"image not readable by Pillow, size from header: {src}")
        IMAGE_INDEX[sha] = {"path": path, "sha": sha[:16], "px": [w, h], "bytes": len(data),
                            "uses": 1, "places": [place], "source": src}
        STATS["images_unique"] += 1
        return path


def image_kind(im):
    kv = dict(im["c"][0][2])
    w, h = cm(kv.get("width")), cm(kv.get("height"))
    if w is None: return "full", w
    if w <= 0.75 and (h or 0) <= 0.75: return "icon", w
    if w <= 3.2: return "thumb", w
    if w <= 9.5: return "right", w
    return "full", w


def make_image(path, alt, cls):
    return {"t": "Image", "c": [["", [cls] if cls != "full" else [], []], [{"t": "Str", "c": alt}], [path, ""]]}


class Ctx:
    def __init__(self, lib, media_root, place, page_title):
        self.lib, self.media_root, self.place = lib, media_root, place
        self.heading = page_title

# ---------------------------------------------------------------- block transforms

LEGEND = re.compile(r"^\s*(?P<label>[^()]{2,60}?)\s*\(\s*(?P<color>green|yellow|blue|red|orange|purple|violet|pink|cyan|magenta|turquoise|brown|white|grey|gray|no colou?r)\s*\)\s*$", re.I)
CALLOUT = re.compile(r"^\s*(note|hint|tip|warning|attention|important|caution)\s*[:!]\s*", re.I)
KBD = re.compile(r"\b((?:ctrl|shift|alt|cmd)(?:\s*\+\s*(?:ctrl|shift|alt))*\s*\+\s*(?:[A-Z0-9]\b|F\d{1,2}\b|space(?:bar)?\b|tab\b|enter\b|del(?:ete)?\b|home\b|esc\b|middle mouse button|left mouse button|right mouse button|mouse ?wheel|scroll ?wheel))", re.I)


def kbd_norm(s):
    parts = [p.strip() for p in s.split("+")]
    fix = {"ctrl": "Ctrl", "shift": "Shift", "alt": "Alt", "cmd": "Cmd", "spacebar": "Space", "space": "Space",
           "middle mouse button": "MMB", "left mouse button": "LMB", "right mouse button": "RMB",
           "delete": "Del", "del": "Del", "enter": "Enter", "return": "Enter", "esc": "Esc", "escape": "Esc", "tab": "Tab", "scroll wheel": "Wheel", "scrollwheel": "Wheel", "mouse wheel": "Wheel"}
    return " + ".join(fix.get(p.lower(), p.upper() if len(p) == 1 else p.capitalize()) for p in parts)


KEYNAME = re.compile(r"^(ctrl|shift|alt|cmd|space(bar)?|enter|return|tab|esc|escape|del|delete|home|end|backspace|F\d{1,2}|[A-Z0-9]|numpad ?[0-9+\-.*/]|(ctrl|shift|alt)( ?\+ ?\S+)+)$", re.I)
UPPERKEY = re.compile(r"\b(SPACE|SPACEBAR|ENTER|TAB|ESC|DEL|CTRL|SHIFT|ALT|F\d{1,2})\b")


def tag_kbd(inls):
    out = []
    for x in inls:
        if x["t"] == "Str":
            out.append(x)
        elif x["t"] in ("Emph", "Strong"):
            txt = stringify(x["c"]).strip()
            if txt and KEYNAME.match(txt) and (len(txt) > 1 or txt.isupper()):
                out.append({"t": "Strong", "c": [{"t": "Str", "c": kbd_norm(txt)}]})
                STATS["hotkeys_tagged"] += 1
            else:
                out.append({"t": x["t"], "c": tag_kbd(x["c"])})
        else:
            out.append(x)
    # upper-case key names written as plain words (SPACE, ENTER)
    tmp = []
    for x in out:
        if x["t"] == "Str" and UPPERKEY.search(x["c"]):
            pos = 0
            for m in UPPERKEY.finditer(x["c"]):
                if m.start() > pos: tmp.append({"t": "Str", "c": x["c"][pos:m.start()]})
                tmp.append({"t": "Str", "c": kbd_norm(m.group(1))})
                STATS["hotkeys_tagged"] += 1
                pos = m.end()
            if pos < len(x["c"]): tmp.append({"t": "Str", "c": x["c"][pos:]})
        else:
            tmp.append(x)
    out = tmp
    # work on the flattened string level: rebuild Str runs
    s = []
    for x in out:
        s.append(x)
    joined = []
    buf = []
    def flush():
        if not buf: return
        text = "".join(" " if b["t"] in ("Space", "SoftBreak") else b["c"] for b in buf)
        pos = 0
        for m in KBD.finditer(text):
            if m.start() > pos: joined.append({"t": "Str", "c": text[pos:m.start()]})
            joined.append({"t": "Str", "c": kbd_norm(m.group(1))})
            STATS["hotkeys_tagged"] += 1
            pos = m.end()
        if pos < len(text): joined.append({"t": "Str", "c": text[pos:]})
        buf.clear()
    for x in s:
        if x["t"] in ("Str", "Space", "SoftBreak"):
            buf.append(x)
        else:
            flush(); joined.append(x)
    flush()
    return joined


def process_inlines_images(inls, ctx, pulled):
    """Replace images in a paragraph: tiny -> inline icon, others pulled out as figures."""
    out = []
    for x in inls:
        if x["t"] == "Image":
            kind, w = image_kind(x)
            if kind == "icon":
                p = ctx.lib.add(ctx.media_root, x["c"][2][0], ctx.place, ctx.heading + " icon")
                if p: out.append(make_image(p, "", "icon")); STATS["inline_icons"] += 1
            else:
                alt = stringify(x["c"][1]).strip() or ctx.heading
                p = ctx.lib.add(ctx.media_root, x["c"][2][0], ctx.place, alt)
                if p: pulled.append({"t": "Para", "c": [make_image(p, alt, kind)]}); STATS["figures_" + kind] += 1
        elif x["t"] in ("Emph", "Strong", "Strikeout", "Superscript", "Subscript"):
            out.append({"t": x["t"], "c": process_inlines_images(x["c"], ctx, pulled)})
        elif x["t"] == "Link":
            out.append({"t": "Link", "c": [x["c"][0], process_inlines_images(x["c"][1], ctx, pulled), x["c"][2]]})
        else:
            out.append(x)
    return clean_inlines(out)


def transform_blocks(blocks, ctx):
    out = []
    for b in blocks:
        t = b["t"]
        if t in ("Para", "Plain"):
            pulled = []
            inls = process_inlines_images(clean_inlines(b["c"]), ctx, pulled)
            only_figure = not stringify(inls).strip() and not any(i["t"] == "Image" for i in inls)
            out.extend(pulled)
            if not only_figure:
                out.append({"t": t, "c": tag_kbd(inls)})
        elif t == "BulletList":
            out.append({"t": t, "c": [tight(transform_blocks(it, ctx)) for it in b["c"]]})
        elif t == "OrderedList":
            out.append({"t": t, "c": [b["c"][0], [tight(transform_blocks(it, ctx)) for it in b["c"][1]]]})
        elif t == "Div":
            out.extend(transform_blocks(b["c"][1], ctx))
        elif t == "BlockQuote":
            out.extend(transform_blocks(b["c"], ctx))
        elif t == "Table":
            co = callout_table(b, ctx)
            if co is not None:
                out.append(co); STATS["callout_tables"] += 1
            else:
                out.append(walk_table_images(single_block_cells(b), ctx)); STATS["data_tables"] += 1
        else:
            out.append(b)
    return detect_legends(detect_callouts(fake_bullets(out)))


def tight(item):
    """Editor writes list items without blank lines between them: first paragraph -> Plain."""
    if item and item[0]["t"] == "Para":
        item = [{"t": "Plain", "c": item[0]["c"]}] + item[1:]
    return item


BULLET = re.compile(r"^\s*[•·▪◦‣–]\s+")


def fake_bullets(blocks):
    """Runs of paragraphs starting with a bullet character -> a real bullet list (words unchanged)."""
    out, run = [], []
    def flush():
        if run:
            out.append({"t": "BulletList", "c": [[{"t": "Plain", "c": it}] for it in run]})
            STATS["fake_bullet_items"] += len(run)
            run.clear()
    for b in blocks:
        if b["t"] in ("Para", "Plain") and b["c"] and b["c"][0]["t"] == "Str" and BULLET.match(b["c"][0]["c"]):
            first = BULLET.sub("", b["c"][0]["c"])
            it = ([{"t": "Str", "c": first}] if first else []) + b["c"][1:]
            while it and it[0]["t"] in ("Space", "SoftBreak"): it = it[1:]
            run.append(it)
        else:
            flush(); out.append(b)
    flush()
    return out


def walk_table_images(tbl, ctx):
    def fix(o):
        if isinstance(o, dict):
            if o.get("t") in ("Para", "Plain"):
                pulled = []
                inls = process_inlines_images(clean_inlines(o["c"]), ctx, pulled)
                for p in pulled:  # keep figures inside the cell as thumbs
                    im = p["c"][0]; im["c"][0][1] = ["thumb"]; inls = [im, {"t": "Space"}] + inls
                return {"t": o["t"], "c": tag_kbd(inls)}
            return {k: fix(v) for k, v in o.items()}
        if isinstance(o, list): return [fix(v) for v in o]
        return o
    return fix(tbl)


CALLOUT_WORDS = {"tip": "Tip", "hint": "Tip", "note": "Note", "warning": "Warning", "attention": "Warning",
                 "caution": "Warning", "important": "Important"}


def table_cells(tbl):
    """All cells of a pandoc Table, row by row, as lists of blocks."""
    _, _, _, head, bodies, foot = tbl["c"]
    rows = list(head[1])
    for body in bodies:
        rows += body[2] + body[3]
    rows += foot[1]
    return [[cell[4] for cell in row[1]] for row in rows]


def callout_table(tbl, ctx):
    """1-column .odt box whose first cell is 'Tip'/'Note'/... -> a quote callout (words unchanged)."""
    rows = table_cells(tbl)
    if not rows or any(len(r) != 1 for r in rows):
        return None
    while rows and not rows[0][0] or (rows and not json.dumps(rows[0][0]).count('"Str"')
                                      and not json.dumps(rows[0][0]).count('"Image"')):
        rows = rows[1:]                                   # empty header row of the .odt box
    if len(rows) < 2:
        return None
    first = " ".join(stringify(b["c"]) for b in rows[0][0] if b["t"] in ("Para", "Plain")).strip().rstrip(":")
    label = CALLOUT_WORDS.get(first.lower())
    if not label:
        return None
    paras = []
    for r in rows[1:]:
        for b in transform_blocks(r[0], ctx):
            md = render([b]).strip()
            if md:
                paras.append(md)
    if not paras:
        return None
    lines = []
    for i, md in enumerate(paras):
        if i == 0:
            md = f"**{label}:** " + md
        else:
            lines.append(">")
        lines += ["> " + ln if ln.strip() else ">" for ln in md.split("\n")]
    return raw("\n".join(lines))


def single_block_cells(tbl):
    """Cells with several paragraphs -> one line joined by a space (the editor drops <br> inside table cells)."""
    def fix_cell(cell):
        blocks = cell[4]
        if len([b for b in blocks if b["t"] in ("Para", "Plain")]) > 1 and all(b["t"] in ("Para", "Plain") for b in blocks):
            inl = []
            for k, b in enumerate(blocks):
                if k: inl.append({"t": "Space"})
                inl += b["c"]
            cell = [cell[0], cell[1], cell[2], cell[3], [{"t": "Plain", "c": inl}]]
            STATS["cells_joined"] += 1
        return cell
    t = copy.deepcopy(tbl)
    _, _, _, head, bodies, foot = t["c"]
    for row in head[1]: row[1] = [fix_cell(c) for c in row[1]]
    for body in bodies:
        for row in body[2] + body[3]: row[1] = [fix_cell(c) for c in row[1]]
    for row in foot[1]: row[1] = [fix_cell(c) for c in row[1]]
    return t


def para_text(b):
    return stringify(b["c"]) if b["t"] in ("Para", "Plain") else None


def detect_callouts(blocks):
    out = []
    for b in blocks:
        s = para_text(b)
        m = CALLOUT.match(s) if s else None
        if m:
            kind = {"hint": "tip", "attention": "warn", "warning": "warn", "caution": "warn", "important": "imp"}.get(m.group(1).lower(), m.group(1).lower())
            md = render_inlines(b["c"])
            md = re.sub(r"^[*_\s]*(note|hint|tip|warning|attention|important|caution)[*_\s]*[:!][*_\s]*", "", md, count=1, flags=re.I).strip()
            if md.count("*") % 2: md = md.rstrip("*").strip()
            label = {"tip": "Tip", "note": "Note", "warn": "Warning", "imp": "Important"}.get(kind, kind.title())
            out.append(raw("\n".join("> " + ln if ln.strip() else ">" for ln in f"**{label}:** {md}".split("\n"))))
            STATS["callouts"] += 1
        else:
            out.append(b)
    return out


def detect_legends(blocks):
    """Figure followed by 'Label ( Colour )' lines -> hotspots block (labels + colours, boxes filled later)."""
    out, i = [], 0
    while i < len(blocks):
        b = blocks[i]
        s = para_text(b)
        if s and LEGEND.match(s):
            # figure right before (skip back over figure paras)
            fig = None
            if out and out[-1]["t"] == "Para" and len(out[-1]["c"]) == 1 and out[-1]["c"][0]["t"] == "Image":
                fig = out.pop()["c"][0]
            items, extra = [], []
            while i < len(blocks):
                s = para_text(blocks[i])
                m = LEGEND.match(s) if s else None
                if m:
                    items.append([m.group("label").strip(" *"), m.group("color").lower().replace("colour", "color"), ""])
                    i += 1; continue
                # a figure between legend lines (small thumb) or one description paragraph
                if blocks[i]["t"] == "Para" and len(blocks[i]["c"]) == 1 and blocks[i]["c"][0]["t"] == "Image" and items:
                    extra.append(blocks[i]); i += 1; continue
                if s and items and not items[-1][2] and words(s) < 60 and i + 1 < len(blocks) and LEGEND.match(para_text(blocks[i + 1]) or ""):
                    items[-1][2] = render_inlines(blocks[i]["c"]); i += 1; continue
                break
            if fig is not None:
                img = fig["c"][2][0]
                alt = stringify(fig["c"][1]) or "Screenshot"
                lines = [f"![{alt}]({img})", ""]
                for lab, col, desc in items:
                    lines.append(f"- **{lab}** ({col})" + (f": {desc}" if desc else ""))
                out.append(raw("\n".join(lines)))
                STATS["hotspot_figures"] += 1
                out.extend(extra)
            else:
                for lab, col, desc in items:
                    out.append({"t": "Para", "c": [{"t": "Strong", "c": [{"t": "Str", "c": lab}]}, {"t": "Str", "c": f" ({col})" + (": " if desc else "")}]})
                    if desc: out.append(raw(desc))
                out.extend(extra)
                STATS["legends_without_figure"] += 1
            continue
        out.append(b); i += 1
    return out


def raw(md):
    return {"t": "RawBlock", "c": ["markdown", md]}

# ---------------------------------------------------------------- rendering

PANDOC_OUT = ("markdown-smart-simple_tables-multiline_tables-grid_tables-raw_attribute-bracketed_spans"
              "-native_spans-native_divs-fenced_divs-header_attributes-auto_identifiers-implicit_figures"
              "-escaped_line_breaks-all_symbols_escapable-fenced_code_attributes+pipe_tables+link_attributes")


def render(blocks):
    doc = {"pandoc-api-version": [1, 23, 1], "meta": {}, "blocks": blocks}
    r = subprocess.run(["pandoc", "-f", "json", "-t", PANDOC_OUT, "--wrap=none"],
                       input=json.dumps(doc), capture_output=True, text=True, check=True)
    md = r.stdout
    md = re.sub(r"\\([\[\]>*_#`|<])", r"\1", md) if False else md
    return md.strip() + "\n"


def render_inlines(inls):
    return render([{"t": "Plain", "c": inls}]).strip()

# ---------------------------------------------------------------- page assembly

def simple_leaf(n, max_words=70):
    if n.children: return False
    if n.images and any(image_kind(i)[0] != "icon" for i in n.images): return False
    if len(n.title.split()) > 7: return False
    if any(b["t"] not in ("Para", "Plain") for b in n.blocks): return False
    if any(i["t"] == "Image" and image_kind(i)[0] != "icon" for b in n.blocks for i in b["c"]): return False
    return words(" ".join(stringify(b["c"]) for b in n.blocks)) <= max_words


def option_row(n, ctx):
    """A setting whose children are only its choices -> one row listing the choices."""
    if not n.children or len(n.children) > 8: return None
    if n.images and any(image_kind(i)[0] != "icon" for i in n.images): return None
    if any(b["t"] not in ("Para", "Plain") for b in n.blocks): return None
    if words(" ".join(stringify(b["c"]) for b in n.blocks)) > 40: return None
    if not all(simple_leaf(c, 40) for c in n.children): return None
    ctx.heading = n.title
    pulled = []                                   # icons inside the text go through the image library too
    own = " ".join(render_inlines(process_inlines_images(clean_inlines(b["c"]), ctx, pulled)) for b in n.blocks).strip()
    opts = []
    for c in n.children:
        t = re.sub(r"^(method|mode)\s+", "", c.title, flags=re.I)
        d = " ".join(render_inlines(tag_kbd(process_inlines_images(clean_inlines(b["c"]), ctx, pulled)))
                     for b in c.blocks).strip()
        opts.append(f"**{t}**" + (f": {d}" if d else ""))
    STATS["option_rows"] += 1
    desc = ((own + " · ") if own else "") + " · ".join(opts)
    return f"| {n.title.replace('|', '/')} | {desc.replace(chr(10), ' ').replace('|', '/')} |"


def leaf_row(n, ctx):
    """A short heading with one or two short paragraphs and nothing else -> table row."""
    r = option_row(n, ctx)
    if r: return r
    if n.children or n.images and any(image_kind(i)[0] != "icon" for i in n.images): return None
    if len(n.title.split()) > 7: return None
    if any(b["t"] not in ("Para", "Plain") for b in n.blocks): return None
    if any(i["t"] == "Image" and image_kind(i)[0] != "icon" for b in n.blocks for i in b["c"]): return None
    text = " ".join(stringify(b["c"]) for b in n.blocks)
    if words(text) > 70: return None
    ctx.heading = n.title
    pulled = []
    cells = []
    for b in n.blocks:
        cells.append(render_inlines(tag_kbd(process_inlines_images(clean_inlines(b["c"]), ctx, pulled))))
    icon = ""
    for im in n.images:
        p = ctx.lib.add(ctx.media_root, im["c"][2][0], ctx.place, n.title + " icon")
        if p: icon = f"![]({p}){{.icon}} "
    desc = " ".join(c.replace("\n", " ").replace("|", "\\|") for c in cells).strip() or "—"
    return f"| {icon}{n.title.replace('|', '/')} | {desc} |"


def emit_node(n, level, ctx, opts, lines):
    STATS["max_depth_seen"] = max(STATS["max_depth_seen"], level)
    ctx.heading = n.title
    if level > 6:
        STATS["deep_headings_as_labels"] += 1
        lines.append(("md", f"**{n.title}**"))
    else:
        lines.append(("md", "#" * level + " " + n.title))
    tool = opts.get("tool_level") == n.level_rel and opts.get("tool_prefix")
    if tool:
        STATS["tool_card_candidates"] += 1   # recognised later from the heading; nothing written
    for im in n.images:
        kind, _ = image_kind(im)
        p = ctx.lib.add(ctx.media_root, im["c"][2][0], ctx.place, n.title)
        if p:
            cls = "thumb" if kind in ("icon", "thumb") else kind
            lines.append(("md", f"![{n.title}]({p}){{.{cls}}}" if cls != "full" else f"![{n.title}]({p})"))
            STATS["heading_images"] += 1
    body = transform_blocks(n.blocks, ctx)
    if body: lines.append(("blocks", body))
    # children: fold runs of short leaves into a table
    run = []
    def flush_run():
        if len(run) >= opts.get("min_rows", 2):
            head = opts.get("table_head", ("Entry", "What it does"))
            lines.append(("md", f"| {head[0]} | {head[1]} |\n|---|---|\n" + "\n".join(r for r, _ in run)))
            STATS["table_rows"] += len(run); STATS["tables_from_leaves"] += 1
        else:
            for _, c in run: emit_node(c, level + 1, ctx, opts, lines)
        run.clear()
    for c in n.children:
        c.level_rel = n.level_rel + 1
        r = leaf_row(c, ctx) if opts.get("fold", True) else None
        if r: run.append((r, c)); continue
        flush_run()
        emit_node(c, level + 1, ctx, opts, lines)
    flush_run()


def assemble(spec, trees, lib, out_dir, media):
    lines = []
    shared = []
    place = spec["images"]
    ctx = Ctx(lib, None, place, spec["title"])
    for part in spec["parts"]:
        if "include" in part:
            if part.get("heading"): lines.append(("md", "## " + part["heading"]))
            sn = SNIPPETS[part["include"]]
            rel = os.path.relpath(os.path.join(out_dir, sn["file"]), os.path.dirname(os.path.join(out_dir, spec["file"])))
            lines.append(("md", f"*Shared section: [{sn['title']}]({rel})*"))
            shared.append(os.path.join(os.environ.get("DOCS_ROOT", ""), sn["file"]))   # repo path, as the editor stores it
            STATS["includes"] += 1
            continue
        if "note" in part:
            lines.append(("md", part["note"]))
            continue
        root = trees[part["src"]]
        ctx.media_root = media[part["src"]]
        opts = dict(spec.get("opts", {})); opts.update(part.get("opts", {}))
        nodes = [root] if part.get("select") in (None, "*") else [find(root, s) for s in part["select"]]
        for n in nodes:
            n.level_rel = 0
            if n is root or part.get("as_intro"):
                ctx.heading = spec["title"]
                body = transform_blocks(n.blocks, ctx)
                if body: lines.append(("blocks", body))
                for c in n.children:
                    c.level_rel = 1
                    emit_node(c, 2 + part.get("shift", 0), ctx, opts, lines)
            else:
                n.level_rel = 1
                if part.get("rename"): n.title = part["rename"]
                emit_node(n, 2 + part.get("shift", 0), ctx, opts, lines)
    # render blocks
    md_parts = []
    for kind, v in lines:
        md_parts.append(v if kind == "md" else render(v).strip())
    body = "\n\n".join(p for p in md_parts if p.strip()) + "\n"
    body = postfix(body)
    pre = os.environ.get("DOCS_URL_PREFIX", "")
    if pre:
        body = body.replace("](/images/", f"]({pre}/images/").replace("img=/images/", f"img={pre}/images/")
    fm = {k: spec[k] for k in ("id", "title", "slug", "section", "path", "icon") if k in spec}
    fm.update({"version": "5.1", "status": "draft", "screenshots": "5.1",
               "source": [p["src"] + ".odt" for p in spec["parts"] if "src" in p and not p["src"].startswith("web:")]})
    fm["source"] = sorted(set(fm["source"])) + sorted({"webflow:" + p["web"] for p in spec["parts"] if "web" in p})
    if shared: fm["shared"] = shared
    if spec.get("status"): fm["status"] = spec["status"]
    head = editor_yaml(fm)
    body = body.strip("\n") + "\n\n"
    if body.rstrip("\n").split("\n")[-1].startswith("|"):
        body += "\n"                                      # the editor keeps two blank lines after a final table
    path = os.path.join(out_dir, spec["file"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(head + body)
    return path, words(re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?", "", body))


YAML_PLAIN_BAD = re.compile(r"^$|^[-?:,\[\]{}#&*!|>'\"%@`\s]|: |\s#|\s$|^(true|false|yes|no|on|off|null|~|[-+]?(\d[\d_]*)?\.?\d+([eE][-+]?\d+)?|0x[0-9a-fA-F]+)$", re.I)


def yaml_scalar(v):
    if isinstance(v, bool): return "true" if v else "false"
    if isinstance(v, (int, float)): return str(v)
    v = str(v)
    return json.dumps(v, ensure_ascii=False) if YAML_PLAIN_BAD.search(v) or "\n" in v else v


def editor_yaml(fm):
    """Front matter the way Pages CMS saves it: plain scalars, quotes only when needed, block lists."""
    out = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            if not v: continue                      # the editor drops empty lists
            out.append(f"{k}:")
            out += [f"  - {yaml_scalar(x)}" for x in v]
        else:
            out.append(f"{k}: {yaml_scalar(v)}")
    return "\n".join(out) + "\n---\n"


EDITOR_ESC = re.compile(r"([\\`*_\[\]~])")


def editor_text(t):
    """Link text the way the Pages CMS editor (Tiptap markdown) writes it."""
    return t.replace("<", "&lt;").replace(">", "&gt;")   # the editor writes no backslash escapes and keeps & raw


def split_row(line):
    row, cells, cur, i = line.strip()[1:-1], [], "", 0
    while i < len(row):
        if row[i] == "\\" and i + 1 < len(row):
            cur += row[i:i + 2]; i += 2; continue
        if row[i] == "|":
            cells.append(cur); cur = ""
        else:
            cur += row[i]
        i += 1
    cells.append(cur)
    return [c.strip() for c in cells]


def editor_tables(md):
    """Write tables as the editor saves them: trimmed rows, delimiter padded to the widest cell."""
    lines, out, i = md.split("\n"), [], 0
    delim = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and delim.match(lines[i + 1]) and "-" in lines[i + 1]:
            block = [lines[i], lines[i + 1]]; j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                block.append(lines[j]); j += 1
            rows = [split_row(l) for k, l in enumerate(block) if k != 1]
            n = max(len(r) for r in rows)
            rows = [r + [""] * (n - len(r)) for r in rows]
            widths = [max(3, max(len(r[c]) for r in rows)) for c in range(n)]
            fmt = lambda r: "| " + " | ".join(r) + " |"
            out.append(fmt(rows[0]))
            out.append("| " + " | ".join("-" * w for w in widths) + " |")
            out.extend(fmt(r) for r in rows[1:])
            STATS["tables_editor_format"] += 1
            i = j
        else:
            out.append(lines[i]); i += 1
    return "\n".join(out)


CODE_TOKEN = re.compile(r"(?<!\S)(\*?)(\S*\\[*_\\\[\]`]\S*?)(\*?)(?=[.,;:)]?(?:\s|$))")
BARE_URL = re.compile(r"(?<![(<\[`])\bhttps?://[^\s<>()\[\]`]+[^\s<>()\[\]`.,;:!?'\"]")


def editor_stable_line(line):
    """Rewrite one prose line so the Pages CMS editor saves it unchanged:
    it drops backslash escapes and writes < > as &lt; &gt;."""
    if not line.strip() or line.startswith("    ") or line.startswith("```"):
        return line
    m = re.match(r"^((?:> ?)*(?:#{1,6} |[-*] |\d+\. )?)(.*)$", line)
    lead, text = m.group(1), m.group(2)
    # protect code spans, links and <br>
    keep = []
    def hold(x):
        keep.append(x.group(0)); return f"\x00{len(keep) - 1}\x00"
    text = re.sub(r"`[^`]*`|!?\[[^\]]*\]\([^)]*\)|<br>", hold, text)
    # a path line full of backslashes -> one code span
    if text.count("\\\\") >= 2 or text.count("\\\\") >= 1 and ":" in text[:4]:
        inner = re.sub(r"\\(.)", r"\1", text)
        text = "`" + inner.replace("`", "") + "`"
        STATS["paths_as_code"] += 1
    else:
        def code_tok(mm):
            STATS["tokens_as_code"] += 1
            return "`" + re.sub(r"\\(.)", r"\1", mm.group(2)) + "`"
        text = CODE_TOKEN.sub(code_tok, text)
        text = re.sub(r"\\([$|~#+!.()\-{}])", r"\1", text)          # escapes CommonMark never needed here
        text = text.replace("\\<", "&lt;").replace("\\>", "&gt;")
        text = re.sub(r">", "&gt;", text)
        text = re.sub(r"(?<!&)<(?!br>)", "&lt;", text)
        text = BARE_URL.sub(lambda u: f"[{u.group(0)}]({u.group(0)})", text)
    text = re.sub(r"\x00(\d+)\x00", lambda x: keep[int(x.group(1))], text)
    return lead + text


def editor_stable(md):
    out, fence = [], False
    for line in md.split("\n"):
        if line.startswith("```"):
            fence = not fence; out.append(line); continue
        if fence:
            out.append(line); continue
        if line.lstrip().startswith("|"):
            if re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
                out.append(line); continue
            cells = split_row(line)
            cells = [editor_stable_line(c.replace("\\|", "\x02")).replace("\x02", "\\|") for c in cells]
            out.append("| " + " | ".join(cells) + " |"); continue
        out.append(editor_stable_line(line))
    md = "\n".join(out)
    md = re.sub(r"^(\s*[-*]) +$", r"\1 ", md, flags=re.M)              # empty list item: "- "
    return md


def editor_spacing(md):
    """Tables get two blank lines before and after, like the editor writes them."""
    lines = md.split("\n"); out = []; i = 0
    while i < len(lines):
        if lines[i].startswith("|") and (i == 0 or not lines[i - 1].startswith("|")):
            while out and out[-1] == "": out.pop()
            if out: out += ["", ""]
            while i < len(lines) and lines[i].startswith("|"):
                out.append(lines[i]); i += 1
            out += ["", ""]
            while i < len(lines) and lines[i] == "": i += 1
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out)


def postfix(md):
    md = re.sub(r"<(https?://[^>\s]+)>", lambda m: f"[{editor_text(m.group(1))}]({m.group(1)})", md)
    md = md.replace("\\'", "'").replace('\\"', '"')
    md = re.sub(r"(!\[[^\]]*\]\([^)]*\))\{\.[a-z]+\}", r"\1", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = editor_stable(md)
    md = editor_tables(md)
    md = editor_spacing(md)
    md = re.sub(r"^((?!\|).*\S) {2,}(?=\S)", lambda m: re.sub(r" {2,}", " ", m.group(0)), md, flags=re.M)
    md = md.replace('{target="_blank"}', "")
    md = re.sub(r"(?<!!)\[\]\([^)]*\)", "", md)          # empty links carry no words
    md = re.sub(r"\*\*\s*\*\*", "", md)
    return md

# ---------------------------------------------------------------- main

def main(manual_dir, cfg_path, out_dir, work):
    cfg = json.load(open(cfg_path))
    os.makedirs(work, exist_ok=True)
    trees, media = {}, {}
    global SNIPPETS
    SNIPPETS = {sn["id"].split(".", 1)[1]: sn for sn in cfg.get("snippets", [])}
    only = [x for x in os.environ.get("DOCS_ONLY", "").split(",") if x]     # convert just these page ids (prefixes)
    if only:
        cfg["pages"] = [pg for pg in cfg["pages"] if any(pg["id"] == o or pg["id"].startswith(o + ".") for o in only)]
        cfg["snippets"] = [sn for sn in cfg.get("snippets", []) if any(sn["id"] == o for o in only)]
    for pg in cfg["pages"] + cfg.get("snippets", []):
        for p in pg["parts"]:
            if "web" in p: p["src"] = "web:" + p["web"]
    srcs = sorted({p["src"] for pg in cfg["pages"] + cfg.get("snippets", []) for p in pg["parts"] if "src" in p})
    src_words = {}
    web_dir = cfg.get("web_dir", "web")
    for s in srcs:
        if s.startswith("web:"):
            key = s[4:]
            r = subprocess.run(["pandoc", "-f", "html", "-t", "json", os.path.join(web_dir, key + ".html")],
                               capture_output=True, text=True, check=True)
            trees[s] = build_tree(json.loads(r.stdout)["blocks"], s)
            media[s] = web_dir
            txt = subprocess.run(["pandoc", "-f", "html", "-t", "plain", "--wrap=none", os.path.join(web_dir, key + ".html")], capture_output=True, text=True).stdout
            src_words[s] = words(txt)
            continue
        odt = os.path.join(manual_dir, s + ".odt")
        fixed = os.path.join(work, slug(s) + ".odt")
        subprocess.run([sys.executable, "-I", os.path.join(HERE, "odt_unwrap.py"), odt, fixed], check=True, capture_output=True)
        mdir = os.path.join(work, "media", slug(s))
        os.makedirs(mdir, exist_ok=True)
        r = subprocess.run(["pandoc", "-f", "odt", "-t", "json", "--extract-media", mdir, fixed],
                           capture_output=True, text=True, check=True)
        doc = json.loads(r.stdout)
        # pandoc rewrites image src to the extraction dir; make relative to mdir
        def rel(o):
            if isinstance(o, dict):
                if o.get("t") == "Image":
                    o["c"][2][0] = os.path.relpath(o["c"][2][0], mdir)
                for v in o.values(): rel(v)
            elif isinstance(o, list):
                for v in o: rel(v)
        rel(doc)
        trees[s] = build_tree(doc["blocks"], s)
        media[s] = mdir
        txt = subprocess.run(["pandoc", "-f", "odt", "-t", "plain", "--wrap=none", odt], capture_output=True, text=True).stdout
        src_words[s] = words(txt)
    lib = Library(out_dir)
    report = {"pages": [], "snippets": []}
    for kind in ("snippets", "pages"):
        for spec in cfg.get(kind, []):
            path, w = assemble(spec, trees, lib, out_dir, media)
            report[kind].append({"file": spec["file"], "words": w, "sources": [p.get("src") for p in spec["parts"] if "src" in p]})
    report["source_words"] = src_words
    report["dropped_words"] = dict(DROPPED)
    report["stats"] = dict(STATS)
    report["images"] = sorted(IMAGE_INDEX.values(), key=lambda r: r["path"])
    report["warnings"] = WARN
    json.dump(report, open(os.path.join(work, "convert-report.json"), "w"), indent=1)
    with open(os.path.join(out_dir, "images", "index.csv"), "w") as f:
        f.write("path,sha256_16,width_px,height_px,bytes,uses,source_odt_media\n")
        for r in report["images"]:
            f.write(f"{r['path']},{r['sha']},{r['px'][0]},{r['px'][1]},{r['bytes']},{r['uses']},{r['source']}\n")
    print(json.dumps(report["stats"], indent=1))
    print("pages", [(p["file"], p["words"]) for p in report["pages"]])
    print("warnings", WARN[:10])


if __name__ == "__main__":
    main(*sys.argv[1:5])
