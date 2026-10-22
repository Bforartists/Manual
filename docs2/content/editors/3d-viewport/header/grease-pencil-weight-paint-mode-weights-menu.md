---
id: editors.3d-viewport.header.grease-pencil-weight-paint-mode-weights-menu
title: Grease Pencil - Weight Paint Mode - Weights Menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Header
  - Grease Pencil - Weight Paint Mode - Weights Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.1.33 Editors - 3D Viewport - Header - Grease Pencil - Weight Paint Mode - Weights Menu.odt
---
a

## Weight Paint Mode - Weights Menu

![Weight Paint Mode - Weights Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/weight-paint-mode-weights-menu.png)

### Normalize All

Normalizes the weight of all Vertex groups so that the values for the single vertices in the sum is 1.

#### Last Operator Normalize all Vertex Group

![Last Operator Normalize all Vertex Group](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/last-operator-normalize-all-vertex-group.png)

##### Lock Active

Keep the values of the active group while normalizing others.


| Entry | What it does |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normalize | Normalize normalizes the weight of the current selected Vertex group so that the values for the single vertices in the sum is 1. Means when there is influence from other groups, then those values are kept, but the one for the current group gets lowered so that the sum is 1. |
| Invert | Invert inverts the weight painting for the selected vertex group. |


### Smooth

Smooths the weight for selected vertices.

#### Last Operator Smooth Vertex Group

![Last Operator Smooth Vertex Group](/docs2/images/editors/3d-viewport/header/grease-pencil-weight-paint-mode-weights-menu/last-operator-smooth-vertex-group.png)


| Entry | What it does |
| ---------- | -------------------------------------------- |
| Factor | Here you adjust the factor. |
| Iterations | Here you adjust how many iterations you use. |


### Sample Weight

Pick the weight under the mouse by a click.

