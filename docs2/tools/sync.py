#!/usr/bin/env python3
"""Sync the docs from GitHub to Webflow staging (bforartists.webflow.io).

    python3 docs2/tools/sync.py [repo root] --plan plan.json            # no Webflow access: show what would be sent
    WEBFLOW_TOKEN=… python3 docs2/tools/sync.py . --apply --publish      # write the CMS items, publish staging

What it does
  📚 Doc Sections  one item per section (folder under content/); the section's index.md is its overview
  ♻️ Doc Snippets  one item per shared section in snippets/
  📄 Doc Pages     one item per page, with level and parent from the folders (chapter / sub-chapter)

Safety
  🔑 Items are matched on page-id / section-id / snippet-id, never on name.
  ⏭️ Unchanged pages are skipped (checksum).
  ✋ An item edited by hand in Webflow after the last sync is skipped and reported (use --force to overwrite).
  🧹 Nothing is ever deleted; items with no page in the repo are listed in the report.
  🌐 Publishing goes to the webflow.io staging address only. Custom domains are never published here.
"""
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docs_io import iter_pages, site_tree, slugify  # noqa: E402
import html_build  # noqa: E402
import landing  # noqa: E402

API = "https://api.webflow.com/v2"
HERE = os.path.dirname(os.path.abspath(__file__))
HAND_EDIT_SLACK = dt.timedelta(minutes=10)


# ---------------------------------------------------------------- Webflow API

TIMEOUT = 300               # seconds per Webflow call; a page with many new screenshots is slow
MAX_IMAGES_PER_CALL = 60    # new screenshots per batched update


class SyncError(Exception):
    pass


class Webflow:
    def __init__(self, token):
        self.token = token
        self.calls = 0

    def req(self, method, path, body=None, retry_timeouts=True):
        data = json.dumps(body).encode() if body is not None else None
        for attempt in range(6):
            r = urllib.request.Request(API + path, data=data, method=method, headers={
                "Authorization": f"Bearer {self.token}", "accept": "application/json",
                "content-type": "application/json"})
            try:
                self.calls += 1
                with urllib.request.urlopen(r, timeout=TIMEOUT) as resp:
                    txt = resp.read().decode()
                    return json.loads(txt) if txt else {}
            except urllib.error.HTTPError as e:
                if e.code == 429 and attempt < 5:
                    time.sleep(int(e.headers.get("Retry-After", "10")))
                    continue
                if e.code >= 500 and attempt < 3:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise SyncError(f"Webflow {method} {path} failed: {e.code} {e.read().decode()[:800]}")
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                if retry_timeouts and attempt < 3:
                    time.sleep(5 * (attempt + 1))
                    continue
                raise SyncError(f"Webflow {method} {path} failed: {e}")

    def items(self, cid):
        out, offset = [], 0
        while True:
            page = self.req("GET", f"/collections/{cid}/items?limit=100&offset={offset}")
            out += page.get("items", [])
            total = page.get("pagination", {}).get("total", 0)
            offset += 100
            if offset >= total:
                return out

    def options(self, cid, field_slug):
        col = self.req("GET", f"/collections/{cid}")
        for f in col.get("fields", []):
            if f["slug"] == field_slug:
                return {o["name"]: o["id"] for o in f.get("validations", {}).get("options", [])}
        return {}

    def create(self, cid, field_data):
        """Create one item. Webflow copies every screenshot of the page to its CDN while it answers,
        so a big page can take minutes. A timed-out create may still have worked: look it up by
        slug before trying again, so a page is never made twice."""
        body = {"isDraft": False, "isArchived": False, "fieldData": field_data}
        for attempt in range(3):
            try:
                return self.req("POST", f"/collections/{cid}/items", body, retry_timeouts=False)
            except SyncError as e:
                if "failed: 4" in str(e) or attempt == 2:
                    raise
                time.sleep(20)
                found = self.req("GET", f"/collections/{cid}/items?slug={urllib.parse.quote(field_data['slug'])}").get("items", [])
                if found:
                    return found[0]

    def update(self, cid, item_id, field_data):
        return self.update_many(cid, [(item_id, field_data)])

    def update_many(self, cid, pairs, max_items=25, max_bytes=1_000_000, max_images=MAX_IMAGES_PER_CALL):
        """PATCH items in batches (fewer calls, kinder to rate limits on a full sync). Batches are also
        capped by screenshot count: Webflow copies each new image while it answers."""
        batch, size, imgs = [], 0, 0
        for item_id, fd in pairs:
            raw = json.dumps(fd)
            n, k = len(raw), raw.count("raw.githubusercontent.com")
            if batch and (len(batch) >= max_items or size + n > max_bytes or imgs + k > max_images):
                self.req("PATCH", f"/collections/{cid}/items", {"items": batch})
                batch, size, imgs = [], 0, 0
            batch.append({"id": item_id, "isDraft": False, "fieldData": fd})
            size += n
            imgs += k
        if batch:
            self.req("PATCH", f"/collections/{cid}/items", {"items": batch})

    def publish_staging(self, site_id):
        return self.req("POST", f"/sites/{site_id}/publish", {"publishToWebflowSubdomain": True, "customDomains": []})


# ---------------------------------------------------------------- build the items from the repo

def git(repo, *args):
    try:
        return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def checksum(fields):
    return hashlib.sha256(json.dumps(fields, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:16]


def tidy(html):
    """Rich text has no use for the newlines between tags."""
    return re.sub(r">\s*\n\s*<", "><", html).strip()


def build(repo, cfg):
    sha = os.environ.get("DOCS_SHA") or git(repo, "rev-parse", "HEAD") or os.environ.get("GITHUB_SHA") or cfg.get("branch", "main")
    gh = cfg["repo"]
    pages = list(iter_pages(repo))
    by_rel = {p.rel: p for p in pages}
    skip = set(cfg.get("skip_sections", []))
    tree = [sec for sec in site_tree(repo, [p for p in pages if p.kind == "page"]) if sec.id not in skip]
    slug_of = {n.page.rel: n.web_slug for sec in tree for n in sec.nodes}
    md = html_build.md_engine()
    branch = cfg.get("branch", "main")
    # Stable links: an image URL names the last commit that changed that image, so it only
    # changes when the image changes. (With the current commit in every URL, any merge made
    # every page with images "changed", re-sent it and made Webflow re-import every screenshot.)
    last_commit = {}
    cur = None
    for line in git(repo, "log", "--format=@%H", "--name-only", sha, "--", "docs2/images").splitlines():
        if line.startswith("@"):
            cur = line[1:]
        elif line and cur:
            last_commit.setdefault(line, cur)

    def img_url(r):
        return f"https://raw.githubusercontent.com/{gh}/{last_commit.get(r, sha)}/{r}"

    urls = dict(
        img_url=img_url,
        page_url=lambda t: cfg["page_url"] + slug_of[t.rel] if t.rel in slug_of else None,
        file_url=lambda r: f"https://github.com/{gh}/blob/{branch}/{r}")

    def edited(p):
        return git(repo, "log", "-1", "--format=%cI", "--", p.rel) or None

    sections, snippets, docs = [], [], []
    for sec in tree:
        f = {"section-id": sec.id, "name": sec.title, "order": sec.order}
        if sec.index:
            body = tidy(html_build.page_html(repo, sec.index, by_rel, md, **urls))
            f["overview"] = body
            if sec.index.fm.get("summary"):
                f["summary"] = str(sec.index.fm["summary"])
        sections.append({"key": sec.id, "slug": slugify(sec.id), "fields": f, "create": {}})
    for p in pages:
        if p.kind != "snippet":
            continue
        sid = str(p.fm.get("id") or "snippet." + os.path.splitext(os.path.basename(p.rel))[0])
        f = {"snippet-id": sid, "name": str(p.fm.get("title") or sid),
             "body": tidy(html_build.page_html(repo, p, by_rel, md, **urls, snippet=True)), "source-path": p.rel}
        snippets.append({"key": sid, "slug": slugify(sid.split(".", 1)[-1]), "fields": f, "rel": p.rel, "create": {}})
    kids = landing.children_map(tree)
    url_of = lambda n: cfg["page_url"] + n.web_slug                  # noqa: E731
    sec_cfg = landing.sections_cfg()
    for sec in tree:                       # each section is a page too: /docs/<section id>, intro + cards
        idx = sec.index
        body = html_build.page_html(repo, idx, by_rel, md, **urls) if idx else ""
        body = tidy(landing.add_cards(body, idx, kids.get(sec.id, []), kids, url_of,
                                      sec_cfg.get(sec.id, {}).get("categories"), sec.id, heading=None))
        if not body:
            continue
        key = str(idx.fm.get("id")) if idx and idx.fm.get("id") else f"{sec.id}.index"
        f = {"page-id": key, "name": str(sec.title), "section-id": sec.id, "section-title": sec.title,
             "order": 0, "level": 0, "parent-page-id": "", "body": body,
             "version": str((idx.fm.get("version") if idx else "") or ""),
             "status": str((idx.fm.get("status") if idx else None) or "draft"),
             "reading-minutes": 1, "source-path": idx.rel if idx else ""}
        if idx and idx.fm.get("summary"):
            f["summary"] = str(idx.fm["summary"])
        docs.append({"key": key, "slug": slugify(sec.id), "fields": f,
                     "create": {"summary": html_build.first_paragraph(body)},
                     "section": sec.id, "shared": [str(s) for s in ((idx.fm.get("shared") if idx else None) or [])]})
    for sec in tree:
        for n in sec.nodes:
            p = n.page
            body = html_build.page_html(repo, p, by_rel, md, **urls)
            body = tidy(landing.add_cards(body, p, kids.get(n.id, []), kids, url_of))
            words = len(re.sub(r"<[^>]+>", " ", body).split())
            f = {"page-id": n.id, "name": str(p.fm.get("title") or n.id), "section-id": sec.id,
                 "section-title": sec.title, "order": n.order, "level": n.level,
                 "parent-page-id": n.parent_id or "",
                 "body": body, "version": str(p.fm.get("version") or ""), "status": str(p.fm.get("status") or "draft"),
                 "reading-minutes": max(1, round(words / 200)), "source-path": p.rel}
            if p.fm.get("summary"):
                f["summary"] = str(p.fm["summary"])                # a written summary always wins
            if p.fm.get("video"):
                f["video"] = str(p.fm["video"])
            last = edited(p)
            if last:
                f["last-edited"] = last
            docs.append({"key": n.id, "slug": n.web_slug, "fields": f,
                         "create": {"summary": html_build.first_paragraph(body)},   # only for new items
                         "section": sec.id, "shared": [str(s) for s in (p.fm.get("shared") or [])]})
    base, icons = landing.load_icons()
    nav = landing.nav_tree(tree, kids, icons, lambda sec: slugify(sec.id), lambda n: n.web_slug, sha[:7])
    nav["base"], nav["page_url"] = base, cfg["page_url"]
    return {"sha": sha, "sections": sections, "snippets": snippets, "pages": docs, "nav": nav}


# ---------------------------------------------------------------- apply

def parse_checksum(value):
    if not value or "|" not in str(value):
        return None, None
    h, t = str(value).split("|", 1)
    try:
        return h, dt.datetime.fromisoformat(t.replace("Z", "+00:00"))
    except ValueError:
        return h, None


def apply_collection(wf, cid, key_field, wanted, report, force, extra=lambda w: {}):
    existing = {it["fieldData"].get(key_field): it for it in wf.items(cid) if it["fieldData"].get(key_field)}
    ids, pending = {}, []
    for w in wanted:
        fields = dict(w["fields"], **extra(w))
        h = checksum(fields)
        now = dt.datetime.now(dt.timezone.utc)
        stamp = f"{h}|{now.isoformat(timespec='seconds')}"
        it = existing.get(w["key"])
        if it:
            ids[w["key"]] = it["id"]
            old_h, old_t = parse_checksum(it["fieldData"].get("checksum"))
            if old_h == h and not force:
                report.append(("⏭️", w["key"], "unchanged"))
                continue
            updated = it.get("lastUpdated")
            if old_t and updated and not force:
                last = dt.datetime.fromisoformat(updated.replace("Z", "+00:00"))
                if last - old_t > HAND_EDIT_SLACK:
                    report.append(("✋", w["key"], "edited by hand in Webflow after the last sync; skipped"))
                    continue
            data = dict(fields)
            if "checksum" in KNOWN.get(cid, {"checksum"}):
                data["checksum"] = stamp
            pending.append((it["id"], data))
            report.append(("🔄", w["key"], "updated"))
        else:
            data = dict(w.get("create", {}), **fields, slug=w["slug"])
            if "checksum" in KNOWN.get(cid, {"checksum"}):
                data["checksum"] = stamp
            res = wf.create(cid, data)
            ids[w["key"]] = res.get("id")
            report.append(("🆕", w["key"], "created"))
    if pending:
        wf.update_many(cid, pending)
    for k in existing:
        if k not in {w["key"] for w in wanted}:
            report.append(("🧹", k, "in Webflow but not in the repo; left alone"))
    return ids


KNOWN = {}      # collection id -> field slugs it has (sections have no checksum field)


def main(argv):
    opts = {a for a in argv if a.startswith("--")}
    args, it = [], iter(argv)
    plan_out = report_out = nav_out = None
    for a in it:
        if a == "--plan":
            plan_out = next(it)
        elif a == "--report":
            report_out = next(it)
        elif a == "--nav":
            nav_out = next(it)
        elif not a.startswith("--"):
            args.append(a)
    repo = args[0] if args else "."
    cfg = json.load(open(os.path.join(HERE, "webflow.json"), encoding="utf-8"))
    plan = build(repo, cfg)
    if plan_out:
        json.dump(plan, open(plan_out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    if nav_out:                            # the sidebar for the docs script (published to GitHub Pages)
        os.makedirs(os.path.dirname(os.path.abspath(nav_out)), exist_ok=True)
        json.dump(plan["nav"], open(nav_out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    lines = [f"### 🌐 Webflow sync{'' if '--apply' in opts else ' (plan only)'}", "",
             f"{len(plan['sections'])} section(s) · {len(plan['pages'])} page(s) · {len(plan['snippets'])} shared section(s) "
             f"from commit `{plan['sha'][:7]}`", ""]
    if "--apply" in opts:
        token = os.environ.get("WEBFLOW_TOKEN")
        if not token:
            print("::warning::WEBFLOW_TOKEN is not set; nothing was sent to Webflow.")
            lines.append("⚠️ No Webflow token set, so nothing was sent. See *Website sync* in the wiki.")
        else:
          try:
            wf = Webflow(token)
            col = cfg["collections"]
            for name, cid in col.items():
                KNOWN[cid] = {f["slug"] for f in wf.req("GET", f"/collections/{cid}").get("fields", [])}
            status_ids = wf.options(col["pages"], "status")
            report = []
            sec_ids = apply_collection(wf, col["sections"], "section-id", plan["sections"], report, "--force" in opts)
            snip_ids = apply_collection(wf, col["snippets"], "snippet-id", plan["snippets"], report, "--force" in opts)
            snip_by_path = {s["rel"]: snip_ids.get(s["key"]) for s in plan["snippets"]}

            def page_extra(w):
                return {"section": sec_ids.get(w["section"]),
                        "snippets": [snip_by_path[s] for s in w["shared"] if snip_by_path.get(s)],
                        "status": status_ids.get(w["fields"]["status"], w["fields"]["status"])}
            apply_collection(wf, col["pages"], "page-id", plan["pages"], report, "--force" in opts, page_extra)
            changed = sum(1 for r in report if r[0] in ("🔄", "🆕"))
            lines += [f"{changed} item(s) created or updated · {wf.calls} API calls", "",
                      "| | Item | Result |", "|---|---|---|"]
            lines += [f"| {i} | `{k}` | {why} |" for i, k, why in report if i != "⏭️"]
            skipped = sum(1 for r in report if r[0] == "⏭️")
            if skipped:
                lines.append(f"| ⏭️ | {skipped} item(s) | unchanged |")
            if changed and "--publish" in opts:
                wf.publish_staging(cfg["site_id"])
                lines += ["", f"🚀 Published to staging: {cfg['staging_url']}"]
          except SyncError as e:
              msg = str(e).replace("\n", " ")
              print(f"::error title=Webflow sync::{msg}")
              lines += ["", f"❌ **Sync stopped:** {msg}"]
              out = "\n".join(lines) + "\n"
              if report_out:
                  open(report_out, "w", encoding="utf-8").write(out)
              print(out)
              return 1
    out = "\n".join(lines) + "\n"
    if report_out:
        open(report_out, "w", encoding="utf-8").write(out)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
