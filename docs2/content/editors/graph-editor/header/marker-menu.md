---
id: editors.graph-editor.header.marker-menu
title: Marker Menu
section: editors
path:
  - Editors
  - Graph Editor
  - Header
  - Marker Menu
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 18.1.5 Editors - Graph Editor - Marker Menu.odt
---
## Dopesheet Editor - Marker Menu

![Dopesheet Editor - Marker Menu](/docs2/images/editors/graph-editor/header/marker-menu/dopesheet-editor-marker-menu.png)

Markers are visual landmarks. They can mark a start of a specific animation sequence, the end of a camera movement, and so on.

When you add one then a marker area appears at the bottom of the timeline.

Markers can be pulled around by clicking at them and dragging them left or right. The active marker is yellow.

By holding down shift you can select more than one marker.

### Add Marker

Adds a marker at the current frame position.

### Duplicate Marker

Duplicates the selected marker(s). The duplicate(s) sticks at the mouse until you click to give it the target destination.

#### Last Operator Duplicate Time Marker

![Last Operator Duplicate Time Marker](/docs2/images/editors/graph-editor/header/marker-menu/last-operator-duplicate-time-marker.png)

##### Frames

The target frame to position the duplicated marker.

### Duplicate Marker to Scene

![Duplicate Marker to Scene](/docs2/images/editors/graph-editor/header/marker-menu/duplicate-marker-to-scene.png)

Duplicate markers to other scenes. A blend file can contain more than one scene. See Scene Properties in the Properties editor.

![Duplicate Marker to Scene](/docs2/images/editors/graph-editor/header/marker-menu/duplicate-marker-to-scene-2.png)

#### Last Operator Make Links to Scene

![Last Operator Make Links to Scene](/docs2/images/editors/graph-editor/header/marker-menu/last-operator-make-links-to-scene.png)

##### Scene

The target scene to duplicate the markers.

### Delete Marker

Deletes the selected marker(s).

### Bind Camera to Markers

![Bind Camera to Markers](/docs2/images/editors/graph-editor/header/marker-menu/bind-camera-to-markers.png)

Bind camera to markers turns an object into a camera object. This can be any object in the scene. Not just camera objects.

When the current frame position does not have a marker yet, then it creates a marker at the current frame position.

By binding different objects or cameras at different marker locations you can switch cameras automatically.

The marker with a bind camera attached will show a camera icon.

### Rename Marker

![Rename Marker](/docs2/images/editors/graph-editor/header/marker-menu/rename-marker.png)

A menu will open up where you can rename the active marker.

#### Last Operator Rename Marker

![Last Operator Rename Marker](/docs2/images/editors/graph-editor/header/marker-menu/last-operator-rename-marker.png)

#### Name

Rename the active marker.


| Entry | What it does |
| ----------------------- | --------------------------------------------------------------------------------------- |
| Grab/Move Marker | Hotkey only functionality! This menu item exists to show the hotkey to move the marker. |
| Jump to Next Marker | Sets the frame position to the next marker. |
| Jump to Previous Marker | Sets the frame position to the previous marker. |


