# 🚀 Release update

> **When a new Bforartists version ships, the manual follows in one pull request per step. Here is the checklist, in order.**

---

```mermaid
flowchart LR
  A["🏷️ Version<br/>and what's new"] --> B["📸 Screenshots<br/>and workspace maps"]
  B --> C["⌨️ Keymap<br/>(when automated)"]
  C --> D["🧹 Blender mentions<br/>and summaries"]
  D --> E["✅ Review<br/>status"]
  E --> F["🌐 Publish<br/>live"]
```

## ✅ Checklist

- [ ] 🏷️ **Version.** Update `version:` on pages you checked against the new release, and `What's new` in `appendix/manual-update-history.md`. The Docs home's "What changed" card links there.
- [ ] 📸 **Workspace maps.** Re-shoot all workspaces with `ws_capture.py` and import them ([Workspace maps](Workspace-Maps.md#re-shoot-the-workspaces-each-release)).
- [ ] 🖼️ **Screenshots that changed.** Drop new screenshots in Pages CMS; the image bot files them under the same names, so pages need no edit ([Images and screenshots](Images-and-Screenshots.md)).
- [ ] ⌨️ **Keymap.** Automatic: run **Docs 2.0 keymap** (Actions) and merge its pull request; add any new keymap to `contexts.yml` if the check asks ([Keymap](Keymap.md)).
- [ ] 🧹 **Clean-up reports.** `python3 docs2/tools/cleanup.py --dry` lists pages that say "Blender" for the program you use; `summaries.py --dry` lists pages without a summary. Fix what they find.
- [ ] ✅ **Checks pass** on the pull request (links, images, sidebar, workspace maps).
- [ ] 👀 **Review status.** Reviewers set `status: reviewed` on the pages they checked.
- [ ] 🌐 **Publish live** (below).

## Publish live

Only the lead maintainer does this, once staging looks right.

1. Open **bforartists.webflow.io/docs/home** and click through: a section overview, a workspace page, the keymap, the search (Ctrl K).
2. Webflow → **Publish** → tick **bforartists.co** (and webflow.io) → Publish.
3. Check the same pages on bforartists.co. If anything is wrong, fix it in GitHub and publish again; site scripts can be rolled back in minutes ([Site scripts](Site-Scripts.md#roll-back)).

**The first time only (October 2026):** the old `/documentation/…` pages are drafts in Webflow. Before that first live publish, add the 41 redirects in [`docs2/reports/webflow-redirects.md`](../reports/webflow-redirects.md) (Site settings › Publishing › 301 redirects), so old links and search results land on the new pages. Delete the old pages in the Designer a week or two later.
