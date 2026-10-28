---
id: editors.dope-sheet.header
title: Header
section: editors
path:
  - Editors
  - Dope Sheet
  - Header
version: "5.1"
status: draft
screenshots: "5.1"
replaces:
  - editors.dope-sheet.header.header-tools-and-options
  - editors.dope-sheet.header.quick-menu
  - editors.dope-sheet.header.view-menu
  - editors.dope-sheet.header.select-menu
  - editors.dope-sheet.header.marker-menu
  - editors.dope-sheet.header.channel-menu
  - editors.dope-sheet.header.key-menu
  - editors.dope-sheet.header.action-menu
order: 10
summary: "The header contains various menus and tools."
---
The pages of this part are listed in the sidebar under *Header*.

# Header Tools and Options

## Introduction

The header contains various menus and tools. This chapter here is about the tools, modes and options elements in the header.

The text menus are covered in an own chapter each. They vary too much, dependent of mode and object type.

![Introduction](/docs2/images/editors/dope-sheet/header/header-tools-and-options/introduction.png)

## Header Tabs

![Header Tabs](/docs2/images/editors/dope-sheet/header/header-tools-and-options/header-tabs.png)

The tabs at the very left allows you to switch between the four most important editor types by one click. Dope sheet Editor, Graph Editor, Driver Editor, NLA Editor.

## Dope Sheet Modes

![Dope Sheet Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet-modes.png)

The Dope sheet has different modes. Each mode has its own purpose. In Mask mode you can for example see and edit the keyframes for mask animations, from the movie clip editor for example.

### Dope Sheet

![Dope Sheet](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet.png)

![Dope Sheet](/docs2/images/editors/dope-sheet/header/header-tools-and-options/dope-sheet-2.png)

Display the keyframe animation of all currently selected object in the 3d view.

### Action Editor

![Action Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-editor.png)

Display and edit the Action part of a keyframe animation of the currently active object in the 3d view. Just the data for this one object is displayed.

![Action Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-editor-2.png)

**Actions** are a generic containers for F-Curves. Actions can contain any number of F-Curves, and can be attached to any data block. For example, an action that modifies the ‘X location’ and ‘Y location’ properties can be shared across multiple objects, since both objects have ‘X location’ and ‘Y location’ properties available.

The Action editor allows you to edit the animation in various ways. For example also turn a keyframe animation into a clip for the NLA editor.

The animation data is build in a hierarchical way. From top to bottom.

Actions - Record and contain animation data.

Groups - Are groups of channels.

Channels - Contains record properties.

F-Curves - F-Curves are used to interpolate the difference between the keyframes.

Keyframes - Keyframes are used to set the values of properties bound to a point in time.

### Shape Key Editor

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor.png)

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor-2.png)

Display and and edit the keyframes for shape key animations. Shape keys is vertex animation.

![Shape Key Editor](/docs2/images/editors/dope-sheet/header/header-tools-and-options/shape-key-editor-3.png)

### Grease Pencil

![Grease Pencil](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil.png)

![Grease Pencil](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil-2.png)

Display and and edit the keyframes for animated grease pencil strokes.

This mode is for when you animate grease pencil strokes and colors at a vertex level. When you record keyframes at an object level then those keyframes gets displayed in the Dope sheet and Action mode.

### Mask

![Mask](/docs2/images/editors/dope-sheet/header/header-tools-and-options/mask.png)

Display and edit the keyframes for animated mask curves. Like from the movie clip editor.

![Mask](/docs2/images/editors/dope-sheet/header/header-tools-and-options/grease-pencil-2.png)

### Cache File

![Cache File](/docs2/images/editors/dope-sheet/header/header-tools-and-options/cache-file.png)

NOT DOCUMENTED BY BLENDER. NOT TO FIND OUT HOW TO USE.

From the Blender Manual: Cache File: Alembic Todo 2.78.

## Show Hide elements

![Show Hide elements](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-hide-elements.png)

This is a group of header operators for animation channel visibility. This is present in all dopesheet modes.

### Summary

![Summary](/docs2/images/editors/dope-sheet/header/header-tools-and-options/summary.png)

Display the Summary label above the list of elements.

| Entry | What it does |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Only Show Selected | Display only the data for the selected object in the list of elements. If off it displays all available animation data of the whole scene. |
| Show Hidden | Include channels from objects / bones that are not visible. This feature just works with Only Selected off. |
| Only Show Errors | Only display F-Curves and Drivers that have errors or are disabled. |

## Filters - Dope Sheet Mode

![Filters - Dope Sheet Mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/filters-dope-sheet-mode.png)

The show hide elements allows you to filter out the general elements. The Filters panel allows you to filter out further elements.

Note that this filter methods just exists for the dope sheet mode.

### Filter by Collection

Just display the content from the chosen collection in the list of elements.

### Filter by Type

![Filter by Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/filter-by-type.png)

In this section you can choose what type of animation data should be displayed. The names should be self explaining.

### Options

| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------ |
| Sort Data Blocks | Alphabetically sort the data in the list of elements. |
| Multi Word Match Search | Enable Multi Word matching for the search in the list of elements. |

## Snapping Panel – Most modes

![Snapping Panel – Most modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/snapping-panel-most-modes.png)

Snapping in animation editors helps align the **playhead** and **keyframes** to meaningful time-based elements, improving precision and workflow efficiency across the **Timeline**, **Dope Sheet**, **Graph Editor**, **NLA**, and **Video Sequencer**.

> **Note:** This sub-subpanel is not available for Grease Pencil Dopesheet Mode

| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Snapping On/Off | Toggles the snapping on or off with a visual indicator. |
| Frame | Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame timeline cursor placement. |
| Second | Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing. |
| Nearest Market | Snaps to the closest timeline marker. Great for aligning actions to scene events or beats. |
| Absolute Time Snap | When enabled, snapping uses absolute time rather than relative pixel proximity. Ensures consistent snapping behavior regardless of zoom level or cursor position. |

## Proportional Editing - All Modes

![Proportional Editing - All Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/proportional-editing-all-modes.png)

Enable proportional editing.

Proportional editing allows you for example to scale two keyframes and influence the not selected neighbour keyframes in a proportional way. Or the proportional editing of fcurve points.

The dropdown menu to choose the proportional editing falloff method is just available when the proportional tool is active.

## Keyframe Easing, Handle Type, Keyframe Interpolation, Keyframe Type - All Modes

![Keyframe Easing, Handle Type, Keyframe Interpolation, Keyframe Type - All Modes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/keyframe-easing-handle-type-keyframe-interpolati.png)

### Easing Mode

![Easing Mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/easing-mode.png)

Choose between different easing modes for the selected keyframes. Easing is a method to fade in and out curves.

### Handle Type

![Handle Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/handle-type.png)

Set the handle type for the currently selected keyframes.

This is a feature for the Graph editor, where each curve point has its own handler with which you can influence the curve behaviour. But the handler type also influences how the animation curve acts at the chosen keyframes. So it has its use in the dopesheet editor too.

![Handle Type](/docs2/images/editors/dope-sheet/handle-type-2.png)

### Set Keyframe Interpolation

![Set Keyframe Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/set-keyframe-interpolation.png)

The Interpolation mode defines how the curve acts from keyframe to keyframe. You can have a linear curve between two keyframes instead of a bent one for example.

The easing methods here in the interpolation mode menü are for the easing shape. There is also a easing menu where you can choose a easing method.

### Keyframe Type

![Keyframe Type](/docs2/images/editors/dope-sheet/header/header-tools-and-options/keyframe-type.png)

Recolor the currently selected keyframes. Or create the next keyframe with this chosen keyframe color.

## Tools + Action Slots - Action Editor mode

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode.png)

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode-2.png)

![Tools + Action Slots - Action Editor mode](/docs2/images/editors/dope-sheet/header/header-tools-and-options/tools-action-slots-action-editor-mode-3.png)

### Action Data Browser property

![Action Data Browser property](/docs2/images/editors/dope-sheet/header/header-tools-and-options/action-data-browser-property.png)

When there is more than one animated object in the scene then you have most probably more than one action in the scene too. The Action Data Browser allows you to display, select and rename the available actions in the scene.

| Entry | What it does |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Action Data Browser | The list of available actions in the scene. |
| Number of Fake Users | Displays the current number of fake users for the active action. |
| Fake User | Assign a fake user to this action. Fake users is a odd concept to keep data in the scene even if it has no user somewhere. The fake user is then a dummy user so that the object is not deleted when saving the scene. |
| New Action | Add a new blank action. |
| Unlink Action | Delete the current active action. |

### Included data property

![Included data property](/docs2/images/editors/dope-sheet/header/header-tools-and-options/included-data-property.png)

This slot identifies which data is included in the action clip. This is useful to animate multiple elements together. You can assign the objects in the Animation Panel or Dopesheet in Action Clip mode. Its identifier natge is used to find the right slot wehn assigning an Action.

| Entry | What it does |
| ------------- | -------------------------------------------------------- |
| Data Browser | The list of available objects in the action. |
| New Slot | Add a new object to the animation slot. |
| Unassign Slot | Delete the current active object from the animation slot |

### Push Down

Adds the active action on to the NLA stack as a contributing strip. The same can be done by pressing the Push Down button in the NLA Editor.

### Stash

Stashes the active action on to the NLA stack. This means it is added as a non-contributing stack in the same way that it would if you were creating a new action instead.

> **Note:** Push down and Stash adds the action to the NLA stack. It is cleared / unassigned from the active action slot.
>
> This means that the action cannot be edited anymore fom the Action or Graph Editors, unless you enter “Tweak Mode” on the corresponding strips later.

### Only show Slot of active Object

Show or hide other action slots.

## Tools - Grease Pencil mode

### Add new Layer

![Add new Layer](/docs2/images/editors/dope-sheet/header/header-tools-and-options/add-new-layer.png)

Adds a new blank grease pencil layer.

### Remove Layer

Removes the currently selected grease pencil layer.

### Layer Specials

![Layer Specials](/docs2/images/editors/dope-sheet/header/header-tools-and-options/layer-specials.png)

A menu with grease pencil functionality.

| Entry | What it does |
| --------------------------- | ------------------------------------------------------ |
| Move to Top | Move the layer to Top |
| Move to Bottom | Move the layer to Bottom. |
| Duplicate layer | Duplicates the currently selected grease pencil layer. |
| Duplicate Empty layer | Add an empty copy of the selected grease pencil layer. |
| Show All | Shows all hidden grease pencil layers. |
| Hide Others | Hides all grease pencil layers but the selected. |
| Lock All | Locks all grease pencil layers. |
| Unlock All | Unlocks all grease pencil layers. |
| Merge Down | Merge the current layer with the layer below. |
| Merge Group | Combine layers based on the mode into one layer. |
| Merge All | Merge all layers together |
| Copy Layer to selected | Copies the grease pencil layer to the selected object. |
| Copy All Layers to selected | Copies all grease pencil layer to the selected object. |

| Entry | What it does |
| ---------------------------------- | --------------------------------------------------------- |
| Move Grease Pencil Layer upwards | Moves the grease pencil layer upwards in the hierarchy. |
| Move Grease Pencil Layer downwards | Moves the grease pencil layer downwards in the hierarchy. |
| Isolate Layer with visibility | Locks and hides the currently active grease pencil layer. |
| Isolate Layer without visibility | Locks the currently active grease pencil layer. |

## Options

![Options](/docs2/images/editors/dope-sheet/header/header-tools-and-options/options.png)

### Real-time Updates

When transforming keyframes then this transformation is also immediately visible in other editors.

### Show Seconds

![Show Seconds](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.

### Sync visible range

Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked.

### Show Sliders

![Show Sliders](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-sliders.png)

![Show Sliders](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-sliders-2.png)

Shows the value sliders for f-curve channels in the channel list.

### Show Handles and Interpolation

![Show Handles and Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-handles-and-interpolation.png)

With this option on the keyframes shows different shapes that depends of their handle type.

With this option off all keyframes shows as diamond shape.

![Show Handles and Interpolation](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-handles-and-interpolation-2.png)

### Show Curve Extremes

![Show Curve Extremes](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-curve-extremes.png)

Shows the curve extremes at the keyframe icons.

| Entry | What it does |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AutoMerge Keyframes | Automatically merge nearby keyframes. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |
| Sync Markers | Sync markers with keyframe edits. When you move the keyframes, then the markers will move too. |
| Show Cache | Show the status of cached frames in the timeline. · **Softbody**: Show the status for softbody objects. · **Particles**: Show the status for Particles objects. · **Cloth**: Show the status for Cloth objects. · **Simulation Nodes**: Show the status for Simulation Nodes objects. · **Smoke**: Show the status for Smoke objects. · **Dynamic Paint**: Show the status for Dynamic Paint objects. · **Rigid Body**: Show the status for Rigid Body objects. |

## Show Overlays

### Show Overlays

![Show Overlays](/docs2/images/editors/dope-sheet/header/header-tools-and-options/show-overlays.png)

Show the overlays.

### Overlay Options

#### Dope Sheet Overlays

##### Show Scene Strip Range

Show the scene strip range when synchronizing the time with the sequencer.

# Quick Menu

## Quick Menu

![Quick Menu](/docs2/images/editors/dope-sheet/header/quick-menu/quick-menu.png)

The quick menu, or in long Quick Favorites menu, is a menu that can be customized to your needs. Here you can add operators for quick access.

It is located in the header. But it can be called by hotkey Q directly under the mouse. This hotkey works in other editors too.

When the menu is empty, then you will see the message "No Menu Items found". This means that you first have to add some tools to the menu. It is a user configurable menu.

Note that added operators in this menu does not have icons. Just text.

### Adding an operator to the Quick menu

![Adding an operator to the Quick menu](/docs2/images/editors/dope-sheet/header/quick-menu/adding-an-operator-to-the-quick-menu.png)

Open the panel or the menu where your operator is that you want to add.

Let's add the open command from the File menu. Open the File menu, right click at open, and choose Add to Quick Favorites.

Do the same with Save As. We should now have two new menu items in the Quick menu, which you can use now.

![Adding an operator to the Quick menu](/docs2/images/editors/dope-sheet/header/quick-menu/adding-an-operator-to-the-quick-menu-2.png)

As a rule of thumb, when the right click menu has an Add to Quick Favorites, then you can add it to the quick menu.

Note that you can also add operators from the tool shelf at the left. And also operators from other editor types. Some other editors have their own quick menu though. The Image Editor for example. These operators gets added in the quick menu of the image editor then. And does not show in the quick menu in the header of the 3D view.

### Adding a menu to the Quick menu

![Adding a menu to the Quick menu](/docs2/images/editors/dope-sheet/header/quick-menu/adding-a-menu-to-the-quick-menu.png)

It is also possible to add a menu to the Quick menu. For example the whole Add menu. The way is the same. Right click at it, and choose Add to Quick Favorites.

![Adding a menu to the Quick menu](/docs2/images/editors/dope-sheet/header/quick-menu/adding-a-menu-to-the-quick-menu-2.png)

### Order

You might notice that the add menu adds at the top of the menu, and not at the bottom as you would expect. First comes menus, then comes operators. And they get added in the order in which you add them.

Besides that, operators and menus gets added in the order that you add them. They cannot be sorted afterwards. So be careful how you add them. You can of course always remove operators and menus, and re-add them at the end of the list.

### Removing an operator from the Quick menu

> The **Quick Favorites** menu (Q) holds the tools and menus you add to it yourself. See **[Quick Favorites](../../../interface/floating-menus.md#quick-favorites)** in the Interface chapter.

### Context and mode dependent content

The quick favorites. menu exists in nearly all editors. But it is just in the 3D view available in the header. So that you know this functionality exists. In the other editors you call it with hotkey Q.

The content of the quick favorites. menu changes, dependent over which editor you are, and in what mode you are. When you add for example an operator from the image editor, then this operator just shows in the quick menu when you call the menu from the image editor. Same goes for the modes. Edit mode tools will just show in edit mode. And so on.

# View Menu

## Dopesheet Editor - View Menu

![Dopesheet Editor - View Menu](/docs2/images/editors/dope-sheet/header/view-menu/dopesheet-editor-view-menu.jpg)

The View menu contains all View related tools.

The content is for all modes the same.

### Channels List

![Channels List](/docs2/images/editors/dope-sheet/header/view-menu/channels-list.png)

Shows or hides the Channels list at the left in the viewport.

### Sidebar

![Sidebar](/docs2/images/editors/dope-sheet/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

### Adjust Last Operation - Dopesheet Editor - View Menu

Show the adjust last operation panel down left when you use a tool.

### Footer

![Footer](/docs2/images/editors/dope-sheet/header/view-menu/footer.png)

Reveals the footer.

### Set Preview Range

Rectangle select an area of the timeline that gets previewed. The playback now just happens in this marked area.

![Set Preview Range](/docs2/images/editors/dope-sheet/header/view-menu/set-preview-range.png)

![Set Preview Range](/docs2/images/editors/dope-sheet/header/view-menu/set-preview-range-2.png)

| Entry | What it does |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clear Preview Range | Clears an existing preview range. |
| Set Preview Range to selected | Sets the preview range to fit the first and last selected keyframe. |
| Frame Scene Range | With Use Preview Range off , reset the horizontal view to the current scene frame range. |
| Frame Preview Range | With Use Preview Range on , reset the horizontal view to the current preview frame range. |
| Zoom In | Zooms into the viewport. |
| Zoom Out | Zooms out of the viewport. |
| Zoom Border | Draws a rectangle and zooms then to fit the size of this rectangle. Zooming in is done with drawing the rectangle with left mouse button. Zooming out is done with drawing the rectangle with middle mouse button. |
| Frame All | Zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |
| Frame Selected | Centers the view at the currently selected keyframe(s). |
| Go to current Frame | Centers the view at the frame slider. |

### Pie menus

![Pie menus](/docs2/images/editors/dope-sheet/header/view-menu/pie-menus.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

### Area

![Area](/docs2/images/editors/dope-sheet/header/view-menu/area.png)

This menu contains general view functionality. And exists in most other editor types too.

| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |

#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/dope-sheet/header/view-menu/duplicate-area-into-new-window.png)

> **Duplicate Area into New Window** opens this editor in a floating window. See **[Floating editor windows](../../../interface/windows.md#floating-editor-windows)** in the Interface chapter.

| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Closes the area window. |

### Toggle Graph Editor

Switch to the Graph Editor.

![Toggle Graph Editor](/docs2/images/editors/dope-sheet/header/view-menu/toggle-graph-editor.png)

Note that this is a Blender relict. In Bforartists we already have a convenient top level UI menu entry to switch between the editors. We haven't removed this Blender entry for two reasons. It can be hotkeyed. And the entry shows that this Blender functionality exists.

# Select Menu

## Dopesheet Editor - Select Menu

![Dopesheet Editor - Select Menu](/docs2/images/editors/dope-sheet/header/select-menu/dopesheet-editor-select-menu.png)

The Select menu contains various tools to select elements.

The content is the same in all modes. With one exception. Grease Pencil mode is missing the More / Less menu items.

### All

Select everything.

### None

Select nothing.

### Invert

Invert the current selection.

### Box Select

Box select enters the Border Select mode. Select elements by dragging a rectangle around it. Just what's inside of the rectangle gets selected then. It adds to selection by default. To subtract from selection hold down Shift key. The selection gets applied when you release the mouse. You leave the mode automatically when you release the mouse.

### Box Select (Axis Range)

Box select enters the Border Select mode. Select elements by dragging a rectangle around it. And what's inside the horizontal range of the rectangle gets selected then. Even when the keyframes are outside of the rectangle. It adds to selection by default. To subtract from selection hold down Shift key. The selection gets applied when you release the mouse. You leave the mode automatically when you release the mouse.

### Circle Select

Circle select enters the Circle Select mode. This is a special select mode where you can select elements by moving with the mouse over it. It adds to selection by default. To subtract from selection hold down Shift key. To exit the Circle select click with the right mouse button. The pencil radius of the circle select tool can be adjusted with the scroll wheel.


### Lasso Select

![Lasso Select](/docs2/images/editors/dope-sheet/header/select-menu/lasso-select.png)

A sub menu with the available lasso select modes.

### Columns on Selected Keys

Select the keyframes in the columns of the currently selected keyframe.

### Columns on Current Frame

Select the keyframes in the columns of the current frame.

### Columns on Selected Markers

Select the keyframes in the columns of the selected markers.

### Between Selected Markers

Select the keyframes between the selected markers. You need to have markers in the view for this feature.

### Linked

Select all keyframes on the same channels as the keyframes you already selected.

### Type submenu

Select every keyframe of one kind at once, for example all **Breakdowns** or all **Extremes**. Handy when you mark your key poses with keyframe types and want to tweak just one group. The submenu lists Keyframe, Breakdown, Moving Hold, Extreme, Jitter and Generated.

> **Note:** **Linked** and **Type** used to be called Select Linked and Select by Type. They're shorter now because they already sit in the Select menu. Neither shows in Grease Pencil mode.

### Before Current Frame

Select the keyframes before the current frame.

### After Current Frame

Select the keyframes after the current frame.


### More/Less Sub-menu

![More/Less Sub-menu](/docs2/images/editors/dope-sheet/header/select-menu/more-less-sub-menu.png)

#### More

Grow the selection.

#### Less

Shrink the selection.


# Marker Menu

## Dopesheet Editor - Marker Menu

![Dopesheet Editor - Marker Menu](/docs2/images/editors/dope-sheet/header/marker-menu/dopesheet-editor-marker-menu.png)

Markers are visual landmarks. They can mark a start of a specific animation sequence, the end of a camera movement, and so on.

When you add one then a marker area appears at the bottom of the timeline.

Markers can be pulled around by clicking at them and dragging them left or right. The active marker is yellow.

By holding down shift you can select more than one marker.

| Entry | What it does |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Add Marker | Adds a marker at the current frame position |
| Duplicate Marker | Duplicates the selected marker(s). The duplicate(s) sticks at the mouse until you click to give it the target destination. |

### Duplicate Marker to Scene

![Duplicate Marker to Scene](/docs2/images/editors/dope-sheet/header/marker-menu/duplicate-marker-to-scene.png)

Duplicate markers to other scenes. A blend file can contain more than one scene. See Scene Properties in the Properties editor.

![Duplicate Marker to Scene](/docs2/images/editors/dope-sheet/header/marker-menu/duplicate-marker-to-scene-2.png)

### Delete Marker

Deletes the selected marker(s).

### Bind Camera to Markers

![Bind Camera to Markers](/docs2/images/editors/dope-sheet/header/marker-menu/bind-camera-to-markers.png)

Bind camera to markers turns an object into a camera object. This can be any object in the scene. Not just camera objects.

When the current frame position does not have a marker yet, then it creates a marker at the current frame position.

By binding different objects or cameras at different marker locations you can switch cameras automatically.

The marker with a bind camera attached will show a camera icon.

### Rename Marker

![Rename Marker](/docs2/images/editors/dope-sheet/header/marker-menu/rename-marker.png)

A menu will open up where you can rename the active marker.

| Entry | What it does |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grab/Move Marker | Hotkey only functionality! This menu item exists to show the hotkey to move the marker. |
| Select submenu | **All**: Select all markers. · **None**: Select nothing. · **Invert**: Invert the selection. · **Before Current Frame**: Select all markers before Current Frame. · **After Current Frame**: Select all markers after Current Frame. |
| Jump to Next Marker | Sets the frame position to the next marker. |
| Jump to Previous Marker | Sets the frame position to the previous marker. |

# Channel Menu

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

# Key Menu

## Dopesheet Editor - Key Menu

![Dopesheet Editor - Key Menu](/docs2/images/editors/dope-sheet/header/key-menu/dopesheet-editor-key-menu.png)

![Dopesheet Editor - Key Menu](/docs2/images/editors/dope-sheet/header/key-menu/dopesheet-editor-key-menu-2.png)

The key menu contains functionality to manage the keyframes.

The menu exist in all modes. In Grease Pencil mode it contains not so much functionality.

The grease pencil object is a special object in this regards. It can have keyframes at an object level. And keyframes at a stroke level, which the grease pencil mode is meant for.

### Transform

![Transform](/docs2/images/editors/dope-sheet/header/key-menu/transform.png)

| Entry | What it does |
| --------- | -------------------------------------------------------------------------------- |
| Grab/Move | Moves the selected keyframe(s). |
| Extend | Moves the last keyframes of the selection. |
| Slide | Slides a selected keyframe between two other keyframes. |
| Scale | Scales the selected keyframes. You need to have more than one keyframe selected. |

#### Adjust Last Operation - Transform

![Last Operator Transform](/docs2/images/editors/dope-sheet/header/key-menu/last-operator-transform.png)

The last operator is nearly equal for the transform operations above.

##### Values

The transform values.

##### Axis

![Axis](/docs2/images/editors/dope-sheet/header/key-menu/axis.png)

Which axis is up.

##### Orientation

![Orientation](/docs2/images/editors/dope-sheet/header/key-menu/orientation.png)

Choose the orientation in which the transform should happen.

##### Mirror Editing

Just with Grab/Move. Allow mirror edit the transform.

##### Proportional editing

![Proportional editing](/docs2/images/editors/dope-sheet/header/key-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.

| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |

### Snap

![Snap](/docs2/images/editors/dope-sheet/header/key-menu/snap.png)

Snaps the selected keyframes by the chosen method.

### Mirror

![Mirror](/docs2/images/editors/dope-sheet/header/key-menu/mirror.png)

Flips the selected keyframes over the current frame position.

### Insert Keyframes

![Insert Keyframes](/docs2/images/editors/dope-sheet/header/key-menu/insert-keyframes.png)

Inserts a keyframe at the current frame. The submenu sets which channels get it.

| Entry | What it does |
| ---------------------- | ---------------------------------------------------- |
| All Channels | Inserts a keyframe in every channel. |
| Only Selected Channels | Inserts a keyframe in the selected channels only. |
| In Active Group | Inserts a keyframe in the channels of the active group. |

### Jump, Copy and Paste

| Entry | What it does |
| ----------------- | ---------------------------------------------------------------------------------- |
| Jump to Selected | Sets the frame marker at the average position of the currently selected keyframes. |
| Copy Keyframes | Copy selected keyframes. |
| Paste Keyframes / Flipped | Pastes copied keyframes. |
| Paste Flipped | Pastes copied keyframes, but flipped. |
| Duplicate | Duplicate selected keyframes. |

To delete the selected keyframes, press `Delete`.

### Delete Breakdown Frames

Remove breakdown frames generated by interpolating between two grease pencil frames.

> **Note:** Grease Pencil operator object only.

#### Workflow

![Workflow](/docs2/images/editors/dope-sheet/header/key-menu/workflow.png)

Grease Pencil in Draw mode. Generate two keyframes. Go to the Draw menu. Choose Interpolate Sequence.

Delete Breakdown Frames now becomes active, and you can delete the interpolated keyframes if you need.

| Entry | What it does |
| --------------- | ----------------------------------------------------------------------------------------- |
| Clean Keyframes | Simplify FCurces by deleting keyframes that are close to each other in all channels |
| Clean Channels | Simplify FCurces by deleting keyframes that are close to each other in selected channels. |

### Bake Keyframes

![Bake Keyframes](/docs2/images/editors/dope-sheet/header/key-menu/bake-keyframes.png)

Adds keyframes at every unit between the selected keyframes.

# Action Menu

## Dopesheet Editor - Key Menu

![Dopesheet Editor - Key Menu](/docs2/images/editors/dope-sheet/header/action-menu/dopesheet-editor-key-menu.png)

Just in Action Editor mode.

| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Merge Animation | Merge the animation of the selected objects into the action of the active object. Actions are not deleted by this. But might end up with zero users. |
| Separate Slots | Move all sorts of the action on the active object into newly created, separate actions. All users of those slots will be reassigned to the new actions. The current action won't be deleted. But will be empty. And might end up with zero users. |

### Replace Action

![Replace Action](/docs2/images/editors/dope-sheet/header/action-menu/replace-action.png)

Swap all users of one action to another one. The normal action slot assignment rules apply. This ignores the NLA and Action Constraints

### Replace Action New

Swap all users of one action to a new action. This ignores the NLA and Action Constraints

### Move Slots to new Action

![Move Slots to new Action](/docs2/images/editors/dope-sheet/header/action-menu/move-slots-to-new-action.jpg)

Move the selected slots into a newly created action.
