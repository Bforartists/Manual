---
id: editors.3d-viewport.grease-pencil.edit
title: "Edit Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Grease Pencil"
  - "Edit Mode"
version: "5.1"
status: draft
icon: editmode_hlt
summary: "Edit the grease pencil itself: every header menu, tool, sidebar tab and context menu of Edit Mode."
order: 20
source:
  - "7.1.27 Editors - 3D Viewport - Header - Grease Pencil - Edit mode - Grease Pencil menu.odt"
  - "7.1.29 Editors - 3D Viewport - Header - Grease Pencil - Edit mode - Point menu.odt"
  - "7.1.30 Editors - 3D Viewport - Header - Grease Pencil - Edit mode - Stroke menu.odt"
  - "7.2.12 Editors - 3D Viewport - Tool Shelf - Grease Pencil - Edit Mode.odt"
  - "7.0.12 Editors - 3D Viewport - Grease Pencil object - Edit Mode - Point context menu.odt"
  - "7.0.13 Editors - 3D Viewport - Grease Pencil object - Edit Mode - Stroke context menu.odt"
replaces:
  - editors.3d-viewport.header.grease-pencil-edit-mode-grease-pencil-menu
  - editors.3d-viewport.header.grease-pencil-edit-mode-point-menu
  - editors.3d-viewport.header.grease-pencil-edit-mode-stroke-menu
  - editors.3d-viewport.tool-shelf.grease-pencil-edit-mode
  - editors.3d-viewport.context-menus.grease-pencil-object-edit-mode-point-context-menu
  - editors.3d-viewport.context-menus.grease-pencil-object-edit-mode-stroke-context-menu
---
Grease Pencil › Edit Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Grease Pencil menu

### Edit Mode - Grease Pencil Menu

![Edit Mode - Grease Pencil Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/edit-mode-grease-pencil-menu.png)

### Transform submenu

![Transform submenu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/transform-submenu.png)

#### To Sphere

Transforms the selected geometry into a sphere shape.

##### Last Operator To Sphere

![Last Operator To Sphere](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-to-sphere.png)


| Entry | What it does |
| -------------- | ------------------------- |
| Factor | The transform factor. |
| Mirror Editing | Edit mirror geometry too. |


###### Proportional Editing

![Proportional Editing](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/proportional-editing.png)

###### Proportional editing

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Shear

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.

##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-shear.png)

###### Offset

Adjust an offset.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines one axis of the imaginary shear axis plane.

###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/header/object-menu/axis.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------- | -------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Bend

Bends the selection.

#### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

##### Last Operator Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the distance of influence of the tool. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Radius

Scales the selected geometry of a curve along its normals. Grease pencil is under the hood a curve. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-transform.png)

###### Values

The transform values.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/axis.png)

The transform axis.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Opacity

Changes the transparency of selected Grease Pencil vertices. Higher values = more opaque; lower values = more transparent. This is useful for shading, layering, or fade effects in drawings.

To use, activate then drag left or right to change the stroke opacity.

> **Note:** This does not affect fill opacity, only stroke.

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-transform.png)

###### Values

The transform values.

###### Axis

![Axis](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/axis.png)

The transform axis.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Mirror submenu

![Mirror submenu](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/mirror.png)

Mirror mirrors the selected geometry along the defined axis.

#### Interactive Mirror

Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored

#### X Global, Y Global etc.

Mirrors the selection around the chosen axis.

##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/x-global-y-global-etc.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Orientation is a drop-down box . Choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Snap submenu

#### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/snap-sub-menu.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last operator Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/active-layer.png)

Set the active layer

#### New Layer

![New Layer](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/new-layer.png)

Add a new greasepencil layer. A popup will appear where you can add the name.

#### Layers

The list of the available layers.

### Animation

#### Insert Blank Key frame ( Active Layer )

![Insert Blank Key frame ( Active Layer )](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/insert-blank-key-frame-active-layer.png)

Inserts a key frame into the active layer.

#### Insert Blank Key frame ( All Layers )

Inserts a key frame into all layers.

#### Last Operator Insert Blank Frame

![Last Operator Insert Blank Frame](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-insert-blank-frame.png)

Some snap operations shows a last operation panel, some not.

##### All Layers

Insert into active layer or into all layers.

#### Duplicate Active Key frame ( Active Layer )

Duplicates the active key frame in the active layer.

#### Duplicate Active Key frame ( All Layers )

Duplicates the active key frame in all layers.

#### Last Operator Insert Blank Frame

![Last Operator Insert Blank Frame](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-insert-blank-frame-2.png)

Some snap operations shows a last operation panel, some not.

##### Mode

Duplicate the active key frame in the active layer or in all layers.

#### Delete Active Key frame ( Active Layer )

Deletes the active key frame in the active layer.

#### Delete Active Key frame ( All Layers )

Deletes the active key frame in all layers

### Single Operators

#### Interpolate Sequence

![Interpolate Sequence](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/interpolate-sequence.png)

Interpolate strokes between the previous and next keyframe by adding multiple keyframes. When you are on a frame between two keyframes and click the sequence button, then a breakdown keyframe will be added on every frame between the previous and next keyframe.

#### Duplicate

Duplicates the current selection. This can be a single control point or a whole curve.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the orientation.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable Mirror Editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


| Entry | What it does |
| ----- | ---------------------------------------------------------------------------- |
| Split | Split selected points to a new stroke. |
| Copy | Copies the selection. |
| Paste | Pastes a copied selection to active layer. You can have more than one layer. |


#### Paste by Layer

Pastes a copied selection to same, original layer. You can have more than one layer.

##### Last operator Paste Strokes

![Last operator Paste Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-paste-strokes.png)

###### Type

Choose between the paste methods again.

#### Dissolve

![Dissolve](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/dissolve.png)

Dissolve is a union operation. Two edges becomes one edge by removing the vertice in between.


| Entry | What it does |
| ---------------- | ----------------------------------------------------- |
| Dissolve | Dissolves the selection. |
| Dissolve Between | Dissolves the vertices between the selected vertices. |


##### Dissolve Unselect

Dissolves the vertices that are not selected.

###### Last Operator Dissolve

![Last Operator Dissolve](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-dissolve.png)

###### Type

Choose how you want to dissolve.

#### Delete

![Delete](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/delete.png)


| Entry | What it does |
| ------------------------------------- | --------------------------------------------------------- |
| Delete | Delete selected stroke points. |
| Delete Active Key frame(Active Layer) | Deletes the active key frame in the current active layer. |
| Delete Active Key frame(All Layers) | Deletes the active key frame in all layers. |


#### Cleanup sub menu

![Cleanup sub menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/cleanup-sub-menu.png)

##### Clean Loose Points

Deletes not connected stroke geometry that is made of loose points.

###### Last Operator Clean Loose Points

![Last Operator Clean Loose Points](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-clean-loose-points.png)

###### Limit

The number of vertices below which a stroke gets counted as a loose point.

##### Delete Duplicated Frames

Deletes all duplicated frames.

###### Last Operator Clean Duplicated Frames

![Last Operator Clean Duplicated Frames](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-clean-duplicated-frames.png)

###### Type

![Type](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/type.png)

Delete just in the selected frames or in all frames.

##### Merge by Distance

Merge selected geometry that is in a specific range to each other.

###### Last Operator Merge by Distance

![Last Operator Merge by Distance](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-merge-by-distance.png)


| Entry | What it does |
| ---------- | ---------------------------------------------------------------------------- |
| Threshold | Delete just in the selected frames or in all frames. |
| Unselected | Also merge geometry by distance that is not selected but part of the stroke. |


##### Re project Strokes

Re project the selected strokes onto a new plane from the current viewport. So that all strokes are on one plane.

###### Re project Strokes menu

![Re project Strokes menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/re-project-strokes-menu.png)

Using this tool opens a popup menu. Choose the projection type method.

###### Last Operator Re projectStrokes

![Last Operator Re projectStrokes](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-re-projectstrokes.png)

###### Projection Type

A popup menu. Choose the projection type method.

##### Remove Fill Guides

In Draw mode with the fill tool you are able to draw so called fill guide with holding down the Alt key. They act as the boundary of the fill area. This tool removes these fill guides.

###### Last Operator Remove Fill Guides

![Last Operator Remove Fill Guides](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-remove-fill-guides.png)

###### Mode

![Mode](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/mode.png)

All frames or just the current frame.

#### Show / Hide

![Show / Hide](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/show-hide.png)

##### Show Hidden

Makes all curve geometry in the scene visible again.

##### Hide Selected

Hides the selected curve geometry.

###### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/header/curve-edit-mode-curve-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected curve geometry.

##### Hide Unselected

Hides the not selected curve geometry. The selected geometry stays visible.

#### Outline

Convert selected strokes to perimeter.

##### Last Operator Outline

![Last Operator Outline](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/last-operator-outline.png)


| Entry | What it does |
| ------------------ | ---------------------------------- |
| Projection mode | Hides the not selected layers. |
| Radius | The radius. |
| Offset Factor | The offset factor. |
| Corner Subdivision | The corner subdivision resolution. |


#### Separate sub menu

![Separate sub menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-grease-pencil-menu/separate-sub-menu.jpg)

Separates the selection into a new grease pencil object.


| Entry | What it does |
| ---------------- | ----------------------------------------------------- |
| Selected Points | Separate the selected points with its edges. |
| Selected Strokes | Separate the whole stroke of the current selection. |
| Active Layer | Separate all the strokes at the current active layer. |


##### Last Operator Separate Strokes

###### Mode

###### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/active-layer.png)

Separate all the strokes at the current active layer.


| Entry | What it does |
| ---------------- | --------------------------------------------------- |
| Selected Strokes | Separate the whole stroke of the current selection. |
| Selected Points | Separate the selected points with its edges. |

## Point menu

### Edit Mode - Point Menu

![Edit Mode - Point Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/edit-mode-point-menu.png)

#### Extrude

Extrude selected points and move them. The new points stay connected with the original points of the stroke.

Extrude does not show in Select mode Stroke.

##### Last Operator Extrude Stroke Points

![Last Operator Extrude Stroke Points](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-extrude-stroke-points.png)

###### Move

The vector coordinates. They start relative to the initial vector.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/orientation.png)

The orientation in which the extrude happens.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | — |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Smooth

Smoothens out the selected geometry.

##### Last Operator Smooth Stroke

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


#### Vertex Groups

![Vertex Groups](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/vertex-groups.png)

![Vertex Groups](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/vertex-groups-2.png)

This menu contains just the Add New Group button.

##### Add New Group

Adds a new group.

#### Set Corner Type submenu

![Set Corner Type submenu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-point-menu/set-corner-type-submenu.png)

Sets the corner type of the selected corners to the methods round, flat or sharp.

## Stroke menu

### Edit Mode - Stroke Menu

![Edit Mode - Stroke Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/edit-mode-stroke-menu.png)

![Edit Mode - Stroke Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/edit-mode-stroke-menu-2.png)

The menu content changes dependant of the Select mode. In Select mode Stroke a few menu items are not displayed. Since they do not work in that mode.

![Edit Mode - Stroke Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/edit-mode-stroke-menu-3.png)

#### Subdivide

Subdivides the selected grease pencil geometry.

##### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/last-operator-subdivide.png)


| Entry | What it does |
| --------------- | ---------------------------------------------------------------- |
| Number of Cuts | Number of subdivision cuts. |
| Selected Points | Limits the effect to only the selected points within the stroke. |


#### Subdivide and smooth

Subdivides the selected grease pencil geometry, and smoothens it.

##### Last Operator Subdivide

###### Number of Cuts

![Number of Cuts](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/number-of-cuts.png)

Number of subdivision cuts.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------- |
| Selected Points | Limits the effect to only the selected points within the stroke. |
| Iterations | How often to smooth. |
| Factor | The smoothing factor |
| Smooth Endpoints | Smoothen the endpoints. |
| Keep Shape | Try to keep the original shape. |
| Position | The operator affects the points location. |
| Radius | The smooth radius around vertices. |
| Opacity | The smooth opacity. |


#### Simplify Strokes - Sub Menu

![Simplify Strokes - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/simplify-strokes-sub-menu.png)

Stroke mode. Simplify the stroke.


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed | Deletes every second point in the stroke, except the start and end points. |
| Adaptive | This method uses an algorithm called RDP algorithm (Ramer-Douglas-Peucker algorithm) for points deletion. The algorithm tries to keep the shape with the remaining points. |
| Sample | Samples points along the shape of the stroke, and increases the length of the edges. |
| Merge | Simplify the stroke by merging vertices closer than a given distance. |


##### Last Operator Simplify Stroke

![Last Operator Simplify Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-simplify-stroke.png)

The simplify strokes operators share the same last operator.

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mode-2.png)

The method.


| Entry | What it does |
| ----------------- | -------------------------------------------------------- |
| Steps (Fixed) | How much levels of simplifying. |
| Factor (Adaptive) | How strong the simplification should be performed. |
| Length (Sample) | The sample length. |
| Distance (Merge) | The distance. Below this value the vertices gets merged. |


#### Join - Sub Menu


| Entry | What it does |
| ------------- | ------------------------------------- |
| Join and Copy | Copy the selection in the new stroke. |
| Join | Move the selection to the new stroke. |


##### Adjust last operator Join Selection

![Adjust last operator Join Selection](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/adjust-last-operator-join-selection.png)

###### Type

Choose the join method.

#### Outline

Convert selected strokes to perimeter.

##### Adjust last operator Outline

![Adjust last operator Outline](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/adjust-last-operator-outline.png)

###### Projection mode

![Projection mode](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/projection-mode.png)

How to project the stroke.


| Entry | What it does |
| ------------------- | --------------------------------- |
| Radius | How big. |
| Offset Factor | Offset from the stroke. |
| Corner Subdivisions | How much subdivisions at corners. |


#### Move to Layer – Sub Menu

![Move to Layer – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu-2.png)

![Move to Layer – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu.png)

Move the current selected stroke to another grease pencil layer. It lists the current layers.

##### New Layer

New Layer button adds a new grease pencil layer.

###### Last Operator Move Strokes to Layer

![Last Operator Move Strokes to Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-move-strokes-to-layer.png)

###### Grease Pencil Layer

Internal the layers are enumerated. So here you move by number.

![Grease Pencil Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/grease-pencil-layer.png)

The number of a layer can be found out in the tool tip, in the Python part of it.

#### Assign Material – Sub Menu

![Assign Material – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu.png)

![Assign Material – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu-2.png)

Assign a new material to the current selected stroke geometry.

The materials can be found and edited in the Properties editor. Here you can also create new materials.

##### Last Operator Change Stroke Color

![Last Operator Change Stroke Color](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-change-stroke-color.png)

###### Material

The materials are defined by its name. So when you want to use another material, then change the name here.

#### Set as active material

Sets the current selected material as the active material.

#### Arrange Strokes - Sub Menu

![Arrange Strokes - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/arrange-strokes-sub-menu.png)

Changes the drawing order of the strokes in the 2D layer.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------ |
| Bring Forward | Moves the selected points/strokes upper the next one in the drawing order. |
| Send Backward | Moves the selected points/strokes below the previous one in the drawing order. |
| Bring to Front | Moves to the top the selected points/strokes. |


##### Send to Back

Moves to the bottom the selected points/strokes.

###### Last Operator Arrange Stroke

![Last Operator Arrange Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-arrange-stroke.png)

###### Direction

Choose the method again.

#### Close

Closes the current stroke by connecting the first vertice with the last vertice by a stroke. See also Toggle Cyclic.

#### Toggle Cyclic

When the curve is open, then it Closes the current stroke by connecting the first vertice with the last vertice by a stroke. When the curve is closed, then it removes the connection between first and last vertice, and makes the curve open.

##### Last Operator Set Cyclical State

![Last Operator Set Cyclical State](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/last-operator-set-cyclical-state.png)


| Entry | What it does |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type | Choose the method again. · **Close all**: Close all open selected strokes. · **Open all**: Open all closed selected strokes. · **Toggle**: Close or Open selected strokes as required. |
| Create geometry | When enabled, points are added for closing the strokes like when using the Close tool. If disabled, the stroke is closed with just one edge. |


#### Set Caps - Sub Menu

![Set Caps - Sub Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/set-caps-sub-menu.png)

Toggles if the start and endpoints of the strokes are rounded or flat.

##### Default

![Default](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/default.png)

Sets stroke start and end points to rounded (default).


| Entry | What it does |
| ----- | ----------------------------------------------------------- |
| Both | Toggle stroke start and end points caps to flat or rounded. |
| Start | Toggle stroke start point cap to flat or rounded. |
| End | Toggle stroke end point cap to flat or rounded. |


##### Last Operator Set Caps Mode

![Last Operator Set Caps Mode](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/last-operator-set-caps-mode.png)

###### Type

Choose the method again.

#### Switch Direction

Switches the direction of the stroke geometry.

#### Set Start Point

![Set Start Point](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/set-start-point.png)

Select which point is the start point of the grease pencil curve. This defines the order of point indices, useful for Geometry nodes.

> **Note:** Not available in stroke selection mode.

#### Normalize Thickness

Adjust the thickness of the stroke.

#### Normalize Opacity

Adjust the opacity of the stroke.

##### Last operator Normalize Stroke

![Last operator Normalize Stroke](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/last-operator-normalize-stroke.png)

This last operator works for both tools, Normalize Thickness and Normalize Opacity.

###### Mode

![Mode](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/mode.png)

Adjust thickness or opacity.

###### Value

The value to adjust the opacity or thickness.

#### Set Spline Type – Sub Menu

![Set Spline Type – Sub Menu](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/set-spline-type-sub-menu.png)

Set the curve type.

#### Set Curve Resolution

Set the resolution of the curve.

##### Ajust last operator Set Curve Resolution

![Ajust last operator Set Curve Resolution](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/ajust-last-operator-set-curve-resolution.png)

###### Resolution

The resolution that you want to choose.

#### Set Stroke Type - Sub Menu

![Set Stroke Type - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/set-stroke-type-sub-menu.png)

Defines how selected points are interpreted on the Grease Pencil.


| Entry | What it does |
| ------ | ---------------------------------------------- |
| Stroke | Points are treated as part of a line stroke. |
| Fill | Points are treated as part of a filled region. |
| Both | Points contribute to both stroke and fill. |


#### Reset UVs

Reset UV Transformation values to zero.

#### Join Fills

![Join Fills](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/join-fills.png)

![Join Fills](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/join-fills-2.png)

Combines selected strokes into a single fill region. If they overlap, it will create a subtractive boolean. Useful for merging complex shapes into one continuous fill for coloring or shading.

- Creates unified fill areas, even across multiple strokes.  
    – Automatically generates holes if overlapping strokes define enclosed spaces.

#### Separate Fills

![Separate Fills](/docs2/images/editors/3d-viewport/header/grease-pencil-edit-mode-stroke-menu/separate-fills.png)

Splits a combined fill back into individual fill regions. Useful for isolating specific areas for recoloring, shading, or animation. Restores stroke-based independence after a join operation.

# Tool Shelf

## Tools

### Tool Shelf - Grease Pencil - Edit Mode

![Tool Shelf - Grease Pencil - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/tool-shelf-grease-pencil-edit-mode.png)

Here you can find tools to edit the curve geometry of the grease pencil strokes.

#### Tweak, Select, Transform, 3D Cursor Measure and Annotate tools

The tweak, select, transform, 3d cursor, measure and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Pen

Extrude selected curve points to the mouse click position.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/tool-settings.png)

###### Radius

The thickness of the generated stroke.

###### Stroke Placement

![Stroke Placement](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/stroke-placement.png)

Where to place the stroke, relative to what element.

###### Drawing Plane

![Drawing Plane](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/drawing-plane.png)

What view plane to use for drawing.

#### Radius

![Radius](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/radius.png)

Bezier curves have a radius. This is displayed by the black lines that points away from the curve. The radius tool allows you to resize this radius.

##### Header Value

![Header Value](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/header-value-2.png)

When you resize the curve radius then you will see a value in the header. It tells you the current scale factor. This factor always starts with 1.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-4.png)

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-transform.png)


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------------- |
| Values X Y Z W | The axis to increase the radius. Just X has an effect with the curve radius. |
| Axis | The axis to use. This has no effect with a curve object. |


###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Adjust the orientation of the extrusion. It usually starts with Normal.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Bend

Bends the selection.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/header-values.png)

When you move the mouse then you will see some values in the header, which shows the current scale factor. This value is relative to the starting value, which always starts with 1.

#### Shear / To Sphere Tools group

![Shear / To Sphere Tools group](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/shear-to-sphere-tools-group.png)

##### Shear


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


###### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current scale factor. This value is relative to the starting value, which always starts with 1.

###### Hotkeys

As shown in the header, you can press X or Y to set the shear axis.

###### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/tool-settings-6.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Choose the orientation for the shear action.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


###### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Defines the other axis of the imaginary shear axis plane.

###### Orientation

Choose the orientation for the shear action.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### To Sphere

Transforms the selection into a sphere shape.


| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Snapping | Holding down Ctrl activates temporary global snapping. |
| Precision movement | When you hold down shift, then you will have a much slower but also much preciser movement. |


###### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/header-values-3.png)

When you move the mouse then you will see some values in the header, which shows the current to sphere factor. This value is relative to the starting value, which always starts with 0.

##### Last Operator To Sphere

![Last Operator To Sphere](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/last-operator-to-sphere.png)

###### Factor

The factor to transform the selection into a shape form.

###### Mirror Editing

Enables Mirror Editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Interpolate

Interpolate grease pencil strokes between animation frames.

##### Active Tool panel

![Active Tool panel](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/active-tool-panel.png)

###### Layer

![Layer](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/layer.png)

Layers included in the interpolation.

###### Exclude Breakdowns

Exclude existing breakdowns keyframes as interpolation extremes.

###### Flip Mode

![Flip Mode](/docs2/images/editors/3d-viewport/tool-shelf/grease-pencil-edit-mode/flip-mode.png)

The method to invert destination stroke to match start and end with source stroke.


| Entry | What it does |
| ---------- | -------------------------------------------------------------------------------- |
| Smooth | Amount of smoothing to apply to interpolate strokes, to reduce jitter and noise. |
| Iterations | Number of times to smooth newly created strokes. |


#### Gradient

Draw a line to set the fill material gradient for the selected stroke.

# Context Menus

## Point context menu

### Edit Mode - Point Context Menu

![Edit Mode - Point Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/edit-mode-point-context-menu.png)

Call this menu with right click in the 3D viewport.

![Edit Mode - Point Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/edit-mode-point-context-menu-2.png)

#### Extrude

Extrude selected points and move them. The new points stay connected with the original points of the stroke.

##### Last Operator Extrude Stroke Points

![Last Operator Extrude Stroke Points](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-extrude-stroke-points.png)

###### Move

The vector coordinates. They start relative to the initial vector.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/orientation.png)

The orientation in which the extrude happens.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Edit along a mirror axis. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Subdivide

Subdivides the selected grease pencil geometry.

##### Last Operator Subdivide

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


#### Subdivide and Smooth

Subdivides the selected grease pencil geometry.

##### Last Operator Subdivide and Smooth

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


#### Set Stroke Type - Sub Menu

![Set Stroke Type - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/set-stroke-type-sub-menu.png)

Defines how selected points are interpreted in the  
Options:


| Entry | What it does |
| ------ | ---------------------------------------------- |
| Stroke | Points are treated as part of a line stroke. |
| Fill | Points are treated as part of a filled region. |
| Both | Points contribute to both stroke and fill. |


#### Transform – Sub Menu

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


#### Smooth Points

Smoothens out the selected geometry.

##### Last Operator Smooth Stroke

![Last Operator Smooth Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-smooth-stroke.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Repeat | How often to repeat the procedure. |
| Factor | The amount of the smoothness to apply. |
| Selected points | When enabled, limits the effect to only the selected points within the stroke. |
| Position | When enabled, the operator affect the points location. |
| Thickness | When enabled, the operator affect the points thickness. |
| Strength | When enabled, the operator affect the points strength (alpha). |
| UV's | When enabled, the operator affect the UV rotation on the points. in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Set Start Point

![Set Start Point](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/set-start-point.png)

Select which point is the start point of the grease pencil curve. This defines the order of point indices, useful for Geometry nodes.

> **Note:** Not available in stroke selection mode.

#### Set Corner Type - Sub Menu

Defines how selected corners are treated on the vertices of the Grease Pencil Useful for controlling the visual style, sharpness, and behavior of corners in strokes.

##### Round

![Round](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/round.png)

Smooths the corner into a curved transition. Ideal for organic shapes, soft edges, or stylized drawing. Automatically adjusts point handles to create a rounded arc.

##### Flat

![Flat](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/flat.png)

Creates a straight, flat corner with no curvature. Useful for blocky, mechanical, or architectural forms. Ensures the corner remains linear and angular.

##### Sharp

![Sharp](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/sharp.png)

Marks the corner as a sharp transition. Preserves a distinct angle between segments.  
Commonly used for precise, technical shapes or hard edges.

#### Mirror - Sub Menu

![Mirror - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mirror-sub-menu.png)

Mirror mirrors the selected geometry along the defined axis.


| Entry | What it does |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Interactive Mirror | Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored. |
| X Global, Y Global etc. | Mirrors the selection around the chosen axis. |


##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

#### Snap- Sub Menu

![Snap- Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/snap-sub-menu.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.

##### With Offset

If the selection should snap as a whole, or if each individual element of the selection should snap.

#### Duplicate

Duplicates the current selection.

When you duplicate a selection, then it sticks to the mouse until you left click. And moves around. A right click repositions the duplicated geometry at its original location.

##### Last Operator Duplicate Strokes

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mode.png)

Not to find out. It has no tooltip and is not documented upstream.

###### Move X, Y, Z

Adjust the position.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.

###### Mirror Editing

Edit along a mirror axis.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Copy

Copies the selection.

#### Paste

Pastes a copied selection to active layer. You can have more than one layer.

##### Last operator Paste Strokes

![Last operator Paste Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-paste-strokes.png)

###### Type

Choose between the paste methods again.

#### Merge by Distance

![Merge by Distance](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/merge-by-distance.png)

Merges seleceted vertices by distance.


| Entry | What it does |
| ---------------- | ----------------------------------------------------- |
| Dissolve | Dissolves the selection. |
| Dissolve Between | Dissolves the vertices between the selected vertices. |


#### Dissolve Unselect

Dissolves the vertices that are not selected.

##### Last Operator Dissolve

![Last Operator Dissolve](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-dissolve.png)

###### Type

Choose how you want to dissolve.

#### Simplify Strokes - Sub Menu

![Simplify Strokes - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/simplify-strokes-sub-menu.png)

Stroke mode. Simplify the stroke.


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed | Deletes every second point in the stroke, except the start and end points. |
| Adaptive | This method uses an algorithm called RDP algorithm (Ramer-Douglas-Peucker algorithm) for points deletion. The algorithm tries to keep the shape with the remaining points. |
| Sample | Samples points along the shape of the stroke, and increases the length of the edges. |
| Merge | Simplify the stroke by merging vertices closer than a given distance. |


##### Last Operator Simplify Stroke

![Last Operator Simplify Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-simplify-stroke.png)

The simplify strokes operators share the same last operator.

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mode-2.png)

The method.


| Entry | What it does |
| ----------------- | -------------------------------------------------------- |
| Steps (Fixed) | How much levels of simplifying. |
| Factor (Adaptive) | How strong the simplification should be performed. |
| Length (Sample) | The sample length. |
| Distance (Merge) | The distance. Below this value the vertices gets merged. |


#### Outline

Adds an outline to the grease pencil.

##### Last Operator Outline

![Last Operator Outline](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-outline.png)

###### Projection Mode

![Projection Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/projection-mode.png)

The orientation to project the outline.


| Entry | What it does |
| ------------------- | --------------------------------------------- |
| Radius | Thickness of the outline |
| Offset Factor | Offset from original outline. |
| Corner Subdivisions | How much iterations to subdivide the corners. |


#### Separate

Separates the selection into a new grease pencil object.

##### Last Operator Separate Strokes

![Last Operator Separate Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-separate-strokes.png)

###### Mode

###### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/active-layer.png)

Separate all the strokes at the current active layer.


| Entry | What it does |
| ---------------- | --------------------------------------------------- |
| Selected Strokes | Separate the whole stroke of the current selection. |
| Selected Points | Separate the selected points with its edges. |


#### Set Spline Type – Sub Menu

![Set Spline Type – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/set-spline-type-sub-menu.png)

Convert the curve type of the grease pencil to another curve type. These different curve types allows you different ways of modification.


| Entry | What it does |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Catmull Rom | Generates smooth curves passing through all control points.   Produces natural, flowing strokes with minimal manual adjustment.   Best for organic shapes and freehand drawing cleanup. |
| Poly | Represents strokes as straight line segments between points. No interpolation is applied. |
| Bézier | Converts strokes into Bézier curves with editable handles. Provides precise control over curvature and tangents. |
| NURBS | Uses Non-Uniform Rational B-Splines for interpolation. Allows smooth curves with weighted control points. |


##### Last Operator Separate Strokes

![Last Operator Separate Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-separate-strokes-2.png)


| Entry | What it does |
| --------- | ---------------------------------------------------------------- |
| Type | The curve types. |
| Threshold | The distance that the resulting points are allowed to be within. |


#### Set Handle Type – Sub Menu

![Set Handle Type – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/set-handle-type-sub-menu.png)

Defines how control point handles behave when editing curves or strokes.  
Useful for shaping curvature, controlling tangents, and refining stroke flow in both Grease Pencil and curve objects.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto | Automatically positions handles to create smooth, natural curves.   Handles adjust dynamically as points are moved. |
| Vector | Creates straight, angular transitions at the control point.   Handles point directly toward adjacent vertices. |
| Align | Keeps both handles aligned in opposite directions.   Ensures smooth, symmetrical transitions through the control point. |
| Free | Allows each handle to move independently.   Provides maximum flexibility for custom curve shaping.   Best for fine-tuning irregular or stylized strokes. |
| Toggle Free/Align | Switches between Free and Align modes for the selected point. |

## Stroke context menu

### Edit Mode - Stroke Context Menu

![Edit Mode - Stroke Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/edit-mode-stroke-context-menu.png)

Call this menu with right click in the 3D viewport. The stroke menu appears in select mode stroke and segment

![Edit Mode - Stroke Context Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/edit-mode-point-context-menu-2.png)

#### Subdivide

Subdivides the selected grease pencil geometry.

##### Last Operator Subdivide

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


#### Subdivide and Smooth

Subdivides the selected grease pencil geometry.

##### Last Operator Subdivide and Smooth

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


#### Set Stroke Type - Sub Menu

![Set Stroke Type - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/set-stroke-type-sub-menu.png)

Defines how selected points are interpreted on the Grease Pencil.


| Entry | What it does |
| ------ | ---------------------------------------------- |
| Stroke | Points are treated as part of a line stroke. |
| Fill | Points are treated as part of a filled region. |
| Both | Points contribute to both stroke and fill. |


#### Transform – Sub Menu

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


#### Smooth

Smoothens out the selected geometry.

##### Last Operator Smooth Stroke

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


#### Move to Layer - Sub Menu

![Move to Layer - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu.png)

![Move to Layer - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/move-to-layer-sub-menu-2.png)

Move the current selected stroke to another grease pencil layer. It lists the current layers.

##### New Layer

New Layer button adds a new grease pencil layer.

###### Last Operator Move Strokes to Layer

![Last Operator Move Strokes to Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-move-strokes-to-layer.png)

###### Grease Pencil Layer

Internal the layers are enumerated. So here you move by number.

![Grease Pencil Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/grease-pencil-layer.png)

The number of a layer can be found out in the tool tip, in the Python part of it.

#### Assign Material - Sub Menu

![Assign Material - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu.png)

![Assign Material - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/assign-material-sub-menu-2.png)

Assign a new material to the current selected stroke geometry.

The materials can be found and edited in the Properties editor. Here you can also create new materials.

##### Last Operator Change Stroke Color

![Last Operator Change Stroke Color](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-change-stroke-color.png)

###### Material

The materials are defined by its name. So when you want to use another material, then change the name here.

#### Set as active material

Sets the current selected material as the active material.

#### Arrange Strokes - Sub Menu

![Arrange Strokes - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/arrange-strokes-sub-menu.png)

Changes the drawing order of the strokes in the 2D layer.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------ |
| Bring Forward | Moves the selected points/strokes upper the next one in the drawing order. |
| Send Backward | Moves the selected points/strokes below the previous one in the drawing order. |
| Bring to Front | Moves to the top the selected points/strokes. |


##### Send to Back

Moves to the bottom the selected points/strokes.

###### Last Operator Arrange Stroke

![Last Operator Arrange Stroke](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-stroke-context-menu/last-operator-arrange-stroke.png)

###### Direction

Choose the method again.

#### Mirror - Sub Menu

![Mirror - Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mirror-sub-menu.png)

Mirror mirrors the selected geometry along the defined axis.


| Entry | What it does |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Interactive Mirror | Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored. |
| X Global, Y Global etc. | Mirrors the selection around the chosen axis. |


##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

#### Snap – Sub Menu

![Snap – Sub Menu](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/snap-sub-menu.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.

##### Offset

If the selection should snap as a whole, or if each individual element of the selection should snap.

#### Duplicate

Duplicates the current selection.

When you duplicate a selection, then it sticks to the mouse until you left click. And moves around. A right click repositions the duplicated geometry at its original location.

##### Last Operator Duplicate Strokes

###### Mode

![Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/mode.png)

Not to find out. It has no tooltip and is not documented upstream.

###### Move X, Y, Z

Adjust the position.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box. Choose the type of orientation for the mirroring action.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| Constraint Axis | Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here. |
| Mirror Editing | Edit along a mirror axis. |


###### Proportional editing

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


#### Paste by Layer

Pastes a copied selection to same, original layer. You can have more than one layer.

##### Last operator Paste Strokes

![Last operator Paste Strokes](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-paste-strokes.png)

###### Type

Choose between the paste methods again.

#### Outline

Adds an outline to the grease pencil.

##### Last Operator Outline

![Last Operator Outline](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-outline.png)

###### Projection Mode

![Projection Mode](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/projection-mode.png)

The orientation to project the outline.


| Entry | What it does |
| ------------------- | --------------------------------------------- |
| Radius | Thickness of the outline |
| Offset Factor | Offset from original outline. |
| Corner Subdivisions | How much iterations to subdivide the corners. |


#### Split

Splits the selection.

#### Separate

![Separate](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/last-operator-separate-strokes.png)

Separates the selection into a new grease pencil object.

##### Last Operator Separate Strokes

###### Mode

###### Active Layer

![Active Layer](/docs2/images/editors/3d-viewport/context-menus/grease-pencil-object-edit-mode-point-context-menu/active-layer.png)

Separate all the strokes at the current active layer.


| Entry | What it does |
| ---------------- | --------------------------------------------------- |
| Selected Strokes | Separate the whole stroke of the current selection. |
| Selected Points | Separate the selected points with its edges. |
