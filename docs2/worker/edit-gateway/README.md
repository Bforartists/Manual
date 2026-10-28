# ✏️ Edit gateway (Cloudflare Worker)

One click from **Edit this page** to Pages CMS on a fresh branch. Pages CMS shows its own GitHub sign-in, so contributors walk in and everyone else stops at the sign-in or the "no access" screen.

```
Edit this page → Worker → branch docs2/edit/<page>-<date> → Pages CMS → first save → auto pull request
```

## 🚀 One-time setup (maintainer): no command line needed

1. **GitHub token.** GitHub → Settings → Developer settings → Fine-grained tokens → new token.
   Repository access: **only `Bforartists/Manual`**. Permission: **Contents: read and write**. Nothing else.
2. **Three repository secrets.** Repo → Settings → Secrets and variables → Actions → New repository secret:
   - `EDIT_GATEWAY_GITHUB_TOKEN`: the token from step 1.
   - `CLOUDFLARE_API_TOKEN`: Cloudflare → My Profile → API Tokens → Create → template **Edit Cloudflare Workers**.
   - `CLOUDFLARE_ACCOUNT_ID`: Cloudflare dashboard → Workers & Pages → the Account ID on the right.
3. **Deploy.** Merge this folder, or open Actions → **Docs 2.0 deploy edit gateway** → Run workflow. The job log shows the Worker URL (`https://bforartists-docs-edit.<account>.workers.dev`).
4. **Try it.** Open `<worker-url>/edit?kind=docs&path=getting-started/index.md`. You should land in Pages CMS on a new `docs2/edit/...` branch.
5. **Switch the website on.** Put `<worker-url>/edit` into `EDIT_GATE` at the top of `docs2/webflow/docs-layer.js` (it is empty now, so the button still opens GitHub's editor), then release the docs layer as usual.
6. **Built-in protection (nothing to set up).** The Worker refuses clicks whose Referer is not the docs site, and allows 20 clicks per minute per visitor. Branch names are per page and day, so spam is bounded, and empty branches are cleaned up after 3 days.

Doing it by hand instead: in this folder run `npx wrangler deploy`, then `npx wrangler secret put GITHUB_TOKEN_EDIT`.

## 🧹 Housekeeping

Branches nobody saved to are deleted after 3 days by the *Docs 2.0 clean up edit branches* workflow. Branches with commits are never touched.

## 🔍 Good to know

- A branch is made per page and day. Clicking again the same day reuses it.
- The page must exist on `master`. Anything else shows a friendly message and the GitHub editor link.
- The Worker never sees passwords. Its token can only touch this repository's contents.
