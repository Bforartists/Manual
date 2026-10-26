---
id: editors.3d-viewport.metaball.edit
title: "Edit Mode"
section: editors
path:
  - "Editors"
  - "3D Viewport"
  - "Metaball"
  - "Edit Mode"
version: "5.1"
status: draft
icon: editmode_hlt
summary: "Edit the metaball itself: every header menu, tool, sidebar tab and context menu of Edit Mode."
order: 10
source:
  - "7.1.25 Editors - 3D Viewport - Header - Metaball - Edit mode - Metaball menu.odt"
  - "7.2.10 Editors - 3D Viewport - Tool Shelf - Metaball - Edit Mode.odt"
  - "7.0.10 Editors - 3D Viewport - Metaball - Edit Mode - Metaball context menu.odt"
replaces:
  - editors.3d-viewport.header.metaball-edit-mode-metaball-menu
  - editors.3d-viewport.tool-shelf.metaball-edit-mode
  - editors.3d-viewport.context-menus.metaball-edit-mode-metaball-context-menu
---
Metaball › Edit Mode: every menu, tool, sidebar tab and context menu of this mode, on one page. Use the panels on the right to jump between the regions.

# Header

## Metaball menu

### Edit Mode - Metaball Menu

![Edit Mode - Metaball Menu](/docs2/images/editors/3d-viewport/header/metaball-edit-mode-metaball-menu/edit-mode-metaball-menu.png)

The Metaball menu just exists for Metaball objects.

### Transform submenu

![Transform submenu](/docs2/images/editors/3d-viewport/header/metaball-edit-mode-metaball-menu/transform-submenu.png)

#### To Sphere

Shapes a selection of Meta elements into the shape of a sphere. The calculation happens with the object origins.

##### Usage

![Usage](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/usage.png)

Select the elements, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape. This also works with meta elements in the same way.

![Usage](/docs2/images/editors/3d-viewport/header/metaball-edit-mode-metaball-menu/usage.png)

##### Last Operator To Sphere

![Last Operator To Sphere](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-to-sphere.png)


| Entry | What it does |
| -------------- | -------------------------------------------------------- |
| Factor | The factor to transform the selection into a shape form. |
| Mirror Editing | Enable mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff. |


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

Bends the selection. You need more than one meta element.

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


#### Warp

![Warp](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/warp.png)

Warps a selection between two defined points. This also works with Metaballs. You need more than one metaball element.

##### Last operator Warp


| Entry | What it does |
| ------------ | ----------------------------------- |
| Warp Angle | The strength of the warp effect. |
| Offset Angle | An offset angle to bend side-wards. |


###### Min

![Min](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/min.png)

The start point.

###### Max

The end point.

#### Randomize

This tool allows randomizes the positions of the selected meta elements.

##### Last Operator Randomize Transform

![Last Operator Randomize Transform](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/last-operator-randomize.png)


| Entry | What it does |
| ----------- | ------------------------------------------ |
| Amount | Adjust the amount. |
| Uniform | The uniform offset distance. |
| Normal | Align the offset direction to the normals. |
| Random Seed | The seed value for randomization. |


#### Move Texture Space

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space.png)

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-2.png)

This tool relies at the move tool. With the difference that it moves the texture space instead of the object. It has also a very special use case, and just works with a material with a Texture Coordinate / Generated node. And requires to have the shading at Material or Rendered to see a result in the viewport.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-3.png)

In the viewport you will see the UV cage in black color. In the header you will see the values for the current position of the UV cage.

Note that once done and applied, there is no way to reset the UV cage back to zero. When you repeat the operation, then the values will start at 0 again. Even when the UV cage is already offset.

![Move Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-4.png)

##### Last Operator Move

![Last Operator Move](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-move.png)

###### Move

Adjust in which directions you want to transform.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/object-menu/orientation.png)

Choose the orientation.

###### Mirror Editing

Enable mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Scale Texture Space

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/scale-texture-space.png)

Scale Texture space is similar to the Move texture Space. With the only difference that it scales the UV space instead of moving it.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-2.png)

This tool relies at the scale tool. With the difference that it scales the texture space instead of the object. It has also a very special use case, and just works with a material with a Texture Coordinate / Generated node. And requires to have the shading at Material or Rendered to see a result in the viewport.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/move-texture-space-3.png)

In the viewport you will see the UV cage in black color. In the header you will see the values for the current position of the UV cage.

Note that once done and applied, there is no way to reset the UV cage back to zero. When you repeat the operation, then the values will start at 0 again. Even when the UV cage is already offset.

![Scale Texture Space](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/scale-texture-space-2.png)

##### Last Operator Resize

![Last Operator Resize](/docs2/images/editors/3d-viewport/header/object-menu/last-operator-resize.png)

###### Scale

Adjust in which directions you want to transform.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/header/object-menu/orientation.png)

Choose the orientation.

###### Mirror Editing

Enable mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/header/object-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Set Dimensions

![Set Dimensions](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/set-dimensions.png)

Edit Mode Only!

Normally all scale operations in Bforartists are relative to the current selection and dimensions. And you always start with a relative value of 1.

Set dimensions allows to scale object selections in absolute world values. No matter how the initial values are. The new values gets set in the Last Operator.

Set dimensions is an add-on. You can turn it off in the add-ons section of the user preferences when you want.

##### Last Operator Set Dimensions

###### New Dimensions

![New Dimensions](/docs2/images/editors/3d-viewport/header/mesh-edit-mode-mesh-menu/new-dimensions.png)

When you activate the tool then you will see the world coordinates of the selection. Change the values to other world coordinates.

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

![Snap submenu](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

#### Snap

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last operator Snap Selection to Cursor

![Last operator Snap Selection to Cursor](/docs2/images/editors/3d-viewport/context-menus/curve-surface-object-edit-mode-curve-context-menus/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | If the selection should be rotated to match the cursor. |


### Operators

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

#### Delete

Deletes the current selection.

# Tool Shelf

## Tools

### Tool Shelf - Metaball - Edit Mode

![Tool Shelf - Metaball - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/metaball-edit-mode/tool-shelf-metaball-edit-mode.png)

#### Tweak, Select, 3D Cursor, Transform, Measure and Annotate tools

The Tweak, Select , 3D Cursor, Transform, Measure and Annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

#### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/metaball-edit-mode/shear.png)

The shear tool allows you to shear the selected geometry. When you activate the tool, then a widget appears that allows you to pull in the desired direction.

The shear happens between the meta elements. This means you need more than one. And you need to select the meta elements first!

##### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/metaball-edit-mode/tool-settings.png)

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/orientation.png)

Choose the orientation for the shear action.

###### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-mirror-2.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

# Context Menus

## Metaball context menu

### Metaball Context Menu

![Metaball Context Menu](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/metaball-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with a Metaball object.

#### Duplicate

Duplicates the current selection.

The copy sticks to the mouse until you release it. A Right click while moving will reset the position of the duplicate. The duplicated part will be part of the same object.

When you drag the duplicate around you will see the position values in the header.

##### Last Operator Duplicate

![Last Operator Duplicate](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-duplicate.png)

###### Move X , Y , Z

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Choose the orientation.

###### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Mirror

![Mirror](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/mirror.png)

Mirror mirrors the selected geometry along the defined axis.

#### Interactive Mirror

Mirror by hotkeys. You activate the tool, type in x for x global for example, or x x for x local. And the selection gets mirrored.

#### X Global, Y Global etc.

Mirrors the selection around the chosen axis.

##### Last Operator Mirror

![Last Operator Mirror](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-mirror.png)

The Last Operator Mirror panel gives you tools to adjust the mirror action.

###### Orientation

![Orientation](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/orientation.png)

Orientation is a drop-down box choose the type of orientation for the mirroring action.

###### Constraint Axis

Constraint Axis gives you again the possibility to define the mirror axis. You can choose more than one axis here.

#### Snap

![Snap](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-vertex-context-menu/snap-vertices.png)

Choose several methods to snap one element to another. The menu items should be self explaining.

##### Last Operator Snap

![Last Operator Snap](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/last-operator-snap.png)

Some snap operations shows a last operation panel, some not.


| Entry | What it does |
| -------- | ---------------------------------------------------------------------------------------------------- |
| Offset | If the selection should snap as a whole, or if each individual element of the selection should snap. |
| Rotation | Rotate to match the cursor. |


#### Show/Hide

![Show/Hide](/docs2/images/editors/3d-viewport/context-menus/metaball-edit-mode-metaball-context-menu/show-hide.png)

Sub-menu with shows or hide selection, unselected or hidden operators.

##### Show Hidden

Makes all geometry in the scene visible again.

##### Hide Selected

Hides the selected geometry.

###### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/mesh-object-edit-mode-edge-context-menu/last-operator-hide-selected.png)

###### Unselected

Hides the not selected geometry.

##### Hide Unselected

Hides the not selected geometry. The selected geometry stays visible.

#### Delete

Deletes the current selection.
