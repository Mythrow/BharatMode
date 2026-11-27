/**
 * Editorial rotation lint. Inspect queued stories in publishing/queue.json.
 * These are HOUSE RULES to reduce repetitiveness, not YouTube policy thresholds.
 */
import fs from 'node:fs';
const registry=JSON.parse(fs.readFileSync('content/registry.json','utf8')).items;
const queue=JSON.parse(fs.readFileSync('publishing/queue.json','utf8')).slugs;
let errors=0,warnings=0;
const records=[];
const normalize=(s)=>s.toLowerCase().replace(/[^a-z0-9 ]/g,'').replace(/\s+/g,' ').trim();
const flag=(type,message)=>{console.log(type+': '+message);if(type==='FAIL')errors++;else warnings++;};
for(const slug of queue){
  const record=registry.find(r=>r.slug===slug);
  if(!record){flag('FAIL','Unknown queue slug '+slug);continue;}
  if(!record.storyPath){console.log('PENDING: '+slug+' — no structured brief yet; creative lint applies once authored');continue;}
  let item;
  try{item=JSON.parse(fs.readFileSync(record.storyPath,'utf8')).story;}
  catch(e){flag('FAIL','Missing story '+slug);continue;}
  if(!item?.youtubeTitle || !item?.visualFamily){flag('FAIL','Missing creative metadata '+slug);continue;}
  const prev=records.at(-1);
  if(prev){
    if(prev.visualFamily===item.visualFamily)flag('FAIL',slug+': same visual family as prior upload');
    if(prev.scenes.map(s=>s.kind).join('>')===item.scenes.map(s=>s.kind).join('>'))flag('FAIL',slug+': exact same storyboard structure as prior upload');
    if(prev.hookType===item.hookType)flag('WARN',slug+': same hook type as prior upload');
    if(prev.thumbnailStyle===item.thumbnailStyle)flag('WARN',slug+': same thumbnail layout as prior upload');
    if(normalize(prev.thumbnailText)===normalize(item.thumbnailText))flag('FAIL',slug+': identical thumbnail wording');
  }
  const recent=records.slice(-6);
  const count=(key,value)=>recent.filter(r=>r[key]===value).length;
  if(count('hookType',item.hookType)>=2)flag('FAIL',slug+': hook pattern would appear 3 times in 7 uploads');
  if(count('thumbnailStyle',item.thumbnailStyle)>=2)flag('WARN',slug+': thumbnail layout would appear 3 times in 7 uploads');
  if(count('topic',item.topic)>=3)flag('WARN',slug+': topic would appear 4 times in 7 uploads');
  // Scene-level theme distribution is reviewed across actual production manifests, not upload-dominant colors.
  const title=normalize(item.youtubeTitle);
  if(records.some(r=>normalize(r.youtubeTitle)===title))flag('FAIL',slug+': duplicate title');
  const words=new Set(title.split(' ').filter(Boolean));
  for(const r of recent){
    const other=new Set(normalize(r.youtubeTitle).split(' ').filter(Boolean));
    const union=new Set([...words,...other]);
    const overlap=[...words].filter(w=>other.has(w)).length/Math.max(1,union.size);
    if(overlap>0.65)flag('WARN',slug+': possible similar title to '+r.slug);
  }
  records.push(item);
}
console.log('Checked '+records.length+' candidate(s): '+errors+' errors, '+warnings+' warnings.');
if(records.length<4)console.log('NOTE: short queue: seven-video rotation rules become meaningful as the queue grows.');
if(errors)process.exitCode=1;
