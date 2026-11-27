import fs from 'node:fs';
import assert from 'node:assert/strict';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const rows=read('content/registry.json').items;
const pages=new Map();
for(const file of fs.readdirSync('publishing').filter(p=>/^BM-\d+-release-page\.json$/.test(p))){
 const p=read('publishing/'+file),row=rows.find(x=>x.id===p.ideaId);
 assert(row&&row.productionCode===p.productionCode,'Unmatched release page '+file);
 assert(!pages.has(row.id),'Duplicate release page '+row.id);pages.set(row.id,p);
 const v=p.publication||{};
 for(const k of ['youtubeUrl','publishedAt','uploadedAt','scheduledAt','scheduleTime'])assert.equal(v[k]??null,row[k]??null,file+' '+k);
 if(row.stage==='published_owner_reported'||row.ownerConfirmedPublic===true){
  assert.equal(v.ownerConfirmedPublic,true,file+' owner report');
  assert.equal(v.reportedOn??v.publicationReportedOn??null,row.publicationReportedOn??null,file+' report date');
 }else assert.notEqual(v.ownerConfirmedPublic,true,file+' contradictory public report');
 if(row.stage==='published'){
  assert.equal(v.publishApprovedByOwner,true,file+' explicit publication sign-off');
  assert.deepEqual(v.publicationVerification,row.publicationVerification,file+' independent verification evidence');
 }
 if(['uploaded','scheduled'].includes(row.stage))assert.equal(v.uploadConfirmedByOwner,true,file+' upload evidence');
 for(const k of ['video','thumbnail']){const a=p.media?.[k];assert(a&&/^[a-f0-9]{64}$/.test(a.sha256)&&a.libraryId&&a.filename&&typeof a.ownerApproved==='boolean',file+' missing media record '+k);}
}
for(const row of rows.filter(x=>['uploaded','scheduled','published_owner_reported','published'].includes(x.stage)))assert(pages.has(row.id),'Missing release page '+row.id);
console.log('Release record reconciliation passed: '+pages.size+' pages.');
