#!/usr/bin/env python3
"""Write docs2/nav.yml (the sidebar order) for the converted manual.

    python3 docs2/tools/make_nav.py [repo]

  - Sections come in the order of tools/sections.yml (the chapter list).
  - Pages inside a section follow the original chapter numbers from tools/page_map.json
    (5, 5.1.1, 5.1.2 … 7, 7.1.1 …), a chapter before its sub-chapters, so the website
    sidebar reads like the old manual's chapter list.
  - Sections written by hand in Tier 1 (getting-started, interface) and test sections keep
    the order they already have in nav.yml.
  - Icons already set in nav.yml are kept.
"""
import json
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
KEEP = {"getting-started", "interface", "workspaces", "assets"}   # hand-ordered sections


def q(s):
    return json.dumps(s, ensure_ascii=False)


def num_key(number):
    parts = [int(x) for x in re.findall(r"\d+", str(number or ""))]
    return parts or [10 ** 6]


def main(repo):
    docs = os.path.join(repo, "docs2")
    nav_path = os.path.join(docs, "nav.yml")
    old = yaml.safe_load(open(nav_path, encoding="utf-8")) or []
    old_by_sec = {s["section"]: s for s in old}
    icons = {p["id"]: p.get("icon") for s in old for p in (s.get("pages") or []) if p.get("icon")}
    sections = yaml.safe_load(open(os.path.join(HERE, "sections.yml"), encoding="utf-8"))["sections"]
    pm = json.load(open(os.path.join(HERE, "page_map.json"), encoding="utf-8"))["pages"]
    pj = json.load(open(os.path.join(HERE, "pages.json"), encoding="utf-8"))["pages"]
    number = {p["id"]: p.get("number") for p in pm}
    seq = {p["id"]: i for i, p in enumerate(pj)}

    out = ["# Sidebar order and icons. Written by tools/make_nav.py: pages follow the original chapter",
           "# numbers (getting-started and interface keep their hand-made order); icons set here are kept.", ""]

    def emit(sid, title, slug, pages):
        out.extend([f"- section: {sid}", f"  title: {q(title)}", f"  slug: {slug}"])
        if not pages:
            out.append("  pages: []")
        else:
            out.append("  pages:")
            for p in pages:
                icon = icons.get(p["id"]) or p.get("icon")
                out.append(f"    - {{ id: {q(p['id'])}, title: {q(p['title'])}, file: {q(p['file'])}, "
                           f"icon: {q(icon) if icon else 'null'} }}")
        out.append("")

    done = set()
    for sc in sections:
        sid = sc["id"]
        done.add(sid)
        prev = old_by_sec.get(sid, {})
        slug = prev.get("slug") or sid
        title = prev.get("title") or sc.get("title", sid)
        if sid in KEEP and prev:
            emit(sid, title, slug, prev.get("pages") or [])
            continue
        pages = [p for p in pj if p.get("section") == sid
                 and os.path.exists(os.path.join(docs, p["file"])) and p["file"].startswith("content/")]
        pages.sort(key=lambda p: (num_key(number.get(p["id"])), not p["file"].endswith("/index.md"), seq[p["id"]]))
        if pages:
            emit(sid, title, slug, [{"id": p["id"], "title": p["title"], "file": p["file"]} for p in pages])
    for s in old:                                   # test sections and anything else stay as they were
        if s["section"] not in done:
            emit(s["section"], s.get("title", s["section"]), s.get("slug", s["section"]), s.get("pages") or [])
    open(nav_path, "w", encoding="utf-8").write("\n".join(out))
    print(f"wrote {nav_path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
