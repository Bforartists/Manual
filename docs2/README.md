# Docs 2.0 · Spike 1 (test branch)

This folder is a **test**, not the new manual yet. It checks whether the `.odt` manual converts cleanly to Markdown before anything else gets built.

- 🌿 Branch: `docs2/spike1-migration`. `master` is untouched.
- 📄 Scope: 3 chapters (Timeline, Interface, Modifiers tab), 18 `.odt` files in total.
- 📊 Results: [`SPIKE1-REPORT.md`](SPIKE1-REPORT.md).

## What is where

| Folder | Holds |
|---|---|
| `content/` | One Markdown file per web page, in the new artist order |
| `snippets/` | Shared sections, written once and included on many pages (`::include{snippet=…}`) |
| `images/` | The image library, each image stored once and named by its place. `images/index.csv` lists them all |
| `tools/` | The converter, re-runnable on any chapter |
| `reports/` | Machine output: conversion counts and the repeated-section scan |
| `dev-docs/` | Draft pages for the developer wiki |

## Run the converter

You need Pandoc 3.x and Python 3.10+ with `lxml` and `Pillow`.

```bash
# from the repository root
DOCS_URL_PREFIX=/docs2 python3 docs2/tools/convert.py . docs2/tools/pages.json docs2 docs2/.work
python3 docs2/tools/find_repeats.py docs2 > docs2/reports/repeats.json
```

`pages.json` decides which source sections go to which page. To convert another chapter, add its pages there.
