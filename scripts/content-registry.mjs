/**
 * Bharat Mode content identity + stage ledger.
 * Single source of truth: content/registry.json; generated human log: content/CONTENT_LOG.md.
 * No third-party services or dependencies. Run from the repository root.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const REGISTRY_PATH = path.join(ROOT, 'content/registry.json');
const LOG_PATH = path.join(ROOT, 'content/CONTENT_LOG.md');
const QUEUE_PATH = path.join(ROOT, 'publishing/queue.json');
const STAGES = ['idea','in_progress','published'];
const LABELS = {idea:'Idea',in_progress:'In Progress',published:'Published'};
const PRIORITIES = ['high','medium','low'];
const ID_RE = /^ID-(\d{3,})$/;
const PRODUCTION_RE=/^BM-(\d{3,})$/;
function nextProductionCode(r){const used=new Set(r.items.map(x=>x.productionCode));let n=1;while(used.has(`BM-${String(n).padStart(3,'0')}`))n++;return `BM-${String(n).padStart(3,'0')}`;}
function matchId(x,id){return [x.id,x.productionCode,x.legacyId].filter(Boolean).some(y=>y.toLowerCase()===String(id).toLowerCase());}
const ISO_DATE = /^\d{4}-\d{2}-\d{2}$/;
const EVENT_DATE = /^\d{4}-\d{2}(?:-\d{2})?$/;
const STOP = new Set('the an a and of to for with from into by is are was were new in india indian how why its our on more another an as gets get at this that has have about using added announces announced expands expansion research major project first facility'.split(' '));

function die(message){throw new Error(message);}
function readJSON(file){return JSON.parse(fs.readFileSync(file,'utf8'));}
function daysAreValid(date,monthly=false){
  if(monthly && /^\d{4}-\d{2}$/.test(date)) return +date.slice(5)<=12 && +date.slice(5)>=1;
  if(!ISO_DATE.test(date))return false;
  const dt=new Date(`${date}T00:00:00.000Z`);
  return !Number.isNaN(dt.valueOf()) && dt.toISOString().slice(0,10)===date;
}
function todayIST(){
  const p=new Intl.DateTimeFormat('en-GB',{timeZone:'Asia/Kolkata',year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(new Date());
  const get=t=>p.find(x=>x.type===t).value;
  return `${get('year')}-${get('month')}-${get('day')}`;
}
function normalizeWords(s){
  return [...new Set(String(s||'').toLowerCase().replace(/[^a-z0-9]+/g,' ').split(/\s+/).filter(w=>w.length>2&&!STOP.has(w)))];
}
function overlap(a,b){
  const x=new Set(normalizeWords(a)),y=new Set(normalizeWords(b));
  if(!x.size||!y.size)return 0;
  return [...x].filter(t=>y.has(t)).length / new Set([...x,...y]).size;
}
function canonicalURL(raw){
  try {
    const u=new URL(raw);
    if(!['https:','http:'].includes(u.protocol)) return null;
    u.hash=''; u.hostname=u.hostname.replace(/^www\./,'').toLowerCase();
    if(u.pathname!=='/')u.pathname=u.pathname.replace(/\/+$/,'');
    for(const k of [...u.searchParams.keys()])if(/^utm_|^fbclid$|^gclid$|^ref$|^source$/i.test(k))u.searchParams.delete(k);
    u.searchParams.sort();
    return `${u.hostname}${u.pathname}${u.search}`;
  }catch{return null;}
}
function normKey(s){return String(s||'').toLowerCase().trim();}
function displayDate(s){return s||'—';}
function markdownCell(s){return String(s??'—').replace(/\|/g,'\\|').replace(/\r?\n/g,' ');}
function sortEntries(items){
  const order={high:0,medium:1,low:2};
  return [...items].sort((a,b)=>order[a.priority]-order[b.priority] || b.eventDate.localeCompare(a.eventDate) || a.id.localeCompare(b.id));
}
function read(){return readJSON(REGISTRY_PATH);}
function expectedResearchPath(id){return `content/research/${id}.md`;}
function validate(registry,{files=true,queue=true}={}){
  const errors=[];
  const err=msg=>errors.push(msg);
  if(registry.schemaVersion!==2)err('schemaVersion must be 2');
  if(!Array.isArray(registry.items))return ['registry.items must be an array'];
  if(!Number.isInteger(registry.nextSequence)||registry.nextSequence<1)err('nextSequence must be a positive integer');
  if(!daysAreValid(registry.updatedAt))err('registry.updatedAt must be a valid YYYY-MM-DD date');
  const ids=new Map(),slugs=new Map(),storyKeys=new Map(),sources=new Map(),youtubeIds=new Map();
  let maxNum=0;const productionCodes=new Set();
  for(const it of registry.items){
    const name=it?.id||'(no ID)';
    if(!ID_RE.test(name)){err(`${name}: invalid permanent ID`);continue;}
    maxNum=Math.max(maxNum,Number(name.match(ID_RE)[1]));
    if(it.stage==='idea'){if(it.productionCode!==null)err(`${name}: unselected idea must not have a production code`);}else{if(!PRODUCTION_RE.test(it.productionCode||''))err(`${name}: selected content requires production code`);else if(productionCodes.has(it.productionCode))err(`${name}: duplicate production code ${it.productionCode}`);else productionCodes.add(it.productionCode);}
    if(ids.has(name))err(`Duplicate content ID ${name}`); ids.set(name,it);
    if(!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(it.slug||''))err(`${name}: invalid slug`);
    if(slugs.has(it.slug))err(`${name}: duplicate slug ${it.slug} (${slugs.get(it.slug)})`);slugs.set(it.slug,name);
    if(!it.title?.trim())err(`${name}: title required`);
    if(!STAGES.includes(it.stage))err(`${name}: stage must be idea, in_progress, or published`);
    if(!PRIORITIES.includes(it.priority))err(`${name}: invalid priority`);
    if(!it.category?.trim())err(`${name}: category required`);
    for(const field of ['storyKey','topicKey'])if(!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(it[field]||''))err(`${name}: invalid ${field}`);
    const key=normKey(it.storyKey);
    if(storyKeys.has(key))err(`${name}: duplicate event/story identity with ${storyKeys.get(key)}`);storyKeys.set(key,name);
    for(const field of ['eventDate','sourceDate','discoveredAt','updatedAt'])if(!daysAreValid(it[field],field==='eventDate'))err(`${name}: ${field} invalid`);
    if(!Array.isArray(it.aliases)||it.aliases.length===0||it.aliases.some(x=>!x?.trim()))err(`${name}: at least one alias required`);
    if(!Array.isArray(it.sourceUrls)||!it.sourceUrls.length)err(`${name}: one primary source URL is required`);
    for(const u of it.sourceUrls||[]){
      const canonical=canonicalURL(u);
      if(!canonical){err(`${name}: invalid source URL ${u}`);continue;}
      if(sources.has(canonical))err(`${name}: source URL re-used by ${sources.get(canonical)}; investigate overlap`);
      sources.set(canonical,name);
    }
    if(it.researchPath!==expectedResearchPath(name))err(`${name}: expected researchPath ${expectedResearchPath(name)}`);
    if(files){
      const research=path.join(ROOT,it.researchPath||'');
      if(!fs.existsSync(research))err(`${name}: missing research file ${it.researchPath}`);
      else if(!fs.readFileSync(research,'utf8').startsWith(`# ${name} — `))err(`${name}: research document must start with permanent ID`);
      if(it.storyPath!==null){
        const story=path.join(ROOT,it.storyPath||'');
        if(!it.storyPath?.startsWith('stories/')||!fs.existsSync(story))err(`${name}: missing story draft ${it.storyPath}`);
        else try{{const draft=readJSON(story).story; if(draft?.slug!==it.slug)err(`${name}: storyPath slug does not match registry slug`); if(draft?.contentId!==name&&draft?.contentId!==it.legacyId)err(`${name}: storyPath contentId must match permanent registry ID`)}}catch{err(`${name}: invalid story JSON`)}
      }
    }
    if(!Array.isArray(it.relatedIds))err(`${name}: relatedIds array required`);
    if(!Array.isArray(it.stageHistory)||!it.stageHistory.length)err(`${name}: stageHistory required`);
    else{
      let prev=null;
      for(const x of it.stageHistory){
        if(!daysAreValid(x.at))err(`${name}: invalid stageHistory date`);
        if(x.from!==prev)err(`${name}: invalid stage history transition from ${x.from} (expected ${prev})`);
        if(!STAGES.includes(x.to)||!(prev===null&&x.to==='idea'||prev==='idea'&&x.to==='in_progress'||prev==='in_progress'&&x.to==='published'))err(`${name}: invalid ${prev}->${x.to} transition`);
        if(!x.note?.trim())err(`${name}: missing history reason`);
        prev=x.to;
      }
      if(prev!==it.stage)err(`${name}: stage differs from stageHistory`);
    }
    if(it.stage==='published'){
      if(!daysAreValid(it.publishedAt))err(`${name}: publishedAt required in published stage`);
      const id=videoId(it.youtubeUrl);
      if(!id)err(`${name}: valid public YouTube watch/video link required in published stage`);
      else {if(youtubeIds.has(id))err(`${name}: duplicate YouTube video ID shared with ${youtubeIds.get(id)}`);youtubeIds.set(id,name)}
      if(it.publishApprovedByOwner!==true)err(`${name}: owner publication sign-off required`);
    }else if(it.publishedAt!==null||it.youtubeUrl!==null||it.publishApprovedByOwner!==false){err(`${name}: unpublished content must have null publication fields / false approval`)}
  }
  if(registry.nextSequence<=maxNum)err(`nextSequence must be > max assigned permanent ID ${maxNum}`);
  for(const it of registry.items){
    if(!ID_RE.test(it.id||''))continue;
    for(const otherId of it.relatedIds||[]){
      if(otherId===it.id||!ids.has(otherId))err(`${it.id}: invalid related content ${otherId}`);
    }
    const sameTopic=registry.items.filter(x=>x.id!==it.id&&normKey(x.topicKey)===normKey(it.topicKey));
    if(sameTopic.length){
      if(!it.distinguishingUpdate?.trim()&&!sameTopic.some(x=>x.relatedIds?.includes(it.id)&&x.distinguishingUpdate?.trim()))err(`${it.id}: topicKey overlaps another entry. A distinct follow-up requires relatedIds and distinguishingUpdate.`);
      if(!sameTopic.some(x=>it.relatedIds?.includes(x.id)||x.relatedIds?.includes(it.id)))err(`${it.id}: same topicKey as ${sameTopic.map(x=>x.id).join(', ')}; cross-link the separate update`);
    }
  }
  for(let i=0;i<registry.items.length;i++)for(let j=i+1;j<registry.items.length;j++){
    const a=registry.items[i],b=registry.items[j];
    if(overlap(a.title,b.title)>=.82)err(`Near-identical titles ${a.id} / ${b.id}; resolve story overlap`);
    // Exact alias is a collision when combined with a near-identical title, but
    // a shared organization by itself does not make distinct developments duplicates.
  }
  if(files && fs.existsSync(path.join(ROOT,'stories'))){
    for(const fname of fs.readdirSync(path.join(ROOT,'stories')).filter(f=>f.endsWith('.json'))){
      try {
        const story=readJSON(path.join(ROOT,'stories',fname)).story;
        if(!story?.slug || !story?.contentId)err(`stories/${fname}: story must include slug + permanent contentId`);
        else if(!registry.items.some(it=>it.slug===story.slug && [it.id,it.legacyId].includes(story.contentId) && it.storyPath===`stories/${fname}`))err(`stories/${fname}: missing or mismatched content register entry`);
      }catch{err(`stories/${fname}: invalid story JSON`)}
    }
  }
  if(queue && fs.existsSync(QUEUE_PATH)){
    const q=readJSON(QUEUE_PATH);const seen=new Set();
    for(const slug of q.slugs||[]){
      if(seen.has(slug))err(`Publishing queue repeats ${slug}`);seen.add(slug);
      const item=registry.items.find(x=>x.slug===slug);
      if(!item)err(`Publishing queue item '${slug}' not registered`);
      else if(item.stage==='published'||item.ownerConfirmedPublic===true)err(`Publishing queue still includes published item ${item.id}`);
    }
  }
  return errors;
}
function videoId(url){
  try{const u=new URL(url);let id=null;
    if(/^(www\.)?youtube\.com$/.test(u.hostname)&&u.pathname==='/watch')id=u.searchParams.get('v');
    if(/^(www\.)?youtube\.com$/.test(u.hostname)&&/^\/shorts\//.test(u.pathname))id=u.pathname.split('/')[2];
    if(u.hostname==='youtu.be')id=u.pathname.split('/')[1];
    return /^[A-Za-z0-9_-]{11}$/.test(id||'')?id:null;
  }catch{return null}
}
function renderLog(registry){
  const lines=[
    '# Bharat Mode — Content Log',
    '',
    '**Canonical register:** [`registry.json`](registry.json) · **Story research:** [`research/`](research/) · **Workflow:** [`docs/CONTENT_PIPELINE.md`](../docs/CONTENT_PIPELINE.md)',
    '',
    `Updated: ${registry.updatedAt} (IST) · Permanent IDs: ${registry.items.length} · **Never reassign or delete an ID.**`,
    '',
    '> This document is generated from `content/registry.json`. Use the registry command to add and move content; run `npm run content:check` before committing. An idea is not a published video.',
    ''
  ];
  for(const stage of STAGES){
    const rows=sortEntries(registry.items.filter(x=>x.stage===stage));
    lines.push(`## ${LABELS[stage]} (${rows.length})`,'');
    if(!rows.length){lines.push('_No content in this stage._','');continue}
    lines.push('| Idea ID | Production | Title | Event / as-of | Priority | Research | Story draft | Publication |','|---|---|---|---|---|---|---|---|');
    for(const x of rows){
      const story=x.storyPath?`[Draft](../${x.storyPath})`:'—';
      const published=x.stage==='published'?`[Watch](${x.youtubeUrl}) · ${x.publishedAt}`:x.ownerConfirmedPublic?'Owner-confirmed published; URL/date pending':'—';
      lines.push(`| **${x.id}** | ${x.productionCode||'—'} | ${markdownCell(x.title)} | ${displayDate(x.eventDate)} | ${x.priority} | [Research](research/${x.id}.md) | ${story} | ${published} |`);
    }
    lines.push('');
  }
  lines.push('## Dedupe and stage rules','',
    '- Every candidate gets one **never-reused** `ID-###` idea identity and its own fact-checked research sheet. Assign the lowest unused `BM-###` only on selection; preserve both codes permanently.',
    '- A primary event is identified by `storyKey`; source URLs, slug, ID, near-identical titles and the complete registry are checked for duplicates.',
    '- A later distinct event in the **same topic** requires a new `storyKey`, links in `relatedIds`, and `distinguishingUpdate` explaining why it deserves another video.',
    '- **Idea → In Progress → Published** is one-way. A published entry must include the actual YouTube video URL, date and explicit owner publication sign-off.',
    '- The `publishing/queue.json` is an editorial planning order, **not a second content identity system**. It may not contain published or unregistered slugs.',
    '- Automated checks catch exact/obvious overlap, not all semantic paraphrases. A human must check the research sheets and older coverage before approving a new event.',
    '', 'See [content workflow](../docs/CONTENT_PIPELINE.md) for usage.','');
  return lines.join('\n');
}
function ensureHealthy(registry){const e=validate(registry);if(e.length)die('Registry invalid:\n- '+e.join('\n- '));}
function atomicWrite(file,body){fs.mkdirSync(path.dirname(file),{recursive:true});const temp=`${file}.tmp-${process.pid}`;fs.writeFileSync(temp,body);fs.renameSync(temp,file)}
function persist(registry){registry.updatedAt=todayIST();ensureHealthy(registry);atomicWrite(REGISTRY_PATH,JSON.stringify(registry,null,2)+'\n');atomicWrite(LOG_PATH,renderLog(registry));}
function parseArgs(args){
  const flags={},pos=[];
  for(let i=0;i<args.length;i++)if(args[i].startsWith('--')){
    const key=args[i].slice(2);
    if(key==='approved-by-owner'){flags[key]=true;continue}
    if(!args[i+1]||args[i+1].startsWith('--'))die(`Missing value for --${key}`);
    flags[key]=args[++i];
  }else pos.push(args[i]);
  return {flags,pos};
}
function add(args){
  const {flags:f}=parseArgs(args);const r=read();ensureHealthy(r);
  for(const k of ['title','slug','story-key','topic-key','primary-source','event-date','source-date'])if(!f[k])die(`Add requires --${k}`);
  if(!daysAreValid(f['event-date'],true))die('Invalid --event-date');
  if(!daysAreValid(f['source-date']))die('Invalid --source-date');
  const source=f['primary-source'];if(!canonicalURL(source))die('Invalid primary source URL');
  const id=`ID-${String(r.nextSequence).padStart(3,'0')}`;
  const related=(f.related||'').split(',').map(s=>s.trim()).filter(Boolean).map(id=>r.items.find(x=>matchId(x,id))?.id||id);
  const item={id,productionCode:null,slug:f.slug,title:f.title,stage:'idea',priority:f.priority||'medium',category:f.category||'general',storyKey:f['story-key'],topicKey:f['topic-key'],aliases:(f.aliases||f.title).split(',').map(x=>x.trim()).filter(Boolean),eventDate:f['event-date'],sourceDate:f['source-date']||todayIST(),discoveredAt:todayIST(),updatedAt:todayIST(),sourceUrls:[source],researchPath:expectedResearchPath(id),storyPath:null,relatedIds:related,distinguishingUpdate:f['distinguishing-update']||null,publishedAt:null,youtubeUrl:null,publishApprovedByOwner:false,stageHistory:[{at:todayIST(),from:null,to:'idea',note:f.note||'New candidate added after source and overlap review.'}]};
  const candidate={...r,items:[...r.items,item],nextSequence:r.nextSequence+1};
  // Validate metadata without the new research file; no partial writes for dupes.
  const errs=validate(candidate,{files:false});if(errs.length)die('Cannot add candidate:\n- '+errs.join('\n- '));
  const doc=`# ${id} — ${item.title}\n\n**Stage:** Idea  \n**Event date:** ${item.eventDate}  \n**Story key:** \`${item.storyKey}\`  \n**Topic key:** \`${item.topicKey}\`\n\n## What happened / why this matters\n\n${f.note||'Research to be completed. Do not script or publish before claim verification.'}\n\n## Primary source\n\n- [Original source](${source}) (source date: ${item.sourceDate})\n\n## Claim ledger / evidence\n\n- [ ] Record each proposed factual claim, primary URL, actual event date, and development stage.\n- [ ] Corroborate unusually large claims and include an explicit counter-claim/limitation.\n\n## Duplication check\n\n- Related IDs: ${related.length?related.join(', '):'none identified'}\n- Distinguishing update: ${item.distinguishingUpdate||'First identified event for this topic'}\n\n## Production checklist\n\n- [ ] Select for active production and move to In Progress.\n- [ ] Verify script and asset rights; generate approved Qwen voice, align and render locked V6.\n- [ ] Human editorial, video and publication sign-off before Published.\n\n## Publication\n\nNot published.\n`;
  atomicWrite(path.join(ROOT,item.researchPath),doc);
  persist(candidate);
  console.log(`Created ${id} (${item.stage}): ${item.title}`);
}
function move(args){
  const {flags:f,pos}=parseArgs(args);
  const [id,target]=pos;
  if(!id||!STAGES.includes(target))die('Usage: move ID-003 in_progress [--note ...] OR move ID-003 published --youtube-url URL --published-at YYYY-MM-DD --approved-by-owner --note ...');
  const r=read();ensureHealthy(r);
  const item=r.items.find(x=>matchId(x,id));if(!item)die('Unknown ID '+id);
  const prev=item.stage;
  if(STAGES.indexOf(target)!==STAGES.indexOf(prev)+1)die(`Cannot transition ${id}: ${prev} -> ${target}. Must move Idea → In Progress → Published.`);
  if(!f.note?.trim())die('Stage transitions need an explicit --note');
  if(target==='published'){
    if(!f['approved-by-owner'])die('Publishing requires explicit --approved-by-owner');
    if(!daysAreValid(f['published-at']))die('Publishing requires a valid --published-at date');
    if(!videoId(f['youtube-url']))die('Publishing requires an actual YouTube watch/shorts URL');
    item.youtubeUrl=f['youtube-url'];item.publishedAt=f['published-at'];item.publishApprovedByOwner=true;
  }
  if(target==='in_progress'){item.productionCode=nextProductionCode(r);item.productionSelectedAt=todayIST();}
  item.stage=target;item.updatedAt=todayIST();item.stageHistory.push({at:todayIST(),from:prev,to:target,note:f.note});
  const e=validate(r);if(e.length)die('Cannot move:\n- '+e.join('\n- '));
  const file=path.join(ROOT,item.researchPath),old=fs.readFileSync(file,'utf8');
  if(!/^\*\*Stage:\*\*.*$/m.test(old))die(`${id} research missing Stage line`);
  const newDoc=old.replace(/^\*\*Stage:\*\*.*$/m,`**Stage:** ${LABELS[target]}  `)+`\n## Stage transition — ${todayIST()}\n\n${prev} → ${target}: ${f.note}\n`;
  atomicWrite(file,newDoc);
  if(target==='published'&&fs.existsSync(QUEUE_PATH)){
    const queue=readJSON(QUEUE_PATH);
    if(queue.slugs?.includes(item.slug)){
      queue.slugs=queue.slugs.filter(x=>x!==item.slug);
      atomicWrite(QUEUE_PATH,JSON.stringify(queue,null,2)+'\n');
    }
  }
  persist(r);
  console.log(`Moved ${item.id} / ${item.productionCode} ${prev} → ${target}`);
}
function check(){
  const r=read(),errs=validate(r);
  if(fs.existsSync(LOG_PATH)){
    if(fs.readFileSync(LOG_PATH,'utf8')!==renderLog(r))errs.push('content/CONTENT_LOG.md is out of sync; run npm run content:sync');
  }else errs.push('Missing content/CONTENT_LOG.md; run npm run content:sync');
  if(errs.length)die('Content registry failed:\n- '+errs.join('\n- '));
  const count=s=>r.items.filter(x=>x.stage===s).length;
  console.log(`Content registry OK — ${r.items.length} IDs | idea ${count('idea')} | in_progress ${count('in_progress')} | published ${count('published')}.`);
}
function find(query){
  const r=read();const q=String(query||'').trim();if(!q)die('Usage: find <phrase|ID>');
  const arr=r.items.map(it=>{
    const corpus=[it.title,it.slug,it.id,it.productionCode,it.legacyId,it.storyKey,it.topicKey,...it.aliases].join(' ');
    const score=matchId(it,q)?10:Math.max(overlap(q,corpus),overlap(q,it.title),[it.title,it.slug,it.storyKey,it.topicKey,...it.aliases].some(x=>String(x).toLowerCase().includes(q.toLowerCase()))?1:0);
    return {...it,score};
  }).filter(x=>x.score>=.10).sort((a,b)=>b.score-a.score).slice(0,12);
  for(const x of arr)console.log(`${x.id}\t${x.productionCode||'—'}\t${LABELS[x.stage]}\t${x.title}\t${x.researchPath}`);
  if(!arr.length)console.log('No strong matches; still examine topic aliases before accepting a story as new.');
}
function list(flag){const r=read();if(flag&&!STAGES.includes(flag))die('Unknown stage '+flag);for(const x of sortEntries(r.items.filter(it=>!flag||it.stage===flag)))console.log(`${x.id}\t${x.productionCode||'—'}\t${LABELS[x.stage]}\t${x.title}`);}
function main(){
  const [cmd,...args]=process.argv.slice(2);
  if(cmd==='check')return check();
  if(cmd==='sync'){const r=read();ensureHealthy(r);atomicWrite(LOG_PATH,renderLog(r));return console.log('Synced content/CONTENT_LOG.md');}
  if(cmd==='add')return add(args);
  if(cmd==='move')return move(args);
  if(cmd==='find')return find(args.join(' '));
  if(cmd==='list')return list(parseArgs(args).flags.stage);
  console.log('Usage: node scripts/content-registry.mjs <check|sync|list [--stage idea|in_progress|published]|find <words>|add --title ... --slug ... --story-key ... --topic-key ... --primary-source ... --event-date YYYY-MM-DD [--related ID-XXX --distinguishing-update ...]|move ID-XXX in_progress|published --note ...>');
  if(cmd)process.exitCode=1;
}
try{main()}catch(e){console.error(e.message);process.exitCode=1}