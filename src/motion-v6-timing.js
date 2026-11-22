/** Pure deterministic timing for the V6 review. Story groupings remain flexible. */
export const clamp01 = value => Math.max(0, Math.min(1, value));
export const easeOut = value => 1 - (1 - clamp01(value)) ** 3;
export const DEMO_BEATS = [
  {id:'origin',startSec:0,endSec:5,theme:'saffron'},
  {id:'deployed',startSec:5,endSec:10.5,theme:'midnight'},
  {id:'research',startSec:10.5,endSec:16,theme:'ivory'}
];
export function currentBeatAt(timeSec, beats=DEMO_BEATS) {
  let latest=0;
  for (let i=1;i<beats.length;i++) if (timeSec>=beats[i].startSec) latest=i;
  return latest;
}
/** Scene-to-scene motion: outgoing drifts 12px left, incoming drifts 18px from right.
 * Both scenes are present for 0.34s, beginning 0.17s before each boundary.
 */
export function scenePoseAt(timeSec, index, beats=DEMO_BEATS, {duration=.34, lead=.17}={}) {
  const s=beats[index];
  let opacity=1, x=0, visible=true;
  if (index>0) {
    const p=easeOut((timeSec-(s.startSec-lead))/duration);
    opacity*=p;
    x+=18*(1-p);
    if (timeSec<s.startSec-lead) visible=false;
  }
  if (index<beats.length-1) {
    const p=easeOut((timeSec-(s.endSec-lead))/duration);
    opacity*=1-p;
    x-=12*p;
    if (timeSec>s.endSec+duration-lead) visible=false;
  }
  return {opacity:visible?opacity:0, translateX:x};
}
export function headlineCharsAt(text,localSec,charsPerSecond=25) {
  return text.slice(0,Math.min(text.length,Math.max(0,Math.floor(Math.max(0,localSec+.09)*charsPerSecond))));
}