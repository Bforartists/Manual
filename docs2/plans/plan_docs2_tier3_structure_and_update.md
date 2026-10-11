# Bforartists Docs 2.0 — Tier 3: Structure, Consolidation and the 5.3 Update

> 🎯 **Goal of this tier:** turn the faithfully migrated manual (≈ 520 small pages) into **about 100 rich chapters**
> that load once and can be explored deep, bring every page up to **Bforartists 5.3**, and write the content that is
> missing. This is where the Refine phase starts: trimming and rewording are allowed from here on (D13 ends).

**Date**: 2026-10-10

**Status**: 📝 Draft for your review

**Depends on**: Tier 2 (`plan_docs2_tier2_full_manual.md`): the whole manual converted and syncing to Webflow

**Blocks**: retiring the `.odt` manual for good; the 5.3 release documentation

**Branch**: `docs2/main`; one `docs2/t3-<chapter>` branch per consolidated chapter, merged by pull request

**Estimated scope**: ≈ 520 pages → **≈ 90–100 chapters** · 1 keymap redesign · 1 interface diff 5.1 → 5.3 ·
new pages for 5.2/5.3 features · Quick Start, Comparing to Blender, Migrating from Blender written

**Companion docs**: [Tier 1](plan_docs2_tier1_getting_started.md) · [Tier 2](plan_docs2_tier2_full_manual.md) ·
Wiki: [Plain writing](../dev-docs/Plain-writing.md) (sub-chapters and icons)

---

## 🔭 At a glance

| Level | What Tier 3 does |
|---|---|
| 🏔️ **Big picture** | From 500 small pages to ~100 big chapters, up to date with 5.3, with the missing content written |
| 🧱 **How** | Writers keep **small source files**; the website **assembles** each chapter into **one long page** with sub-chapters. Keymap rebuilt from data. A 5.1 → 5.3 interface diff makes the to-do list |
| 📏 **Proof it works** | A size and speed test with the largest chapters before anything is consolidated |

---

## Table of Contents

1. [Summary](#1-summary)
2. [The Problem We Are Solving](#2-the-problem-we-are-solving)
3. [Where We Start From](#3-where-we-start-from)
4. [Design Decisions](#4-design-decisions)
5. [Big Pages: Viability](#5-big-pages-viability)
6. [Architecture](#6-architecture)
7. [Implementation Plan](#7-implementation-plan)
   - [Phase 0 — This Document](#phase-0--this-document)
   - [Phase 1 — Big Page Test](#phase-1--big-page-test)
   - [Phase 2 — Target Structure (~100 Chapters)](#phase-2--target-structure-100-chapters)
   - [Phase 3 — Assemble the Chapters](#phase-3--assemble-the-chapters)
   - [Phase 4 — Keymap Redesign](#phase-4--keymap-redesign)
   - [Phase 5 — 5.3 Audit: What Changed](#phase-5--53-audit-what-changed)
   - [Phase 6 — First Pass to 5.3, New Content](#phase-6--first-pass-to-53-new-content)
   - [Phase 7 — Trim and Reword](#phase-7--trim-and-reword)
8. [Files Touched](#8-files-touched)
9. [Verification Plan](#9-verification-plan)
10. [Risks & Mitigations](#10-risks--mitigations)
11. [Out of Scope](#11-out-of-scope)
12. [Open Questions](#12-open-questions)

---

## 1. Summary

Tier 2 moves the manual as it is: one `.odt` file → one page, ≈ 520 pages. That is faithful, but the index is far
too long for a reader. Tier 3 reshapes it:

1. 🧱 **Structure** — about 100 chapters: one per editor, workspace set, interface topic, properties tab. Each
   chapter is **one long page** that loads once; sub-chapters (`#` headings with icons) and the right-side panels
   make it easy to explore deep.
2. ✍️ **Writers keep small files.** A chapter is a folder of small Markdown files (the Tier 2 pages). The build
   **assembles** them into one web page. Editing stays light in Pages CMS; readers get the big page.
3. ⌨️ **Keymap redesign** — hotkey tables generated from Bforartists' own keymap, each with a short description and a
   link to where the operator is documented.
4. 🆕 **5.3** — an automatic interface diff (menus, panels, operators) between 5.1 and 5.3 becomes the update list;
   a first pass brings every chapter up to date and adds pages for new features.
5. ✂️ **Refine** — trimming duplicates, rewording, and the missing pages (Quick Start, Comparing, Migrating).

---

## 2. The Problem We Are Solving

| # | After Tier 2 | Effect | Tier 3 answer |
|---|---|---|---|
| P1 | ≈ 520 pages, one per `.odt` file | A huge sidebar; similar ideas scattered | ≈ 100 assembled chapters |
| P2 | Each page reloads to read the next menu | Exploring is slow and choppy | One long page per chapter, loads once |
| P3 | Standard Keymap: 35,779 words in 368 tables | Hard to scan; no link to where an operator lives | Generated tables, one-line descriptions, links to the operator |
| P4 | Content written for older versions | Wrong menus and missing features | 5.1 → 5.3 diff, first-pass update, new pages |
| P5 | Website pages that have no chapter (assets, development, information…) | Orphans | Become new chapters |
| P6 | Repeated text across editors (Quick menus, add menus) | Long pages, drift | Shared sections; trim duplicates |

---

## 3. Where We Start From

### 3.1 🗂️ Your earlier website consolidation (logged)

The current website already groups the manual differently from the `.odt` chapter list. This is the starting
point for the target structure:

| Website folder | Pages | What you did |
|---|---|---|
| `/documentation/overview` | 7 | Getting Started: intro, about, installation, quick start, data structure, comparing, migrating |
| `/documentation/interface` | 16 | Chapter 3 (one `.odt`) **split by topic**: windows, areas, editors, headers, footers, tool shelves, side bars, tabs & panels, asset shelves, context / floating / pie menus, last operator panel, floating dialogues, properties |
| `/documentation/workspaces` | 18 | Chapter 4 (one `.odt`) **split per workspace** |
| `/documentation/editors` | 25 | **One page per editor**, all `.odt` sub-chapters folded in (incl. top bar and status bar) |
| `/documentation/keymap` | 2 | Standard keymap, important hotkeys |
| `/documentation/advanced` | 7 | Command line, scripting, working limits, troubleshooting + **new**: reporting a bug, requesting a feature, how to help |
| `/documentation/appendix` | 4 | Glossary, Bforartists history, documentation history, chapter index |
| `/documentation/assets` | 6 | **New**: geometry node assets (grease pencil, material, mesh, normals, primitives, utilities) |
| `/documentation/development` | 2 | **New**: compiling on Windows, doing documentation |
| `/documentation/information` | 1 | **New** |

**Take-aways:** one page per editor is the model readers know; the website-only pages become **new chapters**;
small chapters (Interface, Workspaces) can stay one page each with sub-chapters, or split like the website — decided
per section in Phase 2.

### 3.2 📊 Sizes (from the Tier 2 inventory)

| Chapter | Words | Images | ≈ Reading time |
|---|---|---|---|
| 7 3D Viewport | 217,252 | 3,590 | 18 h |
| 26 Properties Editor | 180,551 | 2,562 | 15 h |
| 12 Geometry Node Editor | 54,493 | 1,062 | 4.5 h |
| 41 Standard Keymap | 35,779 | 2 | 3 h |
| 10 Compositor | 35,044 | 544 | 3 h |
| 13 Shader Editor | 31,695 | 520 | 2.6 h |
| 8 Image Editor · 9 UV · 14 VSE · 15 Movie Clip | 17,700–19,600 each | 290–340 each | ≈ 1.5 h each |
| All other chapters | under 13,500 each | under 240 each | under 1 h each |

---

## 4. Design Decisions

| # | Decision | Choice | Status |
|---|---|---|---|
| T3-D1 | Reading unit | **One long page per chapter** (load once, explore deep), ≈ 100 chapters | ✅ Your direction 10 Oct |
| T3-D2 | Writing unit | **Small source files stay** (the Tier 2 pages); a chapter folder with `assemble: true` is built into one page | 📝 Proposed |
| T3-D3 | Giants | 3D Viewport and Properties Editor are split **by area / tab** (≈ 9 and ≈ 20 chapters); everything else is one page | 📝 Proposed |
| T3-D4 | Page size cap | About **40,000 words** per assembled page until the Phase 1 test says otherwise | 🧪 To test |
| T3-D5 | Sub-chapters | Each source file becomes a `#` sub-chapter with its icon (`{icon=name}`), as the template already supports | ✅ Template ready |
| T3-D6 | Old addresses | Every Tier 2 page address redirects to its chapter with an anchor (`/docs/image-editor#sidebar-view-tab`) | 📝 Proposed |
| T3-D7 | Website-only pages | Become **new chapters** (assets, development, information, how to help, reporting a bug, requesting a feature) | ✅ Your direction 10 Oct |
| T3-D8 | Keymap | Generated from Bforartists' keymap export; one-line descriptions from operator tooltips; each operator links to its documented place | ✅ Your direction 10 Oct |
| T3-D9 | Target version | First pass to **Bforartists 5.3**; screenshots in 5.3 with the default theme | ✅ Your direction 10 Oct |
| T3-D10 | Timing | Assemble before the public go-live if possible, so readers never see the 520-page structure | ❓ Your call |

---

## 5. Big Pages: Viability

> **Verdict:** ✅ big pages work, **if** writers keep small files and the site assembles them. Two chapters are too
> big for any single page and are split by area. One Webflow limit must be tested first.

### 5.1 What a big page costs

| Concern | Image Editor as one page (17,888 words, 334 images) | Geometry nodes as one page (54,493 words, 1,062 images) | Verdict |
|---|---|---|---|
| 📄 HTML size | ≈ 170 KB (≈ 30 KB compressed) | ≈ 500 KB (≈ 90 KB compressed) | ✅ Light: less than one screenshot |
| 🖼️ Images | 334, loaded as you scroll | 1,062, loaded as you scroll | ✅ With lazy loading; 🧪 check Webflow keeps it |
| ⏱️ First paint | Like a short page | Like a short page | ✅ Text first, images later |
| 🧭 Finding things | `Ctrl + F` and the outline cover everything | Same, outline gets long | ✅ Sub-chapter panels fold |
| 🔎 Search | One result per chapter + anchors | Same | ✅ Anchors to sub-chapters |
| 🖨️ Print / PDF | One print = the whole chapter | ≈ 150 printed pages | ✅ What "print a chapter" should mean |
| 🗄️ Webflow rich-text field | ≈ 170 KB | ≈ 500 KB | ❓ **Limit unknown, test first** |
| ✍️ Editing | Unchanged: writers edit the small files | Unchanged | ✅ Because of assembling |
| 🔀 Two writers at once | Different files, no conflict | Different files, no conflict | ✅ |

### 5.2 Why writers should keep small files

| | One big Markdown file per chapter | Small files, assembled (recommended) |
|---|---|---|
| Pages CMS | Slow with 50,000 words; hard to find your spot | Fast; the tree shows every sub-chapter |
| Pull requests | Huge diffs, frequent conflicts | Small, focused diffs |
| Shared sections, images | Harder to track | Unchanged from Tier 2 |
| Reader | One page | **The same one page** |

### 5.3 The giants

| Chapter | As one page | Split into | Each part |
|---|---|---|---|
| 7 3D Viewport | ≈ 2 MB HTML, 3,590 images | Overview · Context menus · Header (≈ 3 parts by object type) · Tool Shelf · Sidebar (≈ 2 parts) · Asset Shelf | ≤ 40,000 words |
| 26 Properties Editor | ≈ 1.7 MB HTML, 2,562 images | One chapter per tab (Render, Output, View Layer, … Modifiers, Particles, Physics, Object Data …) | ≤ 40,000 words |
| 12 Geometry nodes | 54,493 words | Editor · Add menu nodes (2–3 parts) | ≤ 40,000 words |

**Result:** 42 `.odt` chapters → **≈ 73 chapters**, plus ≈ 10–15 website-only and new chapters → **≈ 90–100**.

### 5.4 What we test before deciding (Phase 1)

1. 🗄️ The largest bodies through the Webflow API: Standard Keymap (≈ 330 KB) and an assembled Geometry nodes page
   (≈ 500 KB). If the field has a limit, the fallback is a second body field (`body-2`) the template shows after the
   first, or a lower cap.
2. ⏱️ Page speed on a phone with the Image Editor page: first paint, scroll, the outline's highlight.
3. 🖼️ Lazy loading kept on images after Webflow re-hosts them.

---

## 6. Architecture

### 6.1 Writers write small, readers read big

```
 ✍️ SOURCE (GitHub, Pages CMS)                        🌐 WEBSITE (one CMS item)

 content/editors/image-editor/                         /docs/image-editor
   index.md          assemble: true   ──┐               ┌──────────────────────────────┐
   header/                              │               │ Image Editor                 │
     tools-and-options.md               │  assemble     │  intro                       │
     view-menu.md                       ├────────────▶  │ # Header        {icon=…}     │
     image-menu.md                      │  (build)      │   ## Tools and options       │
   tool-shelf.md                        │               │   ## View menu …             │
   sidebar/                             │               │ # Tool Shelf                 │
     image-tab.md · view-tab.md …     ──┘               │ # Sidebar                    │
                                                        └──────────────────────────────┘
 old address /docs/editors-image-editor-header-view-menu ──301──▶ /docs/image-editor#view-menu
```

### 6.2 Keymap from data

```
 Bforartists 5.3 ──(keymap export script)──▶ keymap.json ──▶ keymap pages (generated)
                                               │             | Hotkey | Operator | What it does | 📍 Where |
 operator tooltips (bl_description) ──────────┘                                          │
 operator index (from the docs' headings) ───────────────────────────────────────────────┘ link: /docs/<chapter>#<anchor>
```

### 6.3 What changed in 5.3

```
 Bforartists 5.1 ─┐  ui_dump.py: every menu, panel, operator, property    ┌─▶ 🆕 added   → new sections or pages
                  ├─▶ diff ─────────────────────────────────────────────┼─▶ ✏️ changed → pages to update
 Bforartists 5.3 ─┘                                                      └─▶ 🗑️ removed → text to delete
        │ operator index maps each item to its chapter
        ▼
 update queue per chapter (report + status: needs-update)
```

---

## 7. Implementation Plan

### Phase 0 — This Document

- [x] Draft the plan (this file), with the big-page viability check.
- [ ] 👤 Your review: T3-D2, T3-D3, T3-D10 and the chapter list in Phase 2.

### Phase 1 — Big Page Test

**Goal:** prove big pages work on Webflow before reshaping anything.

- [ ] Send the Standard Keymap body (≈ 330 KB) and an assembled Geometry nodes page (≈ 500 KB) to a draft test item.
- [ ] Measure the Image Editor page on a phone: first paint, scroll, outline highlight; images lazy-load.
- [ ] Set the page cap (T3-D4) from the results; choose the fallback if the field has a limit.

**Acceptance:** a ≈ 500 KB chapter publishes on staging and scrolls smoothly on a mid-range phone.

### Phase 2 — Target Structure (~100 Chapters)

**Goal:** agree the chapter list before any file moves.

- [ ] `structure.yml`: every chapter → which Tier 2 pages it assembles, in which order, with sub-chapter icons.
- [ ] Starts from your website consolidation (§3.1): one page per editor; website-only pages as new chapters.
- [ ] Decide per section: Interface and Workspaces as one page each, or split by topic like the website.
- [ ] Redirect map: every Tier 2 address → chapter + anchor.
- [ ] Review with you, section by section.

**Acceptance:** every Tier 2 page belongs to exactly one chapter; the sidebar shows ≈ 100 entries.

### Phase 3 — Assemble the Chapters

**Goal:** the website shows ≈ 100 chapters; writers' files barely move.

- [ ] `assemble: true` support in `docs_io.site_tree`, `html_build`, `render.py` (preview) and `sync.py`:
      children become `#` sub-chapters with icons; their headings shift down one level.
- [ ] `check.py`: page cap, duplicate anchors inside a chapter, unassembled orphans.
- [ ] Sync: Tier 2 items of assembled pages are archived in Webflow (not deleted) and redirected.
- [ ] Pilot: **Image Editor** (16 files → 1 chapter). Then editor by editor, one pull request each.
- [ ] Shared sections deduplicated where the same text now sits twice on one page.

**Acceptance:** pilot chapter on staging looks and scrolls right; old addresses land on the right sub-chapter.

### Phase 4 — Keymap Redesign

**Goal:** a keymap you can scan, where every hotkey says what it does and where it is documented.

- [ ] `keymap_export.py` (runs inside Bforartists): every keymap item → editor, mode, keys, operator, properties.
- [ ] One-line descriptions from operator tooltips (`bl_description`); a written description wins when present.
- [ ] Operator index: operator → chapter + anchor, built from the docs' headings and tool cards.
- [ ] Generated keymap chapters: per editor and mode, `| Hotkey | Operator | What it does | 📍 Where |`.
- [ ] `check.py`: operators with no documented place are listed (the to-do list for writers).
- [ ] Important Hotkeys: hand-picked list on top, same generated rows.

**Acceptance:** every keymap row links to a page or is on the "not documented yet" list; re-running for a new
version regenerates the tables in one pull request.

### Phase 5 — 5.3 Audit: What Changed

**Goal:** an exact, per-chapter list of what to update.

- [ ] `ui_dump.py` (runs inside Bforartists, also via the bfa-coworker connection): menus, panels, operators,
      properties with labels and tooltips → JSON, for 5.1 and 5.3.
- [ ] Diff → 🆕 added · ✏️ changed · 🗑️ removed, mapped to chapters through the operator index.
- [ ] Release notes of Blender 5.2 / 5.3 and the Bforartists weekly reports for behaviour changes the dump cannot see.
- [ ] Each affected page gets `status: needs-update`; a report lists the queue per chapter.

**Acceptance:** every chapter has an update list (or "no changes"); nothing in the diff is unmapped.

### Phase 6 — First Pass to 5.3, New Content

**Goal:** every chapter correct for 5.3; nothing important missing.

- [ ] Work the queue chapter by chapter; `version: "5.3"` when a chapter is done.
- [ ] Screenshots retaken in 5.3 with the capture tool from Tier 2 (default Bforartists theme).
- [ ] New sections or pages for 5.2 / 5.3 features.
- [ ] Write the empty pages: Quick Start (mini tutorial), Comparing to Blender, Migrating from Blender.
- [ ] Website-only chapters refreshed: geometry node assets, development, how to help, reporting a bug.

**Acceptance:** no chapter left at `needs-update`; the three Getting Started pages written.

### Phase 7 — Trim and Reword

**Goal:** shorter, clearer pages, following the *Reference Manual writing guide*.

- [ ] Remove duplicates that assembling made visible (same paragraph twice on one page).
- [ ] Reword for clarity; no opinions, no tutorials inside reference entries (writing guide rules).
- [ ] Glossary terms linked on first use per chapter.

**Acceptance:** each chapter reviewed once; word count drops where duplicates were.

---

## 8. Files Touched

| File | Change |
|---|---|
| `docs2/tools/structure.yml` | 🆕 Chapter list: what each chapter assembles |
| `docs2/tools/docs_io.py`, `html_build.py`, `render.py`, `sync.py` | `assemble: true` chapters |
| `docs2/tools/check.py` | Page cap, anchors, orphans, undocumented operators |
| `docs2/tools/keymap_export.py`, `ui_dump.py` | 🆕 Run inside Bforartists |
| `docs2/tools/operator_index.py` | 🆕 Operator → chapter + anchor |
| `docs2/content/keymap/**` | Generated keymap chapters |
| `docs2/reports/{update-queue.md, redirects.csv}` | 🆕 Generated |

---

## 9. Verification Plan

| Phase | Test | Pass when |
|---|---|---|
| 1 | Largest bodies to Webflow | Accepted and published on staging |
| 1 | Phone test, Image Editor page | Smooth scroll; images load as you scroll |
| 3 | Pilot chapter | Sub-chapters, icons, outline and old addresses all right |
| 3 | Words before / after assembling | Same count (nothing lost by assembling) |
| 4 | Keymap rows | 100% link to a page or the to-do list |
| 5 | Diff mapping | 0 unmapped items |
| 6 | Queue | 0 chapters at `needs-update` |

---

## 10. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Webflow rich-text field has a size limit | 🟡 | Test first (Phase 1); `body-2` fallback or lower cap |
| Very long outline on giant chapters | 🟡 | Giants split by area; panels fold; outline lists `#` and `##` only |
| Old links break after assembling | 🟢 | Redirect map to chapter + anchor; Tier 2 items archived, not deleted |
| Writers lost in many small files | 🟢 | Pages CMS tree mirrors the chapter's sub-chapters |
| 5.3 dump misses behaviour changes | 🟡 | Release notes and weekly reports as a second source |
| Tier 2 goes public before assembling | 🟡 | T3-D10: assemble before go-live if timing allows |

---

## 11. Out of Scope

- 🌍 Translations.
- 🎬 Video tutorials (pages can link them).
- 🎨 Template redesign (the template session owns the look; it already supports sub-chapters and icons).

---

## 12. Open Questions

1. **T3-D10 timing:** assemble chapters before the public go-live (readers only ever see ~100 chapters), or go live
   with the Tier 2 structure first?
2. **Interface and Workspaces:** one page each with sub-chapters, or split by topic like the current website
   (16 and 18 pages)?
3. **3D Viewport header** (94,868 words): split by object type (Mesh, Curve, Grease Pencil, Armature…) or by menu
   family (View/Select/Add, Object, Edit-mode menus)?
4. **5.3 timing:** is 5.3 released (or close) when Tier 3 starts, so the screenshots of Tier 2 Phase 4 can be taken
   in 5.3 directly instead of twice?
