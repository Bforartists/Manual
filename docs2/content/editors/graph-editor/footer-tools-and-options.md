---
id: editors.graph-editor.footer-tools-and-options
title: Footer tools and options
section: editors
path:
  - Editors
  - Graph Editor
  - Footer tools and options
version: "5.1"
status: draft
screenshots: "5.1"
source:
  - 18.4 Editors - Graph Editor - Footer tools and options.odt
---
## Introduction

This chapter here is about the tools and options elements in the footer. It contains various elements and tools. This footer is shared across the animation editors. Dope Sheet, Graph Editor, Driver Editor and NLA Editor.

![Introduction](/docs2/images/editors/graph-editor/footer-tools-and-options/introduction.png)

## Playback Elements

![Playback Elements](/docs2/images/editors/graph-editor/footer-tools-and-options/playback-elements.png)

The playback elements allows you to play your animation, and set the animation range.

### Jump Time by Delta

Jump forward or backward by a given number of frames or seconds.

#### Time Jump Delta

The amount to step forward or backward.

#### Jump Unit

![Jump Unit](/docs2/images/editors/graph-editor/footer-tools-and-options/jump-unit.png)

The frame jump unit. Seconds or Frames.


| Entry | What it does |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Jump to Endpoint - start | Jumps to the first frame. |
| Jump to Keyframe - previous | Jumps to the keyframe before the current position. |
| Play Animation - backward | Plays the animation in reverse direction. |
| Play Animation - forward | Plays the animation. |
| Jump to Keyframe - next | Jumps to the keyframe after the current position. |
| Jump to Endpoint - end | Jumps to the last frame. |
| Cancel animation | Cancels the animation and returns to the original frame. |
| Current Frame | The edit box with the position of the current frame. Click at the value and type in another value to jump to another frame. |


### Use Preview Range

![Use Preview Range](/docs2/images/editors/graph-editor/footer-tools-and-options/use-preview-range.png)

Toggle an alternative range used to preview animations. The Preview range works for the UI playback, but will not work for rendering an animation.

The preview range is displayed in orange color. The original playback range that is used for rendering is still displayed in grey underneath. When Use Preview Range is on, then the animation will loop between the Preview range.

### Set Start Frame

![Set Start Frame](/docs2/images/editors/graph-editor/footer-tools-and-options/set-start-frame.png)

Sets the current frame position as the start frame.


| Entry | What it does |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Start | The start frame for the animation in current mode. |
| End | The end frame for the animation in current mode. |
| Set End Frame | Sets the current frame position as the end frame. |
| Insert Keyframe | Inserts a keyframe. If you do not have a keying set assigned, this will default to the default keying set defined in the Preferences. |
| Delete Keyframe | Removes the keyframe at the current position in the current active keying set. |


## Playhead Snapping

![Playhead Snapping](/docs2/images/editors/graph-editor/footer-tools-and-options/playhead-snapping.png)

Playhead controls in animation editors help position the current frame indicator with precision, improving navigation and editing across the Timeline, Dope Sheet, Graph Editor, NLA, and Video Sequencer.


| Entry | What it does |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Snap Distance | Sets the snapping threshold in pixels. Determines how close the playhead must be to a target for snapping to occur. |
| Snap Target | **Frames**: Snaps to whole frame numbers. Ideal for frame-accurate editing instead of sub-frame cursor placement. · **Seconds**: Snaps to time intervals measured in seconds. Useful for audio syncing or time-based pacing. · **Markers**: Snaps to the closest timeline marker. Great for aligning actions to scene events or beats. · **Keyframes**: Snaps to keyframe positions. Ensures precise alignment for editing and playback. · **Strips**: Snaps to the start or end of video/audio strips. Useful in the Video Sequencer and NLA editor. |


### Frame Step

![Frame Step](/docs2/images/editors/graph-editor/footer-tools-and-options/frame-step.png)

Defines the step size for frame-by-frame navigation. Controls how far the playhead moves when stepping through frames manually.

> **Note:** Only available with Frames Snap Target

### Second Step

Defines the step size for second-by-second navigation. Controls how far the playhead moves when stepping through the timeline manually.

> **Note:** Only available with Second Snap Target

## Active Keying Set

![Active Keying Set](/docs2/images/editors/graph-editor/footer-tools-and-options/active-keying-set.png)

Objects needs a so called keying set so that you can record animation for it. It is a container for the animation, a set of keyframe channels. When you try to record an animation without an existing keying set, then you will get a warning since the channels for the keyframes are missing.

In this property you can choose a method from the builtin keying sets.

### Auto Keying

With auto keying on every manipulation in the 3d view will automatically create a keyframe, or update the existing keyframe at the current position.

Note that Auto Keying just works with transform properties ( Objects and Bones) in the 3d View. It will not work to animate colors in the Properties Editor for example.

### Auto Keyframing Popover

![Auto Keyframing Popover](/docs2/images/editors/graph-editor/footer-tools-and-options/auto-keyframing-popover.png)

Auto keying settings. These settings shows when you have auto keying activated.


| Entry | What it does |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Auto keying mode | **Add & Replace**: Replace existing keyframes and add new ones where no keyframes exists. · **Replace**: Just replace existing keyframes. |
| Only Active Keying Set | Automatic keyframe insertion using active keying set only. |
| Layered Recording | Add a new nla track and strip for every loop or pass made over the animation. This allows non destructive tweaking. |
| Cycle aware keying | For channels with cyclic extrapolation, the keyframe insertion is automatically remapped inside the cycle time range, and keeps the ends in sync. |


### Active Keying Set

![Active Keying Set](/docs2/images/editors/graph-editor/footer-tools-and-options/active-keying-set-2.png)

Choose your keying set.

## Playback Panel

![Playback Panel](/docs2/images/editors/graph-editor/footer-tools-and-options/playback-panel.png)

Here you can find various options for playback.

### Audio

#### Sync Mode

![Sync Mode](/docs2/images/editors/graph-editor/footer-tools-and-options/sync-mode.png)

How to synchronize playback.


| Entry | What it does |
| -------------- | --------------------------------------------- |
| No Sync | Don't synchronize. Play every frame. |
| Frame Dropping | Drop frames if playback is too slow. |
| AV Sync | Drop frames to synchronize to Audio Playback. |


| Entry | What it does |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Scrubbing | Play existing audio from sequence editor when scrubbing. |
| Play Audio | Play back existing audio from sequence editor, otherwise mute the audio when deactivated. Use the Sequence Editor to add audio. |


### Playback


| Entry | What it does |
| ----------------------------- | --------------------------------------------------------------------- |
| Limit Playback to Frame Range | Don't allow frame selection with the mouse outside of the play range. |
| Follow Current Frame | Follow current frame in editors. |


### Play in

![Play in](/docs2/images/editors/graph-editor/footer-tools-and-options/play-in.png)

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

### Show Subframes

Display and allow setting fractional frame values for the current frame.

## Keying Panel

![Keying Panel](/docs2/images/editors/graph-editor/footer-tools-and-options/keying-panel.png)

Some more keying options.

### New Keyframe Type

![New Keyframe Type](/docs2/images/editors/graph-editor/footer-tools-and-options/new-keyframe-type.png)

Recolor the currently selected keyframes. Or create the next keyframe with this chosen keyframe color.

### Auto Keyframing

![Auto Keyframing](/docs2/images/editors/graph-editor/footer-tools-and-options/auto-keyframing.png)


| Entry | What it does |
| ------------------------------- | -------------------------------------------------------------- |
| Auto Keying Mode | Just replace existing keyframes, or add keyframes too. |
| Auto Keyframe Insert Keying Set | Automatic Keyframe Insertion using the active keying set only. |


| Entry | What it does |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Layered Recording | Add a new NLA Track and Strip for every loop/ pass made over the animation to allow non destructive tweaking. |
| Cycle Aware Keying | For channels with cyclic extrapolation, keyframe insertion is automatically remapped inside the cycle time range, and keeps the ends in sync. |


## Options

![Options](/docs2/images/editors/graph-editor/footer-tools-and-options/options.png)


| Entry | What it does |
| ------------------ | ------------------------------------------------------- |
| Only show errors | Only include f-curves that are disabled or have errors. |
| Only show selected | Just show the keyframes from the selected object. |


### Show Seconds

![Show Seconds](/docs2/images/editors/graph-editor/header/header-tools-and-options/show-seconds.png)

Show the timing in the timeline area in seconds instead of frames.


| Entry | What it does |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sync visible range | Synchronize the visible timeline range with other visible time based editors. When you zoom in or out in the one editor, then it zooms in or out in the other editor too. Each editor to sync needs to have Sync Visible Range ticked. |
| Show Markers | Display the markers row at the bottom of the view. |
| Lock Markers | Make the markers uneditable. |
| Show Cache | Show animation information for cached objects like Particles. · **Softbody, Particles, etc.**: Include or exclude what kind of cache types you want to display. |


