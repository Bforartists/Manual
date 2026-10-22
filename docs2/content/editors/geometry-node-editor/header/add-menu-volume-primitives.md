---
id: editors.geometry-node-editor.header.add-menu-volume-primitives
title: Add Menu - Volume - Primitives
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Volume - Primitives
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.40 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Primitives.odt
---
## Add menu - Volume - Primitives

![Add menu - Volume - Primitives](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/add-menu-volume-primitives.png)

Here you find nodes to modify the volume.

### Volume Cube

![Volume Cube](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/volume-cube.png)

The Volume Cube node generates a voxel based volume cube primitive that can be used for volume conversion to mesh in conjunction with the Volume to Mesh node.

#### Inputs


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Geometry | Standard geometry input. |
| Density | Volume density per voxel. Higher values makes it more dense. |
| Background | Value per voxel outside the cube domain. |
| Min: | Minimum boundary of the volume cube. Max: Maximum boundary of the volume cube. Resolution X Number of volume voxules in the X axis. Resolution Y Number of volume voxules in the Y axis. Resolution Z Number of volume voxules in the Z axis. |


