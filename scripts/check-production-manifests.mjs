import fs from 'node:fs';
import assert from 'node:assert/strict';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const hash=x=>typeof x==='string'&&/^[a-f0-9]{64}$/.test(x);
const ref=x=>x&&hash(x.sha256)&&typeof x.filename==='string'&&x.filename&&typeof x.libraryId==='string'&&x.libraryId;
const rows=read('content/registry.json').items;
const grandfathered=new Set(['BM-001','BM-002','BM-003','BM-004','BM-005']);
const files=fs.readdirSync('production').filter(p=>/^BM-\d+\.json$/.test(p));
const seen=new Set();
for(const file of files){
 const m=read('production/'+file),r=rows.find(x=>x.id===m.ideaId&&x.productionCode===m.productionCode);
 assert(r&&file===m.productionCode+'.json'&&!seen.has(r.id),'Bad manifest identity '+file);seen.add(r.id);
 assert(m.schemaVersion===1&&m.exampleOnly!==true&&m.scriptRevision&&m.storyPath===r.storyPath&&fs.existsSync(m.storyPath),'Missing structured approved brief '+file);
 assert(ref(m.source?.privateBundle),'Recoverable private editable source bundle required '+file);
 const story=read(m.storyPath).story;
 assert(Array.isArray(m.scenes)&&m.scenes.length===story.scenes.length,'Scene inventory mismatch '+file);
 for(const s of m.scenes)assert(ref(s.narration)&&ref(s.alignment)&&ref(s.cueMap),'Missing recoverable scene audio/alignment/cues '+file);
 assert(Array.isArray(m.assets)&&m.assets.length&&m.assets.every(a=>ref(a)&&a.provenance&&a.rightsEvidence),'Missing asset provenance/rights '+file);
 const v=m.render;assert(v?.width===1080&&v.height===1920&&v.fps===60&&v.silentHoldSeconds===1&&Number.isInteger(v.frameCount)&&v.frameCount>60&&v.command&&Object.keys(v.toolVersions||{}).length&&v.fonts?.length,'Incomplete rendering configuration '+file);
 assert(ref(m.qa?.technicalReport)&&Array.isArray(m.qa.ownerApprovals)&&Array.isArray(m.qa.rightsEvidence)&&ref(m.output),'Missing QA/output record '+file);
}
for(const r of rows.filter(x=>['uploaded','scheduled','published_owner_reported','published'].includes(x.stage)&&!grandfathered.has(x.productionCode)))assert(seen.has(r.id),'New release requires recoverable production manifest '+r.productionCode);
console.log('Production manifests checked; historical BM-001–005 missing records are explicit recovery backlog, not certified.');
