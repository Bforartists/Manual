---
id: editors.nonlinear-animation-editor.header.nla-editor-add-menu
title: NLA Editor - Add Menu
section: editors
path:
  - Editors
  - Nonlinear Animation Editor
  - Header
  - NLA Editor - Add Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 20.1.6 Editors - NLA Editor - Add Menu.odt
---
## NLA Editor - Add Menu

![NLA Editor - Add Menu](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-add-menu/nla-editor-add-menu.png)

A menu where you can add various elements to the NLA.

### Add Action Strip

![Add Action Strip](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-add-menu/add-action-strip.png)

Adds an action strip. Opens a popup menu where you can choose what animation data this new action strip should contain.

### Add Transition

![Add Transition](/docs2/images/editors/nonlinear-animation-editor/header/nla-editor-add-menu/add-transition.png)

Adds a transition strip between two selected action strips.

### Add Sound Clip

![Add Sound Clip](/docs2/images/editors/nonlinear-animation-editor/sound-clip-strips.png)

Adds a sound clip at the marker position.

A Sound Clip Controls when a speaker plays a sound. This strip type requires a Speaker object with a sound clip assigned. You can create a speaker object in the 3D view. The sample can be loaded in the Object Data Properties tab in the Properties editor then.

### Add Meta Strips

![Add Meta Strips](/docs2/images/editors/nonlinear-animation-editor/add-meta-strips.png)

Turns selected strips into a meta strip. A group of strips.


| Entry | What it does |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Remove Meta Strips | Ungroups the meta strips into its original action strips. |
| Add Tracks | Adds a new track in the Channel list. |
| Add Tracks Above Selected | Adds a new track in the Channel list. |
| Include Selected Objects | Objects without animation or a NLA strip will not appear in the channel list. With this command you can load selected objects into the NLA, regardless if they have animation yet or not. |


