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

## 🔑 Before you start (one time, about 10 minutes)

Do these **in this order**. The token goes in first, so that the push in step C already does the first real sync
and you can watch it work before the test.

### A. 🔐 Make a Webflow API token

The token is a password that lets GitHub write the docs into Webflow's CMS for this one site only.

- [ ] Open the Webflow dashboard. On the **Bforartists** site card, click **⋯ → Settings**
      (or, in the Designer, the **W** menu → **Site settings**).
- [ ] In the left menu: **Apps & integrations**. Scroll down to **API access**.
- [ ] Click **Generate API token**.
- [ ] **Name:** `Docs sync (GitHub)`.
- [ ] **Access:** set two lines and leave everything else on **No access**:

      | API | Access | Why |
      |---|---|---|
      | **CMS** | Read and write | create and update the Doc Sections, Doc Snippets and Doc Pages items |
      | **Sites** | Read and write | publish the **webflow.io** staging site after a sync |

- [ ] Click **Generate token**. **Copy it now** and keep the tab open until step B is done. Treat it like a password:
      don't paste it in chats, issues or files.

> 💡 The token stays valid until you revoke it, or until it goes unused for 365 days. The sync uses it on every
> merge, so it won't expire in practice. To revoke: the same **API access** list → the token → **Revoke**.

### B. 🗝️ Give the token to GitHub

- [ ] Open https://github.com/Bforartists/Manual/settings/secrets/actions
      (**Settings → Secrets and variables → Actions**).
- [ ] Click **New repository secret**.
- [ ] **Name:** `WEBFLOW_TOKEN` (exactly this, in capitals). **Secret:** paste the token.
- [ ] Click **Add secret**. It shows in the list as `WEBFLOW_TOKEN`, with the value hidden.

> 💡 Nobody can read a secret back, not even you; the logs show `***` in its place. To change it later, click
> the pencil next to it and paste a new token.

### C. ⬆️ Push `docs2/main`

`docs2/main` exists only on your computer for now. It holds Tier 1, Phase 5, the Tier 2 groundwork and the plans.

- [ ] In VS Code, click the branch name at the bottom left and choose **docs2/main**.
- [ ] Click **Publish Branch** (the cloud button in the Source Control view, or the same spot at the bottom left).

### D. 👀 Watch the first sync (the warm-up)

- [ ] On GitHub: **Actions → Docs 2.0 checks and preview**. The newest run is on `docs2/main`. Wait for the green ✓
      (about 2–3 minutes).
- [ ] Open the run. Its summary ends with **🌐 Webflow sync**: about **30 pages created or updated** (Getting
      Started, the Interface and Editors samples, Doc Kit; pages made by hand earlier are updated, not doubled) and **🚀 Published to staging**.
- [ ] Open https://bforartists.webflow.io/docs/getting-started-introduction. It shows the page from the repo.

> ⚠️ **Publishing staging publishes the whole webflow.io site,** including any unfinished Designer work from the
> template session. bforartists.co is never touched. If the template is mid-change, finish or undo it first.

**If something goes wrong**

| You see | Do this |
|---|---|
| ⚠️ *WEBFLOW_TOKEN is not set; nothing was sent to Webflow* | The secret is missing or misspelled. Redo step B, then open the run → **Re-run all jobs**. |
| ❌ *401* or *Unauthorized* in the sync step | The token was copied wrong or revoked. Make a new one (A), update the secret (B), re-run. |
| ❌ *403* or *missing scopes* | The token lacks **CMS** or **Sites** write access. Make a new one with both (A). |
| ❌ The push is refused with *workflow* in the message | VS Code's GitHub sign-in lacks the *workflow* permission. Sign out of GitHub in VS Code (Accounts menu, bottom left), sign in again, push again. |
| 🟡 The sync step is skipped | The checks failed. The summary lists the problems; send them to me. |

---

## 1. 🌿 Make a branch for your test

- [ ] On GitHub, open `Bforartists/Manual`. Click the branch button (top left, it says `master`).
- [ ] Type `docs2/test-chapter`. Click **Create branch docs2/test-chapter from docs2/main**.
      (If it says *from master*, first switch the branch button to `docs2/main`, then type the name.)
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

- [ ] On GitHub: **Compare & pull request**. **Base: `docs2/main`** ← compare: `docs2/test-chapter`.
      ⚠️ Not `master`.
- [ ] Wait for the bot comment. Click **👀 Open the preview** and check your chapter. In the sidebar, *Part one* and
      *Part two* should sit indented under *My first chapter*.
- [ ] Happy? **Merge pull request**. Merging is the publish button: the run on the working branch now sends the
      pages to Webflow and publishes staging.

## 8. 🌐 See it on the website

- [ ] On GitHub: **Actions → Docs 2.0 checks and preview** → the newest run on `docs2/main`.
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

- [ ] 🔁 **Nothing changes twice:** in GitHub, open the newest run on `docs2/main` → **Re-run all jobs**. The sync
      says *unchanged* for everything. (The **Run workflow** button only appears once the workflow is on the
      default branch, after go-live.)
- [ ] ✋ **Hand edits are protected:** change one word of *Part two* in Webflow's CMS, wait 10 minutes, edit *Part two*
      in Pages CMS and merge. The sync skips it and says *edited by hand in Webflow*.

---

## 📝 Notes for the test

| | |
|---|---|
| 🔁 | Saving in Pages CMS **straight on `docs2/main`** also publishes staging (no pull request). For reviewed work, use a branch as in step 1. |
| 🧹 | The sync never deletes. The earlier hand-made Doc Kit pages in Webflow stay; the summary lists them as *not in the repo*. |
| 🖼️ | Images are copied to Webflow's CDN on the first sync, so the website does not depend on GitHub to show them. |
| 🐛 | Anything odd: screenshot it, note the step number, and send it to me. |
