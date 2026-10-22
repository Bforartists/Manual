---
id: editors.nonlinear-animation-editor.header.nla-editor-strip-menu
title: NLA Editor - Strip Menu
section: editors
path:
  - Editors
  - Nonlinear Animation Editor
  - Header
  - NLA Editor - Strip Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 20.1.8 Editors - NLA Editor - Strip Menu.odt
---
## NLA Editor - Strip Menu

![NLA Editor - Strip Menu](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/nla-editor-strip-menu.png)

This menu contains functionality to manage the keyframes.

### Transform

![Transform](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/transform.png)

#### Grab/Move

Moves the selected keyframe(s).

##### Last Operator Move

![Last Operator Move](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/last-operator-move.png)

###### Move X, Y Z

The position. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel.

###### Orientation

![Orientation](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enable Mirror editing

###### Proportional editing

![Proportional editing](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/proportional-editing.png)

Proportional editing is not available for this mode.

#### Extend

Moves the last keyframes of the selection.

##### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/last-operator-transform.png)


| Entry | What it does |
| ---------------- | ------------------------ |
| Values X, Y Z, W | The new position. |
| Axis | Which axis to transform. |


###### Orientation

![Orientation](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enable Mirror editing

###### Proportional editing

![Proportional editing](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/proportional-editing.png)

Proportional editing is not available for this mode.

#### Scale

Scales the selected keyframes. You need to have more than one keyframe selected.

##### Last Operator Resize

![Last Operator Resize](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/last-operator-transform.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


###### Orientation

![Orientation](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enable Mirror editing

###### Proportional editing

![Proportional editing](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/proportional-editing.png)

Proportional editing is not available for this mode.

### Snap

![Snap](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/snap.png)

Snaps the selected keyframes by the chosen method.


| Entry | What it does |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bake Action | Bakes all selected objects locations/scale/rotation animations to an action. To use this operator, a dialogue will prompt to define the parameters before applying the bake action. The final animation of the selected objects or bones is computed with all modifiers, drivers, and constraints applied with keyed results per frame step in a range. |
| Duplicate | Duplicate selected keyframes. |


### Linked Duplicate

![Linked Duplicate](/docs2/images/editors/nonlinear-animation-editor/linked-duplicate.png)

Duplicates the selected strip(s), and creates a new track for the duplicates. This copy is linked to the original action strip. Modifications at the original will also affect the linked action strip.

Linked strips are visually different from normal strips. And when you start to modify the linked duplicate, then the original strip will turn red.

### Split Strips

![Split Strips](/docs2/images/editors/nonlinear-animation-editor/split-strips.png)

Splits the selected strip(s) at the marker position.

### Rename

![Rename](/docs2/images/editors/nonlinear-animation-editor/rename.png)

Allows you to rename the current NLA strip. The operator calls a rename popup.


| Entry | What it does |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Delete Strips | Deletes the selected strips. |
| Delete Tracks | Deletes the selected track(s). **Toggle Muting** Disables the selected action clip. Be careful, there is no visual hint if the clip is muted or not. |
| Apply Scale | Applies the current scale of the clips to be 1. |
| Clear Scale | Resets the scale of the clip back to 1. |
| Sync Action Length | Synchronize the length of the action with the keyframe length used in the strip. |
| Make Single User | You can create linked duplicates. Make single user makes them into individual clips. |
| Swap Strips | Swaps the selected strips. |
| Move strips up | Moves the selected action strips upwards into the next track. |
| Move Strips down | Moves the selected action strips downwards into the next track. |


### Tweak Action (Lower Stack)

![Tweak Action (Lower Stack)](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-strip-menu/tweak-action-lower-stack.png)

Allows you to edit the keyframe data within the Action strip while evaluating only Action clips located below the active track in the NLA stack. This mutes all tracks above the active Action clip track and only evaluates tracks below.

This tweak mode is similar to the one in the header but it allows you to insert keyframes and preserve the pose that you visually keyed while lower strips are evaluating only.

Note that **Tweak Isolated Action** and **Tweak Action (Full Stack)** is done from the header. And leaving the Tweak mode is for all methods evaluated in the header by clicking at the active Tweak button.

