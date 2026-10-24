---
id: editors.geometry-node-editor.header.add-menu.instances
title: "Instances"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Instances"
version: "5.1"
status: draft
icon: node
summary: "Instances nodes."
order: 70
cta: "Nodes"
source:
  - "12.1.27 Editors - Geometry Nodes Editor - Header - Add Menu - Instances.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-instances
---
## Add menu - Instances

![Add menu - Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/add-menu-instances.png)

### Instance on Points

![Instance on Points](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instance-on-points.png)

Instances geometry on points.


| Entry | What it does |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Points**: Standard points input. · **Selection**: A selection of the point cloud. · **Instance**: Instance input. · **Pick Instance**: Select an instance of the point cloud. · **Instance Index**: The instance of the index · **Rotation**: The initial rotation. This is a rotation socket. · **Scale**: The initial scale. |
| Output | **Instances**: Instances output. |


### Instances to Points

![Instances to Points](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instances-to-points.png)

This node takes a geometry set with instances as input, and outputs  
points located on the origins of the top level of instances in the  
geometry set (not nested instances). It also has position and radius  
inputs to allow overriding the default, and a selection input to only  
generate points for some instances.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Instances**: Instances input. · **Selection**: A selection of the instance. · **Position**: The position of the instance. · **Radius**: The radius of the points. |
| Output | **Instances**: Points output. |


### Realize Instances

![Realize Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/realize-instances.png)

Makes the instances in the geometry input real. This means each instance becomes its own object with unique mesh data. This node is useful to realize instances either on everything or to a level of instance depth.


| Entry | What it does |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | — |
| Geometry | Geometry Input. |
| Selection | Geometry Input. |
| Realize All | Boolean Input. This realizes all level of nested instances for a top-level realization of instances. This overrides the value of the Depth input. Depth Input Number of levels of nested instances to realize for each top-level instance. **Note:** *Only relevant when Realize All is toggled off.* |
| Outputs | — |
| Geometry | Geometry outputs. |


### Rotate Instances

![Rotate Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/rotate-instances.png)

Rotates the instances of a geometry.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Geometry**: Standard geometry input. · **Selection**: A selection of the geometry. · **Rotation**: The initial rotation. · **Pivot Point**: The pivot point position to rotate around. · **Local Space**: Rotate in world space or in Local Space of the object. |
| Output | **Geometry**: Standard geometry output. |


### Scale Instances

![Scale Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/scale-instances.png)

Rotates the instances of a geometry.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Instances**: Standard geometry input. · **Selection**: A selection of the geometry. · **Scale**: The initial scale. · **Center**: The pivot point position to scale around. · **Local Space**: Rotate in world space or in Local Space of the object. |
| Output | **Geometry**: Standard geometry output. |


### Translate Instances

![Translate Instances](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/translate-instances.png)

Rotates the instances of a geometry.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Inputs | **Instances**: Standard geometry input. · **Selection**: A selection of the geometry. · **Translation**: The amount to move. · **Local Space**: Rotate in world space or in Local Space of the object. |
| Output | **Geometry**: Standard geometry output. |


### Set Instance Transform

![Set Instance Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/set-instance-transform.png)

This node allows replacing the transformation of every instance by providing a matrix.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Instances**: The input instances. · **Selection**: A selection of the geometry. · **Transform**: The transform matrix that you want to apply to every instance. |
| Output | **Instances**: The output instances. |


### Instance Bounds

![Instance Bounds](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instance-bounds.png)

Calculate position bounds of the geometry set of each instance.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Input | **Use Radius**: For curves, point clouds and grease pencil. Take the radius attribute into account when computing the bounds. |
| Output | **Min**: The minimum bounding box dimension. · **Max**: The maximum bounding box dimension. |


### Instance Transform

![Instance Transform](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instance-transform.png)

Retrieves the transform of the instances.

#### Output

##### Transfrom

Transform Field output.

### Instance Rotation

![Instance Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instance-rotation.png)

Retrieves the rotation of the instances.

#### Output

##### Rotation

Vector Field output

### Instance Scale

![Instance Scale](/docs2/images/editors/geometry-node-editor/header/add-menu-instances/instance-scale.png)

Retrieves the scale of an instances.

#### Output

##### Scale

Vector Field output
