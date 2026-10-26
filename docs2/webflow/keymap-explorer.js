/* Bforartists Docs 2.0 · interactive keymap · @version 1.0.0
 *
 * Runs on the Doc Pages template (registered Webflow script, page footer). The sync turns
 * <!-- keymap-explorer --> in a page into <div class="ui-keymap"><ul><li data-k="keymap" data-src=…>,
 * and this script draws the explorer from keymap.json (built by docs2/tools/keymap.py from the
 * Bforartists source, so it always matches the app):
 *
 *   🧭  pick the editor and the mode; the keymap (PC or macOS) at the top
 *   ⌨️  a keyboard and mouse that show what each key does there, coloured by kind
 *   ⇧   Shift, Ctrl, Alt (and Cmd) toggle on screen, or hold them on your real keyboard
 *   🔎  search both ways: type an action to light its key, or pick a key to see everything on it
 *   📱  phones: a list grouped by modifier, same filters
 * Published as /Manual/webflow/keymap-explorer-<version>.js.
 */
(function () {
  var d = document, R = d.documentElement;
  if (R.dataset.bfaKm) return;
  R.dataset.bfaKm = '1';
  var CDN = 'https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
  var IC = { zoom: '68b9bbd23fb07538f848b579_viewzoom.svg' };

  /* ---------------------------------------------------------------- the keyboard (US layout) */
  var K = function (c, l, w) { return { c: c, l: l || c, w: w || 1 }; };
  var MAIN = [
    [K('ESC', 'Esc'), { gap: .5 }, K('F1'), K('F2'), K('F3'), K('F4'), { gap: .5 }, K('F5'), K('F6'), K('F7'), K('F8'), { gap: .5 }, K('F9'), K('F10'), K('F11'), K('F12')],
    [K('ACCENT_GRAVE', '`'), K('ONE', '1'), K('TWO', '2'), K('THREE', '3'), K('FOUR', '4'), K('FIVE', '5'), K('SIX', '6'), K('SEVEN', '7'), K('EIGHT', '8'), K('NINE', '9'), K('ZERO', '0'), K('MINUS', '-'), K('EQUAL', '='), K('BACK_SPACE', 'Backspace', 2)],
    [K('TAB', 'Tab', 1.5), K('Q'), K('W'), K('E'), K('R'), K('T'), K('Y'), K('U'), K('I'), K('O'), K('P'), K('LEFT_BRACKET', '['), K('RIGHT_BRACKET', ']'), K('BACK_SLASH', '\\', 1.5)],
    [K('CAPSLOCK', 'Caps', 1.75), K('A'), K('S'), K('D'), K('F'), K('G'), K('H'), K('J'), K('K'), K('L'), K('SEMI_COLON', ';'), K('QUOTE', "'"), K('RET', 'Enter', 2.25)],
    [K('LEFT_SHIFT', 'Shift', 2.25), K('Z'), K('X'), K('C'), K('V'), K('B'), K('N'), K('M'), K('COMMA', ','), K('PERIOD', '.'), K('SLASH', '/'), K('RIGHT_SHIFT', 'Shift', 2.75)],
    [K('LEFT_CTRL', 'Ctrl', 1.25), K('OSKEY', 'OS', 1.25), K('LEFT_ALT', 'Alt', 1.25), K('SPACE', 'Space', 6.25), K('RIGHT_ALT', 'Alt', 1.25), K('APP', 'Menu', 1.25), K('RIGHT_CTRL', 'Ctrl', 1.25)]
  ];
  var NAV = [
    [{ gap: 3 }],
    [K('INSERT', 'Ins'), K('HOME', 'Home'), K('PAGE_UP', 'PgUp')],
    [K('DEL', 'Del'), K('END', 'End'), K('PAGE_DOWN', 'PgDn')],
    [{ gap: 3 }], [{ gap: 1 }, K('UP_ARROW', '↑'), { gap: 1 }],
    [K('LEFT_ARROW', '←'), K('DOWN_ARROW', '↓'), K('RIGHT_ARROW', '→')]
  ];
  var PAD = [
    [{ gap: 4 }],
    [K('NUMLOCK', 'Num'), K('NUMPAD_SLASH', '/'), K('NUMPAD_ASTERIX', '*'), K('NUMPAD_MINUS', '−')],
    [K('NUMPAD_7', '7'), K('NUMPAD_8', '8'), K('NUMPAD_9', '9'), K('NUMPAD_PLUS', '+')],
    [K('NUMPAD_4', '4'), K('NUMPAD_5', '5'), K('NUMPAD_6', '6'), { gap: 1 }],
    [K('NUMPAD_1', '1'), K('NUMPAD_2', '2'), K('NUMPAD_3', '3'), K('NUMPAD_ENTER', 'Enter')],
    [K('NUMPAD_0', '0', 2), K('NUMPAD_PERIOD', '.'), { gap: 1 }]
  ];
  var MOUSE = [['LEFTMOUSE', 'Left button'], ['MIDDLEMOUSE', 'Middle button'], ['RIGHTMOUSE', 'Right button'], ['WHEELUPMOUSE', 'Wheel up'], ['WHEELDOWNMOUSE', 'Wheel down'],
    ['BUTTON4MOUSE', 'Button 4 (back)'], ['BUTTON5MOUSE', 'Button 5 (forward)'], ['WHEELINMOUSE', 'Wheel in'], ['WHEELOUTMOUSE', 'Wheel out'], ['TRACKPADPAN', 'Trackpad pan'], ['TRACKPADZOOM', 'Trackpad zoom'], ['MOUSEROTATE', 'Trackpad rotate'], ['ERASER', 'Pen eraser']];
  var HIDE = /^(TIMER|TIMER_REPORT|TIMERREGION|TIMER0|TIMER1|TEXTINPUT|MOUSEMOVE|NDOF_|ACTIONZONE_|MEDIA_)/;
  var NAMES = {};
  [MAIN, NAV, PAD].forEach(function (rows) { rows.forEach(function (r) { r.forEach(function (k) { if (k.c) NAMES[k.c] = k.l; }); }); });
  MOUSE.forEach(function (m) { NAMES[m[0]] = m[1]; });
  var LONG = {}; Object.keys(NAMES).forEach(function (c) { LONG[c] = /^NUMPAD_/.test(c) ? 'Numpad ' + NAMES[c] : NAMES[c]; });
  LONG.OSKEY = 'OS key'; LONG.APP = 'Menu key';
  var MODK = { LEFT_SHIFT: 's', RIGHT_SHIFT: 's', LEFT_CTRL: 'c', RIGHT_CTRL: 'c', LEFT_ALT: 'a', RIGHT_ALT: 'a', OSKEY: 'o' };
  var VAL = { PRESS: '', CLICK: 'click', DOUBLE_CLICK: 'double-click', CLICK_DRAG: 'drag', RELEASE: 'release', ANY: '' };

  /* kinds, for the colours */
  var KINDS = [['view', 'View', '#5cb4f0'], ['select', 'Select', '#f2994a'], ['transform', 'Transform', '#8fd16a'], ['menu', 'Menu', '#c08cf2'], ['mode', 'Mode and tools', '#e8b84a'], ['edit', 'Edit and add', '#e86f5c'], ['other', 'Other', '#9a9a9a']];
  function kindOf(i) {
    var o = i.op || '';
    if (/^wm\.(call_menu|call_panel|context_menu_enum|context_pie_enum)/.test(o)) return 'menu';
    if (/(^view3d\.(view|rotate|move|zoom|dolly|walk|fly|navigate|smoothview|localview|camera)|^view2d\.|\.view_|zoom|^image\.view|^node\.view|^screen\.(region_|area_|screen_full|back_to))/.test(o)) return 'view';
    if (/select|lasso|_pick/.test(o)) return 'select';
    if (/^transform\.|translate|rotate|resize|^object\.(location|rotation|scale)_clear/.test(o)) return 'transform';
    if (/mode_set|tool_set|^paint\.|brush|^object\.mode|^sculpt\.(mask|face_set)/.test(o)) return 'mode';
    if (/add|delete|duplicate|extrude|join|separate|knife|loopcut|bevel|inset|subdivide|merge|split|fill|bridge|copy|paste|cut|insert|keyframe/.test(o)) return 'edit';
    return 'other';
  }
  var KC = {}; KINDS.forEach(function (k) { KC[k[0]] = k[2]; });

  var CSS = [
    '.kmx{--k-card:var(--_bfa---surface--card,#404040);--k-panel:var(--_bfa---surface--panel,#363636);--k-well:var(--_bfa---surface--well,#262626);--k-text:var(--_bfa---text--primary,#ececec);--k-mute:#a8a8a8;--k-sel:var(--_bfa---accent--selected,#4f7fc0);margin:1.5rem 0 2.5rem;color:var(--k-text);font-family:var(--_bfa---type--text,Inter,sans-serif);container-type:inline-size}',
    'html.theme-light .kmx{--k-card:#fff;--k-panel:#f2f2f2;--k-well:#e6e6e6;--k-text:#222;--k-mute:#666}',
    '.kmx-src{display:none!important}',
    '.kmx *{box-sizing:border-box}',
    '.kmx-bar{display:flex;flex-wrap:wrap;gap:.625rem 1rem;align-items:center;margin:0 0 .75rem}',
    '.kmx-bar label{display:flex;flex-direction:column;gap:.25rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--k-mute)}',
    '.kmx select,.kmx input[type=search]{min-height:2.25rem;padding:.25rem .625rem;border:2px solid var(--_bfa---edge--outline,#0008);border-radius:.3rem;background:var(--k-card);color:var(--k-text);font:500 .9375rem Inter,sans-serif;text-transform:none;letter-spacing:0}',
    '.kmx input[type=search]{min-width:14rem}',
    '.kmx-seg{display:flex;gap:3px}',
    '.kmx .kmx-seg .ui-segment-item{cursor:pointer;font-family:inherit}',
    '.kmx-mods{display:flex;flex-wrap:wrap;gap:.375rem;align-items:center;margin:0 0 .75rem}',
    '.kmx-mods>small{font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--k-mute);margin-right:.25rem}',
    '.kmx-mod{min-width:4.5rem;justify-content:center;cursor:pointer;font-family:inherit}',
    '.kmx-mod.is-on{background:var(--k-sel)!important;color:#fff!important}',
    '.kmx-combos{display:flex;flex-wrap:wrap;gap:.375rem;margin-left:auto}',
    '.kmx .kmx-combos .ui-chip{cursor:pointer;font-family:inherit}',
    '.kmx-sink{padding:1rem;border-radius:1.25rem;background:var(--k-well);box-shadow:inset 0 14px 18px -8px #000000bf}',
    '.kmx-row{display:flex;flex-direction:column;gap:1rem}',
    /* keyboard */
    '.kmx-kb{display:flex;gap:1.25%;--u:calc((100% - 2.5%) / 22.5)}',
    '.kmx-blk{display:flex;flex-direction:column;gap:.3em}',
    '.kmx-main{flex:15 1 0}.kmx-nav{flex:3 1 0}.kmx-pad{flex:4 1 0}',
    '.kmx-r{display:flex;gap:.3em;min-height:4.4em}',
    '.kmx-k{position:relative;flex:var(--w,1) 1 0;min-width:0;display:flex;flex-direction:column;justify-content:space-between;padding:.25em .3em;border-radius:.3em;border:0;background:#4c4c4c;color:#f0f0f0;box-shadow:inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a,0 3px 4px #0006;font:inherit;text-align:left;cursor:pointer;overflow:hidden}',
    '.kmx-k.is-gap{visibility:hidden;cursor:default}',
    '.kmx-k b{font:700 .78em/1 Inter,sans-serif;opacity:.85;white-space:nowrap}',
    '.kmx-k span{font:600 .76em/1.12 Inter,sans-serif;color:#fff;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;overflow-wrap:anywhere}',
    '.kmx-k.is-set{background:color-mix(in srgb,var(--c) 34%,#3a3a3a);box-shadow:inset 0 0 0 1.5px var(--c),inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a,0 3px 4px #0006}',
    '.kmx-k.is-free{opacity:.55}',
    '.kmx-k.is-modk{background:#5a5a5a}',
    '.kmx-k.is-modk.is-on{background:var(--k-sel)}',
    '.kmx-k em{position:absolute;right:.25em;top:.2em;font:700 .6em Inter,sans-serif;font-style:normal;color:#fff;opacity:.75}',
    '.kmx-k.is-hit{outline:2px solid #fff;outline-offset:1px;z-index:1}',
    '.kmx-k.is-pick{outline:2px solid var(--c,#fff);outline-offset:2px;z-index:2}',
    '.kmx-k:hover{filter:brightness(1.15)}',
    '.kmx-kbwrap{font-size:clamp(9px,1.12cqw,15px)}',
    /* mouse */
    '.kmx-mouse{display:grid;grid-template-columns:repeat(auto-fill,minmax(10.5rem,1fr));gap:.375rem;margin-top:.875rem}',
    '.kmx-mouse .kmx-k{min-height:3.1rem;font-size:13px}',
    '.kmx-mouse .kmx-k b{font-size:.75rem}',
    /* side: detail card and legend */
    '.kmx-side{display:grid;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));gap:.75rem;align-items:start}',
    '.kmx-card{padding:1rem 1.125rem;border-radius:.625rem;background:var(--k-card);box-shadow:inset .6px 1px 0 #ffffff0f,0 1px 2px #000b}',
    '.kmx-card small{display:block;margin:0 0 .375rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#5cb4f0}',
    '.kmx-card h4{margin:0 0 .5rem!important;font:700 1.25rem/1.2 Inter,sans-serif!important;color:var(--k-text)}',
    '.kmx-card p{margin:0 0 .5rem!important;color:var(--k-mute);font-size:.875rem;line-height:1.5}',
    '.kmx-b{padding:.5rem 0;border-top:1px solid #ffffff12}',
    '.kmx-b:first-of-type{border-top:0}',
    '.kmx-b b{display:block;font-size:.9375rem;color:var(--k-text)}',
    '.kmx-b i{display:inline-block;width:.6rem;height:.6rem;margin-right:.375rem;border-radius:2px;background:var(--c)}',
    '.kmx-b span{display:block;font-size:.75rem;color:var(--k-mute);margin-top:.125rem}',
    '.kmx-b code{font-size:.75rem;opacity:.85}',
    '.kmx-kc{display:inline-flex;gap:3px;flex-wrap:wrap}',
    '.kmx-kc kbd{display:inline-grid;place-items:center;min-width:1.6rem;height:1.5rem;padding:0 .35rem;border-radius:.25rem;background:#4c4c4c;border:1px solid #0009;box-shadow:inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a;color:#f0f0f0;font:700 .7rem Inter,sans-serif}',
    '.kmx-legend{display:flex;flex-wrap:wrap;gap:.375rem .75rem;font-size:.75rem;color:var(--k-mute)}',
    '.kmx-legend span::before{content:"";display:inline-block;width:.6rem;height:.6rem;margin-right:.3rem;border-radius:2px;background:var(--c)}',
    '.kmx-res{display:flex;flex-direction:column;gap:1px;max-height:16rem;overflow:auto}',
    '.kmx-res button{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:.5rem;align-items:center;padding:.375rem .5rem;border:0;border-radius:.3rem;background:none;color:inherit;text-align:left;font:inherit;cursor:pointer}',
    '.kmx-res button:hover{background:#ffffff10}',
    '.kmx-res b{font-size:.875rem;font-weight:600}',
    '.kmx-res small{grid-column:1/-1;margin:0!important;color:var(--k-mute)!important;text-transform:none!important;letter-spacing:0!important;font:400 .75rem Inter,sans-serif!important}',
    '.kmx-note{margin:.75rem 0 0!important;font-size:.75rem;color:var(--k-mute)}',
    /* phones: a list instead of the keyboard */
    '.kmx-list{display:none}',
    '@container (max-width:40rem){.kmx-kbwrap,.kmx-mouse{display:none}.kmx-list{display:flex;flex-direction:column;gap:.75rem}}',
    '.kmx-list h5{margin:0 0 .25rem!important;font:700 .75rem Inter,sans-serif!important;letter-spacing:.08em;text-transform:uppercase;color:var(--k-mute)}',
    '.kmx-list button{display:flex;gap:.625rem;align-items:center;width:100%;padding:.5rem .25rem;border:0;border-bottom:1px solid #ffffff10;background:none;color:inherit;font:inherit;text-align:left;cursor:pointer}',
    '.kmx-list button i{flex:none;width:.6rem;height:.6rem;border-radius:2px;background:var(--c)}',
    '.kmx-list button span{flex:1;min-width:0;font-size:.875rem}',
    '@media (max-width:767px){.kmx input[type=search]{min-width:0;width:100%}.kmx-bar>label{flex:1 1 9rem}.kmx-combos{margin-left:0}}'
  ].join('\n');

  function q(s, r) { return (r || d).querySelector(s); }
  function qa(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function esc(s) { var e = d.createElement('i'); e.textContent = s == null ? '' : String(s); return e.innerHTML; }
  function el(t, c, h) { var e = d.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; }

  var MODS = [['s', 'Shift'], ['c', 'Ctrl'], ['a', 'Alt'], ['o', 'Cmd']];
  function modsOf(i) { return MODS.filter(function (m) { return i[m[0]]; }).map(function (m) { return m[0]; }).join(''); }
  function kbd(i, mac) {
    var parts = MODS.filter(function (m) { return i[m[0]]; }).map(function (m) { return mac && m[0] === 'o' ? '⌘' : m[1]; });
    if (i.km) parts.push(NAMES[i.km] || i.km);
    parts.push(LONG[i.key] || i.key.replace(/_/g, ' ').toLowerCase());
    var v = VAL[i.v]; return '<span class="kmx-kc">' + parts.map(function (p) { return '<kbd>' + esc(p) + '</kbd>'; }).join('') + (v ? ' <small style="display:inline">' + esc(v) + '</small>' : '') + '</span>';
  }

  /* ---------------------------------------------------------------- explorer */
  function explorer(block, data) {
    var li = q('li[data-k=keymap]', block) || {}; var ds = li.dataset || {};
    var root = el('div', 'kmx'); root.tabIndex = -1;
    var S = { v: 'pc', ed: ds.editor || '3D Viewport', mode: ds.mode || 'Object Mode', glob: true, mods: '', pick: null, find: '' };
    var bar = el('div', 'kmx-bar'), mods = el('div', 'kmx-mods'), sink = el('div', 'kmx-sink'), row = el('div', 'kmx-row');
    var main = el('div', 'kmx-main-col'), side = el('aside', 'kmx-side');
    var kbwrap = el('div', 'kmx-kbwrap'), mouse = el('div', 'kmx-mouse'), list = el('div', 'kmx-list');
    var card = el('div', 'kmx-card'), res = el('div', 'kmx-card'), leg = el('div', 'kmx-card');
    main.appendChild(kbwrap); main.appendChild(mouse); main.appendChild(list);
    side.appendChild(card); side.appendChild(res); side.appendChild(leg);
    row.appendChild(main); row.appendChild(side); sink.appendChild(row);
    root.appendChild(bar); root.appendChild(mods); root.appendChild(sink);
    root.insertAdjacentHTML('beforeend', '<p class="kmx-note">Keymap ' + esc(data.version || '') + ', built from the Bforartists source with the default preferences (left-click select). Active-tool and gizmo keys are left out. Spot something off? Report it with the key and the editor.</p>');
    block.classList.add('kmx-src'); block.parentNode.insertBefore(root, block);

    function kms() { return data.variants[S.v] || []; }
    var editors = [];
    kms().forEach(function (k) { if (k.ctx.kind === 'keys' && editors.indexOf(k.ctx.editor) < 0 && k.ctx.editor !== 'Everywhere') editors.push(k.ctx.editor); });
    editors.sort(function (a, b) { return a === '3D Viewport' ? -1 : b === '3D Viewport' ? 1 : a < b ? -1 : 1; });
    function modesOf(ed) {
      var o = []; kms().forEach(function (k) { if (k.ctx.kind === 'keys' && k.ctx.editor === ed && o.indexOf(k.ctx.mode) < 0) o.push(k.ctx.mode); });
      var order = ['Object Mode', 'All modes', 'General'];
      return o.sort(function (a, b) { var ia = order.indexOf(a), ib = order.indexOf(b); return (ia < 0 ? 9 : ia) - (ib < 0 ? 9 : ib) || (a < b ? -1 : 1); });
    }
    /* the keymaps in play: this mode, the editor's shared keymaps (All modes / General), and the window */
    function active() {
      return kms().filter(function (k) {
        var c = k.ctx; if (c.kind !== 'keys') return false;
        if (c.editor === S.ed) return c.mode === S.mode || c.mode === 'All modes' || c.mode === 'General' || (S.mode.indexOf('Grease Pencil') === 0 && c.mode === 'Grease Pencil · All modes');
        return S.glob && c.editor === 'Everywhere';
      });
    }
    function rows() {   /* every binding in play, the mode's own first (it wins when two share a key) */
      var out = [];
      active().sort(function (a, b) { var r = function (k) { return k.ctx.editor !== S.ed ? 3 : k.ctx.mode === S.mode ? 0 : 1; }; return r(a) - r(b); })
        .forEach(function (k) { k.items.forEach(function (i) { if (!i.off && !HIDE.test(i.key)) out.push({ i: i, km: k }); }); });
      return out;
    }
    function drawBar() {
      bar.innerHTML = '<div class="kmx-seg ui-segment" role="tablist" aria-label="Keymap">' + [['pc', 'Windows / Linux'], ['mac', 'macOS']].map(function (v) { return '<button type="button" class="ui-segment-item is-tag' + (S.v === v[0] ? ' is-active' : '') + '" data-v="' + v[0] + '">' + v[1] + '</button>'; }).join('') + '</div>' +
        '<label>Editor<select data-ed>' + editors.map(function (e) { return '<option' + (e === S.ed ? ' selected' : '') + '>' + esc(e) + '</option>'; }).join('') + '</select></label>' +
        '<label>Mode<select data-mode>' + modesOf(S.ed).map(function (m) { return '<option' + (m === S.mode ? ' selected' : '') + '>' + esc(m) + '</option>'; }).join('') + '</select></label>' +
        '<label>Find an action or key<input type="search" data-find placeholder="Extrude, loop cut, Ctrl R…" value="' + esc(S.find) + '"></label>';
    }
    function counts(all) {
      var c = {}; all.forEach(function (r) { var m = modsOf(r.i); c[m] = (c[m] || 0) + 1; }); return c;
    }
    function drawMods(all) {
      var c = counts(all), mac = S.v === 'mac';
      var names = function (m) { return m ? MODS.filter(function (x) { return m.indexOf(x[0]) > -1; }).map(function (x) { return mac && x[0] === 'o' ? '⌘ Cmd' : x[1]; }).join(' + ') : 'No modifier'; };
      var combos = Object.keys(c).sort(function (a, b) { return a.length - b.length || c[b] - c[a]; });
      mods.innerHTML = '<small>Hold</small>' + MODS.filter(function (m) { return m[0] !== 'o' || mac || c.o; }).map(function (m) { return '<button type="button" class="ui-btn is-small kmx-mod' + (S.mods.indexOf(m[0]) > -1 ? ' is-on' : '') + '" data-m="' + m[0] + '" aria-pressed="' + (S.mods.indexOf(m[0]) > -1) + '">' + (mac && m[0] === 'o' ? '⌘ Cmd' : m[1]) + '</button>'; }).join('') +
        '<span class="kmx-combos" aria-label="Combinations with keys here">' + combos.map(function (m) { return '<button type="button" class="ui-chip' + (m === S.mods ? ' is-active' : '') + '" data-combo="' + m + '">' + esc(names(m)) + ' · ' + c[m] + '</button>'; }).join('') + '</span>';
    }
    function keyMap(all) {   /* key → bindings for the modifiers held now ("any" bindings count too) */
      var m = {}; all.forEach(function (r) { var i = r.i; if (!(i.any || modsOf(i) === S.mods)) return; (m[i.key] = m[i.key] || []).push(r); }); return m;
    }
    function keyEl(k, map) {
      if (k.gap) return '<span class="kmx-k is-gap" style="--w:' + k.gap + '"></span>';
      var b = map[k.c] || [], first = b[0], mk = MODK[k.c];
      var on = mk && S.mods.indexOf(mk) > -1;
      var cls = 'kmx-k' + (first ? ' is-set' : (mk ? ' is-modk' : ' is-free')) + (on ? ' is-on' : '') + (S.pick === k.c ? ' is-pick' : '');
      var c = first ? KC[kindOf(first.i)] : '';
      var lab = first ? first.i.l + (VAL[first.i.v] ? ' (' + VAL[first.i.v] + ')' : '') : '';
      return '<button type="button" class="' + cls + '" data-key="' + k.c + '" style="--w:' + k.w + (c ? ';--c:' + c : '') + '" title="' + esc(k.l + (lab ? ': ' + lab : '')) + '"><b>' + esc(k.l) + '</b>' + (lab ? '<span>' + esc(first.i.l) + '</span>' : '') + (b.length > 1 ? '<em>+' + (b.length - 1) + '</em>' : '') + '</button>';
    }
    function blk(rowsDef, map, cls) {
      return '<div class="kmx-blk ' + cls + '">' + rowsDef.map(function (r) { return '<div class="kmx-r">' + r.map(function (k) { return keyEl(k, map); }).join('') + '</div>'; }).join('') + '</div>';
    }
    function draw() {
      var all = rows(), map = keyMap(all);
      drawMods(all);
      kbwrap.innerHTML = '<div class="kmx-kb">' + blk(MAIN, map, 'kmx-main') + blk(NAV, map, 'kmx-nav') + blk(PAD, map, 'kmx-pad') + '</div>';
      mouse.innerHTML = MOUSE.filter(function (m) { return map[m[0]] || /^(LEFT|MIDDLE|RIGHT|WHEELUP|WHEELDOWN)/.test(m[0]); }).map(function (m) { return keyEl({ c: m[0], l: m[1], w: 1 }, map); }).join('');
      /* phones: grouped list for the held modifiers */
      var ks = Object.keys(map).sort(function (a, b) { return (NAMES[a] || a) < (NAMES[b] || b) ? -1 : 1; });
      list.innerHTML = '<h5>' + (S.mods ? 'With ' + MODS.filter(function (x) { return S.mods.indexOf(x[0]) > -1; }).map(function (x) { return x[1]; }).join(' + ') : 'No modifier') + ' · ' + ks.length + ' keys</h5>' +
        ks.map(function (k) { var r = map[k][0]; return '<button type="button" data-key="' + k + '" style="--c:' + KC[kindOf(r.i)] + '"><i></i><span>' + esc(r.i.l) + (map[k].length > 1 ? ' <small>+' + (map[k].length - 1) + '</small>' : '') + '</span>' + kbd(r.i, S.v === 'mac') + '</button>'; }).join('');
      drawCard(all, map); drawFind(all);
      leg.innerHTML = '<small>Colours</small><div class="kmx-legend">' + KINDS.map(function (k) { return '<span style="--c:' + k[2] + '">' + k[1] + '</span>'; }).join('') + '</div>';
    }
    function drawCard(all, map) {
      var k = S.pick;
      if (!k) { card.innerHTML = '<small>' + esc(S.ed) + ' · ' + esc(S.mode) + '</small><h4>Pick a key</h4><p>Point at or tap a key to see everything it does here. Hold Shift, Ctrl or Alt (on screen or on your keyboard) to see those combinations.</p>'; return; }
      var here = all.filter(function (r) { return r.i.key === k; });
      var now = (map[k] || []), other = here.filter(function (r) { return now.indexOf(r) < 0; });
      var line = function (r) { return '<div class="kmx-b" style="--c:' + KC[kindOf(r.i)] + '"><b><i></i>' + esc(r.i.l) + '</b>' + kbd(r.i, S.v === 'mac') + '<span>' + esc(r.km.name) + ' · <code>' + esc(r.i.op) + '</code>' + (r.i.p ? ' · ' + esc(r.i.p.map(function (p) { return p[0] + ' ' + p[1]; }).join(', ')) : '') + '</span></div>'; };
      card.innerHTML = '<small>' + esc(LONG[k] || k) + '</small><h4>' + (now.length ? esc(now[0].i.l) : 'Free here') + '</h4>' +
        (now.length ? now.map(line).join('') : '<p>Nothing on this key with these modifiers, in ' + esc(S.ed) + ' · ' + esc(S.mode) + '. Free for your own shortcut.</p>') +
        (other.length ? '<p style="margin-top:.75rem!important">With other modifiers:</p>' + other.slice(0, 12).map(line).join('') : '') +
        (now.length ? '<p style="margin-top:.5rem!important"><a class="ui-btn dk-btn is-small" href="/search?query=' + encodeURIComponent(now[0].i.l.split(':')[0]) + '"><span class="ui-btn-icon"><img class="ui-icon" alt="" src="' + CDN + IC.zoom + '"></span><span class="ui-btn-label">Find it in the manual</span></a></p>' : '');
    }
    function drawFind(all) {
      var t = S.find.trim().toLowerCase(); qa('.kmx-k.is-hit', root).forEach(function (k) { k.classList.remove('is-hit'); });
      if (!t) { res.innerHTML = '<small>Find</small><p>Type an action (“extrude”) to light up its key, or a key (“ctrl r”).</p>'; return; }
      var words = t.split(/\s+/), mac = S.v === 'mac';
      var hits = all.filter(function (r) {
        var hay = (r.i.l + ' ' + r.i.op + ' ' + MODS.filter(function (m) { return r.i[m[0]]; }).map(function (m) { return m[1]; }).join(' ') + ' ' + (NAMES[r.i.key] || r.i.key)).toLowerCase();
        return words.every(function (w) { return hay.indexOf(w) > -1; });
      }).slice(0, 40);
      res.innerHTML = '<small>Find · ' + hits.length + (hits.length === 40 ? '+' : '') + '</small><div class="kmx-res">' + hits.map(function (r, n) { return '<button type="button" data-hit="' + n + '"><b>' + esc(r.i.l) + '</b>' + kbd(r.i, mac) + '<small>' + esc(r.km.ctx.mode) + ' · ' + esc(r.km.name) + '</small></button>'; }).join('') + '</div>';
      res._hits = hits;
      hits.forEach(function (r) { if (modsOf(r.i) === S.mods) { var e = q('.kmx-k[data-key="' + r.i.key + '"]', kbwrap); if (e) e.classList.add('is-hit'); } });
    }
    function setMods(m) { S.mods = MODS.map(function (x) { return x[0]; }).filter(function (x) { return m.indexOf(x) > -1; }).join(''); draw(); }

    root.addEventListener('click', function (e) {
      var t;
      if ((t = e.target.closest('[data-v]'))) { S.v = t.dataset.v; drawBar(); draw(); return; }
      if ((t = e.target.closest('[data-m]'))) { var m = t.dataset.m; setMods(S.mods.indexOf(m) > -1 ? S.mods.replace(m, '') : S.mods + m); return; }
      if ((t = e.target.closest('[data-combo]'))) { setMods(t.dataset.combo); return; }
      if ((t = e.target.closest('[data-hit]'))) { var r = res._hits[+t.dataset.hit]; S.pick = r.i.key; setMods(modsOf(r.i)); return; }
      if ((t = e.target.closest('[data-key]'))) { var k = t.dataset.key; if (MODK[k]) { setMods(S.mods.indexOf(MODK[k]) > -1 ? S.mods.replace(MODK[k], '') : S.mods + MODK[k]); return; } S.pick = k; draw(); }
    });
    root.addEventListener('mouseover', function (e) { var t = e.target.closest('.kmx-k[data-key]'); if (!t || MODK[t.dataset.key] || S.pick === t.dataset.key) return; S.pick = t.dataset.key; var all = rows(); drawCard(all, keyMap(all)); qa('.kmx-k.is-pick', root).forEach(function (k) { k.classList.remove('is-pick'); }); t.classList.add('is-pick'); });
    root.addEventListener('change', function (e) {
      if (e.target.matches('[data-ed]')) { S.ed = e.target.value; var ms = modesOf(S.ed); S.mode = ms[0] || ''; S.pick = null; drawBar(); draw(); }
      if (e.target.matches('[data-mode]')) { S.mode = e.target.value; S.pick = null; draw(); }
    });
    root.addEventListener('input', function (e) { if (e.target.matches('[data-find]')) { S.find = e.target.value; drawFind(rows()); } });
    /* your real keyboard: hold modifiers to relabel, press a key to pick it (while the pointer is over the explorer) */
    var over = false; root.addEventListener('mouseenter', function () { over = true; }); root.addEventListener('mouseleave', function () { over = false; });
    function live(e) {
      if (!over || (e.target && e.target.matches && e.target.matches('input,select,textarea'))) return;
      var m = (e.shiftKey ? 's' : '') + (e.ctrlKey ? 'c' : '') + (e.altKey ? 'a' : '') + (e.metaKey ? 'o' : '');
      if (m !== S.mods) setMods(m);
      if (e.type === 'keydown' && !/^(Shift|Control|Alt|Meta)$/.test(e.key)) {
        var code = codeOf(e); if (code) { e.preventDefault(); S.pick = code; draw(); }
      }
    }
    d.addEventListener('keydown', live); d.addEventListener('keyup', live);
    drawBar(); draw();
  }
  function codeOf(e) {
    var c = e.code || '';
    var m = /^Key([A-Z])$/.exec(c); if (m) return m[1];
    m = /^Digit(\d)$/.exec(c); if (m) return ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'][+m[1]];
    m = /^Numpad(\d)$/.exec(c); if (m) return 'NUMPAD_' + m[1];
    m = /^F(\d+)$/.exec(c); if (m) return c;
    return { Escape: 'ESC', Tab: 'TAB', Space: 'SPACE', Enter: 'RET', Backspace: 'BACK_SPACE', Delete: 'DEL', Insert: 'INSERT', Home: 'HOME', End: 'END', PageUp: 'PAGE_UP', PageDown: 'PAGE_DOWN',
      ArrowLeft: 'LEFT_ARROW', ArrowRight: 'RIGHT_ARROW', ArrowUp: 'UP_ARROW', ArrowDown: 'DOWN_ARROW', Minus: 'MINUS', Equal: 'EQUAL', BracketLeft: 'LEFT_BRACKET', BracketRight: 'RIGHT_BRACKET',
      Semicolon: 'SEMI_COLON', Quote: 'QUOTE', Backquote: 'ACCENT_GRAVE', Comma: 'COMMA', Period: 'PERIOD', Slash: 'SLASH', Backslash: 'BACK_SLASH', NumpadDivide: 'NUMPAD_SLASH',
      NumpadMultiply: 'NUMPAD_ASTERIX', NumpadSubtract: 'NUMPAD_MINUS', NumpadAdd: 'NUMPAD_PLUS', NumpadEnter: 'NUMPAD_ENTER', NumpadDecimal: 'NUMPAD_PERIOD', ContextMenu: 'APP' }[c] || '';
  }

  function start() {
    var blocks = qa('.ui-keymap'); if (!blocks.length) return;
    if (!d.getElementById('bfa-km-css')) { var st = el('style'); st.id = 'bfa-km-css'; st.textContent = CSS; d.head.appendChild(st); }
    blocks.forEach(function (b) {
      var li = q('li[data-k=keymap]', b); var src = li && li.dataset.src; if (!src) return;
      fetch(src, { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (data) { try { explorer(b, data); } catch (e) { if (window.console) console.warn('keymap', e); } })
        .catch(function (e) { if (window.console) console.warn('keymap data', e); });
    });
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { setTimeout(start, 0); }); else setTimeout(start, 0);
})();
