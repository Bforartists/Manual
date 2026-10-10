# 🌐 Website sync

> **Merge on GitHub, and the pages appear on the staging website. The live site is a separate, manual click.**

🧪 Built in Phase 5 on the test branch `docs2/tier1-phase5`.

---

## 🛣️ What happens after a merge

| Step | What | Where |
|---|---|---|
| 1. 🧾 | New pages get their ID, section and breadcrumb | `fill_front_matter.py` |
| 2. 🖼️ | New screenshots are filed | `image_bot.py` |
| 3. ✅ | Every page is checked | `check.py` |
| 4. 🌐 | Sections, shared sections and pages are written to Webflow's CMS | `sync.py` |
| 5. 🚀 | bforartists.webflow.io is published | Webflow API, staging only |

It runs on every push to the publish branch (`docs2/main`) when the checks pass, and from
**Actions → Docs 2.0 checks and preview → Run workflow**.

---

## 📚 How pages map to the website

| In the repository | On the website |
|---|---|
| A folder under `content/` (`content/doc-kit/`) | 📚 A section in the sidebar (Doc Sections) |
| The section's `index.md` | The section overview |
| A page in the section (`installation.md`) | 📄 A chapter |
| A folder with `index.md` (`my-chapter/index.md`) | 📄 A chapter |
| A page inside that folder (`my-chapter/part-one.md`) | ↳ A sub-chapter, indented under its chapter |
| A file in `snippets/` | ♻️ A shared section (Doc Snippets) |
| `id: doc-kit.my-chapter` | Web address `/docs/doc-kit-my-chapter` |

Order: as in `nav.yml`; new pages follow in folder order; *Position in the sidebar* (`order:`) wins.

---

## 🛡️ Safety

| | |
|---|---|
| 🔑 | Items are matched on their IDs, never on names |
| ⏭️ | Unchanged pages are skipped |
| ✋ | A page edited by hand in Webflow after the last sync is skipped and reported. Fix it in GitHub instead |
| 🧹 | Nothing is deleted; Webflow items with no page in the repository are listed |
| 🌐 | Publishes the **webflow.io** address only. Custom domains (bforartists.co) are never published by the sync |
| 🖼️ | Images are sent as GitHub links at the exact commit; Webflow copies them to its own CDN |

---

## 🔑 One-time setup (maintainer)

1. Webflow → Bforartists site → **Site settings → Apps & integrations → API access → Generate API token**.
   Name `Docs sync`; permissions **CMS: Read and write**, **Sites: Read and write**.
2. GitHub → `Bforartists/Manual` → **Settings → Secrets and variables → Actions → New repository secret**,
   name `WEBFLOW_TOKEN`.
3. Site and collection IDs are in `docs2/tools/webflow.json` (no secrets there).

---

## 💻 Try it without touching Webflow

```bash
python3 docs2/tools/sync.py . --plan plan.json     # writes what would be sent; needs no token
```
