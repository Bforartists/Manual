# Bforartists Docs 2.0 — Usability Test: Getting Started

> 🧪 **Purpose:** check with real people that Docs 2.0 is **easy to write** and **good to read**,
> before we convert any other section. Run it at the end of Tier 1, Phase 6.

**Date**: 2026-10-10

**Status**: 📝 Ready to run once Tier 1 Phases 1–5 pass

**Belongs to**: [`plan_docs2_tier1_getting_started.md`](plan_docs2_tier1_getting_started.md)

**Where**: bforartists.webflow.io (staging) + Pages CMS on the test branch

**Time**: ~30 min per writer · ~20 min per reader

---

## Table of Contents

1. [What We Want to Learn](#1-what-we-want-to-learn)
2. [Who Takes Part](#2-who-takes-part)
3. [Setup Checklist](#3-setup-checklist)
4. [How to Run a Session](#4-how-to-run-a-session)
5. [Writer Tasks](#5-writer-tasks)
6. [Reader Tasks](#6-reader-tasks)
7. [After Each Session: Questions](#7-after-each-session-questions)
8. [Scoring](#8-scoring)
9. [Final Checklist: Ready for Tier 2?](#9-final-checklist-ready-for-tier-2)
10. [Results Log](#10-results-log)

---

## 1. What We Want to Learn

| # | Question | Answered by |
|---|---|---|
| L1 | Can a first-time writer fix and add content **without help**? | Writer tasks W1–W5 |
| L2 | Does plain writing survive the editor, so nobody needs to learn tags? | W3, W4 |
| L3 | Is the preview link enough, or do writers want insert buttons? | W5 + question A4 |
| L4 | Can a new artist **find** what they need fast? | Reader tasks R1–R3 |
| L5 | Does it read and work well on a **phone** and in **print**? | R4, R5 |
| L6 | Does it feel like Bforartists: visual, icon-led, friendly? | Questions B1–B3 |

---

## 2. Who Takes Part

| Role | How many | Profile |
|---|---|---|
| ✍️ Writer | 2 | One who has edited the `.odt` manual · one who never has |
| 📖 Reader | 3 | A new artist · a Blender user moving over · one on a phone |
| 👀 Observer | 1 | You (or a helper): watch, time, note — **do not help** |

---

## 3. Setup Checklist

- [ ] Getting Started is synced to staging (8 pages)
- [ ] Pages CMS is installed on the repo and shows the test branch
- [ ] Each writer has a GitHub account and has been invited to the repo
- [ ] A test pull request exists so writers can see a bot comment and preview link
- [ ] A screenshot is ready on the writer's computer (any Bforartists window)
- [ ] Staging link and a phone ready for the phone reader
- [ ] A copy of the [Results Log](#10-results-log) to fill in
- [ ] Screen recording on (with permission), or notes by the observer

---

## 4. How to Run a Session

1. 👋 Say: *"We are testing the docs, not you. Think out loud. If you get stuck, that's what we want to find."*
2. 📋 Give one task at a time, read it out, start the timer.
3. 🤐 Don't help. If stuck for 3 minutes, note it as ❌ and move on.
4. ✏️ Note: time, where they hesitated, what they said.
5. 💬 Ask the questions in §7 at the end.

---

## 5. Writer Tasks

| # | Task (read this out) | ✅ Pass when | ⏱️ Target |
|---|---|---|---|
| W1 | "On the Installation page, the word *instal* is misspelled. Fix it." | Fixed and saved from Pages CMS, without asking where | 2 min |
| W2 | "Add a sentence under *Install on Linux* saying the AppImage needs execute permission." | Sentence saved under the right heading | 3 min |
| W3 | "Add a tip that says to keep the old version until the new one works." | A callout appears in the preview, no tag syntax used | 3 min |
| W4 | "Write that the user should press Ctrl + Comma to open Preferences, via Edit › Preferences." | Keycaps and menu chips appear in the preview | 3 min |
| W5 | "Add your screenshot under *First start*." | Dragged in and saved; bot files it; it shows in the preview | 4 min |
| W6 | "Open the preview link and check your changes." | Finds the bot comment and the link on the pull request | 2 min |
| W7 | "Mark the page as ready for review." | `status` changed in the form | 1 min |

**Observer notes per task:** time · hesitations · words used ("where is…", "how do I…") · errors.

---

## 6. Reader Tasks

| # | Task (read this out) | ✅ Pass when | 🖱️ Target |
|---|---|---|---|
| R1 | "You just downloaded Bforartists. Find out how to install it on your system." | Reaches the right part of Installation | ≤ 3 clicks |
| R2 | "You know Blender. Find out what is different in Bforartists." | Reaches Comparing to Blender or Migrating | ≤ 3 clicks |
| R3 | "Find where your settings and files are stored." | Reaches the Data Structure section | ≤ 3 clicks |
| R4 | 📱 *On a phone:* "Jump to another chapter, then back to a heading on this page." | Uses the bottom bar; no zooming or side scrolling | — |
| R5 | "Print the Installation page or save it as a PDF." | Uses the Print button; PDF has no sidebars, text selectable | — |
| R6 | "Search for *preferences*." | Finds a result (search box or F3) | ≤ 2 actions |

---

## 7. After Each Session: Questions

**A · Writers**

| # | Question | Scale / answer |
|---|---|---|
| A1 | How easy was it to make your changes? | 1 (hard) – 5 (easy) |
| A2 | Compared with editing the `.odt` in LibreOffice, is this… | worse · same · better |
| A3 | Did anything feel like "code"? What? | open |
| A4 | Was the preview link enough, or would you want insert buttons for tips, videos, keys? | preview enough · want buttons |
| A5 | Would you do this again for fun, for 15 minutes? | yes · maybe · no |

**B · Readers**

| # | Question | Scale / answer |
|---|---|---|
| B1 | How easy was it to find things? | 1 – 5 |
| B2 | Did the pages feel visual and clear, or text-heavy? | 1 (text-heavy) – 5 (visual) |
| B3 | Does it feel like Bforartists? | 1 – 5 |
| B4 | One thing you would change? | open |

---

## 8. Scoring

| Result | Meaning | Action |
|---|---|---|
| ✅ Pass | Done within target, no help | Keep |
| 🟡 Pass with friction | Done, but slow or hesitant | Improve wording, layout or bot message |
| ❌ Fail | Not done within 3 minutes of being stuck | **Must fix** before Tier 2 |

**Success bar for Tier 1:**

- [ ] Every writer task ✅ or 🟡 for both writers; **no ❌**
- [ ] A1 average ≥ 4 · A2 "better" from at least one writer
- [ ] Every reader task ✅ for at least 2 of 3 readers
- [ ] B1 and B2 average ≥ 4

---

## 9. Final Checklist: Ready for Tier 2?

**✍️ Contributor side**

- [ ] Editing, adding text and a tip take no tags or code
- [ ] A dropped screenshot is filed, named and sized by the bot
- [ ] Every pull request shows checks and a preview link
- [ ] Shared sections can be added from the form
- [ ] No step required the terminal, LibreOffice or a manual upload
- [ ] Decision made on insert buttons (D3)

**📖 Reader side**

- [ ] All 8 Getting Started pages on staging, in sidebar order, with icons
- [ ] Callouts, keycaps, menu chips, images and video render
- [ ] Sidebar, outline, sticky path, previous/next work
- [ ] Phone: bottom bar works, no side scrolling, tables scroll in their box
- [ ] Print: clean page, version and address in the footer
- [ ] Page loads fast on a phone connection

**⚙️ Maintenance side**

- [ ] Sync run twice: second run changes nothing
- [ ] Manual edit in Webflow is detected, not overwritten
- [ ] Nothing published beyond bforartists.webflow.io
- [ ] Every finding is logged below with an owner

---

## 10. Results Log

| Date | Person (role) | Task | Result | Time | Note | Fix owner |
|---|---|---|---|---|---|---|
| | | | ✅ / 🟡 / ❌ | | | |
