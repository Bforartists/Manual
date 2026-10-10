#!/usr/bin/env python3
"""Page map: where every .odt file of the manual lands in the new docs.

    python3 docs2/tools/map_pages.py [repo root]                       # write the map and its report
    python3 docs2/tools/map_pages.py . --apply --section editors --chapter 7   # move one chapter into pages.json

Reads  docs2/reports/inventory.json (inventory.py), docs2/tools/sections.yml, docs2/tools/pages.json,
       docs2/tools/legacy_pages.json
Writes docs2/tools/page_map.json   every planned page, in pages.json format
       docs2/reports/page-map.md   the map as a table, with what is done and what is next

Rules (faithful clone, decision D13: structure only, no rewording)
  📚 chapter  "7 Editors - 3D Viewport"          → editors/3d-viewport/index.md   (a page if it has no sub-chapters)
  📄 sub      "7.1 Editors - 3D Viewport - Header" → editors/3d-viewport/header/index.md
  ↳ leaf     "7.1.3 … - Header - View Menu"      → editors/3d-viewport/header/view-menu.md
  🫥 a sub-chapter with no file of its own (7.0, 12.1) gets a short group page with its title only
  🧩 files under fold_below_words fold into the page above them
  ✅ files already converted (in pages.json) are kept as they are
"""
import difflib
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import DOCS_ROOT, slugify  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def segments(title):
    return [s.strip() for s in re.split(r"\s+-\s+|\s+–\s+|-\s(?=[A-Z])", title) if s.strip()]


def strip_prefix(segs, prefix):
    """Drop the leading segments shared with the parent's title (case-insensitive, Editor/Editors tolerant)."""
    norm = lambda s: re.sub(r"\b(editor|editors|nodes?)\b", "", s.lower()).strip()  # noqa: E731
    i = 0
    while i < len(segs) and i < len(prefix) and norm(segs[i]) == norm(prefix[i]):
        i += 1
    return segs[i:] or segs[-1:]


def number_key(num):
    return tuple(int(x) for x in num.split("."))


def build(repo):
    inv = json.load(open(os.path.join(repo, DOCS_ROOT, "reports", "inventory.json"), encoding="utf-8"))["files"]
    cfg = yaml.safe_load(open(os.path.join(HERE, "sections.yml"), encoding="utf-8"))
    pages_cfg = json.load(open(os.path.join(HERE, "pages.json"), encoding="utf-8"))
    legacy = json.load(open(os.path.join(HERE, "legacy_pages.json"), encoding="utf-8"))["pages"]
    fold_below = cfg.get("fold_below_words", 80)
    split_above = cfg.get("split_above_words", 8000)

    done, existing = {}, {}                                # src -> page id already converted
    for pg in pages_cfg["pages"] + pages_cfg.get("snippets", []):
        existing[pg["id"]] = pg
        for part in pg["parts"]:
            if part.get("src"):
                done.setdefault(part["src"], pg["id"])
    by_num = {r["number"]: r for r in inv}
    chapter_of = {}
    for sec in cfg["sections"]:
        for c in sec["chapters"]:
            chapter_of[c] = sec

    pages, folded = [], []
    for sec in cfg["sections"]:
        for c in sec["chapters"]:
            top = by_num.get(str(c))
            if not top:
                continue
            csegs = segments(top["title"])
            alias = [[a] for a in (sec.get("aliases") or {}).get(c, [])]
            folder = str((sec.get("folders") or {}).get(c) or slugify(" ".join(strip_prefix(csegs, ["Editors"]))))
            kids = sorted([r for r in inv if r["chapter"] == c and r["depth"] > 1], key=lambda r: number_key(r["number"]))
            subs = sorted({".".join(r["number"].split(".")[:2]) for r in kids}, key=number_key)
            base = f"{sec['id']}/{folder}"
            ctitle = " ".join(strip_prefix(csegs, ["Editors"])) if sec["id"] == "editors" else top["title"]
            cpath = [sec["title"], ctitle]
            pages.append(page(sec, base + ("/index.md" if kids else ".md"), ctitle, cpath, [top], done, "chapter"))
            for s in subs:
                own = by_num.get(s)
                leaves = [r for r in kids if r["depth"] == 3 and r["number"].startswith(s + ".")]
                if not own and leaves and all(r["src"] in done for r in leaves):
                    srcs_done = True
                else:
                    srcs_done = False
                if own:
                    ssegs = strip_any(segments(own["title"]), csegs, alias)
                    stitle = " ".join(ssegs) if len(ssegs) == 1 else " - ".join(ssegs)
                else:
                    stitle = str((sec.get("groups") or {}).get(s) or common_title(leaves, csegs) or f"Part {s}")
                sslug = slugify(stitle)
                spath = cpath + [stitle]
                sfile = f"{base}/{sslug}" + ("/index.md" if leaves else ".md")
                srcs = [own] if own else []
                if not srcs_done:
                    pages.append(page(sec, sfile, stitle, spath, srcs, done, "sub" if own else "group", number=s))
                parent = pages[-1]
                for leaf in leaves:
                    lsegs = strip_prefix(strip_any(segments(leaf["title"]), csegs, alias), [stitle])
                    ltitle = " - ".join(lsegs)
                    if leaf["words"] < fold_below and leaf["tables"] == 0 and leaf["src"] not in done and parent["status"] == "planned":
                        parent["parts"].append({"src": leaf["src"], "select": "*", "shift": 1})
                        parent["words"] += leaf["words"]
                        parent["images_count"] += leaf["images"]
                        folded.append((leaf["src"], parent["id"]))
                        continue
                    pages.append(page(sec, f"{base}/{sslug}/{slugify(ltitle)}.md", ltitle, spath + [ltitle],
                                      [leaf], done, "leaf"))
    # pages already converted: show them as they are, once
    seen, merged = set(), []
    for p in pages:
        if p["status"] == "done":
            ex = existing[p["id"]]
            if p["id"] in seen:
                continue
            seen.add(p["id"])
            p.update({"file": ex["file"], "title": ex["title"], "path": ex.get("path", p["path"]), "images": ex.get("images", p["images"])})
        merged.append(p)
    pages = merged
    # legacy addresses: best title match within the section's legacy folder
    for p in pages:
        sec = next(s for s in cfg["sections"] if s["id"] == p["section"])
        pool = [lp for lp in legacy if lp["path"].startswith(sec["legacy"] + "/")]
        names = {lp["title"].lower(): lp["path"] for lp in pool}
        hit = difflib.get_close_matches(p["title"].lower(), list(names), n=1, cutoff=0.8)
        if hit and p["kind"] in ("chapter", "sub"):
            p["legacy_path"] = names[hit[0]]
        p["split_candidate"] = p["words"] > split_above
    used = {p.get("legacy_path") for p in pages}
    unmatched = [lp for lp in legacy if lp["path"] not in used and lp["path"].count("/") > 2]
    return cfg, pages, folded, unmatched


def strip_any(segs, csegs, aliases):
    best = strip_prefix(segs, csegs)
    for a in aliases:
        alt = strip_prefix(segs, a)
        if len(alt) < len(best):
            best = alt
    return best


def common_title(leaves, csegs):
    firsts = [strip_prefix(segments(r["title"]), csegs)[0] for r in leaves]
    if firsts:
        top = max(set(firsts), key=firsts.count)
        if firsts.count(top) >= 0.6 * len(firsts):
            return top
    return None


def page(sec, rel, title, path, srcs, done, kind, number=None):
    rel_id = rel[:-len("/index.md")] if rel.endswith("/index.md") else rel[:-3]
    pid = rel_id.replace("/", ".")
    status = "done" if srcs and all(s["src"] in done for s in srcs) else "planned"
    p = {"id": done.get(srcs[0]["src"], pid) if status == "done" else pid,
         "file": f"content/{rel}", "title": title, "section": sec["id"], "path": path,
         "images": rel_id, "kind": kind, "status": status,
         "number": srcs[0]["number"] if srcs else number,
         "parts": [{"src": s["src"], "select": "*"} for s in srcs] or
                  [{"note": f"The pages of this part are listed in the sidebar under *{title}*."}],
         "words": sum(s["words"] for s in srcs), "images_count": sum(s["images"] for s in srcs)}
    return p


def report(cfg, pages, folded, unmatched):
    md = ["# 🗺️ Page map", "",
          "Where every `.odt` file lands in Docs 2.0. Generated by `docs2/tools/map_pages.py` from `sections.yml`.", ""]
    tot = len(pages)
    done = sum(1 for p in pages if p["status"] == "done")
    md += [f"**{tot} pages planned · {done} already converted · {len(folded)} small files folded into their parent · "
           f"{sum(1 for p in pages if p['split_candidate'])} very long pages to check**", "",
           "| # | Section | Chapters | Pages | Words | Images | Converted |", "|---|---|---|---|---|---|---|"]
    for i, sec in enumerate(cfg["sections"], 1):
        ps = [p for p in pages if p["section"] == sec["id"]]
        ch = sec["chapters"]
        md.append(f"| {i} | **{sec['title']}** | {ch[0]}–{ch[-1]} | {len(ps)} | {sum(p['words'] for p in ps):,} | "
                  f"{sum(p['images_count'] for p in ps):,} | {sum(1 for p in ps if p['status'] == 'done')} of {len(ps)} |")
    icon = {"chapter": "📚", "sub": "📄", "group": "🫥", "leaf": "↳"}
    for sec in cfg["sections"]:
        md += ["", f"## {sec['title']}", "", "| | # | Page | File | Words | Legacy address | |", "|---|---|---|---|---|---|---|"]
        for p in [p for p in pages if p["section"] == sec["id"]]:
            flag = ("✅" if p["status"] == "done" else "⏳") + (" ✂️" if p["split_candidate"] else "")
            md.append(f"| {icon[p['kind']]} | {p['number'] or ''} | {p['title']} | `{p['file'].replace('content/', '', 1)}` | {p['words']:,} | "
                      f"{p.get('legacy_path', '')} | {flag} |")
    if unmatched:
        md += ["", "## 🌐 Website pages with no chapter", "",
               "These pages exist on the current website but match no `.odt` chapter. They keep their text from the website "
               "(like Quick Start) or get a redirect at go-live.", "", "| Address | Title |", "|---|---|"]
        md += [f"| {u['path']} | {u['title']} |" for u in unmatched]
    md += ["", "✅ converted · ⏳ planned · ✂️ very long, check the Webflow size limit · 🫥 group page with a title only"]
    return "\n".join(md) + "\n"


def apply(repo, pages, section, chapter):
    path = os.path.join(HERE, "pages.json")
    cfg = json.load(open(path, encoding="utf-8"))
    have = {p["id"] for p in cfg["pages"]}
    add = [p for p in pages if p["section"] == section and p["status"] == "planned"
           and (chapter is None or str(p["number"] or "").split(".")[0] == str(chapter)) and p["id"] not in have]
    keep = ("id", "file", "title", "section", "path", "images", "parts")
    cfg["pages"] += [{k: p[k] for k in keep} for p in add]
    json.dump(cfg, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(add)} page(s) added to pages.json for {section}" + (f" chapter {chapter}" if chapter else ""))


def main(argv):
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] not in ("--section", "--chapter"))]
    repo = args[0] if args else "."
    cfg, pages, folded, unmatched = build(repo)
    json.dump({"pages": pages, "folded": folded}, open(os.path.join(HERE, "page_map.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    open(os.path.join(repo, DOCS_ROOT, "reports", "page-map.md"), "w", encoding="utf-8").write(report(cfg, pages, folded, unmatched))
    print(f"{len(pages)} pages · {sum(1 for p in pages if p['status'] == 'done')} done · {len(folded)} folded · "
          f"{len(unmatched)} website pages without a chapter")
    if "--apply" in argv:
        sec = argv[argv.index("--section") + 1]
        ch = argv[argv.index("--chapter") + 1] if "--chapter" in argv else None
        apply(repo, pages, sec, ch)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
