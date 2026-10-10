# ✅ Checks and previews

> **Every change answers two questions on its own: is it correct, and how will it look?**

🧪 Built in Phase 3 on the test branch `docs2/tier1-phase3`, reviewed as a pull request into `docs2/tier1-getting-started`.

---

## 🔁 What runs, and when

| When | 🤖 Image bot | ✅ Checks | 👀 Preview | 💬 Comment |
|---|---|---|---|---|
| A pull request touches `docs2/` | ✅ files images, commits back | ✅ | ✅ `/preview/pr-<number>/` | ✅ one comment, updated on every push |
| A Pages CMS save on a `docs2/…` branch | ✅ | ✅ | ✅ `/preview/branch-<name>/` | Job summary |
| A pull request from a fork | Dry run only | ✅ | Download from the run | — |

The workflow is `.github/workflows/docs2.yml`. It lives on the docs branches only; `master` is untouched.

---

## 🔍 What is checked

| Check | Fails the change | Example |
|---|---|---|
| 📄 Front matter | ❌ yes | `status` must be draft, needs-review or reviewed; `version: "5.1"` in quotes |
| 🆔 Unique page IDs and addresses | ❌ yes | Two pages with `slug: installation` in one section |
| 🔗 Links between pages | ❌ yes | `[Timeline](../timeline.md)` points nowhere |
| 🖼️ Images exist | ❌ yes | `![…](/docs2/images/missing.png)` |
| ♻️ Shared sections exist | ❌ yes | `shared:` lists a file that is not in `docs2/snippets/` |
| 🧭 Sidebar | ❌ yes | `nav.yml` lists a page that does not exist |
| 🏷️ Alt text | 🟡 warning | Empty on a screenshot, or still the file name (small icons may be empty) |
| 🖋️ Editor-safe text | 🟡 warning | A backslash or `<br>` the editor would drop |
| 🤖 Waiting images | 🟡 warning | An image still in the library root or `_inbox/` |

---

## 👀 The preview

The changed pages, drawn with the **same doc kit CSS as the website** (`docs2/tools/preview/doc-kit.css`, copied from the Webflow template):

- 💡 callouts, ⌨️ keycaps, 🧭 menu chips, 🖼️ floated screenshots, ♻️ shared sections filled in, 🎬 videos, 📋 tables
- the sidebar, the page sections outline, light and dark mode
- ✏️ **Edit this page** opens the page in Pages CMS; 🐙 **View the Markdown** opens it on GitHub

The front page of each preview shows the check results and what the image bot did.

---

## 🔑 One-time setup (maintainer)

| Where | Set |
|---|---|
| ⚙️ Settings → Actions → General → Workflow permissions | **Read and write permissions** (the bot commits filed images and the preview) |
| 📄 Settings → Pages → Build and deployment | **Deploy from a branch** → `gh-pages` / `(root)`; the first preview run creates the branch |

Previews then open at `https://bforartists.github.io/Manual/preview/<pr-N or branch-name>/`.

---

## 💻 Run it on your computer

```bash
pip install -r docs2/tools/requirements.txt
python3 docs2/tools/image_bot.py . --dry-run       # what the bot would file
python3 docs2/tools/check.py .                     # exit code 1 when something must be fixed
python3 docs2/tools/render.py . --out _preview     # open _preview/index.html
```

| Tool | Does |
|---|---|
| `docs2/tools/check.py` | All checks; writes a Markdown report |
| `docs2/tools/image_bot.py` | Files new images ([Images and screenshots](Images-and-Screenshots.md)) |
| `docs2/tools/patterns.py` | The plain-writing recogniser, shared by the preview and the website sync |
| `docs2/tools/render.py` | Builds the preview pages |
| `docs2/tools/docs_io.py` | Shared helpers: pages, front matter, links |
