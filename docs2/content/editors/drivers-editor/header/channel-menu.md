---
id: editors.drivers-editor.header.channel-menu
title: Channel Menu
section: editors
path:
  - Editors
  - Drivers Editor
  - Header
  - Channel Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 19.1.5 Editors - Drivers Editor - Channel Menu.odt
---
## Drivers Editor - Channel Menu

![Drivers Editor - Channel Menu](/docs2/images/editors/drivers-editor/header/channel-menu/drivers-editor-channel-menu.png)

This menu contains functionality to manage the channels in the channels list at the left.

The menu doesn't exist in all modes. It exists in Dopesheet, Action Editor and Grease Pencil mode. And has different content.


| Entry | What it does |
| ---------------------- | ---------------------------------------------------- |
| Delete Channels | Deletes the selected channels and all its keyframes. |
| Delete Invalid Drivers | Deletes invalid drivers. |


### Group Channels

Creates a custom group from the selected channels.

![Group Channels](/docs2/images/editors/drivers-editor/header/channel-menu/group-channels.png)

### Ungroup Channels

Removes the selected channels from the group, and adds them back to the original hierarchy.

### Channel Settings submenu

Adjust the locks and check boxes in the channels list from outside of the channels list for all selected elements at once. With Toggle Mute you could for example disable all selected channels at once.

The menu items should be self explaining.

![Channel Settings submenu](/docs2/images/editors/drivers-editor/header/channel-menu/channel-settings-submenu.png)

#### Last Operator Toggle Channel Settings

![Last Operator Toggle Channel Settings](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-toggle-channel-settings.png)

#### Type

The type to toggle.

### Extrapolation Mode

![Extrapolation Mode](/docs2/images/editors/drivers-editor/header/channel-menu/extrapolation-mode.png)

Sets the extrapolation mode for the selected F-Curves. Means how the curve acts at the beginning and the end of the F-Curve.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Constant Extrapolation | The animation curve continues straight at the end. |
| Linear Extrapolation | The animation curve continues the last direction. |
| Make Cyclic | Makes the animation loopable. The interpolation curves are adjusted so that the first frame fits to the last frame. |
| Clear Cyclic | Removes the cyclic extrapolation. |


#### Last Operator Set F-Curve Extrapolation

![Last Operator Set F-Curve Extrapolation](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-set-f-curve-extrapolation.png)

##### Type

Set the extrapolation mode for the selected F-Curves.

### Add F-Curve Modifer submenu

![Add F-Curve Modifer submenu](/docs2/images/editors/drivers-editor/header/channel-menu/add-f-curve-modifer-submenu.png)

Add an F-Curve Modifier. The modifiers can be found in the Sidebar in the Modifiers tab then.

### Reveal Curves

Reveals all hidden curves.

#### Last Operator Reveal Curves

![Last Operator Reveal Curves](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-reveal-curves.png)

##### Select

Select all revealed curves.

### Hide selected Curves

Hides the selected curves.

### Hide unselected curves

Hides the unselected curves.

#### Last Operator Hide Curves

![Last Operator Hide Curves](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-hide-curves.png)

##### Unselected

Hide the unselected or selected curves.

### Expand Channels

Expands all channels in the channel list.

#### Last Operator Expand Channels

![Last Operator Expand Channels](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-expand-channels.png)

##### All

Expand all Channels, or just the selected channels.

### Collapse Channels

Collapses all channels in the channels list.

#### Last Operator Collapse Channels

![Last Operator Collapse Channels](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-collapse-channels.png)

##### All

Collapse all Channels, or just the selected channels.

### Move submenu

![Move submenu](/docs2/images/editors/drivers-editor/header/channel-menu/move-submenu.png)

Sort the items in the channels list.

#### Frame Selected Channels

Zooms in or out to fit the selected channels into the view.

#### Last Operator Move Channels

![Last Operator Move Channels](/docs2/images/editors/drivers-editor/header/channel-menu/last-operator-move-channels.png)

##### Direction

![Direction](/docs2/images/editors/drivers-editor/header/channel-menu/direction.png)

Sort the items in the channels list.


| Entry | What it does |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Revive Disabled F-Curves | Clears the disabled tag from all f-curves to get broken F-Curves working again. |
| Discontinuity (Euler) Filter | Fix large jumps and flips in the selected Euler Rotation F-Curves. These can arise from rotation values being clipped when baking physics. |


