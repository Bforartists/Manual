# ✍️ Plain writing

Docs pages contain **no special codes**. Write normally; the website build recognises these patterns and turns them into components. Pages read well on GitHub too.

| You write | The website shows | Notes |
|---|---|---|
| `> **Tip:** text` (also Note, Warning, Important) | 💡 Callout | In Pages CMS: `/` → Quote, start with Tip: |
| `Ctrl + Space` | ⌨️ Keycaps | Ctrl, Shift, Alt, Cmd, LMB, MMB, RMB, Wheel, F1–F12 |
| `Edit › Preferences › System` | 🧭 Menu path with icons | Use `›`; only real menu names become chips |
| An image on its own line | 🖼️ Floated right when small, full width when wide | Size decides; no codes |
| An image, then a list of `**Label** (colour): text` | 🎯 Screenshot with hover areas | Matches the coloured areas in the screenshot |
| `*Shared section: [Quick menu](…)*` | ♻️ The shared section, filled in | Add it with the **Shared sections** field |
| A YouTube link alone on a line | 🎬 Video | Or the **Chapter video** field |
| A heading named like a tool (`### Bevel`) | 🧰 Tool card | Name, icon, tooltip and hotkey come from Bforartists |
| A table | 📋 Table | Scrolls sideways on phones |

## 📄 The page header (front matter)

Pages CMS shows this as a form. Fields marked read-only are set by the converter and the build.

```yaml
---
id: "getting-started.installation"     # read-only: stable page ID
title: "Installation"
slug: "installation"                   # read-only: the web address
section: "getting-started"
path: ["Getting Started", "Installation"]
version: "5.1"
status: "draft"                        # draft · needs-review · reviewed
screenshots: "5.1"
video: ""                              # optional chapter video
shared: []                             # shared sections on this page
source: ["2 Installing Bforartists.odt"]   # read-only
---
```

## 🧭 Headings follow the artist route

Page title = the editor or area · `##` object type · `###` mode · `####` area · `#####` panel or menu.
