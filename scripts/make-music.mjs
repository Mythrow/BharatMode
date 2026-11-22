/**
 * Reproducible ORIGINAL quiet ambient music for local demo renders.
 * No music samples, copyrighted melodies, or third-party audio required.
 */
import fs from 'node:fs';
import path from 'node:path';
const sampleRate = 22050;
const seconds = 52;
const total = sampleRate * seconds;
const pcm = Buffer.alloc(44 + total*2);
pcm.write('RIFF',0);
pcm.writeUInt32LE(36+total*2,4);
pcm.write('WAVEfmt ',8);
pcm.writeUInt32LE(16,16);
pcm.writeUInt16LE(1,20);
pcm.writeUInt16LE(1,22);
pcm.writeUInt32LE(sampleRate,24);
pcm.writeUInt32LE(sampleRate*2,28);
pcm.writeUInt16LE(2,32);
pcm.writeUInt16LE(16,34);
pcm.write('data',36);
pcm.writeUInt32LE(total*2,40);
const notes=[110,138.59,164.81,196];
for(let i=0;i<total;i++) {
  const t=i/sampleRate;
  const fadeIn=Math.min(1,t/2),fadeOut=Math.min(1,(seconds-t)/2);
  const swell=0.7+0.3*Math.sin(2*Math.PI*t/19);
  const chord=notes.reduce((v,n,k)=>v+Math.sin(2*Math.PI*n*t+k*0.8)*0.18,0);
  const shimmer=Math.sin(2*Math.PI*440*t)*0.016*Math.sin(Math.PI*t/8)**2;
  const value=Math.max(-1,Math.min(1,(chord+shimmer)*swell*fadeIn*fadeOut*0.4));
  pcm.writeInt16LE(Math.round(value*32767),44+i*2);
}
fs.mkdirSync(path.join('public','music'),{recursive:true});
fs.writeFileSync(path.join('public','music','ambient.wav'),pcm);
console.log('Created original demo audio: public/music/ambient.wav');
