---
id: editors.3d-viewport.tool-shelf.armature-pose-mode
title: Armature - Pose Mode
section: editors
path:
  - Editors
  - 3D Viewport
  - Tool Shelf
  - Armature - Pose Mode
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.2.18 Editors - 3D Viewport - Tool Shelf - Armature - Pose Mode.odt
---
## Tool Shelf - Armature - Pose Mode

![Tool Shelf - Armature - Pose Mode](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/tool-shelf-armature-pose-mode.png)

The Pose mode provides some pose tools.

### Tweak, Select, 3D Cursor, Transform, Annotate and Measure

The tweak, select, 3d cursor and transform tools and the annotation and measure tool is already described in the chapter Object Mode. So we won't cover it here again.

### Breakdowner Push Relax tools group

![Breakdowner Push Relax tools group](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/breakdowner-push-relax-tools-group.png)

#### Breakdowner

Creates a suitable breakdowner pose on the current frame. Requires to have a keyframe before and after the current position.

### Header values

![Header values](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/header-values.png)

When you activate one of the tools, then you will see a percentage slider in the header. This slider is not interactive. It just displays the percentage of the exaggeration.

### Footer hotkey display

In the footer you will some hotkeys for further options. This hotkeys are hard coded, and cannot be changed in the input manager.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display.png)

The hotkeys W, E and R stands for the usual transform modes move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property.

![Footer hotkey display](/docs2/images/editors/3d-viewport/header/armature-pose-mode-pose-menu/footer-hotkey-display-2.png)

Overshoot allows you to go over the 0 -100 per cent range. The header values shows a bigger range then.

The rest of the hotkeys should be self explaining.

#### Breakdowner

Create a suitable breakdowner pose on the current frame.

##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

##### Last Operator Pose Breakdowner

![Last Operator Pose Breakdowner](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-pose-breakdowner.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Which channels to affect.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Lock the action to specific axis.

#### Push

Push exaggerates the current pose.

##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

##### Last Operator Push Pose from Breakdown.

![Last Operator Push Pose from Breakdown.](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-push-pose-from-breakdown.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Which channels to affect.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Lock the action to specific axis.

#### Relax

Relax relaxes the current pose.

##### Header Values

![Header Values](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/header-values-2.png)

When you move the mouse then you will see some values in the header, which shows the current factor. This value is relative to the starting value, which always starts with 0. It also shows some more available transform hotkeys.

It also shows some more available transform hotkeys. The hotkeys W E and R allows you just to move, rotate or scale. Hotkey B stands for Bendy Bones. And C is for a custom property. This hotkeys are hard coded, and cannot be changed in the input manager.

##### Last Operator Relax Pose to Breakdown

![Last Operator Relax Pose to Breakdown](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/last-operator-relax-pose-to-breakdown.png)


| Entry | What it does |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| Previous Keyframe | The keyframe position before the current frame. |
| Next Keyframe | The keyframe position after the current frame. |
| Percentage | The percentage of exaggeration. Interestingly the value in the Last operator differs from the value in the header. |


###### Channels

![Channels](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/channels.png)

Here you can again choose if you just want to limit a specific channel.

###### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/tool-shelf/armature-pose-mode/axis-lock.png)

Allows you to lock a specific axis.

