#!/usr/bin/env python3
"""Image bot: file new screenshots into the image library.

    python3 docs2/tools/image_bot.py [repo root] [--dry-run] [--report bot.md]

New images are the ones in docs2/images/ (the library root, where Pages CMS drops land)
and in docs2/images/_inbox/. For each new image the bot:

  1. removes byte-identical copies (also copies of images already in the library), but only
     once a page links to the new file, so an image uploaded a moment before its page is saved
     is not deleted too early
  2. names it after the page and the heading above it:
     images/<section>/<page>/<heading>.png
  3. rewrites the links in every page and shared section that uses it
  4. replaces alt text that is only a file name with the heading text
  5. shrinks images wider than 1920 px
  6. adds it to images/index.csv

It never touches text other than image links and file-name alt text, and it never
deletes an image a page still uses. Images no page uses yet are left where they are.
"""
import csv
import hashlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import DOCS_ROOT, IMAGE_EXT, LINK, URL_PREFIX, iter_pages, resolve, slugify  # noqa: E402

MAX_WIDTH = 1920
FILE_NAME_ALT = re.compile(r"^[\w.-]+\.(png|jpe?g|webp|gif)$", re.I)
INDEX_HEAD = ["path", "sha256_16", "width_px", "height_px", "bytes", "uses", "source_odt_media"]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


def image_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except Exception:
        return (0, 0)


def new_images(lib):
    found = [os.path.join(lib, f) for f in sorted(os.listdir(lib)) if f.lower().endswith(IMAGE_EXT)]
    inbox = os.path.join(lib, "_inbox")
    if os.path.isdir(inbox):
        found += [os.path.join(inbox, f) for f in sorted(os.listdir(inbox)) if f.lower().endswith(IMAGE_EXT)]
    return found


def read_index(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(argv):
    dry = "--dry-run" in argv
    report = argv[argv.index("--report") + 1] if "--report" in argv else None
    args = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] != "--report")]
    repo = args[0] if args else "."
    lib = os.path.join(repo, DOCS_ROOT, "images")
    index_path = os.path.join(lib, "index.csv")
    index = read_index(index_path)
    known = {}                                     # sha -> library path (repo-relative)
    for row in index:
        known.setdefault(row["sha256_16"], DOCS_ROOT + row["path"])   # index paths are /images/...

    pages = list(iter_pages(repo))
    uses = {}                                      # repo path -> [(page, line, alt)]
    for p in pages:
        for n, is_img, alt, target in p.links():
            if is_img:
                r = resolve(p, target)
                if r:
                    uses.setdefault(r, []).append((p, n, alt))

    moves, notes = {}, []                          # old repo path -> new repo path
    taken = {os.path.relpath(os.path.join(d, f), repo).replace("\\", "/")
             for d, _, fs in os.walk(lib) for f in fs}
    by_hash = {}
    for full in new_images(lib):
        rel = os.path.relpath(full, repo).replace("\\", "/")
        h = sha(full)
        # A picture that is already in the library is only swapped for the library copy once a page
        # links to the new file. Pages CMS uploads the image first and saves the page a moment later;
        # deleting the copy in between leaves that page pointing at a file that is gone.
        if h in known and os.path.exists(os.path.join(repo, known[h])) and uses.get(rel):
            moves[rel] = known[h]
            notes.append(("♻️", rel, known[h], "same picture is already in the library"))
            continue
        if h in by_hash:
            moves[rel] = by_hash[h]
            notes.append(("♻️", rel, by_hash[h], "byte-identical copy"))
            continue
        users = uses.get(rel, [])
        if not users:
            # a copy nobody links to is filed with its twin later; otherwise wait for a page to use it
            by_hash.setdefault(h, rel)
            notes.append(("⏳", rel, "", "no page uses it yet; left in place"))
            continue
        p, line, alt = users[0]
        heading = p.heading_before(line)
        name = slugify(heading if heading else os.path.splitext(os.path.basename(rel))[0])
        ext = os.path.splitext(rel)[1].lower().replace(".jpeg", ".jpg")
        base = f"{DOCS_ROOT}/images/{p.page_key}/{name}"
        new, k = base + ext, 2
        while new in taken:
            new, k = f"{base}-{k}{ext}", k + 1
        taken.add(new)
        moves[rel] = new
        by_hash[h] = new
        known[h] = new
        notes.append(("🏷️", rel, new, f"named after “{heading}” on {p.rel}"))

    # copies of an image that was waiting, whose twin got a name above
    for i, (icon, old, new, why) in enumerate(notes):
        if icon == "⏳":
            h = sha(os.path.join(repo, old))
            if by_hash.get(h) not in (None, old):
                moves[old] = by_hash[h]
                notes[i] = ("♻️", old, by_hash[h], "byte-identical copy")

    # rewrite links in pages
    edited = {}
    alt_fixes = 0
    for p in pages:
        text = p.text

        def fix(m, p=p):
            nonlocal alt_fixes
            bang, alt, target = m.group(1), m.group(2), m.group(3)
            if not bang:
                return m.group(0)
            r = resolve(p, target)
            if r not in moves:
                return m.group(0)
            new_target = URL_PREFIX + moves[r][len(DOCS_ROOT):]
            if FILE_NAME_ALT.match(alt.strip()):
                line = text[:m.start()].count("\n") + 1
                alt = p.heading_before(line) or alt
                alt_fixes += 1
            return f"{bang}[{alt}]({new_target})"
        new_text = LINK.sub(fix, text)
        if new_text != text:
            edited[p.rel] = new_text

    # apply
    filed = [(o, n) for o, n in moves.items() if not any(x[0] == "♻️" and x[1] == o for x in notes)]
    copies = [o for o, n in moves.items() if (o, n) not in filed]
    if not dry:
        for old, new in filed:
            dst = os.path.join(repo, new)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            os.replace(os.path.join(repo, old), dst)
            w, h = image_size(dst)
            if w > MAX_WIDTH:
                from PIL import Image
                with Image.open(dst) as im:
                    im.resize((MAX_WIDTH, round(h * MAX_WIDTH / w)), Image.LANCZOS).save(dst, optimize=True)
                notes.append(("📐", new, "", f"shrunk from {w} px to {MAX_WIDTH} px wide"))
        for old in copies:
            os.remove(os.path.join(repo, old))
        for rel, text in edited.items():
            open(os.path.join(repo, rel), "w", encoding="utf-8", newline="\n").write(text)
        rows = {r["path"]: r for r in index}
        for old, new in filed:
            dst = os.path.join(repo, new)
            w, h = image_size(dst)
            key = new[len(DOCS_ROOT):]
            rows[key] = {"path": key, "sha256_16": sha(dst), "width_px": w, "height_px": h,
                         "bytes": os.path.getsize(dst), "uses": len(uses.get(old, [])), "source_odt_media": ""}
        with open(index_path, "w", newline="", encoding="utf-8") as f:
            wr = csv.DictWriter(f, fieldnames=INDEX_HEAD, lineterminator="\n")
            wr.writeheader()
            wr.writerows(sorted(rows.values(), key=lambda r: r["path"]))

    md = ["### 🤖 Image bot" + (" (dry run)" if dry else ""), ""]
    if not notes:
        md.append("No new images.")
    else:
        md += [f"{len(filed)} filed · {len(copies)} copies removed · {alt_fixes} alt text(s) set · "
               f"{len(edited)} page(s) updated", "", "| | Image | Now | Why |", "|---|---|---|---|"]
        md += [f"| {i} | `{os.path.basename(o)}` | {('`' + n[len(DOCS_ROOT) + 1:] + '`') if n else '—'} | {w} |"
               for i, o, n, w in notes]
    out = "\n".join(md) + "\n"
    if report:
        open(report, "w", encoding="utf-8").write(out)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
