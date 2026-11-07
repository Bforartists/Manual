# 🧪 Docs 2.0 example scenes

One `.blend` per chapter, with the same folder structure as `docs2/content/`. Open a scene, make it pretty, and re-shoot the pictures for that chapter.

| Scene | Chapter |
|---|---|
| `assets/geometry-nodes-library/primitives.blend` | Smart Primitives: all 25 assets laid out in a grid, in the `Smart Primitives` collection, plus a camera |
| `assets/geometry-nodes-library/uv.blend` | UV nodes: source objects, applied copies, per-asset gizmo scenes |
| `assets/compositor-library/lenses.blend`, `patterns.blend` | Compositor Library: one scene per asset (example image > asset > output), render 480x300. lenses.blend also has "Example Bokeh" and "Example Fast Defocus": two rows of columns in perspective with glowing lamps and a back wall, Render Layers Image + Depth into the asset (EEVEE, Z pass) |
| `assets/compositor-library/room.blend` (+ `room.png`) | The example room for Compositor pictures: red and green side walls, a back wall with an open door and warm light outside, a gold Suzanne on a pedestal under a spot light, RGB spheres and CMY cubes (scene "Example Room", Cycles 96 samples, AgX, 480x300, Depth and Normal passes). Plus one scene per Utilities / Vector example: room image > Image Coordinates (Normalized) > asset > Map UV (Z set to 1) > output. Utilities examples (Channel Invert, Color Boolean, Float Boolean, Compare Color, Layer Color, Combine CMYK, Separate CMYK) have their own scene, setup and values in the scene property `capture`. "Example Select Color" waits for an asset fix (see its `capture` note) |
| `assets/shader-library/patterns-shapes.blend` | Shader Library: 51 scenes "Example <Name>" (plane with UV > Mapping > asset > Emission), Cycles 16 samples, 480x300, Standard. Each scene has its capture notes in the custom property `capture` |

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
| `capture_comp_nodes.py` | Node picture and thumbnail of Compositor and Shader Library assets (EDITOR = COMPOSITOR or SHADER, auto-cropped) |
| `render_comp_examples.py` | Builds the example scenes of Compositor Library assets and renders the "after" picture |
| `capture_uv_views.py` | 3D views of the Geometry Nodes Library UV assets: UV grid texture, gizmos, tight framing (scenes "UV <Asset>" in uv.blend) |
| `render_shader_examples.py` | Builds the example scenes of Shader Library patterns and shapes and renders the output picture |
