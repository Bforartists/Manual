---
id: "editors.timeline.header"
title: "Timeline header"
section: "editors"
path: ["Editors", "Timeline", "Header"]
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17.1.1 Editors - Timeline - Header Tools and Options.odt", "17.1.2 Editors - Timeline - Header - Quick Menu.odt", "17.1.3 Editors - Timeline - View Menu.odt", "17.1.4 Editors - Timeline - Marker Menu.odt"]
---

![Timeline header](/docs2/images/ui/timeline/header/introduction.png)

The header holds the menus, the playback controls and the playback and keying options.

## Playback controls

![Playback controls](/docs2/images/ui/timeline/header/playback-elements.png)

Play the animation and set its frame range.

| Control | What it does |
|---|---|
| ![](/docs2/images/ui/timeline/header/time-jump-delta.png){.icon} **Time Jump Delta** | How far a jump goes. **Jump Unit** sets frames or seconds |
| Jump to Endpoint (start / end) | Jumps to the first or the last frame |
| Jump to Keyframe (previous / next) | Jumps to the nearest keyframe before or after the current frame |
| Play Animation (backward / forward) | Plays the animation in reverse, or forwards |
| Cancel Animation | Stops playback and returns to the frame you started from |
| Current Frame | The current frame number. Type a number to jump there |
| ![](/docs2/images/ui/timeline/header/set-start-frame.png){.icon} Set Start Frame / Set End Frame | Makes the current frame the start or the end of the range |
| Start / End | The first and last frame of the range |
| Insert Keyframe | Inserts a keyframe for the active keying set. Without one, it uses the default keying set from the Preferences |
| Delete Keyframe | Deletes the keyframe at the current frame in the active keying set |

### Preview range

![Use Preview Range](/docs2/images/ui/timeline/header/use-preview-range.png){.right}

**Use Preview Range** sets a second, temporary range for playback in the interface. Rendering still uses the normal range.

The preview range is drawn in orange, with the render range in grey underneath. Playback loops inside the preview range while it is on.

## Keying

![Active Keying Set](/docs2/images/ui/timeline/header/active-keying-set.png){.right}

To record animation, an object needs a **keying set**: a group of channels that keyframes are written into. Without one, recording shows a warning. Choose a built-in keying set in **Active Keying Set**.

**Auto Keying** inserts or updates a keyframe at the current frame every time you transform something in the 3D Viewport.

:::note
Auto Keying works for transforms of objects and bones in the 3D Viewport only. It does not key, for example, a colour in the Properties Editor.
:::

### Auto Keying popover

![Auto Keying popover](/docs2/images/ui/timeline/header/auto-keyframing-popover.png){.right}

Shown while Auto Keying is on.

| Option | What it does |
|---|---|
| Auto Keying Mode | **Add & Replace**: adds new keyframes and replaces existing ones<br>**Replace**: only replaces existing keyframes |
| Only Active Keying Set | Inserts keyframes for the active keying set only |
| Layered Recording | Adds a new NLA track and strip on every pass, so you can tweak without losing earlier passes |
| Cycle Aware Keying | On cyclic channels, keeps new keyframes inside the cycle so both ends stay in sync |

## Playback popover

![Playback popover](/docs2/images/ui/timeline/header/playback-panel.png){.right}

| Option | What it does |
|---|---|
| Sync Mode | **No Sync**: plays every frame<br>**Frame Dropping**: skips frames when playback is too slow<br>**AV Sync**: skips frames to stay in sync with the audio |
| Audio Scrubbing | Plays the audio while you drag the time cursor |
| Play Audio | Plays the audio from the Video Sequencer. Off mutes it |
| Sub-frames | Shows the scene sub-frame and lets you set it |
| Limit Playback to Frame Range | Stops you from selecting frames outside the range |
| Follow Current Frame | Scrolls the editors with the current frame |
| Play In | Which editors update during playback: Active Editor, 3D Viewport, Animation Editors, Image Editor, Properties and Sidebars, Movie Clip Editor, Node Editors, Video Sequencer, Spreadsheet |

## Playhead snapping

![Playhead snapping](/docs2/images/ui/timeline/header/playhead-snapping.png){.right}

Snaps the time cursor while you drag it in the Timeline, Dope Sheet, Graph Editor, NLA Editor and Video Sequencer.

| Option | What it does |
|---|---|
| Playhead Snapping | Turns snapping on or off. Hold :kbd[Ctrl] while dragging to flip it for a moment |
| Distance | How close, in pixels, the cursor must come before it snaps |
| Snap Target | **Frames**: whole frames<br>**Seconds**: whole seconds, useful for audio<br>**Markers**: the nearest marker<br>**Keyframes**: the nearest keyframe<br>**Strips**: the start or end of a strip in the NLA Editor or Video Sequencer |
| Frame Step | How many frames one step moves. Only with the Frames target |
| Second Step | How many seconds one step moves. Only with the Seconds target |

## Keying popover

![Keying popover](/docs2/images/ui/timeline/header/keying-panel.png){.right}

| Option | What it does |
|---|---|
| New Keyframe Type | The colour type for new keyframes. It also recolours the selected ones |
| Auto Keying Mode | Replace existing keyframes only, or add new ones too |
| Only Active Keying Set | Auto Keying uses the active keying set only |
| Layered Recording | See [Auto Keying popover](#auto-keying-popover) |
| Cycle Aware Keying | See [Auto Keying popover](#auto-keying-popover) |

## View options

![Options](/docs2/images/ui/timeline/header/options.png){.right}

| Option | What it does |
|---|---|
| Only Show Errors | Shows only F-Curves that are disabled or have errors |
| Only Show Selected | Shows only the keyframes of selected objects |
| Show Seconds | Shows time in seconds instead of frames |
| Sync Visible Range | Zooms and scrolls together with other time editors that also have this on |
| Show Markers | Shows the marker row at the bottom |
| Lock Markers | Markers cannot be edited |
| Show Cache | Shows cached frames, for example of particles. Choose which cache types to show |
| Show Overlays | Turns the Dope Sheet overlays on or off. **Show Scene Strip Range** shows the range of the current scene strip when you sync scene time in the Video Sequencer |

## Quick menu

::include{snippet=quick-menu}

## View menu

![View menu](/docs2/images/ui/timeline/header/view-menu.png){.right}

| Menu entry | What it does |
|---|---|
| Adjust Last Operation | Shows the panel for the last operation, at the bottom left |
| Channels | Shows the channel list on the left |
| Zoom In / Zoom Out | Zooms the view |
| Zoom Border | Draw a box to zoom to it |
| Frame All | Fits everything in the view |
| Go to Current Frame | Centres the view on the time cursor |
| Frame Scene Range | With Use Preview Range off, fits the scene range |
| Frame Preview Range | With Use Preview Range on, fits the preview range |
| Area › | Split, duplicate, maximise or close the area. Same in every editor |

## Marker menu

::include{snippet=marker-menu}
