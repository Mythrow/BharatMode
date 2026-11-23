/**
 * Approved V6 positioned caption overlay driven by *measured word timestamps*.
 * Use as <ApprovedShortsFrame caption={<AlignedNarrationCaptions ... />} />.
 * This is deliberately separate from the immutable approved V6 template.
 */
import React from 'react';
import {BRAND as B} from './brand.js';
import {BODY_FONT} from './fonts.js';
import {groupAlignedWords, visibleAlignedCaption} from './aligned-caption-timing.js';

const clamp = value => Math.max(0,Math.min(1,value));
export function AlignedNarrationCaptions({alignment,timeSec,theme='ivory'}) {
  const groups = groupAlignedWords(alignment);
  const visible = visibleAlignedCaption(groups,timeSec);
  if (!visible || !visible.visibleWords.length) return null;
  const ink = theme==='ivory'?B.graphite:B.ivory;
  const highlight = theme==='ivory'?B.saffronText:'#FFBE91';
  const backing = theme==='midnight'?'rgba(23,40,50,.30)':
    theme==='ivory'?'rgba(11,16,24,.10)':'rgba(11,16,24,.18)';
  const length = visible.words.reduce((s,w)=>s+w.text.length,0);
  const size = Math.max(42,Math.min(57,Math.floor(730/(Math.max(1,length)*.59+visible.words.length*.25))));
  const entered = clamp((timeSec-visible.start)/.12);
  return <div style={{position:'absolute',zIndex:60,top:1405,left:140,right:140,
    height:175,display:'flex',justifyContent:'center',alignItems:'center',pointerEvents:'none'}}>
    <div style={{display:'inline-flex',justifyContent:'center',alignItems:'center',
      width:'max-content',maxWidth:'100%',minHeight:112,
      padding:'18px 24px',borderRadius:12,background:backing,
      boxShadow:'0 5px 20px #0000000C',backdropFilter:'blur(5px)',
      opacity:entered,gap:14,whiteSpace:'nowrap'}}>
      {visible.visibleWords.map((w,i)=>{
        // Owner-approved 0.2s word pop: 60% → 112% → 100%, never shifts caption box.
        const x=clamp(w.ageSeconds/.20);
        const scale = x<.55 ? .60+(.52*x/.55) : 1.12-(.12*(x-.55)/.45);
        return <span key={`${w.start}-${i}`} style={{fontFamily:BODY_FONT,
          fontSize:size,fontWeight:700,lineHeight:1.25,whiteSpace:'nowrap',
          color:w.isActive?highlight:ink,
          opacity:clamp(w.ageSeconds/.08),
          textShadow:theme==='ivory'?'none':'0 1px 5px #0B101878',
          transform:`scale(${scale})`,transformOrigin:'center 65%'}}>{w.text}</span>;
      })}
    </div>
  </div>;
}