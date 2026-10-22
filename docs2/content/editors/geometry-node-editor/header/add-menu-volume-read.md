---
id: editors.geometry-node-editor.header.add-menu-volume-read
title: Add Menu - Volume - Read
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Volume - Read
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.36 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Read.odt
---
## Add menu - Volume - Read

![Add menu - Volume - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/add-menu-volume-read.png)

Here you find nodes to modify the volume.

### Get Named Grid

![Get Named Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/get-named-grid.png)

Get volume grid from a volume geometry with the specified name

#### Inputs


| Entry | What it does |
| ------ | ------------------------------------------------ |
| Volume | The input volume. |
| Name | The name of the grid. |
| Remove | Removes the grid from the volume after retreive. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type.png)

The type of data stored in the grid. It determines both, the expected data type of the **Grid** output, and how it can be used in subsequent nodes.

#### Output


| Entry | What it does |
| ------ | ------------------- |
| Volume | The output grid. |
| Grid | The extracted grid. |


### Grid Info

![Grid Info](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/grid-info.png)

Retreive informations about a grid.

#### Inputs

##### Grid

Standard geometry input.

#### Properties

##### Data type

![Data type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

The data type to retreive.

#### Output


| Entry | What it does |
| ---------------- | ------------------------------------------------ |
| Transform | Transform from grid index space to object space. |
| Background Value | Default value outside of grid voxels. |


### Voxel Index

![Voxel Index](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/voxel-index.png)

Retreive the integer coordinates of the voxel that the field is evaluated on.

#### Outputs


| Entry | What it does |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| X / Y / Z | Vector 3 output of the voxel. |
| Tile subpanel | **Is Tile**: True when the field is evaluated on a tile. · **Extend X / Y / Z**: Number of voxels in the corresponding direction. Or 1 if the field is evaluated at a voxel. |


