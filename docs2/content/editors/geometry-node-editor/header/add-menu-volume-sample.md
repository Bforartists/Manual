---
id: editors.geometry-node-editor.header.add-menu-volume-sample
title: Add Menu - Volume - Sample
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Volume - Sample
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.37 Editors - Geometry Nodes Editor - Header - Add Menu - Volume - Sample.odt
---
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


