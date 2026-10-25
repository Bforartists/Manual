/* Bforartists · instant search popup · @version 1.1.1
 *
 * Site-wide (registered Webflow script, footer). The search button in the site navigation
 * ([data-nav-search]) and Ctrl/⌘ K open a popup that searches the whole site as you type:
 *   - the website (site.json, written by tools/site_index.py): Features, Download, News, About …
 *     titles, descriptions, headings, and art titles on the gallery;
 *   - the manual (search.json, written by the docs sync): page titles, summaries and H1–H3 headings.
 * Both lists are published to GitHub Pages under /nav/. Enter on nothing selected, or the last row,
 * opens the full site search (/search?query=…). Published as /Manual/webflow/quicksearch-<version>.js.
 * 1.1.0: searches the website too, not only the manual ("Search Bforartists").
 */
(function () {
  var d = document, R = d.documentElement;
  if (R.dataset.bfaQs) return;
  R.dataset.bfaQs = '1';
  var URL_ = 'https://bforartists.github.io/Manual/nav/search.json', SURL = 'https://bforartists.github.io/Manual/nav/site.json', CDN = 'https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
  var I = { zoom: '68b9bbd23fb07538f848b579_viewzoom.svg', doc: '68b9b72e6ab175721a9bf7cb_documents.svg', sec: '68b9b786235cfe7a6063d3dc_hierarchy.svg', world: '68b9b4b69f8eb147bccde6cf_world.svg', x: '68b9b6f02b79e1972f80e83b_cancel.svg', news: '68b8d6fe76b8096ac09f74e5_file_text.svg', art: '68b8f543763e8aff56926602_image.svg' };
  var CSS = [
    '.bfa-qs{position:fixed;inset:0;z-index:9999;display:none;align-items:flex-start;justify-content:center;padding:12vh 1rem 1rem;background:#0009;backdrop-filter:blur(3px)}',
    '.bfa-qs.is-open{display:flex}',
    '.bfa-qs-box{width:min(40rem,100%);max-height:72vh;display:flex;flex-direction:column;overflow:hidden;border-radius:var(--_bfa---shape--bevel,.625rem);background:var(--_bfa---surface--card,#404040);box-shadow:0 2px 4px #0006,0 30px 60px -12px #000c;color:var(--_bfa---text--primary,#ececec);font-family:var(--_bfa---type--text,Inter,sans-serif)}',
    '.bfa-qs-field{display:flex;align-items:center;gap:.625rem;padding:.75rem 1rem;border-bottom:1px solid #ffffff14}',
    '.bfa-qs-field img{width:18px;height:18px}',
    '.bfa-qs-field input{flex:1;min-width:0;border:0;outline:0;background:none;color:inherit;font:500 1.0625rem/1.4 inherit}',
    '.bfa-qs-field kbd,.bfa-qs-foot kbd{padding:.1rem .4rem;border-radius:.25rem;background:#0004;color:#bbb;font:600 .6875rem Inter,sans-serif}',
    '.bfa-qs-field .bfa-qs-go{flex:none;margin:0;cursor:pointer;font-family:inherit}',
    '.bfa-qs-field .bfa-qs-go img{width:16px;height:16px}',
    /* touch screens: no keyboard hints (Esc, arrows, Ctrl K) */
    '@media (hover:none){.bfa-qs-field kbd,.bfa-qs-foot{display:none}}',
    '.bfa-qs-x{display:grid;place-items:center;width:1.75rem;height:1.75rem;border:0;border-radius:.25rem;background:none;cursor:pointer;opacity:.7}',
    '.bfa-qs-x:hover{opacity:1;background:#ffffff10}',
    '.bfa-qs-x img{width:14px;height:14px}',
    '.bfa-qs-list{overflow:auto;padding:.375rem}',
    '.bfa-qs-list p{margin:.5rem .625rem .25rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#9a9a9a}',
    '.bfa-qs-list a{display:grid;grid-template-columns:18px minmax(0,1fr);gap:.125rem .625rem;align-items:center;padding:.5rem .625rem;border-radius:.375rem;color:inherit;text-decoration:none}',
    '.bfa-qs-list a img{width:16px;height:16px;grid-row:1/span 2}',
    '.bfa-qs-list a b{font-weight:600;font-size:.9375rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
    '.bfa-qs-list a small{grid-column:2;color:#9a9a9a;font-size:.75rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
    '.bfa-qs-list a mark{background:none;color:#7cc4f4;font-weight:700}',
    '.bfa-qs-list a:hover,.bfa-qs-list a.is-sel{background:var(--_bfa---accent--selected,#4f7fc0);color:#fff}',
    '.bfa-qs-list a:hover small,.bfa-qs-list a.is-sel small,.bfa-qs-list a:hover mark,.bfa-qs-list a.is-sel mark{color:#fff}',
    '.bfa-qs-empty{padding:1.25rem 1rem;color:#9a9a9a;font-size:.875rem}',
    '.bfa-qs-foot{display:flex;gap:1rem;padding:.5rem 1rem;border-top:1px solid #ffffff14;color:#9a9a9a;font-size:.75rem}',
    'html.theme-light .bfa-qs-box{background:#fff;color:#222}html.theme-light .bfa-qs-list a small{color:#666}'
  ].join('\n');
  var IDX = null, SIDX = null, loading = null, box = null, inp = null, list = null, hits = [], sel = -1;

  function esc(s) { var e = d.createElement('i'); e.textContent = s == null ? '' : String(s); return e.innerHTML; }
  function load() {
    if (IDX || loading) return loading;
    var get = function (u) { return fetch(u).then(function (r) { return r.ok ? r.json() : []; }).catch(function () { return []; }); };
    loading = Promise.all([get(URL_), get(SURL)]).then(function (j) { IDX = j[0] || []; SIDX = j[1] || []; run(); });
    return loading;
  }
  function mark(t, words) {
    var out = esc(t);
    words.forEach(function (w) { if (w.length > 1) out = out.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); });
    return out;
  }
  function score(text, q, words) {
    var t = text.toLowerCase();
    if (t === q) return 100;
    if (t.indexOf(q) === 0) return 80;
    if (t.indexOf(q) > -1) return 60;
    return words.every(function (w) { return t.indexOf(w) > -1; }) ? 40 : 0;
  }
  function run() {
    if (!list) return;
    var v = inp.value.trim(), q = v.toLowerCase(), words = q.split(/\s+/).filter(Boolean);
    sel = -1;
    if (!q) { list.innerHTML = '<div class="bfa-qs-empty">Type to search Bforartists: pages, news, art, tools, menus, hotkeys…</div>'; hits = []; return; }
    if (!IDX) { list.innerHTML = '<div class="bfa-qs-empty">Loading…</div>'; load(); return; }
    var site = [], pages = [], heads = [];
    SIDX.forEach(function (p) {
      var s = score(p.t, q, words), sd = p.d ? score(p.d, q, words) * 0.4 : 0;
      if (s || sd) site.push({ p: p, s: Math.max(s, sd) + 10 });
      (p.h || []).forEach(function (h) { var sh = score(h[0], q, words); if (sh) site.push({ p: p, h: h, s: sh * 0.8 }); });
    });
    IDX.forEach(function (p) {
      var s = score(p.t, q, words), sd = p.d ? score(p.d, q, words) * 0.4 : 0;
      if (s || sd) pages.push({ p: p, s: Math.max(s, sd) + (p.k ? 5 : 0) });
      (p.h || []).forEach(function (h) { var sh = score(h[0], q, words); if (sh) heads.push({ p: p, h: h, s: sh }); });
    });
    site.sort(function (a, b) { return b.s - a.s || a.p.t.length - b.p.t.length; });
    pages.sort(function (a, b) { return b.s - a.s || a.p.t.length - b.p.t.length; });
    heads.sort(function (a, b) { return b.s - a.s || a.h[0].length - b.h[0].length; });
    var o = '', seenU = {};
    site = site.filter(function (x) { var k = x.p.u + '#' + (x.h ? x.h[0] : ''); if (seenU[k]) return false; seenU[k] = 1; return true; });
    if (site.length) o += '<p>Website</p>' + site.slice(0, 6).map(function (x) {
      var ic = x.h && x.h[1] === 'browse' && x.p.u === '/gallery' ? I.art : x.p.k === 'news' ? I.news : I.world;
      if (x.h) return '<a href="' + x.p.u + (x.h[1] ? '#' + x.h[1] : '') + '"><img alt="" src="' + CDN + ic + '"><b>' + mark(x.h[0], words) + '</b><small>' + esc(x.p.g) + ' › ' + esc(x.p.t) + '</small></a>';
      return '<a href="' + x.p.u + '"><img alt="" src="' + CDN + ic + '"><b>' + mark(x.p.t, words) + '</b><small>' + esc(x.p.g) + (x.p.d ? ' · ' + esc(x.p.d) : '') + '</small></a>';
    }).join('');
    if (pages.length) o += '<p>Manual</p>' + pages.slice(0, 7).map(function (x) {
      return '<a href="/docs/' + x.p.s + '"><img alt="" src="' + CDN + I.doc + '"><b>' + mark(x.p.t, words) + '</b><small>' + esc(x.p.g) + (x.p.d ? ' · ' + esc(x.p.d) : '') + '</small></a>';
    }).join('');
    if (heads.length) o += '<p>Inside the manual</p>' + heads.slice(0, 9).map(function (x) {
      return '<a href="/docs/' + x.p.s + '#' + x.h[1] + '"><img alt="" src="' + CDN + I.sec + '"><b>' + mark(x.h[0], words) + '</b><small>' + esc(x.p.g) + ' › ' + esc(x.p.t) + '</small></a>';
    }).join('');
    if (!site.length && !pages.length && !heads.length) o += '<div class="bfa-qs-empty">Nothing matches “' + esc(v) + '” yet. Try the full results page below.</div>';
    o += '<p>Everywhere</p><a href="/search?query=' + encodeURIComponent(v) + '"><img alt="" src="' + CDN + I.zoom + '"><b>All results for “' + esc(v) + '”</b><small>Full results page: pages, news, gallery and the manual</small></a>';
    list.innerHTML = o;
    hits = [].slice.call(list.querySelectorAll('a'));
  }
  function build() {
    var st = d.createElement('style'); st.id = 'bfa-qs-css'; st.textContent = CSS; d.head.appendChild(st);
    box = d.createElement('div'); box.className = 'bfa-qs'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', 'Search');
    box.innerHTML = '<div class="bfa-qs-box"><label class="bfa-qs-field"><img alt="" src="' + CDN + I.zoom + '"><input type="search" autocomplete="off" placeholder="Search Bforartists" aria-label="Search Bforartists"><button type="button" class="ui-btn is-accent is-small bfa-qs-go"><span class="ui-btn-icon"><img class="ui-icon" alt="" src="' + CDN + I.zoom + '"></span><span class="ui-btn-label">Discover</span></button><kbd>Esc</kbd><button type="button" class="bfa-qs-x" aria-label="Close"><img alt="" src="' + CDN + I.x + '"></button></label>' +
      '<div class="bfa-qs-list" role="listbox"></div><div class="bfa-qs-foot"><span><kbd>↑</kbd> <kbd>↓</kbd> choose</span><span><kbd>Enter</kbd> open</span><span><kbd>Ctrl</kbd> <kbd>K</kbd> search anywhere</span></div></div>';
    d.body.appendChild(box);
    inp = box.querySelector('input'); list = box.querySelector('.bfa-qs-list');
    inp.addEventListener('input', run);
    inp.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault(); if (!hits.length) return;
        sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + hits.length) % hits.length;
        hits.forEach(function (a, i) { a.classList.toggle('is-sel', i === sel); }); hits[sel].scrollIntoView({ block: 'nearest' });
      } else if (e.key === 'Enter') {
        e.preventDefault(); var a = hits[sel > -1 ? sel : 0];
        location.href = a ? a.getAttribute('href') : '/search?query=' + encodeURIComponent(inp.value.trim());
      }
    });
    /* Discover: the full results page, same as the button on the Docs home */
    box.querySelector('.bfa-qs-go').addEventListener('click', function (e) {
      e.preventDefault(); var v = inp.value.trim();
      if (!v) { inp.focus(); return; }
      location.href = '/search?query=' + encodeURIComponent(v);
    });
    box.addEventListener('click', function (e) { if (e.target === box || e.target.closest('.bfa-qs-x')) close(); else if (e.target.closest('.bfa-qs-list a')) close(); });
  }
  function open(q) {
    if (!box) build();
    box.classList.add('is-open'); R.style.overflow = 'hidden';
    if (q != null) inp.value = q;
    load(); run(); setTimeout(function () { inp.focus(); inp.select(); }, 20);
  }
  function close() { if (box) { box.classList.remove('is-open'); R.style.overflow = ''; } }
  d.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-nav-search],[data-qs-open]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault(); open();
  }, true);
  d.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) { e.preventDefault(); open(); }
    else if (e.key === 'Escape' && box && box.classList.contains('is-open')) close();
  });
  window.bfaQuickSearch = { open: open, close: close };
})();
