// ✏️ Edit gateway: one click from "Edit this page" to Pages CMS on a fresh branch.
//
//   GET /edit?kind=docs&path=editors/video-sequence-editor/header/index.md
//
// 1. checks that the page exists on master,
// 2. creates the branch docs2/edit/<page>-<yyyymmdd> from the latest master (reuses it the same day),
// 3. redirects to Pages CMS on that branch (its edit links use the full repository path). The first save pushes a commit, and the
//    "Docs 2.0 auto pull request" workflow opens the pull request.
//
// Pages CMS asks for the GitHub sign-in itself, so this Worker never sees a password.
// It only holds one token (secret GITHUB_TOKEN_EDIT) that can create branches in the docs repo.

const REPO = "Bforartists/Manual";
const BASE = "master";
const ROOTS = { docs: "docs2/content", snippets: "docs2/snippets" };
// Pages where the "Edit this page" button lives. A click from anywhere else is refused.
// (No Referer at all is allowed: some browsers hide it, and people paste the link by hand.)
const ALLOWED_HOSTS = ["bforartists.com", "www.bforartists.com", "bforartists.webflow.io", "bforartists.github.io"];
const CMS = "https://app.pagescms.org/" + REPO.toLowerCase(); // Pages CMS writes owner/repo in lowercase

const page = (title, body, status = 200) =>
  new Response(
    `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${title}</title>` +
      `<body style="font:16px/1.5 system-ui,sans-serif;max-width:34rem;margin:4rem auto;padding:0 1rem"><h1>${title}</h1>${body}</body>`,
    { status, headers: { "content-type": "text/html; charset=utf-8" } }
  );

const gh = (env, path, init = {}) =>
  fetch("https://api.github.com/repos/" + REPO + path, {
    ...init,
    headers: {
      authorization: "Bearer " + env.GITHUB_TOKEN_EDIT,
      accept: "application/vnd.github+json",
      "user-agent": "bforartists-edit-gateway",
      "content-type": "application/json",
    },
  });

function slugOf(path) {
  const parts = path.replace(/\.md$/, "").split("/").filter((p) => p && p !== "index");
  return (
    parts.slice(-2).join("-").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "page"
  );
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname !== "/edit") return page("Bforartists docs edit gateway", "<p>Use the “Edit this page” button on a docs page.</p>", 404);

    // 1. only the docs site may use the gateway
    const referer = request.headers.get("referer");
    if (referer) {
      let host = "";
      try { host = new URL(referer).hostname; } catch (e) {}
      if (!ALLOWED_HOSTS.includes(host))
        return page("Please use the Edit this page button", "<p>This link only works from the Bforartists docs pages.</p>", 403);
    }

    // 2. a small limit per visitor (the RATE_LIMITER binding in wrangler.toml)
    if (env.RATE_LIMITER) {
      const ip = request.headers.get("cf-connecting-ip") || "unknown";
      const { success } = await env.RATE_LIMITER.limit({ key: ip });
      if (!success) return page("Too many edits at once", "<p>Please wait a minute and try again.</p>", 429);
    }

    const kind = url.searchParams.get("kind") || "docs";
    const path = url.searchParams.get("path") || "";
    const github = `https://github.com/${REPO}/edit/${BASE}/${ROOTS[kind] || ROOTS.docs}/${path}`;
    const fallback = `<p>You can still <a href="${github}">edit the page on GitHub</a>.</p>`;

    if (!ROOTS[kind] || !/^[A-Za-z0-9_\-./ ]+\.md$/.test(path) || path.includes("..") || path.startsWith("/"))
      return page("That link does not look right", fallback, 400);

    try {
      // 1. the page must exist on master
      const exists = await gh(env, `/contents/${ROOTS[kind]}/${path.split("/").map(encodeURIComponent).join("/")}?ref=${BASE}`);
      if (exists.status === 404) return page("Page not found", "<p>This page is not on the main branch (yet).</p>" + fallback, 404);
      if (!exists.ok) throw new Error("contents " + exists.status);

      // 2. a branch for this page and day, from the latest master
      const date = new Date().toISOString().slice(0, 10).replace(/-/g, "");
      const branch = `docs2/edit/${slugOf(path)}-${date}`;
      const head = await gh(env, `/git/ref/heads/${BASE}`);
      if (!head.ok) throw new Error("master ref " + head.status);
      const sha = (await head.json()).object.sha;
      const made = await gh(env, "/git/refs", { method: "POST", body: JSON.stringify({ ref: "refs/heads/" + branch, sha }) });
      if (!made.ok && made.status !== 422) throw new Error("create branch " + made.status); // 422: already there, reuse it

      // 3. open Pages CMS on it
      return Response.redirect(`${CMS}/${encodeURIComponent(branch)}/collection/${kind}/edit/${encodeURIComponent(ROOTS[kind] + "/" + path)}`, 302);
    } catch (e) {
      return page("The editor could not be prepared", "<p>Please try again in a moment.</p>" + fallback, 502);
    }
  },
};
