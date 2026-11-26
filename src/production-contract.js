// Pure production contract: no estimated audio, no implicit story assets.
import {validateAlignedWords} from './aligned-caption-timing.js';
import {resolveStoryChapters} from './chapter-timing.js';
export const FPS=60, WIDTH=1080, HEIGHT=1920, HOLD_FRAMES=60;
export const MUSIC_SHA='adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9';
const digest=x=>typeof x==='string'&&/^[0-9a-f]{64}$/.test(x);
const require=(ok,msg)=>{if(!ok)throw new Error(msg);};
const pathOK=p=>typeof p==='string'&&/^production-private\/[a-zA-Z0-9_./-]+$/.test(p)&&!p.split('/').some(x=>x==='..'||x==='.'||!x);
const finite=x=>Number.isFinite(x);
export const clamp01=x=>Math.max(0,Math.min(1,x));
export const ease=x=>{const t=clamp01(x);return t*t*(3-2*t)};
export const typed=(text,sec)=>Array.from(String(text)).slice(0,Math.max(0,Math.floor(sec*19)+1)).join('');
export const leadCue=word=>Math.max(0,word.start-.35);
const validColor=x=>typeof x==='string'&&(/^#[0-9a-f]{6}$/i.test(x)||x==='none');
const words=s=>(String(s).match(/[\p{L}\p{N}]+(?:['’\-][\p{L}\p{N}]+)*/gu)||[]).map(x=>x.toLowerCase().replace(/’/g,"'"));
export function validateProduction({story,production}={}){
  require(story&&Array.isArray(story.scenes)&&story.scenes.length,'Structured story required');
  require(production?.schemaVersion===1&&production.fps===FPS&&production.width===WIDTH&&production.height===HEIGHT,'Native 1080×1920/60fps production input required');
  require(/^ID-\d{3,}$/.test(story.contentId||'')&&/^BM-\d{3,}$/.test(production.productionCode||''),'Permanent ID and production code required');
  require(typeof production.scriptRevision==='string'&&production.scriptRevision.trim(),'Approved script revision required');
  require(production.musicSourceSha256===MUSIC_SHA&&production.mixPreset==='B','Approved MUSIC-06 Option B required');
  require(pathOK(production.master?.path)&&digest(production.master?.sha256),'Private master WAV path and SHA-256 required');
  require(Array.isArray(production.scenes)&&production.scenes.length===story.scenes.length,'One acoustic/visual scene record per script scene required');
  require(Array.isArray(story.chapters)&&story.chapters.length&&story.chapters[0].sceneStartIndex===0&&story.chapters.every((c,i)=>typeof c.id==='string'&&c.id&&Number.isInteger(c.sceneStartIndex)&&c.sceneStartIndex>=0&&c.sceneStartIndex<story.scenes.length&&(!i||c.sceneStartIndex>story.chapters[i-1].sceneStartIndex))&&new Set(story.chapters.map(c=>c.id)).size===story.chapters.length,'Explicit story chapters required');
  require(Array.isArray(production.assets),'Asset manifest required');
  const assets=new Map();
  for(const a of production.assets){require(pathOK(a.path)&&digest(a.sha256)&&typeof a.provenance==='string'&&a.provenance.trim()&&typeof a.rights==='string'&&a.rights.trim(),'Asset path, hash, provenance and rights record required');require(!assets.has(a.path),'Duplicate asset path');assets.set(a.path,a);}
  const bg=new Set();const layers=new Set();let cursor=0;
  const scenes=production.scenes.map((p,i)=>{
    const s=story.scenes[i],alignment=p.alignment;
    require(typeof s.narration==='string'&&s.narration.trim()&&typeof s.kicker==='string'&&s.kicker.trim()&&typeof s.headline==='string'&&s.headline.trim(),'Narration, kicker and headline required');
    const aligned=validateAlignedWords(alignment);
    require(digest(alignment.audio.sha256)&&finite(alignment.audio.durationSeconds)&&alignment.audio.durationSeconds>0&&alignment.aligner==='whisperx'&&alignment.transcript===s.narration&&JSON.stringify(aligned.flatMap(w=>words(w.text)))===JSON.stringify(words(s.narration)),'Exact approved transcript and hash-verified WhisperX record required');
    require(pathOK(p.wavPath)&&/\.wav$/i.test(p.wavPath)&&assets.get(p.wavPath)?.sha256===alignment.audio.sha256,'Narration WAV must match alignment and manifest');
    require(['ivory','midnight','saffron'].includes(p.theme),'Explicit approved scene theme required');
    require(typeof p.backgroundId==='string'&&p.backgroundId&&!bg.has(p.backgroundId),'Each scene needs a unique contextual background ID');bg.add(p.backgroundId);
    require(Array.isArray(p.background)&&p.background.length&&Array.isArray(p.artwork)&&p.artwork.length,'Independent background and artwork layers required');
    require(p.background.some(l=>l.motion),'Contextual background motion required');
    require(p.artwork.some(l=>['path','bar','counter','orbit'].includes(l.type)||l.motion),'Meaningful independent artwork motion required');
    require(Array.isArray(p.cues),'Original and adjusted acoustic cue map required');
    const cueMap=new Map();
    for(const cue of p.cues){
      require(typeof cue.id==='string'&&cue.id&&!cueMap.has(cue.id)&&Number.isInteger(cue.wordIndex)&&aligned[cue.wordIndex],'Cue must refer to a measured word');
      const w=aligned[cue.wordIndex];
      require(finite(cue.originalSec)&&Math.abs(cue.originalSec-w.start)<.001&&finite(cue.adjustedSec)&&cue.adjustedSec>=0&&cue.adjustedSec<=w.start+.001&&Math.abs(cue.adjustedSec-leadCue(w))<=.20,'Cue must retain original and adjusted anticipatory timing');
      cueMap.set(cue.id,cue.adjustedSec);
    }
    for(const [group,ls] of [['background',p.background],['artwork',p.artwork]])for(const l of ls){
      require(typeof l.id==='string'&&l.id&&!layers.has(l.id),'Unique editable layer ID required');layers.add(l.id);
      require(['path','rect','circle','line','text','counter','bar','orbit','image'].includes(l.type),'Unsupported layer type');
      if(group==='artwork')require(cueMap.has(l.cue),'Artwork must reference an actual acoustic cue');
      if(l.cue!==undefined)require(cueMap.has(l.cue),'Unknown layer cue');
      require(Array.isArray(l.bounds)&&l.bounds.length===4&&l.bounds.every(finite)&&l.bounds[2]>0&&l.bounds[3]>0,'Authored layer bounds required');
      const [x,y,w,h]=l.bounds;
      if(group==='artwork')require(x>=60&&x+w<=1020&&y>=480&&y+h<=1435,'Artwork bounds collide with header/caption safe regions');
      if(l.motion){require(finite(l.motion.dx)&&finite(l.motion.dy)&&finite(l.motion.period)&&l.motion.period>0,'Motion needs continuous period and displacement');if(group==='artwork')require(x-Math.abs(l.motion.dx)>=60&&x+w+Math.abs(l.motion.dx)<=1020&&y-Math.abs(l.motion.dy)>=480&&y+h+Math.abs(l.motion.dy)<=1435,'Moving artwork exits safe region');}
      for(const key of ['fill','stroke'])if(l[key]!==undefined)require(validColor(l[key]),'Use explicit hex or none for layer colors');
      if(l.type==='path')require(typeof l.d==='string'&&l.d.trim(),'SVG path geometry required');
      if(l.type==='text')require(typeof l.text==='string'&&l.text.trim(),'Text layer requires label');
      if(l.type==='counter')require(finite(l.value),'Finite count-up end value required');
      if(l.type==='image')require(assets.has(l.path),'Image must appear in asset manifest');
      if(l.type==='orbit')require(finite(l.period)&&l.period>0,'Analytic orbit period required');
    }
    const frames=Math.ceil(alignment.audio.durationSeconds*FPS);
    const out={...p,startFrame:cursor,narrationFrames:frames,endFrame:cursor+frames,cueMap};cursor+=frames;return out;
  });
  require(production.scenes.some(x=>x.theme==='saffron')||typeof production.saffronException==='string'&&production.saffronException.trim(),'Saffron feature scene or documented editorial exception required');
  require(finite(production.musicResolveSeconds)&&production.musicResolveSeconds>0&&production.musicResolveSeconds<=2,'Short resolved music tail required');
  const resolveFrames=Math.ceil(production.musicResolveSeconds*FPS);
  const audibleFrames=cursor+resolveFrames,durationInFrames=audibleFrames+HOLD_FRAMES;
  require(production.master.frameCount===durationInFrames,'Master must include exact planned timeline and silent hold');
  require(assets.get(production.master.path)?.sha256===production.master.sha256,'Master must appear in asset manifest');
  const chapters=resolveStoryChapters({...story,scenes:scenes.map((p,i)=>({...story.scenes[i],duration:p.narrationFrames/FPS}))});
  chapters.at(-1).endSec=audibleFrames/FPS;
  return {scenes,chapters,narrationFrames:cursor,audibleFrames,durationInFrames};
}
export function frameState(plan,frame){
  const f=Math.max(0,Math.min(frame,plan.audibleFrames-1));
  let index=plan.scenes.findIndex(s=>f<s.endFrame);if(index<0)index=plan.scenes.length-1;
  const scene=plan.scenes[index],sec=(f-scene.startFrame)/FPS;
  return {index,scene,sec,visualFrame:f,progressSec:frame>=plan.audibleFrames-1?plan.audibleFrames/FPS:f/FPS,holding:frame>=plan.audibleFrames,transition:index?clamp01(sec/.34):1};
}
