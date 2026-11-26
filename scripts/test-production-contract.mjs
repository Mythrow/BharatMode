import assert from 'node:assert/strict';
import {validateProduction,frameState,typed,leadCue,MUSIC_SHA,FPS,HOLD_FRAMES} from '../src/production-contract.js';
// Synthetic unit fixture ONLY; never a real narration, render or publication approval.
const hash='a'.repeat(64),master='b'.repeat(64);
const scene={kicker:'News',headline:'A new milestone',narration:'India builds more.'};
const alignment={source:'final-audio-acoustic-alignment',aligner:'whisperx',transcript:scene.narration,audio:{sha256:hash,durationSeconds:2},qa:{exactWordMatch:true,alignedWords:3},words:[{text:'India',start:.1,end:.4},{text:'builds',start:.5,end:.8},{text:'more.',start:1,end:1.3}]};
const record={wavPath:'production-private/test.wav',theme:'saffron',backgroundId:'test',alignment,background:[{id:'bg',type:'circle',bounds:[0,0,100,100],fill:'#283039',motion:{dx:5,dy:2,period:4}}],artwork:[{id:'bar',type:'bar',bounds:[100,600,300,50],fill:'#283039',cue:'build'}],cues:[{id:'build',wordIndex:1,originalSec:.5,adjustedSec:.15}]};
const make=()=>({story:{contentId:'ID-999',scenes:[scene],chapters:[{id:'c',sceneStartIndex:0}]},production:{schemaVersion:1,width:1080,height:1920,fps:60,productionCode:'BM-999',scriptRevision:'test only',musicSourceSha256:MUSIC_SHA,mixPreset:'B',musicResolveSeconds:.8,master:{path:'production-private/master.wav',sha256:master,frameCount:228},scenes:[record],assets:[{path:record.wavPath,sha256:hash,provenance:'unit fixture',rights:'unit fixture'},{path:'production-private/master.wav',sha256:master,provenance:'unit fixture',rights:'unit fixture'}]}});
let p=validateProduction(make());assert.equal(p.narrationFrames,120);assert.equal(p.audibleFrames,168);assert.equal(p.durationInFrames,228);assert.equal(HOLD_FRAMES,FPS);assert.equal(frameState(p,168).holding,true);assert.equal(frameState(p,227).visualFrame,167);assert.equal(frameState(p,168).progressSec,2.8);assert.equal(typed('Meet',0),'M');assert.equal(typed('Meet',1),'Meet');assert.equal(leadCue({start:.1}),0);
for(const [change,error] of [
 [x=>x.production.fps=30,/Native/],
 [x=>x.production.scenes[0].alignment.transcript='wrong',/transcript/],
 [x=>x.production.scenes[0].alignment.source='demo',/Real final-audio/],
 [x=>x.production.scenes[0].cues[0].adjustedSec=.5,/anticipatory/],
 [x=>x.production.scenes[0].artwork[0].bounds=[50,450,200,80],/safe regions/],
 [x=>x.production.master.frameCount=227,/timeline/],
 [x=>x.production.assets[0].sha256='c'.repeat(64),/Narration WAV/],
 [x=>x.production.musicSourceSha256='c'.repeat(64),/MUSIC-06/],
 [x=>x.production.scenes[0].theme='ivory',/Saffron/],
 [x=>x.production.scenes[0].artwork[0].cue='missing',/actual acoustic cue/],
]){const x=structuredClone(make());change(x);assert.throws(()=>validateProduction(x),error);}
console.log('Production contract checks passed (synthetic fixtures; no real media rendered).');
