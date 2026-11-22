import React from 'react';
import {AbsoluteFill} from 'remotion';
import {BRAND as B, getTheme} from './brand.js';
import {DISPLAY_FONT, BODY_FONT} from './fonts.js';

const format=(n)=>Number(n).toLocaleString('en-IN');
export const BharatThumbnail = ({story})=>{
  const theme=getTheme(story.visualTheme);
  const style=story.thumbnailStyle || 'statement';
  const metric=story.scenes?.find(s=>s.kind==='metric'||s.kind==='impact');
  const isStat=style==='stat'&&metric;
  const words=story.thumbnailText || story.title || 'BHARAT MODE';
  const splash=style==='diagram'||style==='split';
  return <AbsoluteFill style={{
    background:theme.bg,color:theme.ink,overflow:'hidden',
    fontFamily:BODY_FONT
  }}>
    <div style={{position:'absolute',right:-270,top:350,width:750,height:750,borderRadius:750,
      background:theme.glow,opacity:.8}}/>
    <div style={{position:'absolute',left:-330,bottom:180,width:760,height:760,borderRadius:760,
      border:'90px solid '+theme.soft,opacity:.75}}/>
    <div style={{position:'absolute',left:85,right:85,top:124,display:'flex',alignItems:'center',gap:18}}>
      <div style={{width:20,height:20,background:theme.accent,borderRadius:30}}/>
      <div style={{fontFamily:DISPLAY_FONT,fontSize:38,fontWeight:800}}>BHARAT MODE</div>
    </div>
    <div style={{position:'absolute',left:85,right:85,top:430}}>
      <div style={{
        display:'inline-block',background:theme.soft,color:theme.accentText,
        borderRadius:50,padding:'15px 22px',fontSize:27,fontWeight:800,
        marginBottom:58,textTransform:'uppercase'
      }}>{story.category}</div>
      {isStat&&<div style={{
        fontFamily:DISPLAY_FONT,fontSize:172,fontWeight:800,
        letterSpacing:-8,lineHeight:1,color:theme.dataColor,
        marginBottom:15
      }}>{format(metric.number)}{metric.suffix||''}</div>}
      <div style={{
        fontFamily:DISPLAY_FONT,fontWeight:800,lineHeight:1.04,
        fontSize:isStat?102:120,letterSpacing:-2.6,
        maxWidth:920,overflowWrap:'break-word'
      }}>{words}</div>
      <div style={{marginTop:62,width:150,height:12,background:theme.accent,borderRadius:12}}/>
      {splash&&<div style={{marginTop:95,display:'flex',gap:35}}>
        {[0,1,2].map((n)=><div key={n} style={{height:180,width:180,borderRadius:n===1?90:32,
          background:n===1?theme.accent:theme.surface,border:'4px solid '+theme.border}}/>)}
      </div>}
    </div>
    <div style={{position:'absolute',left:85,right:85,bottom:260,fontSize:30,color:theme.muted}}>
      {story.sourceShort} · {story.sourcePublished}
    </div>
    <div style={{position:'absolute',left:85,right:85,bottom:205,height:6,borderRadius:10,background:theme.accent}}/>
  </AbsoluteFill>;
};
