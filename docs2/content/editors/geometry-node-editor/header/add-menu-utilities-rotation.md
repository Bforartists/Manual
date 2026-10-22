---
id: editors.geometry-node-editor.header.add-menu-utilities-rotation
title: Add Menu - Utilities - Rotation
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Utilities - Rotation
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.51 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Rotation.odt
---
## Add menu - Utilities - Rotation

![Add menu - Utilities - Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/add-menu-utilities-rotation.png)

Utility nodes are mainly for mathematical operations.

### Align Rotation to Vector

![Align Rotation to Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/align-rotation-to-vector.png)

Aligns a rotation to a vector.

#### Inputs


| Entry | What it does |
| -------- | -------------------------------------------------- |
| Rotation | The input euler rotation vector. |
| Factor | The factor to align the euler value to the vector. |
| Vector | The vector to align to. |


#### Properties

##### Align Axis

To which axis to align the vector.

##### Pivot

![Pivot](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/pivot.png)

The pivot axis.

#### Output

##### Rotation

The output rotation euler angle.

### Axes to rotation

![Axes to rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/axes-to-rotation.png)

Creates a rotation from a primary and a secondary axis. The axis should be ideally orthogonal.


| Entry | What it does |
| ---------- | --------------------------------------------------------------------------------------------------------------- |
| Inputs | **Primary Axis**: The axis to rotate around. · **Secondary Axis**: The secondary axis that gives the alignment. |
| Properties | **Primary axis**: Which axis to rotate around. · **Secondary Axis**: Which axis to align to. |
| Output | **Rotation**: The output rotation euler angle. |


### Axis Angle to Rotation

![Axis Angle to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/axis-angle-to-rotation.png)

Converts an axis angle to a rotation.


| Entry | What it does |
| ------ | ------------------------------------------------------- |
| Inputs | **Axis**: The input axis. · **Angle**: The input angle. |
| Output | **Rotation**: The output rotation value. |


### Euler to Rotation

![Euler to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/euler-to-rotation.png)

Converts an euler angle to a rotation.


| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Euler**: The input euler angle vector. |
| Output | **Rotation**: The output rotation value. |


### Invert Rotation

![Invert Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/invert-rotation.png)

Inverts a rotation


| Entry | What it does |
| ------ | ---------------------------------------- |
| Inputs | **Rotation**: The input rotation vector. |
| Output | **Rotation**: The output rotation value. |


### Mix Rotation

![Mix Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/mix-rotation.png)

Rotates an euler rotation by another euler rotation.

#### Inputs


| Entry | What it does |
| ------ | ---------------------------------------- |
| Factor | amount of mixing between a and b inputs. |
| A, B | The input. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/properties.png)

##### Data Type

What data to calculate.

#### Outputs

##### Rotation

The euler angle output.

### Rotate Rotation

![Rotate Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotate-rotation.png)

Rotates an euler rotation by another euler rotation.

#### Inputs


| Entry | What it does |
| --------- | ----------------------------------------- |
| Rotation | Use the rotation of an existing geometry. |
| Rotate By | The input rotation. |


#### Properties

##### Rotate Space


| Entry | What it does |
| ------ | -------------------------------- |
| Global | Rotate by the global orientation |
| Local | Rotate by the local orientation |


#### Outputs

##### Rotation

The euler angle output.

### Rotate Vector

![Rotate Vector](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotate-vector.png)

Rotates a vector.


| Entry | What it does |
| ------ | ----------------------------------------------------------------- |
| Inputs | **Vector**: The input vector. · **Rotation**: The input rotation. |
| Output | **Rotation**: The output rotation value. |


### Rotation to Axis Angle

![Rotation to Axis Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-to-axis-angle.png)

Converts a rotation vector to axis angle.


| Entry | What it does |
| ------ | --------------------------------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **Axis**: The axis output. · **Angle**: The angle output. |


### Rotation Euler

![Rotation Euler](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-euler.png)

Converts a rotation vector to an euler angle.


| Entry | What it does |
| ------ | ------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **Euler**: The euler angle. |


### Rotation to Quaternion

![Rotation to Quaternion](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/rotation-to-quaternion.png)

Converts a quaternion to a rotation vector.


| Entry | What it does |
| ------ | ----------------------------------------------------------- |
| Inputs | **Rotation**: The input vector. |
| Output | **W, X, Y, Z**: The single output values of the quaternion. |


### Quaternion to Rotation

![Quaternion to Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-rotation/quaternion-to-rotation.png)

Converts a rotation vector to a quaternion.


| Entry | What it does |
| ------ | ---------------------------------------------------------- |
| Inputs | **W, X, Y, Z**: The single input values of the quaternion. |
| Output | **Rotation**: The output rotation. |


