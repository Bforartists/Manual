---
id: editors.geometry-node-editor.header.add-menu-geometry-nodegroups-hair-utility
title: Add Menu - Geometry Nodegroups - Hair - Utility
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Geometry Nodegroups - Hair - Utility
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.65 Editors - Geometry Nodes Editor - Header - Add Menu - Geometry Nodegroups - Hair - Utility.odt
---
## Add menu - Hair - Utility

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/add-menu-hair-utility.png)

The nodes in this submenu are node groups. They use the regular single nodes under the hood.

It is virtually impossible to document these nodes in detail. So we will just list them.

When you double click the header, then you will enter the first level of the group. When you then press tab, or click again at the header, then you will reach the single nodes.

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-2.png)

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-3.png)

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-4.png)

To leave the group you can use the breadcrumb up left in the header. These breadcrumbs are clickable. Or the Parent Node Tree button up right in the header.

![Add menu - Hair - Utility](/docs2/images/editors/geometry-node-editor/header/add-menu-generate/add-menu-generate-5.png)

### Attach Hair Curves to Surface

![Attach Hair Curves to Surface](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/attach-hair-curves-to-surface.png)

Attaches hair curves to a surface mesh.

#### Input


| Entry | What it does |
| ----------------------- | -------------------------------------------------------------------- |
| Geometry | The input geometry. |
| Surface Object | A surface object to attach to. It needs to have matching transforms. |
| Surface | Surface geometry to attach hair curves to. |
| Surface UV Map | Surface UV Map used to attach hairs to. |
| Surface Rest Position | Set the surface into rest position before attachment. |
| Sample Attachment UV | Sample the surface UV mapp at the attachment point. |
| Snap to Surface | Snap the root of the curve to the closest surface point. |
| Align to Surface Normal | Align the curves to surface normals. Needs a guide as reference. |
| Blend along Curve | Blend deformation along eacah curve from the root. |


#### Output


| Entry | What it does |
| --------------------- | ---------------------------------------------- |
| Geometry | The output geometry. |
| Surface UV Coordinate | Surface UV Coordinate at the attachment point. |
| Surface Normal | Surface Normal at the attachment point. |


### Redistribute Curve Points

![Redistribute Curve Points](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/redistribute-curve-points.png)

Redistributes existing control points evenly along each curve.


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Input | **Curves**: The input curve. · **Factor**: Factor to blend overall effect. · **Feature Awareness**: Use simple feature awareness to keep feature definition. |
| Output | **Curves**: The output curves. |


### Restore Curve Segment Length

![Restore Curve Segment Length](/docs2/images/editors/geometry-node-editor/header/add-menu-geometry-nodegroups-hair-utility/restore-curve-segment-length.png)


| Entry | What it does |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input | **Curves**: The input curve. · **Selection**: A selection of the input curve. · **Factor**: Factor to blend overall effect. · **Reference Position**: Reference position before deformation. · **Pin at Parameter**: Pin each curve at a certain point for the operation. |
| Output | **Curves**: The output curves. |


