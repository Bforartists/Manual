# ✏️ Edit gateway (Cloudflare Worker)

One click from **Edit this page** to Pages CMS on a fresh branch. Pages CMS shows its own GitHub sign-in, so contributors walk in and everyone else stops at the sign-in or the "no access" screen.

```
Edit this page → Worker → branch docs2/edit/<page>-<date> → Pages CMS → first save → auto pull request
```

## 🚀 One-time setup (maintainer)

1. **Token.** GitHub → Settings → Developer settings → Fine-grained tokens → new token.
   Repository access: **only `Bforartists/Manual`**. Permission: **Contents: read and write**. Nothing else.
2. **Deploy.** In this folder: `npx wrangler deploy`, then `npx wrangler secret put GITHUB_TOKEN_EDIT` and paste the token.
3. **Try it.** Open `https://<worker-url>/edit?kind=docs&path=getting-started/index.md`. You should land in Pages CMS on a new `docs2/edit/...` branch.
4. **Switch the website on.** Put the Worker URL into `EDIT_GATE` at the top of `docs2/webflow/docs-layer.js` (it is empty now, so the button still opens GitHub's editor).
5. **Optional, recommended.** In Cloudflare → Security → WAF → Rate limiting: limit `/edit` to about 20 requests per minute per IP, because anyone can open the link and every new page-day makes one branch.

## 🧹 Housekeeping

Branches nobody saved to are deleted after 3 days by the *Docs 2.0 clean up edit branches* workflow. Branches with commits are never touched.

## 🔍 Good to know

- A branch is made per page and day. Clicking again the same day reuses it.
- The page must exist on `master`. Anything else shows a friendly message and the GitHub editor link.
- The Worker never sees passwords. Its token can only touch this repository's contents.
