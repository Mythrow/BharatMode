/**
 * Deterministic word-pop helpers. Works with real word-aligned voice timestamps.
 * The generated example schedule below is for a SILENT motion review only.
 */
export const clamp01=(v)=>Math.max(0,Math.min(1,v));

export const springWordEntrance=(elapsedSeconds)=>{
  const t=clamp01(elapsedSeconds/0.20);
  // From 60% to a restrained 112% overshoot, settling to exactly 100%.
  let scale;
  if(t<=0.6){
    const q=t/0.6;
    scale=0.6+0.52*(1-(1-q)**2);
  } else {
    const q=(t-0.6)/0.4;
    scale=1.12-0.12*(1-(1-q)**2);
  }
  return {scale,opacity:clamp01(elapsedSeconds/0.19)};
};

/** Returns up to lookback previously spoken words plus latest started word. */
export const wordsOnScreen=(words=[],timeSec,lookback=3)=>{
  let last=-1;
  for(let i=0;i<words.length;i++){
    if(timeSec>=words[i].start)last=i;
    else break;
  }
  if(last<0)return [];
  return words.slice(Math.max(0,last-lookback),last+1).map(w=>({
    ...w,
    isActive:timeSec>=w.start&&timeSec<w.end,
    ...springWordEntrance(timeSec-w.start)
  }));
};

/** Illustrative-only timing: do NOT use this for publication. */
export const demoWordTimings=(text,startSec,endSec)=>{
  const tokens=text.trim().split(/\s+/).filter(Boolean);
  const weights=tokens.map(w=>Math.max(2.5,Math.min(8.5,w.length)));
  const total=weights.reduce((a,b)=>a+b,0);
  const usable=endSec-startSec-.4;
  let t=startSec+.18;
  return tokens.map((token,i)=>{
    const begin=t;
    t+=usable*weights[i]/total;
    return {text:token,start:begin,end:t};
  });
};

/** Editorial group ranges, from explicitly supplied short phrase groups. */
export const groupWordRanges=(words=[],phrases=[])=>{
  if(!Array.isArray(phrases)||!phrases.length) return [];
  let cursor=0;
  const ranges=phrases.map((phrase,i)=>{
    const tokens=phrase.trim().split(/\s+/).filter(Boolean);
    const range={id:i,start:cursor,end:cursor+tokens.length};
    tokens.forEach((t,j)=>{
      if(words[cursor+j]?.text!==t) throw new Error('Caption groups must preserve transcript tokens and order');
    });
    cursor+=tokens.length;
    return range;
  });
  if(cursor!==words.length)throw new Error('Caption groups must cover every spoken word exactly once');
  return ranges;
};
/** Only the CURRENT editorial phrase remains on screen, revealed word by word. */
export const groupedVisibleWords=(words=[],groups=[],timeSec=0)=>{
  let latest=-1;
  for(let i=0;i<words.length;i++)if(timeSec>=words[i].start)latest=i;
  if(latest<0)return {group:-1,words:[]};
  const group=groups.findIndex(g=>latest>=g.start&&latest<g.end);
  if(group<0)return {group:-1,words:[]};
  const window=words.slice(groups[group].start,latest+1).map(w=>({
    ...w,isActive:timeSec>=w.start&&timeSec<w.end,
    ...springWordEntrance(timeSec-w.start)
  }));
  return {group,words:window};
};