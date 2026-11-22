/** Validate the owner-approved original cover and its 2560×1440 resampled export. */
import {createHash} from 'node:crypto';
import {readFileSync} from 'node:fs';
import assert from 'node:assert/strict';

const files=[
  {
    path:'public/brand/BM_Youtube_Cover.png',
    width:2048, height:1152, bytes:2557370,
    sha256:'cc732add91a1104492d06522db65871547918a482fae6166919e6c34b8a104ae'
  },
  {
    path:'public/brand/BM_Youtube_Cover_2560x1440.png',
    width:2560, height:1440, bytes:2233322,
    sha256:'a75d719a398e88bf5937bea6e27a3e50209994250be3927479de51037da564d6'
  }
];
for(const expected of files){
  const data=readFileSync(expected.path);
  assert.equal(data.subarray(0,8).toString('hex'),'89504e470d0a1a0a','Not PNG '+expected.path);
  assert.equal(data.length,expected.bytes,'Byte size mismatch '+expected.path);
  assert.equal(data.readUInt32BE(16),expected.width,'PNG width mismatch '+expected.path);
  assert.equal(data.readUInt32BE(20),expected.height,'PNG height mismatch '+expected.path);
  assert.equal(createHash('sha256').update(data).digest('hex'),expected.sha256,'Checksum mismatch '+expected.path);
  console.log('Approved cover validated: '+expected.path+' ('+expected.width+'×'+expected.height+')');
}
