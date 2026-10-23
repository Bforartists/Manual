(function(){var d=document,R=d.documentElement,q=function(s,r){return(r||d).querySelector(s)},qa=function(s,r){return[].slice.call((r||d).querySelectorAll(s))};
var CDN='https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/',IC={doc:'68b9b72e6ab175721a9bf7cb_documents.svg',caret:'68b9bbb397785a50ab1c6b64_tria_down.svg',back:'68b9b6dd5029e853d2e4ef85_back.svg',fwd:'68b9b76aa841ed4158a2f249_forward.svg',time:'68b9bb9cc5062fa217606ff2_time.svg',light:'68b9b7c5219bda8870e7cee9_light.svg',text:'68b9bb992ec361f6e58cd575_text.svg',comm:'68b9b70677b5a3b5b8606647_community.svg',zoom:'68b9bbd23fb07538f848b579_viewzoom.svg',x:'68b9b6f02b79e1972f80e83b_cancel.svg',world:'68b9b4b69f8eb147bccde6cf_world.svg'};
function img(k,c){return'<img src="'+CDN+IC[k]+'" alt=""'+(c?' class="'+c+'"':'')+'>'}
function esc(s){var e=d.createElement('i');e.textContent=s||'';return e.innerHTML}
function el(tag,cls,html){var e=d.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e}
var small=matchMedia('(max-width:991px)');
function go(){var art=q('.ui-doc-article');if(!art)return;
var nav=q('.ui-nav');function navH(){if(nav)R.style.setProperty('--dk-nav-h',Math.round(nav.getBoundingClientRect().height)+'px')}navH();addEventListener('resize',navH);
var title=((q('.ui-doc-head h1')||{}).textContent||d.title).trim();
/* 1 sidebar: links, order, sections, sub-chapters */
var side=q('.ui-doc-side'),box=q('.ui-doc-pages'),list=q('.ui-doc-pages .w-dyn-items'),links=qa('.ui-doc-pages a.ui-panel-link');
links.forEach(function(a){if(a.dataset.slug)a.setAttribute('href','/docs/'+a.dataset.slug)});
links.sort(function(a,b){return(+a.dataset.sorder||0)-(+b.dataset.sorder||0)||(a.dataset.section<b.dataset.section?-1:a.dataset.section>b.dataset.section?1:0)||(+a.dataset.order||0)-(+b.dataset.order||0)});
var here=location.pathname.replace(/\/$/,''),cur=-1,sname=((q('.ui-doc-crumb-section')||{}).textContent||'').trim();
links.forEach(function(a,i){if(a.getAttribute('href').replace(/\/$/,'')===here)cur=i});
if(cur<0)links.forEach(function(a,i){if(cur<0&&a.textContent.trim()===title&&(!sname||a.dataset.stitle===sname))cur=i});
if(cur>-1){links[cur].classList.add('is-current');links[cur].setAttribute('aria-current','page')}
var par={};links.forEach(function(a){if(a.dataset.parent)par[a.dataset.parent]=1});links.forEach(function(a){if(par[a.dataset.pid])a.classList.add('is-parent')});
var curSec=cur>-1?links[cur].dataset.section:(links[0]&&links[0].dataset.section),groups={},gord=[];
links.forEach(function(a){var s=a.dataset.section||'';if(!groups[s]){groups[s]=[];gord.push(s)}groups[s].push(a)});
var panel=box&&box.closest('.ui-panel'),before=true;
gord.forEach(function(s){if(s===curSec){before=false;if(list)groups[s].forEach(function(a){list.appendChild(a.closest('.w-dyn-item')||a)});return}
if(!panel)return;var g=groups[s],si=q('.ui-doc-sicon',g[0]),p=el('div','ui-panel ui-doc-sect');
p.innerHTML='<div class="ui-panel-head" data-panel-toggle role="button" tabindex="0">'+img('caret','ui-panel-caret is-collapsed')+'<img class="ui-icon" alt="" src="'+(si&&si.getAttribute('src')||CDN+IC.doc)+'"><div class="ui-panel-title">'+esc(g[0].dataset.stitle||s)+'</div></div><div class="ui-panel-body ui-doc-pages is-collapsed"></div>';
g.forEach(function(a){var w=a.closest('.w-dyn-item');p.lastChild.appendChild(a);if(w&&w!==a)w.remove()});
panel.parentNode.insertBefore(p,before?panel:panel.nextSibling);if(!before)panel=p});
/* 2 breadcrumb: section crumb links to the first page of the section */
var sc=q('.ui-doc-crumb-section'),first=groups[curSec]&&groups[curSec][0];
if(sc&&first){var l=el('a',sc.className);l.href=first.getAttribute('href');l.textContent=sc.textContent;sc.replaceWith(l)}
/* 3 doc footer card */
var sEl=q('.ui-doc-source'),src=art.getAttribute('data-doc-source')||(sEl&&sEl.textContent.trim()),
CMS='https://app.pagescms.org/Bforartists/Manual/'+encodeURIComponent('docs2/tier1-getting-started')+'/collection/',edit=src?CMS+(/^docs2\/snippets\//.test(src)?'snippets':'docs')+'/edit/'+encodeURIComponent(src):CMS+'docs',
eEl=q('[data-doc-edited]'),eT=eEl&&eEl.textContent.trim(),pg=q('[data-doc-pager]');
function half(a,cls,lab,dir){if(!a)return'<div class="ui-doc-foot-half '+cls+' is-empty"></div>';var pi=q('img:not(.ui-doc-sicon)',a);
return'<div class="ui-doc-foot-half '+cls+'"><div class="ui-doc-foot-label">'+img('doc')+lab+'</div><a class="ui-doc-foot-go" href="'+a.getAttribute('href')+'">'+(dir<0?'<i class="ui-doc-tri is-l"></i>':'')+(pi?'<img alt="" src="'+pi.getAttribute('src')+'">':'')+'<span>'+esc(a.textContent.trim())+'</span>'+(dir>0?'<i class="ui-doc-tri"></i>':'')+'</a></div>'}
if(pg)pg.innerHTML='<div class="ui-doc-foot"><div class="ui-doc-foot-row">'+half(cur>0&&links[cur-1],'is-prev','Previous Chapter',-1)+half(cur>-1&&links[cur+1],'is-next','Next Chapter',1)+'</div><div class="ui-doc-foot-meta"><span>'+(eT&&eT!=='date'?img('time')+'Last edited: '+esc(eT):'')+'</span><span class="ui-doc-foot-btns"><a href="https://discord.gg/yKuR77v">'+img('comm')+'Ask on Discord</a><a data-doc-edit href="'+edit+'" target="_blank" rel="noopener" title="Opens the page in Pages CMS (sign in with GitHub)">'+img('text')+'Edit this page</a><a href="https://github.com/Bforartists/Manual/issues/new?title='+encodeURIComponent('Docs: '+title)+'">'+img('light')+'Suggest an Improvement</a></span></div></div>';
/* 4 headings and the lists that point at them */
var hs=qa('.ui-doc-body h1,.ui-doc-body h2,.ui-doc-body h3,.ui-doc-body h4,.ui-doc-body h5,.ui-doc-body h6'),map={},own={},subs=[],allA=[];
hs.forEach(function(h,i){if(!h.id)h.id=(h.textContent.toLowerCase().replace(/[^\w\s-]/g,'').trim().replace(/\s+/g,'-').slice(0,60)||'s')+'-'+i});
var ow=null;hs.forEach(function(h){if(h.tagName==='H1'){ow=h;subs.push(h)}own[h.id]=ow});
var multi=subs.length>0;
function hIco(h){var n=h&&h.getAttribute('data-icon');return n?(/^https?:/.test(n)?n:CDN+n):''}
function icoImg(h,cls){var u=hIco(h);return u?'<img class="'+(cls||'ui-icon')+' is-color" alt="" src="'+u+'">':''}
subs.forEach(function(h){var u=hIco(h);if(u)h.style.setProperty('--ico','url("'+u+'")')});
/* sticky sub-chapter strip: each H1 and its content become a section; the strip sticks under the path bar until the section ends */
var strips=[],subTop=0;subs.forEach(function(h){var n=h.nextSibling,sec=el('section','ui-doc-subsec'),st=el('div','ui-doc-substick',(icoImg(h)||img('doc','ui-icon'))+'<b>'+esc(h.textContent)+'</b><em></em>');
h.parentNode.insertBefore(sec,h);st.setAttribute('aria-hidden','true');st.addEventListener('click',function(){h.scrollIntoView({behavior:R.classList.contains('motion-reduced')?'auto':'smooth'})});
sec.appendChild(st);sec.appendChild(h);while(n&&n.tagName!=='H1'){var nx=n.nextSibling;sec.appendChild(n);n=nx}st._h=h;strips.push(st)});
/* v5.7 chapter cards: every sub-chapter is a card; text before the first sub-chapter (or a page without sub-chapters) gets one too */
(function(){var bd=q('.ui-doc-body');if(!bd)return;var f=bd.firstChild;if(!f||f.nodeType===1&&f.classList.contains('ui-doc-subsec'))return;var c=el('section','ui-doc-subsec '+(multi?'is-intro':'is-solo'));bd.insertBefore(c,f);while(c.nextSibling&&!(c.nextSibling.nodeType===1&&c.nextSibling.classList.contains('ui-doc-subsec')))c.appendChild(c.nextSibling);if(!c.textContent.trim()&&!q('img,iframe,figure',c))bd.removeChild(c)})();
function setTop(){var b=q('.ui-doc-bar'),nb=nav?nav.getBoundingClientRect().height:0;subTop=Math.round(nb+(b&&getComputedStyle(b).position==='sticky'?b.offsetHeight:0));R.style.setProperty('--dk-sub-top',subTop+'px')}
function stick(){if(!strips.length)return;strips.forEach(function(st){var hb=st._h.getBoundingClientRect(),sb=st.parentNode.getBoundingClientRect();st.classList.toggle('is-stuck',hb.bottom<subTop+4&&sb.bottom>subTop+48)})}
function lk(h,cls){var a=el('a',cls||'is-'+h.tagName.toLowerCase());a.href='#'+h.id;a.textContent=h.textContent;if(!cls&&h.tagName==='H1'&&hIco(h)){a.classList.add('has-icon');a.insertAdjacentHTML('afterbegin',icoImg(h))}(map[h.id]=map[h.id]||[]).push(a);allA.push(a);return a}
function fill(box){if(multi)box.classList.add('is-multi');hs.forEach(function(h){box.appendChild(lk(h))})}
/* groups: one per sub-chapter (H1) on multi-chapter pages, one per H2 otherwise */
function hGroups(gt){var G=[],g=null;hs.forEach(function(h){if(h.tagName.toLowerCase()===gt){g={h:h,k:[]};G.push(g)}else{if(!g){g={h:null,k:[]};G.push(g)}g.k.push(h)}});return G}
function openG(p,on){p.classList.toggle('is-open',on);var b=q(':scope>.ui-panel-body',p),c=q('.ui-panel-caret',p);if(b)b.classList.toggle('is-collapsed',!on);if(c)c.classList.toggle('is-collapsed',!on)}
function mkGroup(g,cls){var p=el('div','ui-panel '+cls),hd=el('div','ui-panel-head'),bd=el('div','ui-panel-body ui-doc-outline-list'),t=g.h?lk(g.h,'ui-panel-title'):el('a','ui-panel-title');
if(!g.h){t.href='#';t.textContent=multi?'Introduction':title}
hd.innerHTML=img('caret','ui-panel-caret')+(icoImg(g.h)||img('doc','ui-icon'));hd.appendChild(t);p.appendChild(hd);
g.k.forEach(function(h){bd.appendChild(lk(h))});if(g.k.length)p.appendChild(bd);else hd.firstChild.style.visibility='hidden';
p._id=g.h?g.h.id:'';
hd.setAttribute('data-panel-toggle','');hd.setAttribute('role','button');hd.tabIndex=0;
hd.addEventListener('click',function(e){if(!e.target.closest('a'))return;e.stopPropagation();if(!g.h){e.preventDefault();scrollTo({top:0,behavior:'smooth'})}openG(p,true);if(p.closest('.ui-doc-sheet'))closeSheet()});
hd.addEventListener('keydown',function(e){if(e.target!==hd||(e.key!=='Enter'&&e.key!==' '))return;e.preventDefault();var b=q(':scope>.ui-panel-body',p);openG(p,!!(b&&b.classList.contains('is-collapsed')))});return p}
/* left sidebar: sub-chapter links under the current page */
if(multi&&cur>-1){var hostI=links[cur].closest('.w-dyn-item')||links[cur],sl=el('div','ui-doc-subs');sl.setAttribute('aria-label','Sub-chapters');
subs.forEach(function(h){var a=lk(h,'ui-doc-sublink');a.innerHTML=icoImg(h)+'<span>'+esc(h.textContent)+'</span>';if(hIco(h))a.classList.add('has-icon');sl.appendChild(a)});hostI.parentNode.insertBefore(sl,hostI.nextSibling);links[cur].classList.add('is-parent')}
/* right side: one panel per sub-chapter, or the single Page Section list */
var ol=q('[data-doc-outline]'),subP=[],aside=q('.ui-doc-outline');
if(ol){var op=ol.closest('.ui-panel');if(!hs.length){if(op)op.style.display='none'}
else if(multi&&op){op.style.display='none';var sLab=el('div','ui-doc-subp-label',img('doc')+'<span>Sub-Chapters</span><b>'+subs.length+'</b>');op.parentNode.insertBefore(sLab,op);var at=op;
hGroups('h1').forEach(function(g){var p=mkGroup(g,'ui-doc-subp');openG(p,false);at.parentNode.insertBefore(p,at.nextSibling);at=p;subP.push(p)})}
else fill(ol)}
/* breadcrumb: current sub-chapter */
var cw=null,ca=null;if(multi){var ch=q('.ui-doc-crumb-here');if(ch){cw=el('span','ui-doc-crumb-subw','<span class="ui-doc-crumb-sep">▶</span>'+img('doc','ui-icon is-16'));ca=el('a','ui-doc-crumb-link ui-doc-crumb-sub');ca.href='#';cw.appendChild(ca);cw.hidden=true;ch.parentNode.insertBefore(cw,ch.nextSibling)}}
/* 5 bar: row 1 = crumbs + search/tools; quick buttons go to the site header (small screens, when they fit) or to row 2 */
var bar=q('.ui-doc-bar-in'),mid=matchMedia('(max-width:1279px)'),navBar=q('.ui-nav-bar'),navRight=navBar&&(q('.ui-nav-actions',navBar)||q('.ui-nav-burger',navBar)),
secIco=(q('[data-panel-id="doc-section"] .ui-panel-head img.ui-icon')||q('.ui-doc-side .ui-panel-head img.ui-icon')||{}).src||CDN+IC.doc,row2=null,quick=null,now=null,btnPs=null,btnCh=null,menu=null;
if(bar){var L=el('div','ui-doc-bar-l'),Rt=el('div','ui-doc-bar-r'),tools=q('.ui-doc-tools',bar);
qa(':scope>*',bar).forEach(function(c){if(c!==tools)L.appendChild(c)});
if(tools)Rt.appendChild(tools);
row2=el('div','ui-doc-bar-row2');bar.appendChild(L);bar.appendChild(Rt);bar.appendChild(row2);
quick=el('div','ui-doc-quick');
btnCh=el('button','ui-doc-btn ui-doc-q-ch','<img alt="" src="'+secIco+'"><span>Chapters</span>'+img('caret','is-caret'));btnCh.type='button';btnCh.setAttribute('aria-label','Chapters');btnCh.setAttribute('aria-haspopup','dialog');
now=el('div','ui-doc-now','<button type="button" class="ui-doc-btn ui-doc-q-ps" aria-expanded="false" aria-haspopup="true" aria-label="Page Sections">'+img('doc')+'<span>Page Sections</span><em></em>'+img('caret','is-caret')+'</button><div class="ui-doc-now-menu ui-doc-outline-list"></div>');
btnPs=now.firstChild;menu=now.lastChild;fill(menu);if(!hs.length)now.hidden=true;quick.classList.toggle('is-solo',!hs.length);
quick.appendChild(btnCh);quick.appendChild(now);row2.appendChild(quick)}
function fits(){var r=quick.getBoundingClientRect(),br=q('.ui-nav-brand',navBar),b=br&&br.getBoundingClientRect(),a=navRight&&navRight.getBoundingClientRect();var n=navBar.getBoundingClientRect(),k=q('.ui-nav-burger',navBar),kb=k&&k.getBoundingClientRect();return(!b||r.left>=b.right+8)&&(!a||(r.right<=a.left-8&&a.right<=n.right+1))&&(!kb||!kb.width||kb.right<=n.right+1)&&r.height<=48}
function layout(){if(!quick)return;R.classList.remove('dk-quick-head','dk-quick-row','dk-quick-noem','dk-quick-compact');
/* v5.8.4: the quick buttons always sit in the row under the breadcrumbs (never in the site header), so every page looks the same */
row2.appendChild(quick);if(mid.matches)R.classList.add('dk-quick-row')}
/* 6 two full-screen sheets: Chapters and Page Sections */
function mkSheet(name,ico){var s=el('div','ui-doc-sheet','<div class="ui-doc-sheet-head"><img alt="" src="'+ico+'"><b>'+name+'</b><em>'+esc(title)+'</em><button type="button" class="ui-doc-btn ui-doc-sheet-x" aria-label="Close">'+img('x')+'</button></div><div class="ui-doc-sheet-body"></div>');
s.setAttribute('role','dialog');s.setAttribute('aria-label',name);d.body.appendChild(s);q('.ui-doc-sheet-x',s).addEventListener('click',closeSheet);
s.lastChild.addEventListener('click',function(e){if(e.target.closest('a[href]'))closeSheet()});return s}
var shCh=mkSheet('Chapters',secIco),shPs=mkSheet('Page Sections',CDN+IC.doc),openSh=null;shPs.classList.add('is-ps');
var psG=hGroups(multi?'h1':'h2').map(function(g){var p=mkGroup(g,'ui-doc-ps');openG(p,!multi);shPs.lastChild.appendChild(p);return p});
if(multi){var pc=q('.ui-doc-sheet-head>em',shPs);if(pc)pc.textContent=title+' · '+subs.length+' sub-chapters'}
var home=side&&side.parentNode,anchor=side&&side.nextSibling;
function place(){if(side){if(small.matches){if(side.parentNode!==shCh.lastChild)shCh.lastChild.appendChild(side)}else{closeSheet();if(side.parentNode!==home)home.insertBefore(side,anchor)}}layout()}
function openSheet(s){closeSheet();openSh=s;if(s===shPs&&hs.length)spy();s.classList.add('is-open');R.classList.add('is-doc-sheet');var b=s===shCh?btnCh:btnPs;if(b)b.setAttribute('aria-expanded','true');var a=q('.is-active',s)||q('.is-current',s);if(a)a.scrollIntoView({block:'center'})}
function closeSheet(){if(!openSh)return;openSh.classList.remove('is-open');openSh=null;R.classList.remove('is-doc-sheet');[btnCh,btnPs].forEach(function(b){if(b)b.setAttribute('aria-expanded','false')})}
place();[small,mid].forEach(function(m){m.addEventListener?m.addEventListener('change',place):m.addListener(place)});
if(strips.length){setTop();addEventListener('load',setTop);addEventListener('resize',function(){setTimeout(function(){setTop();stick()},180)})}
var rz=0;addEventListener('resize',function(){clearTimeout(rz);rz=setTimeout(place,120)});addEventListener('load',layout);var lg=navBar&&q('.ui-nav-brand',navBar);if(lg){qa('img',lg).forEach(function(i){if(!i.complete)i.addEventListener('load',layout)});if('ResizeObserver'in window)new ResizeObserver(function(){clearTimeout(rz);rz=setTimeout(layout,60)}).observe(lg)}
function tog(on){if(!now)return;now.classList.toggle('is-open',on);btnPs.setAttribute('aria-expanded',on)}
if(now){btnPs.addEventListener('click',function(e){e.stopPropagation();if(small.matches)return openSheet(shPs);tog(!now.classList.contains('is-open'))});
btnCh.addEventListener('click',function(){openSheet(shCh)});
menu.addEventListener('click',function(){tog(false)});d.addEventListener('click',function(e){if(!now.contains(e.target))tog(false)})}
/* 7 search: real input, instant results, site search */
var srch=q('.ui-search'),field=srch&&q('.ui-search-field',srch),inp=null,res=null,sel=-1,hits=[];
if(field){var lab=qa('span',field).filter(function(s){return!s.classList.contains('ui-doc-key')})[0];
inp=el('input','ui-search-input');inp.type='search';inp.placeholder='Search the documentation';inp.setAttribute('aria-label','Search the documentation');inp.autocomplete='off';
if(lab)lab.replaceWith(inp);else field.appendChild(inp);field.addEventListener('click',function(){inp.focus()});
res=el('div','ui-doc-results');res.setAttribute('role','listbox');srch.appendChild(res);
var pages=links.map(function(a){var i=q('img:not(.ui-doc-sicon)',a);return{t:a.textContent.trim(),h:a.getAttribute('href'),i:i&&i.getAttribute('src'),s:a.dataset.stitle||''}});
var mk=function(t,qq){var i=t.toLowerCase().indexOf(qq);return i<0?esc(t):esc(t.slice(0,i))+'<mark>'+esc(t.slice(i,i+qq.length))+'</mark>'+esc(t.slice(i+qq.length))};
function run(){var v=inp.value.trim(),qq=v.toLowerCase();sel=-1;if(!qq){res.classList.remove('is-open');res.innerHTML='';return}
var P=pages.filter(function(p){return p.t.toLowerCase().indexOf(qq)>-1}).sort(function(a,b){return(b.t.toLowerCase().indexOf(qq)===0)-(a.t.toLowerCase().indexOf(qq)===0)}).slice(0,8),
H=hs.filter(function(h){return h.textContent.toLowerCase().indexOf(qq)>-1}).slice(0,6),o='';
if(P.length){o+='<p>Pages</p>';P.forEach(function(p){o+='<a role="option" href="'+p.h+'">'+(p.i?'<img alt="" src="'+p.i+'">':img('doc'))+'<span>'+mk(p.t,qq)+'</span><small>'+esc(p.s)+'</small></a>'})}
if(H.length){o+='<p>On this page</p>';H.forEach(function(h){var s=own[h.id];o+='<a role="option" href="#'+h.id+'">'+(icoImg(h,'x')||img('doc'))+'<span>'+mk(h.textContent,qq)+'</span>'+(s&&s!==h?'<small>'+esc(s.textContent)+'</small>':'')+'</a>'})}
o+='<p>Everywhere</p><a role="option" href="/search?query='+encodeURIComponent(v)+'">'+img('world')+'<span>Search the whole site for “'+esc(v)+'”</span></a>';
res.innerHTML=o;res.classList.add('is-open');hits=qa('a',res)}
inp.addEventListener('input',run);inp.addEventListener('focus',run);
inp.addEventListener('keydown',function(e){if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();if(!hits.length)return;sel=(sel+(e.key==='ArrowDown'?1:-1)+hits.length)%hits.length;hits.forEach(function(a,i){a.classList.toggle('is-sel',i===sel)});hits[sel].scrollIntoView({block:'nearest'})}
else if(e.key==='Enter'){e.preventDefault();var a=hits[sel>-1?sel:0];if(a){closeSheet();location.href=a.getAttribute('href')}}
else if(e.key==='Escape'){if(inp.value){inp.value='';run()}else inp.blur()}});
res.addEventListener('click',function(){res.classList.remove('is-open')});
d.addEventListener('click',function(e){if(res&&!srch.contains(e.target)&&!(e.target.closest&&e.target.closest('.ui-doc-search-btn')))res.classList.remove('is-open')})}
function openSearch(){if(!inp)return;if(small.matches)openSheet(shCh);else{var r=srch.getBoundingClientRect();if(r.top<0||r.bottom>innerHeight)srch.scrollIntoView({block:'nearest'})}setTimeout(function(){inp.focus()},30)}
/* 8 reading position */
var curSub=null;
function subChange(sid){subP.concat(psG).forEach(function(p){var on=p._id===sid;p.classList.toggle('is-current',on);if(on)openG(p,true)});
if(cw){var s=sid&&d.getElementById(sid);cw.hidden=!s;if(s){ca.textContent=s.textContent;ca.href='#'+sid;var ci=q('img',cw),u=hIco(s);ci.src=u||CDN+IC.doc;ci.classList.toggle('is-color',!!u)}}
var p=subP.filter(function(x){return x._id===sid})[0];if(p&&aside&&aside.scrollHeight>aside.clientHeight+4){var top=p.offsetTop-((sLab&&sLab.offsetHeight)||0)-8;aside.scrollTo({top:Math.max(0,top),behavior:R.classList.contains('motion-reduced')?'auto':'smooth'})}}
var mark=function(id){allA.forEach(function(a){a.classList.remove('is-active','is-in')});(map[id]||[]).forEach(function(a){a.classList.add('is-active')});
var h=d.getElementById(id),s=own[id];if(s&&s!==h)(map[s.id]||[]).forEach(function(a){a.classList.add('is-in')});
if(btnPs&&h)q('em',btnPs).textContent=(s&&s!==h?s.textContent+' › ':'')+h.textContent;
strips.forEach(function(st){q('em',st).textContent=st._h===s&&h!==s?h.textContent:''});
var sid=s?s.id:'';if(multi&&sid!==curSub){curSub=sid;subChange(sid)}};
var last=null,tick=0;function spy(){tick=0;stick();var top=strips.length&&subTop?subTop+56:(R.style.getPropertyValue('--dk-nav-h')?parseInt(R.style.getPropertyValue('--dk-nav-h')):70)+70,c=null;for(var i=0;i<hs.length;i++){if(hs[i].getBoundingClientRect().top<=top+10)c=hs[i];else break}c=c||hs[0];if(c&&c!==last){last=c;mark(c.id)}}
if(hs.length){addEventListener('scroll',function(){if(!tick)tick=requestAnimationFrame(spy)},{passive:true});spy();addEventListener('load',spy);addEventListener('hashchange',function(){setTimeout(spy,60)})}
/* 10 light play: per-surface shadow lean now comes from the site script BFA Shade */
/* 9 focus, keys */
var f=q('.ui-doc-bar [data-focus]');if(f)f.addEventListener('click',function(e){e.preventDefault();R.classList.toggle('is-doc-focus')});
d.addEventListener('keydown',function(e){if(e.key==='F3'){e.preventDefault();openSearch()}else if(e.key==='Escape'){closeSheet();tog(false)}});
/* 11 v6: sidebar, pager, search and landing cards from nav.json (all pages, 3 levels, icons); every sidebar group drags by its grip */
var NAVURL='https://bforartists.github.io/Manual/nav/nav.json',NK='bfa-docs-nav',OK='bfa-docs-sect-order',GRIP=CDN+'68b9b77a9c0887ba54d9d3f2_grip_v.svg',panelD=box&&box.closest('.ui-panel');
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
function iu(f){return!f?'':(/^https?:/.test(f)?f:CDN+f)}
function sKey(p){return p.dataset.sect||((q('.ui-panel-title',p)||{}).textContent||'').trim()}
function saveOrder(){ls(OK,JSON.stringify(qa('.ui-doc-side .ui-doc-sect').filter(function(p){return!p.hidden}).map(sKey)))}
function restoreOrder(){var o;try{o=JSON.parse(ls(OK)||'[]')}catch(e){o=[]}var ps=qa('.ui-doc-side .ui-doc-sect');if(!o.length||ps.length<2)return;var mk=el('i');ps[0].parentNode.insertBefore(mk,ps[0]);ps.sort(function(a,b){var ia=o.indexOf(sKey(a)),ib=o.indexOf(sKey(b));return(ia<0?999:ia)-(ib<0?999:ib)});ps.forEach(function(p){mk.parentNode.insertBefore(p,mk)});mk.remove()}
function gripEl(){var g=el('img','ui-panel-grip dk-grip');g.src=GRIP;g.alt='';g.tabIndex=0;g.setAttribute('role','button');g.setAttribute('aria-label','Move panel');return g}
if(!R.dataset.dkDrag){R.dataset.dkDrag='1';
var gOf=function(e){return e.target.closest&&e.target.closest('.ui-doc-sect .dk-grip')};
d.addEventListener('pointerdown',function(e){var g=gOf(e);if(!g)return;e.preventDefault();e.stopPropagation();var p=g.closest('.ui-doc-sect'),par=p.parentNode;p.classList.add('is-dragging');
function mv(ev){var sib=qa('.ui-doc-sect',par).filter(function(x){return x!==p&&x.parentNode===par&&!x.hidden}),b=null;for(var i=0;i<sib.length;i++){var r=sib[i].getBoundingClientRect();if(ev.clientY<r.top+r.height/2){b=sib[i];break}}if(b){if(b!==p.nextElementSibling)par.insertBefore(p,b)}else if(sib.length){var l=sib[sib.length-1];if(l.nextSibling!==p)par.insertBefore(p,l.nextSibling)}}
function up(){p.classList.remove('is-dragging');d.removeEventListener('pointermove',mv);d.removeEventListener('pointerup',up);saveOrder()}
d.addEventListener('pointermove',mv);d.addEventListener('pointerup',up)},true);
d.addEventListener('click',function(e){if(gOf(e)){e.preventDefault();e.stopPropagation()}},true);
d.addEventListener('keydown',function(e){var g=gOf(e);if(!g||(e.key!=='ArrowUp'&&e.key!=='ArrowDown'))return;e.preventDefault();e.stopPropagation();var p=g.closest('.ui-doc-sect'),par=p.parentNode,s=e.key==='ArrowUp'?p.previousElementSibling:p.nextElementSibling;while(s&&(!s.classList.contains('ui-doc-sect')||s.hidden))s=e.key==='ArrowUp'?s.previousElementSibling:s.nextElementSibling;if(!s)return;e.key==='ArrowUp'?par.insertBefore(p,s):par.insertBefore(s,p);g.focus();saveOrder()},true)}
/* without nav.json: the groups the CMS list made get the same grip as the designed one */
function gripify(){if(panelD){panelD.classList.add('ui-doc-sect');var dg=q('.ui-panel-grip',panelD);if(dg)dg.classList.add('dk-grip')}qa('.ui-doc-side .ui-doc-sect>.ui-panel-head').forEach(function(h){if(!q('.ui-panel-grip',h))h.appendChild(gripEl())});restoreOrder()}
/* landing pages: each item of a .ui-doc-cards list becomes a card */
function cards(bySlug,base){qa('.ui-doc-body .ui-doc-cards li').forEach(function(li){if(li.dataset.dk)return;var a=q('a',li);if(!a)return;li.dataset.dk='1';var h=a.getAttribute('href')||'',s=h.split('#')[0].replace(/\/$/,'').split('/').pop(),n=bySlug[s]||{},t=a.textContent.trim(),sum=li.textContent.slice(li.textContent.indexOf(t)+t.length).replace(/^\s*[—–-]\s*/,'').trim(),cnt=0;(function c(x){(x||[]).forEach(function(k){cnt++;c(k.c)})})(n.c);
var cd=el('a','ui-doc-card');cd.href=h;cd.innerHTML='<img class="ui-icon'+(n.i?' is-color':'')+'" alt="" src="'+(iu(n.i)||CDN+IC.doc)+'"><b>'+esc(t)+'</b>'+(sum?'<span>'+esc(sum)+'</span>':'')+(cnt?'<em>'+cnt+(cnt===1?' page':' pages')+'</em>':'');li.innerHTML='';li.appendChild(cd)});qa('.ui-doc-body .ui-doc-cards').forEach(function(c){c.classList.add('is-cards')})}
/* the whole sidebar from nav.json */
function build(nav){if(!nav||!nav.sections||!side||!panelD)return false;var base=nav.page_url||'/docs/',slug=here.split('/').pop(),bySlug={},flat=[],chain=[];
nav.sections.forEach(function(s){var l={t:s.t,s:s.s,i:s.i,c:s.c,land:1,_sec:s};bySlug[s.s]=l;flat.push(l);(function walk(c,par){(c||[]).forEach(function(n){n._p=par;n._sec=s;bySlug[n.s]=n;flat.push(n);walk(n.c,n)})})(s.c,null)});
var cur=bySlug[slug]||null;for(var x=cur;x&&!x.land;x=x._p)chain.unshift(x);var curS=cur?cur._sec:null;
qa('.ui-doc-side .ui-doc-sect').forEach(function(p){if(p!==panelD)p.remove()});panelD.hidden=true;var at=panelD;
function row(n,lv){var w=el('div','ui-doc-node'),open=chain.indexOf(n)>-1,a=el('a','ui-panel-link'+(n===cur?' is-current':'')+(n.c?' is-parent':'')),r=el('div','ui-doc-row');a.href=base+n.s;a.setAttribute('data-level',lv);if(n===cur)a.setAttribute('aria-current','page');a.innerHTML=(n.i?'<img class="ui-icon is-color" alt="" src="'+iu(n.i)+'">':'')+'<span>'+esc(n.t)+'</span>';
if(n.c){var t=el('button','ui-doc-tw'+(open?' is-open':'')),k=el('div','ui-doc-kids');t.type='button';t.setAttribute('aria-expanded',open?'true':'false');t.setAttribute('aria-label','Show the pages of '+n.t);t.innerHTML=img('caret');k.hidden=!open;n.c.forEach(function(c){k.appendChild(row(c,lv+1))});t.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();var o=k.hidden;k.hidden=!o;t.classList.toggle('is-open',o);t.setAttribute('aria-expanded',o?'true':'false')});r.appendChild(t);r.appendChild(a);w.appendChild(r);w.appendChild(k)}else{r.appendChild(a);w.appendChild(r)}return w}
nav.sections.forEach(function(s){var on=s===curS,p=el('div','ui-panel ui-doc-sect ui-doc-navp'+(on?' is-current-sect':''));p.dataset.sect=s.id;
p.innerHTML='<div class="ui-panel-head" data-panel-toggle role="button" tabindex="0">'+img('caret','ui-panel-caret'+(on?'':' is-collapsed'))+'<img class="ui-icon is-color" alt="" src="'+(iu(s.i)||CDN+IC.doc)+'"><a class="ui-panel-title" href="'+base+s.s+'">'+esc(s.t)+'</a></div><div class="ui-panel-body ui-doc-pages ui-doc-tree'+(on?'':' is-collapsed')+'"></div>';
p.firstChild.appendChild(gripEl());(s.c||[]).forEach(function(n){p.lastChild.appendChild(row(n,1))});if(cur&&cur.land&&cur._sec===s){var hd=q('.ui-panel-title',p);hd.classList.add('is-current');hd.setAttribute('aria-current','page')}
q('.ui-panel-title',p).addEventListener('click',function(e){e.stopPropagation()});at.parentNode.insertBefore(p,at.nextSibling);at=p});
restoreOrder();
var ca=q('.ui-doc-side a.is-current');if(ca){var sc=ca.closest('.ui-doc-side');if(sc&&sc.scrollHeight>sc.clientHeight+4){var top=ca.getBoundingClientRect().top-sc.getBoundingClientRect().top;if(top>sc.clientHeight*.6)sc.scrollTop+=top-sc.clientHeight/3}}
if(pg&&cur){var i=flat.indexOf(cur),A=function(n){if(!n)return null;var a=el('a');a.href=base+n.s;a.textContent=n.t;if(n.i){var im=el('img');im.alt='';im.src=iu(n.i);a.appendChild(im)}return a},rw=q('.ui-doc-foot-row',pg);if(rw)rw.innerHTML=half(A(flat[i-1]),'is-prev','Previous Chapter',-1)+half(A(flat[i+1]),'is-next','Next Chapter',1)}
var ti=q('.ui-doc-tile-icon');if(ti&&cur&&cur.i){ti.src=iu(cur.i);ti.classList.add('is-color')}
var cs=q('.ui-doc-crumb-section');if(cs&&curS&&cs.tagName==='A')cs.href=base+curS.s;
if(typeof pages!=='undefined'&&pages){pages.length=0;flat.forEach(function(n){pages.push({t:n.t,h:base+n.s,i:iu(n.i),s:n.land?'':n._sec.t})})}
cards(bySlug,base);R.classList.add('dk-nav');return true}
var navC=null;try{navC=JSON.parse(ls(NK)||'null')}catch(e){}
var navB=!!(navC&&build(navC));if(!navB){gripify();cards({},'/docs/')}
if(window.fetch&&window.Promise)fetch(NAVURL,{cache:'no-cache'}).then(function(r){return r.ok?r.json():null}).then(function(n){if(!n||!n.sections)return;if(navB&&navC&&navC.commit===n.commit)return;ls(NK,JSON.stringify(n));build(n)}).catch(function(){})}
d.readyState==='loading'?d.addEventListener('DOMContentLoaded',go):go()})();
