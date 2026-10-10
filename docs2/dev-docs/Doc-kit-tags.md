# 🧱 Doc kit tags

Each tag becomes a component on the Webflow docs. Writers type the tag; the build does the rest. 🤖 marks blocks filled from the Bforartists source.

| Block | Type this | Notes |
|---|---|---|
| 💡 Callout | `:::tip` · `:::note` · `:::warn` · `:::imp`, text, then `:::` | One short paragraph |
| 🏷️ Badge | `:badge[New in 5.1]` | Also in front matter: `version`, `status` |
| 🧭 Menu path | `:menu[Properties Editor > Modifiers > Add Modifier > Bevel]` | Icons are added from the menu names |
| ⌨️ Hotkey | `:kbd[Ctrl+Space]` | Use `Ctrl`, `Shift`, `Alt`, `LMB`, `MMB`, `RMB`, `Wheel` |
| 🖼️ Image | `![Alt text](/docs2/images/place/name.png){.right}` | `.right` float, `.thumb` small, `.icon` inline, none = full width |
| 🎯 Hotspots | `:::hotspots{img=…}` then `- **Label** · colour: text` lines, then `:::` | Uses the colour areas in the screenshot; boxes come from the capture script |
| 🧰 Tool card 🤖 | `::tool{id=modifier.bevel}` then `## Does what` / `## How` / `## Why` | Name, icon, tooltip, hotkey come from Bforartists |
| 📋 Property table 🤖 | `::props{rna=BevelModifier fields="width segments"}` | Rows from the extractor; you add "What it changes" |
| 🔁 Loop video | `::loop{src=loops/bevel-amount.mp4}` | Short, no sound |
| ↔️ Compare | `::compare{a=… b=…}` | Blender vs Bforartists |
| 🪜 Step | `::step{n=3 keys="I E"}` + text + `::why` + text | Quick Start paths |
| ♻️ Snippet | `::include{snippet=quick-menu}` | Edit the snippet once, every page updates |

## Front matter

```yaml
---
id: "editors.timeline.header"      # stable, never change after publishing
title: "Timeline header"
section: "editors"
path: ["Editors", "Timeline", "Header"]
version: "5.1"
status: "draft"                    # draft · needs-review · reviewed
screenshots: "5.1"
source: ["17.1.1 Editors - Timeline - Header Tools and Options.odt"]
---
```

## Headings follow the artist route

Page title = the editor or area · `##` object type · `###` mode · `####` area · `#####` panel or menu. Operators become tool cards; properties become table rows.
