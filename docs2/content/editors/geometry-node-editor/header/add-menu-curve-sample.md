---
id: editors.geometry-node-editor.header.add-menu-curve-sample
title: Add Menu - Curve - Sample
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Curve - Sample
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.19 Editors - Geometry Nodes Editor - Header - Add Menu - Curve - Sample.odt
---
## Add - Curve - Sample

![Add - Curve - Sample](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-sample/add-curve-sample.png)

Here you find curve related nodes.

### Sample Curve

![Sample Curve](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-sample/sample-curve.png)

Calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve.

The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.

In case that the curve contains multiple splines, the sample position is found based on the total accumulated length, including the lengths of all previous splines. The order of the splines is the same order as displayed in the Spreadsheet Editor.

#### Input


| Entry | What it does |
| ----------- | --------------------------------------------------------------------------------------- |
| Curve | The input geometry. |
| Value | Input Value. |
| Mode Factor | **Factor**: The resample amount with method Factor. · **Curve Index**: The curve index. |
| Mode Factor | **Factor**: The resample amount with method Factor. |
| Length | The resample amount with method Length. |


#### Properties

##### Data Type

![Data Type](/docs2/images/editors/geometry-node-editor/header/add-menu-curve-sample/data-type.png)

What data to calculate.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------- |
| Sample Curve Mode | How to calculate the curve. By a factor, or by its length. |
| All Curves | Sample lengths based on the length of all curves. |


#### Output


| Entry | What it does |
| -------- | -------------------------------------------- |
| Value | Output Value. |
| Position | The position at the sample along the spline. |
| Tangent | The normalized curve tangent at the sample. |
| Normal | The normalized curve normal at the sample. |


