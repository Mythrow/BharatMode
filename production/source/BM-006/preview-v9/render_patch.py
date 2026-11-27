import preview as p, subprocess,sys
start,end=map(int,sys.argv[1:3]); out=sys.argv[3]
cmd=['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r','60','-i','-','-an','-c:v','libx264','-threads','2','-preset','ultrafast','-crf','17','-pix_fmt','yuv420p','-vf','scale=out_color_matrix=bt709','-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709',out]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(start,end):
 proc.stdin.write(p.frame(n).tobytes())
 if n%120==0: print(n,flush=True)
proc.stdin.close(); assert proc.wait()==0
print('done',start,end,flush=True)
