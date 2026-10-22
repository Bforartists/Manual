---
id: editors.geometry-node-editor.header.add-menu-mesh-primitives
title: Add Menu - Mesh - Primitives
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - Primitives
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.32 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Primitives.odt
---
## Add menu - Mesh - Primitives

![Add menu - Mesh - Primitives](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/add-menu-mesh-primitives.png)

Nodes to modify the mesh geometry.

### Cone

![Cone](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cone.png)

Cone creates a Cone mesh.

#### Input


| Entry | What it does |
| ------------- | ------------------------------------------------ |
| Vertices | Number of vertices. |
| Radius Top | The initial radius at the top. |
| Side Segments | Adjust the number of segments at the side. |
| Fill Segments | Adjust the number of segments at the fill faces. |
| Radius Bottom | The initial radius at the bottom. |
| Depth | The initial height. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.


| Entry | What it does |
| --------- | -------------------------------- |
| None | pure edge geometry. |
| N-Gon | The circle face is a N-Gon face. |
| Triangles | The circle face is triangulated. |


#### Outputs


| Entry | What it does |
| ------ | --------------------- |
| Mesh | Mesh output. |
| Top | Top radius output. |
| Bottom | Bottom radius output. |
| Side | The depth output |
| UV Map | UV map output. |


### Cube

![Cube](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cube.png)

Cube creates a Cubeoid mesh.


| Entry | What it does |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Size**: The initial size in X , Y and Z dimensions · **Vertices**: How much vertices the single edges has. This allows to subdivide the cube. |
| Output | **Mesh**: Mesh output. · **UV Map**: UV map output. |


### Cylinder

![Cylinder](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/cylinder.png)

Cylinder creates a Cylinder mesh.

#### Input


| Entry | What it does |
| ------------- | ------------------------------------------------ |
| Vertices | Number of vertices. |
| Side Segments | Adjust the number of segments at the side. |
| Fill Segments | Adjust the number of segments at the fill faces. |
| Radius | The initial radius. |
| Depth | The initial height. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.


| Entry | What it does |
| --------- | -------------------------------- |
| None | pure edge geometry. |
| N-Gon | The circle face is a N-Gon face. |
| Triangles | The circle face is triangulated. |


#### Outputs


| Entry | What it does |
| ------ | --------------------- |
| Mesh | Mesh output. |
| Top | Top radius output. |
| Bottom | Bottom radius output. |
| Side | The depth output |
| UV Map | UV map output. |


### Grid

![Grid](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/grid.png)

Grid creates a grid mesh.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Size**: The initial size. · **Vertices X**: The initial number of vertices in X direction. · **Vertices Y**: The initial number of vertices in Y direction. |
| Outputs | **Mesh**: Mesh output. · **UV Map**: UV map output. |


### Ico Sphere

![Ico Sphere](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/ico-sphere.png)

Ico Sphere creates a ico Sphere mesh.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------- |
| Input | **Radius**: The initial radius. · **Subdivisions**: The initial subdivisions. |
| Outputs | **Mesh**: Mesh output. · **UV Map**: UV map output. |


### Mesh Circle

![Mesh Circle](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mesh-circle.png)

Circle creates a Circle mesh.

#### Input


| Entry | What it does |
| -------- | ------------------- |
| Vertices | Number of vertices. |
| Radius | The initial radius. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/properties.png)

##### Fill Type

Defines how the Circle mesh is filled.


| Entry | What it does |
| --------- | -------------------------------- |
| None | pure edge geometry. |
| N-Gon | The circle face is a N-Gon face. |
| Triangles | The circle face is triangulated. |


#### Outputs

##### Mesh

Mesh output.

### Mesh Line

![Mesh Line](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mesh-line.png)

Line creates a line mesh.

#### Input


| Entry | What it does |
| -------------- | ------------------------------- |
| Count | The initial number of segments. |
| Start Location | The initial location. |
| Offset | The initial offset. |


#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/mode.png)

###### Offset

Specify the offset from one vertice to the next.

###### End Points

Specify the line start and endpoints.

**Count ModeCount**

![Count](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/count.png)

Specify the number of total vertices.

**End Points**

![End Points](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/end-points.png)

Specify the distance between the vertices.

#### Outputs

##### Mesh

Mesh output.

### UV Sphere

![UV Sphere](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-primitives/uv-sphere.png)

UV Sphere creates a uv sphere mesh.


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Input | **Segments**: The initial number of segments. · **Rings**: The initial number of edgerings. · **Radius**: The initial radius. |
| Outputs | **Mesh**: Mesh output. · **UV Map**: UV map output. |


