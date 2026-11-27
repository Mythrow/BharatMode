import fs from 'node:fs';
import assert from 'node:assert/strict';
const read=p=>JSON.parse(fs.readFileSync(p,'utf8'));
const rows=read('content/registry.json').items;
const known=new Set(rows.map(r=>r.productionCode).filter(Boolean));
const dir='analytics/windows';
const files=fs.existsSync(dir)?fs.readdirSync(dir).filter(p=>p.endsWith('.json')):[];
const seen=new Set();
const keys=Object.keys(read('analytics/window-template.json').metrics);
for(const file of files){
 const d=read(dir+'/'+file),key=d.productionCode+'-'+d.windowHours;
 assert(d.schemaVersion===1&&d.exampleOnly!==true&&known.has(d.productionCode)&&[24,168].includes(d.windowHours)&&!seen.has(key),'Invalid/duplicate analytics window '+file);seen.add(key);
 assert(file===key+'.json'&&typeof d.source==='string'&&d.source.trim(),'Missing Studio source '+file);
 const dates=[d.actualPublishedAt,d.windowStart,d.windowEnd,d.capturedAt];assert(dates.every(x=>typeof x==='string'&&/T.*(?:Z|[+-]\d\d:\d\d)$/.test(x)&&Number.isFinite(Date.parse(x))),'Explicit offset timestamps required '+file);
 const [p,s,e,c]=dates.map(Date.parse);assert(p===s&&e-s===d.windowHours*3600000&&c>=e,'Not a comparable first-window snapshot '+file);
 assert(keys.every(k=>Object.hasOwn(d.metrics||{},k)&&(d.metrics[k]===null||Number.isFinite(d.metrics[k])&&d.metrics[k]>=0)),'Metrics must be nonnegative or null '+file);
}
console.log('Comparable analytics windows checked: '+files.length+'; no missing values invented.');
