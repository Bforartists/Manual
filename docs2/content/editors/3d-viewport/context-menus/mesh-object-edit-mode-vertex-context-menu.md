---
id: editors.3d-viewport.context-menus.mesh-object-edit-mode-vertex-context-menu
title: Mesh Object - Edit Mode - Vertex Context Menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Mesh Object - Edit Mode - Vertex Context Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.2 Editors - 3D Viewport - Mesh Object - Edit Mode - Vertex Context Menu.odt
---
## Vertex Context Menu

![Vertex Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-context-menu.png)

![Vertex Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-context-menu-2.png)

![Vertex Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-context-menu-3.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Mesh object. And in selection mode Vertice to see all its content.

Select geometry to reveal all content.

### Subdivide

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/subdivide.png)

![Subdivide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/subdivide-2.png)

Subdivide divides the selected edges. It subdivides the involved faces too, and can create new vertices.

A more unknown functionality is that it can also randomize the result with the Fractal slider in the Last operator panel.

#### Last Operator Subdivide

![Last Operator Subdivide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-subdivide.png)

##### Number of Cuts

The number of cuts defines the amount of subdivisions.

##### Smoothness

![Smoothness](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/smoothness.png)

This value defines how smooth the subdivision result is. From flat to bent.

##### Create N-Gons

Create N-Gons if required. Else subdividing N-Gons creates Tris.

##### Quad Corner Type

![Quad Corner Type](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/quad-corner-type.png)

Adjust the corner type.


| Entry | What it does |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| Fractal | Randomize the selected vertices. |
| Along Normal | When randomized, this value defines how strong the subdivision follows the normals of the initial vertices. |
| Random Seed | Randomizing value for fractal randomizing. |


### Extrude Vertices

Extrudes out the selected vertices by moving the mouse.

#### Last Operator Extrude Only Vertices and Move

![Last Operator Extrude Only Vertices and Move](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-extrude-only-vertices-and-move.png)

##### Move X Y Z

The coordinates for the extruded geometry.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

Choose the type of orientation, in which coordinate system the action should happen.

##### Mirror Editing

Enable mirror editing.

##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Bevel Vertices

![Bevel Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/bevel-vertices.png)

Adds a bevel at the selected vertices.

#### Last Operator Bevel

![Last Operator Bevel](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-bevel.png)

##### Affect

Affect vertices or edges.

##### Width Type

![Width Type](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/width-type.png)

The width type.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------- |
| Width | The bevel amount. |
| Segments | How many segments gets created. |
| Profile Shape | Controls the Profile shape. 0.5 means round. |
| Material Index | Assigns a material slot to the new bevel faces. -1 is the surrounding material. |


##### Harden Normals

When enabled, the per-vertex face normals of the bevel faces are adjusted to match the surrounding faces, and the normals of the surrounding faces are not affected. This will keep the surrounding faces flat (if they were before), with the bevel faces shading smoothly into them. For this effect to work, custom split normals need to be enabled, which requires Auto Smooth to be enabled (see Normals). As a convenience, that option will be enabled for you if it is not already when you enable Harden Normals here.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clamp Overlap | Do not allow beveled geometry to overlap each other. Prevents bevel geometry from intersecting itself.   Helps avoid messy geometry in tight corners. |
| Loop Slide | Slides new edges along adjacent geometry for better topology flow |
| Mark | **Seams**: Mark the edges of the new created geometry as seams. · **Sharp**: Mark the edges of the new created geometry sharp. |


##### Miter Type

![Miter Type](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/miter-type.png)

###### Miter Outer

How the outer miter is set. Miter is how the bevel rounding at a corner is done.

**Sharp**

![Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/sharp.png)

Creates a sharp miter.

**Patch**

![Patch](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/patch.png)

This replaces the outside vertex of a miter with 3 vertices. And uses a patch pattern there.

**Arc**

![Arc](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/arc.png)

This replaces the vertex of a miter with 2 vertices, joined by an arc. A separate Spread parameter says how far to move the vertices away from their original position.

###### Inner Miter

![Inner Miter](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/miter-type.png)

How the inner miter is set. Miter is how the bevel rounding at a corner is done.

**Sharp**

![Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/sharp.png)

Creates a sharp miter.

**Arc**

![Arc](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/arc.png)

This replaces the vertex of a miter with 2 vertices, joined by an arc. A separate Spread parameter says how far to move the vertices away from their original position.

**Spread**

![Spread](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/spread.png)

Belongs to inner miter method Arc. Adjust how strong the inner radius is bent.

##### Intersection type

![Intersection type](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/intersection-type.png)

The method to use to create meshes at intersections. Bevel can create self intersecting geometry.


| Entry | What it does |
| --------- | ------------------------------------------------------ |
| Grid Fill | Fills intersections with a grid-like topology. |
| Cutoff | Trims or removes overlapping geometry at intersections |


##### Face Strength

![Face Strength](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/face-strength.png)

Set Face Strength on the faces involved in the bevel, according to the specified mode. This can be used in conjunction with a Weight Normals Modifier (with the Face Influence option checked).


| Entry | What it does |
| -------- | -------------------------------------------------------------------------------------------------------------------------- |
| None | Do not set face strength. |
| New | Set the face strength of new faces along edges to Medium, and the face strength of new faces at vertices to Weak. |
| Affected | In addition to those set for the New case, also set the faces adjacent to new faces to have strength Strong. |
| All | In addition to those set for the Affected option, also set all the rest of the faces of the model to have strength Strong. |


###### Profile Type

![Profile Type](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/profile-type.png)

The profile type.

**Superellipse**

Uses a mathematically smooth curve for bevel profiles

**Custom**

Allows manual control of the bevel profile shape via a curve widget.

**Presets**

![Presets](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/presets.png)

Curve presets.

**Navigation elements**


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------------------------- |
| Zoom in and out | The two buttons with the magnifying glass at it zooms in and out in the curve window. |
| Reverse Path | Reverses the curve path. |
| Toggle Profile Clipping | Turns the profile clipping on or off. |


**Tools menu**

![Tools menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/tools-menu.png)


| Entry | What it does |
| ----------- | -------------------------------------- |
| Reset View | Resets the curve windows zoom. |
| Reset Curve | Resets the curve to the initial shape. |


###### Curve view

![Curve view](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/curve-view.png)

Adjust the profile curve.

Left click where no point is adds a new point. Left click at a point allows you to move it.

Holding down Shift while moving a node point activates precision movement.

Holding down ctrl while moving activates temporary snapping.

When a point is selected then the curve view reveals a sub menu at the bottom.

**Handler and node position**

![Handler and node position](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/handler-and-node-position.png)

When you select a node, then the handler and node position tools shows below the curve window.


| Entry | What it does |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Handle Type Auto Handle | Sets the handle type of this curve point to smooth. |
| Handle Type Vector Handle | Sets the handle type of this curve point to sharp. |
| Handle Type Free Handle | Sets the handle type of this curve to Free handles. The curve point has now two handles with which you can adjust the curve before and after the point each. |
| Handle Type Aligned Free Handle | Sets the handle type of this curve to Free handles. The curve point has now a handle with which you can adjust the curve. |
| X Y Values | The position of the currently selected curve point |


| Entry | What it does |
| -------------------- | --------------------------------- |
| Sample straigt edges | Sample edges with vector handles. |
| Sample even length | Sample edges with even lengths. |


### Make Edge/Face

Adds a face when you have edges selected. And Edges when you have Vertices selected. It's a Bridge tool.

You can have either the one method or the other. When you select two adjacent vertices, then you select the edge too. And the tool works in edge mode then. In this case just the possible faces gets created. Not edges between single vertices.

First select the edges or Vertices that you want to bridge. Then click the New Edge/Face from Vertices Button.

![Make Edge/Face](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/make-edge-face.png)

![Make Edge/Face](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/make-edge-face-2.png)

![Make Edge/Face](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/make-edge-face-3.png)

![Make Edge/Face](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/make-edge-face-4.png)

### Connect Vertex Path

![Connect Vertex Path](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/connect-vertex-path.png)

Connect Vertex path connects selected vertices, but takes the vertex order into account in which you selected the vertices. It just creates edges between vertices that are not connected in this order.

### Connect Vertex Pair

![Connect Vertex Pair](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/connect-vertex-pair.png)

Connect Vertex pair connects selected vertices and makes a face of the pairs.

### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

#### Last Operator Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the strength of influence of the tool. |
| Mirror Editing | Enable mirror editing. |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Shrink/Fatten

Shrink/Fatten scales the selected geometry along its normals. Transform orientation and Pivot point gets ignored.

A positive value pushes the vertices outwards. A negative value pushes the vertices inwards.

#### Last Operator Shrink/Fatten

![Last Operator Shrink/Fatten](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-shrink-fatten.png)

The Last Operator Shrink/Fatten panel gives you tools to adjust the Shrink/Fatten operation. Here you have numeric input for the strength and a few more options.


| Entry | What it does |
| -------------- | ---------------------------------------------------------------------- |
| Offset | Offset is the strength of the offset for Shrink/Fatten. |
| Offset Even | Offset Even scales the selection to give more thickness in even areas. |
| Mirror Editing | Enable mirror editing. |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Shear

Shear shears the selection.

#### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-shear.png)

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


##### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enable mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Randomize Vertices

This tool allows randomizes the positions of the selected vertices.

#### Last Operator Randomize

![Last Operator Randomize](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-randomize.png)


| Entry | What it does |
| ----------- | ------------------------------------------ |
| Amount | Adjust the amount. |
| Uniform | The uniform offset distance. |
| Normal | Align the offset direction to the normals. |
| Random Seed | The seed value for randomization. |


### Smooth Laplacian

Laplacian Smooth Vertex smooths out the angles between the selected vertices. It is a tool to reduce noise at the mesh. It works a bit different than the normal Smooth Vertex tool. And gives a different result. The Laplacian method allows you to preserve the volume, and to adjust border smoothing.

#### Last Operator Laplacian Smooth Vertices

![Last Operator Laplacian Smooth Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-laplacian-smooth-vertices.png)


| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Number of Iterations | Number of Iterations is the number of iterations that the smoothing action gets repeated. With 1 the smoothing is just performed once. With 10 it is performed ten times. |
| Lambda Factor | Lambda Factor is the strength of the smoothing. |
| Lambda Factor in border | Lambda Factor is the strength of the smoothing in border areas. |
| Smooth Axis | The Smooth Axis check boxes allows you to limit the smoothing to specific world axis. |
| Preserve Volume | Preserve Volume preserves the volume of the object. |


### Snap Vertices

![Snap Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | Rotate to match the cursor. |


### Mirror Vertices

Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored.

#### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation-2.png)

Orientation is a drop-down box choose the type of orientation for the mirroring action.

##### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

### Vertex Crease

![Vertex Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-crease.png)

When you use a Subdivision Surface Modifier, then you can define the sharpness of selected vertices with this tool. Crease vertices will be marked colored in edit mode.

You will see a value in the header that indicates the current strength when you activate the tool. Move with the mouse to increase or decrease the value. Or type in a value while you are in this mode. You can also scale into negative range.

![Vertex Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-crease-2.png)

A negative crease value will subtract from the current active crease value in case it exists already from a former crease operation. A Crease value of -1 removes the crease from this edge.

#### Last Operator Vertex Crease

![Last Operator Vertex Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-vertex-crease.png)

##### Factor

Adjust the crease factor.

### Merge Vertices

![Merge Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/merge-vertices.png)

Merges the geometry.

#### At Center, At Cursor, Collapse

Merges the geometry with the given methods.

#### Last Operator Merge

![Last Operator Merge](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-merge.png)


| Entry | What it does |
| ----- | ------------------------------------- |
| Type | Choose the merge method again. |
| UV's | Move the UV's according to the merge. |


#### By Distance

Merge the vertices by their distance to each other. This tool is meant to remove double vertices at the same location.

#### Last Operator Merge by Distance

![Last Operator Merge by Distance](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-merge-by-distance.png)


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------- |
| Merge Distance | Adjust the distance below which the vertices gets merged. Merge selected vertices to unselected vertices. |
| Unselected | Merge also unselected vertices |
| Sharp Edges | Calculate sharp edges if possible. |


### Split

Splits the edges between the selected vertices. It creates two edges out of one. And splits the edge by that.

### Separate

![Separate](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/separate.png)

Separate separates the selected geometry, and creates a new object. The geometry becomes uneditable, since it is now a new object. You will have to leave the Edit mode, select the new object, and re-enter Edit mode when you want to edit it.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------ |
| Selection | Selection separates the current selection. |
| By Material | By Material separates all geometry that has the same material than the current selection. |
| By Loose Parts | By Loose parts separates all geometry that is connected by edges to the current selection. |


### Dissolve Vertices

Dissolve Vertices dissolves the selected Vertices.

Note that pressing Del in Vertice select mode calls Dissolve Vertices already. It's the same operator. But you don't get the Last operator that way.

#### Last Operator Dissolve Vertices

![Last Operator Dissolve Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-dissolve-vertices.png)


| Entry | What it does |
| ------------- | ------------------------------------------------------- |
| Face Split | Split off Face corners to maintain surrounding geometry |
| Tear Boundary | Split off Face corners instead of merging faces. |


### Delete Vertices

Deletes the selected vertices.

![Delete Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/delete-vertices.png)

The Show/Hide menu is available for all object types and in all modes. It is usually in the object related menu to find. In Object mode it's the Object menu, for a curve object in edit mode it is the Curve menu. It always contains three menu items. Show Hidden, Hide Selected and Hide Unselected.


| Entry | What it does |
| ------------- | ----------------------------------------------------- |
| Show Hidden | Makes all hidden elements in the scene visible again. |
| Hide Selected | Hides the selected elements. |


### Hide Unselected

Hides the not selected elements. The selected elements stays visible.

#### Last Operator Reveal Hidden / Hide Selected

![Last Operator Reveal Hidden / Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-reveal-hidden-hide-selected.png)

##### Select

Define if the selected or the unselected elements gets hidden or revealed.

