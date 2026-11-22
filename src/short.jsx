import React from 'react';
import {
  AbsoluteFill, Audio, Easing, interpolate, Sequence, spring,
  staticFile, useCurrentFrame, useVideoConfig
} from 'remotion';
import {BRAND as B, getTheme} from './brand.js';
import {DISPLAY_FONT, BODY_FONT} from './fonts.js';
import {BrandAvatar, BrandBadge} from './brand-assets.jsx';

const easing = Easing.bezier(0.22, 1, 0.36, 1);
const rise = (frame, delay = 0) => interpolate(
  frame - delay, [0, 24], [48, 0],
  {easing, extrapolateLeft:'clamp', extrapolateRight:'clamp'}
);
const reveal = (frame, delay = 0) => interpolate(
  frame - delay, [0, 18], [0, 1],
  {extrapolateLeft:'clamp', extrapolateRight:'clamp'}
);
const fmt = (value) => Math.round(value).toLocaleString('en-IN');

function Surface({theme, children, style = {}}) {
  return <div style={{
    background:theme.surface, border:'2px solid '+theme.border, borderRadius:34,
    boxShadow:'0 18px 50px rgba(15,31,36,0.06)', padding:40, ...style
  }}>{children}</div>;
}
function Label({theme, children}) {
  return <div style={{
    alignSelf:'flex-start',display:'inline-flex',borderRadius:80,
    background:theme.soft,color:theme.accentText,
    fontFamily:BODY_FONT,fontSize:23,fontWeight:800,letterSpacing:1,
    padding:'16px 25px',maxWidth:820
  }}>{children}</div>;
}
function Head({theme,children,size=90}) {
  return <div style={{
    fontFamily:DISPLAY_FONT,fontSize:size,fontWeight:800,
    lineHeight:1.08,letterSpacing:-2.6,color:theme.text,whiteSpace:'pre-line'
  }}>{children}</div>;
}
function Backdrop({theme,family}) {
  return <>
    <div style={{
      position:'absolute',width:900,height:900,borderRadius:900,opacity:0.75,
      background:'radial-gradient(circle,'+theme.glow+' 0%, transparent 67%)',
      right:-470,top:250
    }}/>
    <div style={{
      position:'absolute',width:680,height:680,borderRadius:680,opacity:0.45,
      background:'radial-gradient(circle,'+theme.soft+' 0%, transparent 72%)',
      left:-400,bottom:240
    }}/>
    {family==='timeline' && <div style={{position:'absolute',left:44,top:300,bottom:360,width:5,background:theme.accent,opacity:.5,borderRadius:8}}/>}
  </>;
}
function Chrome({story,index,theme}) {
  return <>
    <div style={{position:'absolute',top:110,left:78,right:78,display:'flex',justifyContent:'space-between',alignItems:'center',gap:24}}>
      <BrandAvatar size={82}/>
      <div style={{
        fontFamily:BODY_FONT,fontWeight:750,fontSize:21,background:theme.soft,
        borderRadius:28,padding:'14px 18px',textTransform:'uppercase',color:theme.accentText,
        maxWidth:340
      }}>{story.category}</div>
    </div>
    <div style={{position:'absolute',left:78,right:78,top:216,height:4,borderRadius:4,background:theme.soft,overflow:'hidden'}}>
      <div style={{height:'100%',width:((index+1)/story.scenes.length*100)+'%',background:theme.accent}}/>
    </div>
    <div style={{
      position:'absolute',bottom:338,left:78,right:78,display:'flex',justifyContent:'space-between',
      gap:30,fontSize:22,color:theme.muted,fontFamily:BODY_FONT
    }}>
      <span>Source: {story.sourceShort}</span><span>{index+1} / {story.scenes.length}</span>
    </div>
    <div style={{
      position:'absolute',bottom:296,left:78,right:78,
      fontFamily:BODY_FONT,fontSize:21,color:theme.muted
    }}>{story.sourceContext}</div>
  </>;
}
function VisualGraphic({scene,theme,family}) {
  const type=scene.visual || (family==='explainer'?'process':family==='data-led'?'server-grid':'network');
  const cell={borderRadius:20,border:'2px solid '+theme.border,background:theme.surface};
  if(type==='server-grid')return <div style={{marginTop:84}}>
    <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:20}}>
      {Array.from({length:9},(_,i)=><div key={i} style={{...cell,height:119,padding:22}}>
        <div style={{width:'78%',height:8,background:theme.accent,borderRadius:8,opacity:i%2?.85:.45,marginTop:20}}/>
        <div style={{height:8,width:'52%',background:theme.teal,borderRadius:8,opacity:.43,marginTop:14}}/>
      </div>)}
    </div>
    <div style={{color:theme.muted,fontSize:23,textAlign:'center',marginTop:20}}>Illustrative computing schematic</div>
  </div>;
  if(type==='process')return <div style={{marginTop:93,display:'flex',alignItems:'center',justifyContent:'space-between',gap:11}}>
    {['RESEARCH','LICENSE','DEVELOP'].map((part,i)=><React.Fragment key={part}>
      <div style={{
        width:230,height:230,borderRadius:120,display:'flex',alignItems:'center',justifyContent:'center',
        background:i===1?theme.soft:theme.surface,border:'3px solid '+theme.border,
        color:i===1?theme.accentText:theme.text,fontSize:26,fontWeight:800,textAlign:'center'
      }}>{part}</div>
      {i<2&&<div style={{height:6,width:40,borderRadius:6,background:theme.teal}}/>}
    </React.Fragment>)}
    <div style={{position:'absolute',marginTop:330,color:theme.muted,fontSize:22}}>Illustrative research-to-industry pathway</div>
  </div>;
  if(family==='timeline')return <div style={{marginTop:80,display:'grid',gap:30}}>
    {['PAST','TODAY','NEXT'].map((part,i)=><div key={part} style={{display:'flex',alignItems:'center',gap:20}}>
      <div style={{width:26,height:26,borderRadius:30,background:i===1?theme.accent:theme.teal}}/>
      <Surface theme={theme} style={{flex:1,padding:28,fontWeight:800,fontSize:26,color:theme.text}}>{part}</Surface>
    </div>)}
    <div style={{color:theme.muted,fontSize:22}}>Illustrative sequence — not a factual timeline</div>
  </div>;
  return <div style={{marginTop:90,position:'relative',height:365,display:'flex',alignItems:'center',justifyContent:'center'}}>
    <div style={{width:300,height:300,border:'5px solid '+theme.teal,borderRadius:'50%',opacity:.38}}/>
    <div style={{position:'absolute',width:210,height:210,border:'18px solid '+theme.accent,borderRadius:'50%',opacity:.86}}/>
    <div style={{position:'absolute',width:90,height:90,background:theme.text,borderRadius:'50%'}}/>
    <div style={{position:'absolute',bottom:0,fontSize:22,color:theme.muted}}>Illustrative diagram</div>
  </div>;
}
function Metric({scene,theme,frame,family}) {
  const animated=interpolate(frame,[0,39],[0,scene.number],{easing,extrapolateLeft:'clamp',extrapolateRight:'clamp'});
  const numberSize=scene.number>999999?115:156;
  const number=<div style={{
    fontFamily:DISPLAY_FONT,fontSize:numberSize,fontWeight:800,letterSpacing:-5,
    color:family==='explainer'?theme.text:theme.dataColor,lineHeight:1.1,fontVariantNumeric:'tabular-nums'
  }}>{fmt(animated)}{scene.suffix||''}</div>;
  const label=<div style={{fontFamily:BODY_FONT,fontSize:39,fontWeight:800,color:theme.text,lineHeight:1.23,marginTop:21}}>{scene.metricLabel}</div>;
  if(family==='explainer')return <div style={{marginTop:70}}>
    <div style={{background:theme.soft,padding:'48px 40px',borderRadius:46}}>{number}{label}</div>
    <div style={{fontFamily:BODY_FONT,fontSize:33,color:theme.muted,lineHeight:1.35,marginTop:36}}>{scene.subhead}</div>
    <div style={{marginTop:65,borderLeft:'7px solid '+theme.teal,paddingLeft:28,fontSize:30,color:theme.text,lineHeight:1.36}}>{scene.note}</div>
  </div>;
  return <div style={{marginTop:70}}>
    <Surface theme={theme}>{number}{label}
      <div style={{fontSize:29,color:theme.muted,marginTop:27,lineHeight:1.4}}>{scene.subhead}</div>
    </Surface>
    <div style={{fontSize:29,color:theme.muted,marginTop:37,lineHeight:1.43}}>{scene.note}</div>
  </div>;
}
function Scene({story,scene,index}) {
  const frame=useCurrentFrame();
  const {fps}=useVideoConfig();
  const entered=spring({frame,fps,config:{damping:18,stiffness:96}});
  const theme=getTheme(story.visualTheme);
  const family=story.visualFamily || 'data-led';
  const small=family==='explainer';
  return <AbsoluteFill style={{background:theme.bg,fontFamily:BODY_FONT,overflow:'hidden'}}>
    <Backdrop theme={theme} family={family}/>
    <div style={{
      position:'absolute',top:family==='field-report'?335:348,left:78,right:78,
      opacity:reveal(frame),transform:'translateY('+rise(frame)+'px)'
    }}>
      <Label theme={theme}>{scene.kicker}</Label>
      {scene.kind==='hook'&&<>
        <div style={{marginTop:57}}><Head theme={theme} size={small?92:101}>{scene.headline}</Head></div>
        <div style={{fontSize:39,lineHeight:1.35,color:theme.muted,marginTop:38}}>{scene.subhead}</div>
        <VisualGraphic scene={scene} theme={theme} family={family}/>
      </>}
      {(scene.kind==='metric'||scene.kind==='impact')&&<>
        <div style={{marginTop:60}}><Head theme={theme} size={small?77:81}>{scene.headline}</Head></div>
        <Metric scene={scene} theme={theme} frame={frame} family={family}/>
      </>}
      {scene.kind==='comparison'&&<>
        <div style={{marginTop:55}}><Head theme={theme} size={82}>{scene.headline}</Head></div>
        <div style={{display:'grid',gridTemplateColumns:'1fr',gap:24,marginTop:67}}>
          <Surface theme={theme} style={{borderLeft:'10px solid '+theme.teal}}>
            <div style={{fontSize:25,fontWeight:850,color:theme.teal,letterSpacing:1}}>{scene.leftLabel}</div>
            <div style={{fontFamily:DISPLAY_FONT,fontSize:47,fontWeight:750,color:theme.text,lineHeight:1.2,marginTop:18}}>{scene.leftText}</div>
          </Surface>
          <Surface theme={theme} style={{borderLeft:'10px solid '+theme.accent}}>
            <div style={{fontSize:25,fontWeight:850,color:theme.accentText,letterSpacing:1}}>{scene.rightLabel}</div>
            <div style={{fontFamily:DISPLAY_FONT,fontSize:46,fontWeight:750,color:theme.text,lineHeight:1.2,marginTop:18}}>{scene.rightText}</div>
          </Surface>
        </div>
        <div style={{fontSize:30,color:theme.muted,marginTop:42,lineHeight:1.4}}>{scene.subhead}</div>
      </>}
      {scene.kind==='uses'&&<>
        <div style={{marginTop:56}}><Head theme={theme} size={84}>{scene.headline}</Head></div>
        <div style={{marginTop:64,display:'flex',flexDirection:small?'row':'column',flexWrap:small?'wrap':'nowrap',gap:21}}>
          {scene.items.map((item,i)=><div key={i} style={{opacity:reveal(frame,i*5),flex:small?'1 1 40%':'auto'}}>
            <Surface theme={theme} style={{padding:small?30:40,display:'flex',alignItems:'center',gap:18}}>
              <div style={{width:18,height:18,flexShrink:0,borderRadius:30,background:theme.accent}}/>
              <div style={{fontSize:small?31:37,fontWeight:750,color:theme.text,lineHeight:1.26}}>{item}</div>
            </Surface>
          </div>)}
        </div>
        <div style={{fontSize:32,color:theme.muted,marginTop:42,lineHeight:1.4}}>{scene.subhead}</div>
      </>}
      {scene.kind==='close'&&<>
        <div style={{marginTop:80}}><Head theme={theme} size={96}>{scene.headline}</Head></div>
        <div style={{fontSize:39,lineHeight:1.35,color:theme.muted,marginTop:43}}>{scene.subhead}</div>
        <div style={{marginTop:124,transform:'scale('+(0.95+0.05*entered)+')',transformOrigin:'left'}}>
          <BrandBadge width={860}/>
        </div>
      </>}
    </div>
    <Chrome story={story} index={index} theme={theme}/>
  </AbsoluteFill>;
}
export const BharatShort = ({story}) => {
  if (!story?.scenes?.length) return <AbsoluteFill style={{background:B.ivory}}/>;
  let position=0;
  return <AbsoluteFill style={{background:getTheme(story.visualTheme).bg}}>
    <Audio src={staticFile('music/ambient.wav')} volume={0.14} loop/>
    {story.scenes.map((scene,index)=>{
      const from=position;
      const durationInFrames=Math.round(scene.duration*30);
      position+=durationInFrames;
      return <Sequence key={index} from={from} durationInFrames={durationInFrames}>
        <Scene story={story} scene={scene} index={index}/>
        {['metric','impact'].includes(scene.kind)&&<Audio src={staticFile('sfx/metric-rise.wav')} volume={0.16}/>}
        {scene.kind==='close'&&<Audio src={staticFile('sfx/mode-on.wav')} volume={0.20}/>}
        {story.hasVoice&&<Audio src={staticFile('voice/'+story.slug+'/'+index+'.wav')} volume={0.95}/>}
      </Sequence>;
    })}
  </AbsoluteFill>;
};
