---
id: editors.geometry-node-editor.header.add-menu-utilities-deprecated
title: Add Menu - Utilities - Deprecated
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Utilities - Deprecated
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.52 Editors - Geometry Nodes Editor - Header - Add Menu - Utilities - Deprecated.odt
---
## Add menu - Deprecated

![Add menu - Deprecated](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/add-menu-deprecated.png)

These deprecated nodes are kept for compatibility reasons.

### Align Euler to Vector (Deprecated)

![Align Euler to Vector (Deprecated)](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/align-euler-to-vector-deprecated.png)

Aligns a euler value to a vector.

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

### Rotate Euler (Deprecated)

![Rotate Euler (Deprecated)](/docs2/images/editors/geometry-node-editor/header/add-menu-utilities-deprecated/rotate-euler-deprecated.png)

Rotates an euler rotation. This node will be removed in the near future. Alternatively use the Rotate Rotation node.

#### Inputs


| Entry | What it does |
| --------- | ----------------------------------------- |
| Rotation | Use the rotation of an existing geometry. |
| Rotate By | The input rotation. |


#### Properties


| Entry | What it does |
| ------------ | --------------------------------------------------------------------------------------------------------------- |
| Rotate Type | **Axis Angle**: Rotate around an axis by an angle. · **Euler**: Rotate around the x, y and z axis. |
| Rotate Space | **Object**: Rotate points in the local space of the object. · **Point**: Rotate every point in its local space. |


#### Outputs

##### Rotation

The euler angle output.

