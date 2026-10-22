---
id: editors.graph-editor.header.view-menu
title: View Menu
section: editors
path:
  - Editors
  - Graph Editor
  - Header
  - View Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 18.1.3 Editors - Graph Editor - View Menu.odt
---
## Graph Editor - View Menu

![Graph Editor - View Menu](/docs2/images/editors/graph-editor/header/view-menu/graph-editor-view-menu.png)

The View menu contains all View related tools.

The content is for all modes the same.

### Channels

![Channels](/docs2/images/editors/graph-editor/header/view-menu/channels.png)

Shows or hides the Channels list at the left in the viewport.

### Sidebar

![Sidebar](/docs2/images/editors/graph-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

### Adjust last Operation

![Adjust last Operation](/docs2/images/editors/graph-editor/header/view-menu/adjust-last-operation.png)

Show the Adjust Last Operation panel down left when you perform a tool.

### Playback Controls

![Playback Controls](/docs2/images/editors/graph-editor/header/view-menu/playback-controls.png)

Reveals the footer.

### Set Preview Range

![Set Preview Range](/docs2/images/editors/graph-editor/header/view-menu/set-preview-range.png)

![Set Preview Range](/docs2/images/editors/graph-editor/header/view-menu/set-preview-range-2.png)

Rectangle select an area of the timeline that gets previewed. The playback now just happens in this marked area.


| Entry | What it does |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clear Preview Range | Clears an existing preview range. |
| Set Preview Range to selected | Sets the preview range to fit the first and last selected keyframe. |
| Frame Scene Range | With Use Preview Range off , reset the horizontal view to the current scene frame range. |
| Frame Preview Range | With Use Preview Range on , reset the horizontal view to the current preview frame range. |
| Zoom In | Zooms into the viewport. |
| Zoom Out | Zooms out of the viewport. |
| Zoom to Border | Draws a rectangle and zooms then to fit the size of this rectangle. Zooming in is done with drawing the rectangle with left mouse button. Zooming out is done with drawing the rectangle with middle mouse button. |
| Frame All | Zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |
| Frame Selected | Centers the view at the currently selected keyframe(s). |
| Go to current Frame | Centers the view at the frame slider. |


### Area submenu

![Area submenu](/docs2/images/editors/graph-editor/header/view-menu/area-submenu.png)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/graph-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Closes the area window. |


### Pie menus

![Pie menus](/docs2/images/editors/graph-editor/header/view-menu/pie-menus.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

### Toggle Dope Sheet

Switch to the Dope Sheet Editor.

![Toggle Dope Sheet](/docs2/images/editors/graph-editor/header/view-menu/toggle-dope-sheet.png)

Note that this is a Blender relict. In Bforartists we already have a convenient top level UI menu entry to switch between the editors. We haven't removed this Blender entry for two reasons. It can be hotkeyed. And the entry shows that this Blender functionality exists.

