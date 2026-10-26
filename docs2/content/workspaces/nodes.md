---
id: workspaces.nodes
title: "Nodes"
section: workspaces
path:
  - "Workspaces"
  - "Nodes"
version: "5.1"
status: draft
icon: geometry_nodes
summary: "Build geometry with geometry nodes and check the data."
cta: "Open"
source:
  - "4 Workspaces.odt"
order: 50
---
The workspace to work with the geometry nodes. Basic 3d view with the geometry nodes editor plus the spreadsheet editor to have access to the mesh data. A timeline at the bottom. And the usual outliner and properties editor.

![Nodes workspace](/docs2/images/workspaces/workspaces/standard-workspaces-4.png)

## How the work flows

Nodes is a lab for procedural geometry. You wire a recipe in the [Geometry Node Editor](../editors/geometry-node-editor/index.md) and watch the [3D Viewport](../editors/3d-viewport/index.md) rebuild the result live; when the shape surprises you, the [Spreadsheet](../editors/spreadsheet.md) shows the actual points, faces and attributes behind it. The [Properties Editor](../editors/properties/index.md) exposes the node group's inputs as friendly sliders on the modifier, and the [Timeline](../editors/timeline/index.md) scrubs frames to test setups that move.
