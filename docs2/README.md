# 📘 Docs 2.0 (test branch)

The Bforartists manual as Markdown: one file per web page, written in plain text that reads well on GitHub and is turned into rich components on the website. **This is a test branch;** `master` and the `.odt` manual are untouched.

- 🌿 Branch: `docs2/tier1-getting-started`
- 🗺️ Plan: [`plans/plan_docs2_tier1_getting_started.md`](plans/plan_docs2_tier1_getting_started.md)
- 🧪 Usability test: [`plans/usability_test_getting_started.md`](plans/usability_test_getting_started.md)
- ✅ Faithful-clone check: [`reports/wordcount.md`](reports/wordcount.md)

## 📂 What is where

| Folder | Holds |
|---|---|
| `content/getting-started/` | ⭐ The 8 Getting Started pages (Tier 1) |
| `content/editors/…`, `content/interface/…` | Spike 1 pages: Timeline, Interface, Modifiers tab |
| `snippets/` | ♻️ Shared sections, written once, linked from every page that shows them |
| `images/` | 🖼️ The image library, each image stored once, named by where it is used; `images/index.csv` lists them |
| `nav.yml` | 🧭 Sidebar order and icons |
| `sources/webflow/` | The current website text the converter reads for pages that live on the website |
| `tools/` | ⚙️ Converter, word-count check, repeat scan, sidebar generator |
| `reports/` | 📊 Machine output of the last run |
| `dev-docs/` | 📘 Draft pages for the developer wiki |
| `plans/` | 🗺️ Plans and tests |

## ✍️ Plain writing

Pages contain no special tags. The website build recognises plain patterns:

| You write | The website shows |
|---|---|
| `> **Tip:** …` (also Note, Warning, Important) | A callout |
| `Ctrl + Space` | Keycaps |
| `Edit › Preferences` | A menu path |
| An image on its own line | Floated right when small, full width when wide |
| An image followed by a list of `**Label** (colour)` | A screenshot with hover areas |
| `*Shared section: [Quick menu](…)*` | The shared section, filled in from `snippets/` |

## ⚙️ Run the converter

Needs Pandoc 3.x and Python 3.10+ (`pip install -r docs2/tools/requirements.txt`). From the repository root:

```bash
DOCS_URL_PREFIX=/docs2 python3 docs2/tools/convert.py . docs2/tools/pages.json docs2 docs2/.work
python3 docs2/tools/wordcount.py docs2 docs2/.work            # fails if any source words are lost
python3 docs2/tools/make_nav.py docs2/tools/pages.json docs2/nav.yml
python3 docs2/tools/find_repeats.py docs2 > docs2/reports/repeats.json
```

`tools/pages.json` decides which source sections become which page. No text is trimmed or reworded (decision D13); trimming comes after the full migration is live.
