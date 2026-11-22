/**
 * Bharat Mode 1080x1920 editable Remotion style proofs (NOT yet motion templates).
 *
 * Fact basis: PIB, 04 Oct 2026, Rudra servers, as of Sep 2026.
 * https://www.pib.gov.in/PressNoteDetails.aspx?ModuleId=3&NoteId=160306&lang=1&reg=48
 *
 * These components use approved Sora + Manrope and the unchanged owner SVG avatar.
 * Server graphics are original conceptual schematics, not actual photographs.
 * Do not promote a proof still into a published video without editorial QA.
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BrandAvatar} from './brand-assets.jsx';
import {DISPLAY_FONT, BODY_FONT} from './fonts.js';
import {BRAND} from './brand.js';
import {ChapterProgress,TopicPill} from './motion-system.jsx';

const C = BRAND;
const smallCaps=(color,spacing=2)=>({
  color,fontFamily:BODY_FONT,fontWeight:800,fontSize:23,letterSpacing:spacing
});

const Caption = ({lines}) => (
  <div style={{
    position:'absolute',left:80,top:1370,width:920,height:167,
    borderRadius:28,background:C.charcoal,
    display:'flex',flexDirection:'column',alignItems:'center',
    justifyContent:'center',gap:3,padding:20
  }}>
    {lines.map((line,i)=><div key={i} style={{
      fontFamily:BODY_FONT,fontSize:39,fontWeight:700,color:C.ivory,
      textAlign:'center',lineHeight:1.3
    }}>{line}</div>)}
  </div>
);
const PROOF_CHAPTERS=[
  {id:'intro',startSec:0,endSec:6},
  {id:'deployment',startSec:6,endSec:14},
  {id:'applications',startSec:14,endSec:22}
];
const ProofProgress=({timeSec,themeName='ivory'})=>(
  <ChapterProgress chapters={PROOF_CHAPTERS}
    themeName={themeName} timeSec={timeSec} bottom={255} right={165}/>
);
const Topline=({topic='SCIENCE',themeName='ivory'})=>{
  const dark=themeName==='midnight';
  const ink=dark?C.ivory:C.graphite;
  return <>
    <div style={{position:'absolute',left:82,top:84}}>
      <BrandAvatar size={88}/>
    </div>
    <div style={{position:'absolute',left:186,top:101,
      fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:28,color:ink,letterSpacing:1}}>
      BHARAT MODE
    </div>
    <div style={{position:'absolute',left:186,top:139,
      fontFamily:BODY_FONT,fontWeight:650,fontSize:17,
      color:dark?'#B9C9C9':'#657073',letterSpacing:1.45}}>
      BIG IDEAS. REAL PROGRESS.
    </div>
    <div style={{position:'absolute',right:165,top:91}}>
      <TopicPill topic={topic} themeName={themeName}/>
    </div>
  </>;
};
const ServerRack=({dark=false,compact=false})=>(
  <div style={{
    width:compact?116:199,height:compact?274:284,
    background:dark?'#172A33':'linear-gradient(125deg,#3E5961,#101B24)',
    border:dark?'2px solid #456268':'2px solid #60757A',
    borderRadius:compact?15:24,padding:compact?12:18,
    display:'flex',flexDirection:'column',gap:compact?10:11,
    boxShadow:dark?'0 0 28px rgba(15,126,125,.12)':'0 14px 28px rgba(26,55,62,.12)'
  }}>
    {Array.from({length:compact?7:6},(_,i)=><div key={i} style={{
      height:compact?23:26,borderRadius:6,
      background:dark?'#273F48':'#203943',
      border:'1px solid #4B6A6C',padding:'0 9px',
      display:'flex',alignItems:'center',justifyContent:'space-between'
    }}>
      <div style={{width:'70%',height:3,background:'#789D9C',opacity:.64,borderRadius:4}}/>
      <div style={{height:6,width:6,borderRadius:6,
        background:i%3===0?C.primary:'#69C4BA'}}/>
    </div>)}
  </div>
);
export const BharatProofIvory=()=>(
  <AbsoluteFill style={{background:'linear-gradient(145deg,#FFF7EB,#F4EEE6)',overflow:'hidden'}}>
    <div style={{position:'absolute',width:540,height:540,borderRadius:'50%',
      background:'#F5E4D1',right:-180,top:250,opacity:.7}}/>
    <Topline/>
    <div style={{position:'absolute',left:84,top:260,...smallCaps(C.saffronText)}}>
      AN UNDERREPORTED MILESTONE
    </div>
    <div style={{
      position:'absolute',left:82,top:342,
      fontFamily:DISPLAY_FONT,fontSize:88,fontWeight:800,
      color:C.graphite,lineHeight:1.25,letterSpacing:-3.2
    }}>The machines<br/>behind India's<br/>next discovery.</div>
    <div style={{position:'absolute',left:87,top:700,
      height:9,width:175,borderRadius:8,background:C.primary}}/>
    <div style={{
      position:'absolute',left:80,top:749,width:920,height:578,
      borderRadius:42,background:'#FFFCF6',border:'2px solid #E6DACE'
    }}>
      <div style={{position:'absolute',left:46,top:52,...smallCaps(C.teal)}}>
        A COMPUTING FOUNDATION
      </div>
      <div style={{position:'absolute',left:46,top:105,fontSize:37,
        fontFamily:DISPLAY_FONT,color:C.graphite,fontWeight:800}}>
        PARAM RUDRA
      </div>
      <div style={{position:'absolute',left:71,right:71,bottom:135,display:'flex',
        justifyContent:'space-between',alignItems:'flex-end'}}>
        <ServerRack/><ServerRack/><ServerRack/>
      </div>
      <div style={{position:'absolute',left:75,right:75,bottom:110,
        height:3,background:'#9AC7C2'}}/>
      <div style={{position:'absolute',left:55,right:55,bottom:40,
        fontFamily:BODY_FONT,fontSize:20,textAlign:'center',
        color:'#697C7C'}}>Illustrative server architecture — not actual equipment</div>
    </div>
    <Caption lines={['6,000 Rudra servers deployed','as of September 2026.']}/>
    <ProofProgress timeSec={3} themeName="ivory"/>
  </AbsoluteFill>
);
export const BharatProofDark=()=>(
  <AbsoluteFill style={{background:C.charcoal,overflow:'hidden'}}>
    <div style={{position:'absolute',width:830,height:830,borderRadius:'50%',
      right:-230,top:650,
      background:'radial-gradient(circle,#1B4648 0%,transparent 70%)',opacity:.6}}/>
    <Topline topic="SCIENCE" themeName="midnight"/>
    <div style={{position:'absolute',left:83,top:260,...smallCaps('#ACD4CC')}}>
      THE NUMBER THAT MATTERS
    </div>
    <div style={{position:'absolute',left:75,top:310,
      fontFamily:DISPLAY_FONT,fontWeight:800,fontSize:220,
      letterSpacing:-10,color:C.primary}}>6,000</div>
    <div style={{position:'absolute',left:84,top:591,
      fontFamily:DISPLAY_FONT,fontSize:69,fontWeight:800,
      color:C.ivory,lineHeight:1.15,letterSpacing:-2.2}}>
      Rudra servers<br/>already deployed.
    </div>
    <div style={{position:'absolute',left:83,top:810,borderRadius:26,
      background:'#223238',padding:'17px 31px',
      ...smallCaps('#7DD0C2',1),fontSize:21}}>
      INDIA-DESIGNED · C-DAC
    </div>
    <div style={{
      position:'absolute',left:80,top:906,width:920,height:418,
      background:'#15212B',border:'2px solid #35484D',
      borderRadius:40,display:'flex',justifyContent:'space-evenly',
      alignItems:'center'
    }}>
      {Array.from({length:5},(_,i)=><ServerRack key={i} compact dark/>)}
      <div style={{position:'absolute',bottom:25,
        fontFamily:BODY_FONT,fontSize:19,color:'#849FA5',letterSpacing:1.2}}>
        SYSTEM DIAGRAM · ILLUSTRATION
      </div>
    </div>
    <Caption lines={['This is deployed research','infrastructure — not a proposal.']}/>
    <ProofProgress timeSec={9} themeName="midnight"/>
  </AbsoluteFill>
);
export const BharatProofSaffron=()=>(
  <AbsoluteFill style={{background:C.ivory,overflow:'hidden'}}>
    <div style={{position:'absolute',left:0,top:0,
      width:1080,height:889,
      background:'linear-gradient(130deg,#E8752E,#F4A66A)'}}/>
    <div style={{position:'absolute',right:-120,top:-120,
      borderRadius:'50%',height:500,width:500,
      background:'#FFDDC1',opacity:.24}}/>
    <Topline topic="SCIENCE" themeName="saffron"/>
    <div style={{position:'absolute',left:83,top:290,...smallCaps(C.charcoal,1.5)}}>
      FROM DESIGN TO DEPLOYMENT
    </div>
    <div style={{
      position:'absolute',left:80,top:349,fontFamily:DISPLAY_FONT,
      fontWeight:800,fontSize:109,lineHeight:1.14,
      letterSpacing:-4.2,color:C.charcoal
    }}>Built to<br/>power<br/>research.</div>
    <div style={{
      position:'absolute',left:75,top:819,width:930,height:546,
      background:C.charcoal,borderRadius:42
    }}>
      <div style={{position:'absolute',left:42,top:58,...smallCaps('#F4B98E',1.2)}}>
        THE RUDRA SERVER JOURNEY
      </div>
      <div style={{position:'absolute',left:38,top:144,right:38,
        display:'flex',gap:21,justifyContent:'space-between'}}>
        {[
          ['01','DESIGNED','C-DAC'],
          ['02','MANUFACTURED','In India'],
          ['03','DEPLOYED','PARAM Rudra']
        ].map(([num,title,detail])=><div key={num} style={{
          width:267,height:219,borderRadius:25,
          background:'#1B2B34',border:'2px solid #35474D',
          padding:23,display:'flex',flexDirection:'column'
        }}>
          <div style={{fontFamily:DISPLAY_FONT,fontSize:49,
            fontWeight:800,color:C.primary}}>{num}</div>
          <div style={{fontFamily:BODY_FONT,fontSize:19,
            fontWeight:800,color:C.ivory,marginTop:7}}>{title}</div>
          <div style={{fontFamily:BODY_FONT,fontSize:23,fontWeight:600,
            color:'#BDD0D0',marginTop:12}}>{detail}</div>
        </div>)}
      </div>
      <div style={{position:'absolute',left:38,right:38,bottom:65,
        background:'#2C3B41',borderRadius:22,
        height:105,display:'flex',alignItems:'center',padding:'0 27px',gap:25}}>
        <span style={{fontFamily:DISPLAY_FONT,fontSize:49,fontWeight:800,
          color:'#FFBE91'}}>6,000</span>
        <span style={{fontFamily:BODY_FONT,fontSize:28,color:C.ivory}}>
          servers deployed by Sep 2026
        </span>
      </div>
    </div>
    <Caption lines={['Designed by C-DAC, then','manufactured in India.']}/>
    <ProofProgress timeSec={20} themeName="saffron"/>
  </AbsoluteFill>
);
