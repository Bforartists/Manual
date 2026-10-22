---
id: editors.geometry-node-editor.sidebar.relations-tab
title: Relations tab
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Sidebar
  - Relations tab
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.3.7 Editors - Geometry Nodes Editor - Sidebar - Relations tab.odt
---
## Relations tab - Display Panel

![Relations tab - Display Panel](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/relations-tab-display-panel.png)

### Icon Buttons

![Icon Buttons](/docs2/images/editors/geometry-node-editor/sidebar/add/add-tab-display-panel.png)

You can display the nodes in the panels either as text buttons or as pure icon buttons.

## Relations tab - Group Panel

![Relations tab - Group Panel](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/relations-tab-group-panel.png)

### Group Input

![Group Input](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/group-input.png)

Adds a group input node.

### Group Output

![Group Output](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/group-output.png)

Adds a group output node.

## Relations tab - Nodegroups Panel

![Relations tab - Nodegroups Panel](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/relations-tab-nodegroups-panel.png)

When you create a node group, then this node group is listed here. And can be dragged from there for reuse too.

## Relations tab - Layout Panel

![Relations tab - Layout Panel](/docs2/images/editors/geometry-node-editor/sidebar/relations-tab/relations-tab-layout-panel.png)

These nodes helps organizing the node layout.

### Frame

![Frame](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/frame.png)

The Frame node allows you to drop nodes into a frame. This frame can be dragged around as a whole.

#### Adding and Removing Nodes

![Adding and Removing Nodes](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/adding-and-removing-nodes.jpg)

Nodes can be added by simply dropping them onto the frame. Or with the Join in New Frame menu item in the Node menu.

To remove a node from the frame use Remove from Frame.

#### Resizing Frame

When the Frame node is first placed in the node editor workspace you can resize it by dragging one of the edges.

Once a node is placed in the Frame, the Frame shrinks around the nodes. You cannot resize it anymore with handlers. Just by dragging around the nodes inside of the frame.

![Resizing Frame](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/resizing-frame.png)

This behavior can be changed by disabling the *Shrink* option in the Item tab in the Properties panel. Then you can resize the frame again by dragging the edges.

#### Label and Color

You can change the name of a frame in the Node panel. And you can give it a custom color by checking the Color checkbox and adjusting the color then.

### Reroute

Adds a reroute point that can be used to reroute connections. It allows just one input, but allows multiple output connections.

To quickly add a Reroute node into an existing connection, hold **Shift** and **Right Mouse* *and drag the mouse to cut through the link.** A new reroute node will be added.

![Reroute](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/reroute.png)

![Reroute](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/reroute-2.png)

![Reroute](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/reroute-3.png)

When you exceed a specific angle amount between the reroute nodes, then the node connection becomes a sharp corner, and not longer a Bezier like soft curve.

#### Move, Rotate, Scale

![Move, Rotate, Scale](/docs2/images/editors/geometry-node-editor/header/add-menu-layout/move-rotate-scale.png)

A normal node has a handler. The reroute dot not. You can't simply move it around with the mouse by clicking at the top area. It has none. You have to use the move, rotate and scale commands. They can be found in the View menu.

