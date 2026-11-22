/**
 * Bharat Mode reusable motion and editorial UI primitives (V1 DRAFT).
 * Sources and publication dates go in YouTube descriptions and research metadata,
 * except any factual stage/date qualifier essential to understanding a claim.
 * UI assumes an approved BM SVG avatar, never redraws logo paths.
 */
import React from 'react';
import {Easing,interpolate,spring,useCurrentFrame} from 'remotion';
import {BRAND as B} from './brand.js';
import {BODY_FONT} from './fonts.js';
import {APPROVED_PROGRESS_GUTTER} from './approved-layout.js';

const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'};
const ease=Easing.bezier(0.2,0.8,0.2,1);
export const revealStyle=(frame,{delay=0,duration=14,offsetY=22}={})=>{
  const opacity=interpolate(frame-delay,[0,duration],[0,1],clamp);
  const y=interpolate(frame-delay,[0,duration],[offsetY,0],{...clamp,easing:ease});
  return {opacity,transform:'translateY('+y+'px)'};
};
export const numberReveal=(frame,value,{delay=0,duration=26}={})=>{
  const t=interpolate(frame-delay,[0,duration],[0,1],{...clamp,easing:ease});
  return Math.round(value*t);
};
export const gentlePhotoScale=(frame,durationFrames)=>(
  interpolate(frame,[0,Math.max(1,durationFrames)],[1,1.04],clamp)
);

export const TopicPill=({topic='SCIENCE',themeName='ivory'})=>{
  const dark=themeName==='midnight'||themeName==='saffron';
  const bg=themeName==='midnight'?B.ivory:B.charcoal;
  const fg=themeName==='midnight'?B.charcoal:B.ivory;
  return <div style={{
    minHeight:62,minWidth:165,maxWidth:310,borderRadius:80,
    padding:'0 24px',background:bg,color:fg,display:'flex',
    justifyContent:'center',alignItems:'center',
    fontFamily:BODY_FONT,fontWeight:500,fontSize:23,
    letterSpacing:1.2,whiteSpace:'nowrap'
  }}>{String(topic).toUpperCase()}</div>;
};

/**
 * Equal-width segments represent STORY CHAPTERS, not fixed-length time slices.
 * Each segment fills linearly over that chapter's real seconds.
 * There is no numeric chapter display; the count comes from the story metadata.
 */
export const ChapterProgress=({
  chapters=[],timeSec=null,themeName='ivory',bottom=258,left=APPROVED_PROGRESS_GUTTER,right=APPROVED_PROGRESS_GUTTER,
  height=10,gap=13
})=>{
  const frame=useCurrentFrame();
  const time=timeSec==null?frame/30:timeSec;
  const onSaffron=themeName==='saffron';
  const activeColor=onSaffron?B.charcoal:B.primary;
  const track=themeName==='midnight'?'#3B464F':onSaffron?'rgba(11,16,24,0.24)':'#D9D4CF';
  if (!chapters.length) return null;
  return <div aria-label="Story chapter progress" style={{
    position:'absolute',left,right,bottom,height,
    display:'flex',gap,alignItems:'stretch'
  }}>
    {chapters.map((chapter,i)=>{
      const seconds=Math.max(0.001,chapter.endSec-chapter.startSec);
      const fraction=Math.max(0,Math.min(1,(time-chapter.startSec)/seconds));
      return <div key={chapter.id||i} style={{
        position:'relative',flex:1,height:'100%',
        borderRadius:99,background:track,overflow:'hidden'
      }}>
        <div style={{height:'100%',width:(fraction*100)+'%',
          background:activeColor,borderRadius:99}}/>
      </div>;
    })}
  </div>;
};

// A separate caption surface is used only when a timed transcription exists.
// Demo samples have manually authored cues, not ASR/TTS alignment.
export const CaptionPanel=({lines=[],isDark=false})=>{
  if (!lines.length) return null;
  return <div style={{
    position:'absolute',left:80,right:165,top:1400,
    minHeight:142,borderRadius:26,padding:'20px 24px',
    background:isDark?'rgba(255,247,235,.94)':'rgba(11,16,24,.93)',
    display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',
    gap:3
  }}>
    {lines.slice(0,2).map((line,i)=><div key={i} style={{
      fontFamily:BODY_FONT,fontWeight:700,fontSize:43,
      lineHeight:1.27,textAlign:'center',
      color:isDark?B.charcoal:B.ivory
    }}>{line}</div>)}
  </div>;
};
