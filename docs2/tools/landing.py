"""Landing pages (cards for a group's or chapter's children) and the navigation file.

Shared by sync.py (Webflow) and render.py (preview).

  - Every section is published as a page of its own at /docs/<section id>: its index.md
    (intro) plus cards for its chapters, grouped by `categories` in sections.yml.
  - Every page that has sub-pages gets cards for them, unless its header says `cards: false`.
    A placeholder group page ("listed in the sidebar under …") is replaced by its cards.
  - The cards are sent as a plain list of links inside <div class="ui-doc-cards">, which
    survives Webflow's rich text; the docs script turns each item into a card with its icon.
  - nav.json is the whole tree (sections → pages, any depth) with titles, addresses and
    icons; the docs script draws the sidebar from it.
"""
import html as htmllib
import json
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
PLACEHOLDER = re.compile(r"<p>The pages of this part are listed in the sidebar under <em>[^<]*</em>\.</p>")


def load_icons():
    data = json.load(open(os.path.join(HERE, "icons.json"), encoding="utf-8"))
    return data["base"], data["icons"]


def icon_file(name, icons):
    """An icon name (`view3d`), a Webflow file name or a full URL → file name or URL; '' if unknown."""
    name = str(name or "").strip()
    if not name:
        return ""
    if name.startswith("http") or re.match(r"^[0-9a-f]{24}_", name):
        return name
    return icons.get(name, "")


def sections_cfg():
    cfg = yaml.safe_load(open(os.path.join(HERE, "sections.yml"), encoding="utf-8"))
    return {s["id"]: s for s in cfg.get("sections", [])}


def children_map(tree):
    """parent id → child nodes; a section id → its top-level nodes."""
    kids = {}
    for sec in tree:
        for n in sec.nodes:
            kids.setdefault(n.parent_id or sec.id, []).append(n)
    return kids


def count_below(key, kids):
    return sum(1 + count_below(n.id, kids) for n in kids.get(key, []))


def plain_summary(page, limit=140):
    """The page's Summary, else its first plain sentence(s) from the Markdown."""
    s = str(page.fm.get("summary") or "").strip()
    if not s:
        for block in re.split(r"\n\s*\n", page.body or ""):
            b = block.strip()
            if not b or b[0] in "#!|><-*[`" or re.match(r"^\d+\.", b) or b.startswith("{"):
                continue
            s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", b)
            s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
            s = re.sub(r"[*_`]", "", s)
            s = re.sub(r"\s+", " ", s).strip()
            if s and len(s.split()) >= 4 and not s.startswith("The pages of this part"):
                break
            s = ""
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "…"


def node_key(n, section_id):
    """Folder or file name of a top-level node inside its section (for categories)."""
    content = f"docs2/content/{section_id}/"
    rest = n.page.rel[len(content):] if n.page.rel.startswith(content) else n.page.rel
    return rest.split("/")[0].replace(".md", "")


def cards_html(nodes, kids, url_of, categories=None, section_id=None):
    """A plain list of links per category, wrapped for the docs script to turn into cards."""
    def item(n):
        url = url_of(n)
        title = htmllib.escape(str(n.page.fm.get("title") or n.id))
        summ = htmllib.escape(plain_summary(n.page))
        below = count_below(n.id, kids)
        meta = f' data-count="{below}"' if below else ""
        link = f'<a href="{htmllib.escape(url)}">{title}</a>' if url else title
        return f"<li{meta}>{link}{(' — ' + summ) if summ else ''}</li>"

    groups = []
    if categories and section_id:
        placed = set()
        for cat, keys in categories.items():
            members = [n for k in keys for n in nodes if node_key(n, section_id) == k]
            placed.update(m.id for m in members)
            if members:
                groups.append((cat, members))
        rest = [n for n in nodes if n.id not in placed]
        if rest:
            groups.append(("More", rest))
    else:
        groups = [(None, nodes)]
    out = ['<div class="ui-doc-cards">']
    for cat, members in groups:
        if cat:
            out.append(f"<h3>{htmllib.escape(cat)}</h3>")
        out.append("<ul>" + "".join(item(n) for n in members) + "</ul>")
    out.append("</div>")
    return "".join(out)


def add_cards(body, page, children, kids, url_of, categories=None, section_id=None, heading="In this chapter"):
    """Body HTML with the children's cards placed: instead of a placeholder, else at the end."""
    if not children or page is not None and page.fm.get("cards") is False:
        return body
    cards = cards_html(children, kids, url_of, categories, section_id)
    if PLACEHOLDER.search(body):
        return PLACEHOLDER.sub(lambda m: cards, body, count=1)
    if page is not None and len(re.sub(r"<[^>]+>", " ", body).split()) > 60 and heading:
        cards = f'<h2 id="in-this-chapter">{heading}</h2>' + cards
    return body + cards


PLACEHOLDER_ICON = "file_text"     # pages without an icon of their own still get one in the sidebar
REGION_ICONS = [                    # …and region pages get the icon of their region, as in the Interface group
    (r"context menus?$|context menu\b", "menu"),
    (r"\btool ?shelf\b|^tools$|toolbar", "tool_settings"),
    (r"\bsidebar\b|\bside bar\b", "sidebar"),
    (r"\btab$|\btab\b -|\btabs?\b", "new_window"),
    (r"\bfooter\b", "statusbar"),
    (r"\bheader\b|tools and options", "topbar"),
    (r"\bpanels?$", "toggle_node_options"),
    (r"\bmenu$|\bmenus$", "menu"),
    (r"channel", "sidebar"),
    (r"modifiers", "modifier"),
    (r"^mesh object", "mesh_data"), (r"^curves object", "hair"), (r"^curve object", "outliner_data_curve"),
    (r"^metaball object", "meta_data"), (r"^surface object", "surface_data"), (r"^point cloud object", "pointcloud_data"),
    (r"^text object", "font_data"), (r"^grease pencil object", "outliner_data_greasepencil"),
    (r"^armature object", "armature_data"), (r"^lattice object", "lattice_data"), (r"^empty", "empty_data"),
    (r"^speaker object", "speaker"), (r"^camera object", "camera_data"), (r"^light probe object", "lightprobe_sphere"),
    (r"^light object", "light"), (r"^force field object", "force_force"), (r"^volume object", "volume_data"),
    (r"bone constraint", "constraint_bone"), (r"^cycles$|^eevee$|^workbench$", "scene"),
    (r"^emitter$", "particles"), (r"^hair$", "hair"), (r"keymap|hotkeys", "key_command"),
    (r"^add$", "add"), (r"tracking", "tracker"), (r"timeline", "time"),
]


def region_icon(title):
    t = str(title or "").lower()
    for pat, ic in REGION_ICONS:
        if re.search(pat, t):
            return ic
    return ""


def words_of(page):
    return len(re.sub(r"[#>*_`|\[\]()!-]", " ", page.body or "").split())


def nav_tree(tree, kids, icons, section_slug, page_slug, commit=""):
    """The sidebar as data: sections → pages (any depth); short keys keep the file small.

    Per page:    t title · s slug · i icon (placeholder when none, then ph: 1) · c children
                 b button label (front matter `cta`) · m reading minutes of the page
    Top level:   d summary (for the cards and the Docs home)
    Per section: t, s, i, c as above · d summary · n pages · m minutes (whole section)
    """
    cfg = sections_cfg()
    ph = icon_file(PLACEHOLDER_ICON, icons)

    def node(n, top=False):
        d = {"t": str(n.page.fm.get("title") or n.id), "s": page_slug(n)}
        ic = icon_file(n.page.fm.get("icon"), icons) or icon_file(region_icon(d["t"]), icons)
        d["i"] = ic or ph
        if not ic:
            d["ph"] = 1
        if n.page.fm.get("cta"):
            d["b"] = str(n.page.fm["cta"])
        st = str(n.page.fm.get("status") or "draft")
        if st != "draft":
            d["st"] = st
        d["m"] = max(1, round(words_of(n.page) / 200))
        if top:
            summ = plain_summary(n.page, 120)
            if summ:
                d["d"] = summ
        sub = kids.get(n.id, [])
        if sub:
            d["c"] = [node(k) for k in sub]
        return d

    def count(c):
        return sum(1 + count(x.get("c", [])) for x in c)

    def total(c):
        return count(c), total_m(c)

    def total_m(c):
        return sum(x["m"] + total_m(x.get("c", [])) for x in c)

    secs = []
    for sec in tree:
        if not sec.nodes and not sec.index:
            continue
        ic = icon_file((sec.index.fm.get("icon") if sec.index else None) or cfg.get(sec.id, {}).get("icon"), icons)
        c = [node(n, True) for n in kids.get(sec.id, [])]
        n_pages, minutes = total(c)
        d = {"id": sec.id, "t": str(sec.title), "s": section_slug(sec), "i": ic or ph,
             "n": n_pages, "m": minutes, "c": c}
        summ = plain_summary(sec.index, 140) if sec.index else ""
        if summ:
            d["d"] = summ
        secs.append(d)
    return {"v": 2, "commit": commit, "sections": secs}


def home_html(page, icons, url_of_rel, img_url):
    """The Docs home as plain lists the docs script turns into the page (see home.md)."""
    fm = page.fm
    esc = htmllib.escape

    def li(kind, title, link="", **data):
        attrs = "".join(f' data-{k}="{esc(str(v))}"' for k, v in data.items() if v not in (None, ""))
        href = url_of_rel(link) if link else ""
        inner = f'<a href="{esc(href)}">{esc(str(title))}</a>' if href else esc(str(title))
        return f'<li data-k="{kind}"{attrs}>{inner}</li>'

    out = ['<div class="ui-doc-home"><ul>',
           li("eyebrow", fm.get("eyebrow", "")), li("headline", fm.get("headline", "")),
           li("lead", fm.get("summary", ""))]
    for p in fm.get("popular") or []:
        out.append(li("popular", p.get("title"), p.get("link"), i=icon_file(p.get("icon"), icons)))
    ex = fm.get("explore") or {}
    if ex:
        out.append(li("explore", ex.get("title", ""), ex.get("link"), img=img_url(ex.get("image", "")),
                      text=ex.get("text", "")))
    tz = fm.get("teaser") or {}
    if tz:
        out.append(li("teaser", tz.get("title", ""), tz.get("link"), eyebrow=tz.get("eyebrow"), text=tz.get("text"),
                      when=tz.get("when"), link2=url_of_rel(tz.get("link2")) if tz.get("link2") else "", label2=tz.get("label2")))
    if fm.get("workspace"):
        out.append(li("look", fm["workspace"].get("title", ""), fm["workspace"].get("all"), text=fm["workspace"].get("text")))
    for p in fm.get("paths") or []:
        out.append(li("path", p.get("title"), p.get("link"), area=p.get("area"), level=p.get("level"),
                      min=p.get("minutes"), i=icon_file(p.get("icon"), icons)))
    out.append("</ul></div>")
    return "".join(out)


def index_html(tree, url_of):
    """Information › Index: every page A to Z, grouped by first letter."""
    rows = []
    for sec in tree:
        for n in sec.nodes:
            if n.page.fm.get("generate") == "index":
                continue
            rows.append((str(n.page.fm.get("title") or n.id), str(sec.title), url_of(n)))
    rows.sort(key=lambda r: r[0].lower())
    out, letter = ['<div class="ui-doc-index">'], None
    for t, s, u in rows:
        first = t[:1].upper() if t[:1].isalpha() else "#"
        if first != letter:
            if letter is not None:
                out.append("</ul>")
            out.append(f"<h2>{htmllib.escape(first)}</h2><ul>")
            letter = first
        out.append(f'<li><a href="{htmllib.escape(u)}">{htmllib.escape(t)}</a> · <em>{htmllib.escape(s)}</em></li>')
    out.append("</ul></div>")
    return "".join(out)



# ---------------------------------------------------------------- workspace maps

WS_FILE = os.path.join(os.path.dirname(HERE), "workspaces.yml")
WS_MARK = re.compile(r"<!--\s*workspace-(map|explorer)\s*-->")


def load_workspaces():
    """docs2/workspaces.yml → (editors, {page rel under content/: entry}, [entries in order])."""
    if not os.path.exists(WS_FILE):
        return {}, {}, []
    data = yaml.safe_load(open(WS_FILE, encoding="utf-8")) or {}
    order = data.get("workspaces") or []
    return data.get("editors") or {}, {str(w["page"]): w for w in order}, order


def _area_items(entry, editors, icons, url_rel):
    esc = htmllib.escape
    out = []
    for a in entry.get("areas") or []:
        ed = editors.get(a.get("ed")) or {"name": a.get("ed", "Area"), "color": "#9a9a9a"}
        box = ",".join(f"{float(v):g}" for v in a.get("box") or [])
        href = url_rel(ed.get("page", "")) if ed.get("page") else ""
        name = esc(str(ed.get("name")))
        link = f'<a href="{esc(href)}">{name}</a>' if href else name
        text = esc(str(a.get("note") or ed.get("does") or ""))
        out.append(f'<li data-k="area" data-box="{box}" data-c="{esc(str(ed.get("color", "")))}" '
                   f'data-i="{esc(icon_file(ed.get("icon"), icons))}">{link}{(" — " + text) if text else ""}</li>')
    return out


def workspace_map(body, entry, editors, icons, url_rel, img_url, name="", go=""):
    """A workspace page: the hover map's areas as a list right after the screenshot (the docs
    script lays them over it). Placed at <!-- workspace-map --> when the page has one."""
    if not entry or not entry.get("areas"):
        return WS_MARK.sub("", body)
    src = img_url(entry["image"]) if entry.get("image") else ""
    extra = (f' data-n="{htmllib.escape(name)}"' if name else "") + (f' data-href="{htmllib.escape(go)}"' if go else "")
    shot = f'<li data-k="shot" data-img="{htmllib.escape(src)}" data-v="{htmllib.escape(str(entry.get("captured", "")))}"{extra}>Screenshot</li>'
    block = f'<div class="ui-ws-map"><ul>{shot}{"".join(_area_items(entry, editors, icons, url_rel))}</ul></div>'
    if WS_MARK.search(body):
        return WS_MARK.sub(lambda m: block, body, count=1)
    m = re.search(r'<figure[^>]*>\s*<img src="' + re.escape(src) + r'"[^>]*>.*?</figure>', body, re.S) if src else None
    if m:
        return body[:m.end()] + block + body[m.end():]
    return block + body


def workspace_explorer(body, order, editors, icons, url_rel, img_url, title_of):
    """The Workspaces overview: every workspace with its screenshot and areas, as one flat list
    (a `ws` row, then its `area` rows) the docs script turns into the explorer."""
    esc = htmllib.escape
    rows = []
    for w in order:
        href = url_rel(w["page"])
        if not href:
            continue
        title, summ, icon = title_of(w["page"])
        src = img_url(w["image"]) if w.get("image") else ""
        rows.append(f'<li data-k="ws" data-img="{esc(src)}" data-i="{esc(icon_file(icon, icons))}" data-v="{esc(str(w.get("captured", "")))}" data-sum="{esc(summ)}">'
                    f'<a href="{esc(href)}">{esc(title)}</a></li>')
        rows += _area_items(w, editors, icons, url_rel)
    if not rows:
        return WS_MARK.sub("", body)
    block = f'<div class="ui-ws-explorer"><ul>{"".join(rows)}</ul></div>'
    if WS_MARK.search(body):
        return WS_MARK.sub(lambda m: block, body, count=1)
    m = re.search(r"</p>", body)
    return body[:m.end()] + block + body[m.end():] if m else block + body
