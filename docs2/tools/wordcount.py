#!/usr/bin/env python3
"""Faithful-clone check (decision D13): no source words may be lost.

Groups pages that share sources (a chapter can be split over several pages, and a
page can combine chapters), then compares, per group:

    words in the sources  - words removed on purpose (generated contents lists, file title lines)
    words in the pages + the snippets they use

Usage: wordcount.py OUT_DIR WORK_DIR [--markdown]
Exits 1 when any group lost words, so it can fail a pull request.
"""
import json, os, re, sys, collections

WORD = re.compile(r"[A-Za-z0-9][\w'’-]*")
ADDED = [  # lines the converter adds itself; not source words
    re.compile(r"^> \*\*Note:\*\* The earlier text of this page from the \.odt manual.*$", re.M),
    re.compile(r"^> \*\*Note:\*\* This page has no content yet.*$", re.M),
    re.compile(r"^\*Shared section: \[[^\]]*\]\([^)]*\)\*$", re.M),
    re.compile(r"^## From the \.odt manual \([^)]*\)$", re.M),
]


def page_words(md):
    md = re.sub(r"^---.*?---\n", "", md, flags=re.S)
    for rx in ADDED:
        md = rx.sub("", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)          # images (alt text is generated)
    md = re.sub(r"\]\(([^)]*)\)", "]", md)                 # link targets
    md = re.sub(r"<(https?://[^>]+)>", r"\1", md)           # autolinks keep their text
    md = re.sub(r"[|*_#>`\[\]]", " ", md)
    return len(WORD.findall(md))


def main(out_dir, work_dir, as_md=False):
    rep = json.load(open(os.path.join(work_dir, "convert-report.json")))
    src_words, dropped = rep["source_words"], rep.get("dropped_words", {})
    items = rep["pages"] + rep["snippets"]
    # union-find over pages sharing a source
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            x = parent[x]
        return x
    for it in items:
        srcs = [s for s in it["sources"] if s]
        for s in srcs[1:]:
            parent[find(s)] = find(srcs[0])
        if srcs: find(srcs[0])
    groups = collections.defaultdict(lambda: {"sources": set(), "files": []})
    for it in items:
        srcs = [s for s in it["sources"] if s]
        key = find(srcs[0]) if srcs else "(no source) " + it["file"]
        groups[key]["sources"].update(srcs)
        groups[key]["files"].append(it["file"])
    rows, failed = [], 0
    for g in groups.values():
        src = sum(src_words.get(s, 0) for s in g["sources"])
        drop = sum(dropped.get(s, 0) for s in g["sources"])
        out = sum(page_words(open(os.path.join(out_dir, f)).read()) for f in g["files"])
        need = src - drop
        ok = out >= need * 0.98 if need else True       # 2% slack for pandoc word-splitting differences
        failed += not ok
        name = ", ".join(sorted(s.replace("web:", "website: ") for s in g["sources"])) or g["files"][0]
        rows.append((ok, name, src, drop, out, len(g["files"])))
    rows.sort(key=lambda r: (r[0], r[1]))
    if as_md:
        print("| | Sources | Source words | Removed on purpose | Words in pages + snippets | Pages |")
        print("|---|---|---|---|---|---|")
        for ok, name, src, drop, out, n in rows:
            print(f"| {'✅' if ok else '❌'} | {name[:90]} | {src:,} | {drop:,} | {out:,} | {n} |")
    else:
        for ok, name, src, drop, out, n in rows:
            print(f"{'OK ' if ok else 'LOST'}  src {src:6} - dropped {drop:4} -> out {out:6}  ({n} files)  {name[:100]}")
    print(f"\n{len(rows) - failed} of {len(rows)} groups keep every word" if not as_md else "")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], "--markdown" in sys.argv))
