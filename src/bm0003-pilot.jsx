import React from 'react';
import {AbsoluteFill,Composition,registerRoot,useCurrentFrame} from 'remotion';
import {ApprovedShortsFrame} from './approved-shorts-template.jsx';
import {BM0003NaturalEarthMap} from './natural-earth-map.jsx';
import {AlignedNarrationCaptions} from './aligned-captions.jsx';
import {resolveStoryChapters} from './chapter-timing.js';
import {currentBeatAt,easeOut,headlineCharsAt,scenePoseAt} from './motion-v6-timing.js';
import {BODY_FONT,DISPLAY_FONT} from './fonts.js';
import {BRAND as B} from './brand.js';

const themes=['midnight','ivory','midnight','ivory','midnight','saffron'];

function Evidence({scene,local}) {
  const enter=easeOut((local-.1)/.74);
  const items=scene.items ?? (scene.kind==='comparison' ?
    [scene.leftText,'Active GPU count undisclosed'] : [scene.metricLabel,scene.note].filter(Boolean));
  return <div style={{position:'absolute',top:777,left:80,right:165,minHeight:430,boxSizing:'border-box',
    padding:42,borderRadius:40,background:'#101D27',color:B.ivory,fontFamily:BODY_FONT,
    border:'2px solid #48656B',opacity:enter,transform:`translate(${142*(1-enter)}px,${16*(1-enter)}px)`}}>
    {items.length ? items.map((label,i)=><div key={label} style={{
      fontSize:i===0?48:34,fontWeight:i===0?800:600,color:i===0?'#FFBE91':B.ivory,marginBottom:24,
    }}>{label}</div>) : <>
      <div style={{fontSize:22,letterSpacing:2,color:'#8AD5C8'}}>COMPUTE INFRASTRUCTURE SCHEMATIC</div>
      <div style={{display:'flex',gap:24,margin:'27px 0'}}>
        {[0,1,2].map(i=><div key={i} style={{flex:1,padding:13,border:'2px solid #648486',
          background:'#284651',borderRadius:15,transform:`translateX(${-55*(1-easeOut((local-.2-i*.4)/.6))}px)`}}>
          {[0,1,2,3,4].map(j=><div key={j} style={{height:24,margin:7,background:'#507078',
            borderRadius:4,borderRight:'7px solid #7DD6C9'}}/>)}
        </div>)}
      </div>
    </>}
    <div style={{fontSize:29,lineHeight:1.25}}>{scene.subhead}</div>
  </div>;
}

function Pilot({story,alignments}) {
  const time=useCurrentFrame()/30;
  let start=0;
  const beats=story.scenes.map((scene,i)=>{
    const beat={...scene,startSec:start,endSec:start+scene.duration,theme:themes[i]};
    start=beat.endSec;
    return beat;
  });
  const index=currentBeatAt(time,beats);
  const active=beats[index];
  return <ApprovedShortsFrame theme={active.theme} topic="Infrastructure" timeSec={time}
    chapters={resolveStoryChapters(story)} caption={<AlignedNarrationCaptions
      alignment={alignments[index]} timeSec={time-active.startSec} theme={active.theme}/>}>
    {beats.map((scene,i)=>{
      const pose=scenePoseAt(time,i,beats);
      if(!pose.opacity)return null;
      const local=time-scene.startSec;
      const enter=easeOut((local+.05)/.54);
      const dark=scene.theme==='midnight';
      const background=dark?B.charcoal:scene.theme==='saffron'?
        'linear-gradient(138deg,#E8752E,#EF9962)':'linear-gradient(140deg,#FFF7EB,#FBF0E1)';
      return <AbsoluteFill key={scene.headline} style={{background,color:dark?B.ivory:B.charcoal,
        overflow:'hidden',opacity:pose.opacity,transform:`translateX(${pose.translateX}px)`}}>
        <div style={{position:'absolute',left:-240,top:1130,width:1130,height:750,
          border:'55px solid #117A7A19',borderRadius:'50%',transform:'rotate(-22deg)'}}/>
        <div style={{position:'absolute',top:283,left:86,right:165,fontFamily:BODY_FONT,fontSize:27,
          fontWeight:700,letterSpacing:3.1,color:dark?'#8AD5C8':B.charcoal,
          opacity:enter,transform:`translateX(${90*(1-enter)}px)`}}>{scene.kicker}</div>
        <div style={{position:'absolute',top:364,left:83,right:165,fontFamily:DISPLAY_FONT,fontSize:88,
          fontWeight:800,lineHeight:1.14,letterSpacing:-3,opacity:enter,
          transform:`translateX(${106*(1-enter)}px)`}}>{headlineCharsAt(scene.headline,local)}</div>
        {i===1 ? <BM0003NaturalEarthMap localTime={local} duration={scene.duration}/> : <Evidence scene={scene} local={local}/>}
      </AbsoluteFill>;
    })}
  </ApprovedShortsFrame>;
}

registerRoot(()=> <Composition id="BM0003Pilot" component={Pilot} width={1080} height={1920}
  fps={30} durationInFrames={1} calculateMetadata={({props})=>({
    durationInFrames:props.story.scenes.reduce((total,scene)=>total+Math.round(scene.duration*30),0),
  })}/>);
