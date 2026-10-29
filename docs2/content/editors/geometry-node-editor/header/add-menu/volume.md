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
status: needs-review
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

### Get Grid Names

![Get Grid Names](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/get-grid-names.png)

Lists the names of all grids stored in a volume. Use it to see what a volume contains, for example before you pick a grid with Get Named Grid.

#### Inputs

##### Volume

Data type: Geometry.

The volume to list the grid names of.

#### Outputs

##### Names

Data type: String.

A list of the names of all grids in the volume, sorted alphabetically. If the geometry has no volume, the list is empty.

### Get Named Grid

![Get Named Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/get-named-grid.png)

Get volume grid from a volume geometry with the specified name

### Inputs

#### Volume

The input volume.

#### Name

The name of the grid.

#### Remove

Removes the grid from the volume after retreive.



#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type.png)

The type of data stored in the grid. It determines both, the expected data type of the **Grid** output, and how it can be used in subsequent nodes.

#### Output

##### Volume

The output grid.

##### Grid

The extracted grid.



### Grid Info

![Grid Info](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/grid-info.png)

Retreive informations about a grid.

#### Inputs

##### Grid

Data type: Float.

Standard geometry input.

#### Properties

##### Data type

![Data type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

The data type to retreive.

#### Output

##### Transform

Data type: Matrix.

Transform from grid index space to object space.

##### Background Value

Data type: Float.

Default value outside of grid voxels.



### Voxel Index

![Voxel Index](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/voxel-index.png)

Retreive the integer coordinates of the voxel that the field is evaluated on.

#### Outputs

##### X / Y / Z

Vector 3 output of the voxel.

##### Tile subpanel

###### Is Tile

True when the field is evaluated on a tile.

###### Extend X / Y / Z

Number of voxels in the corresponding direction. Or 1 if the field is evaluated at a voxel.


# Sample

## Add menu - Volume

![Add menu - Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/add-menu-volume.png)

Here you find nodes to modify the volume.

### Sample Grid

![Sample Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Retreive values from the specified volume grid.

#### Inputs

##### Grid

Data type: Float.

The input grid

##### Position

Data type: Vector.

The position field.



##### Interpolation

Data type: Menu.

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/interpolation.png)

How to interpolate the values between neighbouring voxels.

#### Input

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

Which data type to calculate.

#### Output

##### Value

Data type: Float.

The output value.

### Sample Grid Index

![Sample Grid Index](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Retreive values from the specified volume grid.

#### Inputs

##### Grid

Data type: Float.

The input grid

##### Position

The position field.



##### Interpolation

![Interpolation](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/interpolation.png)

How to interpolate the values between neighbouring voxels.

#### Input

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-read/data-type-2.png)

Which data type to calculate.

#### Output

##### Value

Data type: Float.

The output value.

### Advect Grid

![Advect Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/sample-grid.png)

Move grid values through a velocity field using numerical integration. Supports multiple intetgration schemes for different accuracy and performance trade-offs.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Velocity

Data type: Vector.

The velocity.

##### Position

The position field.

##### Time step

Data type: Float (time).

Time step for advection in seconds.



##### Integration scheme

Data type: Menu.

![Integration scheme](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/integration-scheme.png)

Numerical integration method for advection.

##### Limiter

Data type: Menu.

![Limiter](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/limiter.png)

Limiting strategy to prevent numerical artifacts.

#### Output

##### Grid

Data type: Float.

The output grid.

### Grid Curl

![Grid Curl](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-curl.png)

Calculate the magnitude and direction of ciruclation of a directional vector grid.

#### Inputs

##### Grid

Data type: Vector.

The input grid.

#### Outputs

##### Curl

Data type: Vector.

The output grid.



### Grid Divergence

![Grid Divergence](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-divergence.png)

Calculate the flow into and out of each point of a directional vector grid.

#### Inputs

##### Grid

Data type: Vector.

The input grid.

#### Outputs

##### Divergence

Data type: Float.

The output grid.



### Grid Gradient

![Grid Gradient](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-gradient.png)

Calculate the direction and magnitude of the change in values of a scalar grid.

#### Inputs

##### Grid

Data type: Float.

The input grid.

#### Outputs

##### Gradient

Data type: Vector.

The output grid.



### Grid Laplacian

![Grid Laplacian](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-laplacian.png)

Compute the divergence of the gradient of the input grid.

#### Inputs

##### Grid

Data type: Float.

The input grid.

#### Outputs

##### Laplacian

Data type: Float.

The output grid.


#### Grid Solve Poisson

![Grid Solve Poisson](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-sample/grid-solve-poisson.png)

Solves the Poisson equation for a scalar grid. It computes a grid whose Laplacian is the input grid. Use the boundary settings to say what happens at the edge of the active voxels.

The solver works on grids with the same voxel size in all directions. If the voxel size is not uniform, the node shows a warning.

##### Inputs

###### Grid

The scalar grid on the right-hand side of the equation.

###### Max Iterations

The most steps the solver may take. The default is 100. The value can be 1 to 10000.

###### Error Threshold

The solver stops when the error is below this value. The default is 0.001.

###### Threshold Mode

How the error threshold is measured.

- Relative: the error is measured relative to the largest absolute value of the input grid. This is the default.
- Absolute: the error is measured as an absolute value in the units of the solution.

###### Boundary

What happens at the boundary between active and inactive voxels.

- Fixed: you set the value of the solution for the voxels just outside the active ones. This is the default.
- Gradient: you set the gradient of the solution at the boundary.
- Mixed: you set both and blend between them with Boundary Factor.

###### Boundary Value

The value of the solution at the boundary. It is a field, so it can change from voxel to voxel. It is only shown for Fixed and Mixed.

###### Boundary Gradient

The gradient of the solution at the boundary. It is a field. It is only shown for Gradient and Mixed.

###### Boundary Factor

How much of the gradient is used instead of the value, from 0 to 1. At 0 the value is used, at 1 the gradient. It is a field. It is only shown for Mixed.

##### Outputs

###### Solution

The grid that solves the equation.

###### Success

True if the solver reached the error threshold.

###### Iterations

How many steps the solver took.

###### Absolute Error

The absolute error of the solution at the end.

###### Relative Error

The relative error of the solution at the end.

###### Debug Boundary Value

A panel with three outputs that is closed by default. This one is the grid of boundary values the solver used. It is only shown for Fixed and Mixed.

###### Debug Boundary Gradient

The grid of boundary gradients the solver used. It is only shown for Gradient and Mixed.

###### Debug Boundary Factor

The grid of boundary factors the solver used. It is only shown for Mixed.

# Write

## Add menu - Volume

![Add menu - Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/add-menu-volume.png)

Here you find nodes to modify the volume.

### Grid Background

![Grid Background](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/grid-background.png)

Set the background value used for inactive voxels and tiles.

#### Inputs

##### Grid

Standard geometry input.

##### Background

Volume density per voxel. Higher values makes it more dense.



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

##### Grid

Data type: Float.

Standard geometry input.

##### Transform

Data type: Matrix.

The input transform.



#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/data-type.png)

What data type to calculate.

#### Output

##### Is Valid

Data type: Boolean.

If the new transform is successfully applied and working.

##### Grid

Data type: Float.

The grid output.



### Store Named Grid

![Store Named Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-write/set-grid-transform.png)

Set the transform for the grid from index space into object space.

#### Inputs

##### Volume

Data type: Geometry.

The volume input.

##### Name

Data type: String.

The name

##### Grid

Data type: Float.

Standard geometry input.



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

### Grid Topology Boolean

![Grid Topology Boolean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/grid-topology-boolean.png)

Combines the topology of two grids. The topology of a grid is the set of voxels that are active, in other words the shape of the grid and not the numbers stored in it. With this node you can merge two shapes, keep only where they overlap, or cut one out of the other. Use it to build a region for a simulation out of simple pieces, or to restrict one grid to the region of another.

#### Inputs

##### Operation

Data type: Menu.

How the shapes are combined: **Intersect** keeps the voxels that are active in both grids, **Union** keeps the voxels that are active in either grid and **Difference** keeps the voxels of Grid 1 that are not active in Grid 2.

##### Grid 1

Data type: Float.

The first grid. Its values are used for the result.

##### Grid 2

Data type: Float.

The second grid. Only its shape is used.

#### Outputs

##### Grid

Data type: Float.

The grid with the combined shape.

#### How to use

![Grid Topology Boolean example](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/grid-topology-boolean-chain.png)

The example builds two grids and combines their shapes:

1. Each **Cube Grid Topology** node makes the shape of a box. The first box goes from -1 to 1, the second from 0 to 2.
2. Each **Field to Grid** node fills its shape with values. Here the value is `2 - Length(Position)`, which is high near the center of the world and falls off with distance.
3. **Grid Topology Boolean** combines the two grids. Change **Operation** to see how the result changes.
4. **Grid to Mesh** turns the result into a mesh, so you can see it.

A grid that is filled with one constant value has no surface inside, so Grid to Mesh shows nothing for it. Fill the grids with a value that changes, as in the example, when you want to look at the result as a mesh.

### Grid to Mesh

![Grid to Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/grid-to-mesh.png)

Generate a mesh on the surface of a volume grid.

#### Inputs

##### Grid

Data type: Float.

Standard grid input.

##### Threshold

Data type: Float.

Values larger than the threshold are inside the generated mesh.

##### Adaptivity

Data type: Float (factor).

The input radius

#### Outputs

##### Mesh

Data type: Geometry.

The generated mesh.



### Volume to Mesh

![Volume to Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/volume-to-mesh.png)

The Volume to Mesh node generates a mesh on the “surface” of a volume. The surface is defined by a threshold value. All voxels with a larger value than the threshold are considered to be outside.  
  
Note that currently this node only works on volumes generated using geometry nodes.

#### Inputs

##### Volume

Data type: Geometry.

Standard geometry input.

##### Resolution

![Resolution](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/resolution.png)

Base the voxel resolution at the gridsize, the amount or the size of the point cloud.

###### Threshold

The voxel amount to use.

###### Adaptivity

The input radius.



#### Output

##### Mesh

Data type: Geometry.

The generated mesh.

### SDF Grid Boolean

![SDF Grid Boolean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-boolean.png)

Bool multiple sdf grids with each other.

#### Inputs

##### Grid 1

Data type: Float.

The first input grid.

##### Grid 2

Data type: Float.

The second input grid

#### Properties

##### Operation

The bool method.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Fillet

![SDF Grid Fillet](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-fillet.png)

Round off concave internal corners in a signed distance field. Only affects areas with negataive principal curvature. This creates smoother transitions between surfaces.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Iterations

Data type: Integer.

How often to run the algorithm.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Laplacian

![SDF Grid Laplacian](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-fillet.png)

Apply laplacian flow smoothing to a signed distance field.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Iterations

Data type: Integer.

How often to run the algorithm.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Mean

![SDF Grid Mean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-mean.png)

Apply lmean (box) filter smoothing to a signed distance field. Fast separable averaging filter for general smoothing of the distance field.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Width

Data type: Integer.

Filter kernel radius in voxel.

##### Iterations

Data type: Integer.

How often to run the algorithm.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Mean

![SDF Grid Mean](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-mean-2.png)

Apply mean filter smoothing to a signed distance field. Evolves the surface based on its mean curvature. This smooths high curvature regions more than flat areas.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Iterations

Data type: Integer.

How often to run the algorithm.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Median

![SDF Grid Median](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-median.png)

Apply median filter smoothing to a signed distance field. Reduces nioise while preserving sharp features and edges in the distance field.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Width

Data type: Integer.

Filter kernel radius in voxel.

##### Iterations

Data type: Integer.

How often to run the algorithm.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### SDF Grid Offset

![SDF Grid Offset](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/sdf-grid-offset.png)

Offset a signed distance field surface by a world space distance. It dilates or erodes while maintaining the signed distance property.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Distance

Data type: Float (distance).

Object space distance to offset the sdf surface.

#### Outputs

##### Grid

Data type: Float.

The generated grid.



### Deactivate Voxels

![Deactivate Voxels](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/deactivate-voxels.png)

Turns selected voxels off. A volume grid is built from voxels, and only the active ones are stored and used. Deactivating voxels you do not need makes a grid smaller and faster to work with, and it also changes the shape of the grid, because nodes such as Grid to Mesh only see the active part. Use it to cut a hole into a grid or to throw away the part of a grid that is far from where you work.

#### Inputs

##### Grid

Data type: Float.

The grid to change. The node works on any data type, set at the top of the node.

##### Selection

Data type: Boolean.

The voxels to deactivate. A boolean field, evaluated at every voxel. Voxels where it is true are turned off.

#### Outputs

##### Grid

Data type: Float.

The grid without the deactivated voxels.

Data type, shown at the top of the node, is the type of the values in the grid: Float, Integer, Boolean or Vector.

### Field to Grid

![Field to Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/field-to-grid.png)

Create new grids by evaulating new values on an existing volume grid topology.

#### Inputs

##### Topology

Data type: Float.

The input topology.

##### Properties

—



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

Data type: Float.

The input grid.

##### Mode

Data type: Menu.

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/mode.png)

How to progress the state.

###### Inactive

Turn inactive voxels and tiels into inactive background tiles.

###### Threshold

Turn regioons where all voxels have the same value and active state into inactive background tiles. You will see a threshold slider.

###### SDF

Replace inactive tiles with inactive nodes.



##### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/data-type.png)

The data type to evaluate.

#### Output

##### Grid

Data type: Float.

The generated grid.

### Prune Grid

![Prune Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/prune-grid-2.png)

Create new grids by evaulating new values on an existing volume grid topology.

#### Inputs

##### Grid

Data type: Float.

The input grid.

##### Properties

—



##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-operations/data-type.png)

The data type to evaluate.

#### Output

##### Grid

Data type: Float.

The generated grid.

# Primitives

## Add menu - Volume - Primitives

![Add menu - Volume - Primitives](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/add-menu-volume-primitives.png)

Here you find nodes to modify the volume.

### Cube Grid Topology

![Cube Grid Topology](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/cube-grid-topology.png)

Makes the shape of a box of voxels, without any values in it. The output is only a topology, a set of active voxels, which you give to the Field to Grid node to fill it with a field. Use it as the starting point of a grid that you make from nodes, for example a density grid for a cloud, a signed distance field for a shape, or a region for a simulation.

#### Inputs

##### Bounds Min

Data type: Vector.

The corner of the box with the lowest coordinates.

##### Bounds Max

Data type: Vector.

The corner of the box with the highest coordinates.

##### Resolution X

Data type: Integer.

How many voxels the box has along X.

##### Resolution Y

Data type: Integer.

How many voxels the box has along Y.

##### Resolution Z

Data type: Integer.

How many voxels the box has along Z.

##### Min X

Data type: Integer.

Panel Min. The index of the first voxel along X. It moves the box along the grid index space without changing its size.

##### Min Y

Data type: Integer.

Panel Min. The same for Y.

##### Min Z

Data type: Integer.

Panel Min. The same for Z.

#### Outputs

##### Topology

Data type: Boolean.

The shape of the box, as a boolean grid. Connect it to the Topology input of Field to Grid.

#### How to use

![Cube Grid Topology example](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/cube-grid-topology-chain.png)

1. Add **Cube Grid Topology**. Set **Bounds Min** and **Bounds Max** to the size of the box and the resolutions to the detail you need. The voxel size is the box size divided by the resolution, so the same box with a resolution of 32 has voxels half the size of a resolution of 16.
2. Add **Field to Grid** and connect the Topology output to its Topology input. Add a value with the plus socket and connect a field to it. In the example the field is `2 - Length(Position)`.
3. Connect the grid to **Grid to Mesh** and set Threshold to 0.5. The mesh is a sphere-like surface where the value crosses 0.5, cut off by the box.

Keep the resolution low while you build. Every doubling of the resolution makes eight times as many voxels.

### Volume Cube

![Volume Cube](/docs2/images/editors/geometry-node-editor/header/add-menu-volume-primitives/volume-cube.png)

The Volume Cube node generates a voxel based volume cube primitive that can be used for volume conversion to mesh in conjunction with the Volume to Mesh node.

#### Inputs

##### Geometry

Standard geometry input.

##### Density

Data type: Float.

Volume density per voxel. Higher values makes it more dense.

##### Background

Data type: Float.

Value per voxel outside the cube domain.

##### Min:

Minimum boundary of the volume cube. Max: Maximum boundary of the volume cube. Resolution X Number of volume voxules in the X axis. Resolution Y Number of volume voxules in the Y axis. Resolution Z Number of volume voxules in the Z axis.

