#!/usr/bin/env python3
"""Combine the many "Add Menu - X - Y" pages of a node editor into one page per category.

    python3 docs2/tools/combine_add_menu.py geometry-node-editor [compositor shader-editor]

editors/<editor>/header/add-menu.md becomes the hub header/add-menu/index.md (its intro, then
one card per category). Each category ("Input", "Curve", "Utilities" …) becomes one page,
header/add-menu/<category>.md, with one H1 per old sub-page ("Constant", "Gizmo" …), so the
sub-pages are the panels on the right and the sidebar shows short names. Old pages are
listed in `replaces:` and in docs2/reports/redirects.csv.
"""
import csv
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import slugify  # noqa: E402

ROOT = "docs2/content/editors"
FM = re.compile(r"^---\n(.*?)\n---\n?", re.S)
RENAME = {"Geometry Nodegroups": "Node Groups"}


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = FM.match(text)
    return m.group(1), text[m.end():]


def get(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else ""


def demote(body, by=1):
    return re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + by) + " ", body, flags=re.M)


def q(s):
    return '"' + str(s).replace('"', '\\"') + '"'


def nav_order():
    order, i = {}, 0
    for line in open("docs2/nav.yml", encoding="utf-8"):
        m = re.search(r'file: "content/([^"]+)"', line)
        if m:
            order[m.group(1)] = i
            i += 1
    return order


def combine(editor):
    hdr = os.path.join(ROOT, editor, "header")
    files = sorted(f for f in os.listdir(hdr) if f.startswith("add-menu-") and f.endswith(".md"))
    if not files:
        return print(f"{editor}: nothing to combine")
    rank = nav_order()
    files.sort(key=lambda f: rank.get(f"editors/{editor}/header/{f}", 10 ** 6))
    hub_fm, hub_body = parse(os.path.join(hdr, "add-menu.md"))
    hub_id, ed_path = get(hub_fm, "id"), None
    path_m = re.search(r"^path:\n((?:  - .+\n?)+)", hub_fm, re.M)
    base_path = [x.strip()[2:].strip().strip('"') for x in path_m.group(1).splitlines()] if path_m else []
    groups, order = {}, []
    for f in files:
        fm, body = parse(os.path.join(hdr, f))
        parts = [p.strip() for p in get(fm, "title").split(" - ")][1:]       # drop "Add Menu"
        cat = RENAME.get(parts[0], parts[0]) if parts else f[9:-3]
        name = " › ".join(parts[1:]) or None
        if cat not in groups:
            groups[cat] = []
            order.append(cat)
        groups[cat].append((f, get(fm, "id"), name, body, re.findall(r"^\s+-\s+(.+\.odt)\s*$", fm, re.M)))
    out_dir = os.path.join(hdr, "add-menu")
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run(["git", "mv", os.path.join(hdr, "add-menu.md"), os.path.join(out_dir, "index.md")], check=True)
    hub_fm = re.sub(r"^title:.*$", 'title: "Add Menu"', hub_fm, flags=re.M)
    if not re.search(r"^summary:", hub_fm, re.M):
        hub_fm += '\nsummary: "Every node you can add, by category: open a category for its nodes."'
    if not re.search(r"^icon:", hub_fm, re.M):
        hub_fm += "\nicon: add"
    open(os.path.join(out_dir, "index.md"), "w", encoding="utf-8").write(
        f"---\n{hub_fm}\n---\n{hub_body.strip()}\n\nPick a category to see its nodes. Each category page lists its sub-menus in the panels on the right.\n")
    redirects = []
    for i, cat in enumerate(order):
        items = groups[cat]
        items.sort(key=lambda it: it[2] is not None)             # the category's own page first
        cid = f"{hub_id}.{slugify(cat)}"
        body, replaces, sources = [], [], []
        for f, oid, name, b, src in items:
            if name is None:
                body.append(b.strip() + "\n")
            else:
                body.append(f"# {name}\n\n" + demote(b.strip(), 1) + "\n")
            if oid:
                replaces.append(oid)
                redirects.append((oid, "/docs/" + slugify(oid.replace(".", "-"), limit=120), cid,
                                  "/docs/" + slugify(cid.replace(".", "-"), limit=120)))
            sources += [s for s in src if s not in sources]
            subprocess.run(["git", "rm", "-q", os.path.join(hdr, f)], check=True)
        subs = [it[2] for it in items if it[2]]
        summ = f"{cat} nodes" + (": " + ", ".join(subs[:6]) + ("…" if len(subs) > 6 else "") + "." if subs else ".")
        lines = ["---", f"id: {cid}", f"title: {q(cat)}", "section: editors", "path:"]
        lines += [f"  - {q(p)}" for p in base_path + [cat]]
        lines += ['version: "5.1"', "status: draft", "icon: node", f"summary: {q(summ)}", f"order: {(i + 1) * 10}", 'cta: "Nodes"']
        if sources:
            lines += ["source:"] + [f"  - {q(s)}" for s in sources]
        lines += ["replaces:"] + [f"  - {r}" for r in replaces] + ["---"]
        open(os.path.join(out_dir, slugify(cat) + ".md"), "w", encoding="utf-8").write("\n".join(lines) + "\n" + "\n".join(body).strip() + "\n")
    with open("docs2/reports/redirects.csv", "a", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(redirects)
    print(f"{editor}: {len(files)} add-menu pages → {len(order)} categories: {', '.join(order)}")


if __name__ == "__main__":
    for e in sys.argv[1:]:
        combine(e)
