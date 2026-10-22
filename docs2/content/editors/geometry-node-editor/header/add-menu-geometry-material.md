---
id: editors.geometry-node-editor.header.add-menu-geometry-material
title: Add Menu - Geometry - Material
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry - Material
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.15 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry - Material.odt
---
## Add menu - Geometry - Material

![Add menu - Geometry - Material](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/add-menu-geometry-material.png)

Here you find nodes to modify the material.

### Replace Material.

![Replace Material.](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/replace-material.png)

Sets the name of the target geometry.


| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Old**: The material that you want to replace. · **New**: The new material that replaces the old material. |
| Outputs | — |
| Geometry | Geometry output. |


### Material Index

![Material Index](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/material-index.png)

Retreive the material index.


| Entry | What it does |
| -------------- | ------------------- |
| Outputs | — |
| Material Index | The material index. |


### Material Selection

![Material Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/material-selection.png)

Select a mesh part by material.


| Entry | What it does |
| -------------- | ----------------------------- |
| Inputs | **Geometry**: Geometry input. |
| Outputs | — |
| Material Index | The material index. |


### Set Material

![Set Material](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/set-material.png)

Assign a material to a selection.


| Entry | What it does |
| -------- | --------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Selection**: The selection of the geometry. · **Material**: The material to assign. |
| Outputs | — |
| Geometry | The geometry with the new material assigned. |


### Set Material Index

![Set Material Index](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-material/set-material.png)

Set the material index of a selection.


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Selection**: The selection of the geometry. · **Material Index**: The material index to assign to the selection. |
| Outputs | — |
| Geometry | The geometry with the new material index assigned. |


