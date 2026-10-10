# 🌿 Branches and review

> **How a change travels from your save to the website, and who approves it.**

---

## 🌳 Branches

```
master ─────────────────────────────────────────  🔒 .odt manual, untouched until go-live
   └─ docs2/main                                  ⭐ the docs branch: publishes staging, becomes main when all is green
        ├─ docs2/section-<name>                   📄 one branch per section being converted (Tier 2)
        └─ docs2/<your-change>                    ✍️ any reviewed change: Pages CMS on a branch → pull request
```

| Branch | Purpose | Merges into |
|---|---|---|
| `master` | The manual as it is today (`.odt`) | — |
| `docs2/main` | The Docs 2.0 branch. Every merge here syncs to the staging website | `master` (or replaces it) at go-live |
| `docs2/section-<name>` | A section being converted from the `.odt` manual | `docs2/main`, by pull request |
| `docs2/<your-change>` | A change you want reviewed first | `docs2/main`, by pull request |

Earlier test branches (`docs2/spike1-migration`, `docs2/tier1-getting-started`, `docs2/tier1-phase3`, `docs2/tier1-phase5`) are history; their work is all in `docs2/main`.

---

## 🔁 A change, step by step

| Step | Who | What happens |
|---|---|---|
| 1. ✍️ Save | Writer | Pages CMS commits to the working branch, or GitHub opens a pull request |
| 2. 🤖 Check | Bot | Image bot files new images; checks run; a preview link is posted |
| 3. 👀 Review | Section reviewer | Reads the preview, comments or approves |
| 4. 🔀 Merge | Maintainer | Merges the pull request |
| 5. 🌐 Sync | Bot | Pages update on Webflow staging |
| 6. 🚀 Live | Maintainer | Publishes the staging site |

---

## 📘 This wiki and branches

GitHub wikis have **no branches** and **no pull requests**: every edit here is live at once. So:

- 📝 The wiki pages are kept in `docs2/dev-docs/` on the docs branch and reviewed there, like any page.
- 🔄 `docs2/tools/wiki_sync.py` copies them into the wiki.
- 🧪 Until Docs 2.0 is merged into `master`, every copied page carries a **Proposed workflow** notice.
- ✋ Please edit `docs2/dev-docs/`, not the wiki directly; direct wiki edits are overwritten by the next copy.

```bash
python3 docs2/tools/wiki_sync.py docs2/dev-docs ../Manual.wiki --proposed
cd ../Manual.wiki && git add -A && git commit -m "Sync wiki from docs2/dev-docs" && git push
```
