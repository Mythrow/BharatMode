import assert from 'node:assert/strict';
import {springWordEntrance,wordsOnScreen,demoWordTimings} from '../src/motion-v3-timing.js';
for(const [age,expected] of [[0,.6],[.12,1.12],[.2,1],[1,1]]){
 const val=springWordEntrance(age);
 assert.ok(Math.abs(val.scale-expected)<.0001,'unexpected scale at '+age+': '+val.scale);
}
assert.equal(springWordEntrance(0).opacity,0);
assert.equal(springWordEntrance(.2).opacity,1);
const words=demoWordTimings('Bharat Mode moves',2,6);
assert.equal(words.length,3);
assert.equal(wordsOnScreen(words,1.9).length,0);
const first=wordsOnScreen(words,words[0].start);
assert.equal(first.length,1);
assert.equal(first[0].isActive,true);
assert.equal(first[0].scale,.6);
const after=wordsOnScreen(words,words.at(-1).end+.1);
assert.ok(after.every(w=>!w.isActive));
assert.ok(after.every(w=>w.opacity===1));
console.log('V3 caption spring timing and highlight tests passed');