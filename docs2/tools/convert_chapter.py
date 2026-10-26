#!/usr/bin/env python3
"""Convert one chapter of the .odt manual into docs2/, the Tier 2 way.

    python3 docs2/tools/convert_chapter.py <manual dir> <section> <chapter>
    e.g.  python3 docs2/tools/convert_chapter.py ../odt-manual workspaces 4

  1. 🗺️ adds the chapter's planned pages from the page map to pages.json
  2. 🔄 converts only those pages (into docs2/.work/out, nothing else is touched)
  3. 📝 checks that no word was lost (wordcount.py); stops if any was
  4. 📥 copies the new pages and their images into docs2/ (never overwrites an existing page)
  5. ✅ runs the checks

Then commit on a docs2/section-<name> branch and open a pull request into master.
"""
import csv
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
REPO = os.path.dirname(DOCS)


def run(*cmd, env=None):
    print("▶", " ".join(cmd))
    r = subprocess.run(cmd, env=dict(os.environ, **(env or {})))
    if r.returncode:
        sys.exit(f"stopped: {' '.join(cmd[:3])} failed")


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    manual, section, chapter = argv[0], argv[1], argv[2]
    py = sys.executable
    run(py, os.path.join(HERE, "map_pages.py"), REPO, "--apply", "--section", section, "--chapter", chapter)
    pm = json.load(open(os.path.join(HERE, "page_map.json"), encoding="utf-8"))
    ids = [p["id"] for p in pm["pages"] if p["section"] == section and p["status"] == "planned"
           and str(p["number"] or "").split(".")[0] == str(chapter)]
    if not ids:
        sys.exit(f"nothing planned for {section} chapter {chapter}")
    out, work = os.path.join(DOCS, ".work", "out"), os.path.join(DOCS, ".work", "work")
    shutil.rmtree(out, ignore_errors=True)
    env = {"DOCS_ROOT": "docs2", "DOCS_URL_PREFIX": "/docs2", "DOCS_ONLY": ",".join(ids)}
    run(py, os.path.join(HERE, "convert.py"), manual, os.path.join(HERE, "pages.json"), out, work, env=env)
    run(py, os.path.join(HERE, "wordcount.py"), out, work)
    new_pages = new_images = 0
    for d, _, files in os.walk(os.path.join(out, "content")):
        for f in files:
            src = os.path.join(d, f)
            dst = os.path.join(DOCS, os.path.relpath(src, out))
            if not os.path.exists(dst):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)
                new_pages += 1
    idx_rows = {}
    lib_index = os.path.join(DOCS, "images", "index.csv")
    with open(lib_index, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
        head = list(rows[0].keys()) if rows else None
        idx_rows = {r["path"]: r for r in rows}
    for d, _, files in os.walk(os.path.join(out, "images")):
        for f in files:
            src = os.path.join(d, f)
            rel = os.path.relpath(src, out)
            if f == "index.csv":
                with open(src, newline="", encoding="utf-8") as fh:
                    for r in csv.DictReader(fh):
                        idx_rows.setdefault(r["path"], r)
                continue
            dst = os.path.join(DOCS, rel)
            if not os.path.exists(dst):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy(src, dst)
                new_images += 1
    with open(lib_index, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=head, lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(idx_rows.values(), key=lambda r: r["path"]))
    print(f"📥 {new_pages} page(s) and {new_images} image(s) added")
    run(py, os.path.join(HERE, "check.py"), REPO)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
