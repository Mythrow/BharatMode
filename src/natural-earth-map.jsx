/** BM-0003 geographically grounded V6 hero; main-chat visual source, NEVER Work TTS. */
import React from 'react';
import geodata from '../data/maps/naturalearth-bm0003.json';
import {CITY_CHENNAI,decodeNEPolyline,naturalEarthCamera,naturalEarthSvgPath,mapPoint,smooth} from './natural-earth-geo.mjs';

const outlines=Object.fromEntries(['india','Tamil Nadu','Andhra Pradesh','Karnataka','Kerala'].map(name=>[name,decodeNEPolyline(geodata[name])]));
const W=928,H=626;
const common={fontFamily:'Manrope, sans-serif',color:'#fff7eb'};
export function BM0003NaturalEarthMap({localTime=0,duration=7}) {
  const p=Math.max(0,Math.min(1,localTime/Math.max(.01,duration)));
  const camera=naturalEarthCamera(p);
  const paths=Object.fromEntries(Object.entries(outlines).map(([k,v])=>[k,naturalEarthSvgPath(v,camera,W,H)]));
  const [cx,cy]=mapPoint(CITY_CHENNAI,camera,W,H);
  const current=p<.25?'INDIA':p<.65?'TAMIL NADU':'CHENNAI';
  const cityOpacity=smooth((p-.46)/.18);
  const fillOpacity=.05+.58*smooth((p-.15)/.38);
  return <div style={{position:'absolute',top:640,left:77,width:W,height:H,overflow:'hidden',border:'2px solid #496a74',background:'#071827',...common}}>
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" height="100%" style={{position:'absolute',inset:0}}>
      <defs><linearGradient id="ne-bg" x1="0" x2="0" y1="0" y2="1"><stop stopColor="#112a3a"/><stop offset="1" stopColor="#071827"/></linearGradient></defs>
      <rect width={W} height={H} fill="url(#ne-bg)"/>
      {Array.from({length:19},(_,i)=><path key={'v'+i} d={`M${i*53+20} 0 V626`} stroke="#244550" strokeWidth="1" opacity=".38"/>)}
      {Array.from({length:13},(_,i)=><path key={'h'+i} d={`M0 ${i*53+20} H928`} stroke="#244550" strokeWidth="1" opacity=".38"/>)}
      <path d={paths.india} fill="#264354" stroke="#8baeb5" strokeWidth="2.4"/>
      {p>.2&&['Andhra Pradesh','Karnataka','Kerala'].map(name=><path key={name} d={paths[name]} fill="none" stroke="#628793" strokeWidth="2" opacity=".75"/>)}
      <path d={paths['Tamil Nadu']} fill="#e8752e" fillOpacity={fillOpacity} stroke="#ffb16f" strokeWidth={p>.2?4:0}/>
      <g opacity={cityOpacity} transform={`translate(${cx} ${cy})`}>
        <circle r={20+7*Math.sin(localTime*7)} fill="none" stroke="#ffb16f" strokeWidth="2" opacity=".8"/>
        <circle r="10" fill="#fff7eb"/><circle r="6" fill="#e8752e"/>
        <g transform="translate(23 -43)"><rect x="-8" y="-5" width="225" height="70" fill="#0b1f2b" rx="8"/>
          <text x="3" y="25" fill="#fff7eb" fontSize="27" fontWeight="800">CHENNAI</text>
          <text x="3" y="53" fill="#a8cfd0" fontSize="17">Tamil Nadu · India</text></g>
      </g>
      <path d="M28 112 H900" stroke="#306e7c" strokeWidth="2"/>
    </svg>
    <div style={{position:'absolute',top:18,left:26,color:'#a9d5d3',fontSize:16,fontWeight:700,letterSpacing:2}}>GEO FOCUS / SOUTH INDIA</div>
    <div style={{position:'absolute',top:54,left:26,fontSize:42,fontWeight:800}}>{current}</div>
    <div style={{position:'absolute',bottom:132,left:25,fontSize:15,color:'#c1d4d4'}}>Chennai city marker · not the exact L&T facility</div>
    <div style={{position:'absolute',bottom:0,left:0,right:0,height:120,background:'linear-gradient(90deg,#071821f2,#0a2230f5)',display:'flex',alignItems:'center',gap:11,padding:'0 22px'}}>
      {['L&T','Vyoma.AI','LTN Compute','NVIDIA B300'].map((name,i)=><div key={name} style={{flex:i===0?0.8:1,background:'#203646',borderRadius:10,padding:'15px 11px',fontWeight:800,fontSize:i===2?23:26,color:i===1?'#8de8d1':i===3?'#b0f56b':'#fff7eb',textAlign:'center',whiteSpace:'nowrap'}}>{name}</div>)}
    </div>
  </div>;
}