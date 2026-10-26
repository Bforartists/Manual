# ✍️ Plain writing

> **Docs pages contain no special codes. Write normally; the website turns plain patterns into components.**

Pages read well on GitHub too, and the online editor saves them unchanged.

---

## 🧩 Patterns

| You write | The website shows | Notes |
|---|---|---|
| `> **Tip:** text` (also Note, Warning, Important) | 💡 Callout | In Pages CMS: `/` → Quote, start with Tip:. Bold is optional |
| `Ctrl + Space` | ⌨️ Keycaps | Ctrl, Shift, Alt, Cmd, LMB, MMB, RMB, Wheel, F1–F12 |
| `Edit › Preferences › System` | 🧭 Menu path with icons | Use `›`; only real menu names become chips |
| An image on its own line | 🖼️ Floated right when small, full width when wide | Size decides; no codes |
| An image, then a list of `**Label** (colour): text` | 🎯 Screenshot with hover areas | Matches the coloured areas in the screenshot |
| `*Shared section: [Quick menu](…)*` | ♻️ The shared section, filled in | Add it with the **Shared sections** field. See [Shared sections](Shared-Sections.md) |
| A YouTube link alone on a line | 🎬 Video | Or the **Chapter video** field |
| A heading named like a tool (`### Bevel`) | 🧰 Tool card | Name, icon, tooltip and hotkey come from Bforartists |
| A table | 📋 Table | Scrolls sideways on phones |
| A path or file pattern in backticks: `` `./scripts/*.py` `` | `./scripts/*.py` in code style | Keeps `\`, `*` and `$` safe in the editor |

---

## 📄 The page header (front matter)

Pages CMS shows this as a form. Fields marked read-only are set by the converter and the build. It is written the way the editor saves it: plain values, quotes only where needed, one list item per line.

```yaml
---
id: getting-started.installation     # read-only: stable page ID
title: Installation
slug: installation                   # read-only: the web address
section: getting-started
path:
  - Getting Started
  - Installation
version: "5.1"
status: draft                        # draft · needs-review · reviewed
screenshots: "5.1"
video: https://youtu.be/…            # optional chapter video
shared:                              # optional shared sections on this page
  - docs2/snippets/quick-menu.md
source:                              # read-only
  - 2 Installing Bforartists.odt
---
```

---

## 🧭 Headings follow the artist route

Page title = the editor or area · `##` object type · `###` mode · `####` area · `#####` panel or menu.

---

## 🧩 Sub-chapters on one page, with icons

Some pages cover a family of things (the 3D View with meshes, curves, lights). Start each one with a level 1
heading (`#`); add `{icon=name}` at the end for its icon (Bforartists icon names, like the `icon:` field).

```markdown
Short introduction.

# Meshes {icon=outliner_ob_mesh}

## Add a mesh

# Curves {icon=outliner_ob_curve}
```

| Place | What shows |
|---|---|
| ⬅️ Left sidebar | The page, with a link to each sub-chapter |
| ➡️ Right side | One panel per sub-chapter with its headings |
| 📌 Top of the text | A slim bar with the sub-chapter you are reading |

Use `#` only for sub-chapters (the page title comes from the header form). `{icon=…}` works only on `#` headings;
the check warns elsewhere. Three to eight sub-chapters per page.

## 🚫 Avoid

| Avoid | Why | Instead |
|---|---|---|
| Backslashes outside backticks (`\*`, `C:\Users`) | The editor drops them with the next character | Put paths in backticks |
| `<br>` and other HTML | Dropped inside tables; noise elsewhere | A new paragraph, or a list |
| `A > B` for menus | Saved as `A &gt; B` | `A › B` |
