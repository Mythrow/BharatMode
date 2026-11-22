/**
 * BharatMode V2 directional typewriter and one-line karaoke motion study.
 * 16s, no generated voice, demo word timings only. Not publishable.
 * Production must align word timings to actual narration before render.
 */
import React from 'react';
import {AbsoluteFill,useCurrentFrame} from 'remotion';
import {BrandAvatar} from './brand-assets.jsx';
import {BRAND as B} from './brand.js';
import {DISPLAY_FONT,BODY_FONT} from './fonts.js';
import {ChapterProgress,TopicPill,revealStyle} from './motion-system.jsx';
import {atTime,visibleWords,makeIllustrativeWords} from './motion-v2-timing.js';

const BEATS=[
 {id:'context',startSec:0,endSec:5,headline:'Built for\nbreakthroughs.',kicker:'THE RESEARCH BACKBONE',
  caption:'India is building powerful computers to support scientific research.',theme:'saffron'},
 {id:'deployed',startSec:5,endSec:10.5,headline:'6,000 Rudra\nservers.',kicker:'ALREADY DEPLOYED',
  caption:'Six thousand Rudra servers were deployed by September twenty twenty six.',theme:'midnight'},
 {id:'impact',startSec:10.5,endSec:16,headline:'More power.\nMore possibilities.',kicker:'WHY IT MATTERS',
  caption:'That computing power can support weather materials and biomedical science.',theme:'ivory'}
];
const CHAPTERS=BEATS.map(b=>({id:b.id,startSec:b.startSec,endSec:b.endSec}));
const TIMED=BEATS.map(b=>makeIllustrativeWords(b.caption,b.startSec,b.endSec));

export const TypewriterHeadline=({text,localFrame,ink=B.graphite,rate=26})=>{
 const count=Math.max(0,Math.min(text.length,Math.floor(localFrame/30*rate)));
 const done=count>=text.length;
 return <div style={{fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:91,lineHeight:1.18,
   letterSpacing:-3.4,color:ink,whiteSpace:'pre-line',minHeight:345}}>
    {text.slice(0,count)}
    {!done&&<span style={{display:'inline-block',verticalAlign:'-.05em',width:7,height:65,
      marginLeft:7,background:ink,borderRadius:8}}/>}
 </div>;
};

/** Contrast uses no full caption pill — only a soft background gradient. */
export const WordFollowCaption=({words,timeSec,themeName='ivory'})=>{
  const past=visibleWords(words,timeSec,4);
  const dark=themeName!=='ivory';
  const gradient=themeName==='ivory'
    ? 'linear-gradient(180deg,transparent 0%,rgba(255,247,235,.9) 55%,#FFF7EB 100%)'
    : 'linear-gradient(180deg,transparent 0%,rgba(11,16,24,.86) 55%,#0B1018 100%)';
  const ink=dark?B.ivory:B.graphite;
  const active=dark?'#FFBE91':B.saffronText;
  return <div style={{position:'absolute',top:1438,left:0,right:0,height:273,
    display:'flex',alignItems:'center',background:gradient,pointerEvents:'none'}}>
    <div style={{position:'absolute',left:80,right:165,top:76,height:100,
      overflow:'hidden',whiteSpace:'nowrap',display:'flex',alignItems:'center',
      justifyContent:'center',gap:18}}>
      {past.map((w,i)=>{
        const begun=timeSec-w.start;
        const progress=Math.max(0,Math.min(1,begun/Math.max(.01,w.end-w.start)));
        const partial=w.isActive?w.text.slice(0,Math.max(1,Math.ceil(w.text.length*progress))):w.text;
        return <span key={w.start} style={{fontFamily:BODY_FONT,fontWeight:700,
          color:w.isActive?active:ink,opacity:w.isActive?1:.57,
          fontSize:44,whiteSpace:'nowrap',borderBottom:w.isActive?'4px solid '+active:'4px solid transparent',
          paddingBottom:5}}>{partial}</span>;
      })}
    </div>
  </div>;
};

const Rack=({index,localFrame})=>{
 const reveal=Math.max(0,Math.min(1,(localFrame-12-index*15)/18));
 return <div style={{width:178,height:253,background:'#1B333D',border:'3px solid #527C7D',
   borderRadius:22,padding:21,display:'flex',gap:12,flexDirection:'column',
   transform:'translateX('+((1-reveal)*-42)+'px)',opacity:.24+.76*reveal}}>
    {Array.from({length:5},(_,i)=><div key={i} style={{height:26,background:'#2C4B53',
      borderRadius:5,border:'2px solid #5B8485',position:'relative'}}>
      <div style={{width:7,height:7,background:i%2?B.primary:'#70D3CC',borderRadius:8,
        position:'absolute',right:7,top:6}}/>
    </div>)}
 </div>;
};

export const BharatMotionPreviewV2=()=>{
  const frame=useCurrentFrame();const sec=frame/30;
  const i=atTime(CHAPTERS,sec);const beat=BEATS[i];
  const localFrame=frame-Math.round(beat.startSec*30);
  const isLight=beat.theme==='ivory';
  const bg=beat.theme==='saffron'?B.primary:beat.theme==='midnight'?B.charcoal:B.ivory;
  const headlineInk=beat.theme==='midnight'?B.ivory:beat.theme==='ivory'?B.graphite:B.charcoal;
  const kickerInk=beat.theme==='midnight'?'#8FCFC3':beat.theme==='saffron'?B.charcoal:B.saffronText;
  return <AbsoluteFill style={{background:bg,overflow:'hidden'}}>
    <div style={{position:'absolute',left:-230,top:1260,width:1120,height:760,
      border:'46px solid '+(beat.theme==='saffron'?'#FFFFFF1D':'#117A7A15'),
      borderRadius:'50%',transform:'rotate(-22deg)',opacity:.6}}/>
    <div style={{position:'absolute',right:-280,top:530,width:900,height:900,
      borderRadius:1000,background:beat.theme==='midnight'
        ? 'radial-gradient(circle,#17464999,transparent 70%)'
        : 'radial-gradient(circle,#FFDAAD88,transparent 70%)'}}/>
    <div style={{position:'absolute',left:84,top:86}}><BrandAvatar size={90}/></div>
    <div style={{position:'absolute',right:72,top:98}}><TopicPill topic="SCIENCE" themeName={beat.theme}/></div>
    <div style={{position:'absolute',top:325,left:85,right:165}}>
      <div style={{fontFamily:BODY_FONT,fontSize:27,fontWeight:800,letterSpacing:2.4,
        color:kickerInk,opacity:.9,...revealStyle(localFrame,{duration:10,offsetY:15})}}>{beat.kicker}</div>
      <div style={{marginTop:50}}><TypewriterHeadline text={beat.headline} localFrame={localFrame} ink={headlineInk}/></div>
    </div>
    <div style={{position:'absolute',left:80,right:165,top:920,height:500,
      background:'#101D27',borderRadius:42,border:'2px solid #48656B4D'}}>
      <div style={{position:'absolute',left:42,top:38,fontFamily:BODY_FONT,fontSize:23,
        color:'#FFBE91',letterSpacing:1.9,fontWeight:800}}>
        {i===0?'DESIGN → MANUFACTURE → DEPLOY':i===1?'PARAM RUDRA / SYSTEMS':'RESEARCH / SCIENCE / COMPUTING'}
      </div>
      <div style={{position:'absolute',left:75,top:116,display:'flex',gap:37}}>
        {[0,1,2].map(n=><Rack key={n} index={n} localFrame={localFrame}/>)}
      </div>
      <div style={{position:'absolute',left:95,right:95,bottom:51,height:8,
        background:'#264348',borderRadius:8,overflow:'hidden'}}>
        <div style={{height:'100%',width:Math.max(0,Math.min(100,(localFrame-26)/90*100))+'%',
          background:'linear-gradient(90deg,#117A7A,#E8752E)'}}/>
      </div>
    </div>
    <WordFollowCaption words={TIMED[i]} timeSec={sec} themeName={beat.theme}/>
    <ChapterProgress chapters={CHAPTERS} timeSec={sec} themeName={beat.theme}
      bottom={265} left={84} right={165} height={10} gap={14}/>
  </AbsoluteFill>;
};