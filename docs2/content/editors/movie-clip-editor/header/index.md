---
id: editors.movie-clip-editor.header
title: Header
section: editors
path:
  - Editors
  - Movie Clip Editor
  - Header
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 15.1 Editors - Movie Clip Editor - Header.odt
replaces:
  - editors.movie-clip-editor.header.header-tools-and-options
  - editors.movie-clip-editor.header.quick-menu
  - editors.movie-clip-editor.header.view-menu
  - editors.movie-clip-editor.header.select-menu
  - editors.movie-clip-editor.header.tracking-mode-clip-submode-clip-menu
  - editors.movie-clip-editor.header.tracking-mode-clip-submode-track-menu
  - editors.movie-clip-editor.header.tracking-mode-graph-submode-graph-menu
  - editors.movie-clip-editor.header.mask-mode-clip-menu
  - editors.movie-clip-editor.header.mask-mode-add-menu
  - editors.movie-clip-editor.header.mask-mode-mask-menu
order: 10
---
## Movie Clip Editor - Header

The Header contains various menus, navigation elements, settings and tools for the viewport.

The header is divided into two areas. Left menus. Right settings.

![Movie Clip Editor - Header](/docs2/images/editors/movie-clip-editor/header/movie-clip-editor-header.png)

The Movie Clip Editor is three editors in one. And the Clip editor in mask mode looks also different. So we need to explain the content for all three editor types plus the sub mode mask.

![Movie Clip Editor - Header](/docs2/images/editors/movie-clip-editor/header/movie-clip-editor-header-2.png)

## Header right click menus

The general right click menu functionality is explained in chapter 6 Editors introduction.

## Editortype Menu

![Editortype Menu](/docs2/images/editors/movie-clip-editor/header/editortype-menu.png)

Bforartists is made of several editor types. Headers can display a menu where you can switch to other editor types.

This menu is hidden by default. It is meant to edit the layouts, and should not be necessary for regular work. You can reveal it in the header right click menu.

![Editortype Menu](/docs2/images/editors/movie-clip-editor/header/editortype-menu-2.png)

# Header Tools and Options

### Movie Clip Editor - Header

The Movie Clip Editor has two modes, and is three editors in one. So we have to explain the single header tools and options at a one by one base.

![Movie Clip Editor - Header](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-editor-header.png)

### Tracking mode - Clip submode

![Tracking mode - Clip submode](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/tracking-mode-clip-submode.png)

#### Movie Clip property

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property.png)

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property-2.png)

Available in Tracking in Clip mode and Mask mode.

This property contains the list of loaded movie clips. When no movie clip is loaded or active, then it displays the Open Buttons. When a movie clip is loaded and active, then it displays the name of the currently active movie clip.

From left to right ...

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property-3.png)


| Entry | What it does |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List of clips in the scene | This is a list of the movie clips in the scene. Allows you to witch to other images. · **Search form**: Search for specific clips. |
| Clip Edit Box | The name of the currently selected movie clip. You can rename the movie clip here too. |
| Number of Fake Users | In case this file has a fake user assigned, then this number displays the number of fake users. |
| Fake User | With this button you assign a fake user to this selected image. Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behavior. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene. |
| Open | Open a new movie clip. |


#### Remove

Removes the movie clip. Note that it will not be removed when it has a fake user assigned. Then the clip becomes simply inactive. You can still use it from the list again.

#### Pivot Point

![Pivot Point](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/pivot-point.png)

Adjust the pivot point for transform operations. The names should be self explaining.

#### Solve Error

Read only. The solve error for the current tracking.

#### Toggle Lock Selection

![Toggle Lock Selection](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/toggle-lock-selection.png)

![Toggle Lock Selection](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/toggle-lock-selection-2.png)

With lock to selection disabled the viewport stands still and the markers moves. With lock to selection enabled the view is centered at the current selected marker, and the video moves around.

Available in Tracking in Clip mode and Mask mode.

#### Clip Display

![Clip Display](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/clip-display.png)

Display options for the tracking footage.


| Entry | What it does |
| ------------------ | ----------------------------------------------------------------------- |
| R G B | Display the red green and blue channels of the footage |
| BW | Display the footage in black and white. |
| Mute Footage | Hide the footage. |
| Render Undistorted | Render Preview undistorted. |
| Show Metadata | Shows the metadata of the clip if available. |
| Show Stable | Show stable footage in editor. Stabilization needs to be enabled. |
| Grid | Displays a red grid over the footage that displays the lens distortion. |
| Aspect Ratio X Y | The aspect ratio to display the footage. |


### Tracking mode - Graph submode

![Tracking mode - Graph submode](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/tracking-mode-graph-submode.png)

Tools to refine and modify the markers.

#### Refine Markers Backwards

![Refine Markers Backwards](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/refine-markers-backwards.png)

Refine selected markers position by running the tracker from tracks reference to current frame.


| Entry | What it does |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| Clear Track Path Backwards | Clear tracks before the current position. |
| Track Markers Backwards | Track selected markers backwards. |
| Track Markers Sequence Backwards | Track selected marker sequence backwards. |
| Track Markers Sequence Forwards | Track selected marker sequence forwards. |
| Track Markers Forwards | Track selected markers forwards. |
| Clear Track Path Forwards | Clear tracks after the current position. |
| Refine Markers Forwards | Refine selected markers position by running the tracker from tracks reference to current frame. |
| Only selected | Only display channels relating to the current objects and data. |
| Display Hidden | Display also channels from objects/bones that are not visible. |
| Show Frames | Show curve for per frame average error. Camera motion should be solved first. |
| Show Track Motion | Display the speed curves for the selected tracks. Red is X direction. Green is Y direction. |
| Show Tracks Error | Display the reprojection error curve for the selected tracks. |
| Show Gizmo | Display gizmos. |


#### Gizmos

![Gizmos](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/gizmos.png)

##### Viewport Gizmos

###### Navigate

Show the navigate viewport gizmos.

### Tracking mode - Dope Sheet submode

![Tracking mode - Dope Sheet submode](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/tracking-mode-dope-sheet-submode.png)

Tools to refine and modify the markers.

#### Refine Markers Backwards

![Refine Markers Backwards](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/refine-markers-backwards.png)

Refine selected markers position by running the tracker from tracks reference to current frame.


| Entry | What it does |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| Clear Track Path Backwards | Clear tracks before the current position. |
| Track Markers Backwards | Track selected markers backwards. |
| Track Markers Sequence Backwards | Track selected marker sequence backwards. |
| Track Markers Sequence Forwards | Track selected marker sequence forwards. |
| Track Markers Forwards | Track selected markers forwards. |
| Clear Track Path Forwards | Clear tracks after the current position. |
| Refine Markers Forwards | Refine selected markers position by running the tracker from tracks reference to current frame. |
| Only selected | Only display channels relating to the current objects and data. |
| Display Hidden | Display also channels from objects/bones that are not visible. |


#### Dope Sheet Sort Field

![Dope Sheet Sort Field](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/dope-sheet-sort-field.png)

The method to sort the channels in dope sheet view.

##### Invert Dope Sheet Sort

Invert the dope sheet sorting.

#### Options panel

![Options panel](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/options-panel.png)

##### Show Seconds

Option. Display the timeline numbering in seconds instead of frames.

![Show Seconds](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/show-seconds.png)

##### Sync Visible Range

Option. Synchronize the visible timeline range with other time based editors.

#### Gizmos

![Gizmos](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/gizmos.png)

##### Viewport Gizmos

###### Navigate

Show the navigate viewport gizmos.

### Mask mode

![Mask mode](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/mask-mode.png)

#### Movie Clip property

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property.png)

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property-2.png)

Available in Tracking in Clip mode and Mask mode.

This property contains the list of loaded movie clips. When no movie clip is loaded or active, then it displays the Open Buttons. When a movie clip is loaded and active, then it displays the name of the currently active movie clip.

From left to right ...

![Movie Clip property](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/movie-clip-property-3.png)


| Entry | What it does |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List of clips in the scene | This is a list of the movie clips in the scene. Allows you to witch to other images. · **Search form**: Search for specific clips. |
| Clip Edit Box | The name of the currently selected movie clip. You can rename the movie clip here too. |
| Number of Fake Users | In case this file has a fake user assigned, then this number displays the number of fake users. |
| Fake User | With this button you assign a fake user to this selected image. Data, like images, that is not longer linked to anything else gets removed when you save and reload a scene. Bforartists has the concept of fake users to go around this behavior. An image with a fake user is in fact linked to something. And so it is not lost when you save and reload the scene. |
| Open | Open a new movie clip. |


#### Remove

Removes the movie clip. Note that it will not be removed when it has a fake user assigned. Then the clip becomes simply inactive. You can still use it from the list again.

![Remove](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/remove.png)

#### Mask Property

These are display options for mask overlays.

##### Mask Display

###### Spline

![Spline](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/spline.png)

Display spline overlays.


| Entry | What it does |
| ------------ | ------------------------------------------------------------------ |
| Edge Display | Changes the spline overlay to outline, dash, black or white edges. |
| Overlay | Displays an overlay overlays. |


###### Overlay Mode

![Overlay Mode](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/overlay-mode.png)

Show combined color channels or alpha channel. When using combined, the Blending Factor slider can be changed.

#### Pivot Point

![Pivot Point](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/pivot-point.png)

Adjust the pivot point for transform operations. The names should be self explaining.

#### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/proportional-editing.png)

Enables proportional editing.

Proportional Editing is a way of transforming selected elements (such as vertices, or in this case the handlers for the mask spline curves) while having that transformation affect other nearby elements with a falloff. For example, moving a single vertex will move unselected vertices within a given range. And the falloff means that selected vertices that are closer to the selected vertex will move more than those farther from it.

##### Settings

Choose between different falloff methods for the proportional editing. The settings are hidden when you have proportional editing off.

#### Toggle Lock Selection

Toggle Lock Selection of the current clip editor

#### Clip Display

![Clip Display](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/clip-display.png)

Display options for the tracking footage.


| Entry | What it does |
| ------------------ | ----------------------------------------------------------------------- |
| R G B | Display the red green and blue channels of the footage |
| BW | Display the footage in black and white. |
| Mute Footage | Hide the footage. |
| Render Undistorted | Render Preview undistorted. |
| Show Metadata | Shows the metadata of the clip if available. |
| Show Stable | Show stable footage in editor. Stabilization needs to be enabled. |
| Grid | Displays a red grid over the footage that displays the lens distortion. |
| Aspect Ratio X Y | The aspect ratio to display the footage. |


#### Gizmos

![Gizmos](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/gizmos.png)

##### Viewport Gizmos

###### Navigate

Show the navigate viewport gizmos.

#### Show Overlays

![Show Overlays](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/show-overlays.png)

##### Viewport Overlays

###### Guides


| Entry | What it does |
| --------------- | ---------------------------------- |
| Distortion Grid | Show grid showing lens distortion. |
| Cursor | Display 2d cursor. |
| Annotations | Display annotations. |


###### Mask Display

![Mask Display](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/mask-display.jpg)

###### Spline

**Edge Display type**

![Edge Display type](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/edge-display-type.png)

How to display the spline.

###### Overlay

![Overlay](/docs2/images/editors/movie-clip-editor/header/header-tools-and-options/overlay.png)


| Entry | What it does |
| ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Alpha Channel | Show the alpha channel of the mask |
| Combined | Combine space background image with the mask · **Blending Factor**: The blending factor between mask and space background. |

# Quick Menu

### Quick Menu

![Quick Menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/quick-menu.png)

The quick menu, or in long Quick Favorites menu, is a menu that can be customized to your needs. Here you can add operators for quick access.

It is located in the header. But it can be called by hotkey Q directly under the mouse. This hotkey works in other editors too.

When the menu is empty, then you will see the message "No Menu Items found". This means that you first have to add some tools to the menu. It is a user configurable menu.

Note that added operators in this menu does not have icons. Just text.

#### Adding an operator to the Quick menu

![Adding an operator to the Quick menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/adding-an-operator-to-the-quick-menu.png)

Open the panel or the menu where your operator is that you want to add.

Let's add the open command from the File menu. Open the File menu, right click at open, and choose Add to Quick Favorites.

Do the same with Save As. We should now have two new menu items in the Quick menu, which you can use now.

![Adding an operator to the Quick menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/adding-an-operator-to-the-quick-menu-2.png)

As a rule of thumb, when the right click menu has an Add to Quick Favorites, then you can add it to the quick menu.

Note that you can also add operators from the tool shelf at the left. And also operators from other editor types. Some other editors have their own quick menu though. The Image Editor for example. These operators gets added in the quick menu of the image editor then. And does not show in the quick menu in the header of the 3D view.

#### Adding a menu to the Quick menu

![Adding a menu to the Quick menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/adding-a-menu-to-the-quick-menu.png)

It is also possible to add a menu to the Quick menu. For example the whole Add menu. The way is the same. Right click at it, and choose Add to Quick Favorites.

![Adding a menu to the Quick menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/adding-a-menu-to-the-quick-menu-2.png)

#### Order

You might notice that the add menu adds at the top of the menu, and not at the bottom as you would expect. First comes menus, then comes operators. And they get added in the order in which you add them.

Besides that, operators and menus gets added in the order that you add them. They cannot be sorted afterwards. So be careful how you add them. You can of course always remove operators and menus, and re-add them at the end of the list.

#### Removing an operator from the Quick menu

![Removing an operator from the Quick menu](/docs2/images/editors/movie-clip-editor/header/quick-menu/removing-an-operator-from-the-quick-menu.png)

Removing is as simple as adding. Right click at the operators in the Quick menu, and choose Remove from Quick favorites.

#### Context and mode dependent content

The quick favorites. menu exists in nearly all editors. But it is just in the 3D view available in the header. So that you know this functionality exists. In the other editors you call it with hotkey Q.

The content of the quick favorites. menu changes, dependent over which editor you are, and in what mode you are. When you add for example an operator from the image editor, then this operator just shows in the quick menu when you call the menu from the image editor. Same goes for the modes. Edit mode tools will just show in edit mode. And so on.

# View Menu

### Movie Clip Editor Modes

The Movie Clip Editor is three editors in one. And the Clip editor in mask mode looks also different. So we need to explain the content for all three editor types plus the Mask mode.

![Movie Clip Editor Modes](/docs2/images/editors/movie-clip-editor/header/movie-clip-editor-header-2.png)

### View Menu in Tracking mode in Clip sub mode

![View Menu in Tracking mode in Clip sub mode](/docs2/images/editors/movie-clip-editor/header/view-menu/view-menu-in-tracking-mode-in-clip-sub-mode.png)

The View menu contains all View related tools.

#### Toolbar

![Toolbar](/docs2/images/editors/movie-clip-editor/header/view-menu/toolbar.png)

Shows or hides the toolbar at the left.

#### Sidebar

![Sidebar](/docs2/images/editors/movie-clip-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

#### Adjust Last Operation

![Adjust Last Operation](/docs2/images/editors/movie-clip-editor/header/view-menu/adjust-last-operation.png)

Shows the adjust last operation panel down left.


| Entry | What it does |
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| Frame Selected | Zooms to the selection. |
| View All | View all zooms in or out in the viewport until all selected objects are displayed fitting in the viewport. |
| View Fit | View all zooms in or out in the viewport to fit the current selection into the viewport. |
| Center View to Cursor | Center Cursor centers the view to the 2D cursor. |


#### Annotations (Legacy) submenu

![Annotations (Legacy) submenu](/docs2/images/editors/movie-clip-editor/header/view-menu/annotations-legacy-submenu.png)

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
| --------------------- | ------------------------------------------------------------------- |
| Frame Selected | Centers the view at the current frame(s). |
| Frame All | Views all content, zoomed in to fit into the viewport. |
| View Fit | View whole image with markers. |
| Center View to Cursor | Center the view so that the 2d cursor is in the middle of the view. |
| Zoom In | Zooms into the view. |


#### Zoom Out

![Zoom Out](/docs2/images/editors/movie-clip-editor/header/view-menu/zoom-out.png)

Zooms out of the view.

#### Zoom submenu

A set of predefined zoom factors.

#### Pie menus

![Pie menus](/docs2/images/editors/movie-clip-editor/header/view-menu/pie-menus.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

#### Area

![Area](/docs2/images/editors/movie-clip-editor/header/view-menu/area.jpg)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


##### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/movie-clip-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Close the area window. |


### View Menu in in Tracking mode in Graph sub mode

![View Menu in in Tracking mode in Graph sub mode](/docs2/images/editors/movie-clip-editor/header/view-menu/view-menu-in-in-tracking-mode-in-graph-sub-mode.png)

The View menu contains all View related tools.


| Entry | What it does |
| ------------------ | ------------------------------------------------------ |
| Frame Selected | Centers the view at the current frame(s). |
| Frame All | Views all content, zoomed in to fit into the viewport. |
| Zoom In + Zoom Out | Zoom in and out in the viewport. |


#### Pie menus

![Pie menus](/docs2/images/editors/movie-clip-editor/header/view-menu/pie-menus-2.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

#### Area

![Area](/docs2/images/editors/movie-clip-editor/header/view-menu/area.jpg)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


##### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/movie-clip-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Close the area window. |


### View Menu in in Tracking mode in Dopesheet sub mode

![View Menu in in Tracking mode in Dopesheet sub mode](/docs2/images/editors/movie-clip-editor/header/view-menu/view-menu-in-in-tracking-mode-in-dopesheet-sub-m.png)

The View menu contains all View related tools.


| Entry | What it does |
| ------------------ | -------------------------------------------------- |
| Frame All | Show all content, zoomed to fit into the viewport. |
| Zoom In + Zoom Out | Zooms in and out in the viewport. |


#### Pie menus

![Pie menus](/docs2/images/editors/movie-clip-editor/header/view-menu/pie-menus-3.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

#### Area

![Area](/docs2/images/editors/movie-clip-editor/header/view-menu/area.jpg)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


##### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/movie-clip-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Close the area window. |


### View Menu in Mask mode

![View Menu in Mask mode](/docs2/images/editors/movie-clip-editor/header/view-menu/view-menu-in-mask-mode.png)

The View menu contains all View related tools.

#### Toolbar

![Toolbar](/docs2/images/editors/movie-clip-editor/header/view-menu/toolbar.png)

Shows or hides the toolbar at the left.

#### Sidebar

![Sidebar](/docs2/images/editors/movie-clip-editor/header/view-menu/sidebar.png)

Shows or hides the sidebar at the right in the viewport.

#### Adjust Last Operation

![Adjust Last Operation](/docs2/images/editors/movie-clip-editor/header/view-menu/adjust-last-operation.png)

Shows the adjust last operation panel down left.

#### Annotations (Legacy) submenu

![Annotations (Legacy) submenu](/docs2/images/editors/movie-clip-editor/header/view-menu/annotations-legacy-submenu-2.png)

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
| --------------------- | ---------------------------------------------------------------------------------------------------------- |
| Set 2D Cursor | The 2D cursor is the center for mask creation and modification. Hotkey only tool! Please use the hotkey! |
| Frame Selected | Zooms to the selection. |
| Frame All | View all zooms in or out in the viewport until all selected objects are displayed fitting in the viewport. |
| View Fit | View all zooms in or out in the viewport to fit the current selection into the viewport. |
| Center View to Cursor | Center Cursor centers the view to the 2D cursor. |


#### Zoom In

Zooms into the view.

##### Zoom Out

Zooms out of the view.

##### Zoom

![Zoom](/docs2/images/editors/movie-clip-editor/header/view-menu/zoom.png)

A set of predefined zoom factors.

#### Pie menus

![Pie menus](/docs2/images/editors/movie-clip-editor/header/view-menu/pie-menus-4.png)

Lists the available pie menus, and gives you the ability to read the hotkeys and assign own hotkeys.

#### Area

![Area](/docs2/images/editors/movie-clip-editor/header/view-menu/area.jpg)

This menu contains general view functionality. And exists in most other editor types too.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |


##### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/editors/movie-clip-editor/header/view-menu/duplicate-area-into-new-window.png)

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.


| Entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Close the area window. |

# Select Menu

### Movie Clip Editor Modes

![Movie Clip Editor Modes](/docs2/images/editors/movie-clip-editor/header/movie-clip-editor-header-2.png)

The Movie Clip Editor is three editors in one. And the Clip editor in mask mode looks also different. So we need to explain the content for all editor types plus the Mask mode that has a Select menu.

The Dope sheet mode has no Select menu.

### Select Menu in Tracking mode in Clip sub mode

#### All

![All](/docs2/images/editors/movie-clip-editor/header/select-menu/all.png)

Select everything.


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| None | Select nothing. |
| Inverse | Invert the current selection. |
| Box Select | Draw a rectangle to box select markers. It adds to selection by default. To subtract from selection hold down Shift key. |
| Circle Select | Circle select enters the Circle Select mode. This is a special select mode where you can select elements by moving with the mouse over it. It adds to selection by default. To subtract from selection hold down Shift key. To exit the Circle select click with the right mouse button. The pencil radius of the circle select tool can be adjusted with the scroll wheel. |


#### Lasso Select

![Lasso Select](/docs2/images/editors/movie-clip-editor/header/select-menu/lasso-select.png)

A sub menu with the available lasso select modes.

#### Grouped

![Grouped](/docs2/images/editors/movie-clip-editor/header/select-menu/grouped.png)

Here you can select objects that are in the same group by the chosen method. The items should be self explaining.


| Entry | What it does |
| ------------------------------------ | -------------------------------------------------------------- |
| Select Stabilization tracks | Select the tracks that are used for translation stabilization. |
| Select Stabilization Rotation tracks | Select the tracks that are used for rotation stabilization. |


### Select Menu in Tracking mode in Graph sub mode

#### All

![All](/docs2/images/editors/movie-clip-editor/header/select-menu/all-2.png)

Select everything.


| Entry | What it does |
| ------- | ----------------------------- |
| None | Select nothing. |
| Inverse | Invert the current selection. |


### Select Menu in Mask mode

![Select Menu in Mask mode](/docs2/images/editors/movie-clip-editor/header/select-menu/select-menu-in-mask-mode.png)

Note that you need to have a mask so that the content becomes active.


| Entry | What it does |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All | Select everything. |
| None | Select nothing. |
| Inverse | Invert the current selection. |
| Box Select | Draw a rectangle to box select markers. It adds to selection by default. To subtract from selection hold down Shift key. |
| Circle Select | Circle select enters the Circle Select mode. This is a special select mode where you can select elements by moving with the mouse over it. It adds to selection by default. To subtract from selection hold down Shift key. To exit the Circle select click with the right mouse button. The pencil radius of the circle select tool can be adjusted with the scroll wheel. |


#### Lasso Select

![Lasso Select](/docs2/images/editors/movie-clip-editor/header/select-menu/lasso-select.png)

A sub menu with the available lasso select modes.


| Entry | What it does |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Linked | Select all curve points that are linked to the already selected points. |
| More/Less Submenu | **More**: Increase the selection by one point. · **Less**: Decrease the selection by one point. |

# Tracking Mode › Clip Submode › Clip Menu

### Clip Menu

#### Open Clip

![Open Clip](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-clip-menu/open-clip.png)

Opens an Image Sequence or a movie clip.


| Entry | What it does |
| -------------------- | ---------------------------------------------------------------------------------------- |
| Set Scene Frames | Set the start and end frame of the frames to match the start and end frame of the clips. |
| Prefetch Frames | Prefetch frames from disk for faster playback and/or tracking. |
| Reload Clip | Reloads the movie clip. |
| Set as Background | Set the current movie clip as the camera background in the 3d view. |
| Setup Tracking Scene | Prepare the scene fro compositing 3d objects into this footage. |

# Tracking Mode › Clip Submode › Track Menu

### Track Menu

![Track Menu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/track-menu.png)

Contains tracking functionality. Note that lots of this content is currently a double entry to the content in the tool shelf. The tool shelf content will most probably vanish in the future, in favour of a tool shelf with buttons like in the 3d view.

#### Transform submenu

![Transform submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/transform-submenu.png)

Track navigation.

##### Move

Move the selected track(s).

###### Last Operator Move

![Last Operator Move](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-move.png)

###### Move X, Y Z

The position. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and moves relative to this zero then. For the actual location values have a look in the sidebar in the transform panel.

###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enables mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Rotate

Rotate the selected tracks.

###### Last Operator Rotate

![Last Operator Rotate](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-rotate.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enables mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Resize

![Resize](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/resize.png)

Resize the selected track(s).

###### Last Operator Resize

![Last Operator Resize](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-resize.png)


| Entry | What it does |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Angle | The rotation. Attention, the actual world orientation and rotation does not matter here. It always starts with a value of zero, and rotates relative to this zero then. For the actual rotation values have a look in the sidebar in the transform panel. |
| Axis | Which axis to rotate. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/orientation.png)

The widget can have different orientations. The menu items should be self explaining.

###### Mirror Editing

Enables mirror editing.

###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


#### Track Motion submenu

![Track Motion submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/track-motion-submenu.png)


| Entry | What it does |
| --------------- | -------------------------------- |
| Backwards | Track backwards the whole range. |
| Frame Backwards | Track backwards frame wise. |
| Forwards | Track forwards the whole range. |
| Frame Forwards | Track forwards frame wise. |


#### Clear submenu

![Clear submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/clear-submenu.png)


| Entry | What it does |
| ---------- | ----------------------------------------------- |
| Before | Clears track paths before the current position. |
| After | Clears track paths after the current position. |
| Track Path | Clears the currently active Track Path. |
| Solution | Clears all calculated data. |


| Entry | What it does |
| -------------- | --------------------------------------------------------------------------------------------------------------------- |
| Refine submenu | **Backwards**: Refine selectet marker positions forwards. · **Backwards**: Refine selectet marker positions forwards. |
| Add Marker | Add a marker. The marker will appear under the mouse, and stick until you click. |


#### Detect Features

![Detect Features](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/detect-features.png)

Adds automatically markers at the current movie position, and tries to detect marcant areas in the current frame that are useful for tracking. It also sets keyframes at this position.

When enough marcant areas are available then it adds up to eight markers that way.

![Detect Features](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/detect-features-2.png)

##### Last Operator Detect Features

![Last Operator Detect Features](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-detect-features.png)

###### Placement

Placement is a drop down box where you can limit the placement of the markers.

###### Whole frame

![Whole frame](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/whole-frame.png)

The markers can be at every position of the current frame image.


| Entry | What it does |
| --------------------- | ------------------------------------------------ |
| Inside Grease Pencil | The markers have to be inside the Grease Pencil. |
| Outside Grease Pencil | The markers have to be outside Grease Pencil. |


| Entry | What it does |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| Margin | Gives a margin to the border of the frame image. Markers have to stay away from the border by the given amount. |
| Threshold | The threshold level to consider the current position of the marker as good enough for tracking. |
| Distance | The minimum distance between two markers. |


#### Create Plane Track

Creates a plane track. A plane track can be used to map an image or a movie at an area in your clip. The Plane track.

#### New Image from Plane Marker

![New Image from Plane Marker](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/new-image-from-plane-marker.png)

Create new image from the content of the plane markerfrom the pixels of the movie clip that the plane marker “sees” at the current frame. This allows you to create and impose an un-warped texture of any flat surface in the footage.

To use, create and select four tracking points then create a Plane Marker. Once you’ve selected the Plane Marker, create the new image - then edit the image in the Image Editor.

#### Update Image from Plane Marker

Update current image used by plane marker from the content of the plane marker. This updates the pixels of the active Plane Track’s image.

Allows you to update the texture of any flat surface in the footage.

#### Solve Camera Motion

Starts the calculation for the camera motion to match the track motion.

There should be at least eight common tracks on the both of the selected keyframes.

There should be noticeable parallax effects between these two keyframes.

The average re-projection error is reported to the information space and to the clip editor header. Re-projeciton error means the average distance between reconstructed 3D position of tracks projected back to footage and original position of tracks. Re-projection error below 0.3 means accurate re-projection, (0.3 - 3.0) means quite nice solving which still can be used. Values above 3 means some tracks should be tracked more accurately, or that values for focal length or distortion coefficients were set incorrectly.


| Entry | What it does |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Join Tracks | Joins selected tracks. |
| Average Tracks | Average selected tracks into active. |
| Copy Tracks | Copy selected tracks to clipboard. |
| Paste Tracks | Pastes selected tracks from clipboard. |
| Copy Settings to Defaults | Copies track settings from active track to default settings. |
| Apply default settings | Copy tracking settings form active tracks to selected tracks. You need to select the source track first, then hold down shift, then select the target track. Then perform copy track settings. |


#### Animation submenu

![Animation submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/animation-submenu.png)

##### Insert Keyframe

![Insert Keyframe](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/insert-keyframe.png)

Inserts a keyframe at current position in spreadsheet sub mode panel.

##### Delete Keyframe

Deletes keyframes at current position in dope sheet sub mode panel.

#### Show/Hide submenu

![Show/Hide submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/show-hide-submenu.png)

Show or hide tracks.


| Entry | What it does |
| --------------- | --------------------------- |
| Show Hidden | Show all hidden tracks. |
| Hide Selected | Hide the selected tracks. |
| Hide Unselected | Hide the unselected tracks. |


##### Last operator Hide Tracks

![Last operator Hide Tracks](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-hide-tracks.png)

###### Unselected

Hide selected or unselected tracks.

#### Clean up submenu

![Clean up submenu](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/clean-up-submenu.png)


| Entry | What it does |
| ------------- | ----------------------------------------------------------------- |
| Clean Tracks | Clean tracks with high error values or few frames. |
| Filter Tracks | Filter out tracks that has weird looking spikes in motion curves. |


| Entry | What it does |
| ------------- | --------------------------- |
| Delete Track | Delete the selected track. |
| Delete Marker | Delete the selected marker. |


#### Reconstruction

![Reconstruction](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/reconstruction.png)


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set Origin | Set active marker as origin in 3D space. |
| Set Floor | Set plane in the 3D space as a Floor plane, based at three selected markers. You need to have three markers selected. Or you will get an error message. |


##### Set Wall

Set plane in the 3D space as a Wall plane, based at three selected markers.

###### Last Operator Set Plane

![Last Operator Set Plane](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-set-plane.png)

###### Plane

![Plane](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/plane.png)

A drop down box to choose if you want to set the selected markers as plane or as floor.

##### Set X Axis

Set X axis rotation in 3D space, based at the selected marker. You need to have one marker selected. Or you will get an error.

##### Set Y Axis

Set X axis rotation in 3D space, based at the selected marker. You need to have one marker selected. Or you will get an error.

###### Last Operator Set Axis

![Last Operator Set Axis](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-set-axis.png)

###### Axis

A drop down box to choose if you want to use the axis to X or to Y

##### Set Scale

Set scale of scene by scaling camera, based at two selected markers. You need to have two markers selected. Or you will get an error.

###### Last Operator Set Scale

![Last Operator Set Scale](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-set-scale.png)

###### Distance

The distance between two bundles used for scene scaling.

##### Apply Scale

Apply scale to solution.

###### Last operator Apply Solution Scale

![Last operator Apply Solution Scale](/docs2/images/editors/movie-clip-editor/header/tracking-mode-clip-submode-track-menu/last-operator-apply-solution-scale.png)

###### Distance

The distance between two bundles used for scene scaling.


| Entry | What it does |
| ------------------- | ------------------------------------------------------------------------- |
| 3D Markers to Mesh | Creates a vertex cloud using the coordinates of the reconstructed tracks. |
| Link Empty to Track | Creates an Empty which will be copying movement of active track. |

# Tracking Mode › Graph Submode › Graph Menu

### Track Menu

#### Delete Curve

![Delete Curve](/docs2/images/editors/movie-clip-editor/header/tracking-mode-graph-submode-graph-menu/delete-curve.png)

Deletes the track that correspondent to the current curve.

#### Delete Knot

Deletes the selected curve points.

#### Clear Track Path Remained

![Clear Track Path Remained](/docs2/images/editors/movie-clip-editor/header/tracking-mode-graph-submode-graph-menu/clear-track-path-remained.png)

Clears the track path after the current position.

#### Clear Track Path Up To

![Clear Track Path Up To](/docs2/images/editors/movie-clip-editor/header/tracking-mode-graph-submode-graph-menu/clear-track-path-up-to.png)

Clears the track path up to the current position.


| Entry | What it does |
| -------------------- | ----------------------------------- |
| Clear Track Path All | Clears the complete track path. |
| Disable Markers | Disables the selected curve points. |
| Move | Moves the selected curve points. |
| Rotate | Rotates the selected curve points. |
| Resize | Scales the selected curve points. |

# Mask Mode › Clip Menu

### Clip Menu

#### Open Clip

![Open Clip](/docs2/images/editors/movie-clip-editor/header/mask-mode-clip-menu/open-clip.png)

Opens an Image Sequence or a movie clip.


| Entry | What it does |
| -------------------- | ----------------------------------------------------------------------------------------- |
| Set Scene Frames | Set the start and end frame of the scene to match the start frame and length of the clip. |
| Prefetch Frames | Prefetch frames from disk for faster playback and/or tracking. |
| Reload Clip | Reloads the movie clip. |
| Set as Background | Set the current movie clip as a camera background in the 3d viewport. |
| Setup Tracking Scene | Prepare Scene for compositing 3d opbjects into this footage. |

# Mask Mode › Add Menu

### Add Menu

![Add Menu](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/add-menu.png)

Masking can be done by using curves. In the Add menu you will find two spline primitives. You can choose between a circle Bezier curve object and a square Bezier curve object.

You select curve points by clicking with the left mouse button at them. Holding down Shift will add to the selection. Clicking in the off will deselect everything.

#### Circle

![Circle](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/circle.png)

Adds a Bezier circle that you can use for masking.

![Circle](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/circle-2.png)

This circle element can be modified by right clicking at the handlers and pulling at the handlers until the desired result is achieved. The yellow points are handlers. The whole curve can be moved around with right mouse button. See also Transform sub menu in the Mask menu.

##### Last Operator Add Circle

![Last Operator Add Circle](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/last-operator-add-circle.png)


| Entry | What it does |
| ------------ | --------------------------- |
| Size | The size of the circle. |
| Location X Y | The location of the circle. |


#### Square

![Square](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/square.png)

Adds a Bezier circle that you can use for masking.

![Square](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/square-2.png)

This circle element can be modified by right clicking at the handlers and pulling at the handlers until the desired result is achieved. The yellow points are handlers. The whole curve can be moved around with right mouse button. See also Transform sub menu in the Mask menu.

##### Last Operator Add Square

![Last Operator Add Square](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/last-operator-add-square.png)


| Entry | What it does |
| ------------ | --------------------------- |
| Size | The size of the circle. |
| Location X Y | The location of the circle. |


#### Add Vertex and Slide

![Add Vertex and Slide](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/add-vertex-and-slide.png)

You can add more curve points by holding down ctrl and clicking left at a curve.

You can create a spline from scratch with this method too. Simply hold down Ctrl, click into the viewport, and created your needed spline points. To close the created mask spline use Toggle Cyclic from the mask menu.

##### Last operator Add Vertex and Slide

![Last operator Add Vertex and Slide](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/last-operator-add-vertex-and-slide.png)

###### Location X Y

The location of the created spline point.

#### Feather Vertex Slide

![Feather Vertex Slide](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/feather-vertex-slide.png)

Add new vertex to feather and slide it. Hotkey only tool !

##### Last Operator Add Feather Vertex and Slide

![Last Operator Add Feather Vertex and Slide](/docs2/images/editors/movie-clip-editor/header/mask-mode-add-menu/last-operator-add-square.png)

###### Location X Y

The location of the circle.

# Mask Mode › Mask Menu

Masking **preface**

![Mask Mode - Mask Menu](/docs2/images/editors/movie-clip-editor/mask-mode.png)

Masks have many purposes. They can be used in a motion tracking workflow to mask out, or influence a particular object in the footage. They can be used for manual rotoscoping to pull a particular object out of the footage. Or as a rough matte for green screen keying. This is done in the Node editor in compositing mode by a mask node.

Masks are independent from a particular image of movie clip. And so they can just as well be used for creating motion graphics or other effects in the compositor.

Masks are defined by splines. Means you work with splines, and you have a bunch of spline tools available.

S-Curves

The curve type used for creating mask splines is almost a Bezier curve. But there are some differences. Smooth edges of the mask are defined by feathering. These are called S-Curves.

Besides the handles, every control point also has points that define the feather between the current point and the next point on the spline. Each feather point is stored in UV space, where U means position across spline segment, and V means distance between main spline and feather points.

![Mask Mode - Mask Menu](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/mask-mode-mask-menu.png)

This allows for deforming the main spline in almost any way, and the feather will be updated automatically to reflect that change.

For example if there is just rotation of the spline, feather would stay completely unchanged. If one point’s feather is moved, the other feathers will be automatically stretched uniformly along that segment and the overall shape will be almost the same as artists would want it to be.

### Mask Menu

![Mask Menu](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/mask-menu.jpg)

#### Transform

![Transform](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/transform.png)

##### Move

Move the selected curve spline or points.

###### Last Operator Move

###### Values

![Values](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/values.png)

Adjust the move amount.

X, Y and Z defines the position.

###### Axis Ortho

Along which axis to move.

###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to Adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


##### Rotate

Rotate the selected curve spline or points.

###### Last Operator Rotate

###### Angle

![Angle](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/angle.png)

Adjust the angle.

###### Axis

![Axis](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Along which axis to rotate


| Entry | What it does |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| Orientation | Orientation is a drop-down box where you can choose the type of orientation for the transform action. |
| Mirror Editing | Enables mirror editing. |


###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


##### Scale

Scale the selected curve spline or points.

###### Last Operator Resize

###### Scale X Y Z

![Scale X Y Z](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/scale-x-y-z.png)

Adjust the scaling.

###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


##### To Sphere

Shapes a selection of objects into the shape of a sphere. The calculation happens with the object origins.

In Object mode this tools requires to have more than one object selected.

###### Usage

![Usage](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/usage.png)

Select the objects, activate the tool, then drag the mouse in the 3D viewport. In the header you will read the current factor then. Which tells you how close you are towards the sphere shape.

###### Last Operator To Sphere

![Last Operator To Sphere](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-to-sphere.png)

###### Factor

The factor to transform the selection into a shape form.

###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Shear

Shear shears the selection.

In Object mode this tools requires to have more than one object selected.

###### Last Operator Shear

![Last Operator Shear](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-shear.png)

###### Offset

Adjust an offset.

###### Shear Axis

The shear tool works along a imaginary 2d plane. The shear axis controls if the items are sheared along the x or the y axes of this plane. This is the plane along which the transformation happens. You can shear along the x or the y axis of this plane.

To make things even more complicated, the orientation of this imaginary plane is defined by the Axis and Axis Ortho items below.


| Entry | What it does |
| ---------- | --------------------------------------------------------- |
| Axis | Defines one axis of the imaginary shear axis plane. |
| Axis Ortho | Defines the other axis of the imaginary shear axis plane. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Choose the orientation for the shear action.


| Entry | What it does |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mirror Editing | Enables mirror editing. |
| Proportional editing | Enables proportional editing. Activating proportional editing reveals further settings. · **Proportional Falloff**: Adjust the falloff methods. · **Proportional Size**: See and adjust the falloff radius. · **Connected**: The proportional falloff gets calculated for connected parts only. · **Projected(2D)**: The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Push/Pull

It pushes or pulls the object positions relative to the center of the selection.

In Object mode this tool requires to have more than one object selected.

###### Last Operator Push/Pull

![Last Operator Push/Pull](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-push-pull.png)


| Entry | What it does |
| -------------- | --------------------------------------------- |
| Distance | Adjust the strength of influence of the tool. |
| Mirror Editing | Enables mirror editing. |


###### Proportional editing

![Proportional editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Enables proportional editing. Activating proportional editing reveals further settings.


| Entry | What it does |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Proportional Falloff | Adjust the falloff methods. |
| Proportional Size | See and adjust the falloff radius. |
| Connected | The proportional falloff gets calculated for connected parts only. |
| Projected(2D) | The proportional falloff gets calculated in the screen space. Depth doesn't play a role. When it's in the radius, then it gets calculated. |


##### Scale Feather

![Scale Feather](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/scale-feather.png)

Scale feather weight for the selected points.

The curve type that is used to create mask splines is almost a Bezier curve. But it has some differences. Smooth edges of the mask are defined by feathering. The curve needed to support feathering in a way that stuck to the curve as you edited it, for ease of editing an animation. These are called S-Curves.

Besides the handles, every control point also has points that define the feather between the current point and the next point on the spline. Each feather point is stored in UV space, where U means position across spline segment, and V means distance between main spline and feather points.

###### Last Operator Transform

![Last Operator Transform](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-transform.png)


| Entry | What it does |
| ------ | --------------------------------------------------------------------------------- |
| Values | Adjust the scale amount. X, Y and Z defines the position. W defines the rotation. |
| Axis | Around which axis to rotate. X, Y or Z. |


###### Orientation

![Orientation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/orientation.png)

Orientation is a drop-down box where you can choose the type of orientation for the transform action.

###### Mirror Editing

Enables mirror editing.

###### Proportional Editing

![Proportional Editing](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing.png)

Proportional Editing is a drop-down box where you can choose to use proportional editing. When you choose one of the active methods then the neighbor geometry gets influenced too in a proportional way.

**Proportional Editing Falloff**

![Proportional Editing Falloff](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/proportional-editing-falloff.png)

Proportional Editing Falloff is a drop-down box where you can choose a method for the falloff for the proportional editing.


| Entry | What it does |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proportional size | Proportional size is an edit box to adjust the strength of the Proportional falloff. |
| Connected | Just edit geometry that is directly connected with the current selection. 4 Bforartists 2 Reference Manual - 7.1.4 Editors - 3D View - Header - Navigation Menu |
| Projected ( 2D) | Edit geometry that is in 2d space aligned with the current selection. This one goes from the current view in depth direction. |


##### Clear Feather Weight

Reset the feather weight to zero.


| Entry | What it does |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Duplicate | Duplicates the selected curve and moves it. |
| Delete | Deletes the selected mask curve point. |
| Copy Splines | Copies the currently selected spline. |
| Paste Splines | Pastes a copied spline. |
| Make Parent | Set the mask's parenting. |
| Clear Parent | Clears the mask's parenting. |
| Toggle Cyclic | Make the spline closed or open. |
| Switch Direction | Switch the direction in which the spline points. A spline has a direction. A starting point and an endpoint. By switching the starting point becomes the end point, the end point becomes the starting point. |
| Recalc Normals | Recalculate the direction of the selected spline handlers. |


#### Set Handle Type

![Set Handle Type](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/set-handle-type.png)

In this sub menu you can set the handle type for the currently selected spline points.

#### Animation

![Animation](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/animation.png)

##### Insert Shape Key

![Insert Shape Key](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/insert-shape-key.png)

Inserts a shape key keyframe.

The inserted keyframes can then be found in the dope sheet editor in mask mode.

##### Clear Shape Key

Clears an existing shape key keyframe.

##### Reset Feather Animation

Resets the feather offset across all animated frames.

##### Re-key Shape points

Recalculate animation data on selected points for frames selected in the dope sheet.

#### Show / Hide

![Show / Hide](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/show-hide.png)


| Entry | What it does |
| ------------- | ------------------------- |
| Show Hidden | Reveals all hidden curves |
| Hide Selected | Hides the selected curve. |


##### Hide Unselected

Hides the unselected curves.

###### Last operator Hide Layer

![Last operator Hide Layer](/docs2/images/editors/movie-clip-editor/header/mask-mode-mask-menu/last-operator-hide-layer.png)

###### Unselected

Hide selected or unselected curves.
