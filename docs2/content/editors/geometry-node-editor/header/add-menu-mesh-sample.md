---
id: editors.geometry-node-editor.header.add-menu-mesh-sample
title: Add Menu - Mesh - Sample
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - Sample
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.29 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Sample.odt
---
## Add menu - Mesh - Sample

![Add menu - Mesh - Sample](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/add-menu-mesh-sample.png)

Nodes to modify the mesh geometry.

### Sample Nearest Surface

![Sample Nearest Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/sample-nearest-surface.png)

Calculate the interpolated value of a mesh attribute on the closest point of its surface.

#### Inputs


| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| Mesh | Input mesh. |
| Value | The value to calculate. |
| Group ID | Is evaluated on the face domain, and splits the input mesh into multiple parts, each with its own id. |
| Sample Position | The sample position to calculate. |
| Sample Group ID | Determines in which group the closest nearest surface is detected. |


##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/data-type.png)

Which data to calculate.

#### Outputs


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------- |
| Value | The output value. |
| Is Valid | Wether the sampling was successful. It is false when the sampled group is empty. |


### Sample UV Surface

![Sample UV Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/sample-uv-surface.png)

Calculate the interpolated value of a mesh attribute at a UV coordinate.

#### Inputs


| Entry | What it does |
| ------------- | --------------------------------- |
| Mesh | Input mesh. |
| Value | The value to calculate. |
| Source UV Map | The input UV map. |
| Sample UV | The sample position to calculate. |


##### Properties

###### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/data-type.png)

Which data to calculate.

#### Outputs


| Entry | What it does |
| -------- | ------------------------------------------------------------------------ |
| Value | The output value. |
| Is Valid | Wether the node could find a single face to sample at the uv coordinate. |


