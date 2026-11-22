/** Confirm that Git contains the exact owner-approved channel cover.
 * Run after adding public/brand/BM_Youtube_Cover.png.
 */
import {createHash} from 'node:crypto';
import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
const path='public/brand/BM_Youtube_Cover.png';
if (!existsSync(path)) {
  console.error('Missing approved cover: '+path);
  console.error('Upload the original PNG before using the channel banner from this repo.');
  process.exit(1);
}
const file=readFileSync(path);
assert.equal(file.length,2557370,'Unexpected file size');
assert.equal(file.subarray(0,8).toString('hex'),'89504e470d0a1a0a','Not a PNG');
const width=file.readUInt32BE(16),height=file.readUInt32BE(20);
assert.equal(width,2048,'Wrong banner width');
assert.equal(height,1152,'Wrong banner height');
const digest=createHash('sha256').update(file).digest('hex');
assert.equal(digest,'cc732add91a1104492d06522db65871547918a482fae6166919e6c34b8a104ae','Source file differs from owner-approved original');
console.log('Approved channel banner verified: '+path+' at '+width+'x'+height);
