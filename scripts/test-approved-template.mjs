/**
 * Nonrendering regression checks for owner-approved Bharat Mode visual geometry.
 * This checks the exact center and protects HTML, shared Remotion progress and
 * old generic story bars from silently becoming asymmetrical again.
 */
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {
  SHORTS_WIDTH, SHORTS_HEIGHT, SHORTS_FPS,
  APPROVED_PROGRESS_GUTTER, approvedProgressBounds,
} from '../src/approved-layout.js';
assert.equal(SHORTS_WIDTH,1080);
assert.equal(SHORTS_HEIGHT,1920);
assert.equal(SHORTS_FPS,30);
assert.equal(APPROVED_PROGRESS_GUTTER,84);
const bounds=approvedProgressBounds();
assert.deepEqual(bounds,{left:84,right:84,width:912,center:540});
const files=[
  'previews/html/bharat-mode-motion-v6-mixed.html',
  'previews/html/bharat-mode-motion-v6-ivory.html',
  'previews/html/bharat-mode-motion-v6-dark.html',
];
for(const file of files){
  const source=readFileSync(file,'utf8');
  assert.match(source,/\.progress\{position:absolute;z-index:73;bottom:250px;left:84px;right:84px;/,
    'Centered 84px / 84px progress bar missing: '+file);
  assert.doesNotMatch(source,/\.progress\{[^}]*right:165px/,
    'Old asymmetric progress bar found in: '+file);
}
const v6=readFileSync('src/motion-v6.jsx','utf8');
assert.match(v6,/ApprovedShortsFrame/);
const shared=readFileSync('src/approved-shorts-template.jsx','utf8');
assert.match(shared,/left=\{APPROVED_PROGRESS_GUTTER\}/);
assert.match(shared,/right=\{APPROVED_PROGRESS_GUTTER\}/);
const legacy=readFileSync('src/short.jsx','utf8');
assert.match(legacy,/left=\{84\}\s*right=\{84\}/);
console.log('APPROVED: 1080x1920 template, centered 84px / 84px chapter progress, total 912px.');
console.log('Visual approval does not certify voice alignment or production render.');
