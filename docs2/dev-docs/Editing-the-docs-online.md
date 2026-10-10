# ✏️ Editing the docs online

Fix or write a docs page in your browser. Nothing to install, nothing to host. Every save is a Git commit, and changes are reviewed before they reach the website.

## 🧭 Pick your tool

| | 🖋️ Pages CMS | 🐙 GitHub web editor | 💻 github.dev / your own editor |
|---|---|---|---|
| **Best for** | Writers, most edits | A typo, one line | Many pages at once, developers |
| **Looks like** | A form and a word-processor editor | A plain text box | VS Code, in the browser or on your PC |
| **Installs** | None | None | None (github.dev) · Git + editor (local) |
| **WYSIWYG** | ✅ Text, headings, lists, tables, images | ❌ Preview tab | 🟡 Preview beside the text |
| **Drag and drop images** | ✅ Into the page, saved to the image library | 🟡 Uploads go to GitHub, not the library | 🟡 Copy the file into `docs2/images/_inbox/` |
| **Insert a tip, image, table** | ✅ `/` menu | ❌ Type it | ❌ Type it |
| **Review** | Saves to a branch; a maintainer opens the pull request | ✅ Opens a pull request for you | ✅ Your own pull request |
| **Open it** | [app.pagescms.org](https://app.pagescms.org) | ✏️ pencil on any file | Press `.` on the repo page |

On the website, every page will have **Edit this page**, which opens that exact page in Pages CMS.

## 🖋️ Pages CMS (recommended)

### One-time setup (maintainer)

1. Push the docs branch to GitHub.
2. Open [app.pagescms.org](https://app.pagescms.org), sign in with GitHub, and install the **Pages CMS** GitHub App on `Bforartists/Manual` only.
3. Pages CMS reads [`.pages.yml`](../../.pages.yml) in the repository root: the page tree, the form, the image library and the commit messages.

### Writing a page

1. Sign in at [app.pagescms.org](https://app.pagescms.org) with your GitHub account.
2. Choose **Bforartists/Manual** and the docs branch.
3. Open **📘 Documentation pages**. Pages are shown as a tree, like the sidebar.
4. Change the form at the top (title, status, video, shared sections) and the text below.
5. Press `/` on an empty line for the menu: headings, lists, **Image**, **Table**, **Quote**.
6. Drag a screenshot into the page. It is saved to the image library and filed by the image bot.
7. Click **Save**. Pages CMS commits your change with your name.

### ✍️ Plain writing: no codes to learn

| To get | Do this |
|---|---|
| 💡 A tip or note | `/` → **Quote**, then start with **Tip:** (or Note:, Warning:, Important:) |
| ⌨️ Keycaps | Type `Ctrl + S` |
| 🧭 A menu path | Type `Edit › Preferences` |
| 🖼️ A screenshot | Drag it in, or `/` → **Image** |
| 🎬 A video | Paste a YouTube link on its own line, or use the **Chapter video** field |
| ♻️ A shared section | Pick it in **Shared sections on this page**; edit its text in **♻️ Shared snippets** |

More: [Plain writing](Plain-writing.md).

## 🐙 GitHub web editor

Open a page on GitHub and click the ✏️ pencil. Edit, then **Commit changes → Propose changes**. GitHub makes a branch and a pull request for you. Good for a typo.

## 💻 github.dev or your own editor

Press `.` on the repository page: VS Code opens in your browser. Open a page, press `Ctrl+K V` for a preview, commit from Source Control to your own branch, then open a pull request. Locally the same works with Git and any editor.

## 🔍 After you save

1. A pull request shows the change. Checks run: front matter, links, images, no lost words.
2. 👀 A bot comment links to a preview of the page with the website's styles.
3. The section reviewer approves. After merge, the page syncs to the website's staging site. Going live is a maintainer's click.
