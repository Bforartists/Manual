# 🧪 Spike 1 · Extraction and migration test: results

**Verdict: ✅ conversion works.** The `.odt` manual turns into clean, structured Markdown automatically. The converter is ready to scale once it has a page map for every chapter, an icon map and an alt-text pass.

Branch `docs2/spike1-migration`, from `master` at `a8edc2d` (v5.1.1, "Version bump"). `master` is untouched.

## 📦 What went in, what came out

| | In | Out |
|---|---|---|
| ⏱️ Timeline | 6 `.odt` files | 4 pages + 2 shared snippets |
| 🪟 Interface | 1 `.odt` file | 7 pages (basics, input devices, 5 interface components) |
| 🔧 Modifiers tab | 11 `.odt` files | 10 pages (overview + 5 Mesh + 4 Grease Pencil categories) |
| 🖼️ Images | 587 image files | 534 unique files, 10 MB, largest 1920 px, none over the 4 MB API limit |

Pages follow the artist route: `content/editors/properties/modifiers/mesh/generate.md` instead of `26.9.4 Editors - Properties Editor - Modifiers Properties Tab - Add Modifiers menu - Generate modifiers.odt`.

## 🔧 How the converter handles the hard cases

| Found in the `.odt` files | Count | What the converter does | Status |
|---|---|---|---|
| Headings inside 1-cell "banner" tables (Pandoc drops them) | 54 tables | Unwraps the table so the heading survives | ✅ Solved |
| Title tables (icon + "17 Editors - Timeline") | 18 | Read as the file title, then dropped; the page title comes from the page map | ✅ Solved |
| "Detailed table of content" sections | 10 | Removed; the sidebar builds this | ✅ Solved |
| Headings that are only a picture or blank | 21 | Picture kept as content, empty heading removed | ✅ Solved |
| Heading icons and screenshots inside headings | 402 | Moved under the heading as a floated image | ✅ Solved |
| Very deep headings (up to 8 levels, Array modifier) | 12 deeper than H6 | Become bold labels | ✅ Solved |
| Short entries ("Zoom In · Zooms in") | 952 | Folded into 268 tables ("Menu entry / What it does", "Property / What it changes"); settings with choices become one row | ✅ Solved |
| "Note:" / "Hint:" paragraphs | 56 | Become `:::note` / `:::tip` callouts | ✅ Solved |
| Modifiers (Array, Bevel, …) | 83 | Get a `::tool{id=…}` card tag | ⚠️ IDs are guesses; the extractor must supply the real ones (`ArrayModifier`) |
| Colour-coded screenshots ("Header ( Green )") | 2 with a figure | Become `:::hotspots` with labels and colours | ⚠️ Hover boxes come later from the capture script |
| Hotkeys in text | 15 tagged | `Ctrl + Space` → `:kbd[Ctrl+Space]` | ⚠️ Prose like "Hotkey A" or "Alt A" is missed; fix by hand or from extractor data |
| Images by place | 534 | Named by page and heading (`ui/timeline/header/playhead-snapping.png`), stored once | ⚠️ Several images under one heading get `-2`, `-3`; alt text is the heading name |
| Real data tables | 2 | Kept as tables | ✅ |

## ♻️ Repeated content (snippet candidates)

The scan (`reports/repeats.json`) compared 370 sections and found **23 groups of near-identical text, about 2,200 words**. Almost all are Mesh and Grease Pencil modifiers that share settings:

| Repeated section | Copies |
|---|---|
| Influence subpanel (Grease Pencil color, deform, generate) | 4 |
| Array (Mesh, Mesh legacy, Grease Pencil) | 3 |
| Hook, Lattice, Project, Bone Envelopes, Vertex Group, Falloff, Custom Curve | 2 each |

Each group becomes one snippet. The Quick menu and Marker menu snippets are already built.

## ✂️ Trim test: Timeline chapter

Commit 2 trims the converted Timeline chapter by hand, following the writing style rules. Compare commit 2 with commit 1 in VS Code to see every cut.

| Page | Words before → after | Images before → after |
|---|---|---|
| Timeline (overview) | 271 → 203 | 4 → 2 |
| Header | 1,515 → 890 | 24 → 12 |
| Channel list | 536 → 338 | 13 → 8 |
| Viewport | 514 → 278 | 12 → 1 |
| Quick menu snippet | 519 → 195 | 6 → 2 |
| Marker menu snippet | 308 → 191 | 6 → 2 |
| **Total** | **3,663 → 2,095 (−43%)** | **65 → 27** |

Where the fat came from:

- 🔁 Repeats: snapping and the Quick menu were explained in 2–3 places. Now one place and a link.
- 📋 Prose lists of menu entries and settings: now tables.
- 🗣️ Wordy sentences: "The Time Cursor is the green line. It is used to set and display the current time frame." became "The green line. It shows and sets the current frame."
- 🖼️ Submenu screenshots that only repeat the table next to them.

**Your call:** the trim dropped 38 image placements (37 files), mostly screenshots of submenus. They stay in the image library. Keep submenu screenshots, or rely on tables plus fresh recipe screenshots?

## 🚧 Before converting all 517 files

1. 🗺️ **Page map for every chapter.** `tools/pages.json` is hand-written for these 3 chapters. Generate most of it from the file names (they already hold editor › area › object type › mode).
2. 🎨 **Icon map.** Front matter has no `icon` yet; map heading icons to the icon library by image hash.
3. 🔤 **Alt text and image names.** One pass, human or agent, per chapter.
4. 🔗 **Links between pages.** The `.odt` files have almost none; add "see also" links when trimming.
5. ✍️ **Spell check in CI.** Source typos came across ("Phyiscs", "equlaly", "Modifers").
6. 🏷️ **Stale titles.** 26.9 still says "25.8 … Modifiers Tab"; 26.9.6 is titled "Deform" but holds Physics. The page map fixes titles, so nothing depends on them.
7. 🧪 **Webflow tables.** Rich text has no tables, and the output uses many. Phase 0 must settle the table component.

## ✏️ Online editing (for Spike 2)

- `.pages.yml` in the repository root sets up **Pages CMS**: a page tree like the sidebar, a form for the front matter, a rich-text editor for the body, and the image library.
- The wiki drafts in `dev-docs/` explain how to edit online: Pages CMS, github.dev, or the GitHub pencil.
- **Open question for Spike 2:** does the rich-text editor keep `:::tip`, `:kbd[…]`, `::tool{…}` and `{.right}` exactly as typed? If not, the fallback is Source mode for tagged pages, or simpler tags.

## 🗂️ Commits on this branch

1. `Docs 2.0 Spike 1: convert …`: automatic output, converter and reports
2. `Docs 2.0 Spike 1: trim the Timeline chapter by hand`: the trim test
3. `Docs 2.0 Spike 1: online editing setup and report`: `.pages.yml`, wiki drafts, this report
