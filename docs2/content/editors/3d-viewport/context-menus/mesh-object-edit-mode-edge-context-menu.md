---
id: editors.3d-viewport.context-menus.mesh-object-edit-mode-edge-context-menu
title: Mesh Object - Edit Mode - Edge Context Menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Mesh Object - Edit Mode - Edge Context Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.3 Editors - 3D Viewport - Mesh Object - Edit Mode - Edge Context Menu.odt
---
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

###### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

