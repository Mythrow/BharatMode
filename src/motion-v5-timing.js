/** Pure deterministic timing for the V5 review. Story groupings remain flexible. */
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
/** Scene-to-scene motion: outgoing moves left, incoming enters from right.
 * Both scenes are present for 0.64s, beginning 0.24s before each boundary.
 */
export function scenePoseAt(timeSec, index, beats=DEMO_BEATS, {duration=.64, lead=.24}={}) {
  const s=beats[index];
  let opacity=1, x=0, visible=true;
  if (index>0) {
    const p=easeOut((timeSec-(s.startSec-lead))/duration);
    opacity*=p;
    x+=150*(1-p);
    if (timeSec<s.startSec-lead) visible=false;
  }
  if (index<beats.length-1) {
    const p=easeOut((timeSec-(s.endSec-lead))/duration);
    opacity*=1-p;
    x-=110*p;
    if (timeSec>s.endSec+duration-lead) visible=false;
  }
  return {opacity:visible?opacity:0, translateX:x};
}
/** Returns a 0..1 wipe amount only during one of the scene boundaries. */
export function sceneWipeAt(timeSec,beats=DEMO_BEATS,{duration=.64,lead=.24}={}) {
  for (let i=1;i<beats.length;i++) {
    const progress=(timeSec-(beats[i].startSec-lead))/duration;
    if (progress>=0&&progress<=1) return progress;
  }
  return -1;
}
export function headlineCharsAt(text,localSec,charsPerSecond=25) {
  return text.slice(0,Math.min(text.length,Math.max(0,Math.floor(Math.max(0,localSec+.09)*charsPerSecond))));
}