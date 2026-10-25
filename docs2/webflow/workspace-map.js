/* Bforartists Docs 2.0 · workspace maps · @version 1.0.9
 *
 * Runs on the Doc Pages template (registered Webflow script, page footer), next to the docs layer.
 * The sync writes plain lists from docs2/workspaces.yml; this script turns them into:
 *
 *   🗺️  .ui-ws-map       a workspace page: hover an area of the screenshot to see which editor it is,
 *                         what it is for in this workspace, and jump to its chapter
 *   🧭  .ui-ws-explorer  the Workspaces overview: every workspace in one explorer, with the app's
 *                         tabs as a wrapping ribbon, previous / next, ← → keys and full screen.
 *                         On the Docs home (a closing `more` row) the tabs are focus tabs like the
 *                         Download page's release switch: the chosen one widens, the map slides in.
 *
 * List rows: <li data-k="shot|ws|area" …>. Area rows carry data-box="left,top,width,height" (% of
 * the screenshot), data-c (colour), data-i (icon file) and "<a href=chapter>Editor</a> — note".
 * Published as /Manual/webflow/workspace-map-<version>.js.
 */
(function () {
  var d = document, R = d.documentElement;
  if (R.dataset.bfaWs) return;
  R.dataset.bfaWs = '1';
  var CDN = 'https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
  var IC = {
    fwd: '68b9b76aa841ed4158a2f249_forward.svg', back: '68b9b6dd5029e853d2e4ef85_back.svg',
    fsIn: '68b781e1216e0e1e52a012da_fullscreen_enter.svg', fsOut: '68b781e1275c5f760589fe66_fullscreen_exit.svg',
    ws: '68b8cd9563b35e0ca05c7797_workspace.svg', tag: '68b9b78469eaa2203439e9cb_hide_on.svg',
    doc: '68b9b72e6ab175721a9bf7cb_documents.svg'
  };
  var CSS = [
    '.wsx{--wsx-card:var(--_bfa---surface--card,#404040);--wsx-panel:var(--_bfa---surface--panel,#363636);--wsx-sink:#292929;--wsx-text:var(--_bfa---text--primary,#ececec);--wsx-mute:#a8a8a8;--wsx-sel:var(--_bfa---accent--selected,#4f7fc0);margin:1.5rem 0 2rem;color:var(--wsx-text);font-family:var(--_bfa---type--text,Inter,sans-serif)}',
    'html.theme-light .wsx{--wsx-card:#fff;--wsx-panel:#f2f2f2;--wsx-sink:#e6e6e6;--wsx-text:#222;--wsx-mute:#666}',
    '.wsx-src{display:none!important}',
    '.wsx a{text-decoration:none!important}',
    /* ribbon: the app\'s tabs, wrapping instead of scrolling */
    '.wsx .wsx-rib{display:flex;flex-wrap:wrap;gap:.375rem;margin:0 0 .875rem;overflow:visible;background:none;box-shadow:none}',
    '.wsx .wsx-rib .ui-segment-item{flex:0 0 auto;cursor:pointer;font-family:inherit;font-weight:600}',
    '.wsx .wsx-rib .ui-seg-icon{margin:0!important}',
    /* fixed columns: the picture never changes size when the side panel's text does (a size change moved the areas under the mouse and flickered) */
    '.wsx{container-type:inline-size}',
    '.wsx-row{display:grid;grid-template-columns:minmax(0,1fr) 19rem;gap:1.25rem;align-items:start}',
    '.wsx-main{min-width:0;display:flex;flex-direction:column;gap:.75rem}',
    '.wsx-side{min-width:0;display:flex;flex-direction:column;gap:.875rem}',
    '@container (max-width:50rem){.wsx-row{grid-template-columns:minmax(0,1fr)}}',
    '@supports not (container-type:inline-size){@media (max-width:991px){.wsx-row{grid-template-columns:minmax(0,1fr)}}}',
    '.wsx.is-fs .wsx-row{grid-template-columns:minmax(0,1fr)}',
    '.wsx-card{position:relative;padding:.5rem;border-radius:.625rem;background:var(--wsx-card);box-shadow:inset .6px 1px 0 #ffffff0f,0 1px 2px #000b,6px 14px 18px -10px #0009}',
    /* the stage: screenshot + hotspots */
    '.wsx-stage{position:relative;overflow:hidden;border-radius:.375rem;background:var(--wsx-sink);aspect-ratio:1600/870}',
    '.wsx-stage>img{position:absolute;inset:0;width:100%;height:100%;object-fit:fill;margin:0!important;transition:opacity .25s}',
    '.wsx-stage.is-loading>img{opacity:0}',
    '.wsx-stage.is-loading:after{content:"";position:absolute;left:50%;top:50%;width:2rem;height:2rem;margin:-1rem;border-radius:50%;border:3px solid #ffffff22;border-top-color:var(--wsx-sel);animation:wsxspin .8s linear infinite}',
    '@keyframes wsxspin{to{transform:rotate(360deg)}}',
    '.wsx-hot{position:absolute;display:block;box-sizing:border-box;border-radius:.25rem;border:1px dashed #ffffff30;background:transparent;transition:background .15s,box-shadow .15s,border-color .15s;cursor:pointer;outline:0}',
    '.wsx-hot:hover,.wsx-hot:focus-visible{border-color:#ffffff80}',
    '.wsx-hot.is-on{border:2px solid var(--c);background:color-mix(in srgb,var(--c) 18%,transparent);box-shadow:0 0 0 2px #0009,0 0 1.5rem color-mix(in srgb,var(--c) 45%,transparent);z-index:2}',
    '.wsx-tag{position:absolute;left:.375rem;top:.375rem;display:none;align-items:center;gap:.375rem;max-width:calc(100% - .75rem);padding:.2rem .5rem .2rem .3rem;border-radius:.25rem;background:#1d1d1df0;color:#fff;font:600 .75rem/1.2 Inter,sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;pointer-events:none;box-shadow:0 2px 6px #0008}',
    '.wsx-tag img{width:14px;height:14px;margin:0!important}',
    '.wsx-hot.is-on .wsx-tag,.wsx.is-labels .wsx-hot .wsx-tag{display:inline-flex}',
    /* a big editor icon in the middle of the active area (every area with labels on) */
    '.wsx-hot{container-type:size}',
    '.wsx-big{position:absolute;left:50%;top:50%;display:none;place-items:center;box-sizing:border-box;width:min(5rem,40%);height:auto;aspect-ratio:1/1;transform:translate(-50%,-50%);border-radius:16%;background:radial-gradient(circle at 35% 30%,#ffffff26,#ffffff05 60%),#2b2b2be6;box-shadow:0 0 0 2px var(--c),0 3px 10px #000a;pointer-events:none}',
    '@supports (width:1cqh){.wsx-big{width:min(5rem,40cqw,64cqh)}}',
    '.wsx-big img{width:74%;height:74%;object-fit:contain;margin:0!important;filter:drop-shadow(0 2px 3px #0009)}',
    '.wsx-hot.is-on .wsx-big,.wsx.is-labels .wsx-hot .wsx-big{display:grid}',
    /* one icon per area: with the big icon showing, the tag keeps only the name (and goes where there is no room for a name) */
    '.wsx-hot:not(.is-tiny) .wsx-tag img{display:none}.wsx-hot:not(.is-tiny) .wsx-tag{padding:.2rem .5rem}',
    '.wsx-hot.is-narrow:not(.is-tiny) .wsx-tag{display:none!important}',
    /* thin areas (Timeline, Statusbar…): the tag sits just outside the strip, above it in the lower half, below it in the upper half, so it never clips */
    '.wsx-hot.is-tiny .wsx-tag{left:50%;top:50%;max-width:none;transform:translate(-50%,-50%)}',
    '.wsx-hot.is-flat .wsx-tag{top:calc(100% + 4px);transform:translateX(-50%)}',
    '.wsx-hot.is-flat.is-low .wsx-tag{top:auto;bottom:calc(100% + 4px)}',
    '@media (max-width:767px){.wsx-hot:not(.is-tiny) .wsx-tag{display:none!important}}',
    '.wsx-hot.is-on .wsx-big{animation:wsxpop .18s ease-out}',
    '@keyframes wsxpop{from{transform:translate(-50%,-50%) scale(.8);opacity:0}}',
    '.wsx-hot.is-narrow .wsx-tag b{display:none}.wsx-hot.is-narrow .wsx-tag{padding:.2rem}',
    '.wsx-hot.is-tiny .wsx-big{display:none!important}',
    '.wsx-empty{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.5rem;padding:1rem;text-align:center;color:var(--wsx-mute);font-size:.875rem}',
    '.wsx-empty b{color:var(--wsx-text);font-size:1.125rem}',
    /* buttons on the image */
    '.wsx-tools{position:absolute;top:1rem;right:1rem;display:flex;gap:.375rem;z-index:3}',
    '.wsx-ib{display:grid;place-items:center;width:2.25rem;height:2.25rem;padding:0;border:1px solid #ffffff1f;border-radius:.25rem;background:#2b2b2bd9;cursor:pointer;box-shadow:0 1px 2px #0009;backdrop-filter:blur(6px)}',
    '.wsx-ib:hover{background:#3a3a3a}',
    '.wsx-ib.is-on{background:var(--wsx-sel)}',
    '.wsx-ib img{width:16px;height:16px;margin:0!important}',
    '.wsx-edge{position:absolute;top:50%;margin-top:-1.25rem;width:2.5rem;height:2.5rem;z-index:3}',
    '.wsx-edge.is-l{left:1rem}.wsx-edge.is-r{right:1rem}',
    /* pager */
    '.wsx-pager{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);gap:.75rem;align-items:center}',
    '.wsx-pg{display:flex;align-items:center;gap:.625rem;min-width:0;padding:.625rem .875rem;border:0;border-radius:.625rem;background:var(--wsx-card);color:var(--wsx-text);cursor:pointer;text-align:left;font:inherit;box-shadow:inset .6px 1px 0 #ffffff0f,0 1px 2px #000b}',
    '.wsx-pg.is-r{justify-content:flex-end;text-align:right}',
    '.wsx-pg img{width:16px;height:16px;margin:0!important;flex:none}',
    '.wsx-pg small{display:block;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--wsx-mute)}',
    '.wsx-pg>span{min-width:0;overflow:hidden}',
    '.wsx-pg b{display:block;font-size:.9375rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
    '.wsx-pos{display:flex;align-items:center;gap:.5rem;color:var(--wsx-mute);font-size:.8125rem;white-space:nowrap}',
    '.wsx-key{display:inline-grid;place-items:center;min-width:1.6rem;height:1.6rem;padding:0 .35rem;border-radius:.25rem;background:#4c4c4c;border:1px solid #0009;box-shadow:inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a;color:#f0f0f0;font:700 .75rem Inter,sans-serif}',
    /* info panels */
    '.wsx-info{padding:1.125rem;border-radius:.625rem;background:var(--wsx-card);display:flex;flex-direction:column;gap:.625rem;box-shadow:inset .6px 1px 0 #ffffff0f,0 1px 2px #000b,6px 14px 18px -10px #0009}',
    '.wsx-eb{display:flex;align-items:center;gap:.5rem;font:700 .75rem Inter,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#5cb4f0}',
    '.wsx-dot{width:.75rem;height:.75rem;border-radius:3px;flex:none;background:var(--c,#9a9a9a)}',
    '.wsx-info .wsx-h{display:flex;align-items:center;gap:.5rem;margin:0!important;font:700 1.375rem/1.2 Inter,sans-serif!important;color:var(--wsx-text)}',
    '.wsx-info .wsx-h img{width:22px;height:22px;margin:0!important}',
    '.wsx-info p{margin:0!important;color:var(--wsx-mute);font-size:.9375rem;line-height:1.55}',
    '.wsx-info .ui-btn{align-self:flex-start}',
    '.wsx-all{padding:.875rem;border-radius:.625rem;background:var(--wsx-sink);box-shadow:inset 2px 5px 10px #0006}',
    '.wsx-all>small,.wsx-for>small{display:block;margin:0 0 .5rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--wsx-mute)}',
    '.wsx-chips{display:flex;flex-wrap:wrap;gap:.375rem}',
    '.wsx .wsx-chip{cursor:pointer;font-family:inherit;box-shadow:inset 0 -2px 0 var(--c)}',
    '.wsx .wsx-chip img{margin:0!important}',
    '.wsx-for{padding:1rem 1.125rem;border-radius:.625rem;background:var(--wsx-sink);box-shadow:inset 2px 5px 10px #0006;display:flex;flex-wrap:wrap;gap:.75rem 1.25rem;align-items:center;justify-content:space-between}',
    '.wsx-for p{margin:0!important;flex:1 1 18rem;color:var(--wsx-text);font-size:.9375rem;line-height:1.55}',
    '.wsx-for p>small{display:block;margin:0 0 .25rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--wsx-mute)}',
    '.wsx-ver{color:var(--wsx-mute);font-size:.75rem}',
    /* full screen: the picture gets the whole width, the info rides on top */
    '.wsx.is-fs{position:fixed;inset:0;z-index:9990;margin:0;padding:1rem;overflow:auto;background:#1e1e1e}',
    '.wsx.is-fs .wsx-side{display:none}',
    '.wsx.is-fs .wsx-stage{max-height:calc(100vh - 12rem);aspect-ratio:auto;height:min(calc(100vh - 12rem),calc((100vw - 3rem) * .544))}',
    '.wsx-ov{display:none}',
    '.wsx.is-fs .wsx-ov{display:flex;position:absolute;left:1rem;bottom:1rem;z-index:3;max-width:min(28rem,calc(100% - 2rem));padding:.75rem 1rem;gap:.75rem;align-items:center;border-radius:.5rem;background:#1d1d1dee;color:#fff;box-shadow:0 4px 16px #000a;font-size:.875rem;line-height:1.45}',
    '.wsx-ov b{display:block;font-size:1rem}',
    '.wsx-ov .ui-btn{flex:none}',
    'html.wsx-lock{overflow:hidden}',
    /* full screen sits above the site header and always shows a Close button; on small screens the note goes under the picture */
    '.wsx.is-fs{z-index:2147483000}',
    '.wsx-close{display:none}',
    '.wsx.is-fs .wsx-close{position:sticky;top:0;z-index:5;display:flex;justify-content:flex-end;margin:-.25rem 0 .5rem}',
    '.wsx.is-fs .wsx-tools [data-act=fs]{display:none}',
    '.wsx.is-fs .wsx-rib{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}',
    '@media (max-width:991px),(max-height:600px){.wsx.is-fs .wsx-ov{position:static;display:flex;flex-wrap:wrap;margin:.5rem 0 0;max-width:none;padding:.25rem;background:none;box-shadow:none;color:var(--wsx-text)}.wsx.is-fs .wsx-ov>div{flex:1 1 12rem}}',
    '@media (max-width:767px){.wsx-ib[data-act=fs]{display:none}}',
    '@media (max-width:767px){.wsx:not(.is-fs) .wsx-ov{display:flex;flex-wrap:wrap;gap:.5rem .75rem;align-items:center;margin:.5rem .25rem .25rem;font-size:.875rem;line-height:1.45;color:var(--wsx-text)}.wsx-ov>div{flex:1 1 12rem}.wsx-tag b{display:none}.wsx-tag{padding:.2rem}.wsx-edge,.wsx-ib[data-act=labels]{display:none}.wsx-tools{top:.75rem;right:.75rem}.wsx-ib{width:2rem;height:2rem}.wsx-side{max-width:none}.wsx-pager{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.wsx-pg{padding:.5rem .625rem}.wsx-pos{display:none}}',
    /* focus tabs (the Docs home): drawn like the Download page's release switch; the chosen tab widens, the rest narrow */
    '.wsx-ft{display:flex;gap:.5rem;margin:0 0 .75rem}',
    '.wsx .wsx-ftab{position:relative;flex:1 1 0;min-width:0;display:flex;align-items:center;justify-content:center;gap:.75rem;min-height:4.5rem;margin:0;padding:.625rem;border:0;border-radius:var(--_bfa---shape--bevel,14px);background:var(--_bfa---surface--panel,#363636);color:var(--wsx-text);font-family:var(--_bfa---type--ui,inherit);text-align:left;cursor:pointer;overflow:hidden;box-shadow:var(--bfa-low,inset .6px 1px 0 #ffffff0f,0 1px 2px #000b);transition:flex-grow .5s cubic-bezier(.2,.8,.2,1),background-color .15s}',
    '.wsx .wsx-ftab:hover{background-color:color-mix(in srgb,var(--_bfa---surface--panel,#363636) 88%,#fff)}',
    '.wsx .wsx-ftab.is-active{flex-grow:3.2;justify-content:flex-start;padding-right:2.75rem;background:var(--_bfa---surface--card,#404040)}',
    '.wsx .wsx-ftab.is-active:after{content:"";position:absolute;left:.875rem;right:.875rem;bottom:0;height:2px;border-radius:2px;background:var(--_bfa---accent--blue,#5cb4f0)}',
    '.wsx .wsx-ftab:before{display:none!important}',
    '.wsx .wsx-ftab .ui-focus-tile{flex:none;display:grid;place-items:center;width:3.25rem;height:3.25rem;margin:0}',
    '.wsx .wsx-ftab .ui-focus-tile img{width:1.875rem!important;height:1.875rem!important;margin:0!important;padding:0!important;object-fit:contain;max-width:none}',
    '.wsx .wsx-ftab .ui-focus-spine-label{display:none;flex:1 1 auto;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:1.0625rem;font-weight:600;color:var(--wsx-text)}',
    '.wsx .wsx-ftab.is-active .ui-focus-spine-label{display:block;animation:wsxfade .35s ease}',
    '@keyframes wsxfade{from{opacity:0}}',
    '.wsx .wsx-ftab .ui-focus-num{position:absolute;top:.5rem;right:.625rem;margin:0;font-size:.6875rem}',
    '.wsx.is-focus .wsx-row{padding:1rem;border-radius:1.25rem;background:var(--_bfa---surface--well,#262626);box-shadow:inset 0 14px 18px -8px #000000bf,inset 0 -2px 6px -2px #0006;overflow:hidden}',
    '.wsx.is-focus .wsx-pager{display:none}',
    '.wsx .wsx-pager .wsx-pg img{width:16px!important;height:16px!important;max-width:none}',
    '.wsx.is-focus .wsx-for .ui-btn+.ui-btn{margin-left:.5rem}',
    '.wsx-slide-r{animation:wsxinr .5s cubic-bezier(.2,.8,.2,1)}.wsx-slide-l{animation:wsxinl .5s cubic-bezier(.2,.8,.2,1)}',
    '@keyframes wsxinr{from{opacity:0;transform:translateX(3rem)}}@keyframes wsxinl{from{opacity:0;transform:translateX(-3rem)}}',
    '@media (prefers-reduced-motion:reduce){.wsx-slide-r,.wsx-slide-l,.wsx .wsx-ftab{animation:none!important;transition:none!important}}',
    'html.motion-reduced .wsx-slide-r,html.motion-reduced .wsx-slide-l{animation:none!important}',
    '@media (max-width:991px){.wsx .wsx-ftab:not(.is-active) .ui-focus-num{display:none}.wsx .wsx-ftab .ui-focus-tile{width:2.75rem;height:2.75rem}.wsx .wsx-ftab .ui-focus-tile img{width:1.5rem!important;height:1.5rem!important}.wsx .wsx-ftab{min-height:3.75rem;padding:.5rem}}',
    '@media (max-width:767px){.wsx-ft{overflow-x:auto;scrollbar-width:none;margin:0 -.25rem .625rem;padding:0 .25rem 2px}.wsx-ft::-webkit-scrollbar{display:none}.wsx .wsx-ftab{flex:0 0 3.75rem;gap:.5rem}.wsx .wsx-ftab.is-active{flex:0 0 auto;max-width:13rem;padding-right:2.25rem}.wsx.is-focus .wsx-row{padding:.5rem;border-radius:1rem}.wsx.is-focus .wsx-pager{display:grid}.wsx.is-focus .wsx-for .ui-btn+.ui-btn{margin-left:0}}',
    '@media (hover:none){.wsx-hot{border-color:#ffffff40}}'
  ].join('\n');

  function q(s, r) { return (r || d).querySelector(s); }
  function qa(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function esc(s) { var e = d.createElement('i'); e.textContent = s == null ? '' : String(s); return e.innerHTML; }
  function el(tag, cls, html) { var e = d.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function iu(f) { return !f ? '' : (/^https?:/.test(f) ? f : CDN + f); }
  function img(f, cls) { return '<img alt=""' + (cls ? ' class="' + cls + '"' : '') + ' src="' + (iu(f) || CDN + IC.doc) + '">'; }
  function btn(label, icon, mods, href) {
    return '<a class="ui-btn dk-btn' + (mods ? ' ' + mods : '') + '" href="' + esc(href) + '"><span class="ui-btn-icon"><img class="ui-icon is-color" alt="" src="' + (iu(icon) || CDN + IC.fwd) + '"></span><span class="ui-btn-label">' + esc(label) + '</span></a>';
  }
  var coarse = window.matchMedia && matchMedia('(hover: none)').matches;

  /* ---------------------------------------------------------------- reading the lists */
  function area(li) {
    var a = q('a', li), name = ((a || li).textContent || '').trim();
    var full = li.textContent.trim(), k = full.indexOf(name);
    var note = (k > -1 ? full.slice(k + name.length) : '').replace(/^\s*[—–-]\s*/, '').trim();
    var b = (li.dataset.box || '').split(',').map(Number);
    return { name: name, href: a ? a.getAttribute('href') : '', note: note, c: li.dataset.c || '#9a9a9a', i: li.dataset.i || '', box: b.length === 4 ? b : null };
  }
  function read(list) {
    var out = [], cur = null;
    qa(':scope > li, :scope > ul > li', list).forEach(function (li) {
      var k = li.dataset.k;
      if (k === 'ws' || k === 'shot') {
        var a = q('a', li);
        cur = { name: k === 'ws' ? ((a || li).textContent || '').trim() : (li.dataset.n || ''), href: a ? a.getAttribute('href') : (li.dataset.href || ''), img: li.dataset.img || '', i: li.dataset.i || '', v: li.dataset.v || '', sum: li.dataset.sum || '', areas: [] };
        out.push(cur);
      } else if (k === 'more') {
        var ma = q('a', li); out.more = { href: ma ? ma.getAttribute('href') : '', n: +li.dataset.n || 0 };
      } else if (k === 'area') {
        if (!cur) { cur = { name: '', href: '', img: '', v: '', sum: '', areas: [] }; out.push(cur); }
        var x = area(li); if (x.box) cur.areas.push(x);
      }
    });
    return out;
  }
  function hero(w) {   /* the area to show first: the biggest one under the Topbar */
    var best = 0, bi = 0;
    w.areas.forEach(function (a, i) { var s = a.box[2] * a.box[3]; if (a.box[1] > 1 && a.box[3] > 8 && s > best) { best = s; bi = i; } });
    return bi;
  }

  /* ---------------------------------------------------------------- one map (stage + info) */
  function Map(root, opts) {
    var self = this;
    this.root = root; this.opts = opts || {};
    this.stage = el('div', 'wsx-stage');
    this.card = el('div', 'wsx-card'); this.card.appendChild(this.stage);
    this.tools = el('div', 'wsx-tools');
    this.tools.innerHTML = '<button type="button" class="wsx-ib" data-act="labels" title="Show every label" aria-label="Show every label" aria-pressed="false">' + img(IC.tag) + '</button>' +
      '<button type="button" class="wsx-ib" data-act="fs" title="Full screen" aria-label="Full screen">' + img(IC.fsIn) + '</button>';
    this.card.appendChild(this.tools);
    this.ov = el('div', 'wsx-ov'); this.card.appendChild(this.ov);
    this.info = el('div', 'wsx-info');
    this.all = el('div', 'wsx-all');
    this.tools.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.dataset.act === 'labels') { var on = !root.classList.contains('is-labels'); root.classList.toggle('is-labels', on); b.classList.toggle('is-on', on); b.setAttribute('aria-pressed', on); }
      if (b.dataset.act === 'fs') self.fs();
    });
    this.all.addEventListener('click', function (e) { var c = e.target.closest('.wsx-chip'); if (c) self.pick(+c.dataset.n); });
    if (window.ResizeObserver) new ResizeObserver(function () { self.fit(); }).observe(this.stage);
  }
  Map.prototype.show = function (w) {
    var self = this, st = this.stage;
    this.w = w; this.on = -1;
    st.innerHTML = '';
    if (!w.img) {
      st.classList.remove('is-loading');
      st.innerHTML = '<div class="wsx-empty">' + img(IC.ws) + '<b>' + esc(w.name || 'This workspace') + '</b><span>A screenshot of this workspace is coming.</span></div>';
    } else {
      st.classList.add('is-loading');
      var im = new Image(); im.alt = (w.name ? w.name + ' workspace' : 'Workspace') + ' screenshot'; im.decoding = 'async';
      im.onload = function () { st.classList.remove('is-loading'); if (im.naturalWidth) st.style.aspectRatio = im.naturalWidth + '/' + im.naturalHeight; };
      im.onerror = function () { st.classList.remove('is-loading'); };
      im.src = w.img; st.appendChild(im);
    }
    w.areas.forEach(function (a, i) {
      var h = el('button', 'wsx-hot'); h.type = 'button';
      h.style.cssText = 'left:' + a.box[0] + '%;top:' + a.box[1] + '%;width:' + a.box[2] + '%;height:' + a.box[3] + '%;--c:' + a.c;
      if (a.box[1] + a.box[3] / 2 > 50) h.classList.add('is-low');   /* in the lower half: a thin area's tag goes above it */
      h.setAttribute('aria-label', a.name + (a.note ? ': ' + a.note : ''));
      h.innerHTML = '<span class="wsx-tag">' + (a.i ? img(a.i) : '') + '<b>' + esc(a.name) + '</b></span>' + (a.i ? '<span class="wsx-big">' + img(a.i) + '</span>' : '');
      h.addEventListener('mouseenter', function () { self.pick(i); });
      h.addEventListener('focus', function () { self.pick(i); });
      h.addEventListener('click', function () { self.pick(i); if (coarse && self.ov.offsetParent) self.ov.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); });
      h.addEventListener('dblclick', function () { if (a.href && !coarse) location.href = a.href; });
      st.appendChild(h);
    });
    this.all.innerHTML = w.areas.length ? '<small>What\u2019s here</small><div class="wsx-chips">' + w.areas.map(function (a, i) {
      return '<button type="button" class="ui-chip wsx-chip" data-n="' + i + '" style="--c:' + a.c + '">' + (a.i ? img(a.i, 'ui-chip-icon') : '<span class="wsx-dot"></span>') + esc(a.name) + '</button>';
    }).join('') + '</div>' : '';
    this.all.style.display = w.areas.length ? '' : 'none';
    this.fit();
    if (w.areas.length) this.pick(hero(w));
    else { this.info.innerHTML = '<div class="wsx-eb">' + img(IC.ws) + 'Workspace</div><div class="wsx-h">' + esc(w.name) + '</div>' + (w.sum ? '<p>' + esc(w.sum) + '</p>' : '') + (w.href ? btn('Open the ' + w.name + ' page', IC.fwd, 'is-small', w.href) : ''); this.ov.innerHTML = ''; }
  };
  /* small areas: the label shows only the editor icon; very small ones skip the big icon */
  Map.prototype.fit = function () {
    qa('.wsx-hot', this.stage).forEach(function (h) {
      var w = h.offsetWidth, ht = h.offsetHeight, tag = q('.wsx-tag b', h);
      h.classList.toggle('is-narrow', w < Math.max(110, (tag ? tag.textContent.length : 10) * 8 + 40) || (ht < 34 && ht >= 22));   /* a flat strip's tag sits outside it, so its name still fits */
      h.classList.toggle('is-tiny', w < 40 || ht < 22);
      h.classList.toggle('is-flat', ht < 22);
    });
  };
  Map.prototype.pick = function (i) {
    var w = this.w, a = w && w.areas[i]; if (!a || this.on === i) return;
    this.on = i;
    qa('.wsx-hot', this.stage).forEach(function (h, k) { h.classList.toggle('is-on', k === i); });
    qa('.wsx-chip', this.all).forEach(function (c, k) { c.classList.toggle('is-active', k === i); });
    var where = this.opts.title || w.name;
    var go = a.href ? btn('Open the ' + a.name + ' chapter', IC.fwd, 'is-small', a.href) : '';
    this.info.style.setProperty('--c', a.c);
    this.info.innerHTML = '<div class="wsx-eb"><span class="wsx-dot"></span>Area' + (where ? ' in ' + esc(where) : '') + '</div><div class="wsx-h">' + (a.i ? img(a.i) : '') + esc(a.name) + '</div>' + (a.note ? '<p>' + esc(a.note) + '</p>' : '') + go;
    this.ov.innerHTML = '<div><b>' + esc(a.name) + '</b>' + esc(a.note) + '</div>' + go;
  };
  Map.prototype.fs = function (fromBack) {
    var on = !this.root.classList.contains('is-fs'), self = this;
    if (on && window.innerWidth < 768) return;
    if (!this.closeBar) {
      this.closeBar = el('div', 'wsx-close', '<button type="button" class="ui-btn dk-btn is-small"><span class="ui-btn-icon"><img class="ui-icon is-color" alt="" src="' + CDN + IC.fsOut + '"></span><span class="ui-btn-label">Close full screen</span></button>');
      this.closeBar.addEventListener('click', function () { self.fs(); });
      this.root.insertBefore(this.closeBar, this.root.firstChild);
    }
    if (on) { try { history.pushState({ wsxFs: 1 }, ''); } catch (e) {} var pop = function () { window.removeEventListener('popstate', pop); if (self.root.classList.contains('is-fs')) self.fs(true); }; window.addEventListener('popstate', pop); this._pop = pop; }
    else if (!fromBack) { if (this._pop) window.removeEventListener('popstate', this._pop); try { if (history.state && history.state.wsxFs) history.back(); } catch (e) {} }
    this.root.classList.toggle('is-fs', on); R.classList.toggle('wsx-lock', on);
    var b = q('[data-act=fs]', this.tools);
    b.innerHTML = img(on ? IC.fsOut : IC.fsIn); b.title = on ? 'Exit full screen (Esc)' : 'Full screen'; b.setAttribute('aria-label', b.title);
    if (on) this.root.focus({ preventScroll: true });
    this.fit();
  };

  /* ---------------------------------------------------------------- a workspace page */
  function single(block) {
    var data = read(q('ul', block) || block)[0]; if (!data || !data.areas.length) return;
    /* use the screenshot already on the page (Webflow hosts it), and take its place */
    var fig = null, p = block.previousElementSibling;
    for (var k = 0; p && k < 3; k++, p = p.previousElementSibling) { if (p.matches && p.matches('figure') || q('img', p) && /figure/i.test(p.tagName + ' ' + p.className)) { fig = p; break; } }
    var shot = fig && q('img', fig);
    if (shot) { data.img = shot.currentSrc || shot.src || data.img; fig.style.display = 'none'; }
    var title = data.name || ((q('.ui-doc-title, h1') || {}).textContent || '').trim();
    data.name = title;
    var root = el('div', 'wsx is-single'); root.tabIndex = -1;
    var row = el('div', 'wsx-row'), main = el('div', 'wsx-main'), side = el('aside', 'wsx-side');
    var m = new Map(root, { title: title });
    main.appendChild(m.card);
    var hint = el('p', 'wsx-ver', (coarse ? 'Tap an area to see what it is for here' : 'Point at an area to see what it is for here; double-click it to open its chapter') + (data.v ? ' · screenshot from version ' + esc(data.v) : '') + '.');
    main.appendChild(hint);
    if (data.href) {   /* the Docs home: one workspace, then the way to all of them */
      var go = el('div', 'wsx-for');
      go.innerHTML = '<p><small>Go deeper</small>Every workspace that ships with Bforartists works the same way: its editors, what each one is for, and a jump to every chapter.</p>' + btn('Explore all workspaces', IC.ws, 'is-small is-accent', data.href);
      main.appendChild(go);
    }
    side.appendChild(m.all); side.appendChild(m.info);
    row.appendChild(main); row.appendChild(side); root.appendChild(row);
    block.classList.add('wsx-src'); block.parentNode.insertBefore(root, block);
    m.show(data);
    keys(root, null, m);
  }

  /* ---------------------------------------------------------------- the Workspaces overview */
  function explorer(block) {
    var all = read(q('ul', block) || block); if (!all.length) return;
    var more = all.more, focus = !!more;   /* the Docs home: focus tabs, no address change, a way to every workspace */
    var root = el('div', 'wsx is-explorer' + (focus ? ' is-focus' : '')); root.tabIndex = -1;
    var rib = el('div', focus ? 'wsx-ft' : 'ui-segment wsx-rib'); rib.setAttribute('role', 'tablist'); rib.setAttribute('aria-label', 'Workspaces');
    rib.innerHTML = all.map(function (w, i) {
      if (focus) return '<button type="button" role="tab" aria-selected="false" class="wsx-ftab" data-n="' + i + '" title="' + esc(w.name) + '"><span class="ui-focus-tile">' + img(w.i || IC.ws, 'ui-focus-sticker') + '</span><span class="ui-focus-spine-label">' + esc(w.name) + '</span><span class="ui-focus-num">' + (i < 9 ? '0' : '') + (i + 1) + '</span></button>';
      return '<button type="button" role="tab" aria-selected="false" class="ui-segment-item is-tag" data-n="' + i + '">' + (w.i ? img(w.i, 'ui-seg-icon') : '') + esc(w.name) + '</button>';
    }).join('');
    var row = el('div', 'wsx-row'), main = el('div', 'wsx-main'), side = el('aside', 'wsx-side');
    var m = new Map(root, {});
    m.card.insertAdjacentHTML('beforeend', '<button type="button" class="wsx-ib wsx-edge is-l" data-go="-1" title="Previous workspace" aria-label="Previous workspace">' + img(IC.back) + '</button>' +
      '<button type="button" class="wsx-ib wsx-edge is-r" data-go="1" title="Next workspace" aria-label="Next workspace">' + img(IC.fwd) + '</button>');
    var pager = el('div', 'wsx-pager');
    var forb = el('div', 'wsx-for');
    main.appendChild(m.card); main.appendChild(pager); main.appendChild(forb);
    side.appendChild(m.all); side.appendChild(m.info);
    row.appendChild(main); row.appendChild(side);
    root.appendChild(rib); root.appendChild(row);
    block.classList.add('wsx-src'); block.parentNode.insertBefore(root, block);
    var cur = 0, n = all.length;
    function slug(w) { return String(w.href || w.name).split('/').pop().replace(/^workspaces-/, ''); }
    function go(i, keepHash, dir) {
      var was = cur;
      cur = (i + n) % n; var w = all[cur], pv = all[(cur - 1 + n) % n], nx = all[(cur + 1) % n];
      qa('button', rib).forEach(function (b, k) { b.setAttribute('aria-selected', k === cur ? 'true' : 'false'); b.classList.toggle('is-active', k === cur); });
      if (focus && dir && was !== cur) {   /* the map slides in from the side it comes from */
        row.classList.remove('wsx-slide-l', 'wsx-slide-r'); void row.offsetWidth; row.classList.add(dir > 0 ? 'wsx-slide-r' : 'wsx-slide-l');
        var tb = rib.children[cur]; if (tb && rib.scrollWidth > rib.clientWidth) rib.scrollTo({ left: tb.offsetLeft - (rib.clientWidth - tb.offsetWidth) / 2, behavior: 'smooth' });
      }
      m.opts.title = w.name; m.show(w);
      pager.innerHTML = '<button type="button" class="wsx-pg" data-go="-1">' + img(IC.back) + '<span><small>Previous</small><b>' + esc(pv.name) + '</b></span></button>' +
        '<span class="wsx-pos"><span class="wsx-key">←</span>' + (cur + 1) + ' of ' + n + '<span class="wsx-key">→</span></span>' +
        '<button type="button" class="wsx-pg is-r" data-go="1"><span><small>Next</small><b>' + esc(nx.name) + '</b></span>' + img(IC.fwd) + '</button>';
      forb.innerHTML = '<p><small>What ' + esc(w.name) + ' is for</small>' + esc(w.sum || 'A ready-made layout of editors.') + (w.v ? ' <span class="wsx-ver">Screenshot from version ' + esc(w.v) + '.</span>' : '') + '</p>' +
        (focus ? '<span>' + (w.href ? btn('Open the ' + w.name + ' page', IC.doc, 'is-small', w.href) : '') + (more.href ? btn('Explore all ' + (more.n ? more.n + ' ' : '') + 'workspaces', IC.ws, 'is-small is-accent', more.href) : '') + '</span>'
          : (w.href ? btn('Open the ' + w.name + ' page', IC.ws, 'is-small is-accent', w.href) : ''));
      [pv, nx].forEach(function (x) { if (x.img) { var pre = new Image(); pre.src = x.img; } });   /* neighbours load ahead */
      if (!keepHash && !focus && history.replaceState) history.replaceState(history.state, '', '#ws-' + slug(w));
    }
    root.addEventListener('click', function (e) {
      var t = e.target.closest('[data-go]'); if (t) { go(cur + (+t.dataset.go), false, +t.dataset.go); return; }
      var b = e.target.closest('.wsx-rib button, .wsx-ftab'); if (b) go(+b.dataset.n, false, +b.dataset.n - cur);
    });
    /* swipe the picture sideways for the previous / next workspace */
    var sx = null, sy = 0;
    m.stage.addEventListener('touchstart', function (e) { var t = e.touches[0]; sx = t.clientX; sy = t.clientY; }, { passive: true });
    m.stage.addEventListener('touchend', function (e) {
      if (sx === null) return; var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy; sx = null;
      if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) { var dir = dx < 0 ? 1 : -1; go(cur + dir, false, dir); }
    }, { passive: true });
    var h = focus ? '' : (location.hash || '').replace(/^#ws-/, ''), start = 0;
    all.forEach(function (w, i) { if (h && slug(w) === h) start = i; });
    go(start, !h);
    keys(root, function (dir) { go(cur + dir, false, dir); }, m);
  }

  /* ← → step through workspaces while the pointer or focus is on the explorer, or in full screen; Esc leaves full screen */
  function keys(root, step, m) {
    var over = false;
    root.addEventListener('mouseenter', function () { over = true; });
    root.addEventListener('mouseleave', function () { over = false; });
    d.addEventListener('keydown', function (e) {
      if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
      var fs = root.classList.contains('is-fs');
      if (e.key === 'Escape' && fs) { m.fs(); return; }
      if (!step || e.altKey || e.ctrlKey || e.metaKey) return;
      if (!(fs || over || root.contains(d.activeElement))) return;
      if (e.key === 'ArrowLeft') { e.preventDefault(); step(-1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); step(1); }
    });
  }

  function start() {
    var a = qa('.ui-ws-map'), b = qa('.ui-ws-explorer');
    if (!a.length && !b.length) return;
    if (!d.getElementById('bfa-ws-css')) { var st = d.createElement('style'); st.id = 'bfa-ws-css'; st.textContent = CSS; d.head.appendChild(st); }
    a.forEach(function (x) { try { single(x); } catch (e) { if (window.console) console.warn('workspace map', e); } });
    b.forEach(function (x) { try { explorer(x); } catch (e) { if (window.console) console.warn('workspace explorer', e); } });
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { setTimeout(start, 0); }); else setTimeout(start, 0);
})();
