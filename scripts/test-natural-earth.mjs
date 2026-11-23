import assert from 'node:assert/strict';
import fs from 'node:fs';
import {decodeNEPolyline,CITY_CHENNAI,naturalEarthCamera,pointInsidePolygon,mapPoint,naturalEarthSvgPath} from '../src/natural-earth-geo.mjs';
const src=JSON.parse(fs.readFileSync(new URL('../data/maps/naturalearth-bm0003.json',import.meta.url),'utf8'));
const india=decodeNEPolyline(src.india),tn=decodeNEPolyline(src['Tamil Nadu']);
assert.ok(india.length>150,'India 10m POV ring should retain sufficient detailed points');
assert.ok(tn.length>50,'Tamil Nadu 10m outline detail expected');
assert.deepEqual(src.chennai,CITY_CHENNAI);
assert.ok(pointInsidePolygon(CITY_CHENNAI,tn),'Chennai should lie inside TN state polygon');
assert.ok(india.some(([lon,lat])=>lon>95&&lat>25),'India POV should cover northeastern India');
for(let p=0;p<=1;p+=.1){const c=naturalEarthCamera(p);assert.ok(Number.isFinite(c.zoom));assert.ok(c.zoom>0);assert.ok(mapPoint(CITY_CHENNAI,c).every(Number.isFinite));}
const path=naturalEarthSvgPath(tn,naturalEarthCamera(.7));
assert.ok(path.startsWith('M')&&path.endsWith(' Z'));
assert.ok(path.split('L').length>40);
console.log('Natural Earth 10m India / Tamil Nadu, Chennai and camera checks passed.');