---
id: editors.3d-viewport.header.grease-pencil-edit-mode-point-menu
title: Grease Pencil - Edit mode - Point menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Header
  - Grease Pencil - Edit mode - Point menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.1.29 Editors - 3D Viewport - Header - Grease Pencil - Edit mode - Point menu.odt
---
## Edit Mode - Point Menu

![Edit Mode - Point Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/edit-mode-point-menu.png)

### Extrude

Extrude selected points and move them. The new points stay connected with the original points of the stroke.

Extrude does not show in Select mode Stroke.

#### Last Operator Extrude Stroke Points

![Last Operator Extrude Stroke Points](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-extrude-stroke-points.png)

##### Move

The vector coordinates. They start relative to the initial vector.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/orientation.png)

The orientation in which the extrude happens.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | — |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Smooth

Smoothens out the selected geometry.

#### Last Operator Smooth Stroke

![Last Operator Smooth Stroke](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/last-operator-smooth-stroke.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------ |
| Repeat | How often to repeat the procedure. |
| Factor | The amount of the smoothness to apply. |
| Selected points | When enabled, limits the effect to only the selected points within the stroke. |
| Position | When enabled, the operator affect the points location. |
| Thickness | When enabled, the operator affect the points thickness. |
| Strength | When enabled, the operator affect the points strength (alpha). |
| UV's | When enabled, the operator affect the UV rotation on the points. |


### Vertex Groups

![Vertex Groups](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/vertex-groups.png)

![Vertex Groups](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/vertex-groups-2.png)

This menu contains just the Add New Group button.

#### Add New Group

Adds a new group.

### Set Corner Type submenu

![Set Corner Type submenu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/set-corner-type-submenu.png)

Sets the corner type of the selected corners to the methods round, flat or sharp.

