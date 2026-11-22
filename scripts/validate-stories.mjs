import fs from 'node:fs';
import path from 'node:path';
const folder = path.resolve('stories');
let failures = 0;
const kinds = new Set(['hook','metric','impact','uses','comparison','close']);
const themes = new Set(['ivory','midnight','saffron']);
const families = new Set(['data-led','explainer','field-report','people-first','timeline']);
const hookTypes = new Set(['unexpected-number','question','contrast','person','mystery','explainer']);
const thumbs = new Set(['stat','statement','diagram','split','portrait']);
const topicTypes = new Set(['science','health','industry','infrastructure','environment','people','economy','space','education','community']);
for (const file of fs.readdirSync(folder).filter(f=>f.endsWith('.json'))) {
  let data;
  try { data=JSON.parse(fs.readFileSync(path.join(folder,file),'utf8')).story; }
  catch (error) { console.error(file, String(error)); failures++; continue; }
  if (!data?.slug || !data?.sourceUrl || !data?.sourceContext || !data?.sourcePublished || !data?.claimStage || !Array.isArray(data.scenes) || !data.scenes.length) {
    console.error(file+': missing source, claim stage, slug, or scenes'); failures++; continue;
  }
  const validMeta = themes.has(data.visualTheme) && families.has(data.visualFamily) && hookTypes.has(data.hookType) && thumbs.has(data.thumbnailStyle) && topicTypes.has(data.topic) && typeof data.youtubeTitle==='string' && data.youtubeTitle.length>=15 && data.youtubeTitle.length<=85 && typeof data.thumbnailText==='string' && data.thumbnailText.trim().split(/\s+/).length<=5 && !!data.narrativeAngle;
  if (!validMeta) {console.error(file+': missing/invalid creative metadata'); failures++;}
  if (data.thumbnailStyle==='portrait' && (!data.thumbnailImage || !data.thumbnailImageLicense)) {console.error(file+': portrait thumbnail requires a rights-cleared image and license record'); failures++;}
  if (data.thumbnailStyle==='split' && !data.splitComparisonVerified) {console.error(file+': before/after split requires verification'); failures++;}
  const duration = data.scenes.reduce((n,s)=>n+Number(s.duration||0),0);
  if (duration<15 || duration>180) { console.error(file+': unsupported duration '+duration); failures++; }
  for (const [i,s] of data.scenes.entries()) {
    if (!kinds.has(s.kind) || !s.kicker || !s.headline || !s.narration || !(s.duration>0)) { console.error(file+': invalid scene '+i); failures++; }
    if (['metric','impact'].includes(s.kind) && !Number.isFinite(s.number)) { console.error(file+': missing number at '+i); failures++; }
    if (s.kind==='comparison' && (!s.leftLabel || !s.leftText || !s.rightLabel || !s.rightText)) { console.error(file+': invalid comparison at '+i); failures++; }
    if (s.kind==='uses' && (!Array.isArray(s.items)||!s.items.length)) { console.error(file+': missing items at '+i); failures++; }
  }
  console.log(file+': '+duration+'s, '+data.scenes.length+' scenes, '+data.visualTheme+'/'+data.visualFamily);
}
if (failures) process.exitCode=1;
