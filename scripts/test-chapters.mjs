/**
 * Chapter grouping invariants: no rigid chapter count, ordered timing and no
 * blank/inverted segments. This test intentionally has no Remotion dependencies.
 */
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {resolveStoryChapters} from '../src/chapter-timing.js';
const examples=['param-rudra','icmr-tech-transfer'];
const counts=[];
for (const slug of examples) {
  const story=JSON.parse(readFileSync('stories/'+slug+'.json','utf8')).story;
  const beats=resolveStoryChapters(story);
  const total=story.scenes.reduce((sum,s)=>sum+s.duration,0);
  assert.ok(beats.length>0, slug+' must have chapters');
  assert.equal(beats[0].startSec,0);
  assert.equal(beats.at(-1).endSec,total);
  for (let i=0;i<beats.length;i++) {
    assert.ok(beats[i].endSec>beats[i].startSec,slug+' has empty beat');
    if (i) assert.equal(beats[i].startSec,beats[i-1].endSec,slug+' has timing gap');
  }
  counts.push(beats.length);
  console.log(slug+': '+beats.length+' editorial chapters across '+story.scenes.length+' scenes');
}
assert.notEqual(counts[0],counts[1],'Examples should demonstrate flexible chapter groupings');
const implicit=resolveStoryChapters({scenes:[{duration:2,kicker:'A'},{duration:4,kicker:'B'}]});
assert.equal(implicit.length,2);
assert.equal(implicit[1].endSec,6);
console.log('Story-driven chapter timing passed.');
