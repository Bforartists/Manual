# 📦 Docs 1 · the legacy `.odt` manual

These are the original Bforartists manual chapters, one LibreOffice / OpenOffice `.odt` file per chapter, numbered like the old PDF manual (`1 Introduction.odt`, `10.1 Editors - Compositor - Header.odt` …).

> ⚠️ **Archive, not the manual.** Every chapter here was converted word for word into Markdown in [`docs2/`](../docs2), which is what the website shows today. Please make new changes there, not in these files.

[![Read the docs](https://img.shields.io/badge/Read_the-docs-0969da?style=for-the-badge&logo=readthedocs&logoColor=white)](https://www.bforartists.com/docs/home)
[![Edit the docs](https://img.shields.io/badge/Edit_the_docs-Pages_CMS-2ea44f?style=for-the-badge&logo=markdown&logoColor=white)](https://app.pagescms.org/bforartists/manual/master/collection/docs)

## Why it is kept

- 🔎 **Source of truth for the conversion.** The converter (`docs2/tools/convert.py`) and the word-count check read these files, so any page can be compared with its original.
- 🏷️ **Old releases.** The release archives of the PDF manual are on the [releases page](https://github.com/Bforartists/Manual/releases).

## Tools

- `convert_all_odt_to_pdf.bat` (Windows, needs LibreOffice) turns every `.odt` in this folder into a PDF. Double-click it here.
- To re-run the Markdown converter against this folder, from the repository root:

```bash
python3 docs2/tools/convert.py docs1 docs2/tools/pages.json docs2 docs2/.work
python3 docs2/tools/wordcount.py docs2 docs2/.work
```
