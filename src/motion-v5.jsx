/** Bharat Mode V5 — 16-second SILENT storyboard/motion design study.
 * - Both scenes overlap for a visible directional transition.
 * - Caption group is a global overlay, so it never slides off-center.
 * - Typewriter only changes glyph count; its whole text container ALSO moves in.
 * - Exact owner-approved avatar SVG; no recreated BM paths.
 * Word timings are simulated and must be replaced by real audio alignment.
 */
import React from 'react';
import {AbsoluteFill,useCurrentFrame} from 'remotion';
import {BrandAvatar} from './brand-assets.jsx';
import {BRAND as B} from './brand.js';
import {DISPLAY_FONT,BODY_FONT} from './fonts.js';
import {TopicPill,ChapterProgress} from './motion-system.jsx';
import {demoWordTimings,groupWordRanges,groupedVisibleWords,clamp01} from './motion-v4-timing.js';
import {easeOut,DEMO_BEATS,currentBeatAt,scenePoseAt,sceneWipeAt,headlineCharsAt} from './motion-v5-timing.js';

const STORIES=[
  {id:'origin',startSec:0,endSec:5,theme:'saffron',
    kicker:'THE RESEARCH BACKBONE',headline:'Built for\nbreakthroughs.',
    evidence:'DESIGN → MANUFACTURE → DEPLOY',
    speech:'India is building powerful computers to support scientific research.',
    groups:['India is building','powerful computers','to support','scientific research.']},
  {id:'deployed',startSec:5,endSec:10.5,theme:'midnight',
    kicker:'ALREADY DEPLOYED',headline:'6,000 Rudra\nservers.',
    evidence:'PARAM RUDRA / SERVER SYSTEMS',
    speech:'Six thousand Rudra servers were deployed by September twenty twenty six.',
    groups:['Six thousand Rudra','servers were deployed','by September','twenty twenty six.']},
  {id:'research',startSec:10.5,endSec:16,theme:'ivory',
    kicker:'WHY IT MATTERS',headline:'More power.\nMore possibilities.',
    evidence:'RESEARCH / SCIENCE / COMPUTING',
    speech:'That computing power can support weather materials and biomedical science.',
    groups:['That computing power','can support weather,','materials and','biomedical science.']}
];
const WORDS=STORIES.map(s=>demoWordTimings(s.speech,s.startSec,s.endSec));
const GROUPS=STORIES.map((s,i)=>groupWordRanges(WORDS[i],s.groups));
const THEME={
  saffron:{background:'linear-gradient(138deg,#E8752E,#EF9962)',text:B.charcoal,small:B.charcoal},
  midnight:{background:B.charcoal,text:B.ivory,small:'#8AD5C8'},
  ivory:{background:'linear-gradient(140deg,#FFF7EB,#FBF0E1)',text:B.graphite,small:B.saffronText}
};
const ServerRack=({localSec,index})=>{
  const reveal=easeOut((localSec-.20-index*.42)/.63);
  return <div style={{height:242,width:180,flexShrink:0,
    background:'linear-gradient(125deg,#2B4751,#182833)',
    border:'3px solid #5B8285',borderRadius:20,
    padding:18,display:'flex',flexDirection:'column',gap:12,
    transform:'translateX('+((1-reveal)*-82)+'px)',
    opacity:.15+.85*reveal}}>
    {Array.from({length:5},(_,i)=><div key={i} style={{height:28,
      borderRadius:5,background:'#385861',border:'2px solid #648486',
      position:'relative'}}>
      <div style={{position:'absolute',right:7,top:7,height:6,width:6,
        borderRadius:5,background:'#70D3CC'}}/>
    </div>)}
  </div>;
};
const MovingScene=({scene,index,timeSec})=>{
  const local=timeSec-scene.startSec;
  const pose=scenePoseAt(timeSec,index,DEMO_BEATS);
  if(pose.opacity<=0) return null;
  const colors=THEME[scene.theme];
  const kickerEnter=easeOut((local+.10)/.55);
  const headlineEnter=easeOut((local+.05)/.54);
  const evidenceEnter=easeOut((local-.10)/.74);
  const flow=easeOut((local-.6)/3.2);
  const glowX=Math.sin(timeSec*.6)*40;
  const display=headlineCharsAt(scene.headline,local);
  return <AbsoluteFill style={{background:colors.background,overflow:'hidden',
    opacity:pose.opacity,transform:'translateX('+pose.translateX+'px)'}}>
    <div style={{position:'absolute',left:-240,top:1130,width:1130,height:750,
      border:'55px solid #117A7A19',borderRadius:'50%',transform:'rotate(-22deg)'}}/>
    <div style={{position:'absolute',right:-270,top:535,width:960,height:960,
      borderRadius:'50%',transform:'translateX('+glowX+'px)',
      background:scene.theme==='midnight'? 'radial-gradient(circle,#117A7A55,transparent 70%)':
        scene.theme==='ivory'?'radial-gradient(circle,#E8752E20,transparent 71%)':
        'radial-gradient(circle,#FFF7EB42,transparent 72%)'}}/>
    <div style={{position:'absolute',top:283,left:86,right:165,
      color:colors.small,fontFamily:BODY_FONT,fontSize:27,fontWeight:700,letterSpacing:3.1,
      opacity:kickerEnter,transform:'translateX('+((1-kickerEnter)*90)+'px)'}}>
      {scene.kicker}
    </div>
    <div style={{position:'absolute',top:364,left:83,right:165,minHeight:260,
      opacity:headlineEnter,
      transform:'translateX('+((1-headlineEnter)*106)+'px) translateY('+((1-headlineEnter)*9)+'px)'}}>
      <div style={{fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:92,
        lineHeight:1.17,letterSpacing:-3.5,whiteSpace:'pre-line',color:colors.text}}>
        {display}
      </div>
    </div>
    <div style={{position:'absolute',top:777,left:80,right:165,height:500,
      background:'#101D27',border:'2px solid #48656B66',borderRadius:40,
      overflow:'hidden',opacity:evidenceEnter,
      transform:'translateX('+((1-evidenceEnter)*142)+'px) translateY('+((1-evidenceEnter)*16)+'px)',
      boxShadow:'0 24px 54px #101F2A22'}}>
      <div style={{position:'absolute',top:33,left:43,fontFamily:BODY_FONT,fontSize:22,
        color:'#FFBE91',fontWeight:700,letterSpacing:1.6}}>{scene.evidence}</div>
      <div style={{position:'absolute',top:118,left:75,display:'flex',gap:35}}>
        {[0,1,2].map(n=><ServerRack key={n} localSec={local} index={n}/>) }
      </div>
      <div style={{position:'absolute',left:100,right:100,bottom:45,height:8,
        background:'#264348',borderRadius:10,overflow:'hidden'}}>
        <div style={{height:'100%',width:(flow*100)+'%',borderRadius:10,
          background:'linear-gradient(90deg,#117A7A,#E8752E)'}}/>
      </div>
    </div>
  </AbsoluteFill>;
};

/** Global caption surface, centered at x=540 regardless of scene-layer position. */
const CenteredCaptions=({timeSec,index,theme})=>{
  const result=groupedVisibleWords(WORDS[index],GROUPS[index],timeSec);
  if(!result.words.length)return null;
  const words=WORDS[index],range=GROUPS[index][result.group];
  const first=words[range.start];
  const entered=clamp01((timeSec-first.start)/.12);
  const bg=theme==='midnight'?'rgba(23,40,50,.30)':
    theme==='ivory'?'rgba(11,16,24,.10)':'rgba(11,16,24,.18)';
  const ink=theme==='ivory'?B.graphite:B.ivory;
  const active=theme==='ivory'?B.saffronText:'#FFBE91';
  // Conservative fit estimate for a single-line phrase inside symmetric 140px margins.
  const length=result.words.reduce((sum,w)=>sum+w.text.length,0);
  const fontSize=Math.max(44,Math.min(57,Math.floor(730/(Math.max(1,length)*.59+result.words.length*.25))));
  return <div style={{position:'absolute',zIndex:60,top:1405,left:140,right:140,
    height:175,display:'flex',justifyContent:'center',alignItems:'center',pointerEvents:'none'}}>
    <div style={{display:'inline-flex',alignItems:'center',justifyContent:'center',
      width:'max-content',maxWidth:'100%',minHeight:112,
      padding:'18px 24px',borderRadius:12,background:bg,
      boxShadow:'0 5px 20px #0000000C',backdropFilter:'blur(5px)',
      opacity:entered,gap:14,whiteSpace:'nowrap'}}>
      {result.words.map(w=><span key={w.start} style={{fontFamily:BODY_FONT,
        fontSize,fontWeight:700,lineHeight:1.25,whiteSpace:'nowrap',
        color:w.isActive?active:ink,opacity:w.opacity,
        textShadow:theme==='ivory'?'none':'0 1px 5px #0B101878',
        transform:'scale('+w.scale+')',transformOrigin:'center 65%'}}>{w.text}</span>)}
    </div>
  </div>;
};

export const BharatMotionPreviewV5=()=>{
  const frame=useCurrentFrame();
  const sec=frame/30;
  const index=currentBeatAt(sec,DEMO_BEATS);
  const theme=STORIES[index].theme;
  const wipe=sceneWipeAt(sec,DEMO_BEATS);
  const wipeAlpha=wipe>=0?Math.sin(wipe*Math.PI)*.62:0;
  const pillBg=theme==='midnight'?B.ivory:B.charcoal;
  const pillInk=theme==='midnight'?B.charcoal:B.ivory;
  return <AbsoluteFill style={{overflow:'hidden',background:B.charcoal}}>
    {STORIES.map((s,i)=><MovingScene key={s.id} scene={s} index={i} timeSec={sec}/>) }
    <ChapterProgress chapters={DEMO_BEATS} timeSec={sec} themeName={theme}
      bottom={262} left={84} right={165} height={10} gap={14}/>
    {wipe>=0&&<div style={{position:'absolute',inset:0,zIndex:40,
      pointerEvents:'none',opacity:wipeAlpha,overflow:'hidden'}}>
      <div style={{position:'absolute',left:-350,top:-150,width:300,height:2250,
        transform:'translateX('+(-260+1660*wipe)+'px) skewX(-15deg)',
        background:'linear-gradient(90deg,#117A7AE0,#E8752EE8 30%,#E8752E 76%,#FFF7EBBF)',
        boxShadow:'0 0 55px #E8752E44'}}/>
    </div>}
    <div style={{position:'absolute',top:89,left:86,right:72,zIndex:55,
      display:'flex',justifyContent:'space-between',alignItems:'center'}}>
      <BrandAvatar size={88}/>
      <div style={{padding:'17px 26px',borderRadius:50,background:pillBg,
        fontFamily:BODY_FONT,fontWeight:500,fontSize:27,
        letterSpacing:1.4,color:pillInk}}>SCIENCE</div>
    </div>
    <CenteredCaptions timeSec={sec} index={index} theme={theme}/>
  </AbsoluteFill>;
};