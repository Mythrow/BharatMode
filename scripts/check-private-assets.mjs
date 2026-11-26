import {execFileSync} from 'node:child_process';
import assert from 'node:assert/strict';
const allowed=new Set(['public/music/ambient.wav','public/sfx/metric-rise.wav','public/sfx/mode-on.wav']);
const files=execFileSync('git',['ls-files','-z'],{encoding:'utf8'}).split('\0').filter(Boolean);
for(const file of files){
 const restricted=/^(private|out|renders|reference-audio|public\/production-private|public\/voice)\//.test(file)||/\.(mp4|mov|mkv|webm|avi|gif|wav|mp3|flac|m4a|aac|ogg|zip|7z|tar\.gz|pem|key|pfx)$/i.test(file)||/(^|\/)\.env(?:\.|$)/.test(file)&&file!=='.env.example';
 assert(!restricted||allowed.has(file),'Restricted production asset or credential tracked: '+file);
}
console.log('Tracked private-media/credential path check passed. Not a substitute for secret/rights review.');
