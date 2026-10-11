# Bforartists Docs 2.0 — Tier 2: The Whole Manual, Live and Maintainable

> 🎯 **Goal of this tier:** every chapter of the `.odt` manual travels the road Tier 1 built:
> Markdown on GitHub → checked and previewed → on **Webflow**, with fresh screenshots, and proven
> maintainable by a real documentation update done by the team. At the end, bforartists.co can switch
> to the new docs with one maintainer click.

**Date**: 2026-10-10

**Status**: 🟢 Approved 10 Oct — Phase 1 🧪 groundwork done (inventory, page map, `docs2/main`)

**Depends on**: Tier 1 (`plan_docs2_tier1_getting_started.md`): Phase 5 sync and its end-to-end test

**Blocks**: Refine phase (trimming, rewording, new writing — decision D13), retiring the `.odt` manual

**Branch**: `docs2/main`, the docs branch that becomes the main branch once everything is green (holds Tier 1,
Phase 5 and this groundwork); one `docs2/section-<name>` branch per section, merged by pull request. `master`
untouched until go-live.

**Scope (measured)**: 42 chapters · 517 `.odt` files · **763,486 words** · 11,526 images before dedupe ·
**523 pages in 8 sections** (page map) · 97 legacy website pages · 1 screenshot capture tool

**Companion docs**: [Tier 1 plan](plan_docs2_tier1_getting_started.md) · [End-to-end test](test_end_to_end_workflow.md) ·
[Usability test](usability_test_getting_started.md) · Wiki: [How Docs 2.0 works](../dev-docs/How-Docs-2.0-Works.md)

---

## Table of Contents

1. [Summary](#1-summary)
2. [The Problem We Are Solving](#2-the-problem-we-are-solving)
3. [Where We Are Now](#3-where-we-are-now)
4. [Design Decisions](#4-design-decisions)
5. [Architecture](#5-architecture)
6. [Implementation Plan](#6-implementation-plan)
   - [Phase 0 — This Document](#phase-0--this-document)
   - [Phase 1 — Inventory and Section Map](#phase-1--inventory-and-section-map)
   - [Phase 2 — Convert the Whole Manual](#phase-2--convert-the-whole-manual)
   - [Phase 3 — Webflow at Full Size](#phase-3--webflow-at-full-size)
   - [Phase 4 — New Screenshots](#phase-4--new-screenshots)
   - [Phase 5 — Maintenance Test: A Real Docs Update](#phase-5--maintenance-test-a-real-docs-update)
   - [Phase 6 — Usability Test and Go-Live Readiness](#phase-6--usability-test-and-go-live-readiness)
7. [Files Touched](#7-files-touched)
8. [Verification Plan](#8-verification-plan)
9. [Risks & Mitigations](#9-risks--mitigations)
10. [Out of Scope](#10-out-of-scope)
11. [Open Questions](#11-open-questions)

---

## 1. Summary

Tier 1 proved the road on one section. Tier 2 drives the **whole manual** down it, in four streams:

1. 📄 **Parse** — convert all 42 chapters as a **faithful clone** (no trimming, D13), section by section,
   each as its own pull request with the word check, preview and bot.
2. 📸 **Photos** — inventory every screenshot, capture the outdated ones again from Bforartists 5.1 with a
   **recipe per image**, same file names so no page needs editing.
3. 🌐 **Webflow** — the full manual on staging: every section, a sidebar that scales past Webflow's list
   limits, search, legacy redirects ready, PDF on demand.
4. 🧪 **Prove it** — the team does one real documentation update in the new workflow, then a usability
   test with writers and readers. Only then: the go-live decision.

**Guiding principle (unchanged):** less for contributors, more for readers.

---

## 2. The Problem We Are Solving

| # | Today | Effect | Tier 2 answer |
|---|---|---|---|
| P1 | About 494 of 517 chapter files still only in `.odt` | Two manuals; the new workflow covers about 4% | Convert all, section by section |
| P2 | Screenshots from many versions back | Readers see an interface that no longer exists | Capture recipes, refreshed in batches |
| P3 | Website docs mostly empty static pages | Readers land on placeholders | Every section synced into the CMS |
| P4 | Webflow collection lists show at most 100 items | A 500-page sidebar cannot be one list | Sidebar from a generated navigation file |
| P5 | Old addresses (`/documentation/...`) are linked everywhere | Broken links at launch | Redirect map from `legacy-path`, applied at launch |
| P6 | No proof the new workflow survives real work | Risk of a second abandoned manual | A real update by the team, measured |

---

## 3. Where We Are Now

| Piece | State | Where |
|---|---|---|
| Converter | ✅ Faithful (23 of 23 groups keep every word), editor-stable | `docs2/tools/convert.py` |
| Pages in Markdown | ✅ 29 pages + 2 shared sections (Getting Started, Interface, Timeline, Modifiers) | `docs2/content/` |
| Online editing | ✅ Pages CMS, one-line diffs, new chapters fill their own headers | `.pages.yml` |
| Checks, image bot, preview | ✅ On every pull request and save | `.github/workflows/docs2.yml` |
| Sync to Webflow staging | 🧪 Built, in the end-to-end test | `docs2/tools/sync.py` |
| Webflow template | 🟡 Built by the template session (sidebar, outline, footer card, search, light mode) | Doc Pages Template |
| Screenshots | 🟡 541 in the library, mostly older versions | `docs2/images/` |

**The manual by chapter** (files per chapter number):

| Chapters | Files | Notes |
|---|---|---|
| 1–6 Introduction, Install, Interface, Workspaces, Topbar, Editors intro | 12 | Getting Started done |
| 7 3D Viewport | 106 | Largest: tools, menus, modes |
| 8–15 Image, UV, Compositor, Texture/Geometry/Shader nodes, VSE, Movie Clip | 224 | Node "Add menu" chapters repeat heavily → shared sections |
| 16–23 Dope Sheet, Timeline, Graph, Drivers, NLA, Text, Console, Info | 61 | Timeline done (Spike 1) |
| 24–30 Toolbar, Outliner, Properties, File/Asset browser, Spreadsheet, Preferences | 98 | Properties 90 files; Modifiers done |
| 31–42 Data system, Advanced, Extensions, Troubleshooting, Glossary, History, Keymaps | 16 | Short; Data System done |

---

## 4. Design Decisions

| # | Decision | Choice | Status |
|---|---|---|---|
| T2-D1 | Content fidelity | **Faithful clone** of every chapter (D13). Structure work allowed: shared sections, consolidated chapters | ✅ From Tier 1 |
| T2-D2 | Batching | **Follow the chapter list top to bottom** (4 → 42). One pull request per chapter (big chapters split by sub-chapter), each with word check, preview, bot | ✅ Confirmed 10 Oct |
| T2-D3 | Docs branch | **`docs2/main`**: the docs branch and the sync's publish branch; becomes the main branch once all is green | ✅ Confirmed 10 Oct |
| T2-D4 | Sidebar at scale | Generated `nav.json` (sections → chapters → sub-chapters) read by the docs script, instead of collection lists (100-item limit) | 📝 Proposed |
| T2-D5 | Screenshots | **Recipe per image** (workspace, editor, state, crop) captured in Bforartists with the **default Bforartists theme**; same file names, so pages stay untouched | ✅ Theme confirmed 10 Oct |
| T2-D6 | Image format | Keep PNG/JPG through Tier 2; WebP decided after measuring Webflow's CDN | 📝 Proposed |
| T2-D7 | Legacy addresses | Every page carries `legacy-path`; a redirect list is generated and applied at go-live, not before | ✅ From Tier 1 |
| T2-D8 | PDF | Print stylesheet per page; full-manual PDF printed on demand and offered on *Documentation History* | ✅ Confirmed earlier |
| T2-D9 | Go-live | A separate maintainer decision after Phase 6; publishing bforartists.co is never automatic | ✅ Confirmed |
| T2-D10 | Webflow plan | **2,000 CMS items** available; the page map needs about 523 pages + 8 sections + shared sections (< 700) | ✅ Confirmed 10 Oct |
| T2-D11 | Page structure | **One page per `.odt` file** (chapter → folder `index.md`, sub-chapter → page or folder, leaf → page); sub-chapters with no file get a title-only group page; files under 80 words fold into the page above | ✅ Groundwork |

---

## 5. Architecture

### 5.1 Four streams, one road

```
 📄 PARSE                 📸 PHOTOS                       🌐 WEBFLOW                  🧪 PROVE
 517 .odt                 index.csv inventory            sync.py (Tier 1)            routine update
   │ convert.py             │ recipes.yml                  │ + nav.json                 │ by the team
   │ per section            │ capture in Bforartists       │ + redirects.csv            │ usability test
   ▼                        ▼                              ▼                            ▼
 ┌──────────────────────────────────────────────────────────────────────────────────────────┐
 │  🐙 docs2/main   ←── PR per section ──  docs2/section-*      (checks · bot · preview)     │
 └──────────────────────────────────────────┬───────────────────────────────────────────────┘
                                            │ merge
                                            ▼
                         🌐 bforartists.webflow.io (staging) ── maintainer click ──▶ bforartists.co
```

### 5.2 A section, start to finish

```
 pages.json entry ─▶ convert.py ─▶ wordcount ✅ ─▶ repeats → snippets ─▶ PR (preview 👀)
        ─▶ review: structure only (D13) ─▶ merge ─▶ sync ─▶ staging ─▶ legacy-path filled
```

### 5.3 Screenshot recipe (one per image)

```yaml
# docs2/images/recipes.yml
getting-started/installation/download-bforartists.png:
  version: "5.1"                    # version it was captured in; compared with the page's version
  workspace: Layout
  editor: PREFERENCES               # area to capture
  state:                            # small Python snippets run before capture
    - "bpy.context.preferences.active_section = 'INTERFACE'"
  crop: area                        # area | region:HEADER | box: [x, y, w, h]
  scale: 1.0                        # interface scale for consistent pixel size
```

---

## 6. Implementation Plan

### Phase 0 — This Document

- [x] Draft the plan (this file).
- [ ] 👤 Your review: decisions T2-D2, T2-D3, T2-D10 and the section order.

### Phase 1 — Inventory and Section Map

**Goal:** know exactly what we are moving, and where every chapter lands, before converting anything.

**Files:** `docs2/tools/{inventory,map_pages}.py`, `docs2/tools/{sections.yml,page_map.json,legacy_pages.json}`,
`docs2/reports/{inventory.md,inventory.json,page-map.md}`

**🤖 Done by Claude (10 Oct)**

- [x] 🌿 `docs2/main` made from Tier 1 + Phase 5; workflow, Pages CMS buttons, sync and wiki point at it.
- [x] 📦 `inventory.py`: every `.odt` read straight from its XML in 15 seconds → words, images, tables, headings.
      **517 files · 763,486 words · 11,526 images · 2,975 tables.** Largest: Standard Keymap (35,779 words),
      3D Viewport sculpt tool tab (16,153), 3D Viewport header tools (14,710).
- [x] 📚 `sections.yml`: 8 sections in chapter-list order — Getting Started · Interface · Workspaces · Editors ·
      Advanced · Extensions · Appendix · Keymap — matching the current website's documentation folders.
- [x] 🗺️ `map_pages.py`: every file mapped → **523 pages** (20 already converted), 10 title-only group pages,
      11 very long pages flagged for the Webflow size check. `--apply --section editors --chapter 7` moves one
      chapter into `pages.json` when its turn comes.
- [x] 🌐 `legacy_pages.json`: the 97 current `/documentation/...` pages; chapter and sub-chapter pages are matched
      to them by title. The rest (Interface and Workspaces sub-pages, assets, development) are listed in the
      report for redirects to the right page or heading.
- [x] 🧪 **Converter dry run on the whole manual** (all 503 planned pages, scratch only, nothing committed):

| Result | |
|---|---|
| 💥 Crashes | **0** in about 20 minutes |
| 📝 Word check | **505 of 505 groups keep every word** |
| 🖼️ Images | 8,067 unique (3,902 duplicates reused), 216 MB |
| ✅ Checks | 6 broken image links on 2 pages (headings inside lists) → **fixed** in the converter; 12 false alt warnings (a node called *Image*) → **fixed** in `check.py` |
| 📏 Size | 8.4 MB of page HTML in total; largest page Standard Keymap ≈ 330 KB |
| 🗂️ Webflow items | 531 pages + 8 sections + shared sections ≈ **540 of 2,000** |

- [x] 🔄 `convert_chapter.py`: one command per chapter — adds it to `pages.json`, converts only its pages, stops if a word
      is lost, copies new pages and images in (never overwrites an edited page), runs the checks. Tried on
      chapter 4 Workspaces: 1 page, 40 images, all checks green.
- [x] 🌐 Sync ready for the full size: updates go in batches (50 items per call); Doc Sections got a `checksum` field so
      unchanged sections are skipped too. Tested against a stand-in Webflow: run 1 creates, run 2 changes nothing,
      a hand edit is skipped.
- [x] 🧭 Section order comes from `sections.yml` (chapter-list order) in the preview, the sidebar and the sync.

**Acceptance:** every one of the 517 files is mapped to a page or a shared section; nothing unmapped. ✅

### Phase 2 — Convert the Whole Manual

**Goal:** all chapters as Markdown on `docs2/main`, faithful, editor-stable, checked.

**Files:** `docs2/content/**`, `docs2/snippets/**`, `docs2/images/**`, `convert.py` (fixes as found)

Order: **the chapter list, top to bottom** (T2-D2). Chapters 1–3, 17, 26.9 and 31 are done.

| Run | Chapters | Section | Files | Words |
|---|---|---|---|---|
| 1 | 4 Workspaces | Workspaces | 1 | 2,073 |
| 2 | 5 Topbar and Statusbar · 6 Editors introduction | Editors | 7 | 16,501 |
| 3 | 7 3D Viewport | Editors | 106 | 217,252 |
| 4 | 8 Image · 9 UV | Editors | 29 | 35,629 |
| 5 | 10 Compositor · 11 Texture nodes | Editors | 36 | 35,115 |
| 6 | 12 Geometry nodes | Editors | 88 | 54,493 |
| 7 | 13 Shader · 14 Video Sequencer · 15 Movie Clip | Editors | 71 | 69,999 |
| 8 | 16 Dope Sheet · 18 Graph · 19 Drivers · 20 NLA | Editors | 52 | 42,009 |
| 9 | 21–25 Text, Console, Info, Toolbar, Outliner | Editors | 5 | 17,170 |
| 10 | 26 Properties (rest) | Editors | 79 | 143,501 |
| 11 | 27–30 File browser, Asset browser, Spreadsheet, Preferences | Editors | 6 | 22,715 |
| 12 | 32–34, 36 Advanced | Advanced | 4 | 4,487 |
| 13 | 35 Extensions | Extensions | 5 | 4,983 |
| 14 | 37, 39, 40 Glossary, History, Manual history | Appendix | 3 | 12,618 |
| 15 | 41, 42 Keymaps | Keymap | 2 | 36,269 |
| 16 | Website-only pages → **new chapters** (assets, development, information, how to help, reporting a bug, requesting a feature) | Several | ≈ 12 | website text |

- [ ] Per run: `python3 docs2/tools/convert_chapter.py <odt manual> <section> <chapter>` on a `docs2/section-<name>`
      branch → word check 100% → repeats into snippets → PR into `docs2/main` → preview review → merge (syncs staging).
- [ ] Converter fixes found at scale go in their own small PRs, re-run on converted sections (idempotent).
- [ ] Hotspot screenshots (`**Label** (colour)` lists) and tool cards (`### Bevel`) recognised in `patterns.py`.

**Acceptance:** 42 of 42 chapters converted; word check passes for every group; checks green on `docs2/main`.

### Phase 3 — Webflow at Full Size

**Goal:** the whole manual on staging, fast, findable, with a sidebar that works at 500+ pages.

**Files:** `sync.py`, `docs2/tools/nav_json.py` (new), docs script (template session), `docs2/reports/redirects.csv`

- [x] CMS item limit: 2,000 (≈ 540 needed). Updates batched (50 per call).
- [ ] **Size check:** rich-text size per item with the largest pages (Standard Keymap ≈ 330 KB); split rule by top heading if needed.
- [ ] 🧩 With the template session: the sidebar nests three levels in Editors (chapter → sub-chapter → page, e.g.
      3D Viewport → Header → View Menu); the template indents one level today. `#` sub-chapters with `{icon=name}`
      are already sent as `<h1 data-icon="name">` (the template maps names to icons).
- [ ] `nav.json`: sections → chapters → sub-chapters with titles, icons, slugs; synced as one Doc Snippet item
      (or a hosted asset) that the docs script reads for the sidebar and previous/next.
- [ ] Full sync of all sections; second run changes nothing (checksums).
- [ ] Search across all pages (template session's search + Webflow site search).
- [ ] Section overview pages and the Docs home tiles for every section.
- [ ] `redirects.csv` generated from `legacy-path` → `/docs/<slug>`; applied at go-live (Phase 6).
- [ ] Print: every page prints cleanly; full-manual PDF on demand (*Documentation History* page).

**Acceptance:** every page reachable on staging from the sidebar and search; a full sync under 15 minutes;
redirect list covers all 129 legacy pages.

### Phase 4 — New Screenshots

**Goal:** every screenshot shows Bforartists 5.1, captured the same way every time.

**Files:** `docs2/images/recipes.yml` (new), `docs2/tools/capture/` (Bforartists script or add-on), `image_bot.py`

- [ ] Inventory: each image with its page, heading, size, and the version it shows (from `screenshots:`).
- [ ] 🔬 Spike: capture recipes in Bforartists — areas, headers, panels, sidebars (menus and popovers are harder:
      test them first). Try it through the bfa-coworker connection on your PC.
- [ ] Theme and scale fixed for all captures (default theme, interface scale 1.0, same window size).
- [ ] Batches by section, worst first; each batch is a PR whose preview shows old vs new.
- [ ] Images that cannot be captured by recipe get a **"screenshot needed"** list for volunteers (drop in Pages CMS).
- [ ] `screenshots: "5.1"` updated on pages whose images are all refreshed.

**Acceptance:** ≥ 80% of images captured by recipe at 5.1; the rest listed; a re-run on a new version replaces
images in one PR.

### Phase 5 — Maintenance Test: A Real Docs Update

**Goal:** prove the team can keep the manual current with the new workflow, without help.

- [ ] Pick a real update: the changes of one Bforartists release (from the weekly reports).
- [ ] 2–3 team members make the changes in Pages CMS on branches: text edits, new page, new screenshots,
      a shared section change.
- [ ] Measure per change: time, steps, help needed, bot and check results, review time.
- [ ] Compare with the `.odt` way (same change list, from memory or one timed sample).
- [ ] Fix the top friction points (docs, form fields, bot messages) before Phase 6.

**Acceptance:** the release update is done by the team in the new workflow, each change under 10 minutes on
average, no maintainer rescue needed.

### Phase 6 — Usability Test and Go-Live Readiness

**Goal:** readers find answers; writers enjoy writing; the switch is one click.

- [ ] Reader test (5 people): find 6 answers across sections; time to answer, success, comments.
- [ ] Writer test (3 people): the end-to-end test tasks on a real section.
- [ ] Go-live checklist: redirects applied, `master` merge plan for `docs2/`, `.odt` frozen on `odt-5.1-final`,
      bforartists.co publish by a maintainer, announcement.
- [ ] Decision meeting: go / fix first.

**Acceptance:** readers answer ≥ 5 of 6 tasks; writers finish without help; go-live checklist complete.

---

## 7. Files Touched

| File | Change |
|---|---|
| `docs2/tools/inventory.py` | 🆕 Inventory of the `.odt` manual |
| `docs2/tools/pages.json` | All 42 chapters mapped |
| `docs2/tools/nav_json.py` | 🆕 Sidebar navigation file for Webflow |
| `docs2/tools/capture/` | 🆕 Screenshot capture in Bforartists |
| `docs2/images/recipes.yml` | 🆕 One recipe per screenshot |
| `docs2/tools/sync.py` | nav.json item, batched updates, size guard |
| `docs2/tools/patterns.py` | Hotspots, tool cards |
| `docs2/content/**`, `docs2/snippets/**`, `docs2/images/**` | The whole manual |
| `docs2/reports/{inventory.md, redirects.csv}` | 🆕 Generated |
| `.github/workflows/docs2.yml` | Publish branch → `docs2/main` |

---

## 8. Verification Plan

### 8.1 Automated (every pull request)

| Check | Tool |
|---|---|
| No lost words per section | `wordcount.py` |
| Front matter, links, images, shared sections, sidebar | `check.py` |
| Images filed and deduped | `image_bot.py` |
| Preview with the site's styles | `render.py` |
| Second sync changes nothing | `sync.py` (checksums) |

### 8.2 Testing Guide

| Phase | Test | Pass when |
|---|---|---|
| 1 | Inventory totals = files on disk | 517 of 517 mapped |
| 2 | Word check per section | 100% of groups pass |
| 3 | Full sync twice | Second run: 0 updates |
| 3 | Sidebar with all sections | Opens < 1 s on a phone; correct nesting |
| 4 | Recipe re-run | Same pixels for an unchanged interface |
| 5 | Real update | Average change < 10 min, no rescue |
| 6 | Reader tasks | ≥ 5 of 6 answered |

### 8.3 People

| Who | When |
|---|---|
| You | Section PR reviews (structure only), the Phase 5 update, go-live decision |
| Contributors (later) | Writer test; you organise this side |
| Readers | Phase 6 reader test; you organise this side |

---

## 9. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Webflow CMS item limit below the page count | 🟡 | Check in Phase 3.0; consolidate sub-chapters into pages; plan upgrade decision |
| Very long pages exceed rich-text limits | 🟡 | Size guard in `sync.py`; split rule by `##` heading |
| 100-item collection list limit breaks the sidebar | 🔴 known | `nav.json` read by the docs script (T2-D4) |
| Converter edge cases at scale (tables in tables, odd styles) | 🟡 | Warm-up section first; fixes in small PRs; word check catches loss |
| Menus and popovers hard to capture by recipe | 🟡 | Spike first; volunteer list for the rest |
| Writers edit Webflow directly | 🟢 | Checksum guard skips and reports; wiki says edit in GitHub |
| Two manuals drift during Tier 2 | 🟡 | `.odt` edits paused per converted section; freeze tag at go-live |
| Pages CMS changes upstream | 🟢 | Pages are plain Markdown; any editor works |

---

## 10. Out of Scope

- ✂️ Trimming, rewording and new writing (Refine phase, D13).
- 🌍 Translations.
- 🔍 A custom search engine beyond Webflow's.
- 🎨 Template redesign (the template session owns the look).
- 📄 Per-release PDF automation beyond print-on-demand.

---

## 11. Open Questions

1. ✅ Answered 10 Oct: `docs2/main` · 2,000 CMS items · chapter list top to bottom · default Bforartists theme ·
   writers are you, later a few contributors.
2. ✅ **Long pages:** big pages are the goal (load once, explore deep, ~100 chapters). Tier 2 keeps one source file
   per `.odt` file; Tier 3 assembles them into big chapter pages. See `plan_docs2_tier3_structure_and_update.md`.
3. ✅ **Website-only pages** become new chapters (run 16).
