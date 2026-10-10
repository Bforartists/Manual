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
