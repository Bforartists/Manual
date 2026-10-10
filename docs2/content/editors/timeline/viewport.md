---
id: "editors.timeline.viewport"
title: "Timeline viewport"
section: "editors"
path: ["Editors", "Timeline", "Viewport"]
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17 Editors - Timeline.odt"]
---

## Navigation

Some navigation has no menu entry. It works with the mouse and hotkeys only.

| Input | What it does |
|---|---|
| :kbd[RMB] | Moves the time cursor |
| :kbd[LMB] on the number bar | Moves the time cursor |
| :kbd[LMB] drag on a keyframe | Moves the keyframe |
| :kbd[MMB] drag | Pans the view |
| :kbd[Ctrl+MMB] drag or :kbd[Wheel] | Zooms the view |

## Dope Sheet context menu

![Dope Sheet context menu](/docs2/images/ui/timeline/viewport/dope-sheet-context-menu.png){.right}

Right-click in the viewport to open the **Dope Sheet context menu**. The Timeline uses the same menu as the Dope Sheet.

| Menu entry | What it does |
|---|---|
| Copy | Copies the selected keyframes |
| Paste | Pastes the copied keyframes |
| Paste Flipped | Pastes the copied keyframes, mirrored |
| Keyframe Type › | Changes the colour type of the selected keyframes |
| Handle Type › | Sets the handle type of the selected keyframes |
| Interpolation Mode › | Sets how the curve moves from one keyframe to the next, for example linear instead of curved |
| Easing Mode › | Sets the easing method. The easing shape is in Interpolation Mode |
| Insert Keyframes | Inserts a keyframe at the current frame |
| Duplicate | Duplicates the selected keyframes |
| Delete Keyframes | Deletes the selected keyframes |
| Mirror › | Mirrors the selected keyframes by the chosen method |
| Snap › | Snaps the selected keyframes by the chosen method |

:::tip
**Handle Type** matters here too. The handles are edited in the Graph Editor, but they also change how the animation moves at each keyframe.
:::

## Snapping the frame slider

Hold :kbd[Ctrl] while you drag the frame slider to snap by the frame rate, for example in steps of 24 frames at 24 fps. Other sliders snap the same way. See [Menus, buttons and controls › Snapping](../../interface/components/menus-buttons-controls.md#snapping).

## Quick menu

The Timeline has no Quick menu in its header. Press :kbd[Q] over the viewport to open it. See [Quick menu](header.md#quick-menu).
