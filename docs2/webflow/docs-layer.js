/* Bforartists Docs 2.0 · docs layer (Queue 3)
 *
 * Runs on the Doc Pages template next to the inline docs script (bfa-docs-v6, page footer code).
 * Served from this repository through jsDelivr, pinned to a commit, and applied to the template
 * page as a registered Webflow script. Change it here, then register the new version.
 *
 *   1 🎛️  sidebar: the same ▶/▼ triangle on every level, the page scrollbar, icons everywhere (CSS)
 *   2 🧭  breadcrumb: Documentation → Docs home, then every level down to the page
 *   3 🗂️  group overview pages (/docs/<group>): hero, "Start here", chapter cards, help panels
 *   4 🏠  Docs home (/docs/home): search, Quick Start paths, sections at a glance, help cards
 */
(function () {
  var d = document, R = d.documentElement;
  if (R.dataset.dkLayer) return;
  R.dataset.dkLayer = '1';
  var CDN = 'https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
  var NAVURL = 'https://bforartists.github.io/Manual/nav/nav.json', NK = 'bfa-docs-nav';
  var HOME = '/docs/home', DISCORD = 'https://discord.gg/yKuR77v', PRO = 'https://www.trinumedia.com';
  var ISSUE = 'https://github.com/Bforartists/Manual/issues/new';
  var IC = {
    doc: '68b9b72e6ab175721a9bf7cb_documents.svg', file: '68b8d6fe76b8096ac09f74e5_file_text.svg',
    comm: '68b9b70677b5a3b5b8606647_community.svg', light: '68b9b7c5219bda8870e7cee9_light.svg',
    time: '68b9bb9cc5062fa217606ff2_time.svg', world: '68b9b4b69f8eb147bccde6cf_world.svg',
    zoom: '68b9bbd23fb07538f848b579_viewzoom.svg', caret: '68b9bbb397785a50ab1c6b64_tria_down.svg'
  };

  /* ---------------------------------------------------------------- 1 styles */
  var CSS = [
    /* the same triangle as the group headers: ▶ closed, green ▼ open */
    '.ui-doc-tw{width:1.25rem;height:1.25rem;opacity:1}',
    '.ui-doc-tw img{width:16px!important;height:16px!important;object-position:-999px 0;background:var(--ic-tri) center/contain no-repeat;transform:none!important;transition:none}',
    '.ui-doc-tw.is-open img{background-image:var(--ic-tri-down)}',
    '.ui-doc-tw:hover,.ui-doc-tw:focus-visible{background:var(--dk-hair)}',
    '.ui-doc-tree .ui-doc-row>.ui-panel-link:only-child{margin-left:1.375rem}',
    /* every chapter shows an icon; a page without its own shows the placeholder */
    '.ui-doc-tree .ui-panel-link .ui-icon{flex:0 0 16px;width:16px;height:16px;object-fit:contain}',
    /* sidebars use the page scrollbar (Chrome ignores the ::-webkit-scrollbar look once scrollbar-width is set) */
    '.ui-doc-side,.ui-doc-outline{scrollbar-width:auto!important}',
    '@supports not selector(::-webkit-scrollbar){.ui-doc-side,.ui-doc-outline{scrollbar-width:thin!important;scrollbar-color:#858585 #303030}}',
    '.ui-doc-side::-webkit-scrollbar,.ui-doc-outline::-webkit-scrollbar{width:8px}',
    '.ui-doc-side::-webkit-scrollbar-track,.ui-doc-outline::-webkit-scrollbar-track{background:#303030;border-radius:4px}',
    '.ui-doc-side::-webkit-scrollbar-thumb,.ui-doc-outline::-webkit-scrollbar-thumb{background:#858585;border-radius:4px}',
    '.ui-doc-side::-webkit-scrollbar-thumb:hover,.ui-doc-outline::-webkit-scrollbar-thumb:hover{background:#75bfff}',
    '.ui-doc-side::-webkit-scrollbar-thumb:active,.ui-doc-outline::-webkit-scrollbar-thumb:active{background:#fff}',
    /* breadcrumb */
    '.ui-doc-crumb img.is-color{filter:none}',
    '.ui-doc-crumb .dk-crumb-x{display:inline-flex;align-items:center;gap:.5rem}',
    /* shared bits */
    '.dk-eyebrow{font:700 .75rem/1.2 Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#5cb4f0;margin:0 0 .75rem}',
    '.dk-btn{display:inline-flex;align-items:center;gap:.5rem;min-height:2.5rem;padding:.45rem 1rem;border:2px solid var(--_bfa---edge--outline);border-radius:var(--_bfa---shape--bevel-tight,.2875rem);background:var(--_bfa---surface--raised);color:var(--_bfa---text--primary);font:600 .9375rem/1.2 Inter,sans-serif;text-decoration:none;transition:transform .2s ease,box-shadow .2s ease,background-color .2s ease;cursor:pointer}',
    '.dk-btn img{width:16px;height:16px;object-fit:contain}',
    '.dk-btn:hover{background:var(--_bfa---surface--hover,#555);box-shadow:0 2px 3px #0006,4px 10px 14px -6px #0009;transform:translateY(-2px)}',
    '.dk-home-page a,.dk-chapters a,.dk-hero a,.dk-help a{color:var(--dk-text)!important;text-decoration:none!important}',
    '.dk-btn.is-primary{background:#5aa9f0;border-color:#0006;color:#0b1a2a!important}',
    '.dk-btn.is-primary:hover{background:#75bfff}',
    '.dk-btn.is-small{min-height:2rem;padding:.25rem .75rem;font-size:.8125rem}',
    '.dk-card{border-radius:var(--_bfa---shape--bevel,.625rem);background-color:var(--_bfa---surface--card);box-shadow:0 1px 2px #0006,calc(var(--sx,0)*8px) 10px 16px -10px var(--dk-drop)}',
    '.dk-sticker{display:grid;place-items:center;border-radius:1.25rem;background:radial-gradient(circle at 35% 30%,#ffffff1f,#ffffff05 60%),var(--_bfa---surface--panel);box-shadow:inset 0 0 0 2px #ffffff14,0 2px 4px #0006,6px 14px 24px -12px var(--dk-drop)}',
    '.dk-sticker img{width:58%;height:58%;object-fit:contain;filter:drop-shadow(0 3px 4px #0008)}',
    'html.theme-light .dk-sticker{background:radial-gradient(circle at 35% 30%,#fff,#eee 70%);box-shadow:inset 0 0 0 2px #0000000d,0 2px 4px #0002,6px 14px 24px -12px #0003}',

    /* 3 group overview */
    'html.dk-overview .ui-doc-head{display:none}',
    '.dk-hero{display:grid;grid-template-columns:9rem minmax(0,1fr);gap:2rem;align-items:center;margin:0 0 2.5rem}',
    '.dk-hero .dk-sticker{width:9rem;height:9rem}',
    '.dk-hero h1{margin:0 0 .5rem}',
    '.dk-hero .type-lead{margin:0 0 1.25rem}',
    '.dk-hero-go{display:flex;flex-wrap:wrap;align-items:center;gap:.75rem 1rem;color:var(--dk-muted);font-size:.875rem}',
    '.dk-chapters{position:relative;margin:0 0 2rem;padding:1.25rem;border-radius:var(--_bfa---shape--bevel,.625rem);background-color:var(--_bfa---surface--panel);box-shadow:0 1px 2px #0005,calc(var(--sx,0)*12px) 16px 26px -16px var(--dk-drop)}',
    '.dk-chapters-bar{display:flex;align-items:center;justify-content:space-between;gap:1rem;margin:0 0 1rem}',
    '.dk-chapters-bar .type-label{font:700 .75rem Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--dk-muted)}',
    '.dk-seg{display:inline-flex;gap:2px;padding:2px;border-radius:.375rem;background:#0003}',
    '.dk-seg button{border:0;border-radius:.25rem;padding:.3rem .7rem;background:none;color:var(--dk-muted);font:600 .8125rem Inter,sans-serif;cursor:pointer}',
    '.dk-seg button.is-on{background:var(--_bfa---surface--raised);color:var(--dk-text)}',
    '.dk-cat{margin:1.5rem 0 .75rem;font:700 1rem Inter,sans-serif;color:var(--dk-text)}',
    '.dk-cat:first-of-type{margin-top:0}',
    '.dk-cat::before,.dk-cat::after{display:none!important;content:none!important}',
    'html.dk-overview .ui-doc-body>.ui-doc-subsec{padding:0;background:none;box-shadow:none}',
    'html.dk-overview .ui-doc-body>.ui-doc-subsec>p{margin:0 0 1.25rem}',
    'html.dk-overview .ui-doc-now{display:none!important}',
    '.dk-cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:1rem}',
    '.dk-ccard{display:grid;grid-template-columns:4.5rem minmax(0,1fr);gap:1rem;align-items:start;padding:1rem;color:var(--dk-text);text-decoration:none;transition:transform .2s ease,box-shadow .2s ease}',
    '.dk-ccard:hover{transform:translateY(-2px);box-shadow:0 2px 3px #0006,calc(var(--sx,0)*12px) 16px 22px -12px var(--dk-drop)}',
    '.dk-ccard .dk-sticker{width:4.5rem;height:4.5rem;border-radius:.875rem}',
    '.dk-ccard small{display:block;margin:0 0 .25rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--dk-muted)}',
    '.dk-ccard b{display:flex;align-items:center;gap:.5rem;font-family:"Titillium Web",Titillium,sans-serif;font-size:1.3rem;line-height:1.15;font-weight:700}',
    '.dk-ccard b img{flex:0 0 18px;width:18px;height:18px;object-fit:contain}',
    '.dk-ccard p{margin:.375rem 0 .75rem;font-size:.875rem;line-height:1.45;color:var(--dk-text);opacity:.8}',
    '.dk-ccard .dk-btn{pointer-events:none}',
    '.dk-ccard em{margin-left:.75rem;font-style:normal;font-size:.75rem;color:var(--dk-muted)}',
    '.dk-ccard.is-start{grid-column:1/-1;grid-template-columns:6rem minmax(0,1fr);border:1px solid #5aa9f0;box-shadow:0 0 0 1px #5aa9f033,0 1px 2px #0006,calc(var(--sx,0)*8px) 10px 16px -10px var(--dk-drop)}',
    '.dk-ccard.is-start .dk-sticker{width:6rem;height:6rem}',
    '.dk-ccard.is-start small{color:#5cb4f0}',
    '.dk-chapters.is-list .dk-cgrid{grid-template-columns:1fr;gap:.5rem}',
    '.dk-chapters.is-list .dk-ccard{grid-template-columns:2.5rem minmax(0,1fr);padding:.625rem .875rem;align-items:center}',
    '.dk-chapters.is-list .dk-ccard .dk-sticker{width:2.5rem;height:2.5rem;border-radius:.5rem}',
    '.dk-chapters.is-list .dk-ccard p,.dk-chapters.is-list .dk-ccard .dk-btn,.dk-chapters.is-list .dk-ccard small{display:none}',
    '.dk-chapters.is-list .dk-ccard b{font-size:1.05rem}',
    '.dk-chapters.is-list .dk-ccard b img{display:none}',
    '@media(max-width:767px){.dk-hero{grid-template-columns:1fr;gap:1rem}.dk-hero .dk-sticker{width:6rem;height:6rem}.dk-cgrid{grid-template-columns:1fr}.dk-ccard,.dk-ccard.is-start{grid-template-columns:3.5rem minmax(0,1fr)}.dk-ccard .dk-sticker,.dk-ccard.is-start .dk-sticker{width:3.5rem;height:3.5rem}}',
    /* help panels on the right */
    '.dk-help{margin:0 0 1rem}',
    '.dk-help .ui-panel-body{display:flex;flex-direction:column;gap:2px;padding:.375rem}',
    '.dk-help a{display:flex;align-items:center;gap:.5rem;padding:.45rem .5rem;border-radius:4px;color:var(--dk-text);text-decoration:none;font-size:.8125rem}',
    '.dk-help a:hover{background:var(--dk-hover,#ffffff10)}',
    '.dk-help a img{width:16px;height:16px;object-fit:contain}',
    '.dk-help a.is-pro{color:#f2994a!important}',
    'html.dk-overview .ui-doc-outline>.ui-panel:not(.dk-help),html.dk-overview .ui-doc-subp,html.dk-overview .ui-doc-subp-label{display:none!important}',

    /* 4 Docs home */
    'html.dk-home .ui-doc-side,html.dk-home .ui-doc-outline,html.dk-home .ui-doc-head,html.dk-home .ui-doc-pager,html.dk-home .ui-doc-quick{display:none!important}',
    'html.dk-home .ui-doc-grid{grid-template-columns:minmax(0,1fr)!important;max-width:72rem;margin:0 auto}',
    'html.dk-home .ui-doc-body>.ui-doc-subsec{padding:0;background:none;box-shadow:none}',
    'html.dk-home .ui-doc-body{max-width:none!important}',
    '.dk-home-page h2::before,.dk-home-page h2::after,.dk-home-page h1::after{display:none!important;content:none!important}',
    '.dk-home-page img{max-width:none;margin:0;box-shadow:none;border-radius:0;width:16px!important;height:16px!important;object-fit:contain}',
    '.dk-home-page .dk-progress img{width:20px!important;height:20px!important}',
    '.dk-home-page .dk-path-art img{width:3.5rem!important;height:3.5rem!important}',
    '.dk-home-page .dk-sticker img{width:58%!important;height:58%!important}',
    '.dk-home-page .dk-pop img,.dk-home-page .dk-btn img,.dk-home-page .dk-search img,.dk-home-page .dk-results img{width:16px!important;height:16px!important}',
    '.dk-home-page .dk-help-card>img{width:2.25rem!important;height:2.25rem!important}',
    '.dk-home-page .dk-explore img.dk-shot{width:100%!important;height:auto!important;border-radius:.375rem}',
    '.dk-home-page .dk-explore p img{width:1.75rem!important;height:1.75rem!important}',
    '.dk-chapters img,.dk-hero img{margin:0;box-shadow:none;max-width:none;width:16px!important;height:16px!important;object-fit:contain}',
    '.dk-hero .dk-sticker img{width:58%!important;height:58%!important}',
    '.dk-chapters .dk-sticker img{width:58%!important;height:58%!important}',
    '.dk-chapters b img,.dk-chapters .dk-btn img{width:16px!important;height:16px!important;border-radius:0}',
    '.dk-h{margin:0 0 3.5rem}',
    '.dk-h-top{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:2.5rem;align-items:center}',
    '.dk-h h1{margin:0 0 1rem;font-family:"Titillium Web",Titillium,sans-serif;font-size:3.25rem;line-height:1.05;font-weight:700;color:var(--dk-text);background:none!important;border:0!important;box-shadow:none!important;padding:0!important;display:block!important}',
    '.dk-h h1::before{display:none!important}',
    '.dk-h .type-lead{margin:0 0 1.5rem;font-size:1.125rem;line-height:1.6}',
    '.dk-search{position:relative;display:flex;gap:.5rem;margin:0 0 .875rem}',
    '.dk-search label{flex:1;display:flex;align-items:center;gap:.5rem;padding:0 .625rem;border-radius:.375rem;background:#f4f4f4;color:#222}',
    '.dk-search label img{width:18px;height:18px}',
    '.dk-search input{flex:1;min-width:0;height:2.75rem;border:0;outline:0;background:none;color:#222;font:500 1rem Inter,sans-serif}',
    '.dk-search kbd{padding:.1rem .4rem;border-radius:.25rem;background:#ddd;color:#333;font:600 .75rem Inter,sans-serif}',
    '.dk-results{position:absolute;left:0;right:0;top:calc(100% + .375rem);z-index:20;display:none;max-height:22rem;overflow:auto;padding:.375rem;border-radius:.5rem;background:var(--_bfa---surface--card);box-shadow:0 2px 4px #0006,0 18px 40px -10px #0009}',
    '.dk-results.is-open{display:block}',
    '.dk-results a{display:flex;align-items:center;gap:.5rem;padding:.5rem .625rem;border-radius:.25rem;color:var(--dk-text);text-decoration:none;font-size:.9rem}',
    '.dk-results a img{width:16px;height:16px;object-fit:contain}',
    '.dk-results a small{margin-left:auto;color:var(--dk-muted)}',
    '.dk-results a:hover,.dk-results a.is-sel{background:var(--dk-accent);color:#fff}',
    '.dk-results mark{background:none;color:inherit;font-weight:700;text-decoration:underline}',
    '.dk-pop{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;font-size:.8125rem;color:var(--dk-muted)}',
    '.dk-pop a{display:inline-flex;align-items:center;gap:.375rem;padding:.25rem .5rem;border-radius:.25rem;background:var(--_bfa---surface--raised);color:var(--dk-text);text-decoration:none;font-weight:600}',
    '.dk-pop a img{width:14px;height:14px;object-fit:contain}',
    '.dk-explore{display:block;padding:.75rem;color:var(--dk-text);text-decoration:none}',
    '.dk-explore img.dk-shot{display:block;width:100%;border-radius:.375rem;box-shadow:0 1px 3px #0008}',
    '.dk-explore p{display:flex;gap:.625rem;align-items:flex-start;margin:.75rem .25rem .25rem;font-size:.875rem;line-height:1.45}',
    '.dk-explore p img{flex:0 0 1.75rem;width:1.75rem;height:1.75rem;padding:.3rem;border-radius:.375rem;background:#5a6ab0}',
    '.dk-sec-head{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1rem;margin:0 0 1.25rem}',
    '.dk-sec-head h2{margin:0 0 .5rem;font-family:"Titillium Web",Titillium,sans-serif;font-size:2rem;line-height:1.1;color:var(--dk-text);background:none!important;border:0!important;box-shadow:none!important;padding:0!important}',
    '.dk-sec-head p{margin:0;max-width:34rem;color:var(--dk-muted);font-size:.9rem}',
    '.dk-progress{display:flex;align-items:center;gap:.75rem;padding:.625rem .875rem;font-size:.8125rem;color:var(--dk-muted)}',
    '.dk-progress b{color:var(--dk-text)}',
    '.dk-paths{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:1rem;padding:1rem;border-radius:var(--_bfa---shape--bevel,.625rem);background:var(--_bfa---surface--panel);box-shadow:0 1px 2px #0005}',
    '.dk-path{display:flex;flex-direction:column;overflow:hidden;color:var(--dk-text);text-decoration:none;transition:transform .2s ease,box-shadow .2s ease}',
    '.dk-path:hover{transform:translateY(-2px)}',
    '.dk-path-art{position:relative;display:grid;place-items:center;height:7rem;background:radial-gradient(circle at 50% 40%,#ffffff14,transparent 70%),#0002}',
    '.dk-path-art img{width:3.5rem;height:3.5rem;object-fit:contain;filter:drop-shadow(0 4px 6px #0009)}',
    '.dk-path-art span{position:absolute;left:.5rem;top:.5rem;padding:.15rem .4rem;border-radius:.25rem;background:#000a;color:#fff;font:600 .6875rem Inter,sans-serif}',
    '.dk-path-tx{padding:.75rem}',
    '.dk-path-tx b{display:block;margin:0 0 .5rem;font:700 1rem/1.2 Inter,sans-serif}',
    '.dk-path-tx small{display:flex;flex-wrap:wrap;gap:.375rem .75rem;color:var(--dk-muted);font-size:.75rem}',
    '.dk-secs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem}',
    '.dk-sec{display:grid;grid-template-columns:3rem minmax(0,1fr);gap:.875rem;align-items:start;padding:1rem;color:var(--dk-text);text-decoration:none;transition:transform .2s ease,box-shadow .2s ease}',
    '.dk-sec:hover{transform:translateY(-2px)}',
    '.dk-sec .dk-sticker{width:3rem;height:3rem;border-radius:.625rem}',
    '.dk-sec b{display:block;margin:0 0 .25rem;font:700 1.05rem/1.2 Inter,sans-serif}',
    '.dk-sec p{margin:0 0 .375rem;font-size:.8125rem;line-height:1.4;opacity:.8}',
    '.dk-sec small{color:var(--dk-muted);font-size:.75rem}',
    '.dk-two{display:grid;grid-template-columns:1fr 1fr;gap:1rem}',
    '.dk-help-card{display:grid;grid-template-columns:2.25rem minmax(0,1fr);gap:.875rem;padding:1.25rem}',
    '.dk-help-card>img{width:2.25rem;height:2.25rem;object-fit:contain}',
    '.dk-help-card b{display:block;margin:0 0 .375rem;font:700 1.15rem Inter,sans-serif}',
    '.dk-help-card p{margin:0 0 .75rem;font-size:.875rem;color:var(--dk-muted)}',
    '.dk-help-card .dk-btns{display:flex;flex-wrap:wrap;gap:.5rem}',
    '.dk-help-card.is-pro{box-shadow:inset 0 0 0 1px #f2994a99,0 1px 2px #0006}',
    '.dk-help-card.is-pro .dk-btn{background:#f2994a;color:#2a1600!important}',
    '.dk-fresh{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;padding:1.25rem}',
    '.dk-fresh b{display:block;font:700 1.15rem Inter,sans-serif;margin:0 0 .25rem}',
    '.dk-fresh p{margin:0;color:var(--dk-muted);font-size:.875rem}',
    '@media(max-width:991px){.dk-h-top{grid-template-columns:1fr}.dk-paths{grid-template-columns:repeat(3,minmax(0,1fr))}.dk-secs{grid-template-columns:repeat(2,minmax(0,1fr))}}',
    '@media(max-width:600px){.dk-h h1{font-size:2.25rem}.dk-paths{grid-template-columns:repeat(2,minmax(0,1fr))}.dk-secs,.dk-two{grid-template-columns:1fr}}'
  ].join('\n');
  var st = d.createElement('style'); st.id = 'bfa-docs-layer'; st.textContent = CSS; d.head.appendChild(st);

  /* ---------------------------------------------------------------- helpers */
  function q(s, r) { return (r || d).querySelector(s); }
  function qa(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function esc(s) { var e = d.createElement('i'); e.textContent = s == null ? '' : String(s); return e.innerHTML; }
  function el(tag, cls, html) { var e = d.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function iu(f) { return !f ? '' : (/^https?:/.test(f) ? f : CDN + f); }
  function ico(f, cls) { return '<img alt="" class="' + (cls || 'is-color') + '" src="' + (iu(f) || CDN + IC.doc) + '">'; }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function plural(n, one, many) { return n + ' ' + (n === 1 ? one : many); }
  function mins(m) { m = m || 1; return m < 120 ? m + ' min' : Math.round(m / 60) + ' h'; }

  var NAV = null, IDX = null;
  function index(nav) {
    var by = {}, flat = [];
    (nav.sections || []).forEach(function (s, si) {
      var l = { t: s.t, s: s.s, i: s.i, c: s.c, d: s.d, n: s.n, m: s.m, land: 1, _sec: s, _si: si };
      by[s.s] = l; flat.push(l);
      (function walk(c, par) { (c || []).forEach(function (n) { n._p = par; n._sec = s; by[n.s] = n; flat.push(n); walk(n.c, n); }); })(s.c, l);
    });
    return { by: by, flat: flat };
  }
  function slugOf(href) { return String(href || '').split('#')[0].split('?')[0].replace(/\/$/, '').split('/').pop(); }
  var here = slugOf(location.pathname);

  /* ---------------------------------------------------------------- 2 breadcrumb */
  function crumbs() {
    var c = q('.ui-doc-crumb'); if (!c || c.dataset.dk) return; c.dataset.dk = '1';
    var root = q('a', c); if (root) root.setAttribute('href', HOME);
    if (here === 'home') { while (root && root.nextSibling) root.nextSibling.remove(); if (root) root.setAttribute('aria-current', 'page'); return; }
    var cur = IDX.by[here]; if (!cur) return;
    var sec = cur.land ? cur : IDX.by[cur._sec.s];
    var sa = q('.ui-doc-crumb-section', c), hereEl = q('.ui-doc-crumb-here', c);
    if (sa) {
      sa.setAttribute('href', '/docs/' + sec.s); sa.textContent = sec.t;
      var si = sa.previousElementSibling; if (si && si.tagName === 'IMG') { si.src = iu(sec.i); si.classList.add('is-color'); }
    }
    if (cur.land) {                         /* the overview itself: Documentation ▶ Group */
      if (hereEl) { var hi = hereEl.previousElementSibling, hs = hi && hi.previousElementSibling; hereEl.remove(); if (hi && hi.tagName === 'IMG') hi.remove(); if (hs && hs.classList.contains('ui-doc-crumb-sep')) hs.remove(); }
      if (sa) sa.setAttribute('aria-current', 'page');
      return;
    }
    var chain = []; for (var x = cur._p; x && !x.land; x = x._p) chain.unshift(x);
    var hereImg = hereEl && hereEl.previousElementSibling;
    if (hereImg && hereImg.tagName === 'IMG') { hereImg.src = iu(cur.i); hereImg.classList.add('is-color'); } else hereImg = hereEl;
    if (!hereImg) return;
    chain.forEach(function (n) {           /* Documentation ▶ Group ▶ Chapter ▶ … ▶ Page */
      c.insertBefore(el('span', 'dk-crumb-x', '<img alt="" class="ui-icon is-16 is-color" src="' + iu(n.i) + '"><a class="ui-doc-crumb-link" href="/docs/' + n.s + '">' + esc(n.t) + '</a><span class="ui-doc-crumb-sep">▶</span>'), hereImg);
    });
  }

  /* ---------------------------------------------------------------- help panels (right side) */
  function panel(title, rows) {
    var p = el('div', 'ui-panel dk-help');
    p.innerHTML = '<div class="ui-panel-head" data-panel-toggle role="button" tabindex="0"><img alt="" class="ui-panel-caret" src="' + CDN + IC.caret + '"><span class="ui-panel-title">' + esc(title) + '</span></div><div class="ui-panel-body">' +
      rows.map(function (r) { return '<a href="' + r[2] + '"' + (r[3] ? ' class="' + r[3] + '"' : '') + (/^https?:/.test(r[2]) ? ' target="_blank" rel="noopener"' : '') + '>' + ico(r[0]) + '<span>' + esc(r[1]) + '</span></a>'; }).join('') + '</div>';
    var hd = q('.ui-panel-head', p), bd = q('.ui-panel-body', p), cr = q('.ui-panel-caret', p);
    hd.addEventListener('click', function () { var o = bd.hidden; bd.hidden = !o; cr.classList.toggle('is-collapsed', !o); });
    return p;
  }
  function helpPanels(title) {
    var aside = q('.ui-doc-outline'); if (!aside || q('.dk-help', aside)) return;
    var print = 'javascript:window.print()';
    aside.insertBefore(panel('Stuck?', [
      [IC.comm, 'Ask on Discord', DISCORD],
      [IC.light, 'Report a doc issue', ISSUE + '?title=' + encodeURIComponent('Docs: ' + title)],
      [IC.world, 'Pro help · Trinumedia ↗', PRO, 'is-pro']]), aside.firstChild);
    aside.insertBefore(panel('Take it with you', [
      [IC.file, 'This section (print or PDF)', print],
      [IC.doc, 'Full manual, offline (soon)', 'https://github.com/Bforartists/Manual']]), aside.firstChild);
  }

  /* ---------------------------------------------------------------- 3 group overview */
  function overview(sec) {
    if (R.classList.contains('dk-overview')) return;
    R.classList.add('dk-overview');
    var art = q('.ui-doc-article'), body = q('.ui-doc-body'); if (!art || !body) return;
    var secs = NAV.sections, si = sec._si, chapters = sec.c || [], first = chapters[0];
    var title = sec.t, summary = sec.d || ((q('.ui-doc-summary') || {}).textContent || '').trim();
    /* hero */
    var hero = el('div', 'dk-hero');
    hero.innerHTML = '<div class="dk-sticker">' + ico(sec.i) + '</div><div class="dk-hero-tx"><div class="dk-eyebrow">Section ' + (si + 1) + ' of ' + secs.length + ' · Documentation</div>' +
      '<h1 class="type-h1 ui-doc-title">' + esc(title) + '</h1><p class="type-lead ui-doc-summary">' + esc(summary) + '</p><div class="dk-hero-go">' +
      (first ? '<a class="dk-btn is-primary" href="/docs/' + first.s + '">' + ico(first.i) + 'Start with ' + esc(first.t) + '</a>' : '') +
      '<span>' + plural(chapters.length, 'chapter', 'chapters') + ' · ' + plural(sec.n || 0, 'page', 'pages') + ' · about ' + mins(sec.m) + ' of reading</span></div></div>';
    art.insertBefore(hero, art.firstChild);
    /* the intro text that repeats the summary goes */
    qa('p', body).slice(0, 2).forEach(function (p) { var t = p.textContent.trim(); if (summary && t.indexOf(summary.replace(/[.…]+$/, '')) === 0) { var rest = t.slice(summary.length).trim(); if (rest) p.textContent = rest; else p.remove(); } });
    /* chapter cards: categories (h3) and links from the synced list, details from nav.json */
    var src = q('.ui-doc-cards', body); if (!src) return;
    var box = el('div', 'dk-chapters' + (ls('bfa-docs-cards') === 'list' ? ' is-list' : ''));
    box.innerHTML = '<div class="dk-chapters-bar"><span class="type-label">Chapters</span><div class="dk-seg" role="group" aria-label="Card view"><button type="button" data-v="grid">Grid</button><button type="button" data-v="list">List</button></div></div>';
    var num = 0, grid = null;
    function card(a) {
      var href = a.getAttribute('href') || '', n = IDX.by[slugOf(href)] || {}, li = a.closest('li');
      var t = n.t || ((q('b', a) || a).textContent || '').trim();
      var sum = n.d || ((q('span', a) || {}).textContent || '').trim();
      if (!sum && li) { var tx = li.textContent, k = tx.indexOf(t); sum = (k > -1 ? tx.slice(k + t.length) : '').replace(/^\s*[—–-]\s*/, '').replace(/\d+ pages?$/, '').trim(); }
      var below = 0; (function cnt(c) { (c || []).forEach(function (x) { below++; cnt(x.c); }); })(n.c);
      num++;
      var start = num === 1, c = el('a', 'dk-card dk-ccard' + (start ? ' is-start' : ''));
      c.href = href;
      c.innerHTML = '<div class="dk-sticker">' + ico(n.i) + '</div><div><small>' + (start ? 'Start here · 1' : num) + '</small><b>' + ico(n.i) + '<span>' + esc(t) + '</span></b>' +
        (sum ? '<p>' + esc(sum) + '</p>' : '') + '<span class="dk-btn is-small">' + ico(n.i) + esc(n.b || 'Read') + '</span>' + (below ? '<em>' + plural(below, 'page', 'pages') + '</em>' : '') + '</div>';
      return c;
    }
    qa(':scope > *', src).forEach(function (x) {
      if (/^H[2-6]$/.test(x.tagName)) { box.appendChild(el('h3', 'dk-cat', esc(x.textContent))); grid = null; return; }
      qa('a[href]', x).forEach(function (a) { if (!grid) { grid = el('div', 'dk-cgrid'); box.appendChild(grid); } grid.appendChild(card(a)); });
    });
    src.parentNode.replaceChild(box, src);
    function view(v) { box.classList.toggle('is-list', v === 'list'); qa('.dk-seg button', box).forEach(function (b) { b.classList.toggle('is-on', b.dataset.v === v); }); ls('bfa-docs-cards', v); }
    view(ls('bfa-docs-cards') === 'list' ? 'list' : 'grid');
    qa('.dk-seg button', box).forEach(function (b) { b.addEventListener('click', function () { view(b.dataset.v); }); });
    /* pager: back to the Docs home, on to the next group */
    var row = q('[data-doc-pager] .ui-doc-foot-row'), nx = secs[si + 1];
    if (row) row.innerHTML =
      '<div class="ui-doc-foot-half is-prev"><div class="ui-doc-foot-label">' + ico(IC.file, '') + 'Back to</div><a class="ui-doc-foot-go" href="' + HOME + '"><i class="ui-doc-tri is-l"></i><span>Documentation home</span></a></div>' +
      (nx ? '<div class="ui-doc-foot-half is-next"><div class="ui-doc-foot-label">' + ico(IC.doc, '') + 'Next section</div><a class="ui-doc-foot-go" href="/docs/' + nx.s + '">' + ico(nx.i) + '<span>' + esc(nx.t) + '</span><i class="ui-doc-tri"></i></a></div>' : '<div class="ui-doc-foot-half is-next is-empty"></div>');
    helpPanels(title);
  }

  /* ---------------------------------------------------------------- 4 Docs home */
  function home() {
    if (R.classList.contains('dk-home')) return;
    var data = q('.ui-doc-home'); if (!data) return;
    R.classList.add('dk-home');
    var body = q('.ui-doc-body'), F = { popular: [], path: [] };
    qa('li[data-k]', data).forEach(function (li) {
      var a = q('a', li), o = { t: li.textContent.trim(), h: a ? a.getAttribute('href') : '', ds: li.dataset };
      if (F[li.dataset.k] instanceof Array) F[li.dataset.k].push(o); else F[li.dataset.k] = o;
    });
    var secs = NAV.sections, total = 0; secs.forEach(function (s) { total += s.n || 0; });
    var h = el('div', 'dk-home-page');
    var ex = F.explore;
    h.innerHTML =
      '<section class="dk-h"><div class="dk-h-top"><div>' +
        '<div class="dk-eyebrow">' + esc(F.eyebrow ? F.eyebrow.t : 'The Bforartists manual') + '</div>' +
        '<h1>' + esc(F.headline ? F.headline.t : 'Documentation') + '</h1>' +
        '<p class="type-lead">' + esc(F.lead ? F.lead.t : '') + '</p>' +
        '<form class="dk-search" role="search" action="/search"><label>' + ico(IC.zoom, '') + '<input name="query" type="search" autocomplete="off" placeholder="Search tools, menus, hotkeys…" aria-label="Search the documentation"><kbd>F3</kbd></label>' +
        '<button class="dk-btn is-primary" type="submit">' + ico(IC.zoom, '') + 'Discover</button><div class="dk-results" role="listbox"></div></form>' +
        '<div class="dk-pop"><span>Popular:</span>' + F.popular.map(function (p) { return '<a href="' + esc(p.h) + '">' + ico(p.ds.i) + esc(p.t) + '</a>'; }).join('') + '</div>' +
      '</div>' + (ex ? '<a class="dk-card dk-explore" href="' + esc(ex.h || '#') + '"><img class="dk-shot" alt="The Bforartists interface" src="' + esc(ex.ds.img) + '"><p>' + ico('68b8f4efa40047ddcec7c6ae_view3d.svg') + '<span><b>' + esc(ex.t) + '</b> ' + esc(ex.ds.text || '') + '</span></p></a>' : '') +
      '</div></section>' +
      (F.path.length ? '<section class="dk-h"><div class="dk-sec-head"><div><div class="dk-eyebrow">Quick Start · Pick a path</div><h2>Learn by making something</h2><p>Each path is a short project with a template file, clear steps, and the theory behind every step. Finish one and it is checked off here.</p></div>' +
        '<div class="dk-card dk-progress">' + ico('68b9bb9cc5062fa217606ff2_time.svg', '') + '<span><b>Your progress</b> · 0 of ' + F.path.length + ' paths · coming soon</span></div></div>' +
        '<div class="dk-paths">' + F.path.map(function (p) {
          var lv = p.ds.level || '', dots = lv === 'Beginner' ? '●○○' : lv === 'Intermediate' ? '●●○' : lv === 'Advanced' ? '●●●' : '';
          return '<a class="dk-card dk-path" href="' + esc(p.h || '#') + '"><div class="dk-path-art"><span>' + esc(p.ds.area || '') + '</span>' + ico(p.ds.i) + '</div><div class="dk-path-tx"><b>' + esc(p.t) + '</b><small><span>' + dots + ' ' + esc(lv) + '</span>' + (p.ds.min ? '<span>' + esc(p.ds.min) + ' min</span>' : '') + '</small></div></a>';
        }).join('') + '</div></section>' : '') +
      '<section class="dk-h"><div class="dk-sec-head"><div><div class="dk-eyebrow">Reference · The whole manual at a glance</div><h2>' + esc(['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve'][secs.length] || secs.length) + ' sections, same as the sidebar</h2><p>Same order and icons as the sidebar panels, so this page also teaches you the sidebar. ' + total + ' pages in all.</p></div></div>' +
        '<div class="dk-secs">' + secs.map(function (s) {
          return '<a class="dk-card dk-sec" href="/docs/' + s.s + '"><div class="dk-sticker">' + ico(s.i) + '</div><div><b>' + esc(s.t) + '</b>' + (s.d ? '<p>' + esc(s.d) + '</p>' : '') + '<small>' + plural((s.c || []).length, 'chapter', 'chapters') + ' · ' + plural(s.n || 0, 'page', 'pages') + '</small></div></a>';
        }).join('') + '</div></section>' +
      '<section class="dk-h"><div class="dk-card dk-fresh"><div><div class="dk-eyebrow">What changed · 5.1</div><b>Fresh from development</b><p>Pulled from the manual repository every time a docs task closes, so new tools show up here first.</p></div><a class="dk-btn" href="https://github.com/Bforartists/Manual/commits/docs2/main" target="_blank" rel="noopener">' + ico(IC.file, '') + 'All changes</a></div></section>' +
      '<section class="dk-h dk-two">' +
        '<div class="dk-card dk-help-card">' + ico(IC.comm, '') + '<div><b>Stuck? Ask the community</b><p>Artists and developers answer on Discord every day. Share a screenshot and the page you were on.</p><div class="dk-btns"><a class="dk-btn is-small" href="' + DISCORD + '" target="_blank" rel="noopener">' + ico(IC.comm, '') + 'Discord</a><a class="dk-btn is-small" href="' + ISSUE + '" target="_blank" rel="noopener">' + ico(IC.light, '') + 'Report a doc issue</a></div></div></div>' +
        '<div class="dk-card dk-help-card is-pro">' + ico(IC.world, '') + '<div><b>Need it done? Pro support</b><p>Training, pipeline help and custom tools for studios and schools, from the team behind Bforartists at Trinumedia.</p><div class="dk-btns"><a class="dk-btn is-small" href="' + PRO + '" target="_blank" rel="noopener">Talk to Trinumedia ↗</a></div></div></div>' +
      '</section>';
    body.innerHTML = ''; body.appendChild(h);
    homeSearch(q('.dk-search', h));
  }
  function homeSearch(f) {
    if (!f) return;
    var inp = q('input', f), res = q('.dk-results', f), hits = [], sel = -1;
    function mk(t, v) { var i = t.toLowerCase().indexOf(v); return i < 0 ? esc(t) : esc(t.slice(0, i)) + '<mark>' + esc(t.slice(i, i + v.length)) + '</mark>' + esc(t.slice(i + v.length)); }
    function run() {
      var v = inp.value.trim().toLowerCase(); sel = -1;
      if (!v) { res.classList.remove('is-open'); res.innerHTML = ''; return; }
      var P = IDX.flat.filter(function (n) { return n.t.toLowerCase().indexOf(v) > -1; })
        .sort(function (a, b) { return (b.t.toLowerCase().indexOf(v) === 0) - (a.t.toLowerCase().indexOf(v) === 0); }).slice(0, 10);
      res.innerHTML = P.map(function (n) { return '<a role="option" href="/docs/' + n.s + '">' + ico(n.i) + '<span>' + mk(n.t, v) + '</span><small>' + esc(n.land ? 'Section' : n._sec.t) + '</small></a>'; }).join('') +
        '<a role="option" href="/search?query=' + encodeURIComponent(inp.value.trim()) + '">' + ico(IC.world, '') + '<span>Search the whole site for “' + esc(inp.value.trim()) + '”</span></a>';
      res.classList.add('is-open'); hits = qa('a', res);
    }
    inp.addEventListener('input', run); inp.addEventListener('focus', run);
    inp.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (!hits.length) return; sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + hits.length) % hits.length; hits.forEach(function (a, i) { a.classList.toggle('is-sel', i === sel); }); }
      else if (e.key === 'Enter' && sel > -1) { e.preventDefault(); location.href = hits[sel].getAttribute('href'); }
      else if (e.key === 'Escape') { inp.value = ''; run(); }
    });
    d.addEventListener('click', function (e) { if (!f.contains(e.target)) res.classList.remove('is-open'); });
    d.addEventListener('keydown', function (e) { if (e.key === 'F3') { e.preventDefault(); e.stopImmediatePropagation(); inp.focus(); } }, true);
  }

  /* ---------------------------------------------------------------- start */
  function apply(nav) {
    if (!nav || !nav.sections) return;
    NAV = nav; IDX = index(nav);
    crumbs();
    if (here === 'home') return home();
    var n = IDX.by[here];
    if (n && n.land) overview(n);
  }
  function start() {
    var cached = null; try { cached = JSON.parse(ls(NK) || 'null'); } catch (e) {}
    if (cached && cached.sections) apply(cached);
    if (window.fetch) fetch(NAVURL, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).then(function (n) {
      if (!n || !n.sections) return;
      if (!NAV || NAV.commit !== n.commit) { ls(NK, JSON.stringify(n)); if (!NAV) apply(n); }
    }).catch(function () {});
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { setTimeout(start, 0); });
  else setTimeout(start, 0);
})();
