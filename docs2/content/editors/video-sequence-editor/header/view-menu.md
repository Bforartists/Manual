---
id: editors.video-sequence-editor.header.view-menu
title: View Menu
section: editors
path:
  - Editors
  - Video Sequence Editor
  - Header
  - View Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 14.1.3 Editors - Video Sequence Editor - Header - View Menu.odt
---
## Type of Sequencer View

![Type of Sequencer View](/docs2/images/editors/video-sequence-editor/type-of-sequencer-view.png)

The Video Sequence Editor is two editors in one. The Preview sequencer view is a preview window. Here plays the video. The Sequencer sequencer view is the view that contains the video and audio strips.

The view menu for Sequencer/Preview contains the same menu items than in the other two views. So we won't explicitely list it here again.

## View Menu in Preview window

![View Menu in Preview window](/docs2/images/editors/video-sequence-editor/header/view-menu/view-menu-in-preview-window.png)

The View menu contains all View related tools.

### Toolbar

![Toolbar](/docs2/images/editors/video-sequence-editor/header/view-menu/toolbar.png)

Shows or hides the toolbar at the left.

### Sidebar

![Sidebar](/docs2/images/editors/video-sequence-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.


| Entry | What it does |
| ----------------- | --------------------------------------------------- |
| Tool Settings | Show or hide the tool settings at the top. |
| Tool shelf tabs | Show or hide the tool shelf tabs in the tool shelf. |
| Playback Controls | Reveals the footer with the playback controls. |


### Annotations (Legacy) submenu

![Annotations (Legacy) submenu](/docs2/images/editors/video-sequence-editor/header/view-menu/annotations-legacy-submenu.png)

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
| ----------- | ---------------------------------------------------------------------------------------------------------------------- |
| Zoom In | Zooms in. |
| Zoom Out | Zooms out. |
| Zoom Border | Draw a rectangle around the target area to zoom in or out. Left mouse button zoooms in. Middle mouse button zooms out. |


### Zoom

![Zoom](/docs2/images/editors/video-sequence-editor/header/view-menu/zoom.png)

A set of predefined zoom factors.


| Entry | What it does |
| --------------------- | ----------------------------------------------------------------- |
| Fit Preview in Window | Zooms in or out until the video displays fitting in the viewport. |
| Frame Selected | Centers the selection and zooms to fit. |


### Proxy

![Proxy](/docs2/images/editors/video-sequence-editor/header/view-menu/proxy.png)

Proxy works just with movie or image strips. What it does is to create a smaller set of preview images. This speeds up the calculation while you are at editing the video. The final result uses the final images again then.

#### Setup

![Setup](/docs2/images/editors/video-sequence-editor/header/view-menu/setup.png)

Calls a panel where you can choose the resolution of the proxy images. Clicking OK starts the creation process.

#### Rebuild

Recreates the proxy images

#### Scene Render Size

![Scene Render Size](/docs2/images/editors/video-sequence-editor/header/view-menu/scene-render-size.png)

What render size the display should choose.


| Entry | What it does |
| ------------------------- | ---------------------------------------------------------------- |
| Refresh All | Refresh the sequence editor. |
| Sequence render Image | Renders an image of the current frame. |
| Sequence render Animation | Renders the animation in the preview range. |
| Toggle Sequencer/Preview | Toggles the type of sequencer view between Sequencer or Preview. |


### Pie Menu

![Pie Menu](/docs2/images/editors/video-sequence-editor/header/view-menu/pie-menu.png)

The available pie menus for the sequencer in View mode.

### Area

![Area](/docs2/images/editors/video-sequence-editor/header/view-menu/area.png)

This menu contains general view functionality. And exists in most other editor types too.

#### Toggle Quad view

![Toggle Quad view](/docs2/images/editors/video-sequence-editor/header/view-menu/toggle-quad-view.png)

Displays the 3D View divided into four split screen parts. Note that the orthographic views cannot be switched in this mode. They remain orthographic, you cannot rotate them.

To return to single view reuse the menu item in the View menu.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/video-sequence-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space bar. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space bar. |
| Close Area | Closes the area window. |


## View Menu in Sequencer window

![View Menu in Sequencer window](/docs2/images/editors/video-sequence-editor/header/view-menu/view-menu-in-sequencer-window.png)

The View menu contains all View related tools.

### Toolbar

![Toolbar](/docs2/images/editors/video-sequence-editor/header/view-menu/toolbar-2.png)

Shows or hides the toolbar at the left.

### Sidebar

![Sidebar](/docs2/images/editors/video-sequence-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

### Tool Settings

Show or hide the tool settings at the top.

### Adjust Last Operation

![Adjust Last Operation](/docs2/images/editors/video-sequence-editor/header/view-menu/adjust-last-operation.png)

Displays the Adjust last operation panel down left.


| Entry | What it does |
| --------------- | -------------------------------------------------------------- |
| Channels | Display the channels in front of the timeline |
| Tool Shelf Tabs | Show or hide the tool shelf tabs in the tool shelf. |
| Footer | Shows the footer. |
| Zoom In | Zooms in. |
| Zoom Out | Zooms out. |
| Zoom Border | Zooms to the selection. |
| Frame all | Zooms in or out to display all elements fitting into the view. |


### Frame Scene Range / Frame Preview Range

![Frame Scene Range / Frame Preview Range](/docs2/images/editors/video-sequence-editor/header/view-menu/frame-scene-range-frame-preview-range.png)

![Frame Scene Range / Frame Preview Range](/docs2/images/editors/video-sequence-editor/header/view-menu/frame-scene-range-frame-preview-range-2.png)

This menu item changes the name and the icon, dependant of if the Use Preview range is activated. Which can be done besides the play elements in the Timeline editor or in the footer.

![Frame Scene Range / Frame Preview Range](/docs2/images/editors/video-sequence-editor/header/view-menu/frame-scene-range-frame-preview-range-3.png)

Resize the horizontal view to the current scene or preview frame range.


| Entry | What it does |
| ------------------------- | -------------------------------------------------------------------------------- |
| Go to current frame | Centers the view at the current frame. |
| Frame selected | Zooms in or out to display the currently selected element fitting into the view. |
| Refresh all | Refreshes the sequence editor. |
| Sequence render Image | Renders an image of the current frame. |
| Sequence render Animation | Renders the animation in the preview range. |
| Toggle Sequencer/Preview | Toggles the type of sequencer view between Sequencer or Preview. |


### Pie Menu

![Pie Menu](/docs2/images/editors/video-sequence-editor/header/view-menu/pie-menu.png)

The available pie menus for the sequencer in Sequencer mode.

### Area

![Area](/docs2/images/editors/video-sequence-editor/header/view-menu/area.png)

This menu contains general view functionality. And exists in most other editor types too.

#### Toggle Quad view

![Toggle Quad view](/docs2/images/editors/video-sequence-editor/header/view-menu/toggle-quad-view.png)

Displays the 3D View divided into four split screen parts. Note that the orthographic views cannot be switched in this mode. They remain orthographic, you cannot rotate them.

To return to single view reuse the menu item in the View menu.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/video-sequence-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space bar. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space bar. |
| Close Area | Closes the area window. |


