---
id: editors.geometry-node-editor.header.add-menu-grease-pencil-write
title: Add Menu - Grease Pencil - Write
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Grease Pencil - Write
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.25 Editors - Geometry Nodes Editor - Header - Add Menu - Grease Pencil - Write.odt
---
## Add menu - Grease Pencil - Write

![Add menu - Grease Pencil - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/add-menu-grease-pencil-write.png)

Grease pencil nodes.

### Set Grease Pencil Color

![Set Grease Pencil Color](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/set-grease-pencil-color.png)

Sets the color and opacity of a grease pencil geometry.

#### Inputs


| Entry | What it does |
| ------------- | ------------------------------------------ |
| Grease Pencil | The grease pencil geometry. |
| Selection | A selection of the grease pencil geometry. |
| Color | The color. |
| Opacity | The opacity. |


#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/mode.png)


| Entry | What it does |
| ------ | ------------------------ |
| Fill | Change the fill color. |
| Stroke | Change the stroke color. |


#### Outputs

##### Color

The grease pencil output with changed colors.

### Set Grease Pencil Depth

![Set Grease Pencil Depth](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/set-grease-pencil-depth.png)

Set the grease pencil depth order to use. By 2d layers, or by the position in 3d space.

#### Inputs

##### Grease Pencil

The grease pencil geometry.

#### Properties

##### Depth Order

![Depth Order](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/depth-order.png)


| Entry | What it does |
| ----------- | ------------------------------------------------------- |
| 2D Layers | Set the grease pencil depth by the 2d layers. |
| 3D Location | Set the grease pencil depth by the postion in 3d space. |


#### Outputs

##### Grease Pencil

The grease pencil geometry.

### Set Grease Pencil Softness

![Set Grease Pencil Softness](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-write/set-grease-pencil-softness.png)

Adjust the falloff towards the stoke border.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Grease Pencil**: The grease pencil geometry. · **Selection**: A selection of the grease pencil geometry. · **Softness**: The falloff softness. A value of 1 means sharp border. A falloff of 0 means a falloff from the center to the border with a complete transparency at the border. |
| Outputs | **Grease Pencil**: The grease pencil geometry. |


