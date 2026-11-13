/* Bforartists website · news-foot.js · @version 1.0.0 · News template, page footer code. Each original <script> block is wrapped on its own, so one failing block cannot stop the next. */
try{
/* Bforartists · news post v1.2 (12 Oct 2026)
   Builds "On this post" (panel + phone bar) from the h2 headings, copies the link,
   and fills Keep reading + the post footer (Previous Post / Next Post, like the docs). */
(function () {
  // Card links: each card points at its own post. Remove this once the card link
  // is set to "Current News" in the Designer (Link settings > Collection page).
  [].forEach.call(document.querySelectorAll('a[data-slug]'), function (a) {
    var s = a.getAttribute('data-slug');
    if (s && /^\/news\/?$/.test(a.getAttribute('href') || '')) a.href = '/news/' + s;
  });
  // Sections: the side panel on desktop, the "On this post" bar on phones and tablets
  // (same pattern as the docs Page Sections button).
  var body = document.querySelector('.ui-post-body');
  var toc = document.querySelector('[data-toc]');
  var menu = document.querySelector('[data-toc-menu]');
  var now = document.querySelector('[data-now]');
  var nowBtn = document.querySelector('[data-now-btn]');
  var nowCur = document.querySelector('[data-now-cur]');
  var heads = body ? [].slice.call(body.querySelectorAll('h2')) : [];
  heads.forEach(function (h, i) {
    if (!h.id) h.id = (h.textContent || 'section').toLowerCase().trim()
      .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'section-' + i;
    [toc, menu].forEach(function (box) {
      if (!box) return;
      var a = document.createElement('a');
      a.className = 'ui-panel-link';
      a.href = '#' + h.id;
      a.textContent = h.textContent;
      box.appendChild(a);
    });
  });
  if (!heads.length) {
    if (toc) toc.closest('.ui-panel').style.display = 'none';
    var bar = document.querySelector('.ui-post-bar');
    if (bar) bar.style.display = 'none';
  }
  function setOpen(open) {
    if (!now) return;
    now.classList.toggle('is-open', open);
    if (nowBtn) nowBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (nowBtn) nowBtn.addEventListener('click', function (e) { e.preventDefault(); setOpen(!now.classList.contains('is-open')); });
  if (menu) menu.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('click', function (e) { if (now && !now.contains(e.target)) setOpen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  // The bar sticks right under the site header, whatever its height.
  var nav = document.querySelector('.ui-nav');
  function navH() { if (nav) document.documentElement.style.setProperty('--nav-h', Math.round(nav.getBoundingClientRect().height) + 'px'); }
  navH(); window.addEventListener('resize', navH);
  // Current section name next to the button.
  if (nowCur && heads.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) nowCur.textContent = '· ' + en.target.textContent; });
    }, { rootMargin: '-20% 0px -70% 0px' });
    heads.forEach(function (h) { io.observe(h); });
  }

  // Copy link: every [data-copy-link] button (header actions and the post footer).
  [].forEach.call(document.querySelectorAll('[data-copy-link]'), function (copy) {
    copy.addEventListener('click', function (e) {
      e.preventDefault();
      var label = copy.querySelector('.ui-btn-label');
      navigator.clipboard && navigator.clipboard.writeText(location.href).then(function () {
        if (label) { label.textContent = 'Link copied'; setTimeout(function () { label.textContent = 'Copy link'; }, 2000); }
      });
    });
  });

  var main = document.querySelector('main[data-slug]');
  var slug = main ? main.getAttribute('data-slug') : '';
  var items = [].slice.call(document.querySelectorAll('.ui-keep .ui-news-item'));
  var idx = -1;
  items.forEach(function (it, i) {
    var card = it.querySelector('[data-slug]');
    if (card && card.getAttribute('data-slug') === slug) idx = i;
  });
  // Post footer: same pattern as the docs chapter footer. A side with no post is
  // left empty (hidden on phones), like the first and last docs chapters.
  function fill(sel, it) {
    var btn = document.querySelector(sel);
    if (!btn) return;
    var half = btn.closest('.ui-pager-half');
    if (!it) { if (half) half.classList.add('is-empty'); return; }
    var card = it.querySelector('a');
    var title = it.querySelector('.ui-post-title');
    btn.href = card.getAttribute('href');
    var t = btn.querySelector('.ui-pager-title');
    if (t) t.textContent = title ? title.textContent : '';
  }
  if (idx > -1) { fill('[data-prev]', items[idx + 1]); fill('[data-next]', items[idx - 1]); }
  else { var row = document.querySelector('.ui-pager-row'); if (row) row.style.display = 'none'; }
  var shown = 0;
  items.forEach(function (it, i) {
    if (i === idx || shown >= 3) it.style.display = 'none'; else shown++;
  });
  if (!shown) { var k = document.querySelector('.ui-keep-slot'); if (k) k.style.display = 'none'; }
})();
}catch(e){console.error("news-foot block 1",e)}
try{
/* Interview video (news posts with "Has interview" on): a rounded YouTube thumbnail that plays in place. Same look as the Art spotlight (BFA Gallery CSS, site head). */
(function(){var d=document;d.querySelectorAll('[data-yt]').forEach(function(a){var u=a.getAttribute('href')||'',m=u.match(/(?:v=|youtu[.]be[/]|embed[/]|shorts[/]|live[/])([A-Za-z0-9_-]{11})/);if(!m){a.style.display='none';return}var id=m[1],t=(u.match(/[?&](?:t|start)=([0-9]+)/)||[])[1]||0;a.style.backgroundImage='url(https://i.ytimg.com/vi/'+id+'/hqdefault.jpg)';a.style.marginBottom='1.5rem';
a.addEventListener('click',function(e){e.preventDefault();var w=d.createElement('div');w.className='ui-spot-frame';w.style.marginBottom='1.5rem';var f=d.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0&start='+t;f.title='Interview';f.setAttribute('allow','autoplay; encrypted-media; picture-in-picture; fullscreen');f.setAttribute('allowfullscreen','');w.appendChild(f);a.replaceWith(w)})})})();
}catch(e){console.error("news-foot block 2",e)}
try{
/* BFA Post 1.0 - news post reading UX like the docs: path bar (breadcrumb + tools), category flag with its icon,
   side panels that fold from their header (disclosure triangle), focus mode. Panel folding and "Collapse all panels" use
   the site's data-panel-toggle / data-panels-collapse (BFA UI); focus mode is this page's own ([data-focus-post]). */
(function(){var d=document,R=d.documentElement,U='https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/';
var CAT={'Releases':'673e9d47ea869941b66d5bb6_import.svg','Development':'68b9bb34f63df100f2aad61f_script.svg','Artist spotlights':'68b9b6ea1bbae571f2dc7a47_brush_data.svg','Challenges':'68b9bb79488249132ae274da_solo_on.svg','Events':'68b9b70677b5a3b5b8606647_community.svg'};
function ci(k){return U+(CAT[(k||'').trim()]||'68b9bb99aad8c6bd9da0374b_tag.svg')}
function ic(src){var i=d.createElement('img');i.alt='';i.className='ui-icon is-16';i.src=src;return i}
/* category flags: the post's own tag and the Keep reading cards */
d.querySelectorAll('.ui-kind').forEach(function(k){if(k.classList.contains('bfa-flag'))return;var t=k.textContent.trim();k.classList.add('bfa-flag');k.insertBefore(ic(ci(t)),k.firstChild)});
d.querySelectorAll('.ui-cat').forEach(function(c){if(c.classList.contains('bfa-flag'))return;var l=c.querySelector('.ui-cat-label');c.classList.add('bfa-flag');c.insertBefore(ic(ci(l?l.textContent:'')),c.firstChild)});
/* path bar */
var lay=d.querySelector('.ui-side-layout'),kind=d.querySelector('.ui-kind'),h1=d.querySelector('.ui-post-cover h1');
if(lay&&!d.querySelector('.bfa-post-path')){var bar=d.createElement('div');bar.className='bfa-post-path';
var nav=d.createElement('nav');nav.className='ui-doc-crumb';nav.setAttribute('aria-label','Breadcrumb');
function sep(){var s=d.createElement('span');s.className='ui-doc-crumb-sep';s.textContent='▶';s.setAttribute('aria-hidden','true');return s}
var a1=d.createElement('a');a1.className='ui-doc-crumb-link';a1.href='/news';a1.appendChild(ic(U+'68b9bb7c0de081e439981817_speaker.svg'));var s1=d.createElement('span');s1.textContent='News';a1.appendChild(s1);nav.appendChild(a1);
var cat=kind?kind.textContent.trim():'';if(cat){nav.appendChild(sep());var a2=d.createElement('a');a2.className='ui-doc-crumb-link ui-doc-crumb-section';a2.href='/news#all-news';a2.appendChild(ic(ci(cat)));var s2=d.createElement('span');s2.textContent=cat;a2.appendChild(s2);nav.appendChild(a2)}
nav.appendChild(sep());var here=d.createElement('div');here.className='ui-doc-crumb-here';here.setAttribute('aria-current','page');here.textContent=h1?h1.textContent.trim():d.title;nav.appendChild(here);
var tools=d.createElement('div');tools.className='bfa-post-tools';
function tb(attr,label,icon){var a=d.createElement('a');a.href='#';a.className='ui-btn is-small is-square';a.setAttribute(attr,'');a.setAttribute('aria-label',label);a.title=label;a.innerHTML='<span class="ui-btn-icon"><img class="ui-icon" alt="" src="'+U+icon+'"></span>';tools.appendChild(a);return a}
tb('data-panels-collapse','Collapse all panels','68b9b6fd2ce1ac764fd24173_collapsemenu.svg');var fb=tb('data-focus-post','Focus mode','68b781e1216e0e1e52a012da_fullscreen_enter.svg');
bar.appendChild(nav);bar.appendChild(tools);lay.parentNode.insertBefore(bar,lay);
function focus(on){R.classList.toggle('bfa-post-focus',on);fb.setAttribute('aria-pressed',String(on));fb.querySelector('img').src=U+(on?'68b781e1275c5f760589fe66_fullscreen_exit.svg':'68b781e1216e0e1e52a012da_fullscreen_enter.svg');fb.title=fb.getAttribute('aria-label')+(on?' (on)':'');try{sessionStorage.setItem('bfa-post-focus',on?'1':'')}catch(e){}}
fb.addEventListener('click',function(e){e.preventDefault();focus(!R.classList.contains('bfa-post-focus'))});
var keep=false;try{keep=sessionStorage.getItem('bfa-post-focus')==='1'}catch(e){}if(keep)focus(true)}
/* side panels: fold from the header, like the docs */
d.querySelectorAll('aside .ui-panel-head').forEach(function(h){if(h.hasAttribute('data-panel-toggle'))return;h.setAttribute('data-panel-toggle','');h.setAttribute('role','button');h.tabIndex=0;
if(!h.querySelector('.ui-panel-caret')){var c=d.createElement('img');c.className='ui-panel-caret';c.alt='';c.src=U+'68b9bbb397785a50ab1c6b64_tria_down.svg';h.insertBefore(c,h.firstChild)}
h.addEventListener('keydown',function(e){if(e.key=='Enter'||e.key==' '){e.preventDefault();h.click()}})});
})();
}catch(e){console.error("news-foot block 3",e)}
