# 📘 Docs 2.0 (test branch)

The Bforartists manual as Markdown: one file per web page, written in plain text that reads well on GitHub and is turned into rich components on the website. **This is a test branch;** `master` and the `.odt` manual are untouched.

[![Edit the docs in Pages CMS](https://img.shields.io/badge/Edit_the_docs-Pages_CMS-2ea44f?style=for-the-badge&logo=markdown&logoColor=white)](https://app.pagescms.org/Bforartists/Manual/docs2%2Ftier1-getting-started/collection/docs)
[![Shared snippets](https://img.shields.io/badge/Shared-snippets-6f42c1?style=for-the-badge&logo=files&logoColor=white)](https://app.pagescms.org/Bforartists/Manual/docs2%2Ftier1-getting-started/collection/snippets)
[![Image library](https://img.shields.io/badge/Image-library-0969da?style=for-the-badge&logo=googlephotos&logoColor=white)](https://app.pagescms.org/Bforartists/Manual/docs2%2Ftier1-getting-started/media/images)
[![Developer wiki](https://img.shields.io/badge/Developer-wiki-555555?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Bforartists/Manual/wiki)

> ✏️ **To edit:** click **Edit the docs**, sign in with GitHub, pick a page, change it, click **Save**. First time? Read [Editing the docs online](dev-docs/Editing-the-docs-online.md).

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
| `images/` | 🖼️ The image library, each image stored once, named by where it is used; `images/index.csv` lists them. New drops land in the root and the image bot files them |
| `nav.yml` | 🧭 Sidebar order and icons |
| `sources/webflow/` | The current website text the converter reads for pages that live on the website |
| `tools/` | ⚙️ Converter, word-count check, repeat scan, sidebar generator, checks, page-header and image bots, preview, Webflow sync, wiki sync |
| `reports/` | 📊 Machine output of the last run |
| `dev-docs/` | 📘 The [wiki](https://github.com/Bforartists/Manual/wiki) pages, reviewed here and copied by `tools/wiki_sync.py` |
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

## 🤖 On every change

`.github/workflows/docs2.yml` fills in new page headers, files new screenshots, checks every page and posts a 👀 preview link with the website's styles. After a merge it syncs the pages to the staging website. See [Checks and previews](dev-docs/Checks-and-Previews.md) and [Website sync](dev-docs/Website-Sync.md).

## ⚙️ Run the converter

Needs Pandoc 3.x and Python 3.10+ (`pip install -r docs2/tools/requirements.txt`). From the repository root:

```bash
DOCS_ROOT=docs2 DOCS_URL_PREFIX=/docs2 python3 docs2/tools/convert.py . docs2/tools/pages.json docs2 docs2/.work
python3 docs2/tools/wordcount.py docs2 docs2/.work            # fails if any source words are lost
python3 docs2/tools/make_nav.py docs2/tools/pages.json docs2/nav.yml
python3 docs2/tools/find_repeats.py docs2 > docs2/reports/repeats.json
```

`tools/pages.json` decides which source sections become which page. No text is trimmed or reworded (decision D13); trimming comes after the full migration is live.
