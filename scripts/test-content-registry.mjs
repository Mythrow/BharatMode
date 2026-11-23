import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';

const SOURCE=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
let passed=0;
function fixture(){
  const d=fs.mkdtempSync(path.join(os.tmpdir(),'bm-content-registry-'));
  for(const p of ['scripts/content-registry.mjs','content/registry.json','content/CONTENT_LOG.md',
                  'content/research/BM-0001.md','content/research/BM-0002.md',
                  'content/research/BM-0003.md','content/research/BM-0004.md',
                  'publishing/queue.json','stories/param-rudra.json','stories/icmr-tech-transfer.json']){
    const out=path.join(d,p);fs.mkdirSync(path.dirname(out),{recursive:true});fs.copyFileSync(path.join(SOURCE,p),out);
  }
  return d;
}
function run(d,...args){return spawnSync(process.execPath,['scripts/content-registry.mjs',...args],{cwd:d,encoding:'utf8'});}
function test(name,fn){
  const d=fixture();try{fn(d);passed++;console.log(`PASS ${name}`);}finally{fs.rmSync(d,{recursive:true,force:true});}
}
function good(r){assert.equal(r.status,0,r.stderr||r.stdout);}
function bad(r,match){assert.notEqual(r.status,0,'Expected failure');assert.match(r.stderr,match);}
const add=(d,...extra)=>run(d,'add','--title','L&T new Chennai GPU order','--slug','lt-duplicate-test',
  '--story-key','lt-chennai-new-synthetic-update-2027-01-03','--topic-key','unrelated-topic',
  '--primary-source','https://example.org/release-unique-2027','--event-date','2027-01-03','--source-date','2027-01-03',...extra);

test('baseline has four permanent content identities, exact log and stage counts',d=>{
  const r=run(d,'check');good(r);assert.match(r.stdout,/4 IDs \| idea 2 \| in_progress 2 \| published 0/);
});
test('list and search span both Idea and In Progress',d=>{
  const r=run(d,'find','Vyoma');good(r);assert.match(r.stdout,/BM-0003/);
  const l=run(d,'list','--stage','idea');good(l);assert.match(l.stdout,/BM-0002/);assert.doesNotMatch(l.stdout,/BM-0001/);
});
test('reject duplicated event key and avoid reserving an ID',d=>{
  const r=add(d,'--story-key','lt-chennai-ai-b300-additional-order-2026-11-23');bad(r,/duplicate event\/story identity/);
  assert.equal(JSON.parse(fs.readFileSync(path.join(d,'content/registry.json'),'utf8')).nextSequence,5);
  assert.equal(fs.existsSync(path.join(d,'content/research/BM-0005.md')),false);
});
test('reject primary-source URL duplicate even with a distinct event key',d=>{
  const r=add(d,'--primary-source','https://nsearchives.nseindia.com/corporate/PAM_23112026093338_PressRelease23112026.pdf?utm_source=x');bad(r,/source URL re-used/);
});
test('reject duplicate title even with a distinct source',d=>{
  const r=add(d,'--title','L&T expands Chennai AI infrastructure with new B300 order');bad(r,/Near-identical titles/);
});
test('reject repeated topic with no cross-linked, distinct development',d=>{
  const r=add(d,'--topic-key','lt-chennai-ai-infrastructure');bad(r,/topicKey overlaps|cross-link/);
});
test('allow distinct later update in same topic only with cross-link and explanation',d=>{
  const r=add(d,'--title','A separate 2027 L&T GPU deployment milestone','--topic-key','lt-chennai-ai-infrastructure',
    '--related','BM-0003','--distinguishing-update','New 2027 operational milestone with a separate original source and date.');good(r);
  good(run(d,'check'));
  const x=JSON.parse(fs.readFileSync(path.join(d,'content/registry.json'),'utf8'));
  assert.equal(x.items.at(-1).id,'BM-0005');assert.equal(x.nextSequence,6);
});
test('cannot skip Idea and publish an idea directly',d=>{
  bad(run(d,'move','BM-0002','published','--note','No skip','--published-at','2026-11-23',
    '--youtube-url','https://www.youtube.com/shorts/abcdefghijk','--approved-by-owner'),/Must move Idea/);
});
test('moving to In Progress requires a reason and creates stage history',d=>{
  bad(run(d,'move','BM-0002','in_progress'),/explicit --note/);
  good(run(d,'move','BM-0002','in_progress','--note','Selected for script development'));
  good(run(d,'check'));
  const x=JSON.parse(fs.readFileSync(path.join(d,'content/registry.json'),'utf8'));
  assert.equal(x.items[1].stage,'in_progress');assert.equal(x.items[1].stageHistory.length,2);
});
test('publishing requires owner sign-off, video URL, date and a reason',d=>{
  bad(run(d,'move','BM-0003','published','--note','Published','--published-at','2026-11-23',
    '--youtube-url','https://www.youtube.com/watch?v=abcdefghijk'),/approved-by-owner/);
  bad(run(d,'move','BM-0003','published','--note','Published','--published-at','2026-11-23',
    '--youtube-url','https://example.com/short','--approved-by-owner'),/YouTube/);
  good(run(d,'move','BM-0003','published','--note','Final upload and editorial rights QA approved',
    '--published-at','2026-11-23','--youtube-url','https://www.youtube.com/shorts/abcdefghijk','--approved-by-owner'));
  good(run(d,'check'));
  const x=JSON.parse(fs.readFileSync(path.join(d,'content/registry.json'),'utf8'));
  assert.equal(x.items[2].stage,'published');assert.equal(x.items[2].youtubeUrl,'https://www.youtube.com/shorts/abcdefghijk');
  bad(run(d,'move','BM-0003','in_progress','--note','Bad revert'),/Must move Idea/);
});
test('fail when generated dashboard edited without sync',d=>{
  fs.appendFileSync(path.join(d,'content/CONTENT_LOG.md'),'\nManual stale edit\n');
  bad(run(d,'check'),/out of sync/);
  good(run(d,'sync'));good(run(d,'check'));
});
test('reject a missing research sheet',d=>{
  fs.unlinkSync(path.join(d,'content/research/BM-0004.md'));
  bad(run(d,'check'),/missing research file/);
});
test('reject unregistered, duplicate or published slugs in queue',d=>{
  const q=path.join(d,'publishing/queue.json');const d1=JSON.parse(fs.readFileSync(q,'utf8'));
  d1.slugs.push('imaginary-story');fs.writeFileSync(q,JSON.stringify(d1));
  bad(run(d,'check'),/not registered/);
});
test('reject tampered ID or stage history',d=>{
  const f=path.join(d,'content/registry.json'),r=JSON.parse(fs.readFileSync(f,'utf8'));
  r.items[0].stage='published';fs.writeFileSync(f,JSON.stringify(r));
  bad(run(d,'check'),/stage differs from stageHistory|publishedAt/);
});
console.log(`Content registry tests passed: ${passed}`);