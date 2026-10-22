---
id: editors.image-editor.header.view-menu
title: View menu
section: editors
path:
  - Editors
  - Image Editor
  - Header
  - View menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 8.1.3 Editors - Image Editor - Header - View menu.odt
---
## Image Editor - View Menu

The View menu contains all View related tools.

It is available in all sub modes. With a render result the view image shows a different content. And in mask mode it shows one more item. Set 2D cursor.

![Image Editor - View Menu](/docs2/images/editors/image-editor/header/view-menu/image-editor-view-menu.png)

![Image Editor - View Menu](/docs2/images/editors/image-editor/header/view-menu/image-editor-view-menu-2.png)

![Image Editor - View Menu](/docs2/images/editors/image-editor/header/view-menu/image-editor-view-menu-3.png)

![Image Editor - View Menu](/docs2/images/editors/image-editor/header/view-menu/image-editor-view-menu-4.png)

![Image Editor - View Menu](/docs2/images/editors/image-editor/header/view-menu/image-editor-view-menu-5.png)

### Toolbar

![Toolbar](/docs2/images/editors/image-editor/header/view-menu/toolbar.png)

Shows or hides the toolbar at the left.

### Sidebar

![Sidebar](/docs2/images/editors/image-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

### Tool Settings

![Tool Settings](/docs2/images/editors/image-editor/header/view-menu/tool-settings.png)

Shows or hides the tool settings above the header in the 3D view.

### Asset Shelf

Not yet. The asset shelf is planned but not implemented yet.

### Adjust Last Operation

![Adjust Last Operation](/docs2/images/editors/image-editor/header/view-menu/adjust-last-operation.png)

Shows or hides the Adjust Last Operation panel down left.

Note that the Adjust Last Operation menu item in the Edit menu in the main header and the Last button in the toolbar are not related and not functional with this last operator panel. It is an independent element.

### Legacy submenu

![Legacy submenu](/docs2/images/editors/image-editor/header/view-menu/legacy-submenu.png)

This menu contains legay operators that are now available in the tool shelf.

#### Set 2D Cursor

Mask mode only. Set the 2D cursor position. Hotkey only tool! Please use the hotkey!

### Annotations (Legacy) submenu

![Annotations (Legacy) submenu](/docs2/images/editors/image-editor/header/view-menu/annotations-legacy-submenu.png)

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
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Zoom In | Zooms into the viewport. |
| Zoom Out | Zooms out of the viewport. |
| Zoom Border | Draws a rectangle and zooms then to fit the size of this rectangle. Zooming in is done with drawing the rectangle with left mouse button. Zooming out is done with drawing the rectangle with middle mouse button. |


### Zoom submenu

![Zoom submenu](/docs2/images/editors/image-editor/header/view-menu/zoom-submenu.png)

A sub menu where you can choose between predefined zoom factors.


| Entry | What it does |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View Selected | Mask menu. View all selected UV’s. |
| Frame All | Zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |
| View Fit | Zooms out or in to fit the image to the viewport. |
| Center View to Cursor | Center the view to the cursor in the middle of the view. |
| Render Region | Render result only. Allows you to draw a rectangle. And when you re-render the image, just the content in this rectangle region gets rendered. This tool does, different from the 3d view, not draw a permanent red rectangle to define the render region area. You will see what you have chosen when you render the image. |
| Clear Render Region | Render result only. Removes any existing render region rectangle. |
| Render Slot Cycle Next | Render result only. Cycle through the Render slots. |
| Render Slot Cycle Previous | Render result only. Cycle through the Render slots. |


### Area submenu

![Area submenu](/docs2/images/editors/image-editor/header/view-menu/area-submenu.png)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/image-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI any more.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Closes the area window. |


### Pie menus submenu

![Pie menus submenu](/docs2/images/editors/image-editor/header/view-menu/pie-menus-submenu.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

