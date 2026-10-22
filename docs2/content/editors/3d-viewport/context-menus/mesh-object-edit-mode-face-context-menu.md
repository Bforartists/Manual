---
id: editors.3d-viewport.context-menus.mesh-object-edit-mode-face-context-menu
title: Mesh Object - Edit Mode - Face Context Menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Mesh Object - Edit Mode - Face Context Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.4 Editors - 3D Viewport - Mesh Object - Edit Mode - Face Context Menu.odt
---
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

###### Merge Factor

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

###### Method Angle based + Conformal

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

###### Method Minimum Stretch

![Method Minimum Stretch](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/method-minimum-stretch.png)

###### Iterations

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

###### Edge Length Mode

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

###### Direction

![Direction](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/direction.png)

Direction is a drop-down box where you can choose in which direction the spherical projection will be mapped.

###### Align

![Align](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/align.png)

Align is a drop-down box where you can choose the Align method.

###### Pole

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

###### Direction

![Direction](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/direction.png)

Direction is a drop-down box where you can choose in which direction the spherical projection will be mapped.

###### Align

![Align](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-face-context-menu/align.png)

Align is a drop-down box where you can choose the Align method.

###### Pole

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

###### Shortest diagonal

Splits the quads based on their distance between vertices.

###### Fixed Alternate

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

###### Unselected

Hides the not selected geometry.

#### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

