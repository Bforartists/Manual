// Bforartists website · clear Cloudflare's copy of the site after a live Webflow publish.
//
// Webflow calls this Worker (webhook "site_publish") after every publish. Cloudflare keeps copies of the
// pages on bforartists.co for 2 hours (docs 4 hours) so that Webflow serves less bandwidth. After a live
// publish this Worker clears those copies, so the new pages show within seconds.
//
// - Publishes to the webflow.io staging address only (the docs sync does many) are ignored.
// - It can only clear the cache: the token it holds has no other permission.
// - At most 3 clears a minute, so a fake call can't empty the cache over and over.

const LIVE = /(^|\.)bforartists\.co$/;

function hosts(payload) {
  const list = (payload && (payload.domains || payload.customDomains)) || [];
  return list.map((d) => String((d && (d.url || d.name || d.domain)) || d)
    .replace(/^https?:\/\//, "").replace(/\/.*$/, "").toLowerCase());
}

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("Bforartists: clears the site cache after a live Webflow publish. POST only.", { status: 405 });
    }
    let body = {};
    try { body = await request.json(); } catch (e) { /* empty or not JSON */ }
    const domains = hosts(body.payload || body);
    if (!domains.some((d) => LIVE.test(d))) {
      return Response.json({ cleared: false, reason: "not a live publish", domains });
    }
    if (env.LIMIT) {
      const { success } = await env.LIMIT.limit({ key: "purge" });
      if (!success) return Response.json({ cleared: false, reason: "cleared a moment ago" }, { status: 429 });
    }
    const r = await fetch(`https://api.cloudflare.com/client/v4/zones/${env.CF_ZONE_CO}/purge_cache`, {
      method: "POST",
      headers: { Authorization: `Bearer ${env.CF_PURGE_TOKEN}`, "Content-Type": "application/json" },
      body: JSON.stringify({ purge_everything: true }),
    });
    const j = await r.json().catch(() => ({}));
    console.log(`purge after live publish (${domains.join(", ")}): ${j.success ? "ok" : "failed " + JSON.stringify(j.errors || r.status)}`);
    return Response.json({ cleared: !!j.success, domains }, { status: j.success ? 200 : 502 });
  },
};
