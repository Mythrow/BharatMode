/**
 * Verify approved palette, independent brand color roles, and type contrast.
 * Small text contrast threshold: WCAG AA 4.5:1.
 */
import {BRAND, getTheme} from '../src/brand.js';
import assert from 'node:assert/strict';

const approved = {
  primary: '#E8752E',
  ivory: '#FFF7EB',
  teal: '#117A7A',
  graphite: '#283039',
  charcoal: '#0B1018'
};
for (const [key,hex] of Object.entries(approved)) {
  assert.equal(BRAND[key],hex,'Approved color changed: '+key);
}
const linear = channel => {
  const c=channel/255;
  return c<=0.04045?c/12.92:((c+0.055)/1.055)**2.4;
};
const luminance = hex => {
  const rgb=[1,3,5].map(i=>linear(parseInt(hex.slice(i,i+2),16)));
  return rgb[0]*0.2126+rgb[1]*0.7152+rgb[2]*0.0722;
};
const contrast = (a,b) => {
  const l1=luminance(a),l2=luminance(b);
  return (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);
};
const check=(name,text,bg,min=4.5)=>{
  const ratio=contrast(text,bg);
  assert.ok(ratio>=min,name+' has '+ratio.toFixed(2)+':1; expected '+min+':1');
  console.log(name+': '+ratio.toFixed(2)+':1');
};
check('Ivory / Graphite text',getTheme('ivory').text,getTheme('ivory').bg);
check('Ivory / darker saffron labels',getTheme('ivory').accentText,getTheme('ivory').bg);
check('Ivory / Ocean Teal',getTheme('ivory').teal,getTheme('ivory').bg);
check('Charcoal / ivory text',getTheme('midnight').text,getTheme('midnight').bg);
check('Charcoal / saffron labels',getTheme('midnight').accentText,getTheme('midnight').bg);
check('Saffron / charcoal text',getTheme('saffron').text,getTheme('saffron').bg);
console.log('Bharat Mode official color contract passed.');
