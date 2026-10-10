# 🌿 Branches and review

> **How a change travels from your save to the website, and who approves it.**

---

## 🌳 Branches today (testing)

```
master ─────────────────────────────────────────  🔒 .odt manual, untouched
   └─ docs2/spike1-migration                      first test conversion
        └─ docs2/tier1-getting-started            ⭐ working branch: Pages CMS saves here
             └─ docs2/tier1-phase3                🧪 test branch for checks, image bot, preview
                                                     → pull request into the working branch
```

| Branch | Purpose | Merges into |
|---|---|---|
| `master` | The manual as it is today | — |
| `docs2/tier1-getting-started` | Docs 2.0 working branch. Pages CMS edits land here | `master`, once Docs 2.0 is approved |
| `docs2/tier1-phase3` | Test branch for the automation | `docs2/tier1-getting-started`, by pull request |

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
