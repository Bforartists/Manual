---
id: editors.geometry-node-editor.sidebar.group-tab
title: Group tab
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Sidebar
  - Group tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.3.1 Editors - Geometry Nodes Editor - Sidebar - Group tab.odt
---
## Group tab - Introduction

![Group tab - Introduction](/docs2/images/editors/geometry-node-editor/sidebar/introduction.png)

The Shader sidebar Group tab at the right side contains options and settings for node groups and socket input and output properties.

It is especially meant for the group nodes. Grpup Input and Group Output.

In the group sockets panel you can define what sockets the Group Input and Group Output node has.

![Group tab - Introduction](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/group-tab-introduction.png)

![Group tab - Introduction](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/group-tab-introduction-2.png)

![Group tab - Introduction](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/group-tab-introduction-3.png)

## Group Properties Panel

### Name

![Name](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/name.png)

Change the name of the current node group. Type in a new name and hit enter.

### Description

Change the description of the current node group. Type in a new name and hit

enter.

### Color Tag

![Color Tag](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/color-tag.png)

Changes the header color of the current node group.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Node Width | The width for newly created node groups. Value can range between 40 and 700 px. · **Set default group node width**: Sets the width based of the parent node group in the current context. |
| Show Manage Panel | Display the manage panel when creating a modifier. |
| Usage subpanel | **Modifier**: The node group is used as a geometry modifier. This setting is only relevant for marked nodegroups as an asset. · **Tool**: The node group is used as a tool. This setting is only relevant for marked nodegroups as an asset. |


## Group Sockets Panel

![Group Sockets Panel](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/group-sockets-panel.png)

Manage the input and output properties of the Group Input and Output nodes.

More than one input and output slot can be useful when you want to modify the shader in the node group in more than one way.

### Group Socket List

List of available input and output sockets.

> **Note:** The list can be sorted by dragging the items around. And you can rename them.

#### List

The list of input and output sockets.

#### Name

![Name](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/name-2.png)

Change the name of the current selected input socket by double clicking on the socket in the list. Type in a new name and hit enter.

#### New Item

![New Item](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/new-item.png)

Adds a new input sockets to the list.


| Entry | What it does |
| ------ | ------------------------------------- |
| Input | Adds a new input sockets to the list. |
| Output | Adds a new output socket to the list. |
| Panel | Adds a new panel socket to the list. |


##### Panel Toggle

![Panel Toggle](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/panel-toggle.png)

Converts an active selected Boolean socket into a Panel Boolean.

When converting a boolean to a panel boolean, the parent panel of the Boolean socket will move to the panel header.

###### Panel Toggle subpanel

![Panel Toggle subpanel](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/panel-toggle-subpanel.png)

When adding a panel toggle to a panel then a subpanel appears.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------------- |
| Default | Input value used for unconnected sockets. |
| Hide in Modifier | Don’t show the input value in the geometry nodes modifier interface. |


**Shape**

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape.png)

What kind of higher order types are expected to flow through this socket.


| Entry | What it does |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/duplicate-item-icon.png) Duplicate Item | Duplicates the active socket. |
| ![](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/remove-item-icon.png) Remove Item | Removes the selected input socket from the list. Node tree interface specials |


#### Move Item Up/Down

![Move Item Up/Down](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/move-item-up-down.png)

Moves the active item to the specified direction. You can move the active item up or down the list.

> **Note:** You can also alternatively drag and drop the active item to re-order.

### Inputs

![Inputs](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/inputs.png)

Inputs are characterized by the colored dot to the left. These are manifested in the Group Input node.

### Outputs

![Outputs](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/outputs.png)

Outputs are characterized by the colored dot to the right. These are manifested in the Group Output node.

## Group Sockets Panel

The group input sockets differs in functionality from the group outputs sockets. So you will get other content when you selct a group input node compared to the group output node.

### Type

![Type](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type.png)

What kind of node group input or output type it is.

![Type](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-2.png)

![Type](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-3.png)

#### Type Float

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.

##### Default Attribute

The default attribute.

##### Subtype

![Subtype](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/subtype.png)

Subtype of the default value.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Integer

![Type Integer](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-integer.png)

![Type Integer](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-integer-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.

##### Default Attribute

The default attribute.

##### Subtype

![Subtype](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/subtype.png)

Subtype of the default value.


| Entry | What it does |
| ------- | ------------------------------------------------------------------------------------------------ |
| Default | The default value for the socket. |
| Min | The minimum value for the socket. **Note:** *This is only available for vector and float types.* |
| Max | The maximum value for the socket. ***Note:** This is only available for vector and float types.* |


##### Default Input

![Default Input](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/default-input.png)

Input to use when the socket is unconnected.


| Entry | What it does |
| ---------------- | -------------------------------------------------------------- |
| Optional label | Hide the label if not needed. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Boolean

![Type Boolean](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-boolean.png)

![Type Boolean](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-boolean-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------- |
| Default Attribute | The default attribute that is used by a geometry nodes modifier. |
| Default | The default value for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |
| Layer Selection | Take grease pencil or layer group as selection field. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Vector

![Type Vector](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-vector.png)

![Type Vector](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-vector-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.

##### Default Attribute

The default attribute that is used by a geometry nodes modifier.

##### Subtype

![Subtype](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/subtype-2.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------- | --------------------------------------------------------------------- |
| Dimensions | How much dimensions to calculate. |
| Default | The default vector. It changes, dependant of what dimensions you use. |
| Min / Max | Minimum value and maximum value. |


##### Default Input

![Default Input](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/default-input-2.png)

Input to use when the socket is unconnected.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Color

![Type Color](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-color.png)

![Type Color](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-color-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------- |
| Default Attribute | The default attribute that is used by a geometry nodes modifier. |
| Default | The default color for the socket. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Rotation

![Type Rotation](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-rotation.png)

![Type Rotation](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-rotation-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.


| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------- |
| Default Attribute | The default attribute that is used by a geometry nodes modifier. |
| Default | The default rotation values |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Matrix

![Type Matrix](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-matrix.png)

![Type Matrix](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-matrix-2.png)

##### Description

Add a tooltip to the socket description.

##### Atrribute Domain

![Atrribute Domain](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/atrribute-domain-2.png)

The attribute domain used by the geometry nodes modifier to create an attribute output.

##### Default Attribute

The default attribute that is used by a geometry nodes modifier.

##### Default Input

![Default Input](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/default-input-3.png)

Input to use when the socket is unconnected.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type String

![Type String](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-string.png)

![Type String](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-string-2.png)

##### Description

Add a tooltip to the socket description.

##### Subtype

![Subtype](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/subtype-3.png)

What special math operation is required. The subtype menu allows you to define the socket type sliders and read-out.


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Default | The default string. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Menu

![Type Menu](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-menu.png)

![Type Menu](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-menu-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default menu. |
| Expanded | Draw the menu socket as an expanded drop down menu. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


##### Shape

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-2.png)

![Shape](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/shape-3.png)

The shape of the socket.

#### Type Geometry

![Type Geometry](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-geometry.png)

![Type Geometry](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-geometry-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Object

![Type Object](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-object.png)

![Type Object](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-object-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default object. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Collection

![Type Collection](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-collection.png)

![Type Collection](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-collection-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default collection. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Image

![Type Image](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-image.png)

![Type Image](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-image-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default image. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Material

![Type Material](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-material.png)

![Type Material](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-material-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default image. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Font

![Type Font](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-font.png)

![Type Font](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-font-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Default | The default font. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Bundle

![Type Bundle](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-bundle.png)

![Type Bundle](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-bundle-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


#### Type Closure

![Type Closure](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-closure.png)

![Type Closure](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/type-closure-2.png)


| Entry | What it does |
| ---------------- | ---------------------------------------------------------------------------------- |
| Description | Add a tooltip to the socket description. |
| Optional Label | Make the label optional. This may resul tin the label being skipped in some cases. |
| Hide Value | Hide the input value even when the socket is not connected. |
| Hide in Modifier | Don’t show the value in the geometry nodes modifier interface. |


## Group Sockets Panel - Type Panel

![Group Sockets Panel - Type Panel](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/group-sockets-panel-type-panel.png)

TODO

### Closed by default

Panel is closed by default on new nodes.

### Panel Toggle

![Panel Toggle](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/panel-toggle-2.png)

> **Note:** The Panel Toggle properties are only for the Panel Boolean type of panels.


| Entry | What it does |
| ---------------- | ------------------------------------------------------- |
| Default | The default value for the boolean toggles. |
| Hide in Modifier | Hides the panel boolean toggle from the modifier stack. |
| Single Value | The default value for the panel boolean toggle. |


## Animation Panel

![Animation Panel](/docs2/images/editors/geometry-node-editor/sidebar/group-tab/animation-panel.png)

Animation panels are about the Animation Slots for scene wide animation clips.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New | Create a new action clip for the light, used in the Dopesheet Editor - Action Clip mode. |
| Action Selector | This selector allows users to manage actions associated with a particle system, ensuring that the correct animation data is applied. · **Fake User**: Assigns a "fake user" to the action, preventing it from being automatically deleted when it is no longer in use. · **Add**: Make a copy of the current action, including all animation data. · **Remove**: Delete the selected action, removing it from the light source. |


