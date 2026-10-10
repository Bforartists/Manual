---
id: "editors.timeline.header"
title: "Timeline header"
section: "editors"
path: ["Editors", "Timeline", "Header"]
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17.1.1 Editors - Timeline - Header Tools and Options.odt", "17.1.3 Editors - Timeline - View Menu.odt"]
---

## Introduction

The header contains various menus and tools. This chapter here is about the tools and options elements in the header.

The text menus are covered in its own chapter each.

![Introduction](/docs2/images/ui/timeline/header/introduction.png)

## Playback Elements

![Playback Elements](/docs2/images/ui/timeline/header/playback-elements.png)

The playback elements allows you to play your animation, and set the animation range.

### Time Jump Delta

![Time Jump Delta](/docs2/images/ui/timeline/header/time-jump-delta.png){.right}

Number of frames or seconds to jump forward or backward.

#### Jump Unit

What to use for the time jump. Frames or Seconds.

| Property | What it changes |
|---|---|
| Jump to Endpoint - start | Jumps to the first frame. |
| Jump to Keyframe - previous | Jumps to the keyframe before the current position. |
| Play Animation - backward | Plays the animation in reverse direction. |
| Play Animation - forward | Plays the animation. |
| Jump to Keyframe - next | Jumps to the keyframe after the current position. |
| Jump to Endpoint - end | Jumps to the last frame. |
| Cancel animation | Cancels the animation and returns to the original frame. |
| Current Frame | The edit box with the position of the current frame. Click at the value and type in another value to jump to another frame. |

### Set Start Frame

![Set Start Frame](/docs2/images/ui/timeline/header/set-start-frame.png){.right}

Sets the current frame position as the start frame.

### Use Preview Range

![Use Preview Range](/docs2/images/ui/timeline/header/use-preview-range.png){.right}

Toggle an alternative range used to preview animations. The Preview range works for the UI playback, but will not work for rendering an animation.

The preview range is displayed in orange color. The original playback range that is used for rendering is still displayed in grey underneath. When Use Preview Range is on, then the animation will loop between the Preview range.

| Property | What it changes |
|---|---|
| Start | The start frame for the animation in current mode. |
| End | The end frame for the animation in current mode. |
| Set End Frame | Sets the current frame position as the end frame. |
| Insert Keyframe | Inserts a keyframe. If you do not have a keying set assigned, this will default to the default keying set defined in the Preferences. |
| Delete Keyframe | Removes the keyframe at the current position in the current active keying set. |

## Active Keying Set

![Active Keying Set](/docs2/images/ui/timeline/header/active-keying-set.png){.thumb}

Objects needs a so called keying set so that you can record animation for it. It is a container for the animation, a set of keyframe channels. When you try to record an animation without an existing keying set, then you will get a warning since the channels for the keyframes are missing.

In this property you can choose a method from the builtin keying sets.

### Auto Keying

With auto keying on every manipulation in the 3d view will automatically create a keyframe, or update the existing keyframe at the current position.

Note that Auto Keying just works with transform properties ( Objects and Bones) in the 3d View. It will not work to animate colors in the Properties Editor for example.

### Auto Keyframing Popover

![Auto Keyframing Popover](/docs2/images/ui/timeline/header/auto-keyframing-popover.png){.right}

Auto keying settings. These settings shows when you have auto keying activated.

| Property | What it changes |
|---|---|
| Auto keying mode | **Add & Replace**: Replace existing keyframes and add new ones where no keyframes exists.<br>**Replace**: Just replace existing keyframes. |
| Only Active Keying Set | Automatic keyframe insertion using active keying set only. |
| Layered Recording | Add a new nla track and strip for every loop or pass made over the animation. This allows non destructive tweaking. |
| Cycle aware keying | For channels with cyclic extrapolation, the keyframe insertion is automatically remapped inside the cycle time range, and keeps the ends in sync. |

### Active Keying Set

![Active Keying Set](/docs2/images/ui/timeline/header/active-keying-set-2.png){.right}

Choose your keying set.

## Playback Panel

![Playback Panel](/docs2/images/ui/timeline/header/playback-panel.png){.right}

Here you can find various options for playback.

### Sync Mode

How to synchronize playback.

| Property | What it changes |
|---|---|
| No Sync | Don't synchronize. Play every frame. |
| Frame Dropping | Drop frames if playback is too slow. |
| AV Sync | Drop frames to synchronize to Audio Playback. |

### Audio Scrubbing

![Audio Scrubbing](/docs2/images/ui/timeline/header/audio-scrubbing.png){.right}

Play existing audio from sequence editor when scrubbing.

| Property | What it changes |
|---|---|
| Play Audio | Play back existing audio from sequence editor, otherwise mute the audio when deactivated. Use the Sequence Editor to add audio. |
| Sub frames | Show current scene sub frame and allow to set it by using interface tools. |
| Limit Playback to Frame Range | Don't allow frame selection with the mouse outside of the play range. |
| Follow Current Frame | Follow current frame in editors. |

### Play in

![Play in](/docs2/images/ui/timeline/header/play-in.png){.right}

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

![Playhead Snapping](/docs2/images/ui/timeline/header/playhead-snapping.png){.right}

Playhead controls in animation editors help position the current frame indicator with precision, improving navigation and editing across the Timeline, Dope Sheet, Graph Editor, NLA, and Video Sequencer.

| Property | What it changes |
|---|---|
| Toggle Playhead Snapping On/Off | Toggles snapping behavior for the playhead with a visual indicator. When enabled, the playhead will snap to nearby time-based targets during scrubbing or dragging. **Tip:***You can temporarily enable/disable the playhead snapping by holding down :kbd[Ctrl] while dragging the playhead.* |
| Distance | Sets the snapping threshold in pixels. Determines how close the playhead must be to a target for snapping to occur. |
| Snap Target | **Frames**: Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame cursor placement.<br>**Seconds**: Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing.<br>**Markers**: Snaps to the closest timeline marker. Great for aligning actions to scene events or beats.<br>**Keyframes**: Snaps to keyframe positions. Ensures precise alignment for editing and playback.<br>**Strips**: Snaps to the start or end of video/audio strips. Useful in the Video Sequencer and NLA editor. |

### Frame Step

![Frame Step](/docs2/images/ui/timeline/header/frame-step.png){.right}

Defines the step size for frame-by-frame navigation. Controls how far the playhead moves when stepping through frames manually.

:::note
Only available with Frames Snap Target
:::

### Second Step

Defines the step size for second-by-second navigation. Controls how far the playhead moves when stepping through the timeline manually.

:::note
Only available with Second Snap Target
:::

## Keying Panel

![Keying Panel](/docs2/images/ui/timeline/header/keying-panel.png){.right}

Some more keying options.

### New Keyframe Type

![New Keyframe Type](/docs2/images/ui/timeline/header/new-keyframe-type.png){.right}

Recolor the currently selected keyframes. Or create the new keyframes with this chosen keyframe color.

### Auto Keyframing

![Auto Keyframing](/docs2/images/ui/timeline/header/auto-keyframing.png){.thumb}

| Property | What it changes |
|---|---|
| Auto Keying Mode | Just replace existing keyframes, or add keyframes too. |
| Auto Keyframe Insert Keying Set | Automatic Keyframe Insertion using the active keying set only. |

| Property | What it changes |
|---|---|
| Layered Recording | Add a new NLA Track and Strip for every loop/ pass made over the animation to allow non destructive tweaking. |
| Cycle Aware Keying | For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps the ends in sync. |

## Options

![Options](/docs2/images/ui/timeline/header/options.png){.right}

| Property | What it changes |
|---|---|
| Only show errors | Only include f-curves that are disabled or have errors. |
| Only show selected | Just show the keyframes from the selected object. |

### Show Seconds

![Show Seconds](/docs2/images/ui/timeline/header/show-seconds.png){.right}

Show the timing in the timeline area in seconds instead of frames.

| Property | What it changes |
|---|---|
| Sync visible range | Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |
| Show Cache | Show animation information for cached objects like Particles.<br>**Softbody, Particles, etc.**: Include or exclude what kind of cache types you want to display. |

## Dope Sheet Overlays

### Show Overlays

Shows the Dope Sheet Overlays.

### Overlays

![Overlays](/docs2/images/ui/timeline/header/overlays.png){.right}

#### Show Scene Strip Range

When using Scene Time Synchronisation in the video sequence editor, then display the range of the current scene strip.

## Quick menu

::include{snippet=quick-menu}

## View Menu

![View Menu](/docs2/images/ui/timeline/header/view-menu.png){.right}

The View menu contains all View related tools.

### Adjust Last Operation

![Adjust Last Operation](/docs2/images/ui/timeline/header/adjust-last-operation.png){.right}

Shows the adjust last operation panel down left.

### Channels

![Channels](/docs2/images/ui/timeline/header/channels.png){.right}

Shows the channels list at the left

| Menu entry | What it does |
|---|---|
| Zoom In | Zooms in. |
| Zoom Out | Zooms out. |
| Zoom Border | Draw a rectangle to zoom to the selection. |
| Frame All | Zooms in or out in the viewport until all objects in the scene are displayed fitting in the viewport. |
| Go to current Frame | Centers the view at the frame slider. |
| Frame Scene Range | With Use Preview Range off , reset the horizontal view to the current scene frame range. |
| Frame Preview Range | With Use Preview Range on , reset the horizontal view to the current preview frame range. |

### Area submenu

![Area submenu](/docs2/images/ui/timeline/header/area-submenu.png){.right}

This menu contains general view functionality. And exists in most other editor types too.

| Menu entry | What it does |
|---|---|
| Horizontal Split | Splits the current view horizontally into two independent editor windows. |
| Vertical Split | Splits the current view vertically into two independent editor windows. |

#### Duplicate Area into New Window

![Duplicate Area into New Window](/docs2/images/ui/timeline/header/duplicate-area-into-new-window.png){.right}

Duplicate Area into New Window makes the selected editor window floating. You can then drag it around at the monitor. It is not connected with the rest of the UI anymore.

A separated window cannot be merged into the main window again. You have to close it when not longer needed.

| Menu entry | What it does |
|---|---|
| Toggle Maximize Area | Displays the editor maximized with menus. To return from the maximized view press hotkey :kbd[Ctrl+Space]. Or reuse the menu item in the area menu. |
| Toggle Full screen Area | Displays the editor maximized without menus. To return from the full screen view press hotkey :kbd[Ctrl+Alt+Space]. |
| Close Area | Closes the area window. |

## Marker menu

::include{snippet=marker-menu}
