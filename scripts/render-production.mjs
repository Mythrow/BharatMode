// Main production conversation only. Preflight before invoking Remotion.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawnSync} from 'node:child_process';
import {validateProduction} from '../src/production-contract.js';
const [input,output]=process.argv.slice(2);
const fail=m=>{throw Error(m)};
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const run=(bin,args)=>{const r=spawnSync(bin,args,{encoding:'utf8',maxBuffer:64*1024*1024});if(r.status!==0)fail(bin+' failed: '+(r.stderr||r.error||r.status));return r.stdout};
const duration=p=>Number(run('ffprobe',['-v','error','-show_entries','format=duration','-of','default=nw=1:nk=1',p]).trim());
try{
 if(!input||!output)fail('Usage: npm run render:production -- private/props.json out/BM-###-slug.mp4');
 const props=JSON.parse(fs.readFileSync(input,'utf8')),plan=validateProduction(props);
 const registry=JSON.parse(fs.readFileSync('content/registry.json','utf8'));
 const item=registry.items.find(x=>x.id===props.story.contentId&&x.productionCode===props.production.productionCode);
 if(!item||item.stage!=='in_progress')fail('Render restricted to selected active production; no existing release renders');
 if(!item.storyPath)fail('Commit approved structured story first');
 if(JSON.stringify(JSON.parse(fs.readFileSync(item.storyPath)).story)!==JSON.stringify(props.story))fail('Production props differ from committed structured story');
 const publicRoot=fs.realpathSync('public/production-private');
 const resolve=p=>{const absolute=fs.realpathSync(path.join('public',p));if(!absolute.startsWith(publicRoot+path.sep))fail('Private asset escapes approved directory');return absolute};
 for(const asset of props.production.assets)if(hash(resolve(asset.path))!==asset.sha256)fail('Asset hash mismatch: '+asset.path);
 for(const scene of plan.scenes)if(Math.abs(duration(resolve(scene.wavPath))-scene.alignment.audio.durationSeconds)>.025)fail('Scene WAV duration mismatch');
 const master=resolve(props.production.master.path);
 if(Math.abs(duration(master)-plan.durationInFrames/60)>.0167)fail('Master duration mismatch');
 // Silence in final hold: decode actual master samples, not container duration alone.
 const silence=spawnSync('ffmpeg',['-v','error','-ss',String(plan.audibleFrames/60),'-i',master,'-t','1','-f','s16le','-acodec','pcm_s16le','-'],{maxBuffer:8*1024*1024});
 if(silence.status!==0||!silence.stdout?.length||silence.stdout.some(x=>x!==0))fail('Final hold must be digitally silent in PCM master');
 const out=path.resolve(output);if(!out.startsWith(path.resolve('out')+path.sep)||!out.endsWith('.mp4')||fs.existsSync(out))fail('Output must be a new ignored out/ MP4, never overwrite existing media');
 fs.mkdirSync(path.dirname(out),{recursive:true});
 run(process.platform==='win32'?'npx.cmd':'npx',['--no-install','remotion','render','src/index.jsx','BharatShort',out,'--props='+input,'--codec=h264','--crf=17']);
 const probe=JSON.parse(run('ffprobe',['-v','error','-select_streams','v:0','-count_frames','-show_streams','-show_entries','stream=width,height,r_frame_rate,nb_read_frames,duration','-of','json',out])).streams[0];
 if(probe.width!==1080||probe.height!==1920||probe.r_frame_rate!=='60/1'||Number(probe.nb_read_frames)!==plan.durationInFrames)fail('Decoded output geometry/frame count mismatch');
 const pts=JSON.parse(run('ffprobe',['-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',out])).frames;
 if(pts.length!==plan.durationInFrames||pts.some((f,i)=>i>0&&Math.abs(Number(f.best_effort_timestamp_time)-Number(pts[i-1].best_effort_timestamp_time)-1/60)>.00001))fail('Output frame timestamps not consecutive');
 run('ffmpeg',['-v','error','-xerror','-i',out,'-f','null','-']);
 console.log(JSON.stringify({status:'technical_candidate_human_QA_required',frames:plan.durationInFrames,sha256:hash(out),pending:['decoded-frame motion and collision review','audio mix and fade listening','phone QA','owner creative and publication gates']},null,2));
}catch(e){console.error(e.message);process.exitCode=1}
