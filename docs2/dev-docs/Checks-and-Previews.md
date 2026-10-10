# ✅ Checks and previews

> **Every change answers two questions on its own: is it correct, and how will it look?**

🚧 Being built in Phase 3 on the test branch `docs2/tier1-phase3`.

---

## 🔍 What is checked

| Check | Fails the change | Example |
|---|---|---|
| 📄 Front matter | ❌ yes | `status` must be draft, needs-review or reviewed |
| 🆔 Unique page IDs and addresses | ❌ yes | Two pages with `slug: installation` in one section |
| 🔗 Links between pages | ❌ yes | `[Timeline](../timeline.md)` points nowhere |
| 🖼️ Images exist | ❌ yes | `![…](/docs2/images/missing.png)` |
| ♻️ Shared sections exist | ❌ yes | `shared:` lists a file that is not in `docs2/snippets/` |
| 🏷️ Alt text | 🟡 warning | Empty, or still the file name |
| 🖋️ Editor-safe text | 🟡 warning | A backslash or `<br>` the editor would drop |

---

## 👀 The preview

The bot builds every changed page with the website's doc kit styles and posts a link in the pull request:

> 👀 **Preview:** Installation · Comparing to Blender
> ✅ 12 checks passed · 🖼️ 1 image filed

---

## ⚙️ For maintainers

| Tool | Does |
|---|---|
| `docs2/tools/check.py` | All checks; writes a Markdown report |
| `docs2/tools/image_bot.py` | Files new images ([Images and screenshots](Images-and-Screenshots.md)) |
| `docs2/tools/patterns.py` | The plain-writing recogniser, shared by the preview and the website sync |
| `docs2/tools/render.py` | Builds the preview pages |
| `.github/workflows/docs2.yml` | Runs them on every push to a `docs2/` branch and every pull request |
