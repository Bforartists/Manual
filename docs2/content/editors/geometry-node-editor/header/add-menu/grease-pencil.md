---
id: editors.geometry-node-editor.header.add-menu.grease-pencil
title: "Grease Pencil"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Grease Pencil"
version: "5.1"
status: draft
icon: node
summary: "Grease Pencil nodes: Read, Write, Operations."
order: 60
cta: "Nodes"
source:
  - "12.1.24 Editors - Geometry Nodes Editor - Header - Add Menu - Grease Pencil - Read.odt"
  - "12.1.25 Editors - Geometry Nodes Editor - Header - Add Menu - Grease Pencil - Write.odt"
  - "12.1.26 Editors - Geometry Nodes Editor - Header - Add Menu - Grease Pencil - Operations.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-grease-pencil-read
  - editors.geometry-node-editor.header.add-menu-grease-pencil-write
  - editors.geometry-node-editor.header.add-menu-grease-pencil-operations
---
# Read

## Add menu - Grease Pencil - Read

![Add menu - Grease Pencil - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-read/add-menu-grease-pencil-read.png)

Grease pencil nodes.

### Named Layer Selection

![Named Layer Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-read/named-layer-selection.png)

Outputs a selection of a grease pencil layer by its name.


| Entry | What it does |
| ------- | --------------------------------------------------- |
| Inputs | **Name**: The name of the selection. |
| Outputs | **Selection**: The selected grease pencil geometry. |

# Write

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

# Operations

## Add menu - Grease Pencil - Operations

![Add menu - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/add-menu-grease-pencil-operations.png)

Grease Pencil nodes.

### Grease Pencil to Curves

![Grease Pencil to Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/grease-pencil-to-curves.png)

Converts a grease pencil geometry to a curve geometry


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Grease Pencil**: The grease pencil geometry. · **Selection**: A selection of the grease pencil geometry. · **Layers as Instances**: Generate a separate curve instance for every layer. |
| Outputs | **Curves**: Curves output. |


### Merge Layers

![Merge Layers](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/merge-layers.png)

Merge all grease pencil layers into one layer

#### Grease Pencil

![Grease Pencil](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/grease-pencil.png)

The grease pencil geometry.


| Entry | What it does |
| --------- | -------------------------------------------- |
| Selection | A selection of the grease pencil geometry. |
| Group ID | In By Group ID mode. Input a group ID value. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/properties.png)

##### Mode


| Entry | What it does |
| ----------- | -------------------------------------------- |
| By Name | Combine all layers which have the same name. |
| By Group ID | Combine all layers by a provided Group ID. |


#### Outputs

##### Grease Pencil

Grease Pencil geometry output.
