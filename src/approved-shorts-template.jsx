/**
 * Owner-approved Bharat Mode visual frame, built from the reviewed V6 layout.
 *
 * Use this with story-specific motion and evidence as children, plus a caption
 * component built from timestamps of the actual narration recording.
 * Never replace the official badge/avatar SVG with a generated approximation.
 * BharatShort production composition consumes validated actual alignment and story-specific layers.
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BRAND as B} from './brand.js';
import {BrandAvatar} from './brand-assets.jsx';
import {BODY_FONT} from './fonts.js';
import {ChapterProgress} from './motion-system.jsx';
import {
  APPROVED_PROGRESS_GUTTER,
  APPROVED_PROGRESS_BOTTOM,
  APPROVED_PROGRESS_HEIGHT,
  APPROVED_PROGRESS_GAP,
} from './approved-layout.js';

/** Fixed story-independent chrome. Story-specific content is passed in as children. */
export const ApprovedShortsFrame=({
  children,
  chapters=[],
  timeSec=0,
  theme='ivory',
  topic='SCIENCE',
  caption=null,
})=>{
  const isDark=theme==='midnight';
  const pillBg=isDark?B.ivory:B.charcoal;
  const pillInk=isDark?B.charcoal:B.ivory;
  return <AbsoluteFill style={{overflow:'hidden',background:B.charcoal}}>
    {children}
    <div style={{position:'absolute',inset:0,zIndex:65,pointerEvents:'none'}}>
      <ChapterProgress chapters={chapters} timeSec={timeSec} themeName={theme}
        bottom={APPROVED_PROGRESS_BOTTOM}
        left={APPROVED_PROGRESS_GUTTER}
        right={APPROVED_PROGRESS_GUTTER}
        height={APPROVED_PROGRESS_HEIGHT}
        gap={APPROVED_PROGRESS_GAP}/>
    </div>
    <div style={{position:'absolute',top:89,left:86,right:72,zIndex:55,
      display:'flex',justifyContent:'space-between',alignItems:'center'}}>
      <BrandAvatar size={88}/>
      <div style={{padding:'17px 26px',borderRadius:50,
        background:pillBg,color:pillInk,
        fontFamily:BODY_FONT,fontWeight:500,fontSize:27,
        letterSpacing:1.4}}>{String(topic).toUpperCase()}</div>
    </div>
    {caption}
  </AbsoluteFill>;
};
