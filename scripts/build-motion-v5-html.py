from pathlib import Path
import base64, json, html
root=Path(__file__).resolve().parents[1]
out=root/'previews'/'html'
out.mkdir(parents=True,exist_ok=True)
logo=base64.b64encode((root/'public'/'brand'/'bharat-mode-avatar.svg').read_bytes()).decode()
beats=[
 {'id':'origin','from':0,'to':5,'headline':'Built for\nbreakthroughs.','kicker':'THE RESEARCH BACKBONE','theme':'saffron','label':'DESIGN → MANUFACTURE → DEPLOY','groups':['India is building','powerful computers','to support','scientific research.']},
 {'id':'deployed','from':5,'to':10.5,'headline':'6,000 Rudra\nservers.','kicker':'ALREADY DEPLOYED','theme':'midnight','label':'PARAM RUDRA / SERVER SYSTEMS','groups':['Six thousand Rudra','servers were deployed','by September','twenty twenty six.']},
 {'id':'research','from':10.5,'to':16,'headline':'More power.\nMore possibilities.','kicker':'WHY IT MATTERS','theme':'ivory','label':'RESEARCH / SCIENCE / COMPUTING','groups':['That computing power','can support weather,','materials and','biomedical science.']}
]
styles=r'''*{box-sizing:border-box}
:root{--saffron:#E8752E;--ivory:#FFF7EB;--navy:#283039;--charcoal:#0B1018;--teal:#117A7A}
body{margin:0;background:#F5F0E9;color:#283039;font-family:Manrope,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:auto;padding:28px 22px 50px;display:grid;grid-template-columns:minmax(340px,420px) minmax(320px,1fr);gap:30px;align-items:start}
.intro{grid-column:1/-1}.eyebrow{font-size:12px;font-weight:700;letter-spacing:2px;color:#A63F17}.intro h1{font:800 29px/1.25 Sora,Arial,sans-serif;letter-spacing:-1px;margin:7px 0}.intro p{max-width:750px;font-size:14px;line-height:1.6;color:#56616B;margin:8px 0 0}
.viewport{width:100%;aspect-ratio:9/16;overflow:hidden;position:relative;background:var(--charcoal);border-radius:18px;box-shadow:0 26px 65px #0002;isolation:isolate}
.screen{width:1080px;height:1920px;position:absolute;left:0;top:0;transform-origin:0 0;overflow:hidden;isolation:isolate}
.scene{position:absolute;inset:0;overflow:hidden;will-change:transform,opacity;contain:paint}
.scene[data-theme=saffron]{background:linear-gradient(138deg,#E8752E,#EF9962);--ink:#0B1018;--small:#0B1018;--bar:#151F2940;--progress:#FFF7EB}
.scene[data-theme=midnight]{background:#0B1018;--ink:#FFF7EB;--small:#8AD5C8;--bar:#3C4D52;--progress:#E8752E}
.scene[data-theme=ivory]{background:linear-gradient(140deg,#FFF7EB,#FBF0E1);--ink:#283039;--small:#A63F17;--bar:#D8D2CB;--progress:#E8752E}
.soft-orbit{position:absolute;left:-240px;top:1130px;width:1130px;height:750px;border:55px solid #117A7A19;border-radius:50%;transform:rotate(-22deg)}
.glow{position:absolute;right:-270px;top:535px;width:960px;height:960px;border-radius:50%;background:radial-gradient(circle,#FFF7EB42,transparent 72%);will-change:transform}
.scene[data-theme=midnight] .glow{background:radial-gradient(circle,#117A7A55,transparent 70%)}
.scene[data-theme=ivory] .glow{background:radial-gradient(circle,#E8752E20,transparent 71%)}
.header{position:absolute;left:86px;right:72px;top:89px;display:flex;justify-content:space-between;align-items:center;z-index:50}
.header img{width:88px;height:88px}.pill{background:#0B1018;color:#FFF7EB;padding:17px 26px;border-radius:50px;font:500 27px Manrope,Arial,sans-serif;letter-spacing:1.4px}
.screen[data-active-theme=midnight] .pill{background:#FFF7EB;color:#0B1018}
.kicker{position:absolute;top:283px;left:86px;right:165px;font:700 27px Manrope,Arial,sans-serif;letter-spacing:3.1px;color:var(--small);will-change:transform,opacity}
.heading-wrapper{position:absolute;left:83px;right:165px;top:364px;min-height:260px;will-change:transform,opacity}
.typed{font:800 92px/1.17 Sora,Arial,sans-serif;white-space:pre-line;letter-spacing:-3.5px;color:var(--ink);overflow-wrap:normal}
/* The hero moves substantially closer to the headline; the old top was 920. */
.hero{position:absolute;top:777px;left:80px;right:165px;height:500px;background:#101D27;border:2px solid #48656B66;border-radius:40px;overflow:hidden;will-change:transform,opacity;box-shadow:0 24px 54px #101F2A22}
.hero-kicker{position:absolute;top:33px;left:43px;color:#FFBE91;font:700 22px Manrope,Arial,sans-serif;letter-spacing:1.6px}
.racks{position:absolute;top:118px;left:75px;display:flex;gap:35px}
.rack{height:242px;width:180px;background:linear-gradient(125deg,#2B4751,#182833);border:3px solid #5B8285;border-radius:20px;padding:18px;display:flex;flex-direction:column;gap:12px;will-change:transform,opacity}
.rack i{height:28px;border-radius:5px;background:#385861;border:2px solid #648486;position:relative}
.rack i:after{content:'';position:absolute;right:7px;top:7px;width:6px;height:6px;border-radius:50%;background:#70D3CC}
.flow{position:absolute;left:100px;right:100px;bottom:45px;height:8px;background:#264348;border-radius:10px;overflow:hidden}
.flow i{display:block;width:0;height:100%;border-radius:10px;background:linear-gradient(90deg,#117A7A,#E8752E)}
/* Caption is centered against full 1080px canvas, never placed near edges. */
.captions{position:absolute;top:1405px;left:140px;right:140px;height:175px;display:flex;align-items:center;justify-content:center;z-index:52;pointer-events:none}
.caption-box{display:inline-flex;width:max-content;max-width:100%;align-items:center;justify-content:center;padding:18px 24px;min-height:112px;border-radius:12px;background:rgba(11,16,24,.18);backdrop-filter:blur(5px);-webkit-backdrop-filter:blur(5px);box-shadow:0 5px 20px #0000000C;white-space:nowrap;opacity:0}
.screen[data-active-theme=midnight] .caption-box{background:rgba(23,40,50,.30)}
.screen[data-active-theme=ivory] .caption-box{background:rgba(11,16,24,.10)}
.caption-words{display:flex;align-items:center;justify-content:center;gap:14px;white-space:nowrap;max-width:100%;overflow:hidden}
.word{display:inline-block;white-space:nowrap;color:#FFF7EB;text-shadow:0 1px 5px #0B101878;font:700 57px/1.25 Manrope,Arial,sans-serif;transform-origin:center 65%;opacity:0}
.screen[data-active-theme=ivory] .word{color:#283039}.word.active{color:#FFBE91!important}.screen[data-active-theme=ivory] .word.active{color:#A63F17!important}
.progress{position:absolute;z-index:15;bottom:262px;left:84px;right:165px;height:10px;display:flex;gap:14px}
.segment{flex:1;background:var(--bar);border-radius:16px;overflow:hidden}.segment i{height:100%;background:var(--progress);width:0;display:block;border-radius:16px}
/* A designed diagonal accent WIPE, not a background cut. Only visible at chapter boundaries. */
.scene-wipe{position:absolute;z-index:34;left:0;top:0;width:1080px;height:1920px;pointer-events:none;opacity:0;overflow:hidden}
.scene-wipe .slash{position:absolute;left:-350px;top:-150px;height:2250px;width:300px;transform:translateX(0) skewX(-15deg);background:linear-gradient(90deg,#117A7AE0 0%,#E8752EE8 30%,#E8752E 76%,#FFF7EBBF 100%);box-shadow:0 0 55px #E8752E44}
.scene-wipe .fine{position:absolute;left:0;top:0;bottom:0;width:6px;background:#FFF7EBB0}
.panel{padding:25px 26px 23px;background:#FFFDF9;border:1px solid #E5D9CE;border-radius:20px;box-shadow:0 15px 35px #0000000B}
.panel h2{font:800 20px Sora,Arial,sans-serif;margin:0 0 8px}.panel p{font-size:13px;line-height:1.6;color:#56616B;margin:0 0 20px}
.controls{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin:12px 0 20px}button,select{padding:10px 12px;border:1px solid #D9D5CD;background:#F8F5F0;border-radius:10px;font:700 12px Manrope,Arial,sans-serif;cursor:pointer;color:#283039}.primary{background:#0B1018;color:#FFF7EB;border-color:#0B1018}input[type=range]{width:100%;accent-color:#E8752E}.readout{display:flex;justify-content:space-between;font-size:12px;color:#627178;margin-top:7px}.marker{font-size:11px;color:#6A6F74}
.option{border-top:1px solid #EDE4DC;padding:15px 0;font-size:13px;line-height:1.5;color:#47555D}.option strong{color:#283039}.note{font-size:12px;line-height:1.55;color:#72787B;margin:14px 0 0}
@media(max-width:800px){.wrap{grid-template-columns:1fr;padding:18px 12px;gap:18px}.intro{grid-column:1}.viewport{max-width:420px;margin:auto}.panel{max-width:560px;margin:auto;width:100%}}
@media(prefers-reduced-motion:reduce){.glow{transform:none!important}}
'''
js=r'''(()=>{
'use strict';
const scenes=__SCENES__, TOTAL=16, TRANSITION=.64, START_EARLY=.24;
const wrap=document.getElementById('stage'), view=document.getElementById('viewport');
const wipe=document.getElementById('wipe');
let now=0,playing=false,last=null,speed=1,mode='__PRESET__',currentScene=-1;
const btn=document.getElementById('play'),seek=document.getElementById('seek');
const clamp=(x)=>Math.max(0,Math.min(1,x));
const ease=(x)=>1-(1-clamp(x))**3;
const spring=(age)=>{const p=clamp(age/.2); if(p<=.6){const q=p/.6;return .6+.52*(1-(1-q)**2);}const q=(p-.6)/.4;return 1.12-.12*(1-(1-(p-.6)/.4)**2);};
function addWordSchedules(){for(const s of scenes){const words=s.groups.flatMap(g=>g.trim().split(/\s+/));const weights=words.map(w=>Math.max(2.7,Math.min(8.5,w.length)));const total=weights.reduce((a,b)=>a+b,0);let t=s.from+.24;const usable=(s.to-s.from)-.52;s.words=words.map((word,i)=>{const start=t;t+=weights[i]/total*usable;return {word,start,end:t};});let at=0;s.ranges=s.groups.map(g=>{const count=g.trim().split(/\s+/).length;const range={start:at,end:at+count};at+=count;return range;});}}
addWordSchedules();
const layers=[...document.querySelectorAll('.scene')];
function measureScale(){wrap.style.transform='scale('+(view.clientWidth/1080)+')';}
if(window.ResizeObserver)new ResizeObserver(measureScale).observe(view);else window.addEventListener('resize',measureScale);measureScale();
const captionBox=wrap.querySelector('.caption-box'),captionTrack=wrap.querySelector('.caption-words');
let shownBeat=-1,shownGroup=-1,visibleNodes=[];
function activeSceneAt(t){return t<5?0:t<10.5?1:2;}
function sceneVisual(t,i){const s=scenes[i];let p=1,visible=true,x=0;
  // Incoming starts slightly BEFORE the boundary, outgoing lasts briefly AFTER.
  if(i>0){const enter=clamp((t-(s.from-START_EARLY))/TRANSITION);p=ease(enter);x=150*(1-p);if(t<s.from-START_EARLY)visible=false;}
  if(i<scenes.length-1){const boundary=s.to;const q=clamp((t-(boundary-START_EARLY))/TRANSITION);p*=1-ease(q);x-=110*ease(q);if(t>boundary+TRANSITION-START_EARLY)visible=false;}
  return {opacity:visible?p:0,x};
}
function updateCaptions(t){
 const beat=activeSceneAt(t),s=scenes[beat];
 let latest=-1;for(let i=0;i<s.words.length;i++)if(t>=s.words[i].start)latest=i;
 if(latest<0){captionBox.style.opacity='0';return;}
 const group=s.ranges.findIndex(r=>latest>=r.start&&latest<r.end);
 if(group<0){captionBox.style.opacity='0';return;}
 const range=s.ranges[group];
 if(shownBeat!==beat||shownGroup!==group){
  shownBeat=beat;shownGroup=group;captionTrack.replaceChildren();visibleNodes=[];
  for(let i=range.start;i<range.end;i++){
   const el=document.createElement('span');el.className='word';el.textContent=s.words[i].word;
   captionTrack.appendChild(el);visibleNodes.push(el);
  }
 }
 visibleNodes.forEach((node,k)=>{
  const word=s.words[range.start+k],age=t-word.start,vis=age>=0;
  node.style.display=vis?'inline-block':'none';
  node.style.opacity=vis?String(clamp(age/.2)):'0';
  node.style.transform='scale('+spring(age)+')';
  node.classList.toggle('active',vis&&t<word.end);
 });
 const start=s.words[range.start].start;
 captionBox.style.opacity=String(clamp((t-start)/.12));
 // Fit the actual glyph widths to a maximum of 800px, symmetric safe margin 140px.
 visibleNodes.forEach(el=>{el.style.fontSize='57px'});
 if(captionTrack.scrollWidth>710){const font=Math.max(41,Math.floor(57*710/captionTrack.scrollWidth));visibleNodes.forEach(el=>{el.style.fontSize=font+'px'})}
}
function draw(){const sceneId=activeSceneAt(now);
 wrap.dataset.activeTheme=mode==='dynamic'?scenes[sceneId].theme:mode;
 scenes.forEach((s,i)=>{
  const layer=layers[i],vis=sceneVisual(now,i),local=now-s.from;
  layer.style.opacity=String(vis.opacity);
  layer.style.transform='translateX('+vis.x+'px)';
  layer.style.visibility=vis.opacity<=0.001?'hidden':'visible';
  layer.dataset.theme=mode==='dynamic'?s.theme:mode;
  const kicker=layer.querySelector('.kicker'),typed=layer.querySelector('.typed'),heading=layer.querySelector('.heading-wrapper');
  const kp=ease((local+.10)/.55),hp=ease((local+.05)/.54);
  kicker.style.opacity=String(kp);kicker.style.transform='translateX('+((1-kp)*90)+'px)';
  heading.style.opacity=String(hp);heading.style.transform='translateX('+((1-hp)*106)+'px) translateY('+((1-hp)*9)+'px)';
  const chars=Math.min(s.headline.length,Math.max(0,Math.floor(Math.max(0,local+.09)*25)));
  typed.textContent=s.headline.slice(0,chars);
  const hero=layer.querySelector('.hero'),ep=ease((local-.1)/.74);
  hero.style.opacity=String(ep);hero.style.transform='translateX('+((1-ep)*142)+'px) translateY('+((1-ep)*16)+'px)';
  layer.querySelectorAll('.rack').forEach((r,j)=>{const p=ease((local-.20-j*.42)/.63);r.style.transform='translateX('+((1-p)*-82)+'px)';r.style.opacity=String(.15+.85*p)});
  layer.querySelector('.flow i').style.width=(100*ease((local-.6)/3.2))+'%';
  layer.querySelector('.glow').style.transform='translateX('+Math.sin(now*.6)*40+'px)';

 });
 updateCaptions(now);
 // Two animated transition washes precisely at 5s and 10.5s.
 let best=-1;
 for(const boundary of [5,10.5]){const p=(now-(boundary-START_EARLY))/TRANSITION;if(p>=0&&p<=1){best=p;break;}}
 wipe.style.opacity=best>=0?String(Math.sin(Math.PI*best)*.62):'0';
 wipe.querySelector('.slash').style.transform='translateX('+(-260+1660*best)+'px) skewX(-15deg)';
 const progresses=[0,5,10.5,16];
 wrap.querySelectorAll('.progress .segment i').forEach((el,i)=>el.style.width=(100*clamp((now-progresses[i])/(progresses[i+1]-progresses[i])))+'%');
 seek.value=now;
 document.getElementById('readout').textContent=now.toFixed(2)+' / 16.00 sec';
 document.getElementById('chapter').textContent='Scene '+(sceneId+1)+' / 3';
}
function tick(ts){if(!playing)return;if(last!=null)now=Math.min(TOTAL,now+(ts-last)/1000*speed);last=ts;draw();if(now>=TOTAL){playing=false;btn.textContent='▶ Play';}else requestAnimationFrame(tick)}
btn.addEventListener('click',()=>{playing=!playing;last=null;if(playing&&now>=TOTAL)now=0;btn.textContent=playing?'❚❚ Pause':'▶ Play';draw();if(playing)requestAnimationFrame(tick)});
document.getElementById('restart').addEventListener('click',()=>{now=0;last=null;draw()});
seek.addEventListener('input',()=>{now=Number(seek.value);last=null;draw()});
document.getElementById('speed').addEventListener('change',e=>{speed=Number(e.target.value);last=null});
[...document.querySelectorAll('[data-mode]')].forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.mode;document.querySelectorAll('[data-mode]').forEach(el=>el.setAttribute('aria-pressed',String(el===b)));draw()}));
document.querySelectorAll('[data-jump]').forEach(el=>el.addEventListener('click',()=>{now=Number(el.dataset.jump);last=null;draw()}));
const preset=new URLSearchParams(window.location.search).get('theme');if(['ivory','midnight','dynamic'].includes(preset)){mode=preset;document.querySelectorAll('[data-mode]').forEach(el=>el.setAttribute('aria-pressed',String(el.dataset.mode===mode)))}
window.BharatModePreviewV5={draw,setTime:(t)=>{now=Math.max(0,Math.min(16,Number(t)));last=null;draw()},getState:()=>({now,mode})};
window.addEventListener('keydown',e=>{if(e.code==='Space'&&!['INPUT','BUTTON','SELECT'].includes(document.activeElement?.tagName)){e.preventDefault();btn.click()}});
draw();
})();
'''

def scene_markup(b,i):
 racks=''.join('<div class="rack">'+''.join('<i></i>' for _ in range(5))+'</div>' for _ in range(3))
 label=html.escape(b['label'])
 topic='' 
 return f'''<div class="scene" id="scene-{i}" data-theme="{b['theme']}">
   <div class="soft-orbit"></div><div class="glow"></div>{topic}
   <div class="kicker">{html.escape(b['kicker'])}</div>
   <div class="heading-wrapper"><div class="typed" aria-label="{html.escape(b['headline'].replace(chr(10),' '))}"></div></div>
   <div class="hero"><div class="hero-kicker">{label}</div><div class="racks">{racks}</div><div class="flow"><i></i></div></div>
 </div>'''

def create(name,preset='dynamic'):
 source=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Bharat Mode — Directional Scenes & Centered Captions · V5</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700&family=Sora:wght@800&display=swap" rel="stylesheet"/>
<style>{styles}</style></head><body><main class="wrap">
<header class="intro"><div class="eyebrow">BHARAT MODE / MOTION V5 / REVIEW PROOF</div><h1>Typewriter headlines + directional entrances + real scene transitions</h1><p>Three editorial scenes with a 0.64-second overlapping diagonal wipe and slide. The text block itself enters from the right while characters type. Hero graphics begin higher. Each caption group is fixed at screen center—even while the scenes themselves move—and stays inside generous side margins.</p></header>
<div class="viewport" id="viewport"><div class="screen" id="stage">
{''.join(scene_markup(b,i) for i,b in enumerate(beats))}
<div class="header"><img src="data:image/svg+xml;base64,{logo}" alt="Official Bharat Mode avatar"/><div class="pill">SCIENCE</div></div>
<div class="captions"><div class="caption-box"><div class="caption-words"></div></div></div>
<div class="progress">{''.join('<div class="segment"><i></i></div>' for _ in beats)}</div>
<div class="scene-wipe" id="wipe"><div class="slash"><div class="fine"></div></div></div>
</div></div>
<section class="panel"><h2>Watch the transitions</h2><p>Play or jump to 4.9 and 10.4 seconds to see the previous scene slide out, the next slide in, and the diagonal saffron/teal wipe. Typewriter and grouped word-pop captions are retained.</p>
<div class="controls"><button type="button" id="play" class="primary">▶ Play</button><button type="button" id="restart">↺ Replay</button><select id="speed"><option value="0.75">0.75×</option><option value="1" selected>1×</option><option value="1.25">1.25×</option></select></div>
<label style="display:block;font-size:11px;font-weight:800;letter-spacing:1px;color:#637078;margin:20px 0 8px">SCRUB THE STORY</label>
<input id="seek" type="range" min="0" max="16" value="0" step=".02" aria-label="Scrub the animated scenes"/>
<div class="readout"><span id="readout">0 / 16 sec</span><span id="chapter">Scene 1 / 3</span></div>
<div class="controls" style="margin-top:15px"><button type="button" data-jump="4.92">Transition 1 → 2</button><button type="button" data-jump="10.42">Transition 2 → 3</button></div>
<div class="option"><strong>Headlines:</strong> typewriter with no cursor, and the <em>entire headline block</em> slides from right to left as it types.</div>
<div class="option"><strong>Hero:</strong> raised 143px (top 777 instead of 920), sliding in from the right; server racks enter in sequence; teal-to-saffron line grows.</div>
<div class="option"><strong>Captions:</strong> compact, lightly translucent box centered at screen x=540; safe left/right margins; one phrase group at a time; 200ms 60%→112%→100% word pop, active-word color only.</div>
<div class="option"><strong>Between scenes:</strong> a 0.64s overlapping exit/entry with directional motion and a brief diagonal brand-color wipe.</div>
<div class="option"><strong>Topic pill:</strong> light Manrope Medium, fixed on the right. Chapter progress stays subtle.</div>
<p class="note">This is a silent browser motion proof. Caption word timestamps are simulated for review—not aligned to narration. No real device imagery is claimed; server racks are illustrations. The exact approved BM avatar is embedded in the document.</p>
</section></main>
<script>{js.replace('__SCENES__',json.dumps(beats,separators=(',',':'))).replace('__PRESET__',preset)}</script></body></html>'''
 path=out/name
 path.write_text(source,encoding='utf-8')
 print(path,len(source))
 return path
for name,preset in [('bharat-mode-motion-v5-mixed.html','dynamic'),('bharat-mode-motion-v5-ivory.html','ivory'),('bharat-mode-motion-v5-dark.html','midnight')]:create(name,preset)