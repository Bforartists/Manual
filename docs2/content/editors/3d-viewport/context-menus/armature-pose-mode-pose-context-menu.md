---
id: editors.3d-viewport.context-menus.armature-pose-mode-pose-context-menu
title: Armature - Pose Mode - Pose context menu
section: editors
path:
  - Editors
  - 3D Viewport
  - Context menus
  - Armature - Pose Mode - Pose context menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 7.0.19 Editors - 3D Viewport - Armature - Pose Mode - Pose context menu.odt
---
## Pose Mode - Pose Context Menu

![Pose Mode - Pose Context Menu](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-mode-pose-context-menu.png)

Call this menu with double right click in the 3D viewport. You need to be in Edit mode with an armature object.

### Insert Key frame

Inserts a keyframe and uses the default keying set defined in the preferences.

### Insert Key frame with Keying Set

![Insert Key frame with Keying Set](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/insert-key-frame-with-keying-set.png)

Opens a menu where you can insert a key frame with a defined keying set.

### Copy Pose

![Copy Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/copy-pose.png)

Copies the current pose. You copy what you have selected.

### Paste Pose

Pastes a previous copied pose.

### Paste X Flipped Pose

Pastes a previous copied pose, but flipped along X axis.

#### Last Operator Paste Pose

![Last Operator Paste Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-paste-pose.png)


| Entry | What it does |
| ----------------- | -------------------------------------------------------- |
| Flipped on X Axis | Paste the pose flipped along X Axis. |
| On Selected Only | Paste just on the selected bones. Not on the unselected. |


### Rename active Bone

![Rename active Bone](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/rename-active-bone.png)

Calls a dialog where you can rename the active bone.

### “Push Pose from Breakdown

Exaggerates the current pose. Pushes the current pose further away from the previous pose.

#### Last Operator Push Pose

![Last Operator Push Pose](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-push-pose.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of exaggeration. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


##### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the push effect to specific channels.

##### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the push effect to specific axis.

### Relax Pose to Breakdown

Relaxes the current pose.

#### Last Operator Relax Pose to Breakdown

![Last Operator Relax Pose to Breakdown](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-relax-pose-to-breakdown.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of relaxing. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


##### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the relax effect to specific channels.

##### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the relax effect to specific axis.

##### Pose Breakdowner

Creates a suitable breakdowner pose on the current frame.

![Pose Breakdowner](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-breakdowner.png)

When you perform the tool then you will see a per cent slider in the header where you can read the percentual influence of the blending. Move the mouse to position the blend pose where you need it.

###### Last Operator Pose Breakdowner

![Last Operator Pose Breakdowner](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-pose-breakdowner.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------ |
| Percentage | The percentage of exaggeration. |
| Previous Key frame | The key frame position before the current frame. |
| Next Key frame | The key frame position after the current frame. |


##### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels.png)

Limit the breakdowner pose to specific channels.

##### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock.png)

Limit the breakdowner pose to specific axis.

### Blend to Neighbour

Blends the current pose with the neighbouring poses.

![Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/pose-breakdowner.png)

When you perform the tool then you will see a per cent slider in the header where you can read the percentual influence of the blending. Move the mouse to position the blend pose where you need it.

#### Last Operator Blend to Neighbour

![Last Operator Blend to Neighbour](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-blend-to-neighbour.png)


| Entry | What it does |
| ----------------- | ----------------------------------------------------------- |
| Factor | The blend factor. |
| Previous Keyframe | The keyframe to calculate from before the current position. |
| Next Keyframe | The keyframe to calculate from after the current position. |


##### Channels

![Channels](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/channels-2.png)

##### Axis Lock

![Axis Lock](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/axis-lock-2.png)

Lock the transformation along an axis.

### Calculate Motion Paths

![Calculate Motion Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths.png)

Objects can be animated. Let's say you send them from a to b to c. The object will move to b, then to c. Some kind of a path. This path is not visible by default.

With motion paths you can calculate this path, and make it visible.

![Calculate Motion Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/calculate-motion-paths-2.png)

Calculate Motion path calls a setup dialog.

#### Display Type

![Display Type](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/display-type.png)

How to display the motion path.


| Entry | What it does |
| ------------ | -------------------------------------------------------------------------------- |
| Around Frame | Display paths of poses within a fixed number of frames around the current frame. |
| In Range | Display paths of poses within specified frames. |


#### Computation Range

![Computation Range](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/computation-range.png)

How much frames to compute.


| Entry | What it does |
| ----------------- | --------------------------------------------- |
| All Keys | From the first keyframe to the last. |
| Selected Keys | From the first selected keyframe to the last. |
| Scene Frame Range | The entire scene / preview range. |
| Manual Range | Manually determined frame range. |


#### Bake Location

![Bake Location](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/bake-location.png)

To bake from where.


| Entry | What it does |
| ----- | -------------------------------- |
| Heads | Calculate bone paths from heads. |
| Tails | Calculate bone paths from tails. |


#### Last Operator Calculate Bone Paths

![Last Operator Calculate Bone Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-calculate-bone-paths.png)

Same than the dialog.

### Clear Motion Paths

Clear remove the motion path from the object.

#### Last Operator Clear Bone Paths

![Last Operator Clear Bone Paths](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-clear-bone-paths.png)

##### Only Selected

Only clear motion patsh of selected bones.

### Update Armature Motion Paths

Updates the motion paths for the armature object.

### Move to Bone Collection

![Move to Bone Collection](/docs2/images/editors/3d-viewport/context-menus/armature-edit-mode-armature-context-menu/move-to-bone-collection.png)

Armature and bones have their own collection system. This menu item opens a popup where you can put the selected bones into a New Collection or an existing Bone Collection.


| Entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New Bone Collection | Assigns the selected bones to a new Bone Collection. This will prompt to name the new collection. |
| Bone List | Assigns or unassigns the selected bones to or from the collection. The green + icon and red – icon show if you can remove or add a bone to the listed collection. |


### Show Hidden

Reveals the hidden bones.

### Hide Selected

Hides the selected bones.

#### Last Operator Hide Selected

![Last Operator Hide Selected](/docs2/images/editors/3d-viewport/context-menus/object-mode-object-context-menu/last-operator-hide-selected.png)

##### Unselected

Hide unselected bones too.

### Hide Unselected

Makes all unselected bones hidden.

#### Clear User Transforms

Resets Pose of selected bones back to key frame state.

#### Last Operator Clear User Transforms

![Last Operator Clear User Transforms](/docs2/images/editors/3d-viewport/context-menus/armature-pose-mode-pose-context-menu/last-operator-clear-user-transforms.png)

##### Only Selected

Only clear motion patsh of selected bones.

