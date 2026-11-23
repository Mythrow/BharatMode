/** Pure, dependency-free 10m Natural Earth polyline decoder and cinematic camera. */
export const CITY_CHENNAI = [80.278053, 13.091934];
export function decodeNEPolyline(s) {
  if (typeof s !== 'string') throw new Error('Natural Earth path must be string');
  const result=[];
  const xy=[0,0];
  let j=0;
  while(j<s.length) {
    for(let axis=0;axis<2;axis++){
      let value=0,shift=0,c;
      do {
        if(j>=s.length)throw new Error('Incomplete geometry encoding');
        c=s.charCodeAt(j++)-63;
        if(c<0 || c>63)throw new Error('Invalid geometry character');
        value|=(c&31)<<shift;
        shift+=5;
      }while(c>=32);
      xy[axis]+=(value&1)?~(value>>1):value>>1;
    }
    result.push([xy[0]/10000,xy[1]/10000]);
  }
  return result;
}
export const smooth=(u)=>{const t=Math.max(0,Math.min(1,u));return t*t*(3-2*t)};
const lerp=(a,b,t)=>a+(b-a)*smooth(t);
export function naturalEarthCamera(progress) {
  const p=Math.max(0,Math.min(1,progress));
  if(p<.36){const u=p/.36;return {lon:lerp(79.4,79.5,u),lat:lerp(23.5,13.4,u),zoom:19*Math.exp(Math.log(43/19)*smooth(u))};}
  if(p<.78){const u=(p-.36)/.42;return {lon:lerp(79.5,79.75,u),lat:lerp(13.4,12.9,u),zoom:43*Math.exp(Math.log(110/43)*smooth(u))};}
  const u=(p-.78)/.22;return {lon:lerp(79.75,CITY_CHENNAI[0],u),lat:lerp(12.9,CITY_CHENNAI[1],u),zoom:110*Math.exp(Math.log(195/110)*smooth(u))};
}
export function mapPoint([lon,lat],c,w=928,h=626) {
  const pxPerLon=Math.cos(c.lat*Math.PI/180)*c.zoom;
  return [w*.5+(lon-c.lon)*pxPerLon,h*.5-(lat-c.lat)*c.zoom];
}
export function naturalEarthSvgPath(poly,c,w=928,h=626) {
  return poly.map((p,i)=>{const [x,y]=mapPoint(p,c,w,h);return `${i?'L':'M'}${x.toFixed(2)} ${y.toFixed(2)}`}).join(' ')+' Z';
}
export function pointInsidePolygon(pt,coords) {
  let inside=false;
  for(let i=0,j=coords.length-1;i<coords.length;j=i++) {
    const a=coords[i],b=coords[j];
    if(((a[1]>pt[1])!==(b[1]>pt[1])) &&
      (pt[0]<(b[0]-a[0])*(pt[1]-a[1])/(b[1]-a[1])+a[0])) inside=!inside;
  }
  return inside;
}