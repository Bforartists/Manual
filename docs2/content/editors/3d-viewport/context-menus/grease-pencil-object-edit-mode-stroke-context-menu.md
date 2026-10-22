---
id: editors.3d-viewport.context-menus.grease-pencil-object-edit-mode-stroke-context-menu
title: Grease Pencil object - Edit Mode - Stroke context menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Grease Pencil object - Edit Mode - Stroke context menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.13 Editors - 3D Viewport - Grease Pencil object - Edit Mode - Stroke context menu.odt
---
## Edit Mode - Stroke Context Menu

![Edit Mode - Stroke Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/edit-mode-stroke-context-menu.png)

Call this menu with right click in the 3D viewport. The stroke menu appears in select mode stroke and segment

![Edit Mode - Stroke Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/edit-mode-point-context-menu-2.png)

### Subdivide

Subdivides the selected grease pencil geometry.

#### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-subdivide.png)


| Entry | What it does |
| --------------- | ---------------------------------------------------------------- |
| Number of Cuts | Number of subdivision cuts. |
| Smooth | Smoothen the stroke, not just the new added vertices |
| Repeat | The number of times to repeat the procedure. |
| Selected Points | Limits the effect to only the selected points within the stroke. |
| Position | The operator affects the points location. |
| Thickness | The operator affect the points thickness. |
| Strength | The operator affect the points strength (alpha). |
| UV | The operator affect the UV rotation on the points. |


### Subdivide and Smooth

Subdivides the selected grease pencil geometry.

#### Last Operator Subdivide and Smooth

![Last Operator Subdivide and Smooth](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-subdivide-and-smooth.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------- |
| Number of Cuts | Number of subdivision cuts. |
| Selected Points | Limits the effect to only the selected points within the stroke. |
| Iterations | Number of iterations. |
| Factor | Smooth factor |
| Smooth Endpoints | Smooth endpoints too. |
| Keep Shape | Keep the overall shape. |
| Position | The operator affects the points location. |
| Radius | Smooth radius. |
| Opacity | Smooth Opacity. |


### Set Stroke Type - Sub Menu

![Set Stroke Type - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/set-stroke-type-sub-menu.png)

Defines how selected points are interpreted on the Grease Pencil.


| Entry | What it does |
| ------ | ---------------------------------------------- |
| Stroke | Points are treated as part of a line stroke. |
| Fill | Points are treated as part of a filled region. |
| Both | Points contribute to both stroke and fill. |


### Transform – Sub Menu

![Transform – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/transform-sub-menu.png)

Provides geometric and visual transformations for selected Grease Pencil points or strokes.  
Useful for reshaping, stylizing, and refining drawings with precise control


| Entry | What it does |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To Sphere | Moves selected points toward a spherical distribution.   – Strength slider controls how tightly points conform to a sphere.   – Useful for rounding shapes or creating circular strokes. |
| Shear | Skews selected points along a chosen axis.   – Creates slanted or diagonal distortions.   – Ideal for stylized perspective effects or dynamic motion exaggeration. |
| Bend | Bends selected points around a pivot.   – Angle and pivot settings define curvature.   – Useful for wrapping strokes into arcs or circular motifs. |
| Push/Pull | Moves selected points outward or inward relative to their median center.   – Push expands the shape; Pull contracts it.   – Useful for inflating or compressing stroke geometry. |
| Radius | Adjusts the thickness (point radius) of selected vertices.   – Larger radius = thicker stroke segments.   – Useful for line weight variation or emphasis. |
| Opacity | Changes the transparency of selected vertices.   – Higher values = more opaque; lower values = more transparent.   – Useful for shading, layering, or fade effects in drawings. |


### Smooth

Smoothens out the selected geometry.

#### Last Operator Smooth Stroke

![Last Operator Smooth Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-smooth-stroke.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------ |
| Repeat | How often to repeat the procedure. |
| Factor | The amount of the smoothness to apply. |
| Selected points | When enabled, limits the effect to only the selected points within the stroke. |
| Position | When enabled, the operator affect the points location. |
| Thickness | When enabled, the operator affect the points thickness. |
| Strength | When enabled, the operator affect the points strength (alpha). |
| UV's | When enabled, the operator affect the UV rotation on the points. |


### Move to Layer - Sub Menu

![Move to Layer - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu.png)

![Move to Layer - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu-2.png)

Move the current selected stroke to another grease pencil layer. It lists the current layers.

#### New Layer

New Layer button adds a new grease pencil layer.

##### Last Operator Move Strokes to Layer

![Last Operator Move Strokes to Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-move-strokes-to-layer.png)

###### Grease Pencil Layer

Internal the layers are enumerated. So here you move by number.

![Grease Pencil Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/grease-pencil-layer.png)

The number of a layer can be found out in the tool tip, in the Python part of it.

### Assign Material - Sub Menu

![Assign Material - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu.png)

![Assign Material - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu-2.png)

Assign a new material to the current selected stroke geometry.

The materials can be found and edited in the Properties editor. Here you can also create new materials.

#### Last Operator Change Stroke Color

![Last Operator Change Stroke Color](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-change-stroke-color.png)

##### Material

The materials are defined by its name. So when you want to use another material, then change the name here.

### Set as active material

Sets the current selected material as the active material.

### Arrange Strokes - Sub Menu

![Arrange Strokes - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/arrange-strokes-sub-menu.png)

Changes the drawing order of the strokes in the 2D layer.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------ |
| Bring Forward | Moves the selected points/strokes upper the next one in the drawing order. |
| Send Backward | Moves the selected points/strokes below the previous one in the drawing order. |
| Bring to Front | Moves to the top the selected points/strokes. |


#### Send to Back

Moves to the bottom the selected points/strokes.

##### Last Operator Arrange Stroke

![Last Operator Arrange Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-arrange-stroke.png)

###### Direction

Choose the method again.

### Mirror - Sub Menu

![Mirror - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mirror-sub-menu.png)

Mirror mirrors the selected geometry along the defined axis.


| Entry | What it does |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Interactive Mirror | Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored. |
| X Global, Y Global etc. | Mirrors the selection around the chosen axis. |


#### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.

##### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Snap – Sub Menu

![Snap – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/snap-sub-menu.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

#### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.

#### Offset

If the selection should snap as a whole, or if each individual element of the selection should snap.

### Duplicate

Duplicates the current selection.

When you duplicate a selection, then it sticks to the mouse until you left click. And moves around. A right click repositions the duplicated geometry at its original location.

#### Last Operator Duplicate Strokes

##### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mode.png)

Not to find out. No tool tip, no entry in the Blender manual. Good Job Blender Developers.

##### Move X, Y, Z

Adjust the position.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| Constraint Axis | Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here. |
| Mirror Editing | Edit along a mirror axis. |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


| Entry | What it does |
| ----- | ---------------------------------------------------------------------------- |
| Copy | Copies the selection. |
| Paste | Pastes a copied selection to active layer. You can have more than one layer. |


### Paste by Layer

Pastes a copied selection to same, original layer. You can have more than one layer.

#### Last operator Paste Strokes

![Last operator Paste Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-paste-strokes.png)

##### Type

Choose between the paste methods again.

### Outline

Adds an outline to the grease pencil.

#### Last Operator Outline

![Last Operator Outline](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-outline.png)

##### Projection Mode

![Projection Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/projection-mode.png)

The orientation to project the outline.


| Entry | What it does |
| ------------------- | --------------------------------------------- |
| Radius | Thickness of the outline |
| Offset Factor | Offset from original outline. |
| Corner Subdivisions | How much iterations to subdivide the corners. |


### Split

Splits the selection.

### Separate

![Separate](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-separate-strokes.png)

Separates the selection into a new grease pencil object.

#### Last Operator Separate Strokes

##### Mode

###### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/active-layer.png)

Separate all the strokes at the current active layer.


| Entry | What it does |
| ---------------- | --------------------------------------------------- |
| Selected Strokes | Separate the whole stroke of the current selection. |
| Selected Points | Separate the selected points with its edges. |


