---
id: editors.geometry-node-editor.header.add-menu-curve-write
title: Add Menu - Curve - Write
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Curve - Write
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.20 Editors - Geometry Nodes Editor - Header - Add Menu - Curve - Write.odt
---
## Add - Curve - Write

![Add - Curve - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/add-curve-write.png)

Here you find curve related nodes.

### Set Curve Normal

![Set Curve Normal](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-curve-normal.png)

Set the evaluation mode for curve normals.

#### Input


| Entry | What it does |
| --------- | ------------------------------- |
| Curve | The input curve. |
| Selection | A selection of the input curve. |


##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/mode.png)

The evaluation mode for the curve normals.

#### Outputs

##### Curve

The curve output.

### Set Curve Radius

![Set Curve Radius](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-curve-radius.png)

Set the curve radius.


| Entry | What it does |
| ------- | ---------------------------------------------------------------------------------------------------------------- |
| Input | **Geometry**: The input curve. · **Selection**: A selection of the input curve. · **Radius**: The radius to set. |
| Outputs | **Geometry**: Standard geometry output. |


### Set Curve Tilt

![Set Curve Tilt](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-curve-tilt.png)

Controls the tilt angle at each curve control point.


| Entry | What it does |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Geometry**: The input curve. · **Selection**: Whether or not to change the value on each control point. True values mean the value will be changed, false values mean the value will remain the same. · **Tilt**: The tilt rotation. |
| Outputs | **Curve**: Standard geometry output. |


### Set Handle Positions

![Set Handle Positions](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-handle-positions.png)

Set the handle positions of bezier curves


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Geometry**: The input curve. · **Selection**: A selection of the input curve. · **Position**: The position of the handle. · **Offset**: A vector 3 offset for the handles. |
| Properties | **Mode**: Left or right handles. |
| Outputs | **Geometry**: Standard geometry output. |


### Set Handle Type

![Set Handle Type](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-handle-type.png)

Sets a handle type for the curve points of a bezier curve. Handle types determines how the interpolation before and after the curve point happens.

#### Input


| Entry | What it does |
| --------- | ------------------------------- |
| Curve | The input curve. |
| Selection | A selection of the input curve. |


#### Properties

##### Mode

Left or right handles.

##### Handle Type

![Handle Type](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-read/handle-type.png)

The different available handle types.

###### Free

![Free](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/free.png)

The handles can be adjusted individually.

###### Auto

![Auto](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/auto.png)

The left and the right handle will always point to each other. The length of the handles will start in equal size.

###### Vector

![Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/vector.png)

The handles can be adjusted individually.

###### Aligned

![Aligned](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/aligned.png)

The left and the right handle will always point to each other.

#### Output

##### Curve

Standard geometry output.

### Set Spline cyclic

![Set Spline cyclic](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-spline-cyclic.png)

Sets the spline cyclic. Means looping.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| Input | **Geometry**: The input curve. · **Selection**: A selection of the input curve. · **Cyclic**: Cyclic or not |
| Outputs | **Geometry**: Standard geometry output. |


### Set Spline Resolution

![Set Spline Resolution](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-spline-resolution.png)

Sets the resolution of the spline. Means how many evaluated points should be generated on the curve for each control point.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Geometry**: The input curve. · **Selection**: A selection of the input curve. · **Resolution**: The resolution of the spline. |
| Outputs | **Geometry**: Standard geometry output. |


### Set Spline Type

![Set Spline Type](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/set-spline-type.png)

Change the curve spline type.

#### Input


| Entry | What it does |
| --------- | ------------------------------- |
| Curve | The input curve. |
| Selection | A selection of the input curve. |


#### Properties

##### Spline Type

![Spline Type](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-write/spline-type.png)

The spline type to set the curve to.

Note that when converting from a NURBS spline to a Bézier spline, at least six points are needed. When the number of points is not a multiple of three a full conversion is not possible and the spline has to be truncated.

#### Output

##### Curve

Standard geometry output.

