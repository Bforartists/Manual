# 🖼️ Images and screenshots

> **Drop a screenshot into the page. The image bot names it, files it and removes copies.**

---

## 🚀 Adding a screenshot

| Tool | How |
|---|---|
| 🖋️ Pages CMS | Drag the file into the page where it belongs, or `/` → **Image** → upload |
| 🐙 GitHub / 💻 own editor | Copy the file into `docs2/images/`, then add `![What it shows](/docs2/images/your-file.png)` on its own line |

Then write the **alt text**: a few words on what the image shows (*Timeline header with the quick menu open*). Pages CMS fills in the file name; replace it.

---

## 🤖 What the image bot does

New images land in the library root, `docs2/images/`. On the next check run the bot:

| Step | Example |
|---|---|
| 1. 🔍 Finds new images in `docs2/images/` and `docs2/images/_inbox/` | `bforartists_2E0BqKRl0z.png` |
| 2. ♻️ Removes byte-identical copies and points every page at one file | `…z.png` and `…z-1.png` → one file |
| 3. 🏷️ Names it after the page and the heading above it | `getting-started/installation/download-bforartists.png` |
| 4. 🔗 Rewrites the links in every page that uses it | `![…](/docs2/images/getting-started/installation/download-bforartists.png)` |
| 5. 📋 Adds it to `docs2/images/index.csv` with size and checksum | |
| 6. 💬 Lists what it filed in the pull request comment | |

It never deletes an image a page still uses, and it never changes your text.

---

## 📐 Sizes and layout

| Image width | Website shows |
|---|---|
| Under 900 px | Floated right, text flows beside it |
| 900 px and wider | Full width |

No codes needed: the size decides. Crop screenshots to the part that matters.

---

## 📚 The library

- 📂 `docs2/images/<section>/<page>/…`: images used by one page.
- 📂 `docs2/images/ui/shared/…`: images used by shared sections.
- 📋 `docs2/images/index.csv`: every image once, with its size, checksum and the pages that use it.
- ♻️ An image is stored once, however many pages show it.
