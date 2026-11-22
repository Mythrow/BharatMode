/**
 * Bharat Mode V4: DIRECTIONAL motion preserved, headline TYPEWRITER only,
 * no cursor, 0.2s spring-pop word caption, active spoken word color ONLY.
 * 16s illustration, with no narration: timing is not voice-aligned yet.
 * This is a review proof, NOT a video for publishing.
 */
import React from 'react';
import {AbsoluteFill,useCurrentFrame} from 'remotion';
import {BrandAvatar} from './brand-assets.jsx';
import {BRAND as B} from './brand.js';
import {DISPLAY_FONT,BODY_FONT} from './fonts.js';
import {ChapterProgress,TopicPill,revealStyle} from './motion-system.jsx';
import {clamp01,demoWordTimings,groupWordRanges,groupedVisibleWords} from './motion-v4-timing.js';

const BEATS=[
 {id:'context',startSec:0,endSec:5,headline:'Built for\nbreakthroughs.',kicker:'THE RESEARCH BACKBONE',
  evidence:'DESIGN → MANUFACTURE → DEPLOY',
  caption:'India is building powerful computers to support scientific research.',groups:['India is building','powerful computers','to support scientific research.'],theme:'saffron'},
 {id:'deployed',startSec:5,endSec:10.5,headline:'6,000 Rudra\nservers.',kicker:'ALREADY DEPLOYED',
  evidence:'PARAM RUDRA / SERVER SYSTEMS',
  caption:'Six thousand Rudra servers were deployed by September twenty twenty six.',groups:['Six thousand Rudra servers','were deployed','by September twenty twenty six.'],theme:'midnight'},
 {id:'impact',startSec:10.5,endSec:16,headline:'More power.\nMore possibilities.',kicker:'WHY IT MATTERS',
  evidence:'RESEARCH / SCIENCE / COMPUTING',
  caption:'That computing power can support weather materials and biomedical science.',groups:['That computing power','can support weather','materials and biomedical science.'],theme:'ivory'}
];
const CHAPTERS=BEATS.map(x=>({id:x.id,startSec:x.startSec,endSec:x.endSec}));
const DEMO_WORDS=BEATS.map(x=>demoWordTimings(x.caption,x.startSec,x.endSec));
const DEMO_GROUPS=BEATS.map((beat,i)=>groupWordRanges(DEMO_WORDS[i],beat.groups));

const easeOut=t=>1-(1-clamp01(t))**3;

/** Deliberately NO caret or cursor. Only headline glyphs are typed. */
export const TypewriterHeadlineV4=({text,localSec,color,rate=26})=>{
  const count=Math.min(text.length,Math.max(0,Math.floor(Math.max(0,localSec-.06)*rate)));
  return <div style={{fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:91,
    lineHeight:1.18,letterSpacing:-3.4,color,whiteSpace:'pre-line',
    minHeight:350}}>{text.slice(0,count)}</div>;
};

/** A lightly translucent caption box hugs ONLY the current spoken phrase. */
export const WordFollowCaptionV4=({words=[],groups=[],timeSec,themeName='ivory'})=>{
  const current=groupedVisibleWords(words,groups,timeSec);
  if(!current.words.length)return null;
  const range=groups[current.group];
  const lastWord=words[range.end-1];
  const firstWord=words[range.start];
  const fadeIn=clamp01((timeSec-firstWord.start)/.13);
  const fadeOut=clamp01((lastWord.end-timeSec)/.12);
  const onIvory=themeName==='ivory';
  const overlay=onIvory?'rgba(11,16,24,.11)':themeName==='midnight'
    ?'rgba(13,23,32,.32)':'rgba(11,16,24,.24)';
  const ink=onIvory?B.graphite:B.ivory;
  const highlight=onIvory?B.saffronText:'#FFBE91';
  return <div style={{position:'absolute',left:80,right:165,top:1460,height:145,
    display:'flex',justifyContent:'center',alignItems:'center',pointerEvents:'none'}}>
    <div style={{display:'inline-flex',width:'max-content',maxWidth:'100%',
      padding:'14px 20px',borderRadius:13,background:overlay,
      backdropFilter:'blur(5px)',alignItems:'center',justifyContent:'center',gap:14,
      boxShadow:'0 5px 17px rgba(0,0,0,.06)',opacity:Math.min(fadeIn,fadeOut)}}>
      {current.words.map(w=><span key={w.start} style={{display:'inline-block',
        fontFamily:BODY_FONT,fontSize:60,fontWeight:700,lineHeight:1.22,
        whiteSpace:'nowrap',flexShrink:0,color:w.isActive?highlight:ink,
        opacity:w.opacity,transform:'scale('+w.scale+')',transformOrigin:'center 65%'}}>{w.text}</span>)}
    </div>
  </div>;
};

const Rack=({index,localSec})=>{
  const reveal=easeOut((localSec-.5-index*.48)/.6);
  return <div style={{width:178,height:253,background:'#1B333D',
    border:'3px solid #527C7D',borderRadius:22,padding:21,
    display:'flex',flexDirection:'column',gap:12,
    transform:'translateX('+((1-reveal)*-38)+'px)',
    opacity:.25+.75*reveal}}>
    {Array.from({length:5},(_,i)=><div key={i} style={{height:26,
      background:'#2C4B53',borderRadius:5,border:'2px solid #5B8485',
      position:'relative'}}>
      <div style={{width:7,height:7,background:i%2?B.primary:'#70D3CC',
        borderRadius:8,position:'absolute',right:7,top:6}}/>
    </div>)}
  </div>;
};

export const BharatMotionPreviewV4=()=>{
  const frame=useCurrentFrame();
  const sec=frame/30;
  const index=sec<5?0:sec<10.5?1:2;
  const beat=BEATS[index];
  const localSec=sec-beat.startSec;
  const localFrame=Math.round(localSec*30);
  const bg=beat.theme==='saffron'?B.primary:beat.theme==='midnight'?B.charcoal:B.ivory;
  const headlineInk=beat.theme==='midnight'?B.ivory:
    beat.theme==='ivory'?B.graphite:B.charcoal;
  const kickerInk=beat.theme==='midnight'?'#8FCFC3':
    beat.theme==='saffron'?B.charcoal:B.saffronText;
  const e=easeOut((localSec-.3)/.7);
  const line=easeOut((localSec-1)/3.4);
  return <AbsoluteFill style={{background:bg,overflow:'hidden'}}>
    <div style={{position:'absolute',left:-230,top:1260,width:1120,
      height:760,border:'46px solid '+(beat.theme==='saffron'?'#FFFFFF1D':'#117A7A15'),
      borderRadius:'50%',transform:'rotate(-22deg)',opacity:.6}}/>
    <div style={{position:'absolute',right:-280,top:530,width:900,height:900,
      borderRadius:1000,transform:'translateX('+Math.sin(sec*.4)*24+'px)',
      background:beat.theme==='midnight'?'radial-gradient(circle,#17464999,transparent 70%)':
        'radial-gradient(circle,#FFDAAD88,transparent 70%)'}}/>
    <div style={{position:'absolute',left:84,top:86}}><BrandAvatar size={90}/></div>
    <div style={{position:'absolute',right:72,top:98}}>
      <TopicPill topic="SCIENCE" themeName={beat.theme}/>
    </div>
    <div style={{position:'absolute',top:325,left:85,right:165}}>
      <div style={{fontFamily:BODY_FONT,fontSize:27,fontWeight:700,
        letterSpacing:2.4,color:kickerInk,
        ...revealStyle(localFrame,{duration:16,offsetY:0}),
        transform:'translateX('+((1-easeOut(localSec/.55))*48)+'px)'}}>
        {beat.kicker}
      </div>
      <div style={{marginTop:50}}>
        <TypewriterHeadlineV4 text={beat.headline} localSec={localSec} color={headlineInk}/>
      </div>
    </div>
    <div style={{position:'absolute',left:80,right:165,top:920,height:500,
      background:'#101D27',borderRadius:42,border:'2px solid #48656B4D',
      opacity:e,transform:'translate('+((1-e)*74)+'px,'+((1-e)*18)+'px)'}}>
      <div style={{position:'absolute',left:42,top:38,fontFamily:BODY_FONT,
        fontSize:23,color:'#FFBE91',letterSpacing:1.9,fontWeight:700}}>
        {beat.evidence}
      </div>
      <div style={{position:'absolute',left:75,top:116,display:'flex',gap:37}}>
        {[0,1,2].map(n=><Rack key={n} index={n} localSec={localSec}/>) }
      </div>
      <div style={{position:'absolute',left:95,right:95,bottom:51,height:8,
        background:'#264348',borderRadius:8,overflow:'hidden'}}>
        <div style={{height:'100%',width:(line*100)+'%',
          background:'linear-gradient(90deg,#117A7A,#E8752E)'}}/>
      </div>
    </div>
    <WordFollowCaptionV4 words={DEMO_WORDS[index]} groups={DEMO_GROUPS[index]} timeSec={sec} themeName={beat.theme}/>
    <ChapterProgress chapters={CHAPTERS} timeSec={sec} themeName={beat.theme}
      bottom={266} left={84} right={165} height={10} gap={14}/>
  </AbsoluteFill>;
};