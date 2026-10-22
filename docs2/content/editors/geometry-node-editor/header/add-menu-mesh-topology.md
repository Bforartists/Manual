---
id: editors.geometry-node-editor.header.add-menu-mesh-topology
title: Add Menu - Mesh - Topology
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - Topology
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.33 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Topology.odt
---
## Add menu - Mesh - Topology

![Add menu - Mesh - Topology](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/add-menu-mesh-topology.png)

Mesh topology related nodes.

### Corners of Edge

![Corners of Edge](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-edge.png)

Retreive the corners that makes up a edge.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Face Index**: The face to get the data from. · **Weights**: Values used to sort the corners of the face. · **Sort Index**: Which of the corners to output. |
| Outputs | **Corner Index**: The output corner. · **Total**: The number of corners in the face. |


### Corners of Face

![Corners of Face](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-face.png)

Retreive the corners that makes up a face.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Face Index**: The face to get the data from. · **Weights**: Values used to sort the corners of the face. · **Sort Index**: Which of the corners to output. |
| Outputs | **Corner Index**: The output corner. · **Total**: The number of corners in the face. |


### Corners of Vertex

![Corners of Vertex](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/corners-of-vertex.png)

Retreive face corners connected to vertices.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Vertex Index**: The vertice to get the data from. · **Weights**: Values used to sort the corners attached to the vertice. · **Sort Index**: Which of the corners to output. |
| Outputs | **Corner Index**: The output corner. · **Total**: The number of corners connected to each vertice. |


### Edges of Corner

![Edges of Corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/edges-of-corner.png)

Retreive the edges of both sides of a corner.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------- |
| Input | **Corner Index**: The corner to retreive the data from. |
| Outputs | **Next Edge Index**: The edge behind the corner. · **Previous Edge Index**: The edge before the corner. |


### Edges of Vertex

![Edges of Vertex](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/edges-of-vertex.png)

Retreive the edges connected to each vertex.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Vertex Index**: The vertice to get the data from. · **Weights**: Values used to sort the edges attached to the vertice. · **Sort Index**: Which of the edges to output. |
| Outputs | **Edge Index**: The output edge. · **Total**: The number of edges connected to each vertice. |


### Face of Corner

![Face of Corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/face-of-corner.png)

Retreive the faces connected to each corner.


| Entry | What it does |
| ------- | --------------------------------------------------------------------------------------------------------------------------- |
| Input | **Corner Index**: The corner to get the data from. |
| Outputs | **Face Index**: The output faces. · **Index in Face**: The index of the corner, starting from the first corner in the face. |


### Offset Corner in Face

![Offset Corner in Face](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/offset-corner-in-face.png)

Retreive corners within the same face as another


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Corner Index**: The corner to get the data from. · **Offset**: The numbers of corners to move around the face before getting the result. It circles around the start of the face if necessary. |
| Outputs | **Corner Index**: The index of the offset corner. |


### Vertex of corner

![Vertex of corner](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-topology/vertex-of-corner.png)

Retreive the vertex each corner is attached to.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Corner Index**: The corner to get the data from. · **Offset**: The numbers of corners to move around the face before getting the result. It circles around the start of the face if necessary. |
| Outputs | **Vertex Index**: The vertex each corner is attached to. |


