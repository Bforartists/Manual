---
id: editors.geometry-node-editor.header.add-menu.mesh
title: "Mesh"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Mesh"
version: "5.1"
status: needs-review
icon: node
summary: "Mesh nodes: Read, Sample, Write, Operations, Primitives, Topology…."
order: 80
cta: "Nodes"
source:
  - "12.1.28 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Read.odt"
  - "12.1.29 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Sample.odt"
  - "12.1.30 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Write.odt"
  - "12.1.31 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Operations.odt"
  - "12.1.32 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Primitives.odt"
  - "12.1.33 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Topology.odt"
  - "12.1.34 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - UV.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-mesh-read
  - editors.geometry-node-editor.header.add-menu-mesh-sample
  - editors.geometry-node-editor.header.add-menu-mesh-write
  - editors.geometry-node-editor.header.add-menu-mesh-operations
  - editors.geometry-node-editor.header.add-menu-mesh-primitives
  - editors.geometry-node-editor.header.add-menu-mesh-topology
  - editors.geometry-node-editor.header.add-menu-mesh-uv
---
# Read

## Add menu - Mesh - Read

![Add menu - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/add-menu-mesh-read.png)

Nodes to modify the mesh geometry.

### Cluster by Connected

![Cluster by Connected](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/cluster-by-connected.png)

Sorts the vertices of a mesh into groups, but only joins vertices that are connected by an edge and are close together. It works like Cluster by Distance, with the extra rule that two vertices must also share an edge. Use it when nearby vertices of different parts of a mesh must stay apart, for example the tips of two fingers that almost touch.

#### Inputs

##### Selection

Data type: Boolean.

Which vertices are put into clusters.

##### Position

Data type: Vector.

The position used to measure the distance.

##### Distance

Data type: Float (distance).

Connected vertices that are closer than this value belong to the same cluster.

#### Outputs

##### Cluster ID

Data type: Integer.

The number of the cluster of each vertex. The number is the index of the first vertex of the cluster.

#### How to use

With the five points of the Cluster by Distance example and edges between points 0 and 1, 1 and 2, and 3 and 4, the Cluster ID is 0, 0, 2, 3, 3. Points 1 and 2 are connected but 0.0015 apart, which is more than the Distance of 0.001, so they do not share a cluster.

### Edge Angle

![Edge Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edge-angle.png)

Calculates the angle in radians between two faces that meet at an edge. Without two faces on the edge, the angle will be 0.

#### Outputs

##### Unsigned Angle

Data type: Float.

The unsigned output angle. The shortest angle will be picked.

##### Signed Angle

Data type: Float.

The signed angle between the two faces, where Convex angles are positive and Concave angles are negative. This calculation is slower than the unsigned angle.



### Edge Neighbours

![Edge Neighbours](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edge-neighbours.png)

Outputs the number of faces connected to each edge.

#### Outputs

##### Face Count

The number of faces.

### Edge Vertices

![Edge Vertices](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edge-vertices.png)

Outputs the index and position of the two vertices that defines an edge. Index outputs an integer. Position a vector.

#### Outputs

##### Vertex Index 1

Data type: Integer.

The index of the first vertice.

##### Vertex Index 2

Data type: Integer.

The index of the second vertice.

##### Position 1

Data type: Vector.

The position of the first vertice.

##### Position 2

Data type: Vector.

The position of the second vertice.



### Edges to Face Group

![Edges to Face Group](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edges-to-face-group.png)

Group Faces into regions, surrounded by the selected boundary edges.

#### Inuputs

##### Boundary Edges

The input edges.

#### Outputs

##### Face Group ID

The output face group.



### Face Area

![Face Area](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-area.png)

Gives each face area a unique id. Which can be used in a capture attribute for example, to create instances of other geometry to this now unique face areas.

#### Outputs

##### Area

Data type: Float.

The face area output.

### Face Group Boundaries

![Face Group Boundaries](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-group-boundaries.png)

Find edges on the boundaries between face sets

#### Inputs

—

#### Face Set

The input face sets to calculate the boundaries from.

#### Outputs

##### Boundary Edges

Data type: Boolean.

The edges that lies on the boundaries between the different face sets

##### Face Count

The face count for the face neighbors.



### Face Neighbours

![Face Neighbours](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-neighbours.png)

Outputs the number of vertices or faces connected to each face.

#### Outputs

##### Vertex Count

The vertex count for the face neighbors.

##### Face Count

The face count for the face neighbors.



### Is Face Planar

![Is Face Planar](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-face-planar.png)

Returns true if all of the points of the evaluated face are on the same plane.

#### Inputs

##### Threshold

Data type: Float (distance).

The threshold to consinder the points to be at the same plane.

#### Outputs

##### Planar

Data type: Boolean.

True if the face is planar.



### Is Face Smooth

![Is Face Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-face-smooth.png)

Retreives if the face is shaded smooth.

#### Outputs

##### Smooth

Data type: Boolean.

Smooth output.

### Is Edge Smooth

![Is Edge Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-edge-smooth.png)

Retreives if the edge is shaded smooth.

#### Outputs

##### Smooth

Data type: Boolean.

Smooth output.

### Mesh Island

![Mesh Island](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/mesh-island.png)

Outputs a separate index for each mesh island. The indices are based on the order of the lowest-numbered vertex in each island.

#### Outputs

##### Index Index

The index output.

##### Island Count

Data type: Integer.

The count output.



### Shortest Edge Path

![Shortest Edge Path](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/shortest-edge-path.png)

Calculates the shortest path from multiple start points.

#### Inputs

##### End Vertex

The last point of the path.

##### Edge Cost

The amount of calculation to find the shortest path.

#### Outputs

##### Next Vertex Index

The vertices index of the shortest path.

##### Total Cost

The calculation amount.



### Vertex Neighbors

![Vertex Neighbors](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/vertex-neighbors.png)

Outputs the number of vertices or faces connected to each vertex.

#### Outputs

##### Vertex Count

Data type: Integer.

The vertex count for the vertex neighbors.

##### Face Count

Data type: Integer.

The face count for the vertex neighbors.


# Sample

## Add menu - Mesh - Sample

![Add menu - Mesh - Sample](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/add-menu-mesh-sample.png)

Nodes to modify the mesh geometry.

### Sample Nearest Surface

![Sample Nearest Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/sample-nearest-surface.png)

Calculate the interpolated value of a mesh attribute on the closest point of its surface.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Value

Data type: follows the Data Type setting.

The value to calculate.

##### Group ID

Data type: Integer.

Is evaluated on the face domain, and splits the input mesh into multiple parts, each with its own id.

##### Sample Position

Data type: Vector.

The sample position to calculate.

##### Sample Group ID

Data type: Integer.

Determines in which group the closest nearest surface is detected.



##### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/data-type.png)

Which data to calculate.

#### Outputs

##### Value

Data type: follows the Data Type setting.

The output value.

##### Is Valid

Data type: Boolean.

Wether the sampling was successful. It is false when the sampled group is empty.



### Sample UV Surface

![Sample UV Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/sample-uv-surface.png)

Calculate the interpolated value of a mesh attribute at a UV coordinate.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Value

Data type: follows the Data Type setting.

The value to calculate.

##### Source UV Map

The input UV map.

##### Sample UV

Data type: Vector.

The sample position to calculate.



##### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-sample/data-type.png)

Which data to calculate.

#### Outputs

##### Value

Data type: follows the Data Type setting.

The output value.

##### Is Valid

Data type: Boolean.

Wether the node could find a single face to sample at the uv coordinate.


# Write

## Add menu - Mesh - Write

![Add menu - Mesh - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/add-menu-mesh-write.png)

These are nodes for working with Mesh data.

### Set Mesh Normal

![Set Mesh Normal](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/set-mesh-normal.png)

The **Set Mesh Normal** node is used to modify custom normals on a mesh, providing control over shading smoothness and surface appearance. This is useful for adjustingnormalsmoothness, sharp edges, and tangent-based effects

#### Input

##### Mesh

Data type: Geometry.

Input mesh.

#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/mode.png)

##### Sharpness

![Sharpness](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/sharpness.png)

Controls the intensity of edge sharpness. Higher values create stronger shading contrasts between faces.

Store the sharpness of each face or edge. Similar to the "Shade Smooth" and "Shade Flat" operators.

###### Remove Custom

Removes **custom normals** previously set by the user on the original mesh data when enabled.

###### Edge Sharpness

Sets the normal sharpness to the edge domain to “flat”.

###### Face Sharpness

Sets the normal sharpness to the face domain to “flat”.



##### Free

![Free](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/free.png)

Allows direct manipulation of normals as **free vectors,** rather than constrained by geometry. Useful for custom shading effects and non-destructive normal adjustments.

###### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/domain.png)

Attribute domain to store the free custom normals.

- Point
- Face
- Face Corner

> **Note:** Default object normals are stored to Facecorner, this will “pass-through” the normal data. Face normals will make “flat” sharp edges.

##### Tangent Space

![Tangent Space](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/tangent-space.png)

Adjusts normals relative to the surface tangentto store the source meshes normals.Storesnormals in a deformation dependent custom transformation space.

> **Note:** This method is slower, but can be better when subsequent operations change the mesh without handling normals specifically.

##### Custom Normal

*Vector Field based on the normal.*

#### Outputs

##### Geometry

Geometry output.

Got it! Here's the documentation for the **Set Mesh Normal** node:

### Set Shade Smooth

![Set Shade Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/set-shade-smooth.png)

Retrieves if the geometry is shaded smooth.

#### Input

##### Geometry

Input mesh.

##### Selection

Data type: Boolean.

A selection of the input mesh.

##### Shade Smooth

Data type: Boolean.

Set the shading to smooth.



#### Properties

##### Domain

###### Edge

Set Edge to smooth.

###### Face

Set Face to smooth



#### Outputs

##### Geometry

Geometry output.

# Operations

## Add menu - Mesh - Operations

![Add menu - Mesh - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/add-menu-mesh-operations.png)

Nodes to modify the mesh geometry.

### Dual Mesh

![Dual Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/dual-mesh.png)

The Dual Mesh node calculates the dual of the input mesh. This means that faces get replaced with vertices and vertices with faces.

#### Inputs

##### Mesh

Data type: Geometry.

The input mesh.

##### Keep Boundaries

Data type: Boolean.

Keep the (non-manifold) boundaries of the mesh intact.

#### Outputs

##### Dual Mesh

Data type: Geometry.

The output mesh.



### Edge Paths to Curves

![Edge Paths to Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/edge-paths-to-curves.png)

Converts Edge Paths to Curves.

#### Inputs

##### Mesh

Data type: Geometry.

The input mesh.

##### Start Vertices

Data type: Boolean.

The start vertices of the edge path.

##### Next Vertex Index

Data type: Integer.

The edge path by index.

#### Outputs

##### Curves

Data type: Geometry.

The output curve.



### Edge Path to Selection

![Edge Path to Selection](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/edge-path-to-selection.png)

Calculates an edge path, and converts it to a selectoin

#### Inputs

##### Start Vertices

The start vertices of the edge path.

##### Next Vertex Index

The edge path by index.

#### Outputs

##### Selection

The selection



### Extrude Mesh

![Extrude Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/extrude-mesh.png)

Extrudes out geometry at the selection by a given amount.

#### Inputs

##### Mesh

Data type: Geometry.

The input mesh.

##### Selection

Data type: Boolean.

A selection of the mesh.

##### Offset

Data type: Vector (translation).

The offset amount.

##### Offset Scale

Data type: Float.

The offset scale. Without an offset this is equal the amount.

##### Individual

Data type: Boolean.

Just Faces mode. Extrude out individual faces.



#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/properties.png)

##### Mode

What kind of elements to extrude out. Vertices, Edges or Faces.

#### Outputs

##### Mesh

Data type: Geometry.

The output mesh.

##### Top

Data type: Boolean.

The top elements of the extrusion.

##### Side

Data type: Boolean.

The side elements of the extrusion.



### Flip Faces

![Flip Faces](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/flip-faces.png)

Flips the winding order of the selected faces.

Blender developers decided not to call it Flip Normals. Since "normals are  
derived data, changing them is only a side effect." However, what the node does is in fact to flip the normals.

#### Inputs

##### Mesh

Data type: Geometry.

The input mesh.

##### Selection

Data type: Boolean.

A selection of the input mesh.

#### Outputs

##### Dual Mesh

The output mesh.



### Mesh Boolean

![Mesh Boolean](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-boolean.png)

The Boolean Node allows you to cut, subtract, and join the geometry of two inputs. This node offers the same operations as the Boolean modifier.

#### Inputs

##### Mesh 1

Data type: Geometry.

Standard geometry input.

##### Mesh 2

Data type: Geometry.

Standard geometry input.

##### Self Intersect

Allow self intersection.

##### Hole Tolerant

Data type: Boolean.

Allow holes.



#### Properties

##### Operation

![Operation](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/operation.png)

The boolean operation.

###### Intersect

Produce a new geometry containing only the volume inside of both geometry 1 and geometry 2.

###### Union

The two input pieces of geometry are joined, then any interior elements are removed.

###### Difference

Geometry 2 is subtracted from geometry 1 (everything outside of geometry 2 is kept).



##### Solver

![Solver](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/solver.png)

###### Float

Simple solver for the best performance. Does not support overlapping geometry.

###### Exact

Exact solver for the most accurate result.

###### Manifold

Fastest solver with best result, but only works on manifold meshes.



#### Output

##### Geometry

Standard geometry output.

##### Intersecting Edges

Data type: Boolean.

Outputs the intersecting edges.



### Mesh to Curve

![Mesh to Curve](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-to-curve.png)

Converts a mesh geometry to a curve geometry.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Selection

Data type: Boolean.

A selection of the input mesh.

#### Properties

##### Mode

Edges or Faces.

#### Outputs

##### Curve

Data type: Geometry.

Standard curve output.



### Mesh to Density Grid

![Mesh to Density Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-to-density-grid.png)

Converts a mesh geometry to a curve geometry.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Density

Data type: Float.

Mesh density.

##### Voxel Size

Data type: Float (distance).

The vodel size.

##### Gradient Width

Data type: Float (distance).

The width of the gradient.

#### Outputs

##### Density Grid.

Density Grid output.



### Mesh to Points

![Mesh to Points](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-to-points.png)

Converts a mesh geometry to a point geometry.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Selection

Data type: Boolean.

A selection of the input mesh.

##### Position

Data type: Vector.

The position of the points.

##### Radius

Data type: Float (distance).

The radius of the points



#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mode.png)

What geometry to convert to points.

#### Outputs

##### Curve

Standard curve output.

### Mesh to SDF Grid

![Mesh to SDF Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-to-sdf-grid.png)

Converts a mesh geometry to a curve geometry.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Voxel Size

Data type: Float (distance).

The vodel size.

##### Band Width

Data type: Integer.

The width of the band.

#### Outputs

##### Density Grid.

Density Grid output.



### Mesh to Volume

![Mesh to Volume](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/mesh-to-volume.png)

Converts a mesh geometry to a Volume.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Density

Data type: Float.

The density of the volume



##### Resolution Mode

Data type: Menu.

![Resolution Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/resolution-mode.png)

How to calculate the volume. Based of the size or based at the amount.

###### Voxel Amount / Voxel Size

The voxel amount / the voxel size.

###### Interior Bandwidth

Where to start the calculation inside of the volume.



#### Outputs

##### Volume

Data type: Geometry.

The volume output.

### Scale Elements

![Scale Elements](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/scale-elements.png)

Allows to scale the selected elements.

#### Inputs

##### Geometry

Data type: Geometry.

Standard geometry input.

##### Selection

Data type: Boolean.

A selection of the geometry.

##### Scale

Data type: Float.

The scale factor

##### Center

Data type: Vector (translation).

The center of the scaling.



##### Scale Mode

Data type: Menu.

![Scale Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/scale-mode.png)

Uniform scales uniformly in all three world coordinates.

Single Axis scales separately in the single axis.

##### Axis

Data type: Vector.

![Axis](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/axis.png)

Scale Mode Single axis only. Scale the selection separately along its single axis.

#### Properties

##### Domain

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/domain.png)

What kind of elements to scale.

#### Outputs

##### Geometry

Data type: Geometry.

The output geometry.

### Split Edges

![Split Edges](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/split-edges.png)

Splits the edges of the geometry.

Note that splitting edges breaks the mesh topology.

#### Inputs

##### Mesh

Data type: Geometry.

Input mesh.

##### Selection

Data type: Boolean.

A selection of the input mesh.

#### Outputs

##### Mesh

Data type: Geometry.

Standard Mesh output.



### Subdivide Mesh

![Subdivide Mesh](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/subdivide-mesh.png)

Subdivides the geometry by a simple division.

#### Inputs

##### Geometry

Standard geometry input.

##### Level

Data type: Integer.

To which degree the geometry will be deformed.

#### Outputs

##### Geometry

Standard geometry output.



### Subdivision Surface

![Subdivision Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/subdivision-surface.png)

The Subdivision Surface node subdivides the geometry using Catmull-Clark deformation.

#### Inputs

##### Mesh

Data type: Geometry.

Standard geometry input.

##### Level

Data type: Integer.

To which degree the geometry will be deformed.

##### Edge Crease

Data type: Float (factor).

Control how smooth edges should be with Weighted Edge Creases.

##### Vertex Crease

Data type: Float (factor).

Control how smooth edges should be with Weighted Vertex Creases.

##### Limit Surface

Data type: Boolean.

Place the vertices at the surface as if it would be infinite subdivided. This results in the smoothest possible shape.



##### UV Smooth

Data type: Menu.

![UV Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/uv-smooth.png)

The methbod to deal with smoothing the UV.

##### Boundary Smooth

Data type: Menu.

![Boundary Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/boundary-smooth.png)

Controls if open boundaries and corners are smooth.

#### Outputs

##### Geometry

Standard geometry output.

### Triangulate

![Triangulate](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/triangulate.png)

The Triangulate node triangulates all faces in a mesh.

#### Inputs

##### Geometry

Standard geometry input.

##### Minimum Vertices

Minimum number of vertices a face must have to be triangulated. For example, setting this value to 5, will prevent triangulation of Quads and only triangulate N-gons.



#### Properties

##### Quad Method

![Quad Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/quad-method.png)

A quad is a polygon with four edges.

###### Beauty

Split the quads in nice triangles, slower method.

###### Fixed

Split the quads on their 1st and 3rd vertices.

###### Fixed Alternate

Split the quads on their 2nd and 4th vertices.

###### Shortest Diagonal

Split the quads based on the shortest diagonal distance between their vertices.

###### Longest Diagonal

Split the quads based on the longest diagonal distance between their vertices.



##### Polygon Method

![Polygon Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-operations/polygon-method.png)

Meant are N-Gons. Faces with more than four edges. Tris, Quads and N-Gons are all Polygons.

###### Beauty

Arrange the new triangles nicely, slower method.

###### Clip

Split the polygons using an ear-clipping algorithm (gives similar results to the tessellation used for the viewport rendering).



#### Outputs

##### Geometry

Standard geometry output.

# Primitives

## Add menu - Mesh - Primitives

![Add menu - Mesh - Primitives](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/add-menu-mesh-primitives.png)

Nodes to modify the mesh geometry.

### Cone

![Cone](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cone.png)

Cone creates a Cone mesh.

#### Input

##### Vertices

Data type: Integer.

Number of vertices.

##### Radius Top

Data type: Float (distance).

The initial radius at the top.

##### Side Segments

Data type: Integer.

Adjust the number of segments at the side.

##### Fill Segments

Data type: Integer.

Adjust the number of segments at the fill faces.

##### Radius Bottom

Data type: Float (distance).

The initial radius at the bottom.

##### Depth

Data type: Float (distance).

The initial height.



#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.

###### None

pure edge geometry.

###### N-Gon

The circle face is a N-Gon face.

###### Triangles

The circle face is triangulated.



#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### Top

Data type: Boolean.

Top radius output.

##### Bottom

Data type: Boolean.

Bottom radius output.

##### Side

Data type: Boolean.

The depth output

##### UV Map

Data type: Vector.

UV map output.



### Cube

![Cube](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cube.png)

Cube creates a Cubeoid mesh.

#### Inputs

##### Size

Data type: Vector (translation).

The initial size in X , Y and Z dimensions

##### Vertices

How much vertices the single edges has. This allows to subdivide the cube.

#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### UV Map

Data type: Vector.

UV map output.



### Cylinder

![Cylinder](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cylinder.png)

Cylinder creates a Cylinder mesh.

#### Input

##### Vertices

Data type: Integer.

Number of vertices.

##### Side Segments

Data type: Integer.

Adjust the number of segments at the side.

##### Fill Segments

Data type: Integer.

Adjust the number of segments at the fill faces.

##### Radius

Data type: Float (distance).

The initial radius.

##### Depth

Data type: Float (distance).

The initial height.



#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.

###### None

pure edge geometry.

###### N-Gon

The circle face is a N-Gon face.

###### Triangles

The circle face is triangulated.



#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### Top

Data type: Boolean.

Top radius output.

##### Bottom

Data type: Boolean.

Bottom radius output.

##### Side

Data type: Boolean.

The depth output

##### UV Map

Data type: Vector.

UV map output.



### Grid

![Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/grid.png)

Grid creates a grid mesh.

#### Inputs

##### Size

The initial size.

##### Vertices X

Data type: Integer.

The initial number of vertices in X direction.

##### Vertices Y

Data type: Integer.

The initial number of vertices in Y direction.

#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### UV Map

Data type: Vector.

UV map output.



### Ico Sphere

![Ico Sphere](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/ico-sphere.png)

Ico Sphere creates a ico Sphere mesh.

#### Inputs

##### Radius

Data type: Float (distance).

The initial radius.

##### Subdivisions

Data type: Integer.

The initial subdivisions.

#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### UV Map

Data type: Vector.

UV map output.



### Mesh Circle

![Mesh Circle](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mesh-circle.png)

Circle creates a Circle mesh.

#### Input

##### Vertices

Data type: Integer.

Number of vertices.

##### Radius

Data type: Float (distance).

The initial radius.



#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.

###### None

pure edge geometry.

###### N-Gon

The circle face is a N-Gon face.

###### Triangles

The circle face is triangulated.



#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

### Mesh Line

![Mesh Line](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mesh-line.png)

Line creates a line mesh.

#### Input

##### Count

Data type: Integer.

The initial number of segments.

##### Start Location

Data type: Vector (translation).

The initial location.

##### Offset

Data type: Vector (translation).

The initial offset.



#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mode.png)

##### Offset

Specify the offset from one vertice to the next.

##### End Points

Specify the line start and endpoints.

###### Count ModeCount

![Count](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/count.png)

Specify the number of total vertices.

###### End Points

![End Points](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/end-points.png)

Specify the distance between the vertices.

#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

### UV Sphere

![UV Sphere](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/uv-sphere.png)

UV Sphere creates a uv sphere mesh.

#### Inputs

##### Segments

Data type: Integer.

The initial number of segments.

##### Rings

Data type: Integer.

The initial number of edgerings.

##### Radius

Data type: Float (distance).

The initial radius.

#### Outputs

##### Mesh

Data type: Geometry.

Mesh output.

##### UV Map

Data type: Vector.

UV map output.


# Topology

## Add menu - Mesh - Topology

![Add menu - Mesh - Topology](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/add-menu-mesh-topology.png)

Mesh topology related nodes.

### Corners of Edge

![Corners of Edge](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-edge.png)

Retreive the corners that makes up a edge.

#### Inputs

##### Face Index

The face to get the data from.

##### Weights

Data type: Float.

Values used to sort the corners of the face.

##### Sort Index

Data type: Integer.

Which of the corners to output.

#### Outputs

##### Corner Index

Data type: Integer.

The output corner.

##### Total

Data type: Integer.

The number of corners in the face.



### Corners of Face

![Corners of Face](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-face.png)

Retreive the corners that makes up a face.

#### Inputs

##### Face Index

Data type: Integer.

The face to get the data from.

##### Weights

Data type: Float.

Values used to sort the corners of the face.

##### Sort Index

Data type: Integer.

Which of the corners to output.

#### Outputs

##### Corner Index

Data type: Integer.

The output corner.

##### Total

Data type: Integer.

The number of corners in the face.



### Corners of Vertex

![Corners of Vertex](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-vertex.png)

Retreive face corners connected to vertices.

#### Inputs

##### Vertex Index

Data type: Integer.

The vertice to get the data from.

##### Weights

Data type: Float.

Values used to sort the corners attached to the vertice.

##### Sort Index

Data type: Integer.

Which of the corners to output.

#### Outputs

##### Corner Index

Data type: Integer.

The output corner.

##### Total

Data type: Integer.

The number of corners connected to each vertice.



### Edges of Corner

![Edges of Corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/edges-of-corner.png)

Retreive the edges of both sides of a corner.

#### Inputs

##### Corner Index

Data type: Integer.

The corner to retreive the data from.

#### Outputs

##### Next Edge Index

Data type: Integer.

The edge behind the corner.

##### Previous Edge Index

Data type: Integer.

The edge before the corner.



### Edges of Vertex

![Edges of Vertex](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/edges-of-vertex.png)

Retreive the edges connected to each vertex.

#### Inputs

##### Vertex Index

Data type: Integer.

The vertice to get the data from.

##### Weights

Data type: Float.

Values used to sort the edges attached to the vertice.

##### Sort Index

Data type: Integer.

Which of the edges to output.

#### Outputs

##### Edge Index

Data type: Integer.

The output edge.

##### Total

Data type: Integer.

The number of edges connected to each vertice.



### Face of Corner

![Face of Corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/face-of-corner.png)

Retreive the faces connected to each corner.

#### Inputs

##### Corner Index

Data type: Integer.

The corner to get the data from.

#### Outputs

##### Face Index

Data type: Integer.

The output faces.

##### Index in Face

Data type: Integer.

The index of the corner, starting from the first corner in the face.



### Offset Corner in Face

![Offset Corner in Face](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/offset-corner-in-face.png)

Retreive corners within the same face as another

#### Inputs

##### Corner Index

Data type: Integer.

The corner to get the data from.

##### Offset

Data type: Integer.

The numbers of corners to move around the face before getting the result. It circles around the start of the face if necessary.

#### Outputs

##### Corner Index

Data type: Integer.

The index of the offset corner.



### Vertex of corner

![Vertex of corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/vertex-of-corner.png)

Retreive the vertex each corner is attached to.

#### Inputs

##### Corner Index

Data type: Integer.

The corner to get the data from.

##### Offset

The numbers of corners to move around the face before getting the result. It circles around the start of the face if necessary.

#### Outputs

##### Vertex Index

Data type: Integer.

The vertex each corner is attached to.


# UV

## Add menu - UV

![Add menu - UV](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/add-menu-uv.png)

Here you find nodes to modify the UV mapping.

### Pack UV Islands

![Pack UV Islands](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/pack-uv-islands.png)

Pack the UV islands to get the most out of the UV mapping.

#### Inputs

##### UV

Data type: Vector.

The input UV geometry.

##### Selection

Data type: Boolean.

A selection of the UV geometry.

##### Margin

Data type: Float.

How big the gap between the single UV patches should be.

##### Rotate

Data type: Boolean.

Rotate island for best fit.



##### Method

Data type: Menu.

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method.png)

Method used for packing UV Islands.

###### Bottom Left

Bottom left corner of packing bounds.

###### Top Right

Top right corner of packing bounds.



#### Outputs

##### UV

Data type: Vector.

The output UV geometry.

### UV Tangent

![UV Tangent](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/uv-tangent.png)

Generate tangent directions based on a UV map.

#### Inputs

##### Method

Data type: Menu.

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method-2.png)

Exact or fast calculation.

##### UV

Data type: Vector (xyz2d).

x and y values of the UV space.

#### Outputs

##### Tangent

Data type: Vector.

The output UV geometry.

### UV Unwrap

![UV Unwrap](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/uv-unwrap.png)

Unwrap the mesh to give it an UV mapping.

#### Inputs

##### Selection

Data type: Boolean.

Which faces of the mesh should be unwrapped.

##### Seam

Data type: Boolean.

Mark edges as a seam for unwrapping.

##### Margin

Data type: Float.

How big the gap between the single UV patches should be.

##### Fill Holes

Data type: Boolean.

Virtually fill holes before unwrapping the mesh. This preserves symmetry and can avoids overlaps.



##### Method

Data type: Menu.

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method-3.png)

The unwrap method.

#### Outputs

##### UV

Data type: Vector.

The output UV geometry.
