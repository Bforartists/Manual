---
id: editors.timeline.header
title: "Header"
section: editors
path:
  - Editors
  - Timeline
  - Header
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 17.1.1 Editors - Timeline - Header Tools and Options.odt
  - 17.1.3 Editors - Timeline - View Menu.odt
shared:
  - docs2/snippets/quick-menu.md
  - docs2/snippets/marker-menu.md
order: 10
summary: "The header contains various menus and tools."
---
## Introduction

The header contains various menus and tools. This chapter here is about the tools and options elements in the header.

The text menus are covered in its own chapter each.

![Introduction](/docs2/images/ui/timeline/header/introduction.png)

## Playback Elements

![Playback Elements](/docs2/images/ui/timeline/header/playback-elements.png)

The playback elements allows you to play your animation, and set the animation range.

### Time Jump Delta

![Time Jump Delta](/docs2/images/ui/timeline/header/time-jump-delta.png)

Number of frames or seconds to jump forward or backward.

#### Jump Unit

What to use for the time jump. Frames or Seconds.

| Property | What it changes |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Jump to Endpoint - start | Jumps to the first frame. |
| Jump to Keyframe - previous | Jumps to the keyframe before the current position. |
| Play Animation - backward | Plays the animation in reverse direction. |
| Play Animation - forward | Plays the animation. |
| Jump to Keyframe - next | Jumps to the keyframe after the current position. |
| Jump to Endpoint - end | Jumps to the last frame. |
| Cancel animation | Cancels the animation and returns to the original frame. |
| Current Frame | The edit box with the position of the current frame. Click at the value and type in another value to jump to another frame. |

### Set Start Frame

![Set Start Frame](/docs2/images/ui/timeline/header/set-start-frame.png)

Sets the current frame position as the start frame.

### Use Preview Range

![Use Preview Range](/docs2/images/ui/timeline/header/use-preview-range.png)

Toggle an alternative range used to preview animations. The Preview range works for the UI playback, but will not work for rendering an animation.

The preview range is displayed in orange color. The original playback range that is used for rendering is still displayed in grey underneath. When Use Preview Range is on, then the animation will loop between the Preview range.

| Property | What it changes |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Start | The start frame for the animation in current mode. |
| End | The end frame for the animation in current mode. |
| Set End Frame | Sets the current frame position as the end frame. |
| Insert Keyframe | Inserts a keyframe. If you do not have a keying set assigned, this will default to the default keying set defined in the Preferences. |
| Delete Keyframe | Removes the keyframe at the current position in the current active keying set. |

## Keyframing

![Keyframing](/docs2/images/ui/timeline/header/keyframing-group.png)

All the keyframing buttons now sit together in one group, from left to right. The snapping buttons come right after them.

**Insert Keyframe** and **Delete Keyframe** add or remove a keyframe on the current frame, for whatever you have selected. In the NLA editor, Insert Keyframe keys the active strip's action, so it does the right thing there too.

The round button turns **Auto Keying** on. With it on, every change you make in the 3D View sets a keyframe on the current frame, or updates the one that's there. It works for transforms of objects and bones, not for things like colors in the Properties Editor.

The **Keying Set** field picks which channels get keyed, for example only Location, or Location and Rotation.

The last button, with the diamond, opens the **Keyframing** settings. Its icon shows the current keyframe type.

### Keyframing settings

<!-- TODO screenshot: Timeline header, the Keyframing popover (diamond button) open, with Auto Keying on -->

**New Keyframe Type** is now right at the top level, so you can pick it without digging. It sets the type, and with it the color, of new keyframes: Keyframe, Breakdown, Moving Hold, Extreme, Jitter or Generated.

The Auto Keying options only show while Auto Keying is on:

- **Auto Keying Mode** chooses whether auto keying adds new keyframes and replaces existing ones (**Add & Replace**), or only replaces keyframes that already exist (**Replace**). Both now have icons.
- **Only Active Keying Set** keys just the channels in the keying set you picked.
- **Layered Recording** adds a new NLA track and strip for every pass you record over the animation, so you can tweak without destroying earlier passes.
- **Cycle-Aware Keying** keeps cyclic animations in sync. New keys on looping channels are mapped back into the loop.

## Playback Panel

![Playback Panel](/docs2/images/ui/timeline/header/playback-panel.png)

Here you can find various options for playback.

### Sync Mode

How to synchronize playback.

| Property | What it changes |
| -------------- | --------------------------------------------- |
| No Sync | Don't synchronize. Play every frame. |
| Frame Dropping | Drop frames if playback is too slow. |
| AV Sync | Drop frames to synchronize to Audio Playback. |

### Audio Scrubbing

![Audio Scrubbing](/docs2/images/ui/timeline/header/audio-scrubbing.png)

Play existing audio from sequence editor when scrubbing.

| Property | What it changes |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Play Audio | Play back existing audio from sequence editor, otherwise mute the audio when deactivated. Use the Sequence Editor to add audio. |
| Sub frames | Show current scene sub frame and allow to set it by using interface tools. |
| Limit Playback to Frame Range | Don't allow frame selection with the mouse outside of the play range. |
| Follow Current Frame | Follow current frame in editors. |

### Play in

![Play in](/docs2/images/ui/timeline/header/play-in.png)

Plays the animation in the chosen editor types.

- Active Editor
- 3D Viewport
- Animation Editors
- Image Editor
- Properties Editor and Sidebars
- Movie Clip Editor
- Node Editors
- Video Sequencer
- Spreadsheet

## Playhead Snapping

![Playhead Snapping](/docs2/images/ui/timeline/header/playhead-snapping.png)

Playhead controls in animation editors help position the current frame indicator with precision, improving navigation and editing across the Timeline, Dope Sheet, Graph Editor, NLA, and Video Sequencer.

| Property | What it changes |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Playhead Snapping On/Off | Toggles snapping behavior for the playhead with a visual indicator. When enabled, the playhead will snap to nearby time-based targets during scrubbing or dragging. **Tip:** *You can temporarily enable/disable the playhead snapping by holding down Ctrl while dragging the playhead.* |
| Distance | Sets the snapping threshold in pixels. Determines how close the playhead must be to a target for snapping to occur. |
| Snap Target | **Frames**: Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame cursor placement. · **Seconds**: Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing. · **Markers**: Snaps to the closest timeline marker. Great for aligning actions to scene events or beats. · **Keyframes**: Snaps to keyframe positions. Ensures precise alignment for editing and playback. · **Strips**: Snaps to the start or end of video/audio strips. Useful in the Video Sequencer and NLA editor. |

### Frame Step

![Frame Step](/docs2/images/ui/timeline/header/frame-step.png)

Defines the step size for frame-by-frame navigation. Controls how far the playhead moves when stepping through frames manually.

> **Note:** Only available with Frames Snap Target

### Second Step

Defines the step size for second-by-second navigation. Controls how far the playhead moves when stepping through the timeline manually.

> **Note:** Only available with Second Snap Target

## Options

![Options](/docs2/images/ui/timeline/header/options.png)

| Property | What it changes |
| ------------------ | ------------------------------------------------------- |
| Only show errors | Only include f-curves that are disabled or have errors. |
| Only show selected | Just show the keyframes from the selected object. |

### Show Seconds

![Show Seconds](/docs2/images/ui/timeline/header/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.

| Property | What it changes |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sync visible range | Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |
| Show Cache | Show animation information for cached objects like Particles. · **Softbody, Particles, etc.**: Include or exclude what kind of cache types you want to display. |

## Dope Sheet Overlays

### Show Overlays

Shows the Dope Sheet Overlays.

### Overlays

![Overlays](/docs2/images/ui/timeline/header/overlays.png)

#### Show Scene Strip Range

When using Scene Time Synchronisation in the video sequence editor, then display the range of the current scene strip.

## Quick menu

*Shared section: [Quick menu](../../../snippets/quick-menu.md)*

## View Menu

![View Menu](/docs2/images/ui/timeline/header/view-menu.png)

The View menu contains all View related tools.

### Adjust Last Operation

![Adjust Last Operation](/docs2/images/ui/timeline/header/adjust-last-operation.png)

Shows the adjust last operation panel down left.

### Channels

![Channels](/docs2/images/ui/timeline/header/channels.png)

Shows the channels list at the left

| Menu entry | What it does |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| Zoom In | Zooms in. |
| Zoom Out | Zooms out. |
| Zoom Border | Draw a rectangle to zoom to the selection. |
| Frame All | Zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |
| Go to current Frame | Centers the view at the frame slider. |
| Frame Scene Range | With Use Preview Range off , reset the horizontal view to the current scene frame range. |
| Frame Preview Range | With Use Preview Range on , reset the horizontal view to the current preview frame range. |

### Area submenu

![Area submenu](/docs2/images/ui/timeline/header/area-submenu.png)

This menu contains general view functionality. And exists in most other editor types too.

| Menu entry | What it does |
| ---------------- | ------------------------------------------------------------------------- |
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |

#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/ui/timeline/header/duplicate-area-into-new-window.png)

> **Duplicate Area into New Window** opens this editor in a floating window. See **[Floating editor windows](../../interface/windows.md#floating-editor-windows)** in the Interface chapter.

| Menu entry | What it does |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey Ctrl + Space. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey Ctrl + Alt + Space. |
| Close Area | Closes the area window. |

## Marker menu

*Shared section: [Marker menu](../../../snippets/marker-menu.md)*

