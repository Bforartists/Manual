---
id: editors.geometry-node-editor.header.add-menu-mesh-write
title: Add Menu - Mesh - Write
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - Write
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.30 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - Write.odt
---
## Add menu - Mesh - Write

![Add menu - Mesh - Write](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/add-menu-mesh-write.png)

These are nodes for working with Mesh data.

### Set Mesh Normal

![Set Mesh Normal](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/set-mesh-normal.png)

The **Set Mesh Normal** node is used to modify custom normals on a mesh, providing control over shading smoothness and surface appearance. This is useful for adjustingnormalsmoothness, sharp edges, and tangent-based effects

#### Input

##### Mesh

Input mesh.

#### Properties

##### Mode

![Mode](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/mode.png)

###### Sharpness

![Sharpness](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/sharpness.png)

Controls the intensity of edge sharpness. Higher values create stronger shading contrasts between faces.

Store the sharpness of each face or edge. Similar to the "Shade Smooth" and "Shade Flat" operators.


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------- |
| Remove Custom | Removes **custom normals** previously set by the user on the original mesh data when enabled. |
| Edge Sharpness | Sets the normal sharpness to the edge domain to “flat”. |
| Face Sharpness | Sets the normal sharpness to the face domain to “flat”. |


###### Free

![Free](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/free.png)

Allows direct manipulation of normals as **free vectors,** rather than constrained by geometry. Useful for custom shading effects and non-destructive normal adjustments.

**Domain**

![Domain](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/domain.png)

Attribute domain to store the free custom normals.

- Point
- Face
- Face Corner

> **Note:** Default object normals are stored to Facecorner, this will “pass-through” the normal data. Face normals will make “flat” sharp edges.

###### Tangent Space

![Tangent Space](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/tangent-space.png)

Adjusts normals relative to the surface tangentto store the source meshes normals.Storesnormals in a deformation dependent custom transformation space.

> **Note:** This method is slower, but can be better when subsequent operations change the mesh without handling normals specifically.

###### Custom Normal

*Vector Field based on the normal.*

#### Outputs

##### Geometry

Geometry output.

Got it! Here's the documentation for the **Set Mesh Normal** node:

### Set Shade Smooth

![Set Shade Smooth](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-write/set-shade-smooth.png)

Retrieves if the geometry is shaded smooth.

#### Input


| Entry | What it does |
| ------------ | ------------------------------ |
| Geometry | Input mesh. |
| Selection | A selection of the input mesh. |
| Shade Smooth | Set the shading to smooth. |


#### Properties

##### Domain


| Entry | What it does |
| ----- | ------------------- |
| Edge | Set Edge to smooth. |
| Face | Set Face to smooth |


#### Outputs

##### Geometry

Geometry output.

