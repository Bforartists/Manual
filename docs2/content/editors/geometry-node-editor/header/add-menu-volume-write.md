---
id: editors.geometry-node-editor.header.add-menu-volume-write
title: Add Menu - Volume - Write
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Volume - Write
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.38 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Write.odt
---
## Add menu - Volume

![Add menu - Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/add-menu-volume.png)

Here you find nodes to modify the volume.

### Grid Background

![Grid Background](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/grid-background.png)

Set the background value used for inactive voxels and tiles.

#### Inputs


| Entry | What it does |
| ---------- | ------------------------------------------------------------ |
| Grid | Standard geometry input. |
| Background | Volume density per voxel. Higher values makes it more dense. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/data-type.png)

What data type to calculate.

#### Output

##### Grid

The grid output.

### Set Grid Transform

![Set Grid Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/set-grid-transform.png)

Set the transform for the grid from index space into object space.

#### Inputs


| Entry | What it does |
| --------- | ------------------------ |
| Grid | Standard geometry input. |
| Transform | The input transform. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/data-type.png)

What data type to calculate.

#### Output


| Entry | What it does |
| -------- | --------------------------------------------------------- |
| Is Valid | If the new transform is successfully applied and working. |
| Grid | The grid output. |


### Store Named Grid

![Store Named Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/set-grid-transform.png)

Set the transform for the grid from index space into object space.

#### Inputs


| Entry | What it does |
| ------ | ------------------------ |
| Volume | The volume input. |
| Name | The name |
| Grid | Standard geometry input. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/data-type.png)

What data type to calculate.

#### Output

##### Volume Geometry

The volume geometry to add to.

