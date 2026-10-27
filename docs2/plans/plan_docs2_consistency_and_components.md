# 🧭 Docs 2.0 consistency and components: audit and plan

> Measured on `master` (333 pages), 26 Oct 2026. Numbers come from scripts, not estimates.

---

## 1. 🔎 What the audit found

| | Finding | Count |
|---|---|---|
| 📄 | Pages | 333 |
| 📊 | Tables in the manual | **4,545** on **235** pages (about 26,000 table lines) |
| 📊 | …of those, "Entry / What it does" (operators and settings in a grid) | 4,170 |
| 📊 | …"Property / What it changes" | 257 |
| 📊 | …"Action / Keys" (real data grid) | 69 |
| 🔠 | Bold lines used instead of a heading | 557, mostly in 8 pages (Object header 48, GP Draw 39, GP Sculpt 39, Header tools 37) |
| 🪜 | Pages that skip a heading level (`##` to `####`) | 37 (Geometry nodes Node Groups: 20 skips) |
| 🖼️ | Pages with no picture | 54 |
| 🔁 | "Last Operator …" sections | **840** |

### 🔁 Adjust Last Operation (the "Repeat last" panels)

The biggest pattern in the manual, and the least consistent.

| State of the 840 sections | Count |
|---|---|
| Picture only: no sentence, no table | 364 |
| Picture and table, no sentence | 239 |
| No picture, no sentence, no table | 100 |
| Picture and a sentence | 69 |
| Picture, sentence and table (**the target**) | 40 |
| No picture, table | 21 |
| No picture, a sentence | 7 |

- ✅ Only **116 of 840** have an explanation. **128** have no picture at all.
- 🏷️ The headings are named three ways: "Last Operator Move", "Last operator Move", "Adjust Last Operation". Rename them all to the name the UI uses.
- 🪆 They are nested one level under the operator in 839 of 840 cases. Good, that is the shape we want.

### 🔌 Node pages (Inputs / Properties / Outputs)

491 node blocks across Geometry, Shader and Compositor.

- ✅ **The order is already consistent**: Inputs, Properties, Outputs. Only 3 break it.
- ✅ Properties are sub-headings in 166 of 190 cases. Only 17 are tables and 7 are plain text.
- 👉 Nodes are the **model** for the rest of the manual. Little work needed here.

### 📊 Where the tables are

Top pages: 3D Viewport Mesh Edit header (110), Object header (106), Mesh Sculpt sidebar (101), Topbar menus (91), Geometry nodes Utilities (88), Header tools (83), View Layer tab (78), Select menu (76).

---

## 2. ♻️ Repeated content

### The big ones

These are **sections** that repeat, measured by heading name.

| Block | Copies | Pages | Words | Different versions |
|---|---|---|---|---|
| 📐 Proportional Editing | 149 | 27 | 12,500 | 22 |
| 🧭 Orientation | 165 | 29 | 4,600 | 41 |
| 🪞 Mirror Editing | 86 | 24 | 500 | 12 |
| 🖱️ Drag | 68 | 16 | 5,100 | **6** |
| 🧭 Navigation elements | 60 | 29 | 7,400 | 32 |
| 🔢 Header values | 36 | 11 | 2,200 | 13 |

**86 of the 149 Proportional Editing copies, 93 Orientation and 44 Mirror Editing sit inside Adjust Last Operation sections.** Every transform operator (Move, Rotate, Resize, Shear, To Sphere, Push/Pull …) repeats the same properties. This is the single best place to start.

### Paragraphs copied between pages

| Block | Pages |
|---|---|
| ⭐ Quick Favorites (9 to 14 paragraphs each) | 13 |
| 🖌️ Grease Pencil brush asset panel, Stroke panel, pressure curves | 6 to 12 |
| 📈 Curve widget | 15 |
| 🔒 Snapping sliders | 13 |
| ✂️ Shear, To Sphere, Mirror, Snap, axis constraint | 7 to 12 each |
| 📝 Annotation tool and layers | 7 + 8 |
| 🧱 Node editors: Frame node, node groups, collapse, sidebar item move | 3 to 7 |
| 🎞️ Animation editors: channel list, markers, extrapolation, playback range | 4 to 8 |
| 🧊 Cache panels (physics, particles) | 5 |
| 🖼️ Image settings (32 bit float, image type, UDIM) | 3 to 7 |
| ⬜ Duplicate Area into New Window, Legacy submenu, pie menu list | 8 to 11 |

### ⚠️ Half-finished earlier work

The Phase 3 back-link script added "See … in the Interface chapter" lines to 12 to 13 pages, **but the copied text is still there** (for example all of the Quick Favorites paragraphs on the Compositor header). The link and the copy now sit side by side.

---

## 3. 🤔 Is moving shared content into Interface "components" a good idea?

**Yes, for part of it. And the repo already has a second tool, so we should pick the right one for each case.**

| | ♻️ Shared section (exists) | 🧩 Interface component page (proposed) |
|---|---|---|
| What readers see | Full text, in place, on every page | A short callout, a capture of the local variant, a link |
| Best for | An **identical panel or menu** (Quick menu, Marker menu) | A **concept** that needs a proper explanation (proportional editing, curve widget) |
| Reader has to leave the page | No | Yes, if they want the detail |
| Page length | Unchanged | Shorter |
| Fixes in one place | Yes | Yes |
| Handles variants | No (one text for all) | Yes ("common" part plus a note per context) |

### 👍 Why components help
- No content drift: 22 versions of Proportional Editing become one.
- Faster pages for artists to scan, and a real destination for "what is proportional editing?" searches.
- Fewer places to update when the UI changes.

### ⚠️ What to watch
- 🧭 Docs 2.0's own guide says "readers never follow a link to another chapter". Concept components **reverse that for concepts only**. Needs a yes from you.
- 🔍 Variants are real: 22 versions are not 22 typos. Some differ because the context differs (edit mode vs object mode). Each must be reviewed before it is merged, not auto-deleted.
- 🖼️ Each page keeps **its own capture** so the reader still sees the panel they are looking at.
- 🔗 Links must be checked automatically (the docs check already catches broken links).

### ✅ Recommendation: a simple rule

> **Reader needs it to operate this panel, and the text is identical?** → Shared section, shown in full.
> **It explains an idea used in many places?** → One Interface page. Callout + link everywhere else.

**Home (decided):** no new pages and no new group. Each component becomes a **section on the Interface page where it belongs** (for example Properties, Floating menus, Last Operator panel, Windows), so it shows up as a right-sidebar group of that chapter. Each section ends with a "Used in" list from the back-link tool. This makes the Interface chapter richer instead of bigger.

---

## 4. 🗺️ Component map

| # | Component | Type | Home | Where it is copied |
|---|---|---|---|---|
| 1 | 📐 Proportional Editing | 🧩 Component | Last Operator panel page → Common properties | 149 sections, 27 pages, mostly transform operators |
| 2 | 🧭 Orientation and Constraint Axis | 🧩 | same | 165 sections |
| 3 | 🪞 Mirror Editing | 🧩 | same | 86 sections |
| 4 | 🖱️ Drag | ♻️ or 🧩 | relevant Interface page (new section) | 68 sections, only 6 different texts |
| 5 | 🧭 Navigation elements, Header values | 🧩 | relevant Interface page (new section) | 60 + 36 sections |
| 6 | ⭐ Quick Favorites (finish) | ♻️ + 🧩 | exists: floating-menus.md + snippet | 13 pages |
| 7 | 📈 Curve widget, 🔒 Snapping | 🧩 | exists: properties.md | 15 + 13 pages (remove leftover copies) |
| 8 | 🖌️ Brush settings (asset panel, Stroke, pressure curves, clipping, falloff) | 🧩 | Interface › Brush settings | GP Draw/Sculpt/Vertex, Mesh Sculpt/Paint, Hair |
| 9 | 📝 Annotation (tool + layers) | 🧩 | Interface › Annotations | 7 tool shelves, 8 sidebars |
| 10 | 🧱 Node editor common (Frame, groups, collapse, tabs, sidebar) | 🧩 | Node editors overview | Compositor, Shader, Geometry |
| 11 | 🎞️ Animation editor common (channel list, markers, extrapolation, playback range, playhead, F-curve modifiers) | ♻️ + 🧩 | Interface › Animation editors | Dope Sheet, Graph, Drivers, NLA, Timeline |
| 12 | 🧊 Cache panel | ♻️ | snippet | 5 physics and particle pages |
| 13 | 🖼️ Image settings | 🧩 | Interface › Images | Image Editor, Compositor, Texture tab |
| 14 | ⬜ Editor header basics (Duplicate Area, Legacy submenu, pie list, editor type) | ♻️ | snippets | 8 to 11 header pages |
| 15 | 🗂️ Asset properties (Catalog …) | 🧩 | Assets | 10 pages |

---

## 5. 🛣️ Plan: chunks, one task and one PR each

Each chunk is small enough to review in one sitting. Every chunk gets a tracker issue first, then a PR.

### Phase A, the base (this week)
| # | Chunk | Why first |
|---|---|---|
| A1 | 📐 Formatting standard (this PR) | The rule everyone follows |
| A2 | 🧪 Style check in `check.py` (warnings, no failures): level skips, bold-as-heading, tables outside allowed cases, Last Operator without sentence or picture | Progress becomes a number |
| A3 | 🪜 Fix the 37 level skips | Mechanical, quick win |

### Phase B, Adjust Last Operation
| # | Chunk |
|---|---|
| B1 | 🏷️ Rename all "Last Operator X" to "Adjust Last Operation" (script, 840 headings, anchors checked) |
| B2 | 📐 Common properties on the Last Operator page: Proportional Editing, Orientation, Mirror Editing, Snap |
| B3 | ✂️ Transform operators: replace the repeated blocks with only their own properties plus a link (3D Viewport Object, Mesh Edit, Curve, Armature, Lattice, GP, Hair) |
| B4 | 📝 Add the missing sentence and capture, area by area (UV Editor, Image, Sequencer …) |

### Phase C, tables to headings
Same rule as the Strip tab (#1507). About 10 pages per PR, biggest first.
C1 3D Viewport headers · C2 Node add menus · C3 Properties tabs and modifiers · C4 other editors headers · C5 Topbar, Toolbar, Preferences · C6 bold lines to headings.

### Phase D, components
D1 Quick Favorites, curve widget, snapping (finish the unfinished back-links) · D2 Drag, Navigation elements, Header values · D3 Brush settings · D4 Annotations · D5 Node editor common · D6 Animation editor common · D7 Cache, Image settings, Editor header snippets, Asset properties.

### 🗓️ Suggested week
| Day | Work |
|---|---|
| Tue | A1 review, A2, A3 |
| Wed | B1, B2 |
| Thu | B3 (two PRs) |
| Fri | C1, D1 |
| Next week | B4, C2 to C6, D2 to D7 |

One rule for sequencing: **Phase B2 before B3 before anything touching the same pages**, so nobody fixes a table that is about to be deleted.

---

## 6. ✅ Decisions (answered 26 Oct)

1. 🏷️ **"Adjust Last Operation"** is the heading for every redo panel (it is the UI name).
2. 🧩 **Link components for concepts: yes.** Less bloat, depth stays discoverable, and readers are not made to re-read the same thing. The "never leave the page" rule existed because search and hyperlinks were not possible in the old docs.
3. 📁 **No new group or pages.** Components become sections inside the existing Interface pages, in the area where they belong, so they appear as right-sidebar groups of that chapter.
4. 🔔 **Style check: warnings only.** It never fails the build.
