---
id: editors.shader-editor.sidebar.relations-tab
title: Relations tab
section: editors
path:
  - Editors
  - Shader Editor
  - Sidebar
  - Relations tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 13.3.6 Editors - Shader Editor - Sidebar - Relations tab.odt
---
## Relations tab - Display Panel

### Icon Buttons

![Icon Buttons](/docs2/images/editors/shader-editor/sidebar/relations-tab/icon-buttons.png)

You can display the nodes in the panels either as text buttons or as pure icon buttons.

## Relations tab - Group Panel

![Relations tab - Group Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-group-panel.png)

Node groups allows you to group different nodes of the material together to reduce the visual complexity. A node group acts like any other node.

Material node groups should not include Input nodes, like Image nodes, or Output nodes.

If you include a source node in your group, you will end up having the source node appearing twice: once inside the group, and once outside the group in the new material node tree.

If you include an output node in the group, there will not be an output socket available from the group!

### Make Group

Groups the selected nodes together.

Select the nodes that you want to group together. Choose Make Group. You will now see a green background. This indicates that the group is created, and that you are in edit mode for the group now.

![Make Group](/docs2/images/editors/shader-editor/make-group.png)

![Make Group](/docs2/images/editors/shader-editor/make-group-2.png)

To exit the group edit mode press Tab key, or choose Toggle Edit Group menu item . That way you can also enter the Group Edit mode again.

![Make Group](/docs2/images/editors/shader-editor/make-group-3.png)

![Make Group](/docs2/images/editors/shader-editor/make-group-5.png)

There is a third way to enter the group edit mode. Click at the right upper icon of the group node.

![Make Group](/docs2/images/editors/shader-editor/make-group-6.png)

A group can be further collapsed by clicking at the triangle button in the upper left corner.

![Make Group](/docs2/images/editors/shader-editor/make-group-7.png)

The group can be renamed in the sidebar in the Item tab and in the Properties tab in the Node panel.

### Group Insert

Inserts the selected node into the selected group.

#### Usage

Select the node.

Hold down shift, and select the group.

Click the Group Insert button. The node will now be part of the group, and you will land in group edit mode. Press tab to exit the group edit mode.

### Group Input

![Group Input](/docs2/images/editors/shader-editor/sidebar/relations-tab/group-input.png)

Adds a group input node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.

### Group Output

![Group Output](/docs2/images/editors/shader-editor/sidebar/relations-tab/group-output.png)

Adds a group output node.

> **Note:** When at a top level, this node is unavailable. These are only available when inside a node group.


| Entry | What it does |
| ----------------- | -------------------------------------------------------------------------- |
| Toggle Edit Group | Enter or exit the edit group mode. |
| Ungroup | Ungroups an existing group. You need to be outside of the group edit mode. |


## Relations tab - Node Group Panel

![Relations tab - Node Group Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-node-group-panel.png)

When you create a node group, then this node group is listed here. And can be dragged from there for reuse too.

## Relations tab - Layout Panel

![Relations tab - Layout Panel](/docs2/images/editors/shader-editor/sidebar/relations-tab/relations-tab-layout-panel.png)

These nodes helps organizing the node layout.

### Frame

![Frame](/docs2/images/editors/shader-editor/header/add-menu-layout/frame.png)

The Frame node allows you to drop nodes into a frame. This frame can be dragged around as a whole.

#### Adding and Removing Nodes

![Adding and Removing Nodes](/docs2/images/editors/shader-editor/header/add-menu-layout/adding-and-removing-nodes.jpg)

Nodes can be added by simply dropping them onto the frame. Or with the Join in New Frame menu item in the Node menu.

To remove a node from the frame use Remove from Frame.

#### Resizing Frame

When the Frame node is first placed in the node editor workspace you can resize it by dragging one of the edges.

Once a node is placed in the Frame, the Frame shrinks around the nodes. You cannot resize it anymore with handlers. Just by dragging around the nodes inside of the frame.

![Resizing Frame](/docs2/images/editors/shader-editor/header/add-menu-layout/resizing-frame.png)

This behavior can be changed by disabling the *Shrink* option in the Item tab in the Properties panel. Then you can resize the frame again by dragging the edges.

#### Label and Color

You can change the name of a frame in the Node panel. And you can give it a custom color by checking the Color checkbox and adjusting the color then.

### Reroute

Adds a reroute point that can be used to reroute connections. It allows just one input, but allows multiple output connections.

To quickly add a Reroute node into an existing connection, hold **Shift** and **Right Mouse* *and drag the mouse to cut through the link.** A new reroute node will be added.

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute.png)

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute-2.png)

![Reroute](/docs2/images/editors/shader-editor/header/add-menu-layout/reroute-3.png)

When you exceed a specific angle amount between the reroute nodes, then the node connection becomes a sharp corner, and not longer a Bezier like soft curve.

#### Move, Rotate, Scale

![Move, Rotate, Scale](/docs2/images/editors/shader-editor/header/add-menu-layout/move-rotate-scale.png)

A normal node has a handler. The reroute dot not. You can't simply move it around with the mouse by clicking at the top area. It has none. You have to use the move, rotate and scale commands. They can be found in the View menu.

