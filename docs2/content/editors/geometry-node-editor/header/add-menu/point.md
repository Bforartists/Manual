---
id: editors.geometry-node-editor.header.add-menu.point
title: "Point"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Point"
version: "5.1"
status: draft
icon: node
summary: "Point nodes."
order: 90
cta: "Nodes"
source:
  - "12.1.35 Editors - Geometry Nodes Editor - Header - Add Menu - Point.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-point
---
## Add menu - Point

![Add menu - Point](/docs2/images/editors/geometry-node-editor/header/add-menu-point/add-menu-point.png)

### Distribute Points In Grid

![Distribute Points In Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribute-points-in-grid.png)

Distributes points randomly in a grid.

Point, corner and polygon attributes of the input geometry are transferred to the generated points. That includes vertex weights and UV maps. Additionally, the node has Normal and Rotation outputs.

The node also generates a stable ID, which is then stored in the built-in id attribute. It is used as a stable identifier for each point. When the geoemetry is deformed or the density changes the values will be consistent for each remaining point. This attribute is used in the Random Value and Instance on Points nodes.

#### Inputs Random mode

![Inputs Random mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-random-mode.png)


| Entry | What it does |
| ------- | ------------------------------------------- |
| Grid | The grid to import the points to. |
| Density | Density of the points. |
| Seed | The random seed for the point distribution. |


#### Inputs Grid mode

![Inputs Grid mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-grid-mode.png)


| Entry | What it does |
| --------- | --------------------------------------------------------- |
| Grid | The grid to import the points to. |
| Spacing | The spacing between the grid points. |
| Threshold | Minimum density of a volume cell to contain a grid point. |


#### Properties

##### Distribution method

![Distribution method](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribution-method.png)


| Entry | What it does |
| ------ | ---------------------------------------------------------- |
| Random | Distributes the points randomly. This allows overlappings. |
| Grid | Distributes the points along a grid with given width. |


#### Output

##### Points

Points output.

### Distribute Points In Volume

![Distribute Points In Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribute-points-in-volume.png)

Distributes points randomly in a volume.

Point, corner and polygon attributes of the input geometry are transferred to the generated points. That includes vertex weights and UV maps. Additionally, the node has Normal and Rotation outputs.

The node also generates a stable ID, which is then stored in the built-in id attribute. It is used as a stable identifier for each point. When the geoemetry is deformed or the density changes the values will be consistent for each remaining point. This attribute is used in the Random Value and Instance on Points nodes.

#### Inputs Random mode

![Inputs Random mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-random-mode-2.png)


| Entry | What it does |
| ------- | ------------------------------------------- |
| Volume | The volume to import the points to. |
| Density | Density of the points. |
| Seed | The random seed for the point distribution. |


#### Inputs Grid mode

![Inputs Grid mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-grid-mode-2.png)


| Entry | What it does |
| --------- | --------------------------------------------------------- |
| Volume | The volume to import the points to. |
| Spacing | The spacing between the grid points. |
| Threshold | Minimum density of a volume cell to contain a grid point. |


#### Properties

##### Distribution method

![Distribution method](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribution-method.png)


| Entry | What it does |
| ------ | ---------------------------------------------------------- |
| Random | Distributes the points randomly. This allows overlappings. |
| Grid | Distributes the points along a grid with given width. |


#### Output

##### Points

Points output.

### Distribute Points on Faces

![Distribute Points on Faces](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribute-points-on-faces.png)

Distributes points randomly on the faces of a mesh geometry.

Point, corner and polygon attributes of the input geometry are transferred to the generated points. That includes vertex weights and UV maps. Additionally, the node has Normal and Rotation outputs.

The node also generates a stable ID, which is then stored in the built-in id attribute. It is used as a stable identifier for each point. When the mesh is deformed or the density changes the values will be consistent for each remaining point. This attribute is used in the Random Value and Instance on Points nodes.

#### Inputs Random mode

![Inputs Random mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-random-mode-3.png)


| Entry | What it does |
| --------- | -------------------------------------------------------------------------------- |
| Mesh | Standard geometry input. |
| Selection | The selection of which face corners should be considered for point distribution. |
| Density | Density of the points. |
| Seed | The random seed for the point distribution. |


#### Inputs Poisson Disk mode

![Inputs Poisson Disk mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/inputs-poisson-disk-mode.png)


| Entry | What it does |
| -------------- | -------------------------------------------------------------------------------- |
| Mesh | Standard geometry input. |
| Selection | The selection of which face corners should be considered for point distribution. |
| Distance Min | The minimum distance that two points can have. |
| Distance Max | The naximum distance that two points can have. |
| Density Factor | Density of the points. |
| Seed | The random seed for the point distribution. |


#### Properties

##### Distribution method

![Distribution method](/docs2/images/editors/geometry-node-editor/header/add-menu-point/distribution-method-2.png)


| Entry | What it does |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| Random | Distributes the points randomly. This allows overlappings. |
| Poisson Disk | Distributes the points randomly, but prevents overlappings by defining a minimum and maximum distance. |


#### Output


| Entry | What it does |
| ------ | -------------- |
| Points | Points output. |
| Normal | Normal output. |


##### Rotation

Euler Rotation output. Please note that the Z axis of the result rotation will be arbitrary. The mesh normal used to create the rotation does not have enough information to set all three rotation axes.

![Rotation](/docs2/images/editors/geometry-node-editor/header/add-menu-point/rotation.png)

### Points

Generates a single point or points with position, count and radius.

#### Inputs

##### Count

The count of the generated points as an integer.

Position

The position of the points as a vector. This is a field meaning you can set the position per index or ID of the point.

Radius

The radius of the points as a float. This is a field meaning you can set the scale per index or ID of the point.

#### Outputs

##### Mesh

Standard mesh output.

### Points to Cuves

![Points to Cuves](/docs2/images/editors/geometry-node-editor/header/add-menu-point/points-to-cuves.png)

Generates a mesh vertex in the output geometry for each point cloud point in the input geometry.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Points**: Points input. · **Curve Group ID**: A curve is created from every distinct group ID. All points with the same ID are put into the same curve. · **Selection**: Selection input. |
| Outputs | **Mesh**: Standard mesh output. |


### Points to SDF Grid

![Points to SDF Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-point/points-to-sdf-grid.png)

Generates a mesh vertex in the output geometry for each point cloud point in the input geometry.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------- |
| Inputs | **Points**: Points input. · **Radius**: The radius of the grid. · **Voxel size**: The voxel size of the grid. |
| Outputs | **SDF Grid**: Standard mesh output. |


### Points to Vertices

![Points to Vertices](/docs2/images/editors/geometry-node-editor/header/add-menu-point/points-to-vertices.png)

Generates a mesh vertex in the output geometry for each point cloud point in the input geometry.


| Entry | What it does |
| ------- | ----------------------------------------------------------- |
| Inputs | **Points**: Points input. · **Selection**: Selection input. |
| Outputs | **Mesh**: Standard mesh output. |


### Points to Volume

![Points to Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-point/points-to-volume.png)

Creates a fog volume sphere around every point in the input geometry. The new volume grid is then called density.

#### Inputs


| Entry | What it does |
| ------- | -------------------------- |
| Points | Points input. |
| Density | The density of the volume. |


##### Resolution Mode

![Resolution Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-point/resolution-mode.png)

Base the voxel resolution at the amount or the size of the point cloud.


| Entry | What it does |
| ------------ | ----------------------------------------------------- |
| Voxel Amount | Voxel amount of the volume. |
| Radius | The radius of the generated volume around each point. |


#### Outputs

##### Volume

Standard geometry output.

### Rasterize Points

![Rasterize Points](/docs2/images/editors/geometry-node-editor/header/add-menu-point/rasterize-points.png)

Turns points into volume grids. Each point adds its values to the voxels around it with a weighted sum. The Kernel Type decides how far a point reaches and how the weight falls off.

You choose what to rasterize by adding items. Each item has a name and a type. It gives the node one input for the value of each point, and one grid output with the same name. To add an item, connect a link to the empty socket at the bottom of the node, or use the Items panel in the Node tab of the sidebar.

#### Inputs

##### Points

The geometry to rasterize. The points of meshes, point clouds and curves are used.

##### Grid Transform Mode

How the transform of the new grids is set.

- Voxel Size: all grids use a uniform voxel size, without any move or rotation. This is the default.
- Matrix: you set the transform of the grids with a matrix.

##### Voxel Size

The size of one voxel. The default is 0.3 m, the minimum is 0.01. It is only shown for Voxel Size.

##### Matrix

The transform of the grids. It is only shown for Matrix. If the matrix is not valid for a grid, no grids are created.

##### Kernel Type

How the weight of a point is spread over the voxels.

- Constant: the point only goes to the closest voxel.
- Linear: the weight falls off linearly over the voxel range. This is the default.
- Quadratic B-Spline: a quadratic B-spline kernel over 1.5 voxels.
- Cubic B-Spline: a cubic B-spline kernel over 2 voxels.

##### Position

A field with the position of each point. By default it is the position of the point.

##### Items

For each item you add, there is an input with its name. It is a field that gives the value to rasterize for each point.

#### Properties

##### Items

The Items panel in the Node tab of the sidebar lists the items. You can add, remove and move items there.

##### Type

The type of the active item. Scalar rasterizes a single number for each point. Vector rasterizes a vector for each point.

#### Outputs

##### Items

For each item there is a grid output with the same name as the item. A scalar item gives a scalar grid, a vector item gives a vector grid. If a grid cannot be made, the node shows a warning with the name of the item.

### Set Point Radius

![Set Point Radius](/docs2/images/editors/geometry-node-editor/header/add-menu-point/set-point-radius.png)

The Set Point Radius node controls the size each selected point cloud point should display with in the viewport.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------- |
| Inputs | **Points**: Geometry input. · **Selection**: Selection input. · **Radius**: The radius of the points. |
| Outputs | **Points**: Standard geometry output. |

### Set Point Cloud Type

![Set Point Cloud Type](/docs2/images/editors/geometry-node-editor/header/add-menu-point/set-point-cloud-type.png)

Changes how a point cloud is represented. Use it to show the points of a point cloud as 3D Gaussian Splats, or to turn them back into simple points. The points themselves are not changed.

#### Inputs

##### Points

The point cloud to change the type of. Point clouds inside instances are changed too.

##### Type

The new type of the point cloud.

- Points: a simple point cloud with a position and a radius for each point. This is the default.
- 3D Gaussian Splat: a point cloud that works as the original 3D Gaussian Splats technique.

#### Outputs

##### Points

The geometry with the new point cloud type.
