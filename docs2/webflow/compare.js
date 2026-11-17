/* Bforartists website · compare.js · @version 1.2.0 · BFA Compare: the before / after slider (Home, Features, Template, docs pages). Registered in Webflow as bfa_compare, applied site-wide. */
/* 1.2: one script for the website ([data-compare]) and the docs ([data-doc-compare]); it runs once per slider (data-ready), so the
   docs layer's own copy stands down. Intro: the slider shows the old screen (Blender) first, then the new one slides in from the right
   edge to the middle with an ease, once, when it scrolls into view. Again on a tab change. Stops as soon as someone touches it.
   No intro when the reader asked for less motion (system setting, or Motion: off in the View menu). The automatic lite mode
   (perf-auto) keeps it: it is one short clip, cheap on any device. 1.1: tabs swap the picture pair ([data-compare-tab]). */
(function () {
  var d = document, R = d.documentElement;
  function still() {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return true;
    try { if ((JSON.parse(localStorage.getItem('bfa-prefs') || '{}') || {}).motion === 'off') return true; } catch (e) {}
    return R.classList.contains('motion-reduced') && !R.classList.contains('perf-auto');
  }
  function ease(k) { return k < .5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2; }   /* ease in-out (cubic) */
  function init(c) {
    if (c.dataset.ready) return;
    var b = c.querySelector('.is-before'), h = c.querySelector('.ui-compare-handle');
    if (!b || !h) return;
    c.dataset.ready = '1';
    var p = 50, drag = 0, run = 0;
    function set(v) {
      if (v !== v) return;
      p = Math.max(0, Math.min(100, v));
      b.style.clipPath = 'inset(0 ' + (100 - p) + '% 0 0)';
      h.style.left = p + '%';
      c.setAttribute('aria-valuenow', Math.round(p));
    }
    function at(e) { var r = c.getBoundingClientRect(); if (r.width) set((e.clientX - r.left) / r.width * 100); }
    function stop() { run++; }
    function intro(ms, wait) {
      if (still()) { set(50); return; }
      var id = ++run;
      set(100);
      setTimeout(function () {
        if (id !== run) return;
        var t0 = performance.now();
        (function f(n) {
          if (id !== run) return;
          var k = Math.min(1, (n - t0) / ms);
          set(100 - 50 * ease(k));
          if (k < 1) requestAnimationFrame(f);
        })(t0);
      }, wait);
    }
    c.setAttribute('role', 'slider'); c.setAttribute('tabindex', '0');
    c.setAttribute('aria-valuemin', '0'); c.setAttribute('aria-valuemax', '100');
    c.style.cursor = 'ew-resize';
    c.addEventListener('pointerdown', function (e) { stop(); drag = 1; c.setPointerCapture(e.pointerId); at(e); });
    c.addEventListener('pointermove', function (e) { if (drag) at(e); });
    c.addEventListener('pointerup', function () { drag = 0; });
    c.addEventListener('pointercancel', function () { drag = 0; });
    c.addEventListener('keydown', function (e) {
      var m = { ArrowLeft: -2, ArrowDown: -2, ArrowRight: 2, ArrowUp: 2, Home: -100, End: 100 }[e.key];
      if (m) { stop(); set(p + m * (e.shiftKey && Math.abs(m) < 9 ? 5 : 1)); e.preventDefault(); }
    });
    /* tabs: swap the picture pair, then play the intro again (shorter) */
    var s = c.closest('section') || d, T = s.querySelectorAll('[data-compare-tab]');
    T.forEach(function (t) {
      t.addEventListener('click', function (e) {
        e.preventDefault();
        T.forEach(function (x) { x.classList.remove('is-active'); x.setAttribute('aria-selected', 'false'); });
        t.classList.add('is-active'); t.setAttribute('aria-selected', 'true');
        var a = c.querySelector('.ui-compare-img:not(.is-before)');
        [[b, t.dataset.before], [a, t.dataset.after]].forEach(function (x) {
          if (x[0] && x[1]) { x[0].removeAttribute('srcset'); x[0].removeAttribute('sizes'); x[0].src = x[1]; }
        });
        intro(1200, 120);
      });
    });
    /* intro: old screen first, then the new one slides in to the middle, once, when the slider is well in view */
    if (still() || !window.IntersectionObserver) { set(50); return; }
    set(100);
    var o = new IntersectionObserver(function (en) {
      if (!en[0].isIntersecting) return;
      o.disconnect();
      intro(1800, 350);
    }, { threshold: .45 });
    o.observe(c);
  }
  function go() { d.querySelectorAll('[data-compare],[data-doc-compare]').forEach(init); }
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', go); else go();
  window.bfaCompare = { init: go };
})();
