---
id: editors.geometry-node-editor.header.view-menu
title: View Menu
section: editors
path:
  - Editors
  - Geometry Node Editor
  - Header
  - View Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 12.1.3 Editors - Geometry Nodes Editor - Header - View Menu.odt
---
## View Menu

![View Menu](/docs2/images/editors/geometry-node-editor/header/view-menu/view-menu.png)

The View menu contains all View related tools.

The content is the same in all sub modes.

### Toolbar

![Toolbar](/docs2/images/editors/geometry-node-editor/header/view-menu/toolbar.png)

Shows or hides the toolbar at the left.

### Sidebar

![Sidebar](/docs2/images/editors/geometry-node-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the Geometry Nodes editor.

### Asset Shelf

![Asset Shelf](/docs2/images/editors/geometry-node-editor/header/view-menu/asset-shelf.png)

Shows or hides the Asset Shelf to the bottom of the Geometry Nodes Editor.

### Annotations (Legacy)

This group of operators is useful to take notes without changing tool-shelf operators. These notes can be colored in the View tab of the Property Shelf. Each layer is a single color. You can also animate the notes with keyframes, editable in the dopesheet.

> **Note:** These are legacy operators, meaning they are equally available in the Toolshelf as a modal operator.


| Entry | What it does |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Draw Annotation | Starts the annotation free hand draw tool in the editor. |
| Draw Line Annotation | Starts the annotation line draw tool to draw straight lines in the editor. |
| Draw Polyline Annotation | Starts the annotation Polyline draw tool in the editor which allows to draw multiple connected straight lines in the editor. |
| Erase Annotation | Starts the annotation erase tool in the editor which erases any strokes in the editor. |
| Add Annotation Layer | Starts a new annotation layer. |
| Erase Annotation Active Keyframe | Erases the active keyframe of the annotation. |


| Entry | What it does |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Link to Output | Creates a connection to the Output Node. ***Note:** This operator only works under the mouse cursor and is shown in this menu for discoverability purposes only.* |
| Link to Viewer | Creates a temporary connection to the Viewer Node, allowing to quickly preview the output of any node within the shader editor by clicking on it. **Note:** *This operator only works under the mouse cursor and is shown in this menu for discoverability purposes only.* |
| Zoom In | Zooms into the viewport. |
| Zoom Out | Zooms out of the viewport. |
| Zoom Border | Draws a rectangle and zooms then to fit the size of this rectangle. Zooming in is done with drawing the rectangle with left mouse button. Zooming out is done with drawing the rectangle with middle mouse button. |
| Frame Selected | Zooms to the selection. |
| Frame All | View all zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |


### Pie menus

![Pie menus](/docs2/images/editors/geometry-node-editor/header/view-menu/pie-menus.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

### Area

![Area](/docs2/images/editors/geometry-node-editor/header/view-menu/area.png)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/geometry-node-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI any more.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Closes the area window. |


