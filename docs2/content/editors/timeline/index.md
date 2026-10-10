---
id: "editors.timeline"
title: "Timeline"
section: "editors"
path: ["Editors", "Timeline"]
icon: "time"
version: "5.1"
status: "draft"
screenshots: "5.1"
source: ["17 Editors - Timeline.odt"]
---

The **Timeline** is the editor for playing and recording animation. It is one of the five editors that work with animation data.

Usually you only see its header. Drag the top border of the editor upwards to show the rest.

:::hotspots{img=/docs2/images/ui/timeline/timeline.png}
- **Header** · green: playback, keying and the menus. See [Timeline header](header.md).
- **Channel list** · yellow: hidden by default. Click the small button at the top left to show it. See [Channel list](channel-list.md).
- **Viewport** · no colour: the frames, keyframes and markers. See [Viewport](viewport.md).
:::

The header has three parts:

:::hotspots{img=/docs2/images/ui/timeline/timeline-3.png}
- **Menus** · yellow
- **Playback tools** · green
- **Options** · blue
:::

## What the viewport shows

| Element | What it is |
|---|---|
| ![](/docs2/images/ui/timeline/time-cursor.png){.icon} **Time cursor** | The green line. It shows and sets the current frame. |
| **Keyframes** | Shown as one diamond shape for every keyframe type. The Dope Sheet shows the types separately. |
| **Markers** | Labels on important frames, for example where an action starts or a camera moves. They sit at the bottom of the viewport. |

## Markers

![Markers](/docs2/images/ui/timeline/markers.png){.right}

- Add, delete and rename markers in the [Marker menu](header.md#marker-menu).
- Click a marker to select it. Drag it to move it.
- The **active marker** is highlighted and shows a dotted line upwards.
- When the current frame is on a marker, the 3D Viewport shows the marker name in its info text.
