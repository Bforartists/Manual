---
id: editors.geometry-node-editor.header.add-menu-volume-operations
title: Add Menu - Volume - Operations
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Volume - Operations
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.39 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Operations.odt
---
## Add menu - Volume - Operations

![Add menu - Volume - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/add-menu-volume-operations.png)

Here you find nodes to modify the volume.

### Grid to Mesh

![Grid to Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/grid-to-mesh.png)

Generate a mesh on the surface of a volume grid.


| Entry | What it does |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Grid**: Standard grid input. · **Threshold**: Values larger than the threshold are inside the generated mesh. · **Adaptivity**: The input radius |
| Output | **Mesh**: The generated mesh. |


### Volume to Mesh

![Volume to Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/volume-to-mesh.png)

The Volume to Mesh node generates a mesh on the “surface” of a volume. The surface is defined by a threshold value. All voxels with a larger value than the threshold are considered to be outside.  
  
Note that currently this node only works on volumes generated using geometry nodes.

#### Inputs

##### Volume

Standard geometry input.

##### Resolution

![Resolution](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/resolution.png)

Base the voxel resolution at the gridsize, the amount or the size of the point cloud.


| Entry | What it does |
| ---------- | ------------------------ |
| Threshold | The voxel amount to use. |
| Adaptivity | The input radius. |


#### Output

##### Mesh

The generated mesh.

### SDF Grid Boolean

![SDF Grid Boolean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-boolean.png)

Bool multiple sdf grids with each other.


| Entry | What it does |
| ---------- | --------------------------------------------------------------------- |
| Inputs | **Grid 1**: The first input grid. · **Grid 2**: The second input grid |
| Properties | **Operation**: The bool method. |
| Output | **Grid**: The generated grid. |


### SDF Grid Fillet

![SDF Grid Fillet](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-fillet.png)

Round off concave internal corners in a signed distance field. Only affects areas with negataive principal curvature. This creates smoother transitions between surfaces.


| Entry | What it does |
| ------ | --------------------------------------------------------------------------- |
| Inputs | **Grid**: The input grid. · **Iterations**: How often to run the algorithm. |
| Output | **Grid**: The generated grid. |


### SDF Grid Laplacian

![SDF Grid Laplacian](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-fillet.png)

Apply laplacian flow smoothing to a signed distance field.


| Entry | What it does |
| ------ | --------------------------------------------------------------------------- |
| Inputs | **Grid**: The input grid. · **Iterations**: How often to run the algorithm. |
| Output | **Grid**: The generated grid. |


### SDF Grid Mean

![SDF Grid Mean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-mean.png)

Apply lmean (box) filter smoothing to a signed distance field. Fast separable averaging filter for general smoothing of the distance field.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Grid**: The input grid. · **Width**: Filter kernel radius in voxel. · **Iterations**: How often to run the algorithm. |
| Output | **Grid**: The generated grid. |


### SDF Grid Mean

![SDF Grid Mean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-mean-2.png)

Apply mean filter smoothing to a signed distance field. Evolves the surface based on its mean curvature. This smooths high curvature regions more than flat areas.


| Entry | What it does |
| ------ | --------------------------------------------------------------------------- |
| Inputs | **Grid**: The input grid. · **Iterations**: How often to run the algorithm. |
| Output | **Grid**: The generated grid. |


### SDF Grid Median

![SDF Grid Median](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-median.png)

Apply median filter smoothing to a signed distance field. Reduces nioise while preserving sharp features and edges in the distance field.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Grid**: The input grid. · **Width**: Filter kernel radius in voxel. · **Iterations**: How often to run the algorithm. |
| Output | **Grid**: The generated grid. |


### SDF Grid Offset

![SDF Grid Offset](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-offset.png)

Offset a signed distance field surface by a world space distance. It dilates or erodes while maintaining the signed distance property.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------ |
| Inputs | **Grid**: The input grid. · **Distance**: Object space distance to offset the sdf surface. |
| Output | **Grid**: The generated grid. |


### Field to Grid

![Field to Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/field-to-grid.png)

Create new grids by evaulating new values on an existing volume grid topology.

#### Inputs


| Entry | What it does |
| ---------- | ------------------- |
| Topology | The input topology. |
| Properties | — |


##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/data-type.png)

The data type to evaluate.

#### Output

##### Grid

The generated grid.

### Prune Grid

![Prune Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/prune-grid.png)

Create new grids by evaulating new values on an existing volume grid topology.

#### Inputs

##### Grid

The input grid.

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/mode.png)

How to progress the state.


| Entry | What it does |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Inactive | Turn inactive voxels and tiels into inactive background tiles. |
| Threshold | Turn regioons where all voxels have the same value and active state into inactive background tiles. You will see a threshold slider. |
| SDF | Replace inactive tiles with inactive nodes. |


##### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/data-type.png)

The data type to evaluate.

#### Output

##### Grid

The generated grid.

### Prune Grid

![Prune Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/prune-grid-2.png)

Create new grids by evaulating new values on an existing volume grid topology.

#### Inputs


| Entry | What it does |
| ---------- | --------------- |
| Grid | The input grid. |
| Properties | — |


##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/data-type.png)

The data type to evaluate.

#### Output

##### Grid

The generated grid.

