from pathlib import Path
import json, hashlib, subprocess, sys
import render_storyboard as r
from render_motion import raster
from PIL import Image
P=Path(__file__).resolve().parent; D=P.parent; S=P/'segments'; out=D/'BM-007-V5-music-preview.mp4'
M=D/'bm006_recovery/techno-thriller-final.mp3'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(M)=='adb6260d0dd451add9148e0d3ca1d225ab268c2f8fbe3e2010f10337a92755f9'
paths=[S/'s1.mp4',D/'bm007_v4/scene2.mp4',D/'BM-007-V5-map-motion-review.mp4',S/'s4.mp4',S/'s5.mp4',D/'bm007_v3/scene6.mp4']
counts=[480,720,420,660,540,480]
def probe(p):return json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=width,height,r_frame_rate,nb_frames,time_base','-of','json',str(p)]))['streams'][0]
for p,n in zip(paths,counts):
 a=probe(p);assert int(a['nb_frames'])==n and (a['width'],a['height'],a['r_frame_rate'])==(1080,1920,'60/1'),(str(p),a)
# Final hold is the fully resolved last state with completed chapter progress.
frame=raster(r.frame(55.0)); hp=S/'hold.mp4'
cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgra','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','2','-preset','ultrafast','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(hp)]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(60): p.stdin.write(frame.tobytes())
p.stdin.close();assert p.wait()==0
assert int(probe(hp)['nb_frames'])==60
paths.append(hp); counts.append(60)
con=S/'concat.txt';con.write_text(''.join(f"file '{p.resolve()}'\n" for p in paths))
# Keep exact rendered video samples. Music plays at the approved non-speech gain; no standalone master distributed.
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(con),'-i',str(M),'-map','0:v:0','-map','1:a:0','-c:v','copy','-af','volume=0.55,afade=t=in:st=0:d=0.18,afade=t=out:st=54.15:d=0.837,apad=whole_dur=56,atrim=duration=56','-c:a','aac','-b:a','192k','-ar','48000','-t','56','-movflags','+faststart',str(out)],check=True)
print('Assembled',out,sha(out),flush=True)
qa={'preview':out.name,'sha256':sha(out),'scene_frames':counts,'music_sha256':sha(M),'music_gain':.55,'fade_in':.18,'fade_out_start':54.15,'fade_out_duration':.837,'music_only':True,'provisional_scene_bounds':r.BOUNDS,'hold_frames':60,'source_reuse':{'scene2':'V4 approved camera review','scene3':'V5 map review','scene6':'V3 unchanged fleet review'},'segments':[{ 'filename':str(p.relative_to(D)), 'frames':n,'sha256':sha(p)} for p,n in zip(paths,counts)]}
(P/'preview-qa.json').write_text(json.dumps(qa,indent=2)+'\n')
