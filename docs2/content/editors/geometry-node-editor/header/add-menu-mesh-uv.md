---
id: editors.geometry-node-editor.header.add-menu-mesh-uv
title: Add Menu - Mesh - UV
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Mesh - UV
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.34 Editors - Geometry Nodes Editor - Header - Add Menu - Mesh - UV.odt
---
## Add menu - UV

![Add menu - UV](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/add-menu-uv.png)

Here you find nodes to modify the UV mapping.

### Pack UV Islands

![Pack UV Islands](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/pack-uv-islands.png)

Pack the UV islands to get the most out of the UV mapping.

#### Inputs


| Entry | What it does |
| --------- | -------------------------------------------------------- |
| UV | The input UV geometry. |
| Selection | A selection of the UV geometry. |
| Margin | How big the gap between the single UV patches should be. |
| Rotate | Rotate island for best fit. |


##### Method

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method.png)

Method used for packing UV Islands.


| Entry | What it does |
| ----------- | ------------------------------------- |
| Bottom Left | Bottom left corner of packing bounds. |
| Top Right | Top right corner of packing bounds. |


#### Outputs

##### UV

The output UV geometry.

### UV Tangent

![UV Tangent](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/uv-tangent.png)

Generate tangent directions based on a UV map.

#### Inputs

##### Method

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method-2.png)

Exact or fast calculation.

##### UV

x and y values of the UV space.

#### Outputs

##### Tangent

The output UV geometry.

### UV Unwrap

![UV Unwrap](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/uv-unwrap.png)

Unwrap the mesh to give it an UV mapping.

#### Inputs


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------- |
| Selection | Which faces of the mesh should be unwrapped. |
| Seam | Mark edges as a seam for unwrapping. |
| Margin | How big the gap between the single UV patches should be. |
| Fill Holes | Virtually fill holes before unwrapping the mesh. This preserves symmetry and can avoids overlaps. |


##### Method

![Method](/docs2/images/editors/geometry-node-editor/header/add-menu-mesh-uv/method-3.png)

The unwrap method.

#### Outputs

##### UV

The output UV geometry.

