/* Bforartists website · site-foot.js · @version 1.0.0 · Site-wide footer code (Webflow Site settings, Custom code, Footer). Each original <script> block is wrapped on its own, so one failing block cannot stop the next. */
try{
/* BFA IX Idle 1.0 - Webflow's interaction engine loops every frame even with no interactions on the page (75/s on Home). No targets here: switch it off. */
addEventListener('load',function(){setTimeout(function(){try{var W=window.Webflow,ix=W&&W.require&&W.require('ix2');if(!ix||!ix.store||!ix.destroy)return;var D=document,ev=(ix.store.getState().ixData||{}).events||{},pg=D.documentElement.getAttribute('data-wf-page');
if(D.querySelector('[data-w-id]'))return;for(var k in ev){var t=ev[k].target||{};if(t.appliesTo==='PAGE'&&t.id===pg)return;if(t.appliesTo==='CLASS'&&t.selector&&D.querySelector(t.selector))return}
ix.destroy();D.documentElement.setAttribute('data-ix-idle','')}catch(e){}},0)});
}catch(e){console.error("site-foot block 1",e)}
try{
/* BFA Fallbacks 1.0 - links that only exist for visitors without JavaScript. The phone menu button points at the footer links (#site-links) in the HTML; with JavaScript the menu opens instead, so the link goes back to # (no hash added to the address). (Moved here from the registered scripts: Webflow allows 15 per block.) */
(function(){function go(){document.querySelectorAll('.ui-nav-burger[href="#site-links"]').forEach(function(a){a.setAttribute('href','#')})}if(document.readyState=='loading')document.addEventListener('DOMContentLoaded',go);else go()})();
}catch(e){console.error("site-foot block 2",e)}
try{
/* BFA Fork Light 1.1 - the end of every page always turns the mouse light, the specular and the card rims orange: the last section
   (the fork / call to action) and the footer, whatever colour they had. Uses BFA Sectors (data-light). */
(function(){var d=document,s=[].slice.call(d.querySelectorAll('.layout-section')).filter(function(e){return !e.closest('footer,#site-links,.ui-nav')});
if(!s.length)s=[].slice.call(d.querySelectorAll('main section,body>section,.layout-page>section')).filter(function(e){return !e.closest('footer,#site-links,.ui-nav')});
var f=d.getElementById('site-links')||d.querySelector('footer');[s[s.length-1],f].forEach(function(e){if(e)e.setAttribute('data-light','orange')})})();
}catch(e){console.error("site-foot block 3",e)}
try{
/* BFA Light 3.2 - the mouse light. Writes only --light-x/y and --edge-x/y on <html>, and only when they change (3.2: scrolling with a still mouse no longer
   restyles the page). Everything else (pixel position, wall drift) is shared through window.bfaLight for BFA Wall and BFA Shade, without touching CSS.
   Without WebGL the wall drift still goes to --wall-x/y/a for the CSS fallback wall. */
(function(){var b=document,F=window,t=Math,x=b.documentElement,A=x.style,v=innerWidth,c=innerHeight,u=v*.3,m=c*.25,r=-1,s=0,w=.5,f=0,T=0,d=0,E=0,y=0,P={},C=!!(F.matchMedia&&matchMedia("(hover:none)").matches),
L=F.bfaLight={off:false,px:NaN,py:NaN,x:.3,y:.2,wx:.5,wy:.1,wa:180,fns:[],on:function(fn){this.fns.push(fn)}};
function p(){return F.performance?performance.now():+new Date}
function put(k,val){if(P[k]!==val){P[k]=val;A.setProperty(k,val)}}
function drop(){for(var k in P)A.removeProperty(k);P={};['--light-px','--light-py','--wall-o'].forEach(function(k){A.removeProperty(k)})}
function tell(){for(var i=0;i<L.fns.length;i++)try{L.fns[i]()}catch(e){}}
function D(){for(var e=0,i=b.querySelectorAll(".layout-section,.ui-doc-subsec"),o=0,l;o<i.length;o++)if(l=i[o].getBoundingClientRect(),l.top>c*.25){e=l;break}u=e?e.left+e.width*.16:v*.3,m=t.min(e?e.top+56:c*.5,c*.86)}
function Y(){f=0;clearTimeout(T);var e=p(),i=t.min(6,t.max(.1,(e-(d||e-16.7))/16.7)),o,h,l,g;d=e;
 try{v=innerWidth;c=innerHeight;
  if(x.classList.contains("motion-reduced")){if(!L.off){L.off=true;drop();r=-1;tell()}return}
  L.off=false;(y>E||C&&!E)&&D();r<0&&(r=u,s=m);o=1-t.pow(.94,i);r+=(u-r)*o;s+=(m-s)*o;h=r/v;l=s/c;g=t.min(1,scrollY/t.max(1,x.scrollHeight-c));w+=(h-w)*(1-t.pow(.975,i));
  L.px=r;L.py=s+scrollY;L.x=h;L.y=l;L.wx=.25+w*.5;L.wy=.1+g*.3;L.wa=180+g*28;
  put("--light-x",(h*100).toFixed(1)+"%");put("--light-y",(l*100).toFixed(1)+"%");put("--edge-x",((.5-h)*1.6).toFixed(2));put("--edge-y",t.max(.2,(.5-l)*1.2+.6).toFixed(2));
  if(!x.classList.contains("bfa-gl")){put("--wall-x",(L.wx*100).toFixed(1)+"%");put("--wall-y",(L.wy*100).toFixed(1)+"%");put("--wall-a",L.wa.toFixed(1)+"deg")}
  tell()}catch(M){}
 t.abs(u-r)+t.abs(m-s)>.5||t.abs(h-w)>.002?n():d=0}
function n(){f||(f=requestAnimationFrame(Y),clearTimeout(T),T=setTimeout(function(){f&&(cancelAnimationFrame(f),Y())},120))}
function q(e){var i=e.sourceCapabilities;if(e.pointerType=="touch"||i&&i.firesTouchEvents||e.type=="mousemove"&&p()-y<800){y=p();return}E=p();u=e.clientX;m=e.clientY;n()}
var O={passive:!0},a=function(e,i,o){(o||F).addEventListener(e,i,O)};
a("pointermove",q);F.PointerEvent||a("mousemove",q);a("touchstart",function(){y=p()});a("scroll",n);a("resize",n);a("load",n);a("pageshow",function(){d=0,n()});a("visibilitychange",function(){d=0,n()},b);
new MutationObserver(n).observe(x,{attributes:!0,attributeFilter:["class"]});n()})();
}catch(e){console.error("site-foot block 4",e)}
try{
/* BFA Shade 2.3.1 - shadows lean away from the light (--sx). 2.3.1: runs on a timer, not a frame callback, so it also updates in background tabs. 2.3: reads the light from window.bfaLight (no CSS read) and recalculates at most ~8 times a second,
   after the light or a scrolling row moves, instead of every frame. 2.2: a scrolling row only rechecks its own cards. 2.1: only elements on screen, steps of .05. */
(function(){var d=document,R=d.documentElement,M=Math,S='.ui-card,.ui-group,.ui-sink,.depth-raised,.depth-float,.depth-low,.depth-well,.ui-focus-card,.ui-focus-kid,.ui-focus-feature,.ui-sticker-card,.ui-thumb-card,.ui-thumb-tile,.ui-wip-card,.ui-panel,.ui-pager,.ui-mega-door,.ui-mega-tile,.ui-mega-feature,.ui-nav-drop,.ui-menu-list,.ui-splash,.ui-search,.ui-doc-foot,.ui-doc-subsec,.ui-doc-callout,.ui-doc-tile,.ui-spread-frame,.ui-spread-inset,.ui-hero-card,.ui-hero-card-media,.ui-art,.ui-art-tile,.ui-band-img,.ui-compare,.ui-compat-card,.ui-point-icon,.ui-result-tile,.ui-quick-item>*,.ui-lost-tile,.ui-stagger-item,.ui-avatar,.ui-chapters,.ui-chapter-link,.ui-keygroup,.ui-news-intro,.ui-lit-field,.ui-toolbar,.ui-post-bar,.ui-nav-icon-btn,.ui-footer-cols,.ui-quote-track>*',u=[],V=new Set(),io=null,f=0,G=0,lx=NaN,last=0,SC=null,SA=0,GAP=120;
function m(){u=[].slice.call(d.querySelectorAll(S));if(io)io.disconnect();V.clear();if(!window.IntersectionObserver){u.forEach(function(e){V.add(e)});q(1);return}
io=new IntersectionObserver(function(es){es.forEach(function(z){z.isIntersecting?V.add(z.target):V.delete(z.target)});q(1)},{rootMargin:'200px 0px'});u.forEach(function(e){io.observe(e)})}
function lightX(){var L=window.bfaLight;return L&&!L.off?L.px:NaN}
function c(){f=0;last=Date.now();var F=G,sc=SA?null:SC;G=0;SC=null;SA=0;try{var x=lightX(),h=innerWidth/2;
if(R.classList.contains('motion-reduced')||isNaN(x)){u.forEach(function(e){if(e.__sx){e.style.removeProperty('--sx');e.__sx=''}});lx=NaN;return}
var mv=isNaN(lx)||M.abs(x-lx)>=2;if(!F&&!mv)return;if(mv)sc=null;lx=x;var L=[];V.forEach(function(e){if(sc&&!sc.contains(e))return;var r=e.getBoundingClientRect();if(r.width)L.push([e,(M.round(M.max(-1,M.min(1,(r.left+r.width/2-x)/h))*20)/20).toFixed(2)])});
L.forEach(function(t){if(t[1]!==t[0].__sx){t[0].__sx=t[1];t[0].style.setProperty('--sx',t[1])}})}catch(e){}}
function q(F,S){if(F)G=1;if(S){if(SC&&SC!==S)SA=1;SC=S}else if(F)SA=1;if(!f){f=setTimeout(c,M.max(0,last+GAP-Date.now()))}}
var k=0;function h(){clearTimeout(k);k=setTimeout(m,200)}
['load','resize','pageshow'].forEach(function(e){addEventListener(e,h)});window.ResizeObserver&&new ResizeObserver(h).observe(d.body||R);
if(window.bfaLight)window.bfaLight.on(function(){q()});
new MutationObserver(function(){q(1)}).observe(R,{attributes:true,attributeFilter:['class']});d.addEventListener('scroll',function(e){if(e.target!==d&&e.target.nodeType===1)q(1,e.target)},{passive:true,capture:true});
if(d.readyState=='loading')d.addEventListener('DOMContentLoaded',m);else m()})();
}catch(e){console.error("site-foot block 5",e)}
try{
/* BFA Thumb Sizes 1.0 - the small 3D thumbnails (80-120px) ask for a small copy of their image, not the 1024px one. */
[].forEach.call(document.querySelectorAll('img.ui-thumb-tile-icon[srcset]'),function(i){i.sizes=Math.max(80,Math.ceil(i.getBoundingClientRect().width||120))+'px'});
}catch(e){console.error("site-foot block 6",e)}
try{
/* BFA Site Path 2.1 - the breadcrumb pill (About, Community, Support). Built from the nav: section icon + name, this page's menu icon + name;
   the page name opens the section's pages (from the same mega menu). Esc / outside click close it; arrow keys move in it. */
(function(){var d=document,R=d.documentElement,m=location.pathname.match(/^\/(about|community|support)(?:\/|$)/);if(!m)return;
function go(){var main=d.querySelector('main.layout-page');if(!main||d.querySelector('[data-site-path]'))return;
var U='https://cdn.prod.website-files.com/650c5901cff33429a5e537f5/',sec=m[1],names={about:'About',community:'Community',support:'Support'},nav=d.querySelector('.ui-nav'),path=location.pathname.replace(/\/+$/,''),DOC=U+'68b9b72e6ab175721a9bf7cb_documents.svg';
var top=[].slice.call(d.querySelectorAll('.ui-nav [data-nav-toggle]')).filter(function(a){return a.textContent.trim()===names[sec]})[0];
var row=d.querySelector('.ui-nav a.ui-nav-sublink[href="'+path+'"]'),h1=main.querySelector('h1');
var name=row?(row.querySelector('.ui-mega-label')||row).textContent.trim():((h1&&h1.textContent.trim())||d.title.split(' · ')[0]);
var drop=(row&&row.closest('.ui-nav-drop'))||(top&&top.parentElement&&top.parentElement.querySelector('.ui-nav-drop')),seen={};
var rows=drop?[].slice.call(drop.querySelectorAll('a.ui-nav-sublink.is-row[href^="/"]')).filter(function(a){var h=a.getAttribute('href');if(h.indexOf('#')>=0||seen[h])return false;return seen[h]=1}):[];
function el(t,c,x){var e=d.createElement(t);if(c)e.className=c;if(x)e.textContent=x;return e}
function ic(img){var i=el('img','ui-icon is-16');i.alt='';i.src=img?img.getAttribute('src'):DOC;return i}
var bar=el('div','ui-doc-bar is-site'),inn=el('div','layout-wrap ui-doc-bar-in'),nv=el('nav','ui-doc-crumb');bar.setAttribute('data-site-path','');nv.setAttribute('aria-label','Breadcrumb');
var a=el('a','ui-doc-crumb-link ui-doc-crumb-section');a.href='/'+sec+'/overview';a.appendChild(ic(top&&top.querySelector('img.ui-icon')));a.appendChild(el('span','',names[sec]));
var sp=el('span','ui-doc-crumb-sep','▶');sp.setAttribute('aria-hidden','true');
var many=rows.length>1,here=el(many?'button':'div','ui-doc-crumb-here');here.appendChild(ic(row&&row.querySelector('img')));here.appendChild(el('span','',name));
nv.appendChild(a);nv.appendChild(sp);nv.appendChild(here);
if(many){here.type='button';var cr=el('img','bfa-crumb-caret');cr.alt='';cr.src=U+'68b9b72c72af6f6934d37018_disclosure_tri_right.svg';here.appendChild(cr);
 var mu=el('div','ui-menu-list bfa-crumb-menu');mu.id='bfa-crumb-menu';mu.setAttribute('role','menu');mu.setAttribute('aria-label',names[sec]+' pages');
 rows.forEach(function(r){var x=el('a');x.href=r.getAttribute('href');x.setAttribute('role','menuitem');if(r.getAttribute('href')===path)x.setAttribute('aria-current','page');x.appendChild(ic(r.querySelector('img')));x.appendChild(el('span','',(r.querySelector('.ui-mega-label')||r).textContent.trim()));mu.appendChild(x)});
 nv.appendChild(mu);here.setAttribute('aria-haspopup','true');here.setAttribute('aria-expanded','false');here.setAttribute('aria-controls',mu.id);here.setAttribute('aria-label',name+', more '+names[sec]+' pages');
 var open=function(){return mu.classList.contains('is-open')},set=function(o){mu.classList.toggle('is-open',o);here.setAttribute('aria-expanded',String(o))};
 here.addEventListener('click',function(e){e.stopPropagation();set(!open());if(open())(mu.querySelector('[aria-current]')||mu.firstChild).focus()});
 d.addEventListener('click',function(e){if(open()&&!nv.contains(e.target))set(false)});
 d.addEventListener('keydown',function(e){if(!open())return;if(e.key==='Escape'){set(false);here.focus()}else if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault();var L=[].slice.call(mu.children),i=L.indexOf(d.activeElement);L[(i+(e.key==='ArrowDown'?1:-1)+L.length)%L.length].focus()}})}
else here.setAttribute('aria-current','page');
inn.appendChild(nv);bar.appendChild(inn);main.parentNode.insertBefore(bar,main);R.classList.add('has-site-path');
function size(){if(nav)R.style.setProperty('--bfa-nav-h',Math.round(nav.getBoundingClientRect().height)+'px');var h=Math.round(bar.getBoundingClientRect().height),nx=main.firstElementChild,pt=nx?parseFloat(getComputedStyle(nx).paddingTop)||0:0;R.style.setProperty('--bfa-path-h',h+'px');bar.classList.toggle('is-over',!!nx&&(nx.matches('.ui-cover')||pt>=h+24))}
size();addEventListener('resize',size);addEventListener('load',size)}
if(d.readyState=='loading')d.addEventListener('DOMContentLoaded',go);else go()})();
/* BFA To Top 1.0 - [data-to-top] (footer Back to top) scrolls to the top; Webflow ignores plain # links. Instant when motion is off. */
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-to-top]');if(!a)return;e.preventDefault();var R=document.documentElement,still=R.classList.contains('motion-reduced')||matchMedia('(prefers-reduced-motion: reduce)').matches;scrollTo({top:0,behavior:still?'auto':'smooth'})},true);
/* BFA Out Links 1.0 - links to other sites open in a new tab (set on click, so links added later count too). */
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a||a.target||!/^https?:/.test(a.href)||a.host===location.host)return;a.target='_blank';if(!/noopener/.test(a.rel))a.rel=(a.rel+' noopener').trim()},true);
}catch(e){console.error("site-foot block 7",e)}
try{
/* BFA Paths 4.7 - (4.7: data-paths-from="none" = no line in; data-paths-chain = a row of cards linked one after the other, snaking row to row; 4.6: the line layers shrink back before the page is measured, so they never push the page past the footer; 4.5: explicit parents; 4.4: lines pass behind pictures) choice lines for every [data-paths] block (colour: the section light, BFA Sockets; data-paths-color="pink" for boolean pink).
   A link leaves the lead (data-paths-from, or the hero buttons above), runs into the title node, then branches into the path cards row by row in
   straight runs only (4.3: no diagonals; 4.1 fork above a lone top card; 4.2 gap drops for three over two). data-paths-tree: every card hangs from
   the nearest card of the row above (People); 4.5: data-paths-parents="-,0,0,1" names each card's parent by index when it sits in the row above. Hover a card or its line: its branch lights up; clicking a line opens its card. */
(function(){var d=document,R=d.documentElement,NS='http://www.w3.org/2000/svg';
function reduced(){return R.classList.contains('motion-reduced')||matchMedia('(prefers-reduced-motion: reduce)').matches}
function el(t,a,p){var e=d.createElementNS(NS,t);for(var k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e}
function box(e){var r=e.getBoundingClientRect(),sx=scrollX,sy=scrollY;return{l:r.left+sx,t:r.top+sy,r:r.right+sx,b:r.bottom+sy,w:r.width,h:r.height,cx:r.left+sx+r.width/2}}
var all=[],N=0;
[].slice.call(d.querySelectorAll('[data-paths]')).forEach(function(P){var cid='bfa-pc-'+(++N);
 var head=P.querySelector('.ui-paths-head'),cards=[].slice.call(P.querySelectorAll('.ui-card.is-path'));if(!head||!cards.length)return;
 var fs=P.getAttribute('data-paths-from'),lead=fs?d.querySelector(fs):null,col=lead?(lead.closest('.layout-stack')||lead):null,lx=lead?(lead.firstElementChild||lead):null;
 if(!lead&&fs!=='none'){var sec=P.closest('section')||P,hero=sec.previousElementSibling;if(!hero||!hero.matches('.ui-cover'))hero=d.querySelector('.ui-cover');var hb=hero&&(hero.querySelector('.ui-cover-actions')||hero.querySelector('.ui-cover-copy'));if(hb){col=hb;lx=null}}
 var c=P.getAttribute('data-paths-color'),cls='bfa-paths-layer'+(c?' is-'+c:'');
 var low=el('svg',{'class':cls,'aria-hidden':'true'}),top=el('svg',{'class':cls+' is-top','aria-hidden':'true'});d.body.appendChild(low);d.body.appendChild(top);
 var chains=[],shared=[],trunk=[],rowOf=[],hotI=-1,mode='',PAR=null;
 function link(dp,owner){var g=el('g',{'class':'ui-link'},low);['ui-link-edge','ui-link-core','ui-link-flow','ui-link-hit'].forEach(function(k){el('path',{'class':k,d:dp},g)});
  if(owner>=0){var h=g.lastChild;h.addEventListener('mouseenter',function(){hot(owner)});h.addEventListener('mouseleave',function(){hot(-1)});h.addEventListener('click',function(){var b=cards[owner].querySelector('a.ui-btn')||cards[owner].querySelector('a[href]');if(b)b.click()})}return g}
 function sock(x,y,k){return el('circle',{'class':'ui-sock'+(k?' '+k:''),cx:x,cy:y,r:5.2},top)}
 function hot(i){hotI=i;var A={};if(PAR&&i>=0)for(var a=i;a>=0;a=PAR[a])A[a]=1;shared.forEach(function(g){g.classList.toggle('is-hot',i>=0)});
  trunk.forEach(function(t){var on=i>=0&&t.r<=rowOf[i];t.g.classList.toggle('is-hot',on);t.s.forEach(function(s){s.classList.toggle('is-hot',on)})});
  chains.forEach(function(ch,k){var on=PAR?!!A[k]:k===i||(i>=0&&ch.tr!=null&&ch.tr<rowOf[i]);ch.links.forEach(function(g){g.classList.toggle('is-hot',on);if(on)low.appendChild(g)});ch.socks.forEach(function(s){s.classList.toggle('is-hot',on)});cards[k].classList.toggle('is-linked',k===i&&!cards[k].matches(':hover'))})}
 function draw(){low.innerHTML='';top.innerHTML='';chains=[];shared=[];trunk=[];rowOf=[];PAR=null;
  var pb=box(P);if(!pb.w)return;var H=Math.max(R.scrollHeight,d.body.scrollHeight)+'px';low.style.height=top.style.height=H;
  var hd=box(head),cs=cards.map(box),cx=Math.round(hd.cx),B={x:cx,y:Math.round(hd.t+2)},C={x:cx,y:Math.round(hd.b)};
  if(col){var cb=box(col),xb=lx?box(lx):cb,gap=B.y-cb.b,A={x:Math.round(Math.abs(xb.cx-cx)<4||!lx?cx:xb.cx),y:Math.round(cb.b+Math.min(24,Math.max(10,gap*.2)))};
   if(A.y<B.y-6){sock(A.x,A.y,'is-out');
    if(A.x===cx)shared.push(link('M'+A.x+' '+A.y+'V'+B.y,-1));
    else{var jy=Math.round(A.y+(B.y-A.y)*.5);shared.push(link('M'+A.x+' '+A.y+'V'+jy+'H'+cx+'V'+B.y,-1));sock(A.x,jy,'is-reroute');sock(cx,jy,'is-reroute')}}}
  sock(B.x,B.y,'is-in');sock(C.x,C.y,'is-out');
  /* rows of cards, top to bottom */
  var rows=[];cs.forEach(function(k,i){var r=rows.filter(function(r){return Math.abs(r.t-k.t)<8})[0];if(r){r.i.push(i);r.t=Math.min(r.t,k.t);r.b=Math.max(r.b,k.b)}else rows.push({t:k.t,b:k.b,i:[i]})});
  rows.sort(function(a,b){return a.t-b.t});
  mode=rows.length===1?(cs.length>1?'row':'single'):rows.every(function(r){return r.i.length===1})?'stack':'grid';
  if(P.hasAttribute('data-paths-tree')){/* 4.3 tree: each card hangs from the nearest card of the row above (the first row from the title node); straight runs only */
   PAR=[];var byT=[],out={},PP=(P.getAttribute('data-paths-parents')||'').split(','),stk=rows.every(function(w){return w.i.length===1});rows.forEach(function(row,r){var gt=r?rows[r-1].b:C.y,y1=Math.round(gt+(row.t-gt)*.5);
    row.i.forEach(function(i){rowOf[i]=r;var k=cs[i],x=Math.round(k.cx),y=Math.round(k.t),p=-1,px=cx,py=C.y,b=1e9;var e=stk?-1:parseInt(PP[i],10);if(r&&e>=0&&rowOf[e]===r-1)p=e;else if(r)rows[r-1].i.forEach(function(j){var q=Math.abs(cs[j].cx-k.cx);if(q<b){b=q;p=j}});
     if(p>=0){px=Math.round(cs[p].cx);py=Math.round(cs[p].b);if(!out[p]){out[p]=1;sock(px,py,'is-out')}}PAR[i]=p;var st=Math.abs(px-x)<4,so=[sock(x,y,'is-in')];if(!st){so.unshift(sock(x,y1,'is-reroute'));sock(px,y1,'is-reroute')}
     byT[i]={links:[link('M'+px+' '+py+(st?'':'V'+y1+'H'+x)+'V'+y,i)],socks:so}})});
   chains=cards.map(function(_,i){return byT[i]||{links:[],socks:[]}});low.setAttribute('data-mode','tree');behind();if(hotI>=0)hot(hotI);return}
  var from={x:cx,y:C.y},prevB=C.y,byI=[];
  rows.forEach(function(row,r){var gt=prevB,gb=row.t,one=row.i.length===1&&Math.abs(cs[row.i[0]].cx-cx)<4;
   row.i.forEach(function(i){rowOf[i]=r});
   var nx=rows[r+1],gb0=box(cards[0].parentElement);
   if(one&&nx&&nx.i.every(function(i){return Math.abs(cs[i].cx-cx)>=4})&&cs[row.i[0]].l-gb0.l>=28&&gb0.r-cs[row.i[0]].r>=28){
    /* 4.1 fork: a choice on top with more choices under it (three cards on wide phones). The line forks ABOVE the top card:
       one branch drops into it, the others run out to the left and right, down beside it, and step into the cards of the next row.
       Nothing passes under a card, so every choice reads as its own branch. */
    var i0=row.i[0],k0=cs[i0],F={x:cx,y:Math.round(gt+(gb-gt)*(r?.4:.42))},xL=Math.round((gb0.l+k0.l)/2),xR=Math.round((gb0.r+k0.r)/2),y1=Math.round(row.b+(nx.t-row.b)*.5);
    trunk.push({g:link('M'+from.x+' '+from.y+'V'+F.y,-1),r:r,s:[sock(F.x,F.y,'is-reroute')]});
    byI[i0]={links:[link('M'+F.x+' '+F.y+'V'+Math.round(k0.t),i0)],socks:[sock(cx,Math.round(k0.t),'is-in')]};
    nx.i.forEach(function(i){var k=cs[i],x=Math.round(k.cx),y=Math.round(k.t),xs=k.cx<cx?xL:xR;
     byI[i]={links:[link('M'+F.x+' '+F.y+'H'+xs+'V'+y1+'H'+x+'V'+y,i)],socks:[sock(xs,F.y,'is-reroute'),sock(x,y,'is-in')]};rowOf[i]=r+1});
    nx.done=true;from={x:cx,y:Math.round(nx.b)};prevB=nx.b;return}
   if(row.done)return;
   if(one){/* a card straight below: the trunk drops into its top, then runs on under it */
    var i0=row.i[0],k0=cs[i0];byI[i0]={links:[link('M'+from.x+' '+from.y+'V'+Math.round(k0.t),i0)],socks:[sock(cx,Math.round(k0.t),'is-in')],tr:r};
    from={x:cx,y:Math.round(k0.b)}}
   else{var J={x:cx,y:Math.round(gt+(gb-gt)*(r?.4:.42))};
    trunk.push({g:link('M'+from.x+' '+from.y+'V'+J.y,-1),r:r,s:[sock(J.x,J.y,'is-reroute')]});
    row.i.forEach(function(i){var k=cs[i],x=Math.round(k.cx),y=Math.round(k.t),so=[],dp;
     if(Math.abs(x-J.x)<4)dp='M'+J.x+' '+J.y+'V'+y;else{dp='M'+J.x+' '+J.y+'H'+x+'V'+y;if(y-J.y>=22)so.push(sock(x,J.y,'is-reroute'))}
     byI[i]={links:[link(dp,i)],socks:so.concat([sock(x,y,'is-in')])}});
    /* on to the next row: out from under the card that covers the middle, or on down the gap between the columns */
    var cover=row.i.map(function(i){return cs[i]}).filter(function(k){return k.l<cx-2&&k.r>cx+2})[0];
    /* 4.2 gap drops: when a card covers the middle but every card of the next row sits under a gap of this row
       (three over two), each of those cards gets its own branch from the junction that drops straight down the gap.
       No line runs under a card. */
    if(cover&&nx&&nx.i.every(function(i){var x=cs[i].cx;return row.i.every(function(j){return x<cs[j].l-3||x>cs[j].r+3})})){
     nx.i.forEach(function(i){var k=cs[i],x=Math.round(k.cx),y=Math.round(k.t),so=[sock(x,y,'is-in')];if(Math.abs(x-J.x)>=4)so.unshift(sock(x,J.y,'is-reroute'));
      byI[i]={links:[link('M'+J.x+' '+J.y+(Math.abs(x-J.x)<4?'':'H'+x)+'V'+y,i)],socks:so};rowOf[i]=r+1});
     nx.done=true;from={x:cx,y:Math.round(nx.b)};prevB=nx.b;return}
    from=cover?{x:cx,y:Math.round(cover.b)}:{x:J.x,y:J.y}}
   prevB=row.b});
  chains=cards.map(function(_,i){return byI[i]||{links:[],socks:[]}});
  low.setAttribute('data-mode',mode);behind();if(hotI>=0)hot(hotI)}
 /* 4.4: lines pass behind pictures (hero art, splash, image frames, [data-paths-behind]), never over them: each line is clipped around them */
 function behind(){var W=Math.max(R.scrollWidth,d.body.scrollWidth),Y=Math.max(R.scrollHeight,d.body.scrollHeight),p='M0 0H'+W+'V'+Y+'H0Z';
  [].forEach.call(d.querySelectorAll('.ui-art,.ui-spread-frame,.ui-hero-card-media,[data-paths-behind]'),function(e){if(e.closest('.ui-card.is-path'))return;var b=box(e);if(b.w&&b.h)p+='M'+Math.round(b.l)+' '+Math.round(b.t)+'V'+Math.round(b.b)+'H'+Math.round(b.r)+'V'+Math.round(b.t)+'Z'});
  el('path',{d:p},el('clipPath',{id:cid,clipPathUnits:'userSpaceOnUse'},el('defs',{},low)));[].forEach.call(low.querySelectorAll('g.ui-link'),function(g){g.setAttribute('clip-path','url(#'+cid+')')})}
 cards.forEach(function(k,i){k.addEventListener('mouseenter',function(){hot(i)});k.addEventListener('mouseleave',function(){hot(-1)});k.addEventListener('focusin',function(){hot(i)});k.addEventListener('focusout',function(){hot(-1)})});
 if('IntersectionObserver' in window)new IntersectionObserver(function(es){low.classList.toggle('is-live',es[0].isIntersecting&&!reduced())}).observe(P);
 all.push(draw)});
[].slice.call(d.querySelectorAll('[data-paths-chain]')).forEach(function(G){/* 4.7 chain: each card links to the next; along a row left to right, then out the right side, down, back across the row gap and into the next row from the left */
 var c=G.getAttribute('data-paths-color'),cls='bfa-paths-layer'+(c?' is-'+c:''),low=el('svg',{'class':cls,'aria-hidden':'true'}),top=el('svg',{'class':cls+' is-top','aria-hidden':'true'}),L=[];d.body.appendChild(low);d.body.appendChild(top);
 var cards=[].slice.call(G.children).filter(function(k){return k.matches('.ui-card')});
 function hot(i){L.forEach(function(x,k){var on=i>=0&&k<i;x.g.classList.toggle('is-hot',on);x.s.forEach(function(s){s.classList.toggle('is-hot',on)})})}
 cards.forEach(function(k,i){k.addEventListener('mouseenter',function(){hot(i)});k.addEventListener('mouseleave',function(){hot(-1)})});
 if('IntersectionObserver' in window)new IntersectionObserver(function(es){low.classList.toggle('is-live',es[0].isIntersecting&&!reduced())}).observe(G);
 all.push(function(){low.innerHTML='';top.innerHTML='';L=[];var cs=cards.map(box);if(!cs.length||!cs[0].w)return;low.style.height=top.style.height=Math.max(R.scrollHeight,d.body.scrollHeight)+'px';
  var gb=box(G.parentElement||G),r=Math.round;function S(x,y,k){return el('circle',{'class':'ui-sock '+k,cx:x,cy:y,r:5.2},top)}
  function K(p,s){var g=el('g',{'class':'ui-link'},low);['ui-link-edge','ui-link-core','ui-link-flow'].forEach(function(k){el('path',{'class':k,d:p},g)});L.push({g:g,s:s})}
  for(var i=1;i<cs.length;i++){var a=cs[i-1],b=cs[i];
   if(Math.abs(a.t-b.t)<8&&b.l>a.r){var y=r(Math.max(a.t,b.t)+Math.min(a.h,b.h)/2);K('M'+r(a.r)+' '+y+'H'+r(b.l),[S(r(a.r),y,'is-out'),S(r(b.l),y,'is-in')])}
   else if(Math.abs(a.cx-b.cx)<4)K('M'+r(a.cx)+' '+r(a.b)+'V'+r(b.t),[S(r(a.cx),r(a.b),'is-out'),S(r(b.cx),r(b.t),'is-in')]);
   else{var ya=r(a.t+a.h/2),yb=r(b.t+b.h/2),ym=r((a.b+b.t)/2),xr=r(a.r+Math.max(8,Math.min(28,(gb.r-a.r)/2))),xl=r(b.l-Math.max(8,Math.min(28,(b.l-gb.l)/2)));
    K('M'+r(a.r)+' '+ya+'H'+xr+'V'+ym+'H'+xl+'V'+yb+'H'+r(b.l),[S(r(a.r),ya,'is-out'),S(xr,ym,'is-reroute'),S(xl,ym,'is-reroute'),S(r(b.l),yb,'is-in')])}}})});
if(!all.length)return;var raf=0;function drawAll(){raf=0;[].forEach.call(d.querySelectorAll('.bfa-paths-layer'),function(s){s.style.height='0px'});all.forEach(function(f){f()})}function later(){if(!raf)raf=requestAnimationFrame(drawAll)}
drawAll();addEventListener('resize',later);addEventListener('load',later);if(d.fonts&&d.fonts.ready)d.fonts.ready.then(later);
if('ResizeObserver' in window){var ro=new ResizeObserver(later);ro.observe(d.body)}
window.__bfaPaths={draw:drawAll}})();
}catch(e){console.error("site-foot block 8",e)}
try{
/* BFA Perf Note 1.0 - shown once per browser when BFA Perf Guard pauses animation. "Turn animation on" saves Motion: on through the View menu. */
(function(){var d=document,R=d.documentElement,L=localStorage,K='bfa-perf-note';
function show(){if(!R.hasAttribute('data-perf-note')||d.querySelector('.bfa-perf-note'))return;try{if(L.getItem(K))return;L.setItem(K,'1')}catch(e){return}
var b=d.createElement('div');b.className='bfa-perf-note';b.setAttribute('role','status');b.innerHTML='<span>Animations are paused so the site stays fast on this device.</span><button type="button">Turn animation on</button><button type="button" aria-label="Close">✕</button>';d.body.appendChild(b);
var x=b.querySelectorAll('button');x[0].onclick=function(){var p=d.querySelector('[data-pref="motion"][data-value="on"]');R.classList.remove('perf-auto');if(p)p.click();else{try{var o=JSON.parse(L.getItem('bfa-prefs')||'{}')||{};o.motion='on';L.setItem('bfa-prefs',JSON.stringify(o))}catch(e){}R.classList.remove('motion-reduced')}b.remove()};x[1].onclick=function(){b.remove()}}
d.addEventListener('bfa-perf-note',show);show()})();
}catch(e){console.error("site-foot block 9",e)}
