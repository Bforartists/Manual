---
id: editors.3d-viewport.tool-shelf.mesh-texture-paint-mode
title: Mesh - Texture Paint Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Tool Shelf
  - Mesh - Texture Paint Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.2.6 Editors - 3D Viewport - Tool Shelf - Mesh - Texture Paint Mode.odt
---
## Tool Shelf - Mesh - Texture Paint Mode

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode.png)

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode-2.png)

In Texture Paint mode with a mesh object you will find mainly brushes in the tool shelf. Texture painting allows you to paint directly onto the texture of the mesh.

![Tool Shelf - Mesh - Texture Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/tool-shelf-mesh-texture-paint-mode-3.png)

Texture painting requires to have a proper UV mapping and a texture at the mesh. When there is no texture at the mesh then the mesh shows pink. And you will get a No Textures message in the tools settings in the Texture Slots panel. You can add a texture paint slot under the tiny little button at the right.

### Transform and Annotate tools

![Transform and Annotate tools](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/transform-and-annotate-tools.png)

The transform and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.  
The transform tools group shows when you activate Paint Mask sub mode.

### Brush cursor

![Brush cursor](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brush-cursor.png)

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush. It does not align with the surface under the mouse. But always faces towards you.

### Brushes settings

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter Tools Tab - Texture Paint Mode

We won't cover this chapters again, but just explain what the different brushes does.

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brushes-settings.png)

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brushes-settings-2.png)

### Symmetry

![Symmetry](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/symmetry.png)

You can enable Symmetry painting up right in the header.

### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/hotkeys.png)

Pressing F allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/hotkeys-2.png)

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

### Brush

The Brush tool covers several paint brushes in the All panel. The names of the brushes are pretty self explaining. The other ones have each their own button in the toolshelf.

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/brush.png)


| Entry | What it does |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Blur | Smooths out the colours of adjacent vertices. In this mode the Colour Value is ignored. The strength defines how much the colours are blurred. |
| Smear | Smears the color under the brush cursor. |
| Clone | Clone a texture area and paint with it. · **Usage**: Hold down Ctrl and click at the source area that you want to draw with. Then draw with left mouse strokes |
| Fill | Fills the whole selection with the chosen color. |


### Mask

![Mask](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/mask.png)

![Mask](/docs2/images/editors/3d-viewport/tool-shelf/mesh-texture-paint-mode/mask-2.png)

Mask out mesh parts by painting these areas with the mask color, which is by default black. Masked texture parts won't be painted when you paint over it. Turn off the mask to see the effect.

This tool requires to have a stencil texture. This stencil texture can be created or loaded in the tools tab in the Mask panel.

