# Bforartists Docs 2.0 — Tier 1: Getting Started, End to End

> 🎯 **Goal of this tier:** one real section — **Getting Started** — travels the whole road:
> Markdown on a branch → edited in the browser → checked and previewed → synced to
> **Webflow staging** → tested by real people. When this works, every other section
> follows the same road.

**Date**: 2026-10-10

**Status**: 🟢 Approved 10 Oct — Phase 1 in progress

**Depends on**: Spike 1 (`docs2/spike1-migration`, commits `48a7749` → `ca887b9`)

**Blocks**: Phase 3 of the master plan (section-by-section conversion)

**Branch**: `docs2/tier1-getting-started` (from `docs2/spike1-migration`); `master` untouched

**Estimated scope**: 8 pages · ~900–1,300 LOC (converter changes, checks, sync script, docs script) · 1 Webflow template + 3 CMS collections

**Companion docs**: [Plan](https://claude.ai/code/artifact/f2ea4f5a-ec27-4679-9d9c-a8e2c5559863) · [Build Map](https://claude.ai/code/artifact/7c9a92b8-596a-41a1-9f71-77b4fde98c9a) · [`usability_test_getting_started.md`](usability_test_getting_started.md)

---

## Table of Contents

1. [Summary](#1-summary)
2. [The Problem We Are Solving](#2-the-problem-we-are-solving)
3. [Where We Are Now](#3-where-we-are-now)
4. [Design Decisions](#4-design-decisions)
5. [Architecture](#5-architecture)
6. [Implementation Plan](#6-implementation-plan)
   - [Phase 0 — This Document](#phase-0--this-document)
   - [Phase 1 — Getting Started Content](#phase-1--getting-started-content)
   - [Phase 2 — Writer Workflow in the Browser](#phase-2--writer-workflow-in-the-browser)
   - [Phase 3 — Checks, Image Bot and Preview](#phase-3--checks-image-bot-and-preview)
   - [Phase 4 — Webflow Template and Collections](#phase-4--webflow-template-and-collections)
   - [Phase 5 — Sync to Webflow Staging](#phase-5--sync-to-webflow-staging)
   - [Phase 6 — Usability Test, Fixes, Pull Request](#phase-6--usability-test-fixes-pull-request)
7. [Files Touched](#7-files-touched)
8. [Verification Plan](#8-verification-plan)
9. [Risks & Mitigations](#9-risks--mitigations)
10. [Out of Scope](#10-out-of-scope)
11. [Open Questions](#11-open-questions)

---

## 1. Summary

Spike 1 proved the `.odt` manual converts cleanly to Markdown. Tier 1 proves the **whole workflow**
on one section that every new artist reads first:

1. 📄 **Content** — convert the 5 Getting Started chapters **as a faithful clone** (no trimming),
   carry over the current website text for the 3 pages that have no chapter, all in plain writing
   (no custom tags for writers).
2. ✏️ **Writer workflow** — edit in the browser with Pages CMS; drop a screenshot and let the bot file it.
3. 🔍 **Checks + preview** — every pull request is checked and gets a **preview link** that looks like
   the website.
4. 🌐 **Webflow** — a docs template and 3 CMS collections on staging, fed by a sync script.
5. 🧪 **People** — a usability test with writers and readers before anything goes further.

**Guiding principle:** less for contributors, more for readers. Writers write, drop and pick from forms;
the build does the polish; Webflow does the presenting.

---

## 2. The Problem We Are Solving

| # | Old `.odt` workflow | Effect | Tier 1 answer |
|---|---|---|---|
| P1 | Edit in LibreOffice, export PDF, commit by hand | Nobody kept doing it | Edit in the browser, save = commit |
| P2 | Same text repeated in many files (brush curve settings…) | Fixes missed, drift | Shared sections, written once |
| P3 | Screenshots pasted, resized and renamed by hand | Chore, inconsistent | Drop → bot names, sizes, dedupes |
| P4 | PDF export per release | Release bottleneck | Browser print + release PDF from CI |
| P5 | Website pages built by hand, mostly empty | 97 pages, ~6 with text | Sync script fills CMS items |
| P6 | No review, no checks | Errors reach readers | Pull request + checks + preview |

---

## 3. Where We Are Now

| Piece | State | Where |
|---|---|---|
| Converter (`.odt` → Markdown) | ✅ Works on 18 files | `docs2/tools/convert.py` |
| Converted pages | ✅ 21 pages + 2 snippets (Timeline, Interface, Modifiers) | `docs2/content/` |
| Image library | ✅ 534 unique images, deduped | `docs2/images/` |
| Pages CMS config | 🟡 Written, not installed | `.pages.yml` |
| Webflow docs | 🟡 Static pages, sidebar and toolbar built, Getting Started text partly there | bforartists.webflow.io/documentation |
| Checks, bot, preview, sync | ⬜ Not started | — |

**Getting Started sources** (from your local clone):

| Target page | Source | Words |
|---|---|---|
| Introduction | `1 Introduction.odt` | 234 |
| Using the Documentation | `1.1 How to use the Manual.odt` + `38 About this Manual.odt` (merged) | 1,075 + 391 |
| Installation | `2 Installing Bforartists.odt` | 2,559 |
| Data Structure | `31 Data System.odt` | 1,407 |
| Quick Start | **New** | — |
| Comparing to Blender | **New** (website draft if any) | — |
| Migrating from Blender | **New** | — |
| Section overview (Getting Started) | **New**, short | — |

---

## 4. Design Decisions

| # | Decision | Choice | Status |
|---|---|---|---|
| D1 | Source of truth | Markdown in the Manual repo; `.odt` frozen later on `odt-5.1-final` | ✅ Confirmed |
| D2 | Writer editor | **Pages CMS** (hosted, nothing to maintain) | ✅ Confirmed |
| D3 | Insert buttons vs preview | **Preview link on every pull request first** (the low-hanging fruit). A more visual GUI (Sveltia CMS insert buttons) is decided after we see how pages look and how writers do in the test | ✅ Confirmed 10 Oct |
| D4 | Writer syntax | **Plain writing**, recognised by the build; WYSIWYG editing with drag and drop. Simple "insert" components stay a goal. Phase 2 scores the online editor (Pages CMS) against the GitHub editor and a local editor for no-dependency, fun usability | ✅ Confirmed 10 Oct |
| D5 | Page-level options | Pages CMS form fields: status, video, example files, shared sections, Quick Start links | ✅ Confirmed |
| D6 | Images | Drop → `_inbox/` → bot files by page + heading, WebP, ≤ 2,560 px, dedupe | ✅ Confirmed 10 Oct |
| D7 | Webflow model | CMS collections `Doc Sections`, `Doc Pages`, `Doc Snippets`; one page template; staging only. **Reuse the existing Webflow docs structure** (panels, sidebar, toolbar) and keep earlier decisions: panel sidebar with sub-chapter navigation and sticky sections | ✅ Confirmed 10 Oct |
| D8 | Sync direction | One way: repo → Webflow. Checksum guard stops the sync if Webflow was edited by hand | ✅ Confirmed |
| D9 | Print / PDF | Print stylesheet + browser print now; release PDFs in Tier 3 | ✅ Confirmed |
| D10 | Mobile | Bottom bar: Chapters · current heading · Search | ✅ Confirmed |
| D11 | Git workflow | Work on a branch; pull request only when you say it is ready | ✅ Confirmed |
| D12 | Scope | Getting Started only (8 pages) | ✅ Confirmed 10 Oct |
| D13 | Trimming | **No trimming or rewording until the whole manual is migrated and live.** Content is a faithful clone in the new architecture. Structure work is in: shared snippets for repeated text, chapters consolidated into pages. Trimming and new writing come in the Refine phase | ✅ Confirmed 10 Oct |

---

## 5. Architecture

### 5.1 The road a page travels

```
 ✍️ WRITER                  🐙 GITHUB (Manual repo)                     🌐 WEBFLOW
┌──────────────┐  save   ┌────────────────────────────────────┐
│ Pages CMS    │────────▶│ branch: docs2/tier1-getting-started│
│ form + text  │ commit  │  content/getting-started/*.md      │
│ drop image   │         │  images/_inbox/  (dropped files)   │
└──────────────┘         └───────────────┬────────────────────┘
                                         │ pull request
                                         ▼
                         ┌────────────────────────────────────┐
                         │ ⚙️ GitHub Actions                   │
                         │  1. check front matter, links, alt │
                         │  2. image bot: name, WebP, dedupe  │
                         │  3. render preview (same styles)   │
                         │  4. comment: ✅ checks + 👀 link    │
                         └───────────────┬────────────────────┘
                                         │ reviewer approves + merge
                                         ▼
                         ┌────────────────────────────────────┐      ┌────────────────────┐
                         │ 🔄 sync.py                          │─────▶│ CMS: Doc Pages      │
                         │  Markdown → HTML (doc kit classes)  │ API  │ CMS: Doc Snippets   │
                         │  images → Webflow assets            │      │ CMS: Doc Sections   │
                         │  checksum guard                     │      │ template + docs.js  │
                         └────────────────────────────────────┘      │ ➜ webflow.io only   │
                                                                      └────────────────────┘
```

### 5.2 Repository layout (Tier 1)

```
docs2/
├── content/
│   └── getting-started/
│       ├── index.md                 # section overview
│       ├── introduction.md
│       ├── using-the-documentation.md
│       ├── installation.md
│       ├── quick-start.md           # new
│       ├── data-structure.md
│       ├── comparing-to-blender.md  # new
│       └── migrating-from-blender.md# new
├── snippets/                        # shared sections
├── images/
│   ├── _inbox/                      # drops land here, the bot empties it
│   └── ui/…  getting-started/…
├── nav.yml                          # sidebar order + icons (generated, editable)
├── tools/
│   ├── convert.py                   # Spike 1 converter → plain-writing output
│   ├── patterns.py                  # NEW: recognises plain patterns → components
│   ├── check.py                     # NEW: front matter, links, alt text
│   ├── image_bot.py                 # NEW: inbox → library
│   ├── render.py                    # NEW: Markdown → HTML (shared by preview + sync)
│   └── sync.py                      # NEW: HTML → Webflow CMS
└── plans/                           # this document + the usability test
.github/workflows/docs2.yml          # checks, bot, preview
.pages.yml                           # Pages CMS form
```

### 5.3 What a writer sees and writes

The **form** (Pages CMS fields) — picking, not typing:

```yaml
title: "Installation"
status: needs-review            # dropdown: draft · needs-review · reviewed
video: "https://youtu.be/…"     # optional chapter video
examples: [examples/getting-started/first-scene.blend]   # downloads shown on the page
shared: [snippets/menus/quick-menu.md]                   # shared sections this page shows
```

The **text** — plain writing; the right column is what the build makes of it:

```markdown
## Install on Windows                         → heading, sidebar anchor

Press Ctrl + Alt + Delete …                   → :kbd keycaps (recognised)
Open Edit › Preferences › System              → menu path chips (recognised)

> Tip: Keep the old version until …          → Tip callout (recognised)

![Installer window](installer.png)            → small image floats right (by size)

https://youtu.be/abc123                       → video embed (link on its own line)
```

### 5.4 One CMS item, as the sync script sends it

```json
{
  "fieldData": {
    "name": "Installation",
    "slug": "installation",
    "page-id": "getting-started.installation",
    "section": "<Doc Sections item id>",
    "order": 30,
    "icon": "import",
    "summary": "Download, install and start Bforartists on Windows, Linux and macOS.",
    "body": "<h2 id=\"install-on-windows\">…</h2><div class=\"ui-doc-callout is-tip\">…</div>",
    "video": "https://youtu.be/abc123",
    "snippets": ["<Doc Snippets item id>"],
    "version": "5.1",
    "status": "needs-review",
    "source-path": "docs2/content/getting-started/installation.md",
    "checksum": "sha256:3f9a…"
  }
}
```

---

## 6. Implementation Plan

### Phase 0 — This Document

- [x] Write `docs2/plans/plan_docs2_tier1_getting_started.md` and `usability_test_getting_started.md`.
- [x] 👤 **You:** approved 10 Oct.

### Phase 1 — Getting Started Content

**Goal:** 8 Getting Started pages in plain writing, readable on GitHub as they are, with **every word
of the source kept** (faithful clone, D13).

**Files:** `docs2/tools/convert.py`, `docs2/tools/pages.json`, `docs2/content/getting-started/*`, `docs2/nav.yml`

- [x] Switch converter output from tags to plain patterns (`:::tip` → `> Tip:`, `{.right}` → size rule,
      `:kbd[…]` → plain `Ctrl + Space`).
- [x] Add the Getting Started pages to `pages.json`; consolidate `1.1` + `38` into
      *Using the Documentation* (two sections, text unchanged).
- [x] Pull the existing Webflow text for Introduction, About Documentation, Quick Start, Comparing and
      Migrating; where a page has no source chapter, the website text is the source.
- [x] ♻️ Repeated text becomes a shared snippet, word for word (the longest copy wins; differences are
      flagged for you, never dropped).
- [x] 🚫 No trimming or rewording (D13). Only fixes that keep meaning: broken headings, image placement,
      numbering.
- [x] Word-count check per page: converted words + words moved to snippets ≥ source words (report in
      the pull request).
- [x] Generate `nav.yml` (order + icon per page) from `pages.json`.

```yaml
# nav.yml (generated, editable)
- section: getting-started
  title: Getting Started
  icon: getting-started
  pages:
    - { id: getting-started.introduction, title: Introduction, icon: blender }
    - { id: getting-started.using-the-documentation, title: Using the Documentation, icon: documentation }
    - { id: getting-started.installation, title: Installation, icon: import }
    - { id: getting-started.quick-start, title: Quick Start, icon: quickstart }
```

**Done 10 Oct — how it came out:**

- 🔗 Website addresses and titles kept: `/documentation/overview/…`, *About Documentation*, *Comparing to Blender* (`differences`).
- 🌐 Introduction and About Documentation: your newer website text first, then the `.odt` text word for word under
  "From the .odt manual", to merge in the Refine phase. `38 About this Manual` is consolidated into About Documentation.
- 📄 Installation and Data Structure: from `.odt` chapters 2 and 31 (the website pages were placeholders).
- 📝 Quick Start, Comparing to Blender, Migrating: no text exists yet; each keeps its one-line website summary and a note.
- ✅ Word check: 23 of 23 groups keep every word ([`reports/wordcount.md`](../reports/wordcount.md)).
- 🖼️ Website images stay as links to the Webflow CDN for now; icons in `nav.yml` are empty until the icon map (Phase 2).

**Acceptance:** all 8 pages open on GitHub with no visible markup noise; images show; no source text lost.

### Phase 2 — Writer Workflow in the Browser

**Goal:** a writer edits and saves a page in the browser in under 2 minutes, without help.

**Files:** `.pages.yml`

- [ ] Point `.pages.yml` at `docs2/content/getting-started` and `docs2/images/_inbox`.
- [ ] Add form fields: `video` (string), `examples` (file, multiple), `shared` (reference → snippets).
- [ ] 👤 **You:** install the Pages CMS GitHub App on `Bforartists/Manual` (only you can grant it).
- [ ] Push the branch (with your OK) so Pages CMS can see it.
- [ ] Test: does `> Tip:`, `Ctrl + Space`, `Edit › Preferences` survive a save unchanged?
- [ ] Score the three ways to write (Pages CMS online · GitHub web editor · clone + your own editor) on: no installs, WYSIWYG, drag and drop of images, ease of inserting a tip or video, fun. Recommend one as the advertised way.

```yaml
# .pages.yml — additions
      - name: video
        label: Chapter video (YouTube link)
        type: string
      - name: examples
        label: Example files to download
        type: file
        list: true
      - name: shared
        label: Shared sections on this page
        type: reference
        options:
          collection: snippets
          multiple: true
```

**Acceptance:** a save in Pages CMS produces a clean one-file diff; plain patterns unchanged.

### Phase 3 — Checks, Image Bot and Preview

**Goal:** every pull request answers "is it correct?" and "how will it look?" automatically.

**Files:** `.github/workflows/docs2.yml`, `docs2/tools/check.py`, `image_bot.py`, `render.py`, `patterns.py`

- [ ] `check.py` — front matter schema, internal links, image exists, alt text present, repeat scan.
- [ ] `image_bot.py` — move `_inbox/*` to `images/<section>/<page>/<heading>.webp`, resize, dedupe
      by hash, rewrite links, commit back to the pull request branch.
- [ ] `patterns.py` — the plain-writing recogniser (shared by preview and sync).
- [ ] `render.py` — Markdown → HTML with doc kit classes, wrapped in the live site's CSS.
- [ ] Publish the preview to GitHub Pages under `/preview/<pr-number>/`.
- [ ] Bot comment on the pull request: checks ✅/❌, filed images, 👀 preview link.

```python
# patterns.py — the heart of "plain writing"
KBD  = re.compile(r"\b((?:Ctrl|Shift|Alt|Cmd)(?:\s*\+\s*(?:Ctrl|Shift|Alt|Cmd))*\s*\+\s*\w+)")
MENU = re.compile(r"\b([A-Z][\w ]+?)(?:\s*[›>]\s*[A-Z][\w ]+?){1,5}\b")
TIP  = re.compile(r"^>\s*(Tip|Note|Warning|Important):\s*", re.M)

def enhance(html: str, facts: dict) -> str:
    html = KBD.sub(lambda m: keycaps(m.group(1)), html)
    html = MENU.sub(lambda m: menu_chips(m.group(0), facts["menus"]), html)  # only real menu names
    html = callouts(html)                 # blockquote "Tip:" → <div class="ui-doc-callout is-tip">
    html = float_images_by_size(html)     # < 900 px wide → .is-right, else full width
    html = youtube_links_to_embeds(html)  # bare link on its own line → video component
    return html
```

```yaml
# .github/workflows/docs2.yml (outline)
on:
  pull_request:
    paths: ["docs2/**", ".pages.yml"]
jobs:
  docs:
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, pages: write }
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r docs2/tools/requirements.txt
      - run: python docs2/tools/image_bot.py --commit     # files dropped images
      - run: python docs2/tools/check.py                  # fails the PR on errors
      - run: python docs2/tools/render.py --out _preview  # same styles as the site
      # deploy _preview to GitHub Pages /preview/<pr>/ and post the comment
```

**Acceptance:** a test pull request with one dropped image and one broken link → bot files the image,
the check fails on the link, the preview link opens and looks like the site.

### Phase 4 — Webflow Template and Collections

**Goal:** the reader experience, built once, on staging.

**Where:** Webflow Designer (Bforartists site), using the Template page components

- [ ] Collections: `Doc Sections`, `Doc Pages` (fields as §5.4), `Doc Snippets`.
- [ ] Doc Pages template built **on the existing Webflow docs structure** (panels, sidebar, toolbar
      Panels · Print · Focus), keeping the earlier decisions: panel sidebar with sub-chapter anchors,
      sticky section path and right outline; plus section hero, page info strip, previous/next.
- [ ] Doc kit classes on the Template page: callout, keycaps, menu chips, image float, video, step.
- [ ] Docs script v1 (`BFA Docs`): sidebar from `nav.json`, right outline, sticky path, mobile bar,
      focus, panels fold, snippet placement, viewer text size.
- [ ] Print stylesheet (hide sidebars, open folds, page footer with version + address).
- [ ] Docs home: Getting Started tile links to the new section (your current home stays).

**Acceptance:** with 1 hand-made test item, the template renders correctly on desktop, phone and print.

### Phase 5 — Sync to Webflow Staging

**Goal:** merge on the branch → Getting Started appears on bforartists.webflow.io.

**Files:** `docs2/tools/sync.py`, `.github/workflows/docs2.yml` (sync job, manual trigger first)

- [ ] Create or update items by `page-id`; never by name.
- [ ] Upload new images to Webflow assets once (hash cache), rewrite `src`.
- [ ] Checksum guard: if the item in Webflow differs from the last sync, stop and report.
- [ ] Publish to the **webflow.io subdomain only**; custom domains never.
- [ ] Redirect stubs from the old static Getting Started pages (list only, applied at launch).

```python
# sync.py — the safe core
item = find_item(collection, page_id)            # by our ID, never by name
if item and item["fieldData"]["checksum"] != last_synced[page_id]:
    raise SyncStopped(f"{page_id} was edited in Webflow — not overwriting")
body = render_page(md_path)                      # same render.py as the preview
upsert(collection, page_id, field_data(body))    # POST /v2/collections/{id}/items | PATCH …/items/{item_id}
publish_site(site_id, custom_domains=[], webflow_subdomain=True)   # staging only
```

**Acceptance:** run the sync twice — first run creates 8 items, second run changes nothing; a manual
edit in Webflow makes the next sync stop with a clear message.

### Phase 6 — Usability Test, Fixes, Pull Request

**Goal:** real people confirm it is easy to write and good to read.

- [ ] Run [`usability_test_getting_started.md`](usability_test_getting_started.md) with 2 writers and
      3 readers (one on a phone).
- [ ] Fix every ❌ that blocks a task; log the rest.
- [ ] 👤 **You:** decide whether insert buttons are needed (D3).
- [ ] Open the pull request `docs2/tier1-getting-started` → `docs2/spike1-migration` (or `master`, your call).

**Acceptance:** every writer task passes without help; readers find answers in ≤ 3 clicks.

---

## 7. Files Touched

| File | Change |
|---|---|
| `docs2/tools/convert.py` | Plain-pattern output; Getting Started pages |
| `docs2/tools/pages.json` | + 8 Getting Started entries |
| `docs2/tools/patterns.py` | **NEW** — plain writing → components |
| `docs2/tools/check.py` | **NEW** — front matter, links, alt text, repeats |
| `docs2/tools/image_bot.py` | **NEW** — inbox → library |
| `docs2/tools/render.py` | **NEW** — Markdown → HTML (preview + sync) |
| `docs2/tools/sync.py` | **NEW** — Webflow CMS sync, staging only |
| `docs2/tools/requirements.txt` | **NEW** — pinned Python deps |
| `docs2/content/getting-started/*.md` | **NEW** — 8 pages |
| `docs2/nav.yml` | **NEW** — sidebar order + icons |
| `.pages.yml` | Paths + form fields |
| `.github/workflows/docs2.yml` | **NEW** — checks, bot, preview, sync (manual) |
| Webflow: 3 collections, 1 template, `BFA Docs` script, print CSS | **NEW** on staging |

---

## 8. Verification Plan

### 8.1 Automated (every pull request)

| Check | Fails the PR when |
|---|---|
| Front matter | Missing `id`, `title`, `section`, or unknown `status` |
| Links | Internal link or anchor does not exist |
| Images | File missing, no alt text, or > 4 MB after the bot |
| Repeats | New text ≥ 60% identical to existing text (warning, not failure) |
| Render | Any page fails to render |

### 8.2 Testing Guide

#### Phase 1 — Content

| Step | Expected Result |
|---|---|
| Open `installation.md` on GitHub | Reads cleanly, images show, no `:::` or `{…}` noise |
| Compare with `2 Installing Bforartists.odt` | Every sentence and image still there (faithful clone) |

#### Phase 2 — Writer workflow

| Step | Expected Result |
|---|---|
| Edit a sentence in Pages CMS, Save | One commit, one changed line |
| Type `> Tip: …` and `Ctrl + S`, Save | Saved text unchanged in the file |
| Pick a shared section in the form | `shared:` list updated; text not touched |

#### Phase 3 — Checks + preview

| Step | Expected Result |
|---|---|
| Drop `Screenshot 2026-10-12.png` under "Install on Windows" | Bot files it as `…/installation/install-on-windows.webp` and comments |
| Add a link to a missing page | Check fails, names the line |
| Open the 👀 preview link | Page looks like the website (fonts, callouts, keycaps) |

#### Phase 4–5 — Webflow

| Step | Expected Result |
|---|---|
| Run sync | 8 items on staging, sidebar in `nav.yml` order |
| Run sync again | "0 changed" |
| Edit an item by hand in Webflow, run sync | Sync stops: "edited in Webflow — not overwriting" |
| Open a page on a phone | Bottom bar; Chapters and outline open as sheets |
| Print a page | No sidebars, folds open, footer with version + address |

### 8.3 People

→ [`usability_test_getting_started.md`](usability_test_getting_started.md)

---

## 9. Risks & Mitigations

| Risk | Effect | Mitigation |
|---|---|---|
| Pages CMS rich-text editor rewrites plain patterns (escapes `>`, `›`, `+`) | Patterns lost on save | Phase 2 test first; fall back to Source mode or alternate characters |
| Webflow rich text rejects our classes or embeds | Components missing | Phase 4 test item; fallback: markers swapped by the docs script |
| Webflow rich text has no tables | Property tables break | Table component or script-built table from JSON |
| GitHub Pages preview needs Pages enabled on the repo | No preview links | Enable for the repo, or upload the preview as an artifact |
| Image bot commits to a writer's branch | Surprise commits | Bot commits only to pull request branches, with a clear message |
| Webflow API rate limits | Slow sync | Changed items only; batches |
| Contributors confused by two editors | Drop-off | Pages CMS is the only advertised editor; GitHub pencil for typos |

---

## 10. Out of Scope

- 🚫 Trimming, rewording, new writing — Refine phase, after the full migration is live (D13).
- 🚫 Other sections (Interface, Editors…) — Tier 2 onwards.
- 🚫 Extractor, release diff, capture script, example scenes — Tier 3 (automation).
- 🚫 Release PDFs and the Documentation History page — Tier 3.
- 🚫 Algolia search, redirects applied, going live — launch tier.
- 🚫 Insert buttons (Sveltia CMS) — only if Phase 6 says so.
- 🚫 Spanish.

---

## 11. Open Questions

| # | Question | Default if no answer |
|---|---|---|
| Q1 | Push the branch to GitHub now so Pages CMS can see it? | Wait for your OK |
| Q2 | Pull request target: `docs2/spike1-migration` or `master`? | `docs2/spike1-migration` |
| Q3 | Who are the 2 writers and 3 readers for the test? | You + community volunteers from Discord |
| Q4 | Convert screenshots to WebP? | Yes |
| Q5 | Enable GitHub Pages on the Manual repo for previews? | Yes, `gh-pages` branch |
