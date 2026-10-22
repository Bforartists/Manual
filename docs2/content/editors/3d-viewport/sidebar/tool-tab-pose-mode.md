---
id: editors.3d-viewport.sidebar.tool-tab-pose-mode
title: Tool Tab - Pose Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Sidebar
  - Tool Tab - Pose Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.3.5 Editors - 3D Viewport - Sidebar - Tool Tab - Pose Mode.odt
---
## Tools Tab in Pose Mode

There are two object types that has a pose mode. The armature, and the grease pencil object. We will cover the armature here. The grease pencil object has its own chapter as a whole.

The number of available tools in the tools panel is rather small. There is just one panel.

## Pose Mode - Armature

### Pose Options Panel

![Pose Options Panel](/docs2/images/editors/3d-viewport/sidebar/tool-tab-pose-mode/pose-options-panel.png)

#### Auto IK

Add temporary IK constraints while grabbing bones in Pose mode.

#### X Axis Mirror

X Axis Mirror in pose mode synchronizes the right side of a symmetrical armature with the left side of a symmetrical armature.

![X Axis Mirror](/docs2/images/editors/3d-viewport/sidebar/tool-tab-pose-mode/x-axis-mirror.png)

The same checkbox can also be found in the tool settings bar as an icon button. This allows quicker access and better visual control which mirror axis is currently active.

##### Relative Mirror

This is a setting for X Axis Mirror, and just shows when X Axis Mirror is ticked. Here you can define if the mirroring happens relative to the armature or to the world.

### Affect Only Locations

This is for having more than one armature part selected. Scales or rotates the selection instead of scaling or rotating the single armature parts. The single bones keeps their scale and their rotation.

