# 🌿 Branches and review

> **How a change travels from your save to the website, and who approves it.**

---

## 🌳 Branches

```
master ─────────────────────────────────────────  ⭐ the manual: docs2/ publishes staging on every merge
   ├─ docs2/<your-change>                         ✍️ any reviewed change → pull request into master
   ├─ <your-name>-patch-1                         ✏️ made for you by "Edit this page" (GitHub editor)
   └─ docs2/keymap-update                         🤖 the weekly keymap robot
```

| Branch | Purpose | Merges into |
|---|---|---|
| `master` | The manual. The Markdown docs live in `docs2/` (the old `.odt` chapters are archived in `docs1/`). Every merge syncs to the staging website | — |
| `docs2/<your-change>` | A change you want reviewed first | `master`, by pull request |
| `*-patch-*` | Made by GitHub when you use **Edit this page**: always starts from the latest `master` | `master`, by pull request |
| `docs2/keymap-update` | The weekly keymap robot's pull request | `master` |

Earlier branches (`master`, `docs2/spike1-migration`, `docs2/tier1-*`) are history: since October 2026 the docs live on `master`.

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

- 📝 The wiki pages are kept in `docs2/dev-docs/` on `master` and reviewed there, like any page.
- 🤖 After every merge that touches them, the **Docs 2.0 wiki** workflow (`.github/workflows/docs2-wiki.yml`) runs `docs2/tools/wiki_sync.py` and publishes them to the wiki. Run it by hand from **Actions → Docs 2.0 wiki → Run workflow**.
- ✋ Please edit `docs2/dev-docs/`, not the wiki directly; direct wiki edits are overwritten by the next copy. Pages that exist only in the wiki (like the Reference Manual writing guide) are left alone.

To copy by hand from your own computer:

```bash
python3 docs2/tools/wiki_sync.py docs2/dev-docs ../Manual.wiki
cd ../Manual.wiki && git add -A && git commit -m "Sync wiki from docs2/dev-docs" && git push
```
