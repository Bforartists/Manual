---
id: editors.compositor.sidebar.group-tab
title: Group tab
section: editors
path:
  - Editors
  - Compositor
  - Sidebar
  - Group tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 10.3.7 Editors - Compositor Editor - Sidebar - Group tab.odt
---
## Group tab - Introduction

![Group tab - Introduction](/docs2/images/editors/compositor/sidebar/group-tab/group-tab-introduction.png)

The Compositor sidebar Group tab at the right side contains options and settings for node groups and socket input and output properties.

## Group Properties Panel

### Name

![Name](/docs2/images/editors/compositor/sidebar/group-tab/name.png)

Change the name of the current node group. Type in a new name and hit enter.

### Description

Change the description of the current node group. Type in a new name and hit enter.

### Color Tag

![Color Tag](/docs2/images/editors/compositor/sidebar/group-tab/color-tag.png)

Changes the header color of the current node group.

### Node Width

The width for newly created group nodes.

## Group Sockets Panel

![Group Sockets Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel.png)

![Group Sockets Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel-2.png)

Manage the input and output properties of the Group Input and Output nodes.

More than one input and output slot can be useful when you want to modify compositor sockets in the node group in more than one way.

### Group Socket List

List of available input and output sockets.

> **Note:** The list can be sorted by dragging the items around.

#### List

The list of input and output sockets.


| Entry | What it does |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Socket Name | Change the name of the current selected input socket by double clicking on the socket in the list. Type in a new name and hit enter. |
| Searchbar | Clicking at the white arrow button down left of the list will reveal a search input box. |
| Resize Handle | The list can be resized by pulling at the resize handle in the center of the list at the bottom. |


#### New Item

![New Item](/docs2/images/editors/compositor/sidebar/group-tab/new-item.png)

Adds a new input sockets to the list.


| Entry | What it does |
| ------ | ------------------------------------- |
| Input | Adds a new input sockets to the list. |
| Output | Adds a new output socket to the list. |
| Panel | Adds a new panel socket to the list. |


##### Panel Toggle

When you create a panel, then the panel toggle button becomes active. By default the checkbox is ticked. And all available panel toggles are on. When you untick it then you reveal a Panel Toggle subpanel, where you have more fine control over the toggles.

###### Panel toggle subpanel

![Panel toggle subpanel](/docs2/images/editors/compositor/sidebar/group-tab/panel-toggle-subpanel.png)


| Entry | What it does |
| ---------------- | ----------------------------------------------------------------- |
| Default | Input value for unconnected socket. |
| Hide in Modifier | Don’t show the modifier in the geometry nodes modifier interface. |
| Single Value | Only allow single value input rather than field. |


| Entry | What it does |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------ |
| ![](/docs2/images/editors/compositor/sidebar/group-tab/duplicate-item-icon.png) Duplicate Item | Duplicates the active socket. |
| ![](/docs2/images/editors/compositor/sidebar/group-tab/remove-item-icon.png) Remove Item | Removes the selected input socket from the list. |


#### Move Item Up/Down

![Move Item Up/Down](/docs2/images/editors/compositor/sidebar/group-tab/move-item-up-down.png)

Moves the active item to the specified direction. You can move the active item up or down the list.

> **Note:** You can also alternatively drag and drop the active item to re-order.

### Inputs

![Inputs](/docs2/images/editors/compositor/sidebar/group-tab/inputs.png)

Inputs are characterized by the colored dot to the left. These are manifested in the Group Input node.

### Outputs

![Outputs](/docs2/images/editors/compositor/sidebar/group-tab/outputs.png)

Outputs are characterized by the colored dot to the right. These are manifested in the Group Output node.

### Type

![Type](/docs2/images/editors/compositor/sidebar/group-tab/type.png)

What kind of node group input or output type it is.

#### Type Float

![Type Float](/docs2/images/editors/compositor/sidebar/group-tab/type-float.png)

![Type Float](/docs2/images/editors/compositor/sidebar/group-tab/type-float-2.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type Integer

![Type Integer](/docs2/images/editors/compositor/sidebar/group-tab/type-integer.png)

![Type Integer](/docs2/images/editors/compositor/sidebar/group-tab/type-integer-2.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type Boolean

![Type Boolean](/docs2/images/editors/compositor/sidebar/group-tab/type-boolean.png)

![Type Boolean](/docs2/images/editors/compositor/sidebar/group-tab/type-boolean-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default value for the socket. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type Vector

![Type Vector](/docs2/images/editors/compositor/sidebar/group-tab/type-vector.png)

![Type Vector](/docs2/images/editors/compositor/sidebar/group-tab/type-vector-2.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | --------------------------------------------------------------------- |
| Dimensions | How much dimensions to calculate. |
| Default | The default vector. It changes, dependant of what dimensions you use. |
| Min / Max | Minimum value and maximum value. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type Color

![Type Color](/docs2/images/editors/compositor/sidebar/group-tab/type-color.png)

![Type Color](/docs2/images/editors/compositor/sidebar/group-tab/type-color-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default color for the socket. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type String

![Type String](/docs2/images/editors/compositor/sidebar/group-tab/type-string.png)

![Type String](/docs2/images/editors/compositor/sidebar/group-tab/type-string-2.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/compositor/sidebar/group-tab/subtype-2.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Default | The default string. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


#### Type Menu

![Type Menu](/docs2/images/editors/compositor/sidebar/group-tab/type-menu.png)

![Type Menu](/docs2/images/editors/compositor/sidebar/group-tab/type-menu-2.png)


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default menu. |
| Expanded | Draw the menu socket as an expanded drop down menu. |
| Optional Label | This label is not necessary to understand its meaning. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


## Group Sockets Panel - Type Panel

![Group Sockets Panel - Type Panel](/docs2/images/editors/compositor/sidebar/group-tab/group-sockets-panel-type-panel.png)

TODO

### Closed by default

Panel is closed by default on new nodes.

### Panel Toggle

![Panel Toggle](/docs2/images/editors/compositor/sidebar/group-tab/panel-toggle.png)

> **Note:** The Panel Toggle properties are only for the Panel Boolean type of panels.


| Entry | What it does |
| ---------------- | ------------------------------------------------------- |
| Default | The default value for the boolean toggles. |
| Hide in Modifier | Hides the panel boolean toggle from the modifier stack. |
| Single Value | The default value for the panel boolean toggle. |


## Animation Panel

![Animation Panel](/docs2/images/editors/compositor/sidebar/group-tab/animation-panel.png)

Animation panels are about the Animation Slots for scene wide animation clips.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New | Create a new action clip for the light, used in the Dopesheet Editor - Action Clip mode. |
| Action Selector | This selector allows users to manage actions associated with a particle system, ensuring that the correct animation data is applied. · **Fake User**: Assigns a "fake user" to the action, preventing it from being automatically deleted when it is no longer in use. · **Add**: Make a copy of the current action, including all animation data. · **Remove**: Delete the selected action, removing it from the light source. |


