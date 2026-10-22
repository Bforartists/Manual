---
id: editors.geometry-node-editor.header.add-menu-geometry
title: Add Menu - Geometry
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.17 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry.odt
---
## Add menu - Geometry

![Add menu - Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry/add-menu-geometry.png)

Here you find nodes to modify the geometry.

### Geometry to Instance

![Geometry to Instance](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry/geometry-to-instance.png)

Turns every connected input geometry into an instance. These instances can then for example be used in the Instance on Points node.


| Entry | What it does |
| ------- | ------------------------------------ |
| Inputs | **Geometry**: The input geometry. |
| Outputs | **Instances**: The output instances. |


### Join Geometry

![Join Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry/join-geometry.png)

The Join Geometry enables you to merge separately generated pieces of geometry into a single one. In case that the inputted pieces contain different types of geometry, the output will contain multiple types of geometry.


| Entry | What it does |
| ------ | --------------------------------------- |
| Inputs | **Geometry**: Standard geometry input. |
| Output | **Geometry**: Standard geometry output. |


