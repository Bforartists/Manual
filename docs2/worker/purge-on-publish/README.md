# 🧹 Clear the site cache after a live Webflow publish

Cloudflare keeps a copy of every page on **bforartists.co** (2 hours, docs 4 hours), so most visitors are
served by Cloudflare and not by Webflow. That keeps the site inside Webflow's bandwidth plan.

When you publish the site live in Webflow, Webflow calls this Worker. The Worker clears Cloudflare's copies,
so the new pages show within seconds instead of after 2–4 hours.

| | |
|---|---|
| Address | `https://bfa-purge-on-publish.trinumedia.workers.dev` |
| Called by | Webflow webhook **site_publish** on the Bforartists site |
| Does | "Purge Everything" on the bforartists.co zone, only when the publish included bforartists.co |
| Ignores | Staging-only publishes (bforartists.webflow.io), which the docs sync makes many times a day |
| Can do | Nothing but clear the cache: its token only has **Zone · Cache Purge · Purge** on bforartists.co |
| Limit | At most 3 clears a minute |

## Setup (done once)
- Repository secret `CF_PURGE_TOKEN` and variable `CF_ZONE_CO` (Settings → Secrets and variables → Actions).
- The Worker deploys with `.github/workflows/docs2-deploy-purge-on-publish.yml` (after a merge that changes
  this folder, or by hand), using the same `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` as the edit gateway.
- The Webflow webhook (trigger `site_publish`, URL above) is registered once through the Webflow API.

## If the new pages don't show after a publish
Clear by hand: Cloudflare → **bforartists.co** → Caching → Configuration → **Purge Everything**. Then check the
Worker's logs (Cloudflare → Workers & Pages → bfa-purge-on-publish → Logs).
