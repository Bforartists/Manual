---
id: editors.geometry-node-editor.header.add-menu.volume
title: "Volume"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Volume"
version: "5.1"
status: draft
icon: node
summary: "Volume nodes: Read, Sample, Write, Operations, Primitives."
order: 100
cta: "Nodes"
source:
  - "12.1.36 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Read.odt"
  - "12.1.37 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Sample.odt"
  - "12.1.38 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Write.odt"
  - "12.1.39 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Operations.odt"
  - "12.1.40 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Primitives.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-volume-read
  - editors.geometry-node-editor.header.add-menu-volume-sample
  - editors.geometry-node-editor.header.add-menu-volume-write
  - editors.geometry-node-editor.header.add-menu-volume-operations
  - editors.geometry-node-editor.header.add-menu-volume-primitives
---
# Read

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

# Sample

## Add menu - Volume

![Add menu - Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/add-menu-volume.png)

Here you find nodes to modify the volume.

### Sample Grid

![Sample Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Retreive values from the specified volume grid.

#### Inputs


| Entry | What it does |
| -------- | ------------------- |
| Grid | The input grid |
| Position | The position field. |


##### Interpolation

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/interpolation.png)

How to interpolate the values between neighbouring voxels.

#### Input

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

Which data type to calculate.

#### Output

##### Value

The output value.

### Sample Grid Index

![Sample Grid Index](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Retreive values from the specified volume grid.

#### Inputs


| Entry | What it does |
| -------- | ------------------- |
| Grid | The input grid |
| Position | The position field. |


##### Interpolation

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/interpolation.png)

How to interpolate the values between neighbouring voxels.

#### Input

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

Which data type to calculate.

#### Output

##### Value

The output value.

### Advect Grid

![Advect Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Move grid values through a velocity field using numerical integration. Supports multiple intetgration schemes for different accuracy and performance trade-offs.

#### Inputs


| Entry | What it does |
| --------- | ----------------------------------- |
| Grid | The input grid. |
| Velocity | The velocity. |
| Position | The position field. |
| Time step | Time step for advection in seconds. |


##### Integration scheme

![Integration scheme](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/integration-scheme.png)

Numerical integration method for advection.

##### Limiter

![Limiter](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/limiter.png)

Limiting strategy to prevent numerical artifacts.

#### Output

##### Grid

The output grid.

### Grid Curl

![Grid Curl](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-curl.png)

Calculate the magnitude and direction of ciruclation of a directional vector grid.


| Entry | What it does |
| ------ | -------------------------- |
| Inputs | **Grid**: The input grid. |
| Output | **Curl**: The output grid. |


### Grid Divergence

![Grid Divergence](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-divergence.png)

Calculate the flow into and out of each point of a directional vector grid.


| Entry | What it does |
| ------ | -------------------------------- |
| Inputs | **Grid**: The input grid. |
| Output | **Divergence**: The output grid. |


### Grid Gradient

![Grid Gradient](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-gradient.png)

Calculate the direction and magnitude of the change in values of a scalar grid.


| Entry | What it does |
| ------ | ------------------------------ |
| Inputs | **Grid**: The input grid. |
| Output | **Gradient**: The output grid. |


### Grid Laplacian

![Grid Laplacian](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-laplacian.png)

Compute the divergence of the gradient of the input grid.


| Entry | What it does |
| ------ | ------------------------------- |
| Inputs | **Grid**: The input grid. |
| Output | **Laplacian**: The output grid. |

# Write

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

# Operations

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

# Primitives

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
