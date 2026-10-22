---
id: editors.3d-viewport.tool-shelf.lattice-edit-mode
title: Lattice - Edit Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Tool Shelf
  - Lattice - Edit Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.2.19 Editors - 3D Viewport - Tool Shelf - Lattice - Edit Mode.odt
---
## Tool Shelf - Lattice - Edit Mode

![Tool Shelf - Lattice - Edit Mode](/docs2/images/editors/3d-viewport/tool-shelf/lattice-edit-mode/tool-shelf-lattice-edit-mode.png)

### Select, 3D Cursor, Transform, Measure and Annotate tools

The Select, 3D Cursor, Transform, Measure and Annotate tools at the end of the list are explained in the chapter 7.1.1 Editors - 3D View - Tool Shelf - Object Mode. We won't cover this tools again here.

### Shear

![Shear](/docs2/images/editors/3d-viewport/tool-shelf/lattice-edit-mode/shear.png)

Shear shears the selection. When you activate the tool then you will reveal a widget. This widget allows you to shear the selection in all possible axis.

#### Tool Settings

![Tool Settings](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/tool-settings-17.png)

##### Orientation

![Orientation](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Choose the orientation for the shear action.

##### Drag

![Drag](/docs2/images/editors/3d-viewport/tool-shelf/mesh-edit-mode/drag.png)

When you click at the widget of the active tool, then you perform the tool action. Adjust what should happen when you click outside of the widget, in the empty area.


| Entry | What it does |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Tool | When you click off the widget then the click still does the same than clicking at the widget. It performs the active tool. |
| Tweak, Select Box, Circle and Lasso | When you choose this options then you will set the off click to the different select methods. Whereas tweak works more than a move tool then. Tweak is the default. |


##### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/last-operator-shear.png)


| Entry | What it does |
| ------ | --------------------------------------------------- |
| Offset | Adjust an offset. |
| Axis | Defines one axis of the imaginary shear axis plane. |


###### Axis Ortho

![Axis Ortho](/docs2/images/editors/3d-viewport/tool-shelf/armature-edit-mode/orientation.png)

Defines the other axis of the imaginary shear axis plane.


| Entry | What it does |
| -------------- | -------------------------------------------- |
| Orientation | Choose the orientation for the shear action. |
| Mirror Editing | Enable Mirror Editing |


##### Proportional editing

![Proportional editing](/docs2/images/editors/3d-viewport/tool-shelf/curve-edit-mode/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


