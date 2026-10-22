---
id: editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-read
title: Add Menu - Geometry Nodegroups - Hair - Read
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry Nodegroups - Hair - Read
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.64 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Read.odt
---
## Add menu - Hair - Read

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/add-menu-hair-read.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Read](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Curve Info

![Curve Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-info.png)

Reads information about each curve.

#### Output


| Entry | What it does |
| ----------- | ----------------------------------------------- |
| Curve Index | Index of each curve. |
| Curve ID | ID of each curve. |
| Length | Length of each curve. |
| Direction | Direction of each curve. |
| Random | Random Vector of each curve. |
| Surface UV | Attachment surface UV coordinate of each curve. |


### Curve Root

![Curve Root](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-root.png)

Reads information about the root point of each curve.

#### Output


| Entry | What it does |
| -------------- | ----------------------------------------- |
| Root Selection | Boolean selection of curve root points. |
| Root Position | The position of a root point of a curve. |
| Root Direction | Direction of the root segment of a curve. |
| Root Index | Index of the root point of a curve. |


### Curve Segment

![Curve Segment](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-segment.png)

Reads the information of the curve segment before the current point.


| Entry | What it does |
| ----------------- | ------------------------------------------- |
| Output | — |
| Segment Length | Length of the segment |
| Segment Direction | Direction of the segment |
| Neighbor Index | Index of the neighbouring point on segment. |


### Curve Tip

![Curve Tip](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/curve-tip.png)

Reads information about the tip point of each curve.


| Entry | What it does |
| ------------- | ----------------------------------------------------- |
| Output | — |
| Tip Selection | Boolean selection of the tip points. |
| Tip Position | Position of the tip point of a curve. |
| Tip Direction | Direction of the segment of the tip point of a curve. |
| Tip Index | Index of the tip point of a curve. |


### Hair Attachment Info

![Hair Attachment Info](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-read/hair-attachment-info.png)

Reads attatchment information regarding a surface mesh.


| Entry | What it does |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Surface Geometry**: Surface geometry of the curve attachment. · **Surface UV Map**: Surface UV map used for attachment. |
| Output | **Attachment UV**: Surface attachment UV coordinate stored on each curve. · **Attachment is Valid**: Is the attached UV coordinate valid? · **Surface Normal**: The normal direction of the surface mesh at the attachment point. |


