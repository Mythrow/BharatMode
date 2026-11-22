import fs from 'node:fs';
import path from 'node:path';
const folder = path.resolve('stories');
let failures = 0;
const kinds = new Set(['hook','metric','impact','uses','close']);
for (const file of fs.readdirSync(folder).filter(f=>f.endsWith('.json'))) {
  let data;
  try { data=JSON.parse(fs.readFileSync(path.join(folder,file),'utf8')).story; }
  catch (error) { console.error(file, String(error)); failures++; continue; }
  if (!data?.slug || !data?.sourceUrl || !data?.sourceContext || !data?.sourcePublished || !data?.claimStage || !Array.isArray(data.scenes) || !data.scenes.length) {
    console.error(file+': missing source, claim stage, slug, or scenes'); failures++; continue;
  }
  const duration = data.scenes.reduce((n,s)=>n+Number(s.duration||0),0);
  if (duration<15 || duration>180) { console.error(file+': unsupported duration '+duration); failures++; }
  for (const [i,s] of data.scenes.entries()) {
    if (!kinds.has(s.kind) || !s.kicker || !s.headline || !s.narration || !(s.duration>0)) { console.error(file+': invalid scene '+i); failures++; }
    if (['metric','impact'].includes(s.kind) && !Number.isFinite(s.number)) { console.error(file+': missing number at '+i); failures++; }
    if (s.kind==='uses' && (!Array.isArray(s.items)||!s.items.length)) { console.error(file+': missing items at '+i); failures++; }
  }
  console.log(file+': '+duration+'s, '+data.scenes.length+' scenes, '+data.sourceUrl);
}
if (failures) process.exitCode=1;
