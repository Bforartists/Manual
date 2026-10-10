# ✏️ Editing the docs online

> **Fix or write a docs page in your browser. Nothing to install, nothing to host.**

Every save is a Git commit with your name, and changes are reviewed before they reach the website.

[![Edit the docs in Pages CMS](https://img.shields.io/badge/Edit_the_docs-Pages_CMS-2ea44f?style=for-the-badge&logo=markdown&logoColor=white)](https://app.pagescms.org/Bforartists/Manual/docs2%2Ftier1-getting-started/collection/docs)

---

## 🧭 Pick your tool

| | 🖋️ Pages CMS | 🐙 GitHub web editor | 💻 github.dev / your own editor |
|---|---|---|---|
| **Best for** | Writers, most edits | A typo, one line | Many pages at once, developers |
| **Looks like** | A form and a word-processor editor | A plain text box | VS Code, in the browser or on your PC |
| **Installs** | None | None | None (github.dev) · Git + editor (local) |
| **WYSIWYG** | ✅ Text, headings, lists, tables, images | ❌ Preview tab | 🟡 Preview beside the text |
| **Drag and drop images** | ✅ Into the page; the image bot files them | 🟡 Uploads go to GitHub, not the library | 🟡 Copy the file into `docs2/images/` |
| **Insert a tip, image, table** | ✅ `/` menu | ❌ Type it | ❌ Type it |
| **Review** | Saves to the docs branch; a maintainer opens the pull request | ✅ Opens a pull request for you | ✅ Your own pull request |
| **Open it** | [Edit the docs](https://app.pagescms.org/Bforartists/Manual/docs2%2Ftier1-getting-started/collection/docs) | ✏️ pencil on any file | Press `.` on the repo page |
| **Verdict** | ⭐ **The advertised way** | Typos | Bulk and developer work |

On the website, every page will have **Edit this page**, which opens that exact page in Pages CMS.

---

## 🖋️ Pages CMS (recommended)

### 🔑 One-time setup (maintainer)

1. Push the docs branch to GitHub.
2. Open [app.pagescms.org](https://app.pagescms.org), sign in with GitHub, and install the **Pages CMS** GitHub App on `Bforartists/Manual` only.
3. Pages CMS reads `.pages.yml` in the repository root: the page tree, the form, the image library and the commit messages.

### ✍️ Writing a page

1. Click **Edit the docs** above and sign in with your GitHub account.
2. Open **📘 Documentation pages**. Pages are shown as a tree, like the sidebar.
3. Change the form at the top (title, status, video, shared sections) and the text below.
4. Press `/` on an empty line for the menu: headings, lists, **Image**, **Table**, **Quote**.
5. Drag a screenshot into the page. It lands in the image library and the image bot files it.
6. Click **Save** (top right). Pages CMS commits your change with your name.
7. Check your change: on GitHub, the newest commit on the branch is *docs: update … (Pages CMS, your name)*. Only your lines should be green.

### 💡 Plain writing: no codes to learn

| To get | Do this |
|---|---|
| 💡 A tip or note | `/` → **Quote**, then start with **Tip:** (or Note:, Warning:, Important:) |
| ⌨️ Keycaps | Type `Ctrl + S` |
| 🧭 A menu path | Type `Edit › Preferences` (copy the `›`) |
| 🖼️ A screenshot | Drag it in, or `/` → **Image** |
| 🎬 A video | Paste a YouTube link on its own line, or use the **Chapter video** field |
| ♻️ A shared section | Pick it in **Shared sections on this page**; edit its text in **♻️ Shared snippets** |

More: [Plain writing](Plain-writing.md).

### ⚠️ Good to know

| | What happens | What to do |
|---|---|---|
| 🧹 | The editor writes pages in its own tidy style | Nothing. The converter writes the same style, so your save only changes your lines |
| `>` | A plain `>` is saved as `&gt;` | Use `›` for menu paths |
| 🖼️ | Alt text of a dropped image is its file name | Change it to what the image shows, or let the bot suggest one |

---

## 🐙 GitHub web editor

Open a page on GitHub and click the ✏️ pencil. Edit, then **Commit changes → Propose changes**. GitHub makes a branch and a pull request for you. Good for a typo.

## 💻 github.dev or your own editor

Press `.` on the repository page: VS Code opens in your browser. Open a page, press `Ctrl+K V` for a preview, commit from Source Control to your own branch, then open a pull request. Locally the same works with Git and any editor.

---

## 🔍 After you save

1. A pull request shows the change. Checks run: front matter, links, images, no lost words.
2. 👀 A bot comment links to a preview of the page with the website's styles.
3. The section reviewer approves. After merge, the page syncs to the website's staging site. Going live is a maintainer's click.

See [Branches and review](Branches-and-Review.md) and [Checks and previews](Checks-and-Previews.md).
