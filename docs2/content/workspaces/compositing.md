---
id: workspaces.compositing
title: "Compositing"
section: workspaces
path:
  - "Workspaces"
  - "Compositing"
version: "5.1"
status: draft
icon: node_compositing
summary: "Post-process your renders with compositing nodes."
cta: "Open"
source:
  - "4 Workspaces.odt"
order: 110
---
The workspace to do compositing and post processing.

![Compositing workspace](/docs2/images/workspaces/workspaces/standard-workspaces-10.png)

## How the work flows

Compositing is the finishing room after the render. In the [Compositor](../editors/compositor/index.md) you combine render passes and add effects like glow, blur or colour grading with nodes, and the [Image Editor](../editors/image-editor/index.md) shows the result through the Viewer node. The [3D Viewport](../editors/3d-viewport/index.md) keeps the camera view of the scene at hand, the [Properties Editor](../editors/properties/index.md) turns on the passes you need, and the [Timeline](../editors/timeline/index.md) picks the frame to work on.
