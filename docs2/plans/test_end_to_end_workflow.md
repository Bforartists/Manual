# 🧪 End-to-End Test: From a New Chapter to the Website

> 🎯 **Goal:** one person, one browser, no installs. Make a chapter with two sub-chapters and every kind of
> content, send it through a pull request, and see it on **bforartists.webflow.io**.
> Nothing in this test can reach the live site, bforartists.co.

**Time:** about 30 minutes · **Section used:** 🧪 *Doc Kit (test)*, which is not part of the real manual

**Plan:** [`plan_docs2_tier1_getting_started.md`](plan_docs2_tier1_getting_started.md), Phase 5

---

## 🗺️ The road

```
 1 🌿 branch → 2 📁 chapter → 3 📄 sub-chapters → 4 ✍️ content → 5 🖼️ images → 6 💾 save
                                                                                   │
 9 ✅ confirm ← 8 🌐 website ← 7 🔀 pull request + merge (publishes staging) ←─────┘
```

---

## 🔑 Before you start (one time, 5 minutes)

- [ ] **Merge the Phase 5 pull request** (`docs2/tier1-phase5` → `docs2/tier1-getting-started`). The tools must be on
      the working branch first.
- [ ] **Make a Webflow API key:** in Webflow, open the Bforartists site's **Site settings → Apps & integrations →
      API access → Generate API token**. Name it `Docs sync`. Permissions: **CMS: Read and write** and
      **Sites: Read and write** (needed to publish staging). Copy the token.
- [ ] **Give it to GitHub:** `Bforartists/Manual` → **Settings → Secrets and variables → Actions →
      New repository secret**. Name: `WEBFLOW_TOKEN`. Paste the token. **Add secret**.

> 💡 The token lives only in GitHub's secret store. Nobody can read it back, not even in the logs.

---

## 1. 🌿 Make a branch for your test

- [ ] On GitHub, open `Bforartists/Manual`. Click the branch button (top left, it says `master`).
- [ ] Type `docs2/test-chapter`. Click **Create branch docs2/test-chapter from docs2/tier1-getting-started**.
      (If it says *from master*, first switch the branch button to `docs2/tier1-getting-started`, then type the name.)
- [ ] Open [Pages CMS](https://app.pagescms.org/Bforartists/Manual). In the branch picker (top left), choose
      `docs2/test-chapter`.

✅ Pages CMS shows **📘 Documentation pages** for your new branch.

## 2. 📁 Make a chapter

- [ ] Open **📘 Documentation pages → Doc Kit (test)**.
- [ ] Click **Create folder**. Name it `my-first-chapter`.
- [ ] Inside that folder, click **Add an entry**. Title: `My first chapter`.
- [ ] Change the file name to `index.md`. (A folder's `index.md` is the chapter itself.)
- [ ] Type one sentence, for example *This chapter tries every kind of content.* Click **Save**.

✅ The chapter shows in the tree under *Doc Kit (test)*.

## 3. 📄 Make two sub-chapters

- [ ] Inside `my-first-chapter`, click **Add an entry**. Title: `Part one`. Keep the file name (`part-one.md`).
      Type one sentence. **Save**.
- [ ] Do the same for `Part two`.

✅ Both sub-chapters show inside the chapter folder.

## 4. ✍️ Try every kind of content (in *My first chapter*)

Press `/` on an empty line for the menu. Tick each one as you add it:

| ✓ | Content | How |
|---|---|---|
| [ ] | 🔤 Heading | `/` → **Heading 2** → `Text` |
| [ ] | **Bold** and *italic* | Select a word, `Ctrl + B` / `Ctrl + I` |
| [ ] | • Bullet list | `/` → **Bulleted list** |
| [ ] | 1. Numbered steps | `/` → **Numbered list** |
| [ ] | 💡 Tip | `/` → **Quote** → type `Tip: Try this.` |
| [ ] | 📝 Note | `/` → **Quote** → `Note: Good to know.` |
| [ ] | ⚠️ Warning | `/` → **Quote** → `Warning: Careful.` |
| [ ] | 🟣 Important | `/` → **Quote** → `Important: Read this first.` |
| [ ] | ⌨️ Keys | Type `Save with Ctrl + S.` |
| [ ] | 🧭 Menu path | Type `Open Edit › Preferences › Interface.` (copy the `›`) |
| [ ] | 🔎 Find it | Type `Find it: View › Sidebar`, then make `Find it:` bold |
| [ ] | 🏷️ Version label | Type `[New in 5.1] Something new.` |
| [ ] | ➡️ Go button | On its own line: select the text `Next: Part one`, click the link button, type `part-one.md` |
| [ ] | 📋 Table | `/` → **Table**, fill two rows |
| [ ] | 💻 Code | `/` → **Code block**, type two lines |
| [ ] | 🎬 Video | Paste a YouTube link on its own line |
| [ ] | ♻️ Shared section | In the form at the top, pick **Quick menu** in *Shared sections on this page* |

## 5. 🖼️ Add two images

- [ ] Drag a **wide** screenshot (wider than 900 px) into the page. It will show full width.
- [ ] Drag a **small** screenshot (narrower than 900 px) into the page. It will float on the right.
- [ ] Click each image and change its alt text from the file name to what it shows, for example
      *The Preferences window, Interface tab*. (If you forget, the bot uses the heading above.)

## 6. 💾 Save

- [ ] Click **Save**.
- [ ] On GitHub, open the branch `docs2/test-chapter` → **commits**. Your save is there with your name.
- [ ] Wait about 2 minutes, then refresh. A bot commit appears:
      *docs: fill page headers and file new images [docs-bot]*.

✅ Your images moved from `images/_inbox/` to `images/doc-kit/my-first-chapter/…`, and your three pages got their
hidden fields (ID, section, breadcrumb).

## 7. 🔀 Pull request, then merge

- [ ] On GitHub: **Compare & pull request**. **Base: `docs2/tier1-getting-started`** ← compare: `docs2/test-chapter`.
      ⚠️ Not `master`.
- [ ] Wait for the bot comment. Click **👀 Open the preview** and check your chapter. In the sidebar, *Part one* and
      *Part two* should sit indented under *My first chapter*.
- [ ] Happy? **Merge pull request**. Merging is the publish button: the run on the working branch now sends the
      pages to Webflow and publishes staging.

## 8. 🌐 See it on the website

- [ ] On GitHub: **Actions → Docs 2.0 checks and preview** → the newest run on `docs2/tier1-getting-started`.
      Its summary ends with **🌐 Webflow sync**: 3 items created, and *🚀 Published to staging*.
- [ ] Open https://bforartists.webflow.io/docs/doc-kit-my-first-chapter
- [ ] Then the sub-chapters: `/docs/doc-kit-my-first-chapter-part-one` and `…-part-two`.

## 9. ✅ Confirm it worked

| ✓ | Check on the website |
|---|---|
| [ ] | 🧭 Sidebar: *Doc Kit (test)* → *My first chapter* with *Part one* and *Part two* indented under it |
| [ ] | ⏮️⏭️ Previous / next at the bottom go chapter → part one → part two |
| [ ] | 💡📝⚠️🟣 Four callouts, each in its own colour |
| [ ] | ⌨️ Keycaps for `Ctrl + S`; 🧭 a menu chip for *Edit › Preferences › Interface* |
| [ ] | 🔎 *Find it* row and 🏷️ *New in 5.1* label |
| [ ] | 🖼️ Wide image full width, small image floated right; both load from Webflow's CDN |
| [ ] | 📋 Table and 💻 code block with its language label |
| [ ] | 🎬 Video plays, with *Watch on YouTube* under it |
| [ ] | ♻️ The Quick menu section at the end of the page |
| [ ] | ➡️ *Next: Part one →* is a button and opens Part one |
| [ ] | 📝 *Edit this page* opens the page source on GitHub |
| [ ] | 🔒 bforartists.co is unchanged (no Doc Kit pages there) |

**Extra checks (optional)**

- [ ] 🔁 **Nothing changes twice:** in GitHub, **Actions → Docs 2.0 checks and preview → Run workflow** on
      `docs2/tier1-getting-started`. The sync says *unchanged* for everything.
- [ ] ✋ **Hand edits are protected:** change one word of *Part two* in Webflow's CMS, wait 10 minutes, edit *Part two*
      in Pages CMS and merge. The sync skips it and says *edited by hand in Webflow*.

---

## 📝 Notes for the test

| | |
|---|---|
| 🔁 | Saving in Pages CMS **straight on `docs2/tier1-getting-started`** also publishes staging (no pull request). For reviewed work, use a branch as in step 1. |
| 🧹 | The sync never deletes. The earlier hand-made Doc Kit pages in Webflow stay; the summary lists them as *not in the repo*. |
| 🖼️ | Images are copied to Webflow's CDN on the first sync, so the website does not depend on GitHub to show them. |
| 🐛 | Anything odd: screenshot it, note the step number, and send it to me. |
