---
id: "snippet.marker-menu"
title: "Marker menu"
section: "snippets"
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17.1.4 Editors - Timeline - Marker Menu.odt"]
---

![Marker menu](/docs2/images/ui/shared/marker-menu/marker-menu.png)

Markers are visual landmarks. They can mark a start of a specific animation sequence, the end of a camera movement, and so on.

When you add one then a marker area appears at the bottom of the timeline.

Markers can be pulled around by clicking at them and dragging them left or right. The active marker is yellow.

By holding down shift you can select more than one marker.

## Add Marker

Adds a marker at the current frame position.

## Duplicate Marker

Duplicates the selected marker(s). The duplicate(s) sticks at the mouse until you click to give it the target destination.

## Duplicate Marker to Scene

![Duplicate Marker to Scene](/docs2/images/ui/shared/marker-menu/duplicate-marker-to-scene.png)

A blend file can contain more than one scene. See Scene Properties in the Properties editor. Here you can duplicate markers to other scenes.

![Duplicate Marker to Scene](/docs2/images/ui/shared/marker-menu/duplicate-marker-to-scene-2.png)

## Delete Marker

Deletes the selected marker(s).

## Bind Camera to Markers

![Bind Camera to Markers](/docs2/images/ui/shared/marker-menu/bind-camera-to-markers.png)

Bind camera to markers turns an object into a camera object. This can be any object in the scene. Not just camera objects.

When the current frame position does not have a marker yet, then it creates a marker at the current frame position.

By binding different objects or cameras at different marker locations you can switch cameras automatically.

The marker with a bind camera attached will show a camera icon.

## Rename Marker

![Rename Marker](/docs2/images/ui/shared/marker-menu/rename-marker.png)

A menu will open up where you can rename the active marker.

## Move Marker

Hotkey only functionality! This menu item exists to show the hotkey to move the marker.

## Select sub menu

![Select sub menu](/docs2/images/ui/shared/marker-menu/select-sub-menu.png)

| Menu entry | What it does |
| -------------------- | --------------------------------------------- |
| All | Select all markers. |
| None | Deselect all markers. |
| Invert | Inverts the current selection. |
| Before Current Frame | Selects the markers before the current frame. |
| After Current Frame | Selects the markers after the current frame. |

## Jump to Next Marker

Sets the frame position to the next marker.

## Jump to Previous Marker

Sets the frame position to the previous marker.
