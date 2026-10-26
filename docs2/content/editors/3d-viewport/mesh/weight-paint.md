---
id: editors.3d-viewport.mesh.weight-paint
title: "Weight Paint"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Mesh"
  - "Weight Paint"
version: "5.1"
status: draft
icon: wpaint_hlt
summary: "Paint vertex group weights on the mesh: menus, brushes and settings."
order: 40
source:
  - "7.1.19 Editors - 3D Viewport - Header - Mesh - Weight Paint mode - Weights menu.odt"
  - "7.2.5 Editors - 3D Viewport - Tool Shelf - Mesh - Weight Paint Mode.odt"
  - "7.3.9 Editors - 3D Viewport - Sidebar - Tool Tab - Mesh - Weight Paint Mode.odt"
  - "7.0.7 Editors - 3D Viewport - Mesh Object - Weight Paint Mode - Brushes context menus.odt"
replaces:
  - editors.3d-viewport.header.mesh-weight-paint-mode-weights-menu
  - editors.3d-viewport.tool-shelf.mesh-weight-paint-mode
  - editors.3d-viewport.sidebar.tool-tab-mesh-weight-paint-mode
  - editors.3d-viewport.context-menus.mesh-object-weight-paint-mode-brushes-context-menus
---
Mesh › Weight Paint: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Weights menu

### Weight Paint Mode - Weights Menu

![Weight Paint Mode - Weights Menu](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/weight-paint-mode-weights-menu.png)

#### Assign from Bone Envelopes

Weights the vertices from the connected bone envelopes. And takes the distance to the bone envelope into account.

#### Assign Automatic from Bones

Weights the vertices connected with the bone. And takes the distance to the bone into account.

##### Last Operator Weight from Bones

![Last Operator Weight from Bones](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-weight-from-bones.png)

This last operator is the same for both tools. Assign Automatic from Bones, and Assign from Bone Envelopes.

###### Type

Choose if you want to Assign from Bone Envelopes, or from Bones.

#### Normalize All

![Normalize All](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/normalize-all.png)

Normalize all normalizes the weight of all Vertex groups so that the values for the single vertices in the sum is 1.

##### Last Operator Normalize all

| Entry | What it does |
| ----------- | ------------------------------------------------------ |
| Subset | Subset is a drop-down menu choose the Subset method. |
| Lock Active | Normalize just the other groups. Not the active group. |

#### Normalize

Normalize normalizes the weight of the current selected Vertex group so that the values for the single vertices in the sum is 1. Means when there is influence from other groups, then those values are kept, but the one for the current group gets lowered so that the sum is 1.

#### Mirror

Mirror Vertex Group mirrors Vertex Groups and flips weights and/or names. It only edits selected Vertices. It flips when both sides are selected. Otherwise it copies from Unselected.

##### Last Operator Mirror Vertex Group

![Last Operator Mirror Vertex Group](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-mirror-vertex-group.png)

| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------ |
| Mirror Weights | With Mirror Weights ticked it mirrors the weights. |
| Flip Group Names | With Flip Group Names ticked it flips the Group names |
| All Groups | Mirrors all Vertex Groups. |
| Topology Mirror | Uses topology based mirroring. This requires matching mirrored topology. |

#### Invert

Invert inverts the weight painting for the selected vertex group.

##### Last Operator Invert Vertex Group

![Last Operator Invert Vertex Group](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-invert-vertex-group.png)

###### Subset

![Subset](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/subset.png)

Subset is a drop-down menu choose the Subset method.

| Entry | What it does |
| -------------- | ------------------------------------------------------------------- |
| Add Weights | Add Vertices from Groups that have zero Weighting before inverting. |
| Remove Weights | Remove Vertices from Groups that have zero weight after inverting. |

#### Clean

Removes Vertex group assignments that are not required from the active vertex group.

##### Last Operator Clean Vertex Group

![Last Operator Clean Vertex Group](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-clean-vertex-group.png)

###### Subset

Subset is a drop-down menu choose the Subset method.

###### Limit

![Limit](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/subset.png)

Remove weights that are below or equal to the limit value.

###### Keep Single

Keep Vertices assigned to at least one vertex group when cleaning.

#### Quantize

![Quantize](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/quantize.png)

Quantize quantizes the weight paint values. It starts with 4 steps. With a step of 1 you have a single vertex color, no matter how you have painted it before.

##### Last Operator Quantize Vertex Weights

![Last Operator Quantize Vertex Weights](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/subset.png)

| Entry | What it does |
| ------ | ---------------------------------------------------------------------------- |
| Subset | Subset is a drop-down menu choose the Subset method. |
| Steps | Here you adjust in how many steps the weight paint colors should be divided. |

#### Levels

![Levels](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/levels.png)

Adds some offset to the Weight paint, and multiplys it with some gain.

##### Last Operator Levels

###### Subset

Subset is a drop-down menu choose the Subset method.

###### Offset

![Offset](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/subset.png)

Here you adjust the offset.

###### Gain

Here you adjust the gain.

#### Smooth

![Smooth](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/smooth.png)

Smooths the weight for selected vertices.

##### Last Operator Smooth Vertex Weights

###### Subset

Subset is a drop-down menu choose the Subset method.

###### Factor

![Factor](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/subset.png)

Here you adjust the factor.

| Entry | What it does |
| --------------- | -------------------------------------------- |
| Iterations | Here you adjust how many iterations you use. |
| Expand/Contract | Expand or contract the weights. |

#### Transfer Weights

![Transfer Weights](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/transfer-weights.png)

Transfer weights allows you to transfer weights from one object to another object in the same space. For example to copy the weight of a body shape to a covering cloth.

##### Usage

Make sure the target part is at its location.

In Object mode Select the source object(s). Then shift click to select the target object too. This makes the target object the active object

Switch to Weight Paint mode.

Click the Transfer Weight Button, and the weighting should be transferred to the target object.

You can adjust the result in the Last Operator Transfer Mesh Data panel.

![Usage](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/usage.png)

![Usage](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/usage-2.png)

##### Last Operator Transfer Mesh Data

![Last Operator Transfer Mesh Data](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-transfer-mesh-data.png)

###### Freeze Operator

Prevent the operator to rerun when you tweak the settings. So that you can tweak many settings at once, then untick to run the operator again.

###### Data Type

A drop down box choose the data type to work with.

![Data Type](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/data-type.png)

###### Create Data

Add Data layers on target object if needed.

###### Vertex Mapping

![Vertex Mapping](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/vertex-mapping.png)

A drop down box choose the vertex mapping method.

| Entry | What it does |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Auto Transform | Automatically compute transformation to get the best possible match between source and target object. |
| Object Transform | Calculate the objects in Global space. Unticked means the transfer happens from and to the origin of the objects. |
| Only Neighbor Geometry | Source Objects must be closer than given distance to the target objects. |

###### Ray Radius

![Ray Radius](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/ray-radius.png)

The ray distance for Only Neighbor Geometry.

###### Source Layers Selection

![Source Layers Selection](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/source-layers-selection.png)

A drop down box choose the Source Layer selection method.

###### Destination Layers Matching

A drop down box choose the Destination Layers matching.

###### Mix Mode

![Mix Mode](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/mix-mode.png)

A drop down box choose the mix mode. That's how the mapping gets transferred into the target object.

###### Mix Factor

The strength of the chosen mix mode.

#### Limit Total

Limit the number of deform weights for a vertex by removing the lowest weights. For example when five vertex groups are assigned to one vertice, and you set the limit to 4, then the vertice will just be assigned to the four vertex groups with the highest weight. This is useful for game content where the game engine has a limit for how much bones can be connected to one vertice.

#### Last Operator Limit Number of Weights

![Last Operator Limit Number of Weights](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-limit-number-of-weights.png)

| Entry | What it does |
| ------ | ------------------------------------------------------------------- |
| Subset | A drop down box choose to work with the Active Group or All Groups. |
| Limit | Set the limit. |

#### Set Weight

![Set Weight](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/set-weight.png)

This tool is just active when you have either Face Selection Masking or Vertex Selection Masking activated.

The tool fills the selection with the current active weight color that you have adjusted in the Brush panel in the Tools tab in the Tool shelf.

#### Locks

![Locks](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/locks.png)

Locks is a sub menu with which you can modify the vertex group locks in the properties editor.

The names should be self explaining.

![Locks](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/locks-2.png)

##### Last Operator Change Lock

![Last Operator Change Lock](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/last-operator-change-lock.png)

###### Action

![Action](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/action.png)

Choose the locking method again.

###### Mask

![Mask](/docs2/images/editors/3d-viewport/header/mesh-weight-paint-mode-weights-menu/mask.png)

Choose what vertex groups should be affected.

# Tool Shelf

## Tools

### Tool Shelf - Mesh - Weight Paint Mode

![Tool Shelf - Mesh - Weight Paint Mode](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/tool-shelf-mesh-weight-paint-mode.png)

In Vertex Paint mode with a mesh object you will find mainly brushes in the tool shelf. Vertex painting allows you to paint the vertices of a mesh object with a specific color. This can then be used in various ways. As direct painting without any UV mapping. Or for some special calculations. There is a shader node that reads the vertex color values.

#### Transform and Annotate tools

![Transform and Annotate tools](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/transform-and-annotate-tools.png)

The transform and annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.  
The transform tools group shows when you activate Paint Mask or Vertex selection sub modes.

#### Brush cursor

When you activate one of the brushes then the mouse cursor turns into a brush cursor. This cursor represents the size of the current brush. It does not align with the surface under the mouse. But always faces towards you.

![Brush cursor](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/brush-cursor.png)

#### Brushes settings

The different brushes settings can be found in the sidebar in the tools tab. Or in the properties editor in the Active Tool and Workspace settings tab. Or above the header area.

The different brushes settings in the Active Tool and Workspace settings are explained in the chapter 25.1.4 Editors - Properties Editor - Tools Tab - Vertex Paint Mode

We won't cover this chapters again, but just explain what the different brushes does.

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/brushes-settings.png)

![Brushes settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/brushes-settings-2.png)

#### Symmetry

![Symmetry](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/symmetry.png)

You can enable Symmetry painting up right in the header.

#### Hotkeys

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/hotkeys.png)

Pressing F allows you to change the brush size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/hotkeys-2.png)

Pressing Shift F allows you to change the strength of the brush. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

![Hotkeys](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/hotkeys-3.png)

Pressing Ctrl F allows you to change the weight size onscreen. Drag the mouse to increase or decrease the size. Left click applies the new size, right click cancels the resizing.

#### Brush

![Brush](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/brush.png)

Paint brush.

| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Blur | Smooths out the colors of adjacent vertices. In this mode the Color Value is ignored. The strength defines how much the colors are blurred. |
| Average | Smooths color by painting the average resulting color from all colors under the brush. |
| Smear | Smudges colors by grabbing the colors under the brush and “dragging” them. |

#### Gradient

![Gradient](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/gradient.png)

Allows you to draw a gradient between two defined points. The gradient gets drawn with the starting color at the start point, and the color for zero weight at the end point.

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/tool-settings.png)

| Entry | What it does |
| -------- | ------------------------------------------------------------- |
| Weight | The starting weight. |
| Strength | The strength with which it mixes with the existing weighting. |
| Type | Choose the gradient type. Linear or Radial. |

###### Falloff

![Falloff](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/falloff.png)

Allows you to adjust the falloff by a curve.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/curve-presets.png)

Curve presets to choose from.

###### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

###### Adding Points

![Adding Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/adding-points.png)

You can add new curve points by simply left clicking at the curve. Move the mouse to position them where you need it.

###### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/navigation-elements.png)

The navigation elements at the top are described from left to right.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom in and out | The two buttons with the magnifying glass at it zooms in and out in the curve window. |
| Tools | Tools is a menu where you can find some curve related tools. · **Reset View**: Resets the curve windows zoom. · **Vector Handle**: Set handle type to Vector. · **Auto Handle**: Set handle type to Auto. · **Auto Clamped Handle**: Set handle type to Auto Clamped. · **Reset Curve**: Resets the curve to the initial shape. |

###### Use Clipping

![Use Clipping](/docs2/images/editors/3d-viewport/header/header-tools-and-options/use-clipping.png)

Clipping options. Set up clipping for the stroke. The blue button at the top turns clipping on or off.

###### Delete Points

Deletes the selected curve point.

###### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/curve-presets-2.png)

Predefined curve presets.

##### Last Operator Weight Gradient

![Last Operator Weight Gradient](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/last-operator-weight-gradient.png)

###### Type

Choose the gradient type. Linear or Radial.

#### Sample tools group

![Sample tools group](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/sample-tools-group.png)

##### Sample Weight

Sets the actual weight value to the color under the mouse.

![Sample Weight](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/sample-weight.png)

The mouse turns into a picker. When clicking at the mesh with that picker, the header shows the weight value of the weighting of the corresponding vertice under the mouse

##### Sample Vertex Group

![Sample Vertex Group](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/sample-vertex-group.png)

Opens a popup menu where you can select one of the vertex groups that are under the mouse.

# Sidebar

## Weight Paint Mode

### Tools tab in Weight Paint Mode

![Tools tab in Weight Paint Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/tools-tab-in-weight-paint-mode.png)

The Tools tab in Weight Paint Mode provides you the tools to do weight painting at a mesh. Skinned characters for example.

The vertices becomes a "weighting" assigned in this process. Means a per centage influence of the bone to a vertice. And under the hood you create vertex groups with the vertices that are assigned to the bones.

The amount of influence is defined by the weight paint color. Pure red has an influence value of 1. Pure blue has an influence value of 0. And the gradients between red and blue defines the in between steps in the 0-1 range. This is needed since there can be more than one bone influence and deform a vertice. Usually at the transition areas between two bones. The green areas in this shot.

The Weight Paint mode is just available for mesh objects.

#### Weight painting at characters

The main purpose for Weight painting is to weight the skin for characters. So that they deform proper when you pose your armature.

##### Skinning

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning.png)

To do weight painting at a character you first have to assign the mesh to the armature. This process is called skinning. The mesh becomes the "skin" for the skeleton.

Let's do a quick run through skinning. You can skin in Object Mode. But also from Pose Mode. Lock Object Modes needs to be unticked to get it to work from Pose Mode, which it is by default. In case you have it on, untick it now.

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning-2.png)

Create an object, create an armature

First we activate Display "in Front" for the armature. So that we can still see the armature inside of the mesh.

Position the mesh at its final location.

Now select the Mesh, hold down Shift key, and select the Armature. Both should be selected now.

Dive into the Object menu in the header of the 3D view, and search for Parent, with automatic weights. You can also press the hotkey Ctrl P. This calls the parenting menu under the mouse position.

Here we choose "With Automatic Weights". Automatic weighting means that the bones grabs the nearest vertices within a given radius, and assigns them to this bone.

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning-3.png)

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning-4.png)

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning-5.png)

When everything went well then the mesh, in our case the Cylinder, is now part of the hierarchy of the armature.

And when you select the armature, and switch to Pose mode now, then you can already deform the mesh by posing the armature.

![Skinning](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/skinning-6.png)

##### Enter and leave Weight painting

Weight painting should happen in Pose mode so that you can pose your mesh to see the resulting deforming.

When you simply select the mesh, and enter the weight paint mode, then you can weightpaint the mesh. However, you cannot change the bone. Since the armature is not selected.

So you need to select the armature too when you want to do weight painting. Select the armature, hold down shift, select the mesh, then enter weight paint mode.

![Enter and leave Weight painting](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/enter-and-leave-weight-painting.png)

When you do everything right then you will see a bone symbol in the header.

##### Face Selection Mode

![Face Selection Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/face-selection-mode.png)

The face selection mode allows using selection operators to define a mask based on faces for weight painting. You can then use the weight paint brush tools and operators to assign new weight to the selection.

##### Vertex Selection Mode

![Vertex Selection Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/vertex-selection-mode.png)

The vertex selection mode allows using selection operators to define a mask for based on vertex selection for weight painting. You can then use the weight paint brush tools and operators to assign new weight to the selection.

##### Bone Selection Mode

The weighting that gets displayed in the Bone Selection mode when you enter Weight Paint mode and the armature is in Pose mode. The last active bone defines which vertex group you will weight paint. With this method to define the bone to define where you want to weight paint and assign weight accordingly. You can also switch bones while in weight painting mode on the active mesh object.

![Bone Selection Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/enter-and-leave-weight-painting.png)

To switch bones while weight painting, hold down **Ctrl**, and **left click** at the bone that you want to set active. Then the weighting for this bone gets displayed.

Be careful. You can select the bones in the hierarchy of the outliner. But it does not change the active bone to do the weightpainting. Even when it shows selected, the active bone for weightpainting is still unchanged. And another trap, you can change the active bone in the dropdown at the top. But this one does not change the selected bone. So best is to hold down Ctrl and left click to change the active bone.

![Bone Selection Mode](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/bone-selection-mode.png)

#### Weight painting a plain mesh

You can also do weight painting without an armature. Just at the pure mesh. In this case you just create the vertex groups for the mesh. And those vertex groups can be accessed in edit mode then for further usage. As shown in the shots below.

![Weight painting a plain mesh](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/weight-painting-a-plain-mesh.png)

![Weight painting a plain mesh](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/weight-painting-a-plain-mesh-2.png)

#### Weight painting in combination with particles

You can also combine weight painting with particles. To influence the density of hair for example. The weightmap can be assigned in the Vertex Groups panel in the Particles tab.

![Weight painting in combination with particles](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/weight-painting-in-combination-with-particles.png)

### Brush Asset Panel

![Brush Asset Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/brush-asset-panel.png)

The Brush Asset Panel contains the different Brushes and some Brush settings. Choose and adjust your current active brush.

#### Browse Brush

The big image at the top is a dropdown box that allows you to choose a brush. Click at it, and you will see the different brushes. A click at one of the images will choose this brush then.

![Browse Brush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/browse-brush.png)

Brushes are assets. You can load them from different libraries if you want.

#### Brush Specials menu

![Brush Specials menu](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/brush-specials-menu.png)

This menu becomes active when you create a new brush. Which can be done wiht the Plus button in the name property. This data cannot be changed for builtin system brushes.

##### Edit Metadata

![Edit Metadata](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/edit-metadata.jpg)

Calls a popup where you can adjust further informations and settings for the brush.

| Entry | What it does |
| ------------------ | ----------------------------------------------- |
| Catalog | The asset catalog in which the brush is stored. |
| Author | The brush author. |
| Desctription | Add a description |
| OK / Cancel | Accept or decline the changes. |
| Edit Preview Image | Allows you to load a custom preview image. |

| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| Save Brush Asset | This button is just active with a custom brush. It saves all changes made at the brush settings into the current custom brush. |
| Revert Brush Asset | Reverts the brush settings to the default values of the brush in the asset library. |

##### Name

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name.png)

The edit box below the Image shows the name of the current active brush.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT automatically saved when you close Bforartists. You need to save the brush asset. See above.

**The X button** deletes the brush from the brushes list and from the asset library. This button is just active with a custom brush. You will be prompted by a warning so that you don't accidentally remove the brush.

![Name](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/name-2.png)

### Brush Settings Panel

![Brush Settings Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/brush-settings-panel.png)

The Brush Settings Panel contains the Brush settings. The content differs, dependent of which brush you have chosen.

#### Blend

![Blend](/docs2/images/editors/3d-viewport/context-menus/mesh-object-vertex-paint-mode-brushes-context-menus/blend.png)

Define how the stroke will blend. You can choose between various blend modes.

| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weight | Adjust the strength of the weight painting. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. |
| Radius | The Radius edit box allows you to adjust the radius of the brush. The button behind the edit box enables tablet pressure sensitivity for radius. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
| Strength | The Strength edit box allows you to adjust the strength of the brush. The button behind the edit box enables tablet pressure sensitivity for strength. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |

### Brush Settings Panel - Advanced Sub panel

#### Brush Type

![Brush Type](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/brush-type.png)

Displays the current brush type (e.g., **Draw, **Blur, Average, Smear)

### Brush Settings Panel - Stroke Sub panel

![Brush Settings Panel - Stroke Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/brush-settings-panel-stroke-sub-panel.png)

The Stroke panel contains settings to influence the behavior of the brush stroke. There are various stroke methods available. We will go through them one by one.

#### Stroke Panel with Stroke method Space

This is the default Stroke method. The sculpt stroke gets added continuously with given settings.

![Stroke Panel with Stroke method Space](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-space.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/spacing-edit-box.png)

The drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

###### Spacing Pressure

The icon behind the edit box enables tablet pressure sensitivity for tablets.

| Entry | What it does |
| ----------- | ------------------------------------------------------ |
| Dash Ratio | Ratio of samples in a cycle that the brush is enabled. |
| Dash Length | Length of a dash cycle measured in stroke samples. |

##### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |

###### Input Samples Edit Box

![Input Samples Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/input-samples-edit-box.png)

Average multiple input samples together to smooth the brush stroke.

###### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stabilize-stroke.png)

The brush lags behind the mouse position, and produces a much smoother stroke by that.

| Entry | What it does |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Smooth Stroke Radius Edit Box | Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

#### Stroke Panel with Stroke method Curve

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-curve.png)

The Stroke method curve doesn't simply influence the way how the stroke is painted. It is a special method. First you draw a curve object by holding down ctrl and clicking with left mouse button. Then you tweak the curve. You can click at the curve point, and drag out handlers to make the curve points smooth.

Then you hit the Draw Curve button. And the curve gets drawn onto the surface.

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-curve-2.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-curve-3.png)

![Stroke Panel with Stroke method Curve](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-curve-4.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/spacing-edit-box.png)

The drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Paint Curve edit box

![Paint Curve edit box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/paint-curve-edit-box.png)

Here you set the active curve.

**The first element** is a drop down box where you will find your curves objects. You can have more than one.

**The second element** is the edit box that displays the active curve.

**The number** right of it, **in this case 2**, indicates how much number of users ( internally ) this brush uses. This means that this data block (the brush) shares currently settings with at least one other object. Most probably the parent brush where we have created it from. Click at the value to make this brush a single user. The button will vanish then.

**F** set the brush to have a fake user. Zero user data-blocks are normally not saved. But sometimes you want to force the data to be kept even when the data block has no user.

**The + button** allows you to add a new pencil with the current settings. Note that the brushes are NOT saved when you close Bforartists. You can save them into the current blend file. Or you can save the startup file. But be careful here. This saves everything else of the current state of Bforartists too.

**The X button** deletes the brush as the active one. It does NOT delete it from the brushes list.

##### Draw Curve Button

A click at it to turns the curve into a sculpt stroke.

##### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |
| Input Samples Edit Box | Average multiple input samples together to smooth the brush stroke. |

#### Stroke Panel with Stroke method Line

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-line.png)

With Stroke method line you draw a line between a starting point and an endpoint. And when you release the mouse then the line gets sculpted.

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-line-2.png)

![Stroke Panel with Stroke method Line](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-line-3.png)

##### Spacing Edit Box

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/stroke-panel-with-stroke-method-line-4.png)

![Spacing Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/spacing-edit-box.png)

The sculpt drawing happens by mapping the pencil onto the mouse position. And when you move the mouse then the next mapping happens. Adjust the spacing after what mouse movement the next mapping should happen. The lower the value, the lower the distance between the single dots.

The icon behind the edit box enables tablet pressure sensitivity for tablets.

##### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |

##### Input Samples Edit Box

Average multiple input samples together to smooth the brush stroke.

#### Stroke Panel with Stroke method Airbrush

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-airbrush.png)

The stroke acts like an airbrush pencil. The dots gets sprayed randomly.

![Stroke Panel with Stroke method Airbrush](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-airbrush-2.png)

##### Rate Edit Box

Define the rate of the drawing.

##### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |

##### Input Samples Edit Box

Average multiple input samples together to smooth the brush stroke.

##### Smooth Stroke

![Smooth Stroke](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stabilize-stroke.png)

The brush lags behind the mouse position, and produces a much smoother stroke by that.

| Entry | What it does |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Smooth Stroke Radius Edit Box | Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

#### Stroke Panel with Stroke method Dots

![Stroke Panel with Stroke method Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-dots.png)

![Stroke Panel with Stroke method Dots](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stroke-panel-with-stroke-method-dots-2.png)

The stroke method Dots draws dots of the pencil onto the surface. The mapping happens from the current view. Means you will get distortions when your view is not aligned with the surface of the object.

##### Jitter Edit Box

![Jitter Edit Box](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/jitter-edit-box.png)

Add Jitter to the brush while painting.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------- |
| Jitter Pressure | The icon behind the edit box enables tablet pressure sensitivity for tablets. |
| Jitter Unit | If the jitter happens in screen space in pixels, or relative to the brush size. |

##### Input Samples Edit Box

Average multiple input samples together to smooth the brush stroke.

##### Stabilize Stroke

![Stabilize Stroke](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/stabilize-stroke.png)

The brush lags behind the mouse position, and produces a much smoother stroke by that.

| Entry | What it does |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| Smooth Stroke Radius Edit Box | Is just active when Smooth Stroke is activated. Adjust the radius of the smoothing. |
| Smooth Stroke Factor Edit Box | Is just active when Smooth Stroke is activated. Adjust the factor of the smoothing. |

### Brush Settings Panel - Falloff Sub panel

The Falloff panel allows you to define different falloffs methods for the border of the brush.

#### Presets

![Presets](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-sculpt-mode/presets.png)

The different available falloff presets. The method custom allows you to define your own falloff. And reveals a curve panel.

##### Selecting Points

![Selecting Points](/docs2/images/editors/3d-viewport/header/header-tools-and-options/selecting-points.png)

You can select curve points. This reveals two edit boxes for the x and y coordinate of this point.

Selected points can be moved around. Left click at them, hold the mouse button down and move them to a new location.

##### Adding Points

> This setting uses the **curve widget**: click to add points, drag to move them. See **[Curve Widget](../../../interface/properties.md#curve-widget)** in the Interface chapter.

##### Navigation elements

![Navigation elements](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/navigation-elements.png)

The navigation elements at the top are described from left to right.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Zoom in and out | The two buttons with the magnifying glass at it zooms in and out in the curve window. |
| Tools | Tools is a menu where you can find some curve related tools. · **Reset View**: Resets the curve windows zoom. · **Vector Handle**: Set handle type to Vector. · **Auto Handle**: Set handle type to Auto. · **Auto Clamped Handle**: Set handle type to Auto Clamped. · **Reset Curve**: Resets the curve to the initial shape. |

##### Use Clipping

![Use Clipping](/docs2/images/editors/3d-viewport/header/header-tools-and-options/use-clipping.png)

Clipping options. Set up clipping for the stroke. The blue button at the top turns clipping on or off.

##### Delete Points

Deletes the selected curve point.

##### Curve Presets

![Curve Presets](/docs2/images/editors/3d-viewport/tool-shelf/mesh-weight-paint-mode/curve-presets-2.png)

Predefined curve presets as a starting point.

##### Front Face Falloff

###### Angle

![Angle](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-texture-paint-mode/angle-4.png)

Adjust the angle.

### Brush Settings Panel - Cursor Sub panel

![Brush Settings Panel - Cursor Sub panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/brush-settings-panel-cursor-sub-panel.png)

Adjust the color and appearance of the brush cursor to custom values.

#### Cursor Checkbox

Activate the custom settings.

#### Cursor Color

![Cursor Color](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/cursor-color.png)

Choose another color for the brush cursor. Double clicking at the color field will open a color picker.

#### Falloff Opacity

![Falloff Opacity](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-vertex-paint-mode/falloff-opacity.png)

You can turn on the cursor overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.

| Entry | What it does |
| ------------------ | -------------------------------------- |
| Override Overlay | Hide the Cursor Overlay when painting. |
| Use Cursor Overlay | Turn on Cursor Overlay. |

#### Texture Opacity

This is for the case when you paint with a texture brush. You can turn on the Texture overlay with the eye button at the end. The falloff opacity slider allows you to adjust the opacity of this cursor overlay.

| Entry | What it does |
| ------------------ | --------------------------------------- |
| Override Overlay | Hide the Texture Overlay when painting. |
| Use Cursor Overlay | Turn on Texture Overlay. |

### Symmetry Panel

![Symmetry Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/symmetry-panel.png)

The same buttons plus the whole Symmetry Lock Panel as a drop down menu can also be found in the tool settings bar as icon buttons. This allows quicker access and better.

| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mirror Vertex Groups | Mirror the left/right vertex groups when painting. · **Topology Mirror**: Not available with Mirror Vertex Groups deactivated. Use topology based mirroring. Both sides of the mesh needs matching geometry. |
| Mirror | Mirror along given axis. With Mirror Vertex groups on you just can turn on or off the X axis. |
| Radial | Tiling. The number of times to repeat the strokes across the surface. Not available with Mirror Vertex Groups activated. |

### Options Panel

#### Auto Normalize

![Auto Normalize](/docs2/images/editors/3d-viewport/sidebar/tool-tab-mesh-weight-paint-mode/auto-normalize.png)

Ensure that all bone deforming vertex groups adds up to 1.0 while weight painting.

| Entry | What it does |
| --------------- | -------------------------------------------------------------------------------------------------------------------- |
| Lock - Relative | Display bone-deforming groups as if all locked defom groups were deleted, and the remaining ones were re-normalized. |
| Multi Paint | Paint across the weights of all selected bones, maintaining their relative influence. |
| Restrict | Restrict painting to vertices in the group. |

# Context Menus

## Brushes context menus

### Brushes context menus

![Brushes context menus](/docs2/images/editors/3d-viewport/context-menus/mesh-object-weight-paint-mode-brushes-context-menus/brushes-context-menus.png)

Call this menu with right click in the 3D viewport. You need to be in Weight Paint mode with a mesh object.

In Weight Paint mode you will call a context menu with the sliders from the Brush settings.

| Entry | What it does |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Weight | Adjust the strength of the weight painting. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. |
| Radius | The Radius edit box allows you to adjust the radius of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
| Strength | The Strength edit box allows you to adjust the strength of the brush. · **Size Pressure**: The first button behind the edit box enables tablet pressure sensitivity for radius. · **Use Unified Radius**: The second button behind the edit box enables global radius size. Any modification at the radius will also modify the radius value for other paint tools. |
