from pathlib import Path
import base64
from textwrap import dedent
PROJECT=Path(__file__).resolve().parents[1]
root=PROJECT/'previews'/'html'
root.mkdir(parents=True,exist_ok=True)
logo=(PROJECT/'public'/'brand'/'bharat-mode-avatar.svg').read_bytes()
encoded=base64.b64encode(logo).decode('ascii')
html=r'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Bharat Mode · Typewriter & word-follow caption motion preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Manrope:wght@500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{color-scheme:light;--ivory:#FFF7EB;--saffron:#E8752E;--teal:#117A7A;--charcoal:#0B1018;--graphite:#283039}
*{box-sizing:border-box}
body{margin:0;background:#F5F0E9;color:#283039;font-family:'Manrope',sans-serif;-webkit-font-smoothing:antialiased}
.page{max-width:1080px;padding:22px 20px 60px;margin:auto;display:grid;grid-template-columns:minmax(330px,420px) minmax(300px,1fr);align-items:start;gap:30px}
.intro{grid-column:1/-1}
.eyebrow{font-weight:800;font-size:11px;letter-spacing:.2em;color:#A63F17}
h1{font-family:'Sora',sans-serif;font-size:clamp(21px,2.8vw,31px);letter-spacing:-.04em;line-height:1.25;margin:8px 0}
.lead{margin:7px 0;color:#626C72;line-height:1.55;font-size:14px;max-width:800px}
.preview{position:relative;width:100%;aspect-ratio:9/16;border-radius:19px;overflow:hidden;box-shadow:0 25px 65px rgba(11,16,24,.16);background:var(--charcoal)}
.stage{width:1080px;height:1920px;position:absolute;top:0;left:0;transform-origin:0 0;overflow:hidden;isolation:isolate;color:var(--charcoal);background:var(--ivory);--headline:var(--graphite);--caption:#FFF7EB;--muted:#7E8586;--active:#FFA45D;--track:#DAD4CC;--fill:var(--saffron);--glass:linear-gradient(180deg,rgba(255,247,235,0) 0%,rgba(255,247,235,.92) 57%,#FFF7EB 100%)}
.stage[data-theme=midnight]{background:var(--charcoal);--headline:var(--ivory);--caption:var(--ivory);--muted:#9FB1B7;--active:#FFBE91;--track:#3E4D55;--fill:var(--saffron);--glass:linear-gradient(180deg,rgba(11,16,24,0) 0%,rgba(11,16,24,.87) 48%,#0B1018 100%)}
.stage[data-theme=saffron]{background:#E8752E;--headline:#0B1018;--caption:#FFF7EB;--muted:#ADBEC3;--active:#FFA45D;--track:#42505A;--fill:#FFBE91;--glass:linear-gradient(180deg,rgba(11,16,24,0) 0%,rgba(11,16,24,.83) 48%,#0B1018 100%)}
.bg-waves{position:absolute;inset:0;pointer-events:none;z-index:0;opacity:.85}
.bg-waves .glow{position:absolute;width:850px;height:850px;border-radius:50%;left:540px;top:510px;background:radial-gradient(circle,#FFC99C 0%,transparent 72%);opacity:.28;animation:drift 7s ease-in-out infinite alternate}
.bg-waves .stripe{position:absolute;left:-330px;top:1180px;border:55px solid #117A7A17;width:1100px;height:760px;transform:rotate(-22deg);border-radius:50%}
.stage[data-theme=midnight] .bg-waves .glow{background:radial-gradient(circle,#117A7A 0%,transparent 70%);opacity:.23}
.stage[data-theme=saffron] .bg-waves .glow{background:radial-gradient(circle,#FFF7EB 0%,transparent 70%);opacity:.3}
@keyframes drift{from{transform:translate3d(0,0,0)}to{transform:translate3d(-40px,28px,0)}}
.top{position:absolute;top:88px;left:85px;right:72px;z-index:9;display:flex;align-items:center;justify-content:space-between}
.logo{width:92px;height:92px;object-fit:contain}
.topic{font-size:26px;letter-spacing:2.1px;line-height:1;font-weight:500;padding:21px 32px;border-radius:42px;white-space:nowrap;color:var(--ivory);background:var(--charcoal)}
.stage[data-theme=midnight] .topic{background:var(--ivory);color:var(--charcoal)}
.head-zone{position:absolute;z-index:6;top:325px;left:86px;right:166px}
.kicker{font-size:27px;font-weight:800;letter-spacing:2.4px;line-height:1.3;color:var(--headline);opacity:.75;text-transform:uppercase}
.headline{font-family:'Sora',sans-serif;font-size:91px;letter-spacing:-4px;font-weight:800;line-height:1.18;color:var(--headline);margin-top:48px;min-height:360px;white-space:pre-line;overflow-wrap:break-word}
.headline .typed{white-space:pre-line}
.abstract-evidence{position:absolute;z-index:5;left:80px;right:166px;top:920px;height:500px;border-radius:46px;background:#0D1B25E8;border:2px solid #6DB0B021;overflow:hidden}
.abstract-evidence:before{content:'';position:absolute;inset:0;background:radial-gradient(circle at 50% 110%,#1F6D70 0%,transparent 69%);opacity:.48}
.abstract-evidence .evidence-label{position:absolute;left:48px;top:38px;font:800 25px 'Manrope',sans-serif;letter-spacing:2px;color:#F8BB88}
.racks{position:absolute;top:116px;left:83px;display:flex;gap:37px;align-items:center}
.rack{width:180px;height:260px;border-radius:24px;background:linear-gradient(130deg,#263F48,#0E1A23);border:3px solid #4F7379;box-shadow:0 18px 40px rgba(0,0,0,.17);padding:22px;display:flex;flex-direction:column;gap:12px;opacity:.45;transform:translateX(-34px);transition:transform 480ms cubic-bezier(.22,1,.36,1),opacity 480ms ease}
.rack.active{opacity:1;transform:translateX(0)}
.rack i{height:25px;background:#263E46;border:2px solid #507D7D;border-radius:5px;position:relative}
.rack i:after{content:'';position:absolute;right:6px;top:6px;width:8px;height:8px;border-radius:50%;background:#70D3CC}
.flow-line{position:absolute;left:130px;right:130px;bottom:58px;height:9px;background:#8FC2C12C;border-radius:10px;overflow:hidden}
.flow-line .flow-fill{width:0;height:100%;background:linear-gradient(90deg,#117A7A,#E8752E);transition:width 160ms linear}
.signal{position:absolute;z-index:2;width:145px;height:145px;right:0;top:0;border:2px solid #117A7A35;transform:rotate(45deg) translateX(15px);border-radius:22px;opacity:.65}
/* Consistent semi-transparent dark stripe, NOT a rounded caption pill. */
.caption-space{position:absolute;z-index:12;left:0;right:0;top:1435px;height:185px;background:rgba(11,16,24,.79);pointer-events:none}
.stage[data-theme=midnight] .caption-space{background:rgba(24,34,43,.89)}
.stage[data-theme=saffron] .caption-space{background:rgba(11,16,24,.75)}
.caption-line{position:absolute;top:39px;left:80px;right:166px;height:104px;overflow:hidden;-webkit-mask-image:linear-gradient(to right,transparent,#000 2%,#000 98%,transparent);mask-image:linear-gradient(to right,transparent,#000 2%,#000 98%,transparent)}
.caption-track{position:absolute;white-space:nowrap;display:flex;gap:17px;align-items:center;height:101px;transform:translateX(0);transition:transform 205ms cubic-bezier(.2,.8,.2,1);will-change:transform}
.caption-word{font-family:'Manrope',sans-serif;font-weight:700;font-size:60px;line-height:1.22;color:var(--caption);opacity:0;position:relative;transform:scale(.6);transform-origin:50% 65%;white-space:nowrap;will-change:transform,opacity}
.caption-word.spoken{color:var(--caption);opacity:1}
.caption-word.active{color:var(--active);opacity:1}
.evidence-enter{transition:none;will-change:opacity,transform}
.kicker{will-change:opacity,transform}
.progress{position:absolute;z-index:14;left:84px;right:167px;bottom:266px;height:11px;display:flex;gap:14px}
.progress .segment{flex:1;border-radius:12px;background:var(--track);overflow:hidden}
.progress .segment i{display:block;height:100%;width:0;background:var(--fill);border-radius:12px}
.controls{background:white;border:1px solid #E6DDD3;border-radius:20px;padding:23px;box-shadow:0 12px 36px #1019280C}
.controls h2{font:800 19px 'Sora',sans-serif;letter-spacing:-.04em;margin:0 0 8px}
.controls p{font-size:13px;line-height:1.65;color:#667176;margin:0 0 20px}
.row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:17px}
button,select{font:700 12px 'Manrope',sans-serif;border:1px solid #D9D9D6;border-radius:11px;padding:11px 13px;background:#F7F7F5;color:#283039;cursor:pointer}
button:hover,select:hover{border-color:#E8752E}
button.primary{background:#0B1018;color:white;border-color:#0B1018}
label{display:block;font:800 11px 'Manrope',sans-serif;letter-spacing:.09em;color:#59666C;margin:18px 0 9px}
input[type=range]{accent-color:#E8752E;width:100%;cursor:pointer}
.readout{display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#627178;font-variant-numeric:tabular-nums}
.chips{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px}
.chip{font-size:11px;padding:11px 5px}
.chip[aria-pressed=true]{background:#0B1018;color:white;border-color:#0B1018}
.option{padding:15px 0;border-top:1px solid #ECE9E5;font-size:13px;line-height:1.6;color:#4D5A60}
.option strong{color:#25323B}
.note{font-size:12px;line-height:1.6;color:#65737B;margin:13px 0 0}
.downloads{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.downloads a{background:#FFF7EB;border:1px solid #E5D7CB;border-radius:10px;color:#283039;padding:10px 13px;text-decoration:none;font:700 12px Manrope,sans-serif}
@media(max-width:780px){.page{grid-template-columns:minmax(0,1fr);gap:18px;padding:17px 13px}.preview{max-width:390px;margin:auto}.intro{grid-column:1}.controls{max-width:560px;width:100%;margin:auto}}
@media(prefers-reduced-motion:reduce){.bg-waves .glow{animation:none}.rack,.caption-track,.caption-word{transition:none}}
</style>
</head><body>
<main class="page">
 <header class="intro"><div class="eyebrow">BHARAT MODE / MOTION SYSTEM V2 / REVIEW ONLY</div><h1>Typewriter headlines. Spring-pop word captions.</h1><p class="lead">Directional composition with a single-line, scrolling spoken-word highlight. Captions use a <strong>semi-transparent dark rectangular overlay</strong>, with a spring-pop on each new word and a temporarily highlighted spoken word. The headline has no cursor. Preview timing is illustrative until a real voice track is aligned.</p></header>
 <div class="preview" id="preview"><div class="stage" id="stage" data-theme="saffron">
  <div class="bg-waves"><div class="glow"></div><div class="stripe"></div></div>
  <div class="top"><img class="logo" src="data:image/svg+xml;base64,___AVATAR___" alt="Approved BM logo"><span class="topic">SCIENCE</span></div>
  <div class="head-zone"><div class="kicker" id="kicker">THE RESEARCH BACKBONE</div><div class="headline"><span id="typed" class="typed"></span></div></div>
  <div class="abstract-evidence" id="evidence-enter"><div class="signal"></div><div class="evidence-label" id="evidence-label">RUDRA / PROCESS</div><div class="racks" id="racks"><div class="rack" id="rack0"><i></i><i></i><i></i><i></i><i></i></div><div class="rack" id="rack1"><i></i><i></i><i></i><i></i><i></i></div><div class="rack" id="rack2"><i></i><i></i><i></i><i></i><i></i></div></div><div class="flow-line"><div class="flow-fill" id="flow-fill"></div></div></div>
  <div class="caption-space"><div class="caption-line" id="caption-line"><div class="caption-track" id="caption-track"></div></div></div>
  <div class="progress"><div class="segment"><i id="seg0"></i></div><div class="segment"><i id="seg1"></i></div><div class="segment"><i id="seg2"></i></div></div>
 </div></div>
 <section class="controls" aria-label="Playback controls">
  <h2>Try the motion</h2><p>Play, pause, scrub or change the background treatment. Typewriter headlines have no cursor. Each spoken word pops in at 60% size, briefly overshoots and settles while the active word changes color. Diagram motion is preserved.</p>
  <div class="row"><button type="button" class="primary" id="play">▶ Play</button><button type="button" id="restart">↺ Restart</button><select id="speed" aria-label="Playback speed"><option value="0.75">0.75× speed</option><option value="1" selected>1× speed</option><option value="1.25">1.25× speed</option></select></div>
  <label for="timeline">REVIEW THE TIMELINE</label><input id="timeline" type="range" min="0" max="16" value="0" step="0.02" aria-label="Scrub preview"/><div class="readout"><span id="time">0.0 / 16.0 sec</span><span id="chapter">Chapter 1 of 3 (demo only)</span></div>
  <label>BACKGROUND / CONTRAST</label><div class="chips"><button class="chip" type="button" data-mode="dynamic" aria-pressed="true">Mixed themes</button><button class="chip" type="button" data-mode="ivory" aria-pressed="false">Ivory</button><button class="chip" type="button" data-mode="midnight" aria-pressed="false">Charcoal</button></div>
  <div class="option"><strong>Typewriter:</strong> headlines reveal character by character with <strong>no cursor</strong>. The rest of the directional transitions and diagram choreography are preserved.</div>
  <div class="option"><strong>Captions:</strong> one moving line, <strong>60px Manrope</strong>, semitransparent dark rectangular backing. Every word enters from 60% scale, springs up with a small overshoot, then stays fully legible in the normal color; only the word being spoken temporarily changes to saffron.</div>
  <div class="option"><strong>Topic tag:</strong> kept near the right edge and reduced to Manrope Medium (500), rather than bold.</div>
  <p class="note">This is a browser-based motion proof, not a finished Short. The timed words are simulated for review and are <em>not yet synchronized to an actual voice recording</em>. Production will use word timestamps aligned to the narration audio.</p>
 </section>
</main>
<script>
(function(){
'use strict';
const TOTAL=16;
const BEATS=[
 {start:0,end:5,title:'Built for\\nbreakthroughs.',kicker:'THE RESEARCH BACKBONE',evidence:'DESIGN → MANUFACTURE → DEPLOY',caption:'India is building powerful computers to support scientific research.'},
 {start:5,end:10.5,title:'6,000 Rudra\\nservers.',kicker:'ALREADY DEPLOYED',evidence:'PARAM RUDRA / SERVER SYSTEMS',caption:'Six thousand Rudra servers were deployed by September twenty twenty six.'},
 {start:10.5,end:16,title:'More power.\\nMore possibilities.',kicker:'WHY IT MATTERS',evidence:'RESEARCH / SCIENCE / COMPUTING',caption:'That computing power can support weather materials and biomedical science.'}
];
const stage=document.getElementById('stage');
const preview=document.getElementById('preview');
const track=document.getElementById('caption-track');
const windowEl=document.getElementById('caption-line');
const timeEl=document.getElementById('time');
const chapterEl=document.getElementById('chapter');
const titleEl=document.getElementById('typed');
const topicModes=[...document.querySelectorAll('.chip')];
const play=document.getElementById('play');
const timeline=document.getElementById('timeline');
let sec=0,playing=false,lastTick=null,speed=1,mode='dynamic',beatIndex=-1,activeIndex=-1,wordEls=[],wordSchedule=[];
function resize(){const s=preview.clientWidth/1080;stage.style.transform='scale('+s+')';}
if(window.ResizeObserver)new ResizeObserver(resize).observe(preview);else window.addEventListener('resize',resize);resize();
function beatFor(t){return t<BEATS[1].start?0:t<BEATS[2].start?1:2;}
function themeFor(i){return mode==='dynamic'?(['saffron','midnight','ivory'][i]):mode;}
function chapterTime(i){return Math.max(0,Math.min(BEATS[i].end-BEATS[i].start,sec-BEATS[i].start));}
function wordsFor(beat){const words=beat.caption.trim().split(/\s+/);
 let durations=words.map(w=>Math.max(.23,Math.min(.72,.14+w.length*.058)));
 const freeTime=(beat.end-beat.start)-.65;
 const factor=freeTime/durations.reduce((a,b)=>a+b,0);
 let t=.18;return words.map((w,i)=>{const start=t;t+=durations[i]*factor;return {text:w,start,end:t};});
}
function buildCaptions(i){const b=BEATS[i];wordSchedule=wordsFor(b);track.replaceChildren();wordEls=wordSchedule.map((w,j)=>{
 const span=document.createElement('span');span.className='caption-word';span.textContent=w.text;span.dataset.index=String(j);track.appendChild(span);return span;});activeIndex=-1;}
// Fixed 200ms word entrance. p=.0 => 60%; p=.60 => 110%; p=1 => 100%.
function popScale(age){
 const p=Math.max(0,Math.min(1,age/.2));
 if(p<=.6){const z=p/.6;return .6+.52*(1-Math.pow(1-z,2));}
 const z=(p-.6)/.4;return 1.12-.12*(1-Math.pow(1-z,2));
}
function updateCaption(local){
 if(!wordSchedule.length)return;
 let current=-1;
 for(let i=0;i<wordSchedule.length;i++)if(local>=wordSchedule[i].start)current=i;
 // Center latest word while retaining previously spoken words at full normal opacity.
 if(current!==activeIndex){
  activeIndex=current;
  const target=wordEls[Math.max(0,current)];
  const ideal=windowEl.clientWidth/2-target.offsetLeft-target.offsetWidth/2;
  track.style.transform='translateX('+ideal+'px)';
 }
 wordEls.forEach((el,i)=>{
  const w=wordSchedule[i],age=local-w.start,visible=age>=0;
  const speaking=visible&&local<w.end;
  el.className='caption-word'+(speaking?' active':visible?' spoken':'');
  el.style.visibility=visible?'visible':'hidden';
  el.style.opacity=visible?String(Math.max(0,Math.min(1,age/.19))):'0';
  el.style.transform='scale('+popScale(age)+')';
 });
}
function draw(){
 const i=beatFor(sec),b=BEATS[i],local=chapterTime(i);
 if(i!==beatIndex){beatIndex=i;buildCaptions(i);}
 stage.dataset.theme=themeFor(i);
 document.getElementById('kicker').textContent=b.kicker;
 document.getElementById('evidence-label').textContent=b.evidence;
 const title=b.title.replaceAll('\\n','\n');
 const count=Math.max(0,Math.min(title.length,Math.floor(Math.max(0,local-.06)*26)));
 titleEl.textContent=title.slice(0,count);
 // Keep earlier directional stage entrances; typewriter applies only to headline.
 const kicker=document.getElementById('kicker');
 const kp=Math.max(0,Math.min(1,local/.55));
 kicker.style.transform='translateX('+((1-kp)*48)+'px)';
 kicker.style.opacity=String(kp);
 const ev=document.getElementById('evidence-enter');
 const ep=Math.max(0,Math.min(1,(local-.30)/.7));
 const ease=1-Math.pow(1-ep,3);
 ev.style.transform='translate('+((1-ease)*74)+'px,'+((1-ease)*18)+'px)';
 ev.style.opacity=String(ease);

 for(let j=0;j<3;j++){
  const rack=document.getElementById('rack'+j);
  const show=Math.max(0,Math.min(1,(local-.5-j*.48)/.6));
  rack.style.opacity=String(.25+.75*show);
  rack.style.transform='translateX('+((1-show)*(-38))+'px)';
  const fill=document.getElementById('seg'+j);
  fill.style.width=(100*Math.max(0,Math.min(1,(sec-BEATS[j].start)/(BEATS[j].end-BEATS[j].start))))+'%';
 }
 document.getElementById('flow-fill').style.width=(Math.min(1,Math.max(0,(local-1)/3.4))*100)+'%';
 updateCaption(local);
 timeline.value=String(sec);
 timeEl.textContent=sec.toFixed(1)+' / '+TOTAL.toFixed(1)+' sec';
 chapterEl.textContent='Chapter '+(i+1)+' of 3 (demo only)';
}
function tick(ts){if(playing){if(lastTick!==null)sec=Math.min(TOTAL,sec+(ts-lastTick)/1000*speed);if(sec>=TOTAL){playing=false;play.textContent='▶ Play';lastTick=null;}else{lastTick=ts;}}draw();if(playing)requestAnimationFrame(tick);}
function toggle(){playing=!playing;lastTick=null;play.textContent=playing?'❚❚ Pause':'▶ Play';if(playing){if(sec>=TOTAL)sec=0;requestAnimationFrame(tick)}}
play.addEventListener('click',toggle);
document.getElementById('restart').addEventListener('click',()=>{sec=0;beatIndex=-1;lastTick=null;draw();if(playing)requestAnimationFrame(tick)});
timeline.addEventListener('input',e=>{sec=Number(e.target.value);lastTick=null;draw()});
document.getElementById('speed').addEventListener('change',e=>{speed=Number(e.target.value);lastTick=null});
topicModes.forEach(button=>button.addEventListener('click',()=>{mode=button.dataset.mode;topicModes.forEach(b=>b.setAttribute('aria-pressed',String(b===button)));draw()}));
window.addEventListener('keydown',e=>{if(e.code==='Space'&&!['BUTTON','INPUT','SELECT'].includes(document.activeElement?.tagName)){e.preventDefault();toggle()}});
const params=new URLSearchParams(location.search);const preset=params.get('theme');
if(['dynamic','ivory','midnight'].includes(preset)){mode=preset;topicModes.forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.mode===mode)))}
draw();
})();
</script>
</body></html>'''
html=html.replace('___AVATAR___',encoded)
for name in ['bharat-mode-motion-v3-mixed.html','bharat-mode-motion-v3-ivory.html','bharat-mode-motion-v3-dark.html']:
 s=html
 if 'ivory' in name:s=s.replace("const preset=params.get('theme');", "const preset=params.get('theme')||'ivory';")
 if 'dark' in name:s=s.replace("const preset=params.get('theme');", "const preset=params.get('theme')||'midnight';")
 (root/name).write_text(s,encoding='utf-8')
print([(p.name,p.stat().st_size) for p in root.glob('bharat-mode-motion-v3-*.html')])