/* Bforartists website · perf-guard.js · @version 1.2.0 · BFA Perf Guard: slow machines start still (motion-reduced) and lite (perf-auto). Registered in Webflow as bfa_perf_guard, site-wide, header. */
/* Lite (perf-auto, see BFA Lite in the site head): no GPU wall, grain or glass blur, light layers scroll with their card.
   A saved Motion choice (View menu) always wins. Smooth scrolling is not part of it: it is free (the browser only animates a jump),
   so only the reader's own setting turns it off (site head 1.0.1).
   1.2 (less eager, Nov 2026): 1.1 sent fast computers to lite for good, because the first scrolls ran while the page was still loading
   pictures and fonts. Now:
   - the scroll test starts 4 s after the page has loaded, and counts 120 frames while the page moves;
   - lite only when more than 40 % of them are slower than 50 ms (under 20 fps), on two separate visits;
   - the load-time frame test waits 1.5 s after load and allows 30 % slow frames;
   - a "slow" verdict expires after 14 days, then the machine is tested again;
   - old 1.1 verdicts ("low" without a date) are dropped once, so every machine gets a fair retest.
   Still lite at once: TVs, save-data, 2G, 2 cores or less, 2 GB or less. */
(function () {
  var d = document, R = d.documentElement, L = localStorage, K = 'bfa-perf', A = 'perf-auto', C = 'motion-reduced', N = navigator,
      c = N.hardwareConcurrency || 4, m = N.deviceMemory || 4, n = N.connection || {}, k = '', DAY = 864e5,
      tv = /SMART-?TV|Tizen|Web0S|WebOS|NetCast|BRAVIA|HbbTV|Android TV|GoogleTV|AFT[A-Z]|CrKey|Roku|Opera TV|VIDAA|Viera|PhilipsTV|Hisense|PlayStation|Xbox/i.test(N.userAgent || '');
  function sv() { try { return !!(JSON.parse(L.getItem('bfa-prefs') || '{}') || {}).motion; } catch (e) { return !0; } }
  if (sv()) return;
  function get() { try { return L.getItem(K) || ''; } catch (e) { return ''; } }
  function put(v) { try { L.setItem(K, v); } catch (e) {} }
  k = get();
  /* verdicts: ok2 (passed everything), ok (passed the load test), warn:<t> (one slow scroll), low:<t> (lite, until t + 14 days) */
  if (k === 'low' || k === 'warn') { k = ''; put(''); }
  var kt = +(k.split(':')[1] || 0);
  if (k.indexOf('low:') === 0 && Date.now() - kt > 14 * DAY) { k = ''; put(''); }
  var weak = tv || n.saveData || /2g/.test(n.effectiveType || '') || c <= 2 || m <= 2, strong = !tv && c >= 8 && m >= 4;
  function set(on) { if (!sv()) { R.classList.toggle(C, !on); R.classList.toggle(A, !on); } }
  function note() { R.setAttribute('data-perf-note', ''); d.dispatchEvent(new Event('bfa-perf-note')); }
  function low() { put('low:' + Date.now()); set(!1); note(); }
  function strike() { if (get().indexOf('warn:') === 0) low(); else put('warn:' + Date.now()); }
  new MutationObserver(function () { if (R.classList.contains(A) && !R.classList.contains(C) && !sv()) R.classList.add(C); })
    .observe(R, { attributes: !0, attributeFilter: ['class'] });
  if (k.indexOf('low:') === 0 || weak) { set(!1); note(); return; }
  if (k === 'ok2') return;
  /* load test: 1.4 s of frames on an idle, visible page */
  function test(cb) {
    var t0 = performance.now(), l = t0, f = 0, s = 0;
    function st(t) {
      if (d.visibilityState != 'visible') return cb(null);
      f++; if (t - l > 40) s++; l = t;
      t - t0 < 1400 ? requestAnimationFrame(st) : cb(f >= 30 && s / f < .3);
    }
    d.visibilityState == 'visible' ? requestAnimationFrame(st) : cb(null);
  }
  /* scroll test: counts only frames while the page is moving, from 4 s after load; 120 of them decide */
  function watch() {
    var last = 0, l = 0, f = 0, s = 0, run = 0;
    function onS() { last = performance.now(); if (!run) { run = 1; l = 0; requestAnimationFrame(st); } }
    function st(t) {
      if (t - last > 150 || d.visibilityState != 'visible') { run = 0; return; }
      if (l) { f++; if (t - l > 50) s++; }
      l = t;
      if (f >= 120) {
        removeEventListener('scroll', onS);
        if (s / f > .4) strike(); else put('ok2');
        return;
      }
      requestAnimationFrame(st);
    }
    setTimeout(function () { addEventListener('scroll', onS, { passive: !0 }); }, 4000);
  }
  function later(fn) { if (d.readyState === 'complete') fn(); else addEventListener('load', fn); }
  if (k === 'ok' || k.indexOf('warn:') === 0) { later(watch); return; }
  if (!strong) set(!1);
  later(function () {
    setTimeout(function () {
      test(function (ok) {
        if (ok === null) { set(!0); watch(); return; }   /* opened in a background tab: no fair test, so motion on and the scroll test decides */
        if (!ok) { strong ? set(!0) : low(); if (strong) watch(); return; }
        if (strong) { put('ok'); watch(); }
        else {
          set(!0);
          setTimeout(function () {
            test(function (o2) {
              if (o2 === null) return;
              if (!o2) low(); else { put('ok'); watch(); }
            });
          }, 400);
        }
      });
    }, 1500);
  });
})();
