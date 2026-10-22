---
id: editors.3d-viewport.header.mesh-vertex-paint-mode-paint-menu
title: Mesh - Vertex Paint mode - Paint menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Header
  - Mesh - Vertex Paint mode - Paint menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.1.17 Editors - 3D Viewport - Header - Mesh - Vertex Paint mode - Paint menu.odt
---
## Vertex paint Mode - Paint Menu

![Vertex paint Mode - Paint Menu](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/vertex-paint-mode-paint-menu.png)

The Paint menu contains tools for vertex painting in Vertex paint mode.


| Entry | What it does |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set Vertex Color | Flood fills the vertex colors with the current vertex color value. · **Affect Alpha**: Set color to completely opaque instead of reusing existing alpha. |
| Smooth Vertex Colors | Smooths out the vertex colors. |


### Dirty Vertex Colors

![Dirty Vertex Colors](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/dirty-vertex-colors.png)

Dirty vertex colors is a special tool for aging meshes. Let's for example imagine we have a relief. Edges that are outstanding are often touched, and tends to become brighter. While areas in the inner side of a relief are not so often touched. And here the relief collects dirt too. So this areas becomes darker.

And that's what the tool simulates. It makes the outer edges brighter, and the inner edges darker. This calculation is somehow similar to Ambient Occlusion. Ambient Occlusion makes corners darker. The dirty tool makes edges brighter too. And it calculates with the vertices. Not Texel positions like AO.

You need to convert this result to a texture to use it in your texturing, as a mask for example. This conversion can be done by baking.

The tessellation of the mesh should not be too high for this operation. Since it calculates the angles of the mesh edges.

#### Last Operator Dirty Vertex Colors

![Last Operator Dirty Vertex Colors](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-dirty-vertex-colors.png)


| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| Blur strength | How strong the result should be blurred |
| Blur Iterations | The number of iterations for the blur. |
| Highlight Angle | The angle for the bright areas. Angles higher as this value will not be recognized as an edge to highlight. |
| Dirt Angle | The angle for the dark areas. Angles lower as this value will not be recognized as a corner to darken. |
| Dirt only | Ignore the highlight areas, just calculate the dirt angles. |
| Normalize | Normalize the colors to increase the contrast. |


### Vertex Color from Weight

![Vertex Color from Weight](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/vertex-color-from-weight.png)

This tool requires to have Weight Painting at the mesh. It converts the weight paint colors into greyscale vertex colors.

### Invert

Inverts the vertex colors.

### Levels

This tool allows you to level the values of the vertex painting. You adjust the settings in the last operator.

#### Last Operator Vertex Paint Levels

![Last Operator Vertex Paint Levels](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-vertex-paint-levels.png)


| Entry | What it does |
| ------ | --------------------------------------- |
| Offset | Adjust the Offset of the vertex colors. |
| Gain | Adjust the Gain of the vertex colors. |


### Hue Saturation Value

![Hue Saturation Value](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/hue-saturation-value.png)

This tool allows you to adjust the hue, saturation and value values of the vertex painting. You adjust the settings in the last operator.

#### Last Operator Vertex Paint Hue Saturation Value


| Entry | What it does |
| ---------- | ------------------------------------------- |
| Hue | Adjust the Hue of the vertex colors. |
| Saturation | Adjust the Saturation of the vertex colors. |
| Value | Adjust the Value of the vertex colors. |


### Brightness / Contrast

This tool allows you to adjust the brightness and the contrast of the vertex painting. You adjust the settings in the last operator.

#### Last Operator Vertex Paint Brightness/Contrast

![Last Operator Vertex Paint Brightness/Contrast](/docs2/images/editors/3d-viewport/header/mesh-vertex-paint-mode-paint-menu/last-operator-vertex-paint-brightness-contrast.png)


| Entry | What it does |
| ---------- | ------------------------------------------- |
| Brightness | Adjust the brightness of the vertex colors. |
| Contrast | Adjust the contrast of the vertex colors. |


