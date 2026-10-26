#!/usr/bin/env python3
"""Repeated interface explanations → one short link to the Interface chapter (Queue 3, Phase 3).

    python3 docs2/tools/backlinks.py [--dry]

Some explanations were copied into many editor pages (the Quick Favorites menu, the curve
widget, slider snapping, floating windows). Each topic gets one home in the Interface group;
everywhere else the copied paragraphs are replaced by one line that links there. A section that
is mostly the copied text is replaced as a whole (its screenshots too); otherwise only the copied
paragraphs go.
"""
import os
import re
import sys

C = "docs2/content"
TOPICS = [
    {"name": "Quick Favorites", "home": "interface/floating-menus.md", "anchor": "quick-favorites",
     "line": "The **Quick Favorites** menu (Q) holds the tools and menus you add to it yourself.",
     "sig": ["The quick menu, or in long Quick Favorites", "When the menu is empty, then you will see", "Let's add the open command",
             "Do the same with Save As", "As a rule of thumb, when the right click menu", "Note that you can also add operators from the tool shelf",
             "It is also possible to add a menu to the Quick menu", "You might notice that the add menu adds at the top",
             "Besides that, operators and menus gets added", "Removing is as simple as adding", "The quick favorites. menu exists",
             "The content of the quick favorites", "It is located in the header. But it can be called by hotkey Q",
             "When you right click at a menu or a button, then a right click menu will open"]},
    {"name": "Curve Widget", "home": "interface/properties.md", "anchor": "curve-widget",
     "line": "This setting uses the **curve widget**: click to add points, drag to move them.",
     "sig": ["You can select curve points.", "Selected points can be moved around.", "You can add new curve points by simply left clicking"]},
    {"name": "Snapping", "home": "interface/properties.md", "anchor": "snapping",
     "line": "Hold **Ctrl** while dragging a slider to snap it.",
     "sig": ["When it's a default value between 0 and 1 then it usually snaps", "Snapping also works at sliders."]},
    {"name": "Floating editor windows", "home": "interface/windows.md", "anchor": "floating-editor-windows",
     "line": "**Duplicate Area into New Window** opens this editor in a floating window.",
     "sig": ["A separated window cannot be merged into the main window", "Duplicate Area into New Window makes the selected editor window floating"]},
]
HEAD = re.compile(r"^(#{1,6}) (.+)$", re.M)


def paras(text):
    return [p for p in re.split(r"\n\s*\n", text)]


def is_sig(p, topic):
    t = re.sub(r"\s+", " ", p).strip()
    return any(t.startswith(s) for s in topic["sig"])


def sections(body):
    """[(start, end, level)] for every heading section (to the next heading of the same or higher level)."""
    hs = [(m.start(), len(m.group(1))) for m in HEAD.finditer(body)]
    out = []
    for i, (s, lv) in enumerate(hs):
        e = len(body)
        for s2, lv2 in hs[i + 1:]:
            if lv2 <= lv:
                e = s2
                break
        out.append((s, e, lv))
    return out


def link(rel_from, topic):
    href = os.path.relpath(os.path.join(C, topic["home"]), os.path.dirname(rel_from)).replace("\\", "/")
    return f"> {topic['line']} See **[{topic['name']}]({href}#{topic['anchor']})** in the Interface chapter."


def fix_file(path, dry):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    head, body = (text[:m.end()], text[m.end():]) if m else ("", text)
    changed = []
    for topic in TOPICS:
        if path.endswith(topic["home"]):
            continue
        if not any(is_sig(p, topic) for p in paras(body)):
            continue
        # innermost section whose text is mostly this topic → replace its body
        best = None
        for s, e, lv in sections(body):
            sec = body[s:e]
            words = len(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", sec).split())
            sigw = sum(len(p.split()) for p in paras(sec) if is_sig(p, topic))
            if sigw and words and sigw / words >= 0.5 and (best is None or e - s < best[1] - best[0]):
                best = (s, e)
        if best:
            s, e = best
            first_line = body[s:].split("\n", 1)[0]
            body = body[:s] + first_line + "\n\n" + link(path, topic) + "\n\n" + body[e:]
        else:
            out, done = [], False
            for p in paras(body):
                if is_sig(p, topic):
                    if not done:
                        out.append(link(path, topic))
                        done = True
                    continue
                out.append(p)
            body = "\n\n".join(out)
        changed.append(topic["name"])
    if changed and not dry:
        open(path, "w", encoding="utf-8").write(head + re.sub(r"\n{3,}", "\n\n", body))
    return changed


def ensure_homes(dry):
    """Give each topic its section in the Interface page, copied from the first place it appears."""
    for topic in TOPICS:
        home = os.path.join(C, topic["home"])
        text = open(home, encoding="utf-8").read()
        if re.search(rf"^#+ {re.escape(topic['name'])}\s*$", text, re.M):
            continue
        src = None
        for root, _, files in os.walk(os.path.join(C, "editors")):
            for f in sorted(files):
                p = os.path.join(root, f)
                body = open(p, encoding="utf-8").read()
                for s, e, lv in sections(body):
                    sec = body[s:e]
                    if sum(1 for x in paras(sec) if is_sig(x, topic)) >= (len(topic["sig"]) if len(topic["sig"]) <= 3 else len(topic["sig"]) // 2):
                        if src is None or len(sec) < len(src):
                            src = sec
            if src:
                break
        if not src:
            print(f"no source for {topic['name']}")
            continue
        body = src.split("\n", 1)[1] if "\n" in src else ""
        lv = int(re.match(r"^(#+)", src).group(1).__len__())
        body = re.sub(r"^(#{1,6}) ", lambda m: "#" * max(3, min(6, len(m.group(1)) - lv + 3)) + " ", body, flags=re.M)
        add = f"\n\n## {topic['name']}\n\n" + body.strip() + "\n"
        if not dry:
            open(home, "a", encoding="utf-8").write(add)
        print(f"{topic['home']}: added ## {topic['name']}")


def main(argv):
    dry = "--dry" in argv
    ensure_homes(dry)
    n = 0
    for root, _, files in os.walk(os.path.join(C, "editors")):
        for f in sorted(files):
            if f.endswith(".md"):
                p = os.path.join(root, f)
                ch = fix_file(p, dry)
                if ch:
                    n += 1
                    print(f"{p}: {', '.join(ch)}")
    print(f"{n} pages now link to the Interface chapter")


if __name__ == "__main__":
    main(sys.argv[1:])
