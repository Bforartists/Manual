# ✏️ Editing the docs online

You can fix or write a docs page in your browser. Nothing to install, nothing to host. Every save becomes a Git commit, and every change is reviewed in a pull request before it goes live.

## Pick your tool

| | 🖋️ Pages CMS | 💻 github.dev | 🐙 GitHub editor |
|---|---|---|---|
| **Best for** | Writers, most edits | Many pages at once, developers | A typo, one line |
| **Looks like** | A form and a word-processor editor | VS Code in the browser | A plain text box |
| **WYSIWYG** | ✓ Text, headings, lists, links, images | ~ Side-by-side preview | ✗ Preview tab only |
| **Open it** | [app.pagescms.org](https://app.pagescms.org) | Press `.` on any repo page | The ✏️ pencil on any file |
| **Saves to** | A branch you choose | Your branch | A new branch + pull request |

On the docs website, every page will have **Edit this page**, which opens that exact file.

## 🖋️ Pages CMS (recommended)

### One-time setup (maintainer)

1. Install the **Pages CMS** GitHub App on the `Bforartists/Manual` repository: open [app.pagescms.org](https://app.pagescms.org), sign in with GitHub and follow the install prompt. Only this repository needs access.
2. The editor reads [`.pages.yml`](../../.pages.yml) in the repository root. It defines the page form, the image library and the commit messages.
3. Create a `docs-drafts` branch. Writers save there; a maintainer opens one pull request from `docs-drafts` to `main` when a batch is ready.

### Writing a page

1. Sign in at [app.pagescms.org](https://app.pagescms.org) with your GitHub account.
2. Choose **Bforartists/Manual** and the branch **docs-drafts**.
3. Open **Documentation pages**. Pages are shown as a tree, the same as the sidebar.
4. Edit the form at the top (title, status, version) and the page text below.
5. Insert images with the image button. They go into the image library under a place name, like `ui/timeline/header.png`.
6. Click **Save**. Pages CMS commits your change with your name.

### Doc kit tags

The editor shows normal text, headings, lists, tables, links and images as they will read. The doc kit blocks are short tags. Switch to **Source** (top right of the editor) to add or change them:

| You type | You get on the website |
|---|---|
| `:::tip` … `:::` | A tip callout (also `note`, `warn`, `imp`) |
| `:kbd[Ctrl+Space]` | Keycaps |
| `:menu[View > Area > Split]` | A menu path with icons |
| `![Header](/docs2/images/ui/timeline/header.png){.right}` | Image floated right; also `.thumb`, `.icon`, or none for full width |
| `::tool{id=modifier.bevel}` | A tool card filled from Bforartists (name, icon, tooltip, hotkey) |
| `::include{snippet=marker-menu}` | A shared section, written once in **Shared snippets** |
| `:::hotspots{img=…}` + a list | A screenshot with hover areas |

The full list is on [Doc kit tags](Doc-kit-tags.md).

:::warn
Spike 2 checks whether the rich-text editor keeps these tags exactly as typed. Until then, edit pages that have tags in **Source** mode.
:::

## 💻 github.dev

Press `.` on the repository page on GitHub. VS Code opens in your browser with the repository. Open a page and press `Ctrl+K V` for a live preview beside it. Commit from the Source Control tab to your own branch, then open a pull request.

## 🐙 GitHub web editor

Open a file on GitHub and click the ✏️ pencil. Edit, then **Propose changes**. GitHub makes a branch and a pull request for you. Good for a typo; for anything bigger use Pages CMS.

## 🔍 What happens after you save

1. A pull request shows your change. Checks run: front matter, links, images and tags.
2. The section reviewer gets asked to review it (from `CODEOWNERS`).
3. After merge, the build sends the changed pages to Webflow staging. Going live is a maintainer's click.
