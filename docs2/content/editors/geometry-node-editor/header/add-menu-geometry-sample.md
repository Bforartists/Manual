---
id: editors.geometry-node-editor.header.add-menu-geometry-sample
title: Add Menu - Geometry - Sample
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry - Sample
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.13 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry - Sample.odt
---
## Add menu - Geometry - Sample

![Add menu - Geometry - Sample](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/add-menu-geometry-sample.png)

Here you find nodes to modify the geometry.

### Geometry Proximity

![Geometry Proximity](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/geometry-proximity.png)

This node finds the closest position on the target for each point in the input geometry.

#### Inputs


| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------------------- |
| Geometry | The target object. |
| Group ID | Is evaluated on the face domain, and splits the input mesh into multiple parts, each with its own id. |
| Sample Position | The position where the computed location is stored. |
| Sample Group ID | Determines in which group the closest nearest surface is detected. |


#### Properties

##### Target Geometry

![Target Geometry](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/target-geometry.png)

The element of the target geometry to calculate the distance from.

#### Outputs


| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------ |
| Position | Closest location on the surface of the target mesh, or the closest point in the target point cloud in Points mode. |
| Distance | Distance from the source position to the closest location in the target. |
| Is Valid | Wether the sampling was successful. It is false when the sampled group is empty. |


### Index of Nearest

![Index of Nearest](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/index-of-nearest.png)

Retreive values from specific geometry elements.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------- |
| Inputs | **Position**: The position of the nearest element. · **Group ID**: The group ID of the nearest element. |
| Outputs | **Index**: The Index of the nearest element. · **Has Neighbor**: Has this element a neighbor. |


### Raycast

![Raycast](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/raycast.png)

This node sends a raycast and retreives data from the hit target.

#### Inputs


| Entry | What it does |
| --------------- | ------------------------------------------------------ |
| Target Geometry | This is actually the source object that sends the ray. |
| Attribute | Attribute input. |


##### Interpolation

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/interpolation.png)

Mapping from the target geometry to hit points.


| Entry | What it does |
| --------------- | --------------------------------- |
| Source Position | Source position input. |
| Ray Direction | A vector 3 for the ray direction. |
| Ray Length | The length of the ray. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/data-type.png)

What data to calculate on hit.

#### Output


| Entry | What it does |
| ------------ | -------------------------------- |
| Is Hit | Has the raycast hit something? |
| Hit Position | The hit position if any. |
| Hit Normal | The normal of the hit point. |
| Hit Distance | The distance of the hit point. |
| Attribute | The attribute of the hit object. |


### Sample Index

![Sample Index](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/sample-index.png)

Retreive values from specific geometry elements.

#### Inputs


| Entry | What it does |
| -------- | ---------------------------------------- |
| Geometry | The source object to take the data from. |
| Value | The value to retreive. |
| Index | The index position of the value. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/data-type-2.png)

The type for the source and result data.

##### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/domain.png)

What kind of data to process.

##### Clamp

Clamp the indices to the size of the attribute domain.

#### Output

##### Value

The output value.

### Sample Nearest

![Sample Nearest](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/sample-nearest.png)

Retreives the element of a geometry closest to a position.

#### Inputs


| Entry | What it does |
| --------------- | ---------------------------------------- |
| Geometry | The source object to take the data from. |
| Sample Position | The position of the source object. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-sample/properties.png)

##### Domain

What data to process.

#### Output

##### Index

The index output.

