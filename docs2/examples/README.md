# 🧪 Docs 2.0 example scenes

One `.blend` per chapter, with the same folder structure as `docs2/content/`. Open a scene, make it pretty, and re-shoot the pictures for that chapter.

| Scene | Chapter |
|---|---|
| `assets/geometry-nodes-library/primitives.blend` | Smart Primitives: all 25 assets laid out in a grid, in the `Smart Primitives` collection, plus a camera |
| `assets/geometry-nodes-library/uv.blend` | UV nodes: source objects, applied copies, per-asset gizmo scenes |
| `assets/compositor-library/lenses.blend`, `patterns.blend` | Compositor Library: one scene per asset (example image > asset > output), render 480x300 |

The Smart Primitives scene links the assets from `G_Primitives.blend` in the Geometry Nodes Library, so the asset library must be set up.

## 📐 Rule: every example file can be re-shot by hand

A picture must never depend on the agent that took it. Every example `.blend` therefore holds:

| Needed | Where |
|---|---|
| 🎬 A scene per asset (or per category) | The `.blend` scenes, named `<Category> <Asset>` |
| 📁 A collection with the subject | Inside that scene |
| 🎥 A camera | Exact framing used for the picture |
| 💡 The lighting | Exact lights used (type, energy, rotation) |
| 📝 Viewport settings per capture | Scene custom property `capture` (JSON) plus a `Capture Notes` text datablock |
| 🔁 The capture script | `capture_viewport.py` text datablock (repo copy: `docs2/examples/tools/capture_viewport.py`) |

Also:

- 🚫 No temporary files or scenes. Anything made for a picture is saved into the `.blend` and documented.
- 🎯 The subject is fully in frame, never cropped (gizmos included), and isolated: nothing else in the scene.
- ⚙️ Note preferences that are not stored in the `.blend` (Gizmo Size, Line Width).
- 🖼️ Re-take: open the `.blend`, run `capture_viewport.py` from the Text Editor, then crop and scale as written in the `capture` property.

## 🛠️ Capture scripts (`docs2/examples/tools/`)

| Script | Does |
|---|---|
| `capture_viewport.py` | Viewport pictures of the scenes that have a `capture` property |
| `capture_comp_nodes.py` | Node picture and thumbnail of Compositor Library assets (auto-cropped) |
| `render_comp_examples.py` | Builds the example scenes of Compositor Library assets and renders the "after" picture |
