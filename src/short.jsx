import React from 'react';
import {
  AbsoluteFill, Audio, Easing, interpolate, Sequence, spring,
  staticFile, useCurrentFrame, useVideoConfig
} from 'remotion';
import {BRAND as B, TYPEFACE as F} from './brand.js';

const easing = Easing.bezier(0.22, 1, 0.36, 1);
const fade = (frame, delay = 0) => interpolate(
  frame - delay, [0, 20], [0, 1],
  {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'}
);
const slide = (frame) => interpolate(frame, [0, 24], [42, 0], {
  easing, extrapolateLeft: 'clamp', extrapolateRight: 'clamp'
});
const pretty = (value) => Math.round(value).toLocaleString('en-IN');

function Chrome({story,index}) {
  return <>
    <div style={{position:'absolute',top:118,left:78,right:78,display:'flex',justifyContent:'space-between',alignItems:'center'}}>
      <div style={{display:'flex',gap:14,alignItems:'center',fontSize:31,fontWeight:850,letterSpacing:-0.8,color:B.ink}}>
        <div style={{width:17,height:17,borderRadius:'50%',background:B.primary}}/>
        BHARAT MODE
      </div>
      <span style={{fontSize:22,fontWeight:750,color:B.primary,background:B.white,borderRadius:50,padding:'13px 20px',maxWidth:330,textTransform:'uppercase'}}>{story.category}</span>
    </div>
    <div style={{position:'absolute',top:218,left:78,right:78,height:4,background:B.soft,borderRadius:10}}>
      <div style={{height:'100%',width:((index+1)/story.scenes.length*100)+'%',background:B.primary,borderRadius:10}}/>
    </div>
    <div style={{position:'absolute',bottom:345,left:78,right:78,display:'flex',justifyContent:'space-between',fontSize:24,color:B.muted}}>
      <span>Source: {story.sourceShort}</span>
      <span>{index+1} / {story.scenes.length}</span>
    </div>
    <div style={{position:'absolute',bottom:300,left:78,right:78,color:B.muted,fontSize:21}}>{story.sourceContext}</div>
  </>;
}
function Background() {
  return <>
    <div style={{position:'absolute',width:840,height:840,borderRadius:'50%',background:'radial-gradient(circle, '+B.soft+' 0%, transparent 70%)',right:-400,top:280}}/>
    <div style={{position:'absolute',width:850,height:850,borderRadius:'50%',background:'radial-gradient(circle, #FCEBD9 0%, transparent 70%)',left:-500,bottom:170}}/>
  </>;
}
function Tag({children}) {
  return <div style={{alignSelf:'flex-start',display:'inline-block',background:B.white,border:'2px solid '+B.soft,color:B.primary,borderRadius:80,padding:'16px 25px',fontSize:25,fontWeight:800,letterSpacing:1}}>{children}</div>;
}
function Heading({children,size=94}) {
  return <div style={{fontWeight:850,fontSize:size,lineHeight:1.09,letterSpacing:-2.5,color:B.ink,whiteSpace:'pre-line'}}>{children}</div>;
}
function Panel({children}) {
  return <div style={{background:'rgba(255,255,255,.95)',border:'2px solid '+B.soft,borderRadius:36,padding:50,boxShadow:'0 24px 64px rgba(23,54,58,.07)'}}>{children}</div>;
}
function Diagram() {
  return <div style={{marginTop:88,display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:20}}>
    {Array.from({length:9},(_,i)=><div key={i} style={{height:132,borderRadius:23,background:i%2?B.soft:'#F4E8D8',border:'3px solid #B8D2CB',padding:22}}>
      <div style={{height:10,background:B.primary,opacity:.5,borderRadius:8,marginTop:17}}/>
      <div style={{height:10,width:'70%',background:B.muted,opacity:.27,borderRadius:8,marginTop:14}}/>
    </div>)}
    <div style={{gridColumn:'1 / -1',fontSize:24,color:B.muted,textAlign:'center',marginTop:8}}>Illustrative computing infrastructure</div>
  </div>;
}
function Scene({story,scene,index}) {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const entered = spring({frame,fps,config:{damping:18,stiffness:96}});
  const mainStyle = {
    position:'absolute',top:355,left:78,right:78,
    opacity:fade(frame),transform:'translateY('+slide(frame)+'px)'
  };
  const detailStyle = {fontSize:40,lineHeight:1.35,color:B.muted,marginTop:40};
  return <AbsoluteFill style={{fontFamily:F,background:B.bg,overflow:'hidden'}}>
    <Background/>
    <div style={mainStyle}>
      <Tag>{scene.kicker}</Tag>
      {scene.kind==='hook' && <>
        <div style={{marginTop:62}}><Heading size={104}>{scene.headline}</Heading></div>
        <div style={detailStyle}>{scene.subhead}</div>
        <Diagram/>
      </>}
      {(scene.kind==='metric'||scene.kind==='impact') && <>
        <div style={{marginTop:62}}><Heading size={77}>{scene.headline}</Heading></div>
        <div style={{marginTop:72}}>
          <Panel>
            <div style={{fontSize:scene.number>999999?118:166,fontWeight:850,letterSpacing:-7,color:B.primary,lineHeight:1}}>
              {pretty(interpolate(frame,[0,38],[0,scene.number],{easing,extrapolateLeft:'clamp',extrapolateRight:'clamp'}))}{scene.suffix||''}
            </div>
            <div style={{fontSize:40,fontWeight:780,lineHeight:1.23,color:B.ink,marginTop:32}}>{scene.metricLabel}</div>
            <div style={{fontSize:27,color:B.muted,marginTop:30}}>{scene.subhead}</div>
          </Panel>
        </div>
        <div style={{fontSize:30,color:B.muted,marginTop:45,lineHeight:1.4}}>{scene.note}</div>
      </>}
      {scene.kind==='uses' && <>
        <div style={{marginTop:56}}><Heading size={82}>{scene.headline}</Heading></div>
        <div style={{marginTop:68,display:'flex',flexDirection:'column',gap:22}}>
          {scene.items.map((item,i)=><div key={i} style={{opacity:fade(frame,i*6)}}>
            <Panel><span style={{fontSize:40,fontWeight:750,color:B.ink}}><span style={{color:B.primary}}>● </span>{item}</span></Panel>
          </div>)}
        </div>
        <div style={detailStyle}>{scene.subhead}</div>
      </>}
      {scene.kind==='close' && <>
        <div style={{marginTop:90}}><Heading size={102}>{scene.headline}</Heading></div>
        <div style={detailStyle}>{scene.subhead}</div>
        <div style={{marginTop:150,display:'flex',alignItems:'center',gap:24,transform:'scale('+(0.93+0.07*entered)+')',transformOrigin:'left'}}>
          <div style={{width:65,height:65,background:B.primary,borderRadius:100}}/>
          <div>
            <div style={{fontSize:55,fontWeight:900,letterSpacing:-2,color:B.ink}}>BHARAT MODE</div>
            <div style={{fontSize:26,color:B.primary,fontWeight:800}}>MODE: ON · {B.tagline}</div>
          </div>
        </div>
      </>}
    </div>
    <Chrome story={story} index={index}/>
  </AbsoluteFill>;
}
export const BharatShort = ({story}) => {
  if (!story?.scenes?.length) return <AbsoluteFill style={{background:B.bg}}/>;
  let position=0;
  return <AbsoluteFill style={{background:B.bg}}>
    <Audio src={staticFile('music/ambient.wav')} volume={0.14} loop/>
    {story.scenes.map((scene,index)=>{
      const from=position;
      const durationInFrames=Math.round(scene.duration*30);
      position+=durationInFrames;
      return <Sequence key={index} from={from} durationInFrames={durationInFrames}>
        <Scene story={story} scene={scene} index={index}/>
        {['metric','impact'].includes(scene.kind) && <Audio src={staticFile('sfx/metric-rise.wav')} volume={0.16}/>}
        {scene.kind==='close' && <Audio src={staticFile('sfx/mode-on.wav')} volume={0.20}/>}
        {story.hasVoice && <Audio src={staticFile('voice/'+story.slug+'/'+index+'.wav')} volume={0.95}/>}
      </Sequence>;
    })}
  </AbsoluteFill>;
};
