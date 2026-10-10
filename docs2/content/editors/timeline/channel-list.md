---
id: "editors.timeline.channel-list"
title: "Timeline channel list"
section: "editors"
path: ["Editors", "Timeline", "Channel list"]
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17.2 Editors - Timeline - Channel list.odt", "17 Editors - Timeline.odt"]
---

![Channel list](/docs2/images/ui/timeline/channel-list/timeline-channel-list.png){.right}

The **channel list** shows your objects and their animation channels. It is the same list as in the Dope Sheet, but the Timeline has no modes, so it only shows Dope Sheet content. Shape key and Grease Pencil animation are not listed.

The list is hidden by default. Click the small button at the top left to show it. Drag its right border to resize it.

## Hotkeys

| Input | What it does |
|---|---|
| :kbd[A] | Selects all channels |
| :kbd[Alt+A] | Deselects all |
| :kbd[LMB] | Selects a channel |
| :kbd[Shift+LMB] | Adds a channel to the selection, or removes it |
| :kbd[LMB] drag | Box select |

## Row elements

| Element | What it does |
|---|---|
| ![](/docs2/images/ui/timeline/channel-list/search-field.png){.icon} **Search field** | Filters the list by name |
| ![](/docs2/images/ui/timeline/channel-list/expand-collapse-triangle.png){.icon} **Expand triangle** | Opens or closes a level of the hierarchy |
| ![](/docs2/images/ui/timeline/channel-list/object-type-icon.png){.icon} **Object type icon** | Shows what the channel belongs to. It cannot be clicked |
| **Channel name** | Double-click to rename an element, such as an action or object. Press :kbd[Enter] or click elsewhere to confirm |
| ![](/docs2/images/ui/timeline/channel-list/enable-f-curve-modifiers.png){.icon} **Enable F-Curve modifiers** | Turns the channel's F-Curve modifiers on or off. Modifiers are added in the Graph Editor |
| ![](/docs2/images/ui/timeline/channel-list/mute-channel.png){.icon} **Mute** | The channel is not calculated |
| ![](/docs2/images/ui/timeline/channel-list/lock-channel.png){.icon} **Lock** | The channel cannot be edited |

## Channel context menu

![Channel context menu](/docs2/images/ui/timeline/channel-list/channel-context-menu.png){.right}

Right-click in the channel list to open the **Channel context menu**.

| Menu entry | What it does |
|---|---|
| Frame Selected Channels | Centres the selected channels in the view |
| Mute / Unmute Channel | Stops or restarts calculating the channel |
| Protect / Unprotect Channels | Locks or unlocks the channels for editing |
| Toggle Channel Editability | Switches protection on or off |
| Group / Ungroup Channels | Groups the channels. Ungrouped channels do not return to their old group |
| Extrapolation Mode › | How the curve continues before the first and after the last keyframe (below) |
| Expand / Collapse Channels | Opens or closes the hierarchy |
| Move Channels › | Changes the order of the channels |
| Delete Channels | Deletes the selected channels |

### Extrapolation mode

| Entry | What it does |
|---|---|
| Constant Extrapolation | The curve stays flat after the last keyframe |
| Linear Extrapolation | The curve keeps its last direction |
| Make Cyclic | Loops the animation. The first frame is matched to the last |
| Clear Cyclic | Removes the loop |
