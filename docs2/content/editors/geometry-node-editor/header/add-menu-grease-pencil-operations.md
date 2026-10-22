---
id: editors.geometry-node-editor.header.add-menu-grease-pencil-operations
title: Add Menu - Grease Pencil - Operations
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - Add Menu - Grease Pencil - Operations
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.26 Editors - Geometry Nodes Editor - Header - Add Menu - Grease Pencil - Operations.odt
---
## Add menu - Grease Pencil - Operations

![Add menu - Grease Pencil - Operations](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/add-menu-grease-pencil-operations.png)

Grease Pencil nodes.

### Grease Pencil to Curves

![Grease Pencil to Curves](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/grease-pencil-to-curves.png)

Converts a grease pencil geometry to a curve geometry


| Entry | What it does |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inputs | **Grease Pencil**: The grease pencil geometry. · **Selection**: A selection of the grease pencil geometry. · **Layers as Instances**: Generate a separate curve instance for every layer. |
| Outputs | **Curves**: Curves output. |


### Merge Layers

![Merge Layers](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/merge-layers.png)

Merge all grease pencil layers into one layer

#### Grease Pencil

![Grease Pencil](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/grease-pencil.png)

The grease pencil geometry.


| Entry | What it does |
| --------- | -------------------------------------------- |
| Selection | A selection of the grease pencil geometry. |
| Group ID | In By Group ID mode. Input a group ID value. |


#### Properties

![Properties](/docs2/images/editors/geometry-node-editor/header/add-menu-grease-pencil-operations/properties.png)

##### Mode


| Entry | What it does |
| ----------- | -------------------------------------------- |
| By Name | Combine all layers which have the same name. |
| By Group ID | Combine all layers by a provided Group ID. |


#### Outputs

##### Grease Pencil

Grease Pencil geometry output.

