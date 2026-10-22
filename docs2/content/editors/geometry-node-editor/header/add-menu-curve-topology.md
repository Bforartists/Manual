---
id: editors.geometry-node-editor.header.add-menu-curve-topology
title: Add Menu - Curve - Topology
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Curve - Topology
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.23 Editors - Geometry Nodes Editor - Header - Add Menu - Curve - Topology.odt
---
## Add menu - Curve Topology

![Add menu - Curve Topology](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-topology/add-menu-curve-topology.png)

Curve topology related nodes.

### Curve of Point

![Curve of Point](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-topology/curve-of-point.png)

Retrieve the curve of which the control point is part of.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Point Index**: The point index of the curve. · **Offset**: Offset of the point index. |
| Outputs | **Curve Index**: The curve of which the control point is part of. · **Index in Curve**: How far along the curve the control point is. |


### Offset Points in Curve

![Offset Points in Curve](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-topology/offset-points-in-curve.png)

Offset a control point index in the curve.


| Entry | What it does |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Point Index**: The point index of the curve. · **Offset**: Offset of the point index. |
| Outputs | **Is Valid Offset**: Outputs true if the evaluated controlpoint plus the offset is a valid index. · **Point Index**: The index of the control point plus the offset. |


### Points of Curve

![Points of Curve](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-topology/points-of-curve.png)

Retreive a point index within a curve.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Curve Index**: The curve to retreive the data from · **Weights**: Values to sort the curve points. · **Sort Index**: The point to output. |
| Outputs | **Point Index**: The output point. · **Total**: The number of points in the curve. |


