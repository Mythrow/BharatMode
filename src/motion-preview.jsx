/**
 * A 14s MOTION STUDY, not a publishable factual Short.
 * Three chapters chosen for this example, not a prescribed story structure.
 * Captions are illustrative cues only, with no narration audio yet.
 */
import React from 'react';
import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame} from 'remotion';
import {BrandAvatar} from './brand-assets.jsx';
import {BRAND as B} from './brand.js';
import {DISPLAY_FONT,BODY_FONT} from './fonts.js';
import {ChapterProgress,TopicPill,CaptionPanel,revealStyle,numberReveal} from './motion-system.jsx';

const CHAPTERS=[
  {id:'hook',title:'The question',startSec:0,endSec:4},
  {id:'deployed',title:'What was deployed',startSec:4,endSec:9},
  {id:'impact',title:'Why it matters',startSec:9,endSec:14}
];
const Head=({children,color=B.graphite,size=92})=>(
  <div style={{fontFamily:DISPLAY_FONT,fontSize:size,fontWeight:800,
    color,lineHeight:1.15,letterSpacing:-3}}>{children}</div>
);
const Rack=({n})=><div style={{
  width:174,height:310,borderRadius:22,
  border:'3px solid #3D5B62',background:'#1B333F',
  boxShadow:'0 18px 28px #102C341A',
  display:'flex',flexDirection:'column',
  justifyContent:'space-evenly',padding:20
}}>
 {Array.from({length:7},(_,i)=><div key={i} style={{
   height:23,border:'1px solid #628184',borderRadius:6,
   background:'#294953',display:'flex',alignItems:'center',gap:12,padding:5
 }}>
  <div style={{height:5,flex:1,background:'#507579',borderRadius:8}}/>
  <div style={{height:7,width:7,borderRadius:10,
    background:(n+i)%3===0?B.primary:'#72D0C4'}}/>
 </div>)}
</div>;
export const BharatMotionPreview=()=>{
  const frame=useCurrentFrame();
  const sec=frame/30;
  const isHook=frame<120;
  const isFact=frame>=120&&frame<270;
  const phaseFrame=isHook?frame:isFact?frame-120:frame-270;
  const themeName=isFact?'midnight':isHook?'ivory':'saffron';
  const dark=isFact;
  const background=isFact?B.charcoal:isHook?B.ivory:'#E8752E';
  return <AbsoluteFill style={{background,overflow:'hidden'}}>
    <Audio src={staticFile('music/ambient.wav')} volume={0.10} loop/>
    <Sequence from={127} durationInFrames={65}>
      <Audio src={staticFile('sfx/metric-rise.wav')} volume={0.15}/>
    </Sequence>
    <div style={{
      position:'absolute',width:630,height:630,borderRadius:800,
      right:-260,top:500,opacity:.65,
      background:isFact?'radial-gradient(circle,#153C40,transparent 70%)'
        :isHook?'radial-gradient(circle,#F4DFCA,transparent 70%)'
        :'radial-gradient(circle,#FFD2AA,transparent 70%)'
    }}/>
    <div style={{position:'absolute',left:82,top:90}}><BrandAvatar size={86}/></div>
    <div style={{position:'absolute',right:72,top:100}}>
      <TopicPill topic="SCIENCE" themeName={themeName}/>
    </div>
    {isHook&&<div style={{position:'absolute',left:84,right:170,top:300}}>
      <div style={{fontFamily:BODY_FONT,fontSize:25,letterSpacing:2,
        color:B.saffronText,fontWeight:800,
        ...revealStyle(phaseFrame,{duration:12})}}>DID YOU KNOW?</div>
      <div style={{marginTop:70,
        ...revealStyle(phaseFrame,{delay:5,duration:16})}}>
        <Head>What powered<br/>India's next<br/>discovery?</Head>
      </div>
      <div style={{marginTop:95,height:8,width:180,
        borderRadius:10,background:B.primary,
        transformOrigin:'left center',
        transform:'scaleX('+Math.max(.005,Math.min(1,(phaseFrame-11)/20))+')'}}/>
      <div style={{marginTop:130,display:'flex',gap:34,
        ...revealStyle(phaseFrame,{delay:13,duration:22})}}>
        <Rack n={0}/><Rack n={1}/><Rack n={2}/>
      </div>
      <div style={{fontFamily:BODY_FONT,color:'#55646A',
        fontSize:23,marginTop:25}}>Illustrative server schematic</div>
    </div>}
    {isFact&&<div style={{position:'absolute',left:83,right:166,top:335}}>
      <div style={{fontFamily:BODY_FONT,fontSize:26,fontWeight:800,
        color:'#8FD1C9',letterSpacing:2,
        ...revealStyle(phaseFrame,{duration:12})}}>GOVERNMENT-REPORTED DEPLOYMENT</div>
      <div style={{marginTop:62,
        fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:186,
        color:'#FFBE91',letterSpacing:-8,
        ...revealStyle(phaseFrame,{delay:4,duration:15})}}>
        {numberReveal(phaseFrame,6000,{delay:6,duration:27}).toLocaleString('en-IN')}
      </div>
      <div style={{marginTop:30,...revealStyle(phaseFrame,{delay:10,duration:20})}}>
        <Head size={79} color={B.ivory}>Rudra servers<br/>deployed.</Head>
      </div>
      <div style={{marginTop:90,padding:34,
        borderRadius:28,background:'#1A303B',
        ...revealStyle(phaseFrame,{delay:23,duration:23})}}>
        <div style={{fontFamily:BODY_FONT,fontWeight:650,fontSize:37,
          color:B.ivory,lineHeight:1.34}}>Part of India's PARAM Rudra<br/>supercomputing systems.</div>
      </div>
    </div>}
    {!isHook&&!isFact&&<div style={{position:'absolute',left:80,right:165,top:320}}>
      <div style={{fontFamily:BODY_FONT,fontWeight:800,
        fontSize:27,letterSpacing:2,color:B.charcoal,
        ...revealStyle(phaseFrame,{duration:11})}}>WHY IT MATTERS</div>
      <div style={{marginTop:65,
        ...revealStyle(phaseFrame,{delay:4,duration:19})}}>
        <Head size={98} color={B.charcoal}>More computing.<br/>More possibilities.</Head>
      </div>
      <div style={{
        marginTop:118,borderRadius:34,padding:45,
        background:B.charcoal,...revealStyle(phaseFrame,{delay:13,duration:22})
      }}>
        {['Climate & weather','Materials research','Biomedical discovery'].map((item,i)=>
        <div key={item} style={{
          color:B.ivory,fontFamily:BODY_FONT,fontSize:43,fontWeight:700,
          padding:'26px 0',borderBottom:i<2?'2px solid #3C4A51':'none',
          display:'flex',alignItems:'center',gap:26
        }}>
          <span style={{width:16,height:16,borderRadius:10,background:B.primary}}/>
          {item}
        </div>)}
      </div>
    </div>}
    <CaptionPanel
      isDark={dark}
      lines={isHook?['India is expanding its','scientific computing tools.']
        :isFact?['6,000 Rudra servers deployed','as of September 2026.']
        :['More capacity can support','future research breakthroughs.']}
    />
    <ChapterProgress chapters={CHAPTERS} timeSec={sec} themeName={themeName}
      bottom={247} right={165}/>
  </AbsoluteFill>;
};
