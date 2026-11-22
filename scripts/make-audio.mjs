/**
 * Rebuild the ORIGINAL committed Bharat Mode soundtrack and sound effects.
 * Usage: npm run audio:generate
 * The three WAV masters are tracked in Git; do not run at every build.
 * Sample rate 24kHz, mono PCM16. No third-party musical samples used.
 */
import fs from 'node:fs';
import path from 'node:path';
const RATE=24000;
function sound(name,duration,fn){
  const count=Math.round(RATE*duration),bytes=Buffer.alloc(44+count*2);
  bytes.write('RIFF',0);bytes.writeUInt32LE(36+count*2,4);bytes.write('WAVEfmt ',8);
  bytes.writeUInt32LE(16,16);bytes.writeUInt16LE(1,20);bytes.writeUInt16LE(1,22);
  bytes.writeUInt32LE(RATE,24);bytes.writeUInt32LE(RATE*2,28);
  bytes.writeUInt16LE(2,32);bytes.writeUInt16LE(16,34);
  bytes.write('data',36);bytes.writeUInt32LE(count*2,40);
  for(let i=0;i<count;i++){
    const t=i/RATE,v=Math.max(-.95,Math.min(.95,fn(t,duration)));
    bytes.writeInt16LE(Math.round(v*32767),44+i*2);
  }
  fs.mkdirSync(path.dirname(name),{recursive:true});
  fs.writeFileSync(name,bytes);
  console.log(name+' '+bytes.length+' bytes');
}
const chords=[[130.81,164.81,196,246.94],[110,130.81,164.81,196],[87.31,130.81,164.81,220],[98,146.83,196,246.94]];
sound('public/music/ambient.wav',9.6,(t,d)=>{
  const chord=chords[Math.min(3,Math.floor(t/2.4))],base=chord[0]/2;
  const edge=Math.min(1,t/.18,(d-t)/.18),b=t%0.6;
  const pad=chord.reduce((v,n,k)=>v+Math.sin(2*Math.PI*n*t+k*.43)*(.038+.015*Math.sin(Math.PI*t/9.6)**2),0);
  const bass=Math.sin(2*Math.PI*base*t)*.085;
  const seq=chord[Math.floor(t/.6)%4]*2;
  const pluck=.045*Math.exp(-9*b)*Math.sin(2*Math.PI*seq*t);
  const air=.009*Math.sin(2*Math.PI*3*t)*Math.sin(2*Math.PI*392*t);
  return edge*(pad+bass+pluck+air);
});
sound('public/sfx/mode-on.wav',.60,(t)=>{
  const env=Math.min(1,t/.018)*Math.exp(-4.8*t);
  const c=Math.sin(2*Math.PI*523.25*t)+.42*Math.sin(2*Math.PI*784*t);
  const hit=Math.sin(2*Math.PI*130.81*t)*Math.exp(-14*t)*.15;
  return .23*env*c+hit;
});
sound('public/sfx/metric-rise.wav',.25,(t)=>{
  const env=Math.min(1,t/.006)*Math.exp(-17*t);
  return .22*env*(Math.sin(2*Math.PI*(660*t+160*t*t))+.15*Math.sin(2*Math.PI*1320*t));
});
