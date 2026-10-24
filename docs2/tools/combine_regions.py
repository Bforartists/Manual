#!/usr/bin/env python3
"""Combine a region's small pages into the region page itself ("less is more").

    python3 docs2/tools/combine_regions.py docs2/content/editors/image-editor/header [more region folders]

The region folder's index.md (Header, Sidebar, Tool Shelf …) keeps its id and address and gets
one H1 per old page (View Menu, Select Menu, Image Tab …), so they show as the panels on the
right. Sub-folders (such as add-menu/) stay as pages below it. A region bigger than LIMIT_KB
is left alone. Old pages go to `replaces:` and docs2/reports/redirects.csv.
"""
import csv
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import slugify  # noqa: E402

LIMIT_KB = 150
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)


def parse(path):
    t = open(path, encoding="utf-8").read()
    m = FM.match(t)
    return m.group(1), t[m.end():]


def get(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def demote(body):
    return re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + 1) + " ", body, flags=re.M)


STOP = {"header", "sidebar", "tool shelf", "toolbar", "topbar", "topbar menus", "footer"}
SMALL = {"and", "or", "of", "the", "in", "to", "a", "by"}


def short(title, editor_title=""):
    """'Video Sequence Editor - Sidebar - Preview - Tool tab' → 'Preview › Tool Tab'."""
    parts = [p.strip() for p in title.split(" - ") if p.strip()]
    while len(parts) > 1 and (parts[0].lower() in STOP or parts[0].lower() == editor_title.lower()
                              or parts[0].lower().endswith("editor") or parts[0].lower().endswith("viewport")):
        parts.pop(0)
    words = " › ".join(parts).split(" ")
    return " ".join(w if (w.lower() in SMALL and i) or not w[:1].islower() else w[:1].upper() + w[1:]
                    for i, w in enumerate(words))


def nav_rank():
    rank, i = {}, 0
    for line in open("docs2/nav.yml", encoding="utf-8"):
        m = re.search(r'file: "content/([^"]+)"', line)
        if m:
            rank["docs2/content/" + m.group(1)] = i
            i += 1
    return rank


def combine(folder):
    idx = os.path.join(folder, "index.md")
    kids = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".md") and f != "index.md"]
    if not kids:
        return print(f"{folder}: nothing to combine")
    size = sum(os.path.getsize(p) for p in kids + [idx])
    if size > LIMIT_KB * 1024:
        return print(f"{folder}: {size // 1024} KB, too big, left alone")
    rank = nav_rank()
    kids.sort(key=lambda p: rank.get(p, 10 ** 6))
    fm, body = parse(idx)
    pid = get(fm, "id")
    ed_idx = os.path.join(os.path.dirname(folder), "index.md")
    ed_title = get(parse(ed_idx)[0], "title") if os.path.exists(ed_idx) else ""
    out, replaces, redirects = [body.strip()], [], []
    for p in kids:
        kfm, kbody = parse(p)
        out.append(f"# {short(get(kfm, 'title'), ed_title)}\n\n" + demote(kbody.strip()))
        oid = get(kfm, "id")
        if oid:
            replaces.append(oid)
            redirects.append((oid, "/docs/" + slugify(oid.replace(".", "-"), limit=120), pid,
                              "/docs/" + slugify(pid.replace(".", "-"), limit=120)))
        subprocess.run(["git", "rm", "-q", p], check=True)
    if replaces:
        if re.search(r"^replaces:", fm, re.M):
            fm += "\n" + "\n".join(f"  - {r}" for r in replaces)
        else:
            fm += "\nreplaces:\n" + "\n".join(f"  - {r}" for r in replaces)
    open(idx, "w", encoding="utf-8").write(f"---\n{fm}\n---\n" + "\n\n".join(x for x in out if x) + "\n")
    with open("docs2/reports/redirects.csv", "a", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(redirects)
    print(f"{folder}: {len(kids)} pages combined ({size // 1024} KB)")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        combine(f.rstrip("/"))
