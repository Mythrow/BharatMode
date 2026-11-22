/** Pure timing utilities shared by the V2 Remotion demo.
 * These methods only select from supplied word boundaries; production timings
 * must come from actual audio alignment, not estimated from speech length.
 */
export const atTime=(chapters,sec)=>{
  if(!chapters?.length) return -1;
  const i=chapters.findIndex(c=>sec>=c.startSec&&sec<c.endSec);
  return i>=0?i:sec>=chapters.at(-1).endSec?chapters.length-1:0;
};
export const activeWordAt=(words,timeSec)=>{
  if(!words?.length) return -1;
  let active=-1;
  for(let i=0;i<words.length;i++){
    if(timeSec>=words[i].start) active=i;
    if(timeSec<words[i].start) break;
  }
  return active;
};
export const visibleWords=(words,timeSec,lookback=4)=>{
  const active=activeWordAt(words,timeSec);
  if(active<0) return [];
  return words.slice(Math.max(0,active-lookback),active+1).map((w,i,arr)=>({...w,isActive:i===arr.length-1}));
};
/** A demonstration-only timing generator; never use for publishing. */
export const makeIllustrativeWords=(text,startSec,endSec)=>{
  const tokens=text.trim().split(/\s+/);
  const weights=tokens.map(w=>Math.max(2.5,Math.min(8.5,w.length)));
  const total=weights.reduce((a,b)=>a+b,0);
  const usable=endSec-startSec-.35;
  let current=startSec+.15;
  return tokens.map((token,i)=>{
    const begin=current;
    current+=usable*weights[i]/total;
    return {text:token,start:begin,end:current};
  });
};