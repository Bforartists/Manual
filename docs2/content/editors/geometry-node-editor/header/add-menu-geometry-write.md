---
id: editors.geometry-node-editor.header.add-menu-geometry-write
title: Add Menu - Geometry - Write
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry - Write
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.14 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry - Write.odt
---
## Add menu - Geometry - Write

![Add menu - Geometry - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-write/add-menu-geometry-write.png)

Here you find nodes to modify the geometry.

### Set Geometry Name

![Set Geometry Name](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-write/set-geometry-name.png)

Sets the name of the target geometry.


| Entry | What it does |
| -------- | ----------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Name**: The name that you want to set |
| Outputs | — |
| Geometry | Geometry output. |


### Set ID

![Set ID](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-write/set-id.png)

Sets the ID of the target geometry.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Selection**: Selection input. · **ID**: ID Input |
| Outputs | — |
| Geometry | Geometry output. |


### Set Position

![Set Position](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-write/set-position.png)

The Set Position node controls the location of each point, the same way as controlling the position attribute. If the input geometry contains instances, this node will affect the location of the origin of each instance.

The input node for this data is the Position Node.


| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Geometry**: Geometry input. · **Selection**: Whether or not to change the position of each point or instance. True values mean the position will be changed, false values mean it will remain the same. · **Position**: The new position for selected elements. By default, this is the same as if the Position Node was connected, meaning the node will do nothing. · **Offset**: An optional translation for each point. This is evaluated at the same time as the Position input, meaning that fields evaluated for it will not reflect the changed position. |
| Outputs | — |
| Geometry | Geometry outputs. |


