---
id: editors.3d-viewport.mesh.edit.context-menus
title: "Context Menus"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Edit Mode"
  - "Context Menus"
version: "5.1"
status: draft
icon: menu
summary: "The right-click menus of Mesh › Edit Mode."
order: 40
cta: "Open"
---
# Edge Context Menu

## Edge Context Menu

![Edge Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-context-menu.png)

![Edge Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-context-menu-2.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Mesh object. And in selection mode Edge.

![Edge Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-context-menu-3.png)

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


### Extrude Edges

Extrudes out the selected edges by moving the mouse.

#### Last Operator Extrude Only Edges and Move

![Last Operator Extrude Only Edges and Move](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-extrude-only-edges-and-move.png)


| Entry | What it does |
| ------------ | ------------------------------------------ |
| Flip Normals | Flip the normals at the involved faces. |
| Move X Y Z | The coordinates for the extruded geometry. |


#### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Choose the type of orientation, in which coordinate system the action should happen.


| Entry | What it does |
| --------------- | ---------------------- |
| Constraint Axis | — |
| Mirror Editing | Enable mirror editing. |


#### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Bevel Edges

![Bevel Edges](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/bevel-edges.png)

Adds a bevel at the selected edges.

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

##### Miter Outer

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

##### Inner Miter

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


##### Profile Type

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


##### Curve view

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

### Bridge Edge loops

![Bridge Edge loops](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/bridge-edge-loops.png)

The Bridge edge loops tool bridges selected edges, and adds a polygon between them. You need to have at least two edges selected.

#### Last Operator Bridge Edge loops

![Last Operator Bridge Edge loops](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-bridge-edge-loops.png)


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Connect Loops | Choose the method how to deal with bridging multiple loops. |
| Merge | With merge ticked it will not create a bridge face, but merge the selected edges. · **Merge Factor**: The merge factor determines at which distance between the selected edges the merge happens. 0.5 is the middle of the selected edges. |
| Twist | The twist offset for closed loops. |
| Number of Cuts | Adds cuts to the bridge face. |
| Interpolation | Choose the interpolation mode for the cuts. |
| Smoothness | Adjust the smoothness for the cuts. |
| Profile Factor | Adjust the profile factor for the cuts. |
| Profile shape | Adjust the profile shape for the cuts. |


### Fill

![Fill](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/fill.png)

Fill closes holes in the selected mesh geometry, and triangulates the faces.

#### Last Operator Fill

##### Beauty

![Beauty](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/beauty.png)

Uses the best possible triangulation.

### Loop Cut and Slide

![Loop Cut and Slide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/loop-cut-and-slide.png)

Loop Cut and Slide adds edge loops to divide faces

When you click once, then this edge gets created. When you click and hold, then you can move this edge to a new location.

Loop cut and Slide ignores selections. It will try to divide the face under the mouse, and continue the loop until it is closed, or until it cannot continue.

#### Last Operator Loop Cut and Slide

![Last Operator Loop Cut and Slide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-loop-cut-and-slide.png)

Note that all settings here just changes the latest added loop. Not all added loops in the current session.

##### Number of Cuts

The number of cuts that gets added. It can be more than one loop at once.

##### Smoothness

![Smoothness](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/smoothness.png)

This value defines how smooth the loop cut gets added. From flat to bent.

##### Falloff

![Falloff](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/falloff.png)

Adjust the Falloff type for smoothness.


| Entry | What it does |
| -------------- | -------------------------------------------------------------------- |
| Factor | Change the center of the added loop. |
| Even | Make the edge loop match the shape of the adjacent edge loop |
| Flipped | When Even mode is active, flips between the two adjacent edge loops. |
| Clamp | Clamp within the edge extend. |
| Mirror Editing | Enable mirror editing. |
| Correct UV's | Corrects the UV's when modifying the geometry. |


### Offset Edge Slide

![Offset Edge Slide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/offset-edge-slide.png)

Adds left and right an edge from the selected edge and slides it outwards.

#### Last Operator Offset Edge Slide

![Last Operator Offset Edge Slide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-offset-edge-slide.png)

##### Cap Endpoint

![Cap Endpoint](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/cap-endpoint.png)

Connects the endpoints of the slided edges.


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------- |
| Factor | The amount of sliding. |
| Even | Make the edge loop match the shape of the adjacent edge loop |
| Flipped | Connected with Even. When even mode is active then flips between the two adjacent edge loops. |
| Clamp | Clamp within the edge extends. |
| Mirror Editing | Enable mirror editing. |
| Correct UV's | Correct UV coordinates when transforming. |


### Knife Topology

![Knife Topology](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/knife-topology.png)

The Knife tool cuts the geometry, and adds edges. When it crosses existing geometry then it adds a vertice at the crossing point.

Usage: activate the tool, left click to define the starting point. This can also be a point in the middle of a face. But ideally you choose an existing vertice or an edge as the start and endpoints. The knife tool tries to snap to them when you get close with the mouse cursor.

When done press Enter or Space bar to confirm. Right click abandons the operation.

When you create a vertice in the middle of a face, then the knife tool will try to connect this vertice by an existing vertice of this face when you confirm with space bar.

#### Hotkey functionality in the footer text

![Hotkey functionality in the footer text](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/hotkey-functionality-in-the-footer-text.png)

Have a look at the footer when you work with this tool. Here you will find further instructions and hotkeys.

Enter, Pad Enter, Space bar - confirm

Esc key, RMB - cancel the operation

LMB start the cut

Double LMB - close the cut

E - create new cut

Ctrl or Shift while dragging - Snap to the middle of an edge

Z - cut through the whole geometry, also the back faces.

MMB - pan the view.

Alt MMB - rotate the view.

### Rotate Edge CW

![Rotate Edge CW](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/rotate-edge-cw.png)

Rotate Edge rotates the selected edge clockwise.

#### Last Operator Rotate Selected Edge

##### Counter Clockwise

![Counter Clockwise](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/counter-clockwise.png)

Rotate selected edges counter clockwise.

### Edge Split

![Edge Split](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-split.png)

Splits selected edges so that each neighbor face gets its own copy. You have two methods here.

#### Last Operator Edge Split

![Last Operator Edge Split](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-edge-split.png)

##### Type

Choose the method again.

### Edge Crease

![Edge Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-crease.png)

When you use a Subdivision Surface Modifier, then you can define the sharpness of selected edges with this tool. Crease edges will be marked colored in edit mode.

You will see a value in the header that indicates the current strength when you activate the tool. Move with the mouse to increase or decrease the value. Or type in a value while you are in this mode. You can also scale into negative range.

![Edge Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/vertex-crease-2.png)

A negative crease value will subtract from the current active crease value in case it exists already from a former crease operation. A Crease value of -1 removes the crease from this edge.

#### Last Operator Edge Crease

![Last Operator Edge Crease](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-edge-crease.png)

##### Factor

Adjust the crease factor.

### Edge Bevel Weight

![Edge Bevel Weight](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-bevel-weight.png)

![Edge Bevel Weight](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-bevel-weight-2.png)

This tool adjusts the edge bevel weight for selected edges when you use the Bevel modifier at the mesh.

You need to have set the limit method to Weight. This way you can achieve a bevel weight for every individual selected edge if you want, and achieve different bevel strengths at the mesh.

You will see a value in the header that indicates the current strength when you activate the tool. Move with the mouse to increase or decrease the value. Or type in a value while you are in this mode. You can also scale into negative range.

![Edge Bevel Weight](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/edge-bevel-weight-3.png)

A negative Edge Bevel Weight value will subtract from the current active crease value in case it exists already from a former crease operation. An Edge Bevel Weight value of -1 removes the weight from this edge.

#### Last Operator Edge Bevel Weight

##### Factor

![Factor](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/factor.png)

Adjust the Edge Bevel Weight factor.

### Mark Sharp

![Mark Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/mark-sharp.png)

Mark Sharp is a tool that you need for the Edge Split modifier. Marked edges are displayed and rendered as sharp edges.

![Mark Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/mark-sharp-2.png)

#### Last Operator Mark Sharp

![Last Operator Mark Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-mark-sharp.png)

##### Vertices

Calculate by the selected vertices instead of edges to mark the edges.

### Clear Sharp

Clears formerly as sharp marked selected edges.

#### Last Operator Mark Sharp

![Last Operator Mark Sharp](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-mark-sharp-2.png)

##### Vertices

Calculate by the selected vertices instead of edges to mark the edges.

### Set sharpness by Angle

Sets the sharpness of edges by their angle to the neighbour face.

#### Last Operator Set sharpness by Angle

![Last Operator Set sharpness by Angle](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-set-sharpness-by-angle.png)


| Entry | What it does |
| ------ | ---------------------------------------------------------- |
| Angle | The angle after which the edge counts as sharp. |
| Extend | Add new sharp edges without clearing existing sharp edges. |


| Entry | What it does |
| -------------------- | -------------------------------------------------------- |
| Mark Freestyle Edge | Mark the selected edges as a Freestyle feature edges. |
| Clear Freestyle Edge | Clears formerly as freestyle feature edges marked edges. |


### Un-Subdivide

![Un-Subdivide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/un-subdivide.png)

Decimates the geometry by trying to make one quad out of four quads. But can also end in Tris where this is not possible.

#### Last Operator Un-Subdivide

##### Iterations

![Iterations](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/iterations.png)

Number of iterations. This means how deep the calculation should go. One level of SDS, two levels, three levels, etc. . Down to the point where you cannot decimate any geometry anymore.

### Split

Splits the edges between the selected vertices. It creates two edges out of one. And splits the edge by that.

### Separate submenu

![Separate submenu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/separate-submenu.png)

Separate separates the selected geometry, and creates a new object. The geometry becomes uneditable, since it is now a new object. You will have to leave the Edit mode, select the new object, and re-enter Edit mode when you want to edit it.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------ |
| Selection | Selection separates the current selection. |
| By Material | By Material separates all geometry that has the same material than the current selection. |
| By Loose Parts | By Loose parts separates all geometry that is connected by edges to the current selection. |


### Dissolve Edges

Dissolve Edges dissolves the selected edges.

Note that pressing Del in Vertice select mode calls Dissolve Vertices already. It's the same operator. But you don't get the Last operator that way.

#### Last Operator Dissolve Edges

![Last Operator Dissolve Edges](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-dissolve-edges.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| Dissolve Vertices | Dissolve remaining vertices which connect to only two edges. |
| Angle threshold | Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. |
| Face Split | Split off Face corners to maintain surrounding geometry |


### Delete Edges

Deletes the selected Edges.

### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/show-hide.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

#### Show Hidden

Makes all geometry in the scene visible again.

#### Hide Selected

Hides the selected geometry.

##### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-hide-selected.png)

##### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

# Face Context Menu

## Face Context Menu

![Face Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/face-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Mesh object. And in selection mode Edge.

![Face Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/face-context-menu-2.png)

![Face Context Menu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/face-context-menu-3.png)

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


### Extrude Faces

Extrudes out the selected faces into the face direction by moving the mouse. When it's more than one face, then the middle will be used.

#### Last Operator Extrude Region and Move

![Last Operator Extrude Region and Move](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-extrude-region-and-move.png)


| Entry | What it does |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Flip Normals | Flips the normals of the extruded faces. |
| Dissolve Orthogonal Edges | Dissolves orthogonal edges. |
| Move X, Y Z | The position. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel. |


##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

#### Mirror Editing

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


### Extrude Faces Along Normals

![Extrude Faces Along Normals](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/extrude-faces-along-normals.png)

Extrudes the selection along local normals.

#### Header Value

![Header Value](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/header-value.png)

This tool works like a shrink fatten extrude. And so you will see a corresponding set of values in the header.

#### Last Operator Extrude Region and Shrink/Fatten

![Last Operator Extrude Region and Shrink/Fatten](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-extrude-region-and-shrink-fatten.png)


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Flip Normals | Flips the normals of the extruded faces. · **Dissolve Orthogonal Edges**: Dissolves orthogonal edges. |
| Offset | The current extrude amount. |
| Offset Even | Scales the offset to give more even thickness. Without this checked the farer away faces will have a bigger extrude amount. |
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


### Extrude Individual

![Extrude Individual](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/extrude-individual.png)

Extrudes the selection along local normals of each individual face.

The method works the same in all Mesh select modes. Vertice, Edge and Face Mode.

#### Header Value

![Header Value](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/header-value.png)

This tool works like a shrink fatten extrude. And so you will see a corresponding set of values in the header.

#### Last Operator Extrude Individual Faces and Move

![Last Operator Extrude Individual Faces and Move](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-extrude-individual-faces-and-move.png)


| Entry | What it does |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- |
| Offset | The current extrude amount. |
| Offset Even | Scales the offset to give more even thickness. Without this checked the farer away faces will have a bigger extrude amount. |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


### Inset Faces

![Inset Faces](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/inset-faces.jpg)

Inset insets edges into the selected faces. Think of it as an extrude inwards the face.

Activate the tool, drag the mouse. But carefully. The control is not the best. You better adjust the amount in the last operator.

#### Last Operator Inset Faces

![Last Operator Inset Faces](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-inset-faces.png)

##### Boundary

With Boundary ticked you will get the connect edges in the corners. Without the edges ends straight.

![Boundary](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/boundary.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------- |
| Offset Even | Scales the offset to give more even thickness. |
| Offset Relative | Scales the offset by surrounding geometry. |
| Edge Rail | Inset the region along existing edges. |
| Thickness | Thickness adjusts the thickness of the inset geometry. |
| Depth | With depth you can bevel the inset geometry. It is then not longer co planar to the initial face. |
| Outset | With outset ticked the Inset will not extrude inwards but outwards. |
| Select Outer | With Select Outer the outer ring will be selected after the Inset. |
| Individual | Inset every face individually. |
| Interpolate | Blend Face Data across the inset. |


### Bridge Faces

The Bridge Faces tool bridges selected faces, and adds polygons between them. You need to have at least two faces selected.

This tool is basically the Bridge Edge Loops tool, just that it operates in Face mode.

Note that this tool just shows when you are in Face Select Mode.

#### Last Operator Bridge Edge loops

##### Connect Loops

Choose the method how to deal with bridging multiple loops.

##### Merge

![Merge](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/merge.png)

With merge ticked it will not create a bridge face, but merge the selected edges.

##### Merge Factor

The merge factor determines at which distance between the selected edges the merge happens. 0.5 is the middle of the selected edges.


| Entry | What it does |
| -------------- | ------------------------------------------- |
| Twist | The twist offset for closed loops. |
| Number of Cuts | Adds cuts to the bridge face. |
| Interpolation | Choose the interpolation mode for the cuts. |
| Smoothness | Adjust the smoothness for the cuts. |
| Profile Factor | Adjust the profile factor for the cuts. |
| Profile shape | Adjust the profile shape for the cuts. |


### Poke Faces

![Poke Faces](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/poke-faces.png)

Splits the selected faces to create a triangulated geometry.

#### Last Operator Poke Faces

##### Poke Offset

![Poke Offset](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/poke-offset.png)

Normally the center vertice of the poke operation is planar with the rest. Adjust an offset.

##### Offset Relative

Scale the offset by surrounding geometry.

![Offset Relative](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/offset-relative.png)

##### Poke Center

![Poke Center](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/poke-center.png)

Poke Center is a drop-down box choose what the center of the poke operation should be. You can choose between weighted mean, mean and bounds.

### UV Unwrap Faces submenu

![UV Unwrap Faces submenu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/uv-unwrap-faces-submenu.png)

The UV menu from the header.

Here you find the UV mapping methods and some further functionality. You use it best in the U Editing layout. There you can see the result in the UV Editor then.

The UV menu is just available for Mesh objects


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unwrap ABF | Unwrap ABF unwraps the selected geometry with the method Angle based. ABF stands for Angle Based Flattening. ABF can give a bit better result than LSCM when unwrapping organic shapes. |
| Unwrap Conformal | Unwrap Conformal unwraps the selected geometry with the method LSCM, which is the short for Least Square Conformal Mapping. LSCM can give a bit better results than ABF with geometric shapes. |


#### Last Operator Unwrap

##### Method

Method is a drop down box where you can choose the unwrap method.

##### Method Angle based + Conformal

![Method Angle based + Conformal](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/method-angle-based-conformal.png)

Unwrap ABF and Unwrap LSCM shares the same Last Operator.

**Method**

Method is a drop down box where you can choose between Unwrap method Angle Based and Conformal.

**Fill Holes**

![Fill Holes](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/fill-holes.png)

Fill holes in the mesh before unwrapping.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------- |
| Use Subdivision Surface | Unwraps an existing Subdivision Modifier. You need to add a Subdivision Modifier first. |
| Correct Aspect | Take the Image Aspect Ratio into account. |


**Margin Method**

![Margin Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/margin-method.png)


| Entry | What it does |
| -------- | ------------------------------------------------ |
| Scaled | Use the scale of existing UV to multiply margin. |
| Add | Just add the margin and ignore any existing UV. |
| Fraction | Specify a precise fraction of specific UV. |


**Margin**

The distance between the single UV patches.

##### Method Minimum Stretch

![Method Minimum Stretch](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/method-minimum-stretch.png)

##### Iterations

Number of iterations.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------- |
| No Flip | Prevent flipping UV's |
| Importance Weight | Take per vertex importance weights into account. |
| Use Subdivision Surface | Unwraps an existing Subdivision Modifier. You need to add a Subdivision Modifier first. |
| Correct Aspect | Take the Image Aspect Ratio into account. |


**Margin Method**

![Margin Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/margin-method.png)


| Entry | What it does |
| -------- | ------------------------------------------------ |
| Scaled | Use the scale of existing UV to multiply margin. |
| Add | Just add the margin and ignore any existing UV. |
| Fraction | Specify a precise fraction of specific UV. |


**Margin**

The distance between the single UV patches.

### Smart UV Project

![Smart UV Project](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/smart-uv-project.png)

Smart UV Project projects the UV mapping from different angles.

#### Smart UV Project Settings dialogue

##### Angle Limit

The Angle Limit defines after which angle the mapping happens from the next side. With an angle of 66 you have around six sides to map from. The calculation is 360/66.

##### Margin Method

![Margin Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/margin-method.png)


| Entry | What it does |
| -------- | ------------------------------------------------ |
| Scaled | Use the scale of existing UV to multiply margin. |
| Add | Just add the margin and ignore any existing UV. |
| Fraction | Specify a precise fraction of specific UV. |


##### Rotation Method

![Rotation Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/rotation-method.png)

How to rotate islands.


| Entry | What it does |
| -------------- | ---------------------------------------------------------- |
| Island Margin | Island Margin defines the distance between the UV patches. |
| Area Weight | Weight Projection Vector by faces with larger areas. |
| Correct Aspect | Take the Image Aspect Ratio into account. |


#### Last Operator Smart UV Project

![Last Operator Smart UV Project](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-smart-uv-project.png)

The Last Operator for Smart UV Project contains the same settings than the Smart UV Project Settings dialogue.

### Lightmap Pack

![Lightmap Pack](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/lightmap-pack.png)

Lightmap Pack maps each face individually, and puts the result into the UV space. Without margin.

Lightmap Pack has no Last Operator.

#### Settings


| Entry | What it does |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| Selection | Selection is a drop-down box where you can choose what will be packed, either Selected Faces or All Faces. |
| Share Tex Space | Map all objects into one lightmap. |
| New UV Map | Create a new UV map for every new mesh. |
| Pack Quality | The pack quality. |
| Margin | The distance between the single UV patches. |


#### Follow Active Quads

Follow Active quads maps UV coordinates starting from an active face, and maps all adjacent faces in quad shape then. This way you can for example unwrap a pipe or a road. You first need to have a face selected. Then select everything. And then click at Follow Active Quads.

##### Settings

![Settings](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/settings.png)

##### Edge Length Mode

Edge Length Mode is a drop-down box where you can choose the Length method.

##### Last Operator Follow Active Quads

![Last Operator Follow Active Quads](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-follow-active-quads.png)

The Last Operator contains the same settings than the Settings dialogue.

#### Cube Projection

Cube Projection maps the mesh from six sides, means cubic.

##### Last Operator Cube Projection

![Last Operator Cube Projection](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-cube-projection.png)


| Entry | What it does |
| --------------- | ---------------------------------------------------------- |
| Cube Size | Cube Size defines the size of the UV mesh in the UV space. |
| Correct Aspect | Take Image Aspect ratio into account. |
| Clip to Bounds | Clip UV Coordinates to bounds after unwrapping. |
| Scale to Bounds | Scale UV Coordinates to bounds after unwrapping. |


#### Cylinder Projection

Cylinder Projection tries to map the geometry cylindric.

##### Last Operator Cylinder Projection

![Last Operator Cylinder Projection](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-cylinder-projection.png)

##### Direction

![Direction](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/direction.png)

Direction is a drop-down box where you can choose in which direction the spherical projection will be mapped.

##### Align

![Align](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/align.png)

Align is a drop-down box where you can choose the Align method.

##### Pole

![Pole](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/pole.png)

How to handle the faces at the poles.


| Entry | What it does |
| --------------- | ------------------------------------------------------------- |
| Preserve Seams | Keep existing seams intact. |
| Radius | Radius defines the Polar size of the UV mesh in the UV space. |
| Correct Aspect | Take Image Aspect ratio into account. |
| Clip to Bounds | Clip UV Coordinates to bounds after unwrapping. |
| Scale to Bounds | Scale UV Coordinates to bounds after unwrapping. |


#### Sphere Projection

Sphere Projection tries to map the geometry spherical.

##### Last Operator Sphere Projection

![Last Operator Sphere Projection](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-sphere-projection.png)

##### Direction

![Direction](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/direction.png)

Direction is a drop-down box where you can choose in which direction the spherical projection will be mapped.

##### Align

![Align](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/align.png)

Align is a drop-down box where you can choose the Align method.

##### Pole

![Pole](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/pole.png)

How to handle the faces at the poles.


| Entry | What it does |
| --------------- | ------------------------------------------------ |
| Preserve Seams | Keep existing seams intact. |
| Correct Aspect | Take Image Aspect ratio into account. |
| Clip to Bounds | Clip UV Coordinates to bounds after unwrapping. |
| Scale to Bounds | Scale UV Coordinates to bounds after unwrapping. |


#### Project from View

Project from View projects the UV from the current 3D view.

##### Last Operator Project from View

![Last Operator Project from View](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-project-from-view.png)


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------ |
| Orthographic | User orthographic projection. |
| Camera Bounds | Map UV's to the camera region taking resolution and aspect into account. |
| Correct Aspect | Take Image Aspect ratio into account. |
| Clip to Bounds | Clip UV Coordinates to bounds after unwrapping. |
| Scale to Bounds | Scale UV Coordinates to bounds after unwrapping. |


#### Project from View (Bounds)

Project from View projects the UV from the current 3D view.

Same as Project from View, but with Scale to Bounds ticked in the Last operator. And so it scales to the bounds.

#### Mark Seam

![Mark Seam](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/mark-seam.png)

The unwrap algorithms Angle based and Conformal requires to have edges marked as seams. Think of it as a cutting pattern for a trouser for example. Such a trouser is also made of fabric patterns.

Same goes for the UV patches when you use Angle based or conformal unwrapping. You need to cut your mesh into parts and mark edges as seams, so that the algorithm knows where the seams are.

Mark seam marks the currently selected edge(s) as a seam. Seam edges will be displayed as red in the 3D viewport.


| Entry | What it does |
| ---------- | ---------------------------------------------------------------- |
| Clear Seam | Clear seam removes the seam from the currently selected edge(s). |
| Reset | Resets the UV Projection. |


### Triangulate Faces

![Triangulate Faces](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/triangulate-faces.png)

Triangulate Faces triangulates the faces of the selected geometry.

#### Last Operator Triangulate Faces

##### Quad Method

![Quad Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/quad-method.png)

Choose how quads should be triangulated.

##### Shortest diagonal

Splits the quads based on their distance between vertices.

##### Fixed Alternate

![Fixed Alternate](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/fixed-alternate.png)

Splits the quads on the second and fourth vertice.


| Entry | What it does |
| ------ | ------------------------------------------------ |
| Fixed | Splits the quads on the first and third vertice. |
| Beauty | Tries to optimize the triangulation. |


##### Polygon Method

![Polygon Method](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/polygon-method.png)

Choose how N-Gons should be triangulated.


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Clip | Splits the polygons with an ear clipping algorithm. |
| Beauty | Tries to optimize the triangulation. |


### Triangles to Quads

![Triangles to Quads](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/triangles-to-quads.png)

Tris to quads tries to convert triangulated geometry back to a quad geometry by removing the edges inside of the quads.

#### Last Operator Tris to Quads

##### Max Face Angle

![Max Face Angle](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/max-face-angle.png)

Adjust the threshold to adjacent triangles.


| Entry | What it does |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| Max Shape Angle | Adjust the shape angle limit. |
| Topology influence | How much to priorize regular grids of qads as well as quads that touch existing quads. |
| Compare UV's | Takes the UV patches for the calculation into account. Border geometry will not be calculated. |
| Compare Color attributes | Takes the Vertex colors for the calculation into account. Border geometry will not be calculated. |
| Compare Seam | Takes the Vertex colors for the calculation into account. Border geometry will not be calculated. |
| Compare Sharp | Takes the as sharp marked edges for the calculation into account. Border geometry will not be calculated. |
| Compare Materials | Takes the Materials colors for the calculation into account. Border geometry will not be calculated. |
| Deselect Joined | Only select remaining triangles that were not merged. |


### Shade Smooth

Sets the shading for the object to smooth. Flat means that every face of the object shows facettet, with a sharp edge. Smooth means that the edges are not longer to see.

![Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-flat.png)

![Shade Smooth](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-smooth.png)

### Shade Flat

Sets the shading for the object to flat. Flat means that every face of the object shows facettet, with a sharp edge. Smooth means that the edges are not longer to see.

![Shade Flat](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-flat.png)

![Shade Flat](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/shade-smooth.png)

### Un-Subdivide

![Un-Subdivide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/un-subdivide.png)

Decimates the geometry by trying to make one quad out of four quads. But can also end in Tris where this is not possible.

#### Last Operator Un-Subdivide

##### Iterations

![Iterations](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/iterations.png)

Number of iterations. This means how deep the calculation should go. One level of SDS, two levels, three levels, etc. . Down to the point where you cannot decimate any geometry anymore.

### Split

Splits the edges between the selected vertices. It creates two edges out of one. And splits the edge by that.

### Separate submenu

![Separate submenu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/separate.png)

Separate separates the selected geometry, and creates a new object. The geometry becomes uneditable, since it is now a new object. You will have to leave the Edit mode, select the new object, and re-enter Edit mode when you want to edit it.


| Entry | What it does |
| -------------- | ------------------------------------------------------------------------------------------ |
| Selection | Selection separates the current selection. |
| By Material | By Material separates all geometry that has the same material than the current selection. |
| By Loose Parts | By Loose parts separates all geometry that is connected by edges to the current selection. |


### Dissolve Faces

Dissolves the selected faces, which unions the involved faces to one.

#### Last Operator Dissolve Vertices

![Last Operator Dissolve Vertices](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-dissolve-vertices.png)

##### Dissolve Vertices

Dissolve remaining vertices.

### Delete Faces

Deletes the selected faces.

### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/show-hide.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

#### Show Hidden

Makes all geometry in the scene visible again.

#### Hide Selected

Hides the selected geometry.

##### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/last-operator-hide-selected.png)

##### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

# Vertex Context Menu

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

##### Miter Outer

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

##### Inner Miter

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


##### Profile Type

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


##### Curve view

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
