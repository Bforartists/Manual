# 🔄 Converting chapters

> **Turn `.odt` chapters into pages without losing a word.**

For maintainers. Writers never need this: once a chapter is converted, it is edited as Markdown.

---

## 🧰 Needs

| Tool | Version |
|---|---|
| 🐍 Python | 3.10 or newer |
| 📄 Pandoc | 3.x |
| 📦 Python packages | `pip install -r docs2/tools/requirements.txt` |

---

## 🗺️ Plan a chapter first

```bash
python3 docs2/tools/inventory.py ../path/to/odt/manual          # words, images, tables per file → docs2/reports/
python3 docs2/tools/map_pages.py .                               # where every file lands → docs2/reports/page-map.md
python3 docs2/tools/map_pages.py . --apply --section editors --chapter 7   # move one chapter into pages.json
```

| File | Holds |
|---|---|
| `docs2/tools/sections.yml` | The 8 sidebar sections, in chapter-list order, with folder names and group titles |
| `docs2/tools/page_map.json` | Every planned page, in `pages.json` format |
| `docs2/tools/legacy_pages.json` | The current website's documentation addresses, for redirects |
| `docs2/reports/page-map.md` | The map as a table: done ✅, planned ⏳, very long ✂️ |

The rule: one page per `.odt` file. A chapter becomes a folder with `index.md`, its sub-chapters pages inside it.
Files under 80 words fold into the page above them.

## ▶️ Run

From the repository root:

```bash
DOCS_ROOT=docs2 DOCS_URL_PREFIX=/docs2 python3 docs2/tools/convert.py . docs2/tools/pages.json docs2 docs2/.work
python3 docs2/tools/wordcount.py docs2 docs2/.work            # fails if any source words are lost
python3 docs2/tools/make_nav.py docs2/tools/pages.json docs2/nav.yml
python3 docs2/tools/find_repeats.py docs2 > docs2/reports/repeats.json
```

---

## 🗂️ `pages.json`

Decides which source sections become which page.

| Key | Meaning |
|---|---|
| `file` | The page to write, under `docs2/` |
| `parts` | Where its text comes from: an `.odt` chapter (`src`), the current website (`web`), or a short note (`note`) |
| `slug`, `icon`, `status` | Front matter for the website |
| `snippets` | Shared sections, written to `docs2/snippets/` |

---

## ✅ What the converter guarantees

| Guarantee | How |
|---|---|
| 📝 No lost words | `wordcount.py` compares every chapter with its pages; the run fails otherwise |
| 🖋️ Editor-ready | Pages are written exactly as Pages CMS saves them, so a later one-word edit changes one line |
| ✍️ Plain writing | Tips become `> **Tip:**` quotes, hotkeys `Ctrl + S`, menus `A › B` |
| 🔒 Safe characters | No backslash escapes; paths and `*.py` patterns go in backticks |
| 🖼️ One copy per image | Images are stored once and named by where they are used |
