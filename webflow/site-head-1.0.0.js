/* Bforartists website · site-head.js · @version 1.0.0 · Site-wide head code (Webflow Site settings, Custom code, Head). Each original <script> block is wrapped on its own, so one failing block cannot stop the next. */
try{
/* BFA Paper 1.2 - adds the dither layer as the last child of <body>. */
document.addEventListener('DOMContentLoaded',function(){var b=document.body;if(!b||b.querySelector(':scope>.bfa-dither'))return;var e=document.createElement('div');e.className='bfa-dither';e.setAttribute('aria-hidden','true');b.appendChild(e)});
}catch(e){console.error("site-head block 1",e)}
try{
/* BFA Cover 1.0 - hero videos: always muted + looping (browsers only autoplay muted video); no playback when motion is reduced. */
document.addEventListener('DOMContentLoaded',function(){var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;document.querySelectorAll('video[data-cover-video]').forEach(function(v){v.muted=true;v.loop=true;v.playsInline=true;v.setAttribute('muted','');if(rm||document.querySelector('.motion-reduced')){v.pause();return}var p=v.play();if(p&&p.catch)p.catch(function(){})})});
}catch(e){console.error("site-head block 2",e)}
try{
/* BFA Sectors 1.0 - picks the section in the middle of the screen and sets html[data-sector] (checked at most every 50ms while scrolling). */
(function(){var d=document,R=d.documentElement,C=['blue','orange','green','purple'],zones=[],cur='',raf=0;
function colour(el){var a=el.getAttribute('data-light');if(a)return a;var f=el.querySelector('.ui-spread-frame');if(!f)return null;for(var i=0;i<C.length;i++)if(f.classList.contains('is-'+C[i]))return C[i];return null}
function scan(){zones=[].slice.call(d.querySelectorAll('[data-light],.ui-stage,.ui-spread')).map(function(e){return{e:e,c:colour(e)}}).filter(function(z){return z.c})}
function pick(){raf=0;var mid=innerHeight*.5,best=null;zones.forEach(function(z){var r=z.e.getBoundingClientRect();if(r.top<mid&&r.bottom>mid)best=z});var c=best?best.c:'blue';if(c!==cur){cur=c;if(c==='blue')R.removeAttribute('data-sector');else R.setAttribute('data-sector',c)}}
function req(){if(!raf)raf=setTimeout(pick,50)}
d.addEventListener('DOMContentLoaded',function(){scan();if(!zones.length)return;pick();addEventListener('scroll',req,{passive:true});addEventListener('resize',req)})})();
}catch(e){console.error("site-head block 3",e)}
try{
/* BFA Wall 1.3 - 1.3: stands down on slow devices (html.perf-auto). 1.2: smooth falloffs (no edge rings), better noise, built-in paper grain. 1.2: drawn at 1x pixel density (soft light, same look, a quarter of the
   pixels on Retina), the light comes from window.bfaLight (BFA Light 3.2), and colours are read only when the theme or section colour changes. */
(function(){var d=document,R=d.documentElement;
var VS='attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
var FS='precision highp float;uniform vec2 uRes,uGrain;uniform float uDpr,uAng,uGlow;uniform vec2 uLight,uWall;uniform vec3 uBase;uniform vec4 uTop,uBot,uWarm,uSpec,uBlue,uBlue2;'+
'float h(vec2 q){vec3 p3=fract(vec3(q.xyx)*.1031);p3+=dot(p3,p3.yzx+33.33);return fract((p3.x+p3.y)*p3.z);}'+
'float fall(float d,float e){return 1.-smoothstep(0.,e,d);}'+
'vec3 ov(vec3 c,vec3 k,float a){return mix(c,k,clamp(a,0.,1.));}'+
'void main(){vec2 p=vec2(gl_FragCoord.x,uRes.y*uDpr-gl_FragCoord.y)/uDpr;vec2 S=uRes;vec3 c=uBase;'+
'vec2 dir=vec2(sin(uAng),-cos(uAng));float L=abs(S.x*dir.x)+abs(S.y*dir.y);float t=dot(p-S*.5,dir)/L+.5;'+
'if(t<.38)c=ov(c,uTop.rgb,uTop.a*(1.-smoothstep(0.,.38,t)));else c=ov(c,uBot.rgb,uBot.a*smoothstep(.38,1.,t));'+
'c=ov(c,uWarm.rgb,uWarm.a*fall(length((p-vec2(.9*S.x,S.y))/vec2(.45*S.x,.4*S.y)),.7));'+
'c=ov(c,uSpec.rgb,uSpec.a*fall(length((p-uWall)/vec2(.7*S.x,.55*S.y)),.7));'+
'float db=length(p-uLight)/uGlow,gw=fall(db,.72);c=ov(c,mix(uBlue.rgb,uBlue2.rgb,smoothstep(0.,.45,db)),uBlue.a*gw);'+
'float n=h(gl_FragCoord.xy)+h(gl_FragCoord.xy+vec2(47.3,11.9))-1.;c+=n*(1.+uGrain.x+uGrain.y*gw)/255.;gl_FragColor=vec4(c,1.);}';
function start(){if(d.querySelector('.bfa-wall')||R.classList.contains('perf-auto'))return;var cv=d.createElement('canvas');cv.className='bfa-wall';cv.setAttribute('aria-hidden','true');
var gl=cv.getContext('webgl',{alpha:false,antialias:false,depth:false,stencil:false,powerPreference:'low-power'});if(!gl)return;
function sh(t,s){var o=gl.createShader(t);gl.shaderSource(o,s);gl.compileShader(o);return gl.getShaderParameter(o,gl.COMPILE_STATUS)?o:null}
var v=sh(gl.VERTEX_SHADER,VS),f=sh(gl.FRAGMENT_SHADER,FS);if(!v||!f)return;var pr=gl.createProgram();gl.attachShader(pr,v);gl.attachShader(pr,f);gl.linkProgram(pr);if(!gl.getProgramParameter(pr,gl.LINK_STATUS))return;gl.useProgram(pr);
var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);var ap=gl.getAttribLocation(pr,'p');gl.enableVertexAttribArray(ap);gl.vertexAttribPointer(ap,2,gl.FLOAT,false,0,0);
var U={};['uRes','uGrain','uDpr','uAng','uGlow','uLight','uWall','uBase','uTop','uBot','uWarm','uSpec','uBlue','uBlue2'].forEach(function(n){U[n]=gl.getUniformLocation(pr,n)});
var x2=d.createElement('canvas').getContext('2d');function col(s){x2.fillStyle='#000';x2.fillStyle=(s||'').trim()||'transparent';var q=x2.fillStyle;if(q[0]=='#')return[parseInt(q.substr(1,2),16)/255,parseInt(q.substr(3,2),16)/255,parseInt(q.substr(5,2),16)/255,1];var m=q.match(/[\d.]+/g);return[m[0]/255,m[1]/255,m[2]/255,m.length>3?+m[3]:1]}
var W=0,H=0,dpr=1,K=null;function size(){W=innerWidth;H=innerHeight;cv.width=Math.round(W*dpr);cv.height=Math.round(H*dpr);gl.viewport(0,0,cv.width,cv.height)}
/* colours and grain: read from CSS only when asked (start, theme / section change, resize) */
function colours(){var cs=getComputedStyle(d.body),g=function(k){return cs.getPropertyValue(k)},n=function(k,def){var s=parseFloat(g(k));return isNaN(s)?def:s};
K={base:col(g('--_bfa---surface--wall')).slice(0,3),top:col(g('--w-top')),bot:col(g('--w-bot')),warm:col(g('--w-warm')),spec:col(g('--w-spec')),blue:col(g('--w-blue')),blue2:col(g('--w-blue2')),
g1:n('--paper-g',.6),g2:n('--paper-gs',1.6),rem:parseFloat(getComputedStyle(R).fontSize)||16}}
function draw(fresh){if(!cv.isConnected)return;if(fresh||!K)colours();var L=window.bfaLight,on=L&&!L.off;
gl.uniform2f(U.uRes,W,H);gl.uniform2f(U.uGrain,K.g1,K.g2);gl.uniform1f(U.uDpr,dpr);gl.uniform1f(U.uAng,(on?L.wa:180)*Math.PI/180);gl.uniform1f(U.uGlow,Math.min(56*K.rem,1.2*Math.min(W,H)));
gl.uniform2f(U.uLight,(on?L.x:.3)*W,(on?L.y:.2)*H);gl.uniform2f(U.uWall,(on?L.wx:.56)*W,(on?L.wy:.18)*H);
gl.uniform3fv(U.uBase,K.base);gl.uniform4fv(U.uTop,K.top);gl.uniform4fv(U.uBot,K.bot);gl.uniform4fv(U.uWarm,K.warm);gl.uniform4fv(U.uSpec,K.spec);gl.uniform4fv(U.uBlue,K.blue);gl.uniform4fv(U.uBlue2,K.blue2);
gl.drawArrays(gl.TRIANGLES,0,3)}
var pend=0,until=0;function req(){if(!pend)pend=requestAnimationFrame(function(){pend=0;draw()})}
/* a theme or section change fades the colours over about a second: re-read them each frame only for that long */
function loop(){draw(true);if(performance.now()<until)requestAnimationFrame(loop)}
function anim(ms){var on=performance.now()<until;until=performance.now()+ms;if(!on)requestAnimationFrame(loop)}
cv.addEventListener('webglcontextlost',function(){R.classList.remove('bfa-gl');cv.remove()});
size();draw(true);d.body.insertBefore(cv,d.body.firstChild);R.classList.add('bfa-gl');
if(window.bfaLight)window.bfaLight.on(req);else addEventListener('load',function(){if(window.bfaLight)window.bfaLight.on(req)});
new MutationObserver(function(){anim(1400)}).observe(R,{attributes:true,attributeFilter:['class','data-sector']});
addEventListener('resize',function(){size();K=null;req()})}
/* 1.3: a slow device (html.perf-auto, set by BFA Perf Guard) gets no GPU wall - the CSS wall in body::before draws instead; if the guard decides later, the canvas goes */
function gate(){var cv=d.querySelector('.bfa-wall');if(R.classList.contains('perf-auto')){if(cv){cv.remove();R.classList.remove('bfa-gl')}}else if(!cv&&d.body)start()}
new MutationObserver(gate).observe(R,{attributes:true,attributeFilter:['class']});
if(d.readyState=='loading')d.addEventListener('DOMContentLoaded',gate);else gate()})();
}catch(e){console.error("site-head block 4",e)}
