# 🗺️ How Docs 2.0 works

> **Less work for contributors, more for the reader. No server to run.**

---

## 🛣️ The road a page travels

```
  📄 .odt chapters (master)                   ✍️ Writers
          │  converter (once per chapter)          │  Pages CMS · GitHub · own editor
          ▼                                        ▼
  ┌───────────────────────────────────────────────────────┐
  │  📘 docs2/  Markdown pages on a GitHub branch          │
  │     content/   snippets/   images/   nav.yml           │
  └───────────────────────────┬───────────────────────────┘
                              │  every save / pull request
                              ▼
  ┌───────────────────────────────────────────────────────┐
  │  🤖 GitHub Actions                                     │
  │     🖼️ image bot   ✅ checks   👀 preview link          │
  └───────────────────────────┬───────────────────────────┘
                              │  after review and merge
                              ▼
  ┌───────────────────────────────────────────────────────┐
  │  🌐 Webflow staging  →  maintainer's click  →  live    │
  │     📄 PDF printed on demand from the website          │
  └───────────────────────────────────────────────────────┘
```

---

## 🧱 Pieces

| Piece | What it is | Where |
|---|---|---|
| 📘 Pages | One Markdown file per web page | `docs2/content/` |
| ♻️ Snippets | Sections shared by several pages | `docs2/snippets/` |
| 🖼️ Image library | Every image once, filed by page | `docs2/images/` |
| 🧭 Sidebar | Order and icons of the website sidebar | `docs2/nav.yml` |
| 🖋️ Online editor | [Pages CMS](https://app.pagescms.org), free and open source, nothing to host | `.pages.yml` |
| ⚙️ Tools | Converter, checks, image bot, preview, sync | `docs2/tools/` |
| 🤖 Automation | Runs the tools on every change | `.github/workflows/docs2.yml` |
| 🌐 Website | Webflow CMS: Doc Sections, Doc Pages, Doc Snippets | bforartists.webflow.io (staging) |

---

## 📏 Rules we keep

| # | Rule |
|---|---|
| 1 | 🧰 Writers install nothing |
| 2 | ✍️ Pages contain no special codes ([Plain writing](Plain-writing.md)) |
| 3 | 📝 Nothing is trimmed or reworded until the whole manual is migrated and live |
| 4 | 🔒 `master` and the `.odt` manual stay untouched until Docs 2.0 is approved |
| 5 | 🌐 Nothing reaches the live website without a maintainer's click |
