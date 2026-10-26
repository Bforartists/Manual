/* Bforartists Docs 2.0 · interactive keymap · @version 1.1.2
 *
 * Runs on the Doc Pages template (registered Webflow script, page footer). The sync turns
 * <!-- keymap-explorer --> in a page into <div class="ui-keymap"><ul><li data-k="keymap" data-src=…>,
 * and this script draws the explorer from keymap.json (built by docs2/tools/keymap.py from the
 * Bforartists source, so it always matches the app):
 *
 *   🧭  header: the keymap (Bforartists, Blender, Industry Compatible), PC or macOS, the editor and
 *       the mode (dropdowns with the Bforartists icons), and find, with its results under the box
 *   ⌨️  a keyboard and mouse that show what each key does there, coloured by kind; pointing only
 *       highlights a key, a click or tap reads it out below
 *   ⇧   Shift, Ctrl, Alt (and Cmd) toggle on screen, or hold them on your real keyboard
 *   🎨  the colours, then everything the picked key does, full width in columns
 *   📱  phones: the same keyboard with the key names only, and the list of keys under it
 *   ⭐  data-mini="1" (Important Hotkeys): only the everyday keys light up
 *   🖼️  data-k="keys" (<!-- keymap-keys keys="W=Move; Ctrl+S=Save; MMB=Pan" -->): a small keyboard
 *       picture with just those keys lit and labelled, no data needed
 * Published as /Manual/webflow/keymap-explorer-<version>.js.
 */
(function () {
  var d = document, R = d.documentElement;
  if (R.dataset.bfaKm) return;
  R.dataset.bfaKm = '1';
  var CDN = 'https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
  var IC = { zoom: '68b9bbd23fb07538f848b579_viewzoom.svg' };
  var ICON = {   /* Bforartists icons in the Webflow asset library (docs2/tools/icons.json) */
    view3d: '68b8f4efa40047ddcec7c6ae_view3d.svg', time: '68b9bb9cc5062fa217606ff2_time.svg', action: '68b9dc77588b589049a6b151_action.svg',
    filebrowser: '68b9b758d4f2674b8485d135_filebrowser.svg', graph: '68b9b7779ed747621eb33cd9_graph.svg', image: '68b8f543763e8aff56926602_image.svg',
    info: '68b8dbecbfd9caf36c6c3800_e71a9f6d36046e247e4c66c163a17682_info.png', tracker: '68b9bba68bf7d0e70d12c0e5_tracker.svg',
    nodetree: '68b9b6366471bec877610651_nodetree.svg', nla: '68b9b8e348822d01d677f130_nla.svg', outliner: '68b9b91c9f11937550db98e5_outliner.svg',
    preferences: '68b9b9402d131603f8283ec8_preferences.svg', properties: '68b9b9450739193840158e60_properties.svg', console: '68b9b70e870da2e1d34fbd77_console.svg',
    spreadsheet: '68b9bb82688b6bd2d2b97e0b_spreadsheet.svg', text: '68b9bb992ec361f6e58cd575_text.svg', sequence: '68b9bb585b21106bf2938fb9_sequence.svg',
    window: '68b8d7589dacef091df81759_window.svg', bforartists: '68b9b6e34c7998c9fca24560_blender.svg', object_datamode: '68b9b4ad3c7014ce29269cbb_object_datamode.svg', editmode_hlt: '68b9b73a62a18132461564fb_editmode_hlt.svg',
    sculptmode_hlt: '68b9bb35378431b6f223bca7_sculptmode_hlt.svg', vpaint_hlt: '68b9bbd9f63df100f2ab0b73_vpaint_hlt.svg', wpaint_hlt: '68b9bbe2688b6bd2d2b99bfa_wpaint_hlt.svg',
    tpaint_hlt: '68b9bba3f4e9a8f95b7dc4d9_tpaint_hlt.svg', pose_hlt: '68b9b93e25eed9bb42d40618_pose_hlt.svg', particlemode: '68b9b9313a78871163fde2a6_particlemode.svg',
    greasepencil: '68b9b778f5f5795369104956_greasepencil.svg', uv: '68b8f55bf9193241eb1db35b_uv.svg', marker: '68b9b7ebe5b26d66efa3b4df_marker.svg',
    fcurve: '68b9b74b3e9d6ef3a8da3b95_fcurve.svg', mod_mask: '68b9b813125a9240040c047f_mod_mask.svg',
    outliner_ob_mesh: '68b9b924aa6d1700b8cdeada_outliner_ob_mesh.svg', outliner_ob_armature: '68b9b92254fc56ca7b47676a_outliner_ob_armature.svg',
    outliner_ob_curve: '68b9b922a071114063447b63_outliner_ob_curve.svg', outliner_ob_lattice: '68b9b924efe54e8b2bc419b8_outliner_ob_lattice.svg',
    outliner_ob_meta: '68b9b9252dc70d4223b14cf2_outliner_ob_meta.svg', outliner_ob_pointcloud: '68b9b92549d195d35961b047_outliner_ob_pointcloud.svg',
    outliner_ob_font: '68b9b9231a2000c4b5e9e976_outliner_ob_font.svg', outliner_ob_curves: '68b9b9224cc9602ee9063fe8_outliner_ob_curves.svg',
    mouse_lmb: '68b9b8d40bd269ade0cff2f0_mouse_lmb.svg', mouse_mmb: '68b9b8d55029e853d2e61f44_mouse_mmb.svg', mouse_rmb: '68b9b8d69ec0ac9428a3c2ff_mouse_rmb.svg',
    mouse_lmb_drag: '68b9b8d4fd7eb986095b7dc2_mouse_lmb_drag.svg', mouse_mmb_drag: '68b9b8d51980ac91de6b4ce2_mouse_mmb_drag.svg',
    mouse_rmb_drag: '68b9b8d90bd269ade0cff4cf_mouse_rmb_drag.svg', mouse_lmb_2x: '68b9b8d454fc56ca7b474fb1_mouse_lmb_2x.svg', mouse_move: '68b9b8d6074cbaabc69ebd93_mouse_move.svg'
  };
  var ED_IC = { '3D Viewport': 'view3d', 'Animation editors': 'time', 'Dope Sheet': 'action', 'File Browser': 'filebrowser', 'Graph Editor': 'graph', 'Image Editor': 'image',
    'Info Editor': 'info', 'Movie Clip Editor': 'tracker', 'Node Editor': 'nodetree', 'Nonlinear Animation': 'nla', 'Outliner': 'outliner', 'Preferences': 'preferences',
    'Properties Editor': 'properties', 'Python Console': 'console', 'Spreadsheet': 'spreadsheet', 'Text Editor': 'text', 'Video Sequencer': 'sequence', 'Everywhere': 'window' };
  function modeIcon(m, ed) {
    var x = { 'Object Mode': 'object_datamode', 'Pose Mode': 'pose_hlt', 'Sculpt Mode': 'sculptmode_hlt', 'Sculpt Mode · Hair Curves': 'sculptmode_hlt', 'Particle Edit': 'particlemode',
      'Texture Paint': 'tpaint_hlt', 'Paint modes': 'tpaint_hlt', 'Vertex Paint': 'vpaint_hlt', 'Weight Paint': 'wpaint_hlt', 'Vertex and Weight Paint': 'wpaint_hlt',
      'UV Editing': 'uv', 'Masks': 'mod_mask', 'Markers': 'marker', 'Channels': 'fcurve', 'Frames': 'time', 'Time scrubbing': 'time',
      'Grease Pencil · Edit': 'editmode_hlt', 'Grease Pencil · Sculpt': 'sculptmode_hlt', 'Grease Pencil · Vertex Paint': 'vpaint_hlt', 'Grease Pencil · Weight Paint': 'wpaint_hlt' }[m];
    if (x) return x;
    if (/^Grease Pencil/.test(m)) return 'greasepencil';
    var e = /^Edit Mode · (.+)$/.exec(m);
    if (e) return { Armature: 'outliner_ob_armature', Curve: 'outliner_ob_curve', 'Hair Curves': 'outliner_ob_curves', Lattice: 'outliner_ob_lattice', Mesh: 'outliner_ob_mesh',
      Metaball: 'outliner_ob_meta', 'Point Cloud': 'outliner_ob_pointcloud', Text: 'outliner_ob_font' }[e[1]] || 'editmode_hlt';
    return ED_IC[ed] || 'window';
  }
  function img(name, cls) { return ICON[name] ? '<img class="' + (cls || 'kmx-ic') + '" alt="" src="' + CDN + ICON[name] + '">' : ''; }
  var MOUSE_IC = { LEFTMOUSE: 'mouse_lmb', MIDDLEMOUSE: 'mouse_mmb', RIGHTMOUSE: 'mouse_rmb', WHEELUPMOUSE: 'mouse_mmb', WHEELDOWNMOUSE: 'mouse_mmb', WHEELINMOUSE: 'mouse_mmb', WHEELOUTMOUSE: 'mouse_mmb' };
  function mouseIcon(key, v) {
    var b = MOUSE_IC[key]; if (!b) return '';
    if (v === 'CLICK_DRAG' && ICON[b + '_drag']) return b + '_drag';
    if (v === 'DOUBLE_CLICK' && ICON[b + '_2x']) return b + '_2x';
    return b;
  }
  var PRESETS = [['bforartists', 'Bforartists', 'keymap.json'], ['blender', 'Blender', 'keymap-blender.json'], ['industry', 'Industry Compatible', 'keymap-industry.json']];
  /* everyday keys (Important Hotkeys): navigation, selection, transform, modes, files, undo, render, search */
  var IMPORTANT = /^(view3d\.(rotate|move|zoom|dolly|view_axis|view_camera|view_all|view_selected|localview|view_persportho|view_center_cursor|select|select_box|select_circle|select_lasso|cursor3d|toggle_xray|object_mode_pie_or_toggle|navigate)|view2d\.(pan|zoom|scroll_up|scroll_down|zoom_in|zoom_out)|wm\.(save_mainfile|save_as_mainfile|open_mainfile|read_homefile|search_menu|search_operator|tool_set_by_id|radial_control|batch_rename)|ed\.(undo|redo)|render\.(render|view_show|play_rendered_anim)|screen\.(redo_last|region_flip|screen_full_area|animation_play|frame_jump|repeat_last)|object\.(mode_set|delete|duplicate_move|parent_set|parent_clear|select_all|hide_view_set|hide_view_clear|join|transfer_mode)|mesh\.(select_mode|extrude_context_move|extrude_region_move|loop_select|edgering_select|shortest_path_pick|delete|duplicate_move|select_all)|armature\.(extrude_move|extrude_forked|parent_set|parent_clear|separate)|transform\.(translate|rotate|resize|trackball)|sculpt\.|paint\.(brush_select|sample_color)|brush\.scale_size|outliner\.item_rename|image\.view_)/;


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
    '.kmx{--k-card:var(--_bfa---surface--card,#404040);--k-panel:var(--_bfa---surface--panel,#363636);--k-well:var(--_bfa---surface--well,#262626);--k-text:var(--_bfa---text--primary,#ececec);--k-mute:#a8a8a8;--k-sel:var(--_bfa---accent--selected,#4f7fc0);margin:1.5rem 0 2.5rem;color:var(--k-text);font-family:var(--_bfa---type--text,Inter),Inter,sans-serif;container-type:inline-size}',
    '.kmx-src{display:none!important}',
    '.kmx *{box-sizing:border-box}',
    /* header */
    '.kmx-head{display:flex;flex-wrap:wrap;gap:.625rem 1rem;align-items:flex-end;margin:0 0 .75rem}',
    '.kmx-fld{display:flex;flex-direction:column;gap:.25rem;position:relative}',
    '.kmx-fld>span,.kmx-cap{font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--k-mute)}',
    '.kmx-segs{display:flex;flex-wrap:wrap;gap:.5rem}',
    '.kmx-seg{display:flex;gap:3px;flex-wrap:wrap;max-width:100%}',
    '.kmx .kmx-seg .ui-segment-item{white-space:nowrap;flex:0 0 auto;font-weight:600;display:inline-flex;align-items:center;gap:.375rem}',
    '.kmx .kmx-seg .ui-seg-icon{width:16px;height:16px;margin:0!important}',
    '.kmx-short{display:none}',
    '.kmx .kmx-seg .ui-segment-item{cursor:pointer;font-family:inherit}',
    '.kmx-dd{position:relative}',
    '.kmx-dd>button,.kmx-find input{display:flex;align-items:center;gap:.5rem;min-height:2.25rem;padding:.25rem .625rem;border:2px solid var(--_bfa---edge--outline,#0008);border-radius:.3rem;background:var(--k-card);color:var(--k-text);font:500 .9375rem Inter,sans-serif;text-transform:none;letter-spacing:0}',
    '.kmx-dd>button{min-width:13rem;cursor:pointer;text-align:left}',
    '.kmx-dd>button .kmx-dd-l{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}',
    '.kmx-dd>button::after{content:"";flex:none;border:5px solid transparent;border-top-color:currentColor;margin-top:5px;opacity:.7}',
    '.kmx-ic{width:18px;height:18px;flex:none;object-fit:contain}',
    '.kmx-pop{position:absolute;z-index:40;left:0;top:calc(100% + 4px);min-width:100%;max-height:22rem;overflow:auto;margin:0;padding:.25rem;list-style:none;border-radius:.45rem;background:var(--k-panel);box-shadow:0 10px 28px #000b,inset 0 0 0 1px #ffffff14}',
    '.kmx-pop[hidden]{display:none!important}',
    '.kmx .kmx-pop{overflow-x:hidden!important;overflow-y:auto!important;overscroll-behavior:contain;-webkit-overflow-scrolling:touch}',
    '.kmx-pop li{display:flex;align-items:center;gap:.5rem;margin:0;padding:.375rem .5rem;border-radius:.3rem;cursor:pointer;font:500 .875rem Inter,sans-serif;white-space:nowrap;color:var(--k-text)}',
    '.kmx-pop li::before{display:none}',
    '.kmx-pop li:hover,.kmx-pop li.is-hl{background:#ffffff14}',
    '.kmx-pop li[aria-selected=true]{background:var(--k-sel);color:#fff}',
    '.kmx-find{flex:1 1 16rem}',
    '.kmx-find input{width:100%}',
    '.kmx-find .kmx-pop{width:max(100%,24rem);white-space:normal}',
    '.kmx-find .kmx-pop li{display:grid;grid-template-columns:minmax(0,1fr) auto;white-space:normal}',
    '.kmx-find .kmx-pop li small{grid-column:1/-1;color:var(--k-mute);font-size:.75rem}',
    '.kmx-tip{flex:1 1 100%;margin:0!important;font-size:.8125rem;color:var(--k-mute)}',
    /* hold row */
    '.kmx-mods{display:flex;flex-direction:column;gap:.5rem;margin:0 0 .75rem}',
    '.kmx-hold{display:flex;flex-wrap:wrap;gap:.375rem;align-items:center}',
    '.kmx-mods>small{margin-right:.25rem}',
    '.kmx .kmx-mod{min-width:4.75rem;justify-content:center;cursor:pointer;font-family:inherit}',
    '.kmx-mod.is-on{background:var(--k-sel)!important;color:#fff!important}',
    '.kmx-combos{display:flex;flex-wrap:wrap;gap:.375rem}',
    '.kmx .kmx-combos .ui-chip{cursor:pointer;font-family:inherit}',
    '.kmx-sink{padding:1rem;border-radius:1.25rem;background:var(--k-well);box-shadow:inset 0 14px 18px -8px #000000bf}',
    /* keyboard */
    '.kmx-kb{display:flex;gap:1.25%}',
    '.kmx-blk{display:flex;flex-direction:column;gap:.3em}',
    '.kmx-main{flex:15 1 0}.kmx-nav{flex:3 1 0}.kmx-pad{flex:4 1 0}',
    '.kmx-r{display:flex;gap:.3em;min-height:3.6em}',
    '.kmx-k{position:relative;flex:var(--w,1) 1 0;min-width:0;display:flex;flex-direction:column;justify-content:space-between;padding:.25em .3em;border-radius:.3em;border:0;background:#4c4c4c;color:#f0f0f0;box-shadow:inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a,0 3px 4px #0006;font:inherit;text-align:left;cursor:pointer;overflow:hidden}',
    '.kmx-k.is-gap{visibility:hidden;cursor:default}',
    '.kmx-k b{font:700 .78em/1 Inter,sans-serif;opacity:.85;white-space:nowrap}',
    '.kmx-k span{font:600 .72em/1.1 Inter,sans-serif;color:#fff;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;overflow-wrap:anywhere}',
    '.kmx-k.is-set{background:color-mix(in srgb,var(--c) 34%,#3a3a3a);box-shadow:inset 0 0 0 1.5px var(--c),inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a,0 3px 4px #0006}',
    '.kmx-k.is-free{opacity:.55}',
    '.kmx-k.is-modk{background:#5a5a5a}',
    '.kmx-k.is-modk.is-on{background:var(--k-sel)}',
    '.kmx-k em{position:absolute;right:.25em;top:.2em;font:700 .6em Inter,sans-serif;font-style:normal;color:#fff;opacity:.75}',
    '.kmx-k.is-hit{outline:2px solid #fff;outline-offset:1px;z-index:1}',
    '.kmx-k:hover{filter:brightness(1.2);outline:2px dashed #ffffffb0;outline-offset:1px;z-index:1}',
    '.kmx-k.is-pick{outline:2px solid var(--c,#fff)!important;outline-offset:2px;z-index:2;filter:brightness(1.15)}',
    '.kmx-kbwrap{font-size:clamp(9px,1.12cqw,15px)}',
    /* mouse */
    '.kmx-mouse{display:grid;grid-template-columns:repeat(auto-fill,minmax(10.5rem,1fr));gap:.375rem;margin-top:.875rem}',
    '.kmx-mouse .kmx-k{min-height:2.9rem;font-size:13px}',
    '.kmx-mouse .kmx-k b{display:flex;align-items:center;gap:.375rem;font-size:.75rem}',
    '.kmx-mouse .kmx-k b img{width:16px;height:16px}',
    /* below: colours, then the picked key */
    '.kmx-legend{display:flex;flex-wrap:wrap;gap:.375rem 1rem;align-items:center;margin:.875rem 0 0;padding:.625rem 1rem;border-radius:.625rem;background:var(--k-card);font-size:.8125rem;color:var(--k-mute)}',
    '.kmx-legend span::before{content:"";display:inline-block;width:.65rem;height:.65rem;margin-right:.35rem;border-radius:2px;background:var(--c);vertical-align:-1px}',
    '.kmx-card{margin-top:.75rem;padding:1rem 1.125rem;border-radius:.625rem;background:var(--k-card);box-shadow:inset .6px 1px 0 #ffffff0f,0 1px 2px #000b}',
    '.kmx-card>small{display:block;margin:0 0 .375rem;font:700 .6875rem Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#5cb4f0}',
    '.kmx-card h4{margin:0 0 .5rem!important;font:700 1.25rem/1.2 Inter,sans-serif!important;color:var(--k-text)}',
    '.kmx-card p{margin:0 0 .5rem!important;color:var(--k-mute);font-size:.875rem;line-height:1.5}',
    '.kmx-cols{display:grid;grid-template-columns:repeat(auto-fill,minmax(16rem,1fr));gap:.5rem 1rem}',
    '.kmx-b{padding:.625rem .75rem;border-radius:.4rem;background:#ffffff08;box-shadow:inset 3px 0 0 var(--c)}',
    '.kmx-b b{display:block;font-size:.9375rem;color:var(--k-text);margin-bottom:.25rem}',
    '.kmx-b span{display:block;font-size:.75rem;color:var(--k-mute);margin-top:.25rem;overflow-wrap:anywhere}',
    '.kmx-b code{font-size:.75rem;opacity:.85}',
    '.kmx-sub{margin:.875rem 0 .5rem!important;font:700 .6875rem Inter,sans-serif!important;letter-spacing:.08em;text-transform:uppercase;color:var(--k-mute)!important}',
    '.kmx-kc{display:inline-flex;gap:3px;flex-wrap:wrap;align-items:center}',
    '.kmx-kc kbd{display:inline-flex;align-items:center;gap:3px;min-width:1.6rem;height:1.5rem;padding:0 .35rem;border-radius:.25rem;background:#4c4c4c;border:1px solid #0009;box-shadow:inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a;color:#f0f0f0;font:700 .7rem Inter,sans-serif;justify-content:center}',
    '.kmx-kc kbd img{width:14px;height:14px}',
    /* keys picture (keymap-keys) */
    '.kmk{margin:.75rem 0 1.25rem;padding:.75rem;border-radius:1rem;background:var(--_bfa---surface--well,#262626);box-shadow:inset 0 10px 14px -8px #000000bf;container-type:inline-size;color:#f0f0f0}',
    '.kmk .kmx-kb{gap:2%}',
    '.kmk .kmx-r{min-height:3.1em}',
    '.kmk .kmx-kbwrap{font-size:clamp(8px,1.3cqw,14px)}',
    '.kmk .kmx-k{cursor:default}',
    '.kmk .kmx-k:hover{filter:none;outline:0}',
    '.kmk .kmx-k.is-lit{background:color-mix(in srgb,#5cb4f0 34%,#3a3a3a);box-shadow:inset 0 0 0 1.5px #5cb4f0,inset 0 1px 0 #ffffff1f,0 2px 0 #1a1a1a}',
    '.kmk .kmx-k.is-mod{background:color-mix(in srgb,#e8b84a 30%,#3a3a3a);box-shadow:inset 0 0 0 1.5px #e8b84a,0 2px 0 #1a1a1a}',
    '.kmk .kmx-k.is-dim{opacity:.35}',
    '.kmk .kmx-mouse{grid-template-columns:repeat(auto-fill,minmax(9rem,1fr));margin-top:.625rem}',
    '.kmk .kmx-mouse .kmx-k{min-height:2.6rem}',
    '.kmk-list{display:flex;flex-wrap:wrap;gap:.375rem .75rem;margin:.625rem 0 0;font:500 .8125rem Inter,sans-serif;color:#cfcfcf}',
    '.kmk-list span{display:inline-flex;align-items:center;gap:.375rem}',
    '@container (max-width:44rem){.kmk .kmx-k span,.kmk .kmx-k em{display:none}.kmk .kmx-k{justify-content:center;align-items:center}.kmk .kmx-r{min-height:2.5em}.kmk .kmx-kbwrap{font-size:clamp(7px,2.4cqw,12px)}.kmk .kmx-mouse .kmx-k span{display:-webkit-box}}',
    '.kmx-note{margin:.75rem 0 0!important;font-size:.75rem;color:var(--k-mute)}',
    '.kmx-card .ui-btn .ui-icon{width:16px;height:16px}',
    '.kmx.is-loading .kmx-sink{opacity:.5;transition:opacity .2s}',
    /* phones: same keyboard, key names only; the list under it */
    '.kmx-listd{display:none;margin-top:.75rem}',
    '.kmx-listd summary{cursor:pointer;font:600 .875rem Inter,sans-serif;color:var(--k-text);padding:.375rem 0}',
    '.kmx-list{display:flex;flex-direction:column}',
    '.kmx-list button{display:flex;gap:.625rem;align-items:center;width:100%;padding:.5rem .25rem;border:0;border-bottom:1px solid #ffffff10;background:none;color:inherit;font:inherit;text-align:left;cursor:pointer}',
    '.kmx-list button i{flex:none;width:.6rem;height:.6rem;border-radius:2px;background:var(--c)}',
    '.kmx-list button span{flex:1;min-width:0;font-size:.875rem}',
    '@container (max-width:44rem){.kmx-kb{flex-wrap:wrap;gap:.6em}.kmx-main{flex:1 1 100%}.kmx-nav,.kmx-pad{flex:1 1 0}.kmx-nav .kmx-r:first-child,.kmx-pad .kmx-r:first-child{display:none}.kmx-k span,.kmx-k em{display:none}.kmx-k{justify-content:center;align-items:center;padding:.1em}.kmx-k b{font-size:.95em;max-width:100%;overflow:hidden;text-overflow:ellipsis}.kmx-r{min-height:2.7em}.kmx-kbwrap{font-size:clamp(8px,2.5cqw,13px)}.kmx-mouse{grid-template-columns:repeat(auto-fill,minmax(8.5rem,1fr))}.kmx-mouse .kmx-k span{display:-webkit-box}.kmx-mouse .kmx-k{align-items:flex-start}.kmx-listd{display:block}.kmx-dd>button{min-width:0;width:100%}.kmx-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:.625rem}.kmx-head>.kmx-fld:first-child,.kmx-head>.kmx-find,.kmx-head>.kmx-tip{grid-column:1/-1}.kmx-long{display:none}.kmx-short{display:inline}.kmx-seg{flex:1 1 100%}.kmx .kmx-seg .ui-segment-item{flex:1 1 0;justify-content:center}.kmx-pop{max-height:16rem}.kmx-sink{padding:.625rem}}'
  ].join('\n');

  function q(s, r) { return (r || d).querySelector(s); }
  function qa(s, r) { return [].slice.call((r || d).querySelectorAll(s)); }
  function esc(s) { var e = d.createElement('i'); e.textContent = s == null ? '' : String(s); return e.innerHTML; }
  function el(t, c, h) { var e = d.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; }

  var MODS = [['s', 'Shift'], ['c', 'Ctrl'], ['a', 'Alt'], ['o', 'Cmd']];
  function modsOf(i) { return MODS.filter(function (m) { return i[m[0]]; }).map(function (m) { return m[0]; }).join(''); }
  function kbd(i, mac) {
    var parts = MODS.filter(function (m) { return i[m[0]]; }).map(function (m) { return esc(mac && m[0] === 'o' ? '⌘' : m[1]); });
    if (i.km) parts.push(esc(NAMES[i.km] || i.km));
    var mi = mouseIcon(i.key, i.v);
    parts.push((mi ? img(mi) : '') + esc(LONG[i.key] || i.key.replace(/_/g, ' ').toLowerCase()));
    var v = VAL[i.v]; return '<span class="kmx-kc">' + parts.map(function (p) { return '<kbd>' + p + '</kbd>'; }).join('') + (v ? ' <small style="display:inline">' + esc(v) + '</small>' : '') + '</span>';
  }

  /* ---------------------------------------------------------------- a dropdown with icons */
  function dropdown(label, items, value, onPick) {   /* items: [[value, text, icon]] */
    var f = el('div', 'kmx-fld'), id = 'kmx' + Math.random().toString(36).slice(2, 8);
    var cur = items.filter(function (x) { return x[0] === value; })[0] || items[0] || ['', '', ''];
    f.innerHTML = '<span id="' + id + '-l">' + esc(label) + '</span><div class="kmx-dd"><button type="button" aria-haspopup="listbox" aria-expanded="false" aria-labelledby="' + id + '-l ' + id + '-b" id="' + id + '-b">' +
      img(cur[2]) + '<span class="kmx-dd-l">' + esc(cur[1]) + '</span></button><ul class="kmx-pop" role="listbox" hidden aria-labelledby="' + id + '-l">' +
      items.map(function (x) { return '<li role="option" data-val="' + esc(x[0]) + '" aria-selected="' + (x[0] === cur[0]) + '">' + img(x[2]) + '<span>' + esc(x[1]) + '</span></li>'; }).join('') + '</ul></div>';
    var btn = q('button', f), pop = q('ul', f), hl = -1;
    function opts() { return qa('li', pop); }
    function open(on) {
      closeAll(on ? pop : null); pop.hidden = !on; btn.setAttribute('aria-expanded', on);
      if (on) { hl = Math.max(0, opts().findIndex(function (o) { return o.getAttribute('aria-selected') === 'true'; })); mark(); keep(); }
    }
    function mark() { opts().forEach(function (o, n) { o.classList.toggle('is-hl', n === hl); }); }
    function keep() {   /* bring the highlighted option into view inside the list, never by scrolling the page */
      var o = opts()[hl]; if (!o) return;
      var top = o.offsetTop, bot = top + o.offsetHeight;
      if (top < pop.scrollTop) pop.scrollTop = top - 4; else if (bot > pop.scrollTop + pop.clientHeight) pop.scrollTop = bot - pop.clientHeight + 4;
    }
    btn.addEventListener('click', function () { open(pop.hidden); });
    pop.addEventListener('click', function (e) { var o = e.target.closest('li'); if (!o) return; open(false); onPick(o.dataset.val); });
    f.addEventListener('keydown', function (e) {
      var os = opts();
      if (e.key === 'Escape') { open(false); btn.focus(); return; }
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (pop.hidden) { open(true); return; } hl = (hl + (e.key === 'ArrowDown' ? 1 : -1) + os.length) % os.length; mark(); keep(); }
      if (e.key === 'Enter' && !pop.hidden && os[hl]) { e.preventDefault(); open(false); onPick(os[hl].dataset.val); }
    });
    return f;
  }
  function closeAll(except) { qa('.kmx-pop').forEach(function (p) { if (p !== except) { p.hidden = true; var b = p.parentNode.querySelector('button[aria-expanded]'); if (b) b.setAttribute('aria-expanded', 'false'); } }); }
  d.addEventListener('click', function (e) { if (!e.target.closest('.kmx-fld')) closeAll(null); });

  /* ---------------------------------------------------------------- explorer */
  function explorer(block, first, base) {
    var li = q('li[data-k=keymap]', block) || {}; var ds = li.dataset || {};
    var root = el('div', 'kmx' + (ds.mini ? ' is-mini' : '')); root.tabIndex = -1;
    var cache = { bforartists: first };
    var S = { p: 'bforartists', v: 'pc', ed: ds.editor || '3D Viewport', mode: ds.mode || 'Object Mode', glob: true, mods: '', pick: null, find: '', mini: !!ds.mini };
    var head = el('div', 'kmx-head'), mods = el('div', 'kmx-mods'), sink = el('div', 'kmx-sink');
    var kbwrap = el('div', 'kmx-kbwrap'), mouse = el('div', 'kmx-mouse');
    var leg = el('div', 'kmx-legend'), card = el('div', 'kmx-card'), listd = el('details', 'kmx-listd');
    sink.appendChild(kbwrap); sink.appendChild(mouse);
    [head, mods, sink, leg, card, listd].forEach(function (x) { root.appendChild(x); });
    var note = el('p', 'kmx-note'); root.appendChild(note);
    block.classList.add('kmx-src'); block.parentNode.insertBefore(root, block);

    function data() { return cache[S.p] || first; }
    function kms() { return data().variants[S.v] || []; }
    function editors() {
      var e = [];
      kms().forEach(function (k) { if (k.ctx.kind === 'keys' && e.indexOf(k.ctx.editor) < 0 && k.ctx.editor !== 'Everywhere') e.push(k.ctx.editor); });
      return e.sort(function (a, b) { return a === '3D Viewport' ? -1 : b === '3D Viewport' ? 1 : a < b ? -1 : 1; });
    }
    function modesOf(ed) {
      var o = []; kms().forEach(function (k) { if (k.ctx.kind === 'keys' && k.ctx.editor === ed && o.indexOf(k.ctx.mode) < 0) o.push(k.ctx.mode); });
      var order = ['Object Mode', 'All modes', 'General'];
      return o.sort(function (a, b) { var ia = order.indexOf(a), ib = order.indexOf(b); return (ia < 0 ? 9 : ia) - (ib < 0 ? 9 : ib) || (a < b ? -1 : 1); });
    }
    function fix() {   /* keep the editor and mode valid when the keymap changes */
      var es = editors(); if (es.indexOf(S.ed) < 0) S.ed = es[0] || '';
      var ms = modesOf(S.ed); if (ms.indexOf(S.mode) < 0) S.mode = ms[0] || '';
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
        .forEach(function (k) { k.items.forEach(function (i) { if (!i.off && !HIDE.test(i.key) && (!S.mini || IMPORTANT.test(i.op || ''))) out.push({ i: i, km: k }); }); });
      return out;
    }
    function drawHead() {
      head.innerHTML = '';
      var segs = el('div', 'kmx-fld');
      segs.innerHTML = '<span>Keymap</span><div class="kmx-segs"><div class="kmx-seg ui-segment" role="group" aria-label="Keymap preset">' +
        PRESETS.map(function (p) { var sh = p[0] === 'industry' ? 'Industry' : p[1]; return '<button type="button" class="ui-segment-item is-tag' + (S.p === p[0] ? ' is-active' : '') + '" data-p="' + p[0] + '" aria-pressed="' + (S.p === p[0]) + '" title="' + p[1] + '">' + (p[0] === 'bforartists' ? img('bforartists', 'ui-seg-icon kmx-ic') : '') + (sh !== p[1] ? '<span class="kmx-long">' + p[1] + '</span><span class="kmx-short">' + sh + '</span>' : p[1]) + '</button>'; }).join('') +
        '</div><div class="kmx-seg ui-segment" role="group" aria-label="Platform">' + [['pc', 'Windows / Linux'], ['mac', 'macOS']].map(function (v) { return '<button type="button" class="ui-segment-item is-tag' + (S.v === v[0] ? ' is-active' : '') + '" data-v="' + v[0] + '" aria-pressed="' + (S.v === v[0]) + '">' + v[1] + '</button>'; }).join('') + '</div></div>';
      head.appendChild(segs);
      head.appendChild(dropdown('Editor', editors().map(function (e) { return [e, e, ED_IC[e]]; }), S.ed, function (v) { S.ed = v; S.mode = modesOf(v)[0] || ''; S.pick = null; drawHead(); draw(); }));
      head.appendChild(dropdown('Mode', modesOf(S.ed).map(function (m) { return [m, m, modeIcon(m, S.ed)]; }), S.mode, function (v) { S.mode = v; S.pick = null; drawHead(); draw(); }));
      var f = el('div', 'kmx-fld kmx-find');
      f.innerHTML = '<span>Find an action or key</span><input type="search" data-find placeholder="Extrude, loop cut, Ctrl R…" value="' + esc(S.find) + '" aria-controls="kmx-res" autocomplete="off"><ul class="kmx-pop" role="listbox" hidden></ul>';
      head.appendChild(f);
      head.insertAdjacentHTML('beforeend', '<p class="kmx-tip">' + (S.mini ? 'Only the everyday keys light up. ' : '') + 'Point at a key to highlight it, click or tap to read what it does below. Hold Shift, Ctrl or Alt to see those combinations.</p>');
    }
    function counts(all) { var c = {}; all.forEach(function (r) { var m = modsOf(r.i); c[m] = (c[m] || 0) + 1; }); return c; }
    function drawMods(all) {
      var c = counts(all), mac = S.v === 'mac';
      var names = function (m) { return m ? MODS.filter(function (x) { return m.indexOf(x[0]) > -1; }).map(function (x) { return mac && x[0] === 'o' ? '⌘ Cmd' : x[1]; }).join(' + ') : 'No modifier'; };
      var combos = Object.keys(c).sort(function (a, b) { return a.length - b.length || c[b] - c[a]; });
      mods.innerHTML = '<div class="kmx-hold"><small class="kmx-cap">Hold</small>' + MODS.filter(function (m) { return m[0] !== 'o' || mac || c.o; }).map(function (m) { var on = S.mods.indexOf(m[0]) > -1; return '<button type="button" class="ui-btn dk-btn is-small kmx-mod' + (on ? ' is-accent is-on' : '') + '" data-m="' + m[0] + '" aria-pressed="' + on + '"><span class="ui-btn-label">' + (mac && m[0] === 'o' ? '⌘ Cmd' : m[1]) + '</span></button>'; }).join('') + '</div>' +
        '<span class="kmx-combos" aria-label="Combinations with keys here">' + combos.map(function (m) { return '<button type="button" class="ui-chip' + (m === S.mods ? ' is-active' : '') + '" data-combo="' + m + '">' + esc(names(m)) + ' · ' + c[m] + '</button>'; }).join('') + '</span>';
    }
    function keyMap(all) {   /* key → bindings for the modifiers held now ("any" bindings count too) */
      var m = {}; all.forEach(function (r) { var i = r.i; if (!(i.any || modsOf(i) === S.mods)) return; (m[i.key] = m[i.key] || []).push(r); }); return m;
    }
    function keyEl(k, map, icon) {
      if (k.gap) return '<span class="kmx-k is-gap" style="--w:' + k.gap + '"></span>';
      var b = map[k.c] || [], first = b[0], mk = MODK[k.c];
      var on = mk && S.mods.indexOf(mk) > -1;
      var cls = 'kmx-k' + (first ? ' is-set' : (mk ? ' is-modk' : ' is-free')) + (on ? ' is-on' : '') + (S.pick === k.c ? ' is-pick' : '');
      var c = first ? KC[kindOf(first.i)] : '';
      var lab = first ? first.i.l + (VAL[first.i.v] ? ' (' + VAL[first.i.v] + ')' : '') : '';
      return '<button type="button" class="' + cls + '" data-key="' + k.c + '" style="--w:' + k.w + (c ? ';--c:' + c : '') + '" title="' + esc(k.l + (lab ? ': ' + lab : '')) + '"><b>' + (icon ? img(icon) : '') + esc(k.l) + '</b>' + (lab ? '<span>' + esc(first.i.l) + '</span>' : '') + (b.length > 1 ? '<em>+' + (b.length - 1) + '</em>' : '') + '</button>';
    }
    function blk(rowsDef, map, cls) {
      return '<div class="kmx-blk ' + cls + '">' + rowsDef.map(function (r) { return '<div class="kmx-r">' + r.map(function (k) { return keyEl(k, map); }).join('') + '</div>'; }).join('') + '</div>';
    }
    function draw() {
      var all = rows(), map = keyMap(all);
      drawMods(all);
      kbwrap.innerHTML = '<div class="kmx-kb">' + blk(MAIN, map, 'kmx-main') + blk(NAV, map, 'kmx-nav') + blk(PAD, map, 'kmx-pad') + '</div>';
      mouse.innerHTML = MOUSE.filter(function (m) { return map[m[0]] || /^(LEFT|MIDDLE|RIGHT|WHEELUP|WHEELDOWN)/.test(m[0]); }).map(function (m) { return keyEl({ c: m[0], l: m[1], w: 1 }, map, MOUSE_IC[m[0]]); }).join('');
      leg.innerHTML = '<small class="kmx-cap">Colours</small>' + KINDS.map(function (k) { return '<span style="--c:' + k[2] + '">' + k[1] + '</span>'; }).join('');
      var ks = Object.keys(map).sort(function (a, b) { return (NAMES[a] || a) < (NAMES[b] || b) ? -1 : 1; });
      listd.innerHTML = '<summary>' + (S.mods ? 'With ' + MODS.filter(function (x) { return S.mods.indexOf(x[0]) > -1; }).map(function (x) { return x[1]; }).join(' + ') : 'No modifier') + ': all ' + ks.length + ' keys as a list</summary><div class="kmx-list">' +
        ks.map(function (k) { var r = map[k][0]; return '<button type="button" data-key="' + k + '" style="--c:' + KC[kindOf(r.i)] + '"><i></i><span>' + esc(r.i.l) + (map[k].length > 1 ? ' <small>+' + (map[k].length - 1) + '</small>' : '') + '</span>' + kbd(r.i, S.v === 'mac') + '</button>'; }).join('') + '</div>';
      drawCard(all, map); drawFind(all);
      var dd = data();
      note.innerHTML = esc(dd.name || 'Bforartists') + ' keymap ' + esc(dd.version || '') + ', built from the Bforartists source with the default preferences. Active-tool and gizmo keys are left out.' +
        (S.mini ? ' Every key: <a href="/docs/keymap-standard-keymaps">Standard Keymaps</a>.' : '') + ' Spot something off? Report it with the key and the editor.';
    }
    function drawCard(all, map) {
      var k = S.pick;
      if (!k) { card.innerHTML = '<small>' + esc(S.ed) + ' · ' + esc(S.mode) + '</small><h4>Pick a key</h4><p>Click or tap a key to see everything it does here.</p>'; return; }
      var here = all.filter(function (r) { return r.i.key === k; });
      var now = (map[k] || []), other = here.filter(function (r) { return now.indexOf(r) < 0; });
      var line = function (r) { return '<div class="kmx-b" style="--c:' + KC[kindOf(r.i)] + '"><b>' + esc(r.i.l) + '</b>' + kbd(r.i, S.v === 'mac') + '<span>' + esc(r.km.name) + ' · <code>' + esc(r.i.op) + '</code>' + (r.i.p ? ' · ' + esc(r.i.p.map(function (p) { return p[0] + ' ' + p[1]; }).join(', ')) : '') + '</span></div>'; };
      card.innerHTML = '<small>' + esc(LONG[k] || k) + ' · ' + esc(S.ed) + ' · ' + esc(S.mode) + '</small><h4>' + (now.length ? esc(now[0].i.l) : 'Free here') + '</h4>' +
        (now.length ? '<div class="kmx-cols">' + now.map(line).join('') + '</div>' : '<p>Nothing on this key with these modifiers here. Free for your own shortcut.</p>') +
        (other.length ? '<p class="kmx-sub">With other modifiers</p><div class="kmx-cols">' + other.slice(0, 18).map(line).join('') + '</div>' : '') +
        (now.length ? '<p style="margin-top:.75rem!important"><a class="ui-btn dk-btn is-small" href="/search?query=' + encodeURIComponent(now[0].i.l.split(':')[0]) + '"><span class="ui-btn-icon"><img class="ui-icon" alt="" src="' + CDN + IC.zoom + '"></span><span class="ui-btn-label">Find it in the manual</span></a></p>' : '');
    }
    function drawFind(all) {
      var t = S.find.trim().toLowerCase(), pop = q('.kmx-find .kmx-pop', head);
      qa('.kmx-k.is-hit', root).forEach(function (k) { k.classList.remove('is-hit'); });
      if (!pop) return;
      if (!t) { pop.hidden = true; pop.innerHTML = ''; return; }
      var words = t.split(/\s+/), mac = S.v === 'mac';
      var hits = all.filter(function (r) {
        var hay = (r.i.l + ' ' + r.i.op + ' ' + MODS.filter(function (m) { return r.i[m[0]]; }).map(function (m) { return m[1]; }).join(' ') + ' ' + (NAMES[r.i.key] || r.i.key)).toLowerCase();
        return words.every(function (w) { return hay.indexOf(w) > -1; });
      }).slice(0, 40);
      pop.innerHTML = hits.length ? hits.map(function (r, n) { return '<li role="option" data-hit="' + n + '"><b>' + esc(r.i.l) + '</b>' + kbd(r.i, mac) + '<small>' + esc(r.km.ctx.mode) + ' · ' + esc(r.km.name) + '</small></li>'; }).join('')
        : '<li aria-disabled="true"><span>No key for “' + esc(S.find) + '” in ' + esc(S.ed) + ' · ' + esc(S.mode) + '</span></li>';
      pop._hits = hits;
      if (d.activeElement === q('[data-find]', head)) pop.hidden = false;
      hits.forEach(function (r) { if (modsOf(r.i) === S.mods) { var e = q('.kmx-k[data-key="' + r.i.key + '"]', kbwrap); if (e) e.classList.add('is-hit'); } });
    }
    function setMods(m) { S.mods = MODS.map(function (x) { return x[0]; }).filter(function (x) { return m.indexOf(x) > -1; }).join(''); draw(); }
    function setPreset(p) {
      if (cache[p]) { S.p = p; fix(); drawHead(); draw(); return; }
      var file = PRESETS.filter(function (x) { return x[0] === p; })[0][2];
      root.classList.add('is-loading');
      fetch(base + file, { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (dd) { cache[p] = dd; S.p = p; fix(); drawHead(); draw(); })
        .catch(function (e) { if (window.console) console.warn('keymap data', e); }).then(function () { root.classList.remove('is-loading'); });
    }

    root.addEventListener('click', function (e) {
      var t;
      if ((t = e.target.closest('[data-p]'))) { setPreset(t.dataset.p); return; }
      if ((t = e.target.closest('[data-v]'))) { S.v = t.dataset.v; fix(); drawHead(); draw(); return; }
      if ((t = e.target.closest('[data-m]'))) { var m = t.dataset.m; setMods(S.mods.indexOf(m) > -1 ? S.mods.replace(m, '') : S.mods + m); return; }
      if ((t = e.target.closest('[data-combo]'))) { setMods(t.dataset.combo); return; }
      if ((t = e.target.closest('[data-hit]'))) { var pop = t.closest('.kmx-pop'), r = pop._hits[+t.dataset.hit]; pop.hidden = true; S.pick = r.i.key; setMods(modsOf(r.i)); card.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); return; }
      if ((t = e.target.closest('[data-key]'))) { var k = t.dataset.key; if (MODK[k]) { setMods(S.mods.indexOf(MODK[k]) > -1 ? S.mods.replace(MODK[k], '') : S.mods + MODK[k]); return; } S.pick = k; draw(); }
    });
    root.addEventListener('input', function (e) { if (e.target.matches('[data-find]')) { S.find = e.target.value; drawFind(rows()); } });
    root.addEventListener('focusin', function (e) { if (e.target.matches('[data-find]') && S.find) drawFind(rows()); });
    root.addEventListener('keydown', function (e) { if (e.target.matches('[data-find]') && e.key === 'Escape') { var p = q('.kmx-find .kmx-pop', head); if (p) p.hidden = true; } });
    /* your real keyboard: hold modifiers to relabel, press a key to pick it (while the pointer is over the explorer) */
    var over = false; root.addEventListener('mouseenter', function () { over = true; }); root.addEventListener('mouseleave', function () { over = false; });
    function live(e) {
      if (!over || (e.target && e.target.matches && e.target.matches('input,select,textarea,[role=listbox] *,.kmx-dd button'))) return;
      var m = (e.shiftKey ? 's' : '') + (e.ctrlKey ? 'c' : '') + (e.altKey ? 'a' : '') + (e.metaKey ? 'o' : '');
      if (m !== S.mods) setMods(m);
      if (e.type === 'keydown' && !/^(Shift|Control|Alt|Meta)$/.test(e.key)) {
        var code = codeOf(e); if (code) { e.preventDefault(); S.pick = code; draw(); }
      }
    }
    d.addEventListener('keydown', live); d.addEventListener('keyup', live);
    fix(); drawHead(); draw();
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

  /* ---------------------------------------------------------------- keys picture */
  var KEYWORD = { ESC: 'ESC', ESCAPE: 'ESC', TAB: 'TAB', SPACE: 'SPACE', ENTER: 'RET', RETURN: 'RET', DEL: 'DEL', DELETE: 'DEL', BACKSPACE: 'BACK_SPACE', HOME: 'HOME', END: 'END',
    LMB: 'LEFTMOUSE', 'LEFT CLICK': 'LEFTMOUSE', 'LEFT MOUSE': 'LEFTMOUSE', MMB: 'MIDDLEMOUSE', 'MIDDLE MOUSE': 'MIDDLEMOUSE', RMB: 'RIGHTMOUSE', 'RIGHT CLICK': 'RIGHTMOUSE', 'RIGHT MOUSE': 'RIGHTMOUSE',
    SCROLLWHEEL: 'WHEELUPMOUSE', WHEEL: 'WHEELUPMOUSE', SHIFT: 'LEFT_SHIFT', CTRL: 'LEFT_CTRL', ALT: 'LEFT_ALT', CMD: 'OSKEY',
    '`': 'ACCENT_GRAVE', '-': 'MINUS', '=': 'EQUAL', '[': 'LEFT_BRACKET', ']': 'RIGHT_BRACKET', ';': 'SEMI_COLON', ',': 'COMMA', '.': 'PERIOD', '/': 'SLASH' };
  var DIG = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE'];
  function codeOfName(n) {
    var u = n.trim().toUpperCase(), m;
    if (KEYWORD[u]) return KEYWORD[u];
    if (/^[A-Z]$/.test(u)) return u;
    if (/^\d$/.test(u)) return DIG[+u];
    if (/^F(\d|1[0-2])$/.test(u)) return u;
    if ((m = /^NUMPAD\s*(\d)$/.exec(u))) return 'NUMPAD_' + m[1];
    if ((m = /^NUMPAD\s*([*\/+.\-])$/.exec(u))) return { '*': 'NUMPAD_ASTERIX', '/': 'NUMPAD_SLASH', '+': 'NUMPAD_PLUS', '.': 'NUMPAD_PERIOD', '-': 'NUMPAD_MINUS' }[m[1]];
    return '';
  }
  function keysPicture(block, spec) {
    var lit = {}, mods = {}, items = [], pad = false, mice = false;
    spec.split(';').forEach(function (part) {
      var eq = part.indexOf('='); if (eq < 0) return;
      var combo = part.slice(0, eq).trim(), label = part.slice(eq + 1).trim();
      var toks = combo.split('+').map(function (t) { return t.trim(); }).filter(Boolean);
      var key = toks.pop(), code = codeOfName(key || ''); if (!code) return;
      toks.forEach(function (t) { var c = codeOfName(t); if (c) mods[c] = 1; });
      (lit[code] = lit[code] || []).push((toks.length ? toks.join(' + ') + ' + ' : '') + label);
      if (/^NUMPAD_/.test(code)) pad = true;
      if (/MOUSE$/.test(code)) mice = true;
      items.push([combo, label, code]);
    });
    var root = el('div', 'kmk'), row = function (r) {
      return '<div class="kmx-r">' + r.map(function (k) {
        if (k.gap) return '<span class="kmx-k is-gap" style="--w:' + k.gap + '"></span>';
        var l = lit[k.c], md = mods[k.c] || (k.c === 'RIGHT_SHIFT' && mods.LEFT_SHIFT) || (k.c === 'RIGHT_CTRL' && mods.LEFT_CTRL) || (k.c === 'RIGHT_ALT' && mods.LEFT_ALT);
        var cls = 'kmx-k' + (l ? ' is-lit' : md ? ' is-mod' : ' is-dim');
        return '<span class="' + cls + '" style="--w:' + k.w + '" title="' + esc(k.l + (l ? ': ' + l.join(' · ') : '')) + '"><b>' + esc(k.l) + '</b>' + (l ? '<span>' + esc(l[0].replace(/^.* \+ /, '')) + '</span>' + (l.length > 1 ? '<em>+' + (l.length - 1) + '</em>' : '') : '') + '</span>';
      }).join('') + '</div>';
    };
    var kb = '<div class="kmx-kb"><div class="kmx-blk kmx-main">' + MAIN.map(row).join('') + '</div>' + (pad ? '<div class="kmx-blk kmx-pad">' + PAD.map(row).join('') + '</div>' : '') + '</div>';
    var mouseRow = mice ? '<div class="kmx-mouse">' + MOUSE.slice(0, 5).filter(function (m) { return lit[m[0]] || /^(LEFT|MIDDLE|RIGHT)/.test(m[0]); }).map(function (m) {
      var l = lit[m[0]]; return '<span class="kmx-k ' + (l ? 'is-lit' : 'is-dim') + '"><b>' + img(MOUSE_IC[m[0]]) + esc(m[1]) + '</b>' + (l ? '<span>' + esc(l.join(' · ')) + '</span>' : '') + '</span>';
    }).join('') + '</div>' : '';
    root.innerHTML = '<div class="kmx-kbwrap">' + kb + '</div>' + mouseRow;
    root.setAttribute('role', 'img');
    root.setAttribute('aria-label', 'Keyboard: ' + items.map(function (x) { return x[0] + ' ' + x[1]; }).join(', '));
    block.classList.add('kmx-src'); block.parentNode.insertBefore(root, block);
  }

  function start() {
    var blocks = qa('.ui-keymap'); if (!blocks.length) return;
    if (!d.getElementById('bfa-km-css')) { var st = el('style'); st.id = 'bfa-km-css'; st.textContent = CSS; d.head.appendChild(st); }
    blocks.forEach(function (b) {
      var kli = q('li[data-k=keys]', b);
      if (kli) { try { keysPicture(b, kli.dataset.keys || ''); } catch (e) { if (window.console) console.warn('keymap keys', e); } return; }
      var li = q('li[data-k=keymap]', b); var src = li && li.dataset.src; if (!src) return;
      var base = src.replace(/[^/]*$/, '');
      fetch(src, { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (data) { try { explorer(b, data, base); } catch (e) { if (window.console) console.warn('keymap', e); } })
        .catch(function (e) { if (window.console) console.warn('keymap data', e); });
    });
  }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', function () { setTimeout(start, 0); }); else setTimeout(start, 0);
})();
