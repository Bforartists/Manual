---
id: editors.geometry-node-editor.header.add-menu.normals
title: "Normals"
section: editors
path:
  - "Editors"
  - "Geometry Node Editor"
  - "Header"
  - "Add Menu"
  - "Normals"
version: "5.1"
status: draft
icon: node
summary: "Normals nodes."
order: 170
cta: "Nodes"
source:
  - "12.1.75 Editors - Geometry Nodes Editor - Header - Add Menu - Normals.odt"
replaces:
  - editors.geometry-node-editor.header.add-menu-normals
---
## Add menu - Normals

![Add menu - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-normals/add-menu-normals.png)

The Normals node Smooth by Angle is a Node Group. Node groups differ from the other nodes in the add menu due to being mid level node groups instead of individual low level nodes.

You can enter the node tree by clicking at the icon up right. Tab to leave the node tree. And you can of course also edit the node tree.

![Add menu - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-normals/add-menu-normals-2.png)

![Add menu - Normals](/docs2/images/editors/geometry-node-editor/header/add-menu-normals/add-menu-normals-3.png)

### Smooth by Angle

![Smooth by Angle](/docs2/images/editors/geometry-node-editor/header/add-menu-normals/smooth-by-angle.png)

Smoothens or sharpens the mesh edges based on the angle between faces.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Mesh**: The input geometry. · **Angle**: Maximum face angle for smooth edges. · **Ignore Sharpness**: Ignore the sharpness at edges that are set to sharp. |
| Output | **Geometry**: The output geometry. |
