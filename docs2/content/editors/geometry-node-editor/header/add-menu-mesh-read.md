---
id: editors.geometry-node-editor.header.add-menu-mesh-read
title: Add Menu - Mesh - Read
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - Read
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.28 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Read.odt
---
## Add menu - Mesh - Read

![Add menu - Mesh - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/add-menu-mesh-read.png)

Nodes to modify the mesh geometry.

### Edge Angle

![Edge Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edge-angle.png)

Calculates the angle in radians between two faces that meet at an edge. Without two faces on the edge, the angle will be 0.

#### Outputs


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unsigned Angle | The unsigned output angle. The shortest angle will be picked. |
| Signed Angle | The signed angle between the two faces, where Convex angles are positive and Concave angles are negative. This calculation is slower than the unsigned angle. |


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


| Entry | What it does |
| -------------- | ----------------------------------- |
| Vertex Index 1 | The index of the first vertice. |
| Vertex Index 2 | The index of the second vertice. |
| Position 1 | The position of the first vertice. |
| Position 2 | The position of the second vertice. |


### Edges to Face Group

![Edges to Face Group](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/edges-to-face-group.png)

Group Faces into regions, surrounded by the selected boundary edges.


| Entry | What it does |
| ------- | ----------------------------------------- |
| Inuputs | **Boundary Edges**: The input edges. |
| Outputs | **Face Group ID**: The output face group. |


### Face Area

![Face Area](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-area.png)

Gives each face area a unique id. Which can be used in a capture attribute for example, to create instances of other geometry to this now unique face areas.

#### Outputs

##### Area

The face area output.

### Face Group Boundaries

![Face Group Boundaries](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-group-boundaries.png)

Find edges on the boundaries between face sets


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | — |
| Face Set | The input face sets to calculate the boundaries from. |
| Outputs | **Boundary Edges**: The edges that lies on the boundaries between the different face sets · **Face Count**: The face count for the face neighbors. |


### Face Neighbours

![Face Neighbours](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/face-neighbours.png)

Outputs the number of vertices or faces connected to each face.

#### Outputs


| Entry | What it does |
| ------------ | ---------------------------------------- |
| Vertex Count | The vertex count for the face neighbors. |
| Face Count | The face count for the face neighbors. |


### Is Face Planar

![Is Face Planar](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-face-planar.png)

Returns true if all of the points of the evaluated face are on the same plane.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------- |
| Inputs | **Threshold**: The threshold to consinder the points to be at the same plane. |
| Outputs | **Planar**: True if the face is planar. |


### Is Face Smooth

![Is Face Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-face-smooth.png)

Retreives if the face is shaded smooth.

#### Outputs

##### Smooth

Smooth output.

### Is Edge Smooth

![Is Edge Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/is-edge-smooth.png)

Retreives if the edge is shaded smooth.

#### Outputs

##### Smooth

Smooth output.

### Mesh Island

![Mesh Island](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/mesh-island.png)

Outputs a separate index for each mesh island. The indices are based on the order of the lowest-numbered vertex in each island.

#### Outputs


| Entry | What it does |
| ------------ | ----------------- |
| Index Index | The index output. |
| Island Count | The count output. |


### Shortest Edge Path

![Shortest Edge Path](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/shortest-edge-path.png)

Calculates the shortest path from multiple start points.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------- |
| Input | **End Vertex**: The last point of the path. · **Edge Cost**: The amount of calculation to find the shortest path. |
| Outputs | **Next Vertex Index**: The vertices index of the shortest path. · **Total Cost**: The calculation amount. |


### Vertex Neighbors

![Vertex Neighbors](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-read/vertex-neighbors.png)

Outputs the number of vertices or faces connected to each vertex.

#### Outputs


| Entry | What it does |
| ------------ | ------------------------------------------ |
| Vertex Count | The vertex count for the vertex neighbors. |
| Face Count | The face count for the vertex neighbors. |


