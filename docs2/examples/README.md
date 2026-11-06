# 🧪 Docs 2.0 example scenes

One `.blend` per chapter, with the same folder structure as `docs2/content/`. Open a scene, make it pretty, and re-shoot the pictures for that chapter.

| Scene | Chapter |
|---|---|
| `assets/geometry-nodes-library/primitives.blend` | Smart Primitives: all 25 assets laid out in a grid, in the `Smart Primitives` collection, plus a camera |

| `assets/geometry-nodes-library/uv.blend` | UV nodes: source objects, applied copies, per-asset gizmo scenes |
| `assets/compositor-library/lenses.blend`, `patterns.blend` | Compositor Library: one scene per asset (example image > asset > output), render 480x300 |

The Smart Primitives scene links the assets from `G_Primitives.blend` in the Geometry Nodes Library, so the asset library must be set up.

## 🛠️ Capture scripts (`docs2/examples/tools/`)

| Script | Does |
|---|---|
| `capture_viewport.py` | Viewport pictures of the scenes that have a `capture` property |
| `capture_comp_nodes.py` | Node picture and thumbnail of Compositor Library assets (auto-cropped) |
| `render_comp_examples.py` | Builds the example scenes of Compositor Library assets and renders the "after" picture |
