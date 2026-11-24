import assert from 'node:assert/strict';
import {validateAlignedWords,groupAlignedWords,visibleAlignedCaption} from '../src/aligned-caption-timing.js';
const alignment={
  schemaVersion:1,source:'final-audio-acoustic-alignment',
  audio:{durationSeconds:4,sha256:'a-valid-audio-digest'},
  qa:{alignedWords:7,exactWordMatch:true,humanPronunciationReview:'PENDING',publishReady:false},
  words:[
    {text:'India',start:.1,end:.4},
    {text:'is',start:.42,end:.6},
    {text:'building',start:.61,end:1.05},
    {text:'more.',start:1.06,end:1.38},
    {text:'Meet',start:1.8,end:2.13},
    {text:'PARAM',start:2.16,end:2.6},
    {text:'Rudra.',start:2.61,end:3.2},
  ]
};
const groups=groupAlignedWords(alignment);
assert.equal(validateAlignedWords(alignment).length,7);
assert.equal(groups.length,2,'sentence boundary should start new phrase');
assert.equal(groups[0].words.map(w=>w.text).join(' '),'India is building more.');
assert.equal(groups[1].words.map(w=>w.text).join(' '),'Meet PARAM Rudra.');
assert.equal(visibleAlignedCaption(groups,0),null,'no caption before audio');
assert.deepEqual(visibleAlignedCaption(groups,.12).visibleWords.map(w=>w.text),['India']);
assert.equal(visibleAlignedCaption(groups,1.28).visibleWords.at(-1).isActive,true);
assert.equal(visibleAlignedCaption(groups,1.8).visibleWords.length,1);
assert.equal(visibleAlignedCaption(groups,3.7),null,'old group must disappear');
const long={...alignment,qa:{...alignment.qa,alignedWords:5},words:[
  {text:'Amazingly',start:.1,end:.3},{text:'complex',start:.31,end:.6},
  {text:'computer',start:.7,end:1.1},{text:'systems',start:1.11,end:1.6},
  {text:'exist',start:1.61,end:1.9},
]};
assert.ok(groupAlignedWords(long).every(g=>g.words.map(w=>w.text).join(' ').length<=27));
assert.throws(()=>groupAlignedWords({...alignment,source:'demo-generated'}),/Real final-audio alignment/);
assert.throws(()=>groupAlignedWords({...alignment,words:alignment.words.slice(0,6)}),/acoustic word match/);
assert.throws(()=>groupAlignedWords({...alignment,words:alignment.words.map((w,i)=>i===1?{...w,start:.2}:w)}),/Invalid acoustic/);
assert.throws(()=>groupAlignedWords({...alignment,qa:{...alignment.qa,exactWordMatch:false}}),/exact acoustic/);
console.log('PASS: 13 assertions on validated real-alignment schema, V6 phrase boundaries, visibility and rejection rules');

// Post-launch style regression: no shadow, blur or colored backing.
import {CAPTION_RADIUS,captionSurfaceStyle,captionInkStyle} from '../src/caption-style.js';
assert.equal(CAPTION_RADIUS,32);
for(const theme of ['ivory','midnight','saffron']){
 const surface=captionSurfaceStyle(theme);
 assert.equal(surface.borderRadius,32);assert.equal(surface.boxShadow,'none');assert.equal(surface.backdropFilter,'none');assert.match(surface.background,/^rgba\(11,16,24,\.(10|30|18)\)$/);
}
assert.equal(captionInkStyle.textShadow,'none');
console.log('PASS: post-launch caption style invariants');
