---
id: editors.dope-sheet.header.channel-menu
title: Channel Menu
section: editors
path:
  - Editors
  - Dope Sheet
  - Header
  - Channel Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 16.1.6 Editors - Dope Sheet - Channel Menu.odt
---
## Dopesheet Editor - Channel Menu

![Dopesheet Editor - Channel Menu](/docs2/images/editors/dope-sheet/header/channel-menu/dopesheet-editor-channel-menu.png)

This menu contains functionality to manage the channels in the channels list at the left.

The menu doesn't exist in all modes. It exists in Dope sheet, Action Editor and Grease Pencil mode. And has different content.

## Channel Menu - Dope sheet + Action Editor mode

### Delete Channels

Deletes the selected channels and all its keyframes.

### Group Channels

Creates a custom group from the selected channels.

![Group Channels](/docs2/images/editors/dope-sheet/header/channel-menu/group-channels.png)

### Ungroup Channels

Removes the selected channels from the group, and adds them back to the original hierarchy.

### Channel Settings

Adjusts the locks and check boxes in the channels list from outside of the channels list for all selected elements at once. With Toggle Mute you could, for example, disable all selected channels at once.

The menu items should be self explaining.

These are also accessible from the Dopesheet Channel Context Menu.

![Channel Settings](/docs2/images/editors/dope-sheet/header/channel-menu/channel-settings.png)

### Toggle Channel Editability

Toggles the locks in the channel list from their previous state to locked and back.

### Extrapolation Mode

![Extrapolation Mode](/docs2/images/editors/dope-sheet/header/channel-menu/extrapolation-mode.png)

Sets the extrapolation mode for the selected F-Curves. Means how the curve acts at the beginning and the end of the F-Curve.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Constant Extrapolation | The animation curve continues straight at the end. |
| Linear Extrapolation | The animation curve continues the last direction. |
| Make Cyclic | Makes the animation loopable. The interpolation curves are adjusted so that the first frame fits to the last frame. |
| Clear Cyclic | Removes the cyclic extrapolation. |


| Entry | What it does |
| ----------------- | -------------------------------------------- |
| Expand Channels | Expands all channels in the channel list. |
| Collapse Channels | Collapses all channels in the channels list. |


### Move

![Move](/docs2/images/editors/dope-sheet/header/channel-menu/move.png)

Sort the items in the channels list.

### Revive Disabled F-Curves

Clears the disabled tag from all f-curves to get broken F-Curves working again.

### Bake Channels

Bakes the animation by adding a keyframe at every single frame.

#### Adjust last operator Bake Channels

![Adjust last operator Bake Channels](/docs2/images/editors/dope-sheet/header/channel-menu/adjust-last-operator-bake-channels.png)


| Entry | What it does |
| -------------------- | ------------------------------------------------------ |
| Frame Range | The frame range of the animation to bake. |
| Frame Step | Create a keyframe every nth frame. |
| Remove Outside Range | Removes keyframes that are outside of the frame range. |


##### Interpolation Type

![Interpolation Type](/docs2/images/editors/dope-sheet/header/channel-menu/interpolation-type.png)

Interpolation type for the animation curves.

##### Bake Modifiers

Bake modifiers into keyframes, and delete them.


| Entry | What it does |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Frame Selected Channels | Resets the viewable area to show the selected channel keyframes. This will change the zoom to fit all in the selected chanel. |
| Discontinuity (Euler Filter) | Fix large jumps and flips in the selected Euler Rotacion F-Curves arising from the rotation values being clipped when baking physics. This operator only affects Euler rotation animation. |


## Channel Menu - Grease Pencil mode

### Delete Channels

![Delete Channels](/docs2/images/editors/dope-sheet/header/channel-menu/delete-channels.png)

Deletes the selected channels and all its keyframes.

### Channel Settings

![Channel Settings](/docs2/images/editors/dope-sheet/header/channel-menu/channel-settings-2.png)

Adjust the locks and check boxes in the channels list from outside of the channels list for all selected elements at once. With Toggle Mute you could for example disable all selected channels at once.

The menu items should be self explaining.

![Channel Settings](/docs2/images/editors/dope-sheet/header/channel-menu/channel-settings-3.png)

### Move Channels

![Move Channels](/docs2/images/editors/dope-sheet/header/channel-menu/move-channels.png)

Sort the items in the channels list.

### Frame Selected Channels

Zooms in or out to fit the view to the selected channels.

