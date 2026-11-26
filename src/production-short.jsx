import React from 'react';
import {AbsoluteFill, Audio, staticFile, useCurrentFrame} from 'remotion';
import {ApprovedShortsFrame} from './approved-shorts-template.jsx';
import {AlignedNarrationCaptions} from './aligned-captions.jsx';
import {getTheme} from './brand.js';
import {DISPLAY_FONT,BODY_FONT} from './fonts.js';
import {validateProduction,frameState,ease,typed,FPS} from './production-contract.js';

// Scene art is authored per story, not a generic boxed template. Independent
// SVG layers have native coordinates, explicit bounds and measured cue IDs.
const strokeProps=l=>({stroke:l.stroke||'none',strokeWidth:l.strokeWidth||3,strokeLinecap:'round',strokeLinejoin:'round',fill:l.fill||'none'});
function Layer({layer:l,sec,cues,theme,background=false}){
  const onset=l.cue===undefined?0:cues.get(l.cue),age=sec-onset;
  if(age<0)return null;
  const [x,y,w,h]=l.bounds,progress=ease(age/(l.duration||.48));
  const motion=l.motion?Math.sin(2*Math.PI*sec/l.motion.period):0;
  const dx=(l.motion?.dx||0)*motion,dy=(l.motion?.dy||0)*motion;
  const shift=background?0:(1-ease(age/.48))*16;
  const ink=l.fill&&l.fill!=='none'?l.fill:theme.text;
  let art;
  switch(l.type){
    case 'path': art=<path d={l.d} {...strokeProps(l)} pathLength={1} strokeDasharray={l.draw===false?undefined:'1 1'} strokeDashoffset={l.draw===false?undefined:1-progress}/>;break;
    case 'line': art=<line x1={x} y1={y} x2={x+w*progress} y2={y+h*progress} {...strokeProps(l)}/>;break;
    case 'rect': art=<rect x={x} y={y} width={w} height={h} rx={l.radius||0} {...strokeProps(l)}/>;break;
    case 'bar': {const width=w*progress;art=width>0?<rect x={x} y={y} width={width} height={h} rx={Math.min(l.radius||h/2,width/2,h/2)} fill={ink}/>:null;break;}
    case 'circle': art=<ellipse cx={x+w/2} cy={y+h/2} rx={w/2} ry={h/2} {...strokeProps(l)}/>;break;
    case 'orbit': {const a=2*Math.PI*age/l.period+(l.phase||0);art=<><ellipse cx={x+w/2} cy={y+h/2} rx={w/2} ry={h/2} {...strokeProps(l)}/><circle cx={x+w/2+w/2*Math.cos(a)} cy={y+h/2+h/2*Math.sin(a)} r={l.markerRadius||8} fill={ink}/></>;break;}
    case 'image':art=<image href={staticFile(l.path)} x={x} y={y} width={w} height={h} preserveAspectRatio="xMidYMid meet"/>;break;
    case 'text':
    case 'counter': {const label=l.type==='counter'?Math.round(l.value*progress).toLocaleString('en-IN')+(l.suffix||''):typed(l.text,age);art=<text x={x} y={y} dominantBaseline="hanging" fontFamily={l.type==='counter'?DISPLAY_FONT:BODY_FONT} fontSize={l.fontSize||42} fontWeight={700} fill={ink}>{label}</text>;break;}
    default:return null;
  }
  return <g opacity={background?1:Math.max(.15,ease(age/.18))} transform={`translate(${dx} ${dy+shift})`}>{art}</g>;
}
function StoryScene({spec,scene,sec}){
  const theme=getTheme(spec.theme),headlines=scene.headline.split('\n');
  return <AbsoluteFill style={{background:theme.bg,overflow:'hidden'}}>
    <svg width="1080" height="1920" viewBox="0 0 1080 1920" style={{position:'absolute',inset:0}}>
      {spec.background.map(l=><Layer key={l.id} layer={l} sec={sec} cues={spec.cueMap} theme={theme} background/>)}
      {spec.artwork.map(l=><Layer key={l.id} layer={l} sec={sec} cues={spec.cueMap} theme={theme}/>)}
    </svg>
    <div style={{position:'absolute',left:84,right:84,top:230,color:theme.text,transform:`translateY(${16*(1-ease(sec/.48))}px)`,fontFamily:BODY_FONT,fontSize:29,fontWeight:700}}>{typed(scene.kicker,sec)}</div>
    <div style={{position:'absolute',top:290,left:84,right:84,fontFamily:DISPLAY_FONT,fontSize:spec.headlineSize||76,fontWeight:800,lineHeight:1.12,color:theme.text,transform:`translateY(${16*(1-ease(sec/.48))}px)`}}>
      {headlines.map((line,i)=><div key={i}>{sec>=i*.18?typed(line,sec-i*.18):''}</div>)}
    </div>
  </AbsoluteFill>;
}
export const BharatShort=({story,production})=>{
  const frame=useCurrentFrame();
  if(!production)return <AbsoluteFill style={{background:'#0B1018',color:'#FFF7EB',justifyContent:'center',alignItems:'center',fontSize:36}}>Production props required — use validated render command.</AbsoluteFill>;
  const plan=validateProduction({story,production}),state=frameState(plan,frame);
  const {scene,index,sec,transition}=state;
  const previous=index>0?plan.scenes[index-1]:null;
  const old=previous&&transition<1;
  const caption=sec<scene.narrationFrames/FPS&&!state.holding?<AlignedNarrationCaptions alignment={scene.alignment} timeSec={sec} theme={scene.theme}/>:null;
  return <ApprovedShortsFrame chapters={plan.chapters} timeSec={state.progressSec} theme={scene.theme} topic={story.category||story.topic} caption={caption}>
    {old&&<StoryScene spec={previous} scene={story.scenes[index-1]} sec={previous.narrationFrames/FPS-.001}/>}
    <AbsoluteFill style={{opacity:old ? .15+.85*transition : 1,transform:`translateX(${old?14*(1-transition):0}px)`}}>
      <StoryScene spec={scene} scene={story.scenes[index]} sec={sec}/>
    </AbsoluteFill>
    <Audio src={staticFile(production.master.path)}/>
  </ApprovedShortsFrame>;
};
