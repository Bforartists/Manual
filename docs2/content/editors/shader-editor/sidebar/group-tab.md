---
id: editors.shader-editor.sidebar.group-tab
title: Group tab
section: editors
path:
  - Editors
  - Shader Editor
  - Sidebar
  - Group tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 13.3.7 Editors - Shader Editor - Sidebar - Group tab.odt
---
## Group tab - Introduction

![Group tab - Introduction](/docs2/images/editors/shader-editor/sidebar/group-tab/group-tab-introduction.png)

The Geometry Node sidebar Group tab at the right side contains options and settings for node groups nodes and socket input and output properties.

## Group Properties Panel

### Name

![Name](/docs2/images/editors/shader-editor/sidebar/group-tab/name.png)

Change the name of the current node group. Type in a new name and hit enter.

### Description

Change the description of the current node group. Type in a new name and hit enter.

### Color Tag

![Color Tag](/docs2/images/editors/shader-editor/sidebar/group-tab/color-tag.png)

Changes the header color of the current node group.

### Node Width

The default width of the node.

## Group Sockets Panel

![Group Sockets Panel](/docs2/images/editors/shader-editor/sidebar/group-tab/group-sockets-panel.png)

Manage the input and output properties of the Group Input and Output nodes.

More than one input and output slot can be useful when you want to modify the geometry in the node group in more than one way.

### Group Socket List

List of available input and output sockets.

> **Note:** The list can be sorted by dragging the items around.

#### List

The list of input and output sockets.

#### Name

![Name](/docs2/images/editors/shader-editor/sidebar/group-tab/name-2.png)

Change the name of the current selected input socket by double clicking on the socket in the list. Type in a new name and hit enter.

#### New Item

![New Item](/docs2/images/editors/shader-editor/sidebar/group-tab/new-item.png)

Adds a new input sockets to the list.


| Entry | What it does |
| ------ | ------------------------------------- |
| Input | Adds a new input sockets to the list. |
| Output | Adds a new output socket to the list. |
| Panel | Adds a new panel socket to the list. |


| Entry | What it does |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| ![](/docs2/images/editors/shader-editor/sidebar/group-tab/duplicate-item-icon.png) Duplicate Item | Duplicates the active socket. |
| ![](/docs2/images/editors/shader-editor/sidebar/group-tab/remove-item-icon.png) Remove Item | Removes the selected input socket from the list. |


#### Move Item Up/Down

![Move Item Up/Down](/docs2/images/editors/shader-editor/sidebar/group-tab/move-item-up-down.png)

Moves the active item to the specified direction. You can move the active item up or down the list.

> **Note:** You can also alternatively drag and drop the active item to re-order.

### Type

![Type](/docs2/images/editors/shader-editor/sidebar/group-tab/type.png)

What kind of node group input or output type it is. To know more about the properties of the socket types, refer to the next section.

#### Type Float

![Type Float](/docs2/images/editors/shader-editor/sidebar/group-tab/type-float.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype.png)

Subtype of the default value.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Integer

![Type Integer](/docs2/images/editors/shader-editor/sidebar/group-tab/type-integer.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype-2.png)

Subtype of the default value.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Boolean

![Type Boolean](/docs2/images/editors/shader-editor/sidebar/group-tab/type-boolean.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default value for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Vector

![Type Vector](/docs2/images/editors/shader-editor/sidebar/group-tab/type-vector.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/shader-editor/sidebar/group-tab/subtype-3.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Dimensions | How much dimensions to calculate. |
| Default | The default vector. It changes, dependant of what dimensions you use. |
| Min / Max | Minimum value and maximum value. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Color

![Type Color](/docs2/images/editors/shader-editor/sidebar/group-tab/type-color.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default color for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Menu

![Type Menu](/docs2/images/editors/shader-editor/sidebar/group-tab/type-menu.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default menu. |
| Expanded | Draw the menu socket as an expanded drop down menu. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Shader

![Type Shader](/docs2/images/editors/shader-editor/sidebar/group-tab/type-shader.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Bundle

![Type Bundle](/docs2/images/editors/shader-editor/sidebar/group-tab/type-bundle.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Closure

![Type Closure](/docs2/images/editors/shader-editor/sidebar/group-tab/type-closure.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


## Animation Panel

![Animation Panel](/docs2/images/editors/shader-editor/sidebar/group-tab/animation-panel.png)

Allows you to add FCurvces for animation.

TODO

