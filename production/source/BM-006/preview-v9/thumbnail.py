from pathlib import Path
import sys,io,math
from PIL import Image, ImageDraw, ImageFont
import cairosvg
src=Path(sys.argv[1]);sys.path.insert(0,str(src));import render_storyboard as r
out=Path(sys.argv[2]);W,H=1080,1920
im=Image.new('RGB',(W,H),'#0B1018');d=ImageDraw.Draw(im)
# Quiet circuit board background, same story-specific dark opening design.
for i in range(11):
 x=65+95*i; y=960+45*(i%3);d.line([(x,880),(x,y),(x+32,y+32),(x+32,1620)],fill='#243D46',width=2)
fdir=Path('/usr/share/fonts/opentype/inter')
def font(n,s):return ImageFont.truetype(str(fdir/('Inter-'+n+'.otf')),s)
def visible(x,cy,s,f,fill):
 b=d.textbbox((0,0),s,font=f);d.text((x-b[0],round(cy-(b[1]+b[3])/2)),s,font=f,fill=fill)
 return (x,round(cy-(b[1]+b[3])/2)+b[1],x+b[2]-b[0],round(cy-(b[1]+b[3])/2)+b[3])
a=Image.open(io.BytesIO(cairosvg.svg2png(url=str(src/'avatar.svg'),output_width=138,output_height=138))).convert('RGBA');im.paste(a,(72,84),a)
word=visible(229,153,'BHARAT MODE',font('Bold',32),'#FFF7EB')
d.rounded_rectangle((730,120,1008,185),radius=33,fill='#FFF7EB');f=font('Medium',17);tw=d.textlength('ARTIFICIAL INTELLIGENCE',font=f);pill=visible(round(869-tw/2),152.5,'ARTIFICIAL INTELLIGENCE',f,'#0B1018')
assert abs((word[1]+word[3])/2-153)<=1
visible(82,328,'CHARIOT-1',font('Bold',39),'#70D3CC')
for s,y in [('India’s',465),('Homegrown',620),('AI',775)]:
 f=font('Bold',133);assert d.textlength(s,font=f)<916;visible(78,y,s,f,'#FFF7EB' if s!='AI' else '#FFBE91')
# Larger opening chip with side components; native SVG rendered without text overlays.
svg='<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">'
for x,y in [(185,1000),(895,1000),(185,1500),(895,1500)]:
 svg+=r.line(540,1250,x,y,'#70D3CC',3,.65)+r.circ(x,y,7,'#FFBE91')
 svg+=r.chip(x,y,120,100,0,True)
svg+=r.chip(540,1250,468,386,0,True)+'</svg>'
art=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert('RGBA');im.paste(art,(0,0),art)
d=ImageDraw.Draw(im);f=font('Medium',37);s='Trained from scratch in India';visible(round((W-d.textlength(s,font=f))/2),1720,s,f,'#70D3CC')
im.save(out);print('header bounds',word,pill,'avatar center',153)
