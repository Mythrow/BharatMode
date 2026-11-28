from pathlib import Path
import json,base64,html,zipfile
from PIL import Image,ImageDraw
import cairosvg
import render_storyboard as r
B=Path(__file__).resolve().parent; O=B/'frames';O.mkdir(exist_ok=True)
# 3 meaningful states each, plus opening and last state.
times=[0,.5,3.2,7.7,9.3,10.95,12.75,14.55,16.3,17.4,19.7,20.5,21.75,22.65,23.45,24.25,25.35,26.75,28.5,33,37.7,39.5,43,46.7,47.4,49.8,51.1,52.55,54.7]
rows=[]
for k,t in enumerate(times):
 i=min(5,__import__('bisect').bisect_right(r.BOUNDS,t)-1);name=f'{k+1:02d}-s{i+1}-{t:.2f}.png';p=O/name
 svg=r.frame(t);cairosvg.svg2png(bytestring=svg.encode(),write_to=str(p));assert Image.open(p).size==(1080,1920)
 rows.append({'time':t,'scene':i+1,'file':name,'image':'data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode(),'narration':r.SCRIPTS[i]})
# Contact grid grouping chronological states; actual render thumbnails only.
thumbw=216;thumbh=384;cols=5;rowsn=(len(rows)+cols-1)//cols
sheet=Image.new('RGB',(cols*(thumbw+12)+12,rowsn*(thumbh+42)+12),'#18242b');d=ImageDraw.Draw(sheet)
for k,row in enumerate(rows):
 im=Image.open(O/row['file']).convert('RGB').resize((thumbw,thumbh),Image.Resampling.LANCZOS);x=12+(k%cols)*(thumbw+12);y=12+(k//cols)*(thumbh+42);sheet.paste(im,(x,y));d.text((x,y+thumbh+9),f"S{row['scene']:02d}  |  {row['time']:.2f}s",fill='white')
sheet.save(B.parent/'BM-007-storyboard-contact-v4.png')
# Self-contained browser viewer, static grid fallback.
items=''.join(f'<article><img src="{a["image"]}" alt="Scene {a["scene"]} at {a["time"]} seconds" loading="lazy"><h3>Scene {a["scene"]} · {a["time"]:.2f}s</h3><p>{html.escape(a["narration"])}</p></article>' for a in rows)
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>BM-007 | Visual storyboard</title><style>body{margin:0;background:#0b1018;color:#fff7eb;font:16px system-ui}main{max-width:1300px;margin:auto;padding:25px}h1{font-size:clamp(24px,4vw,40px)}header{border-bottom:2px solid #e8752e;margin-bottom:22px}p{line-height:1.5;color:#c6d1d0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:20px}article{min-width:0}img{width:100%;height:auto;display:block;border-radius:10px;cursor:zoom-in}h3{font-size:15px}article p{font-size:13px}dialog{border:0;padding:12px;background:#18242b;color:white;max-width:95vw}dialog img{width:auto;max-width:90vw;max-height:83vh;object-fit:contain;cursor:default}button{background:#fff7eb;color:#0b1018;border:0;padding:9px 15px;border-radius:6px;cursor:pointer}nav{display:flex;justify-content:space-between;margin:8px 0}</style><main><header><p>BHARAT MODE / BM-007 / STORYBOARD V4</p><h1>Indian Navy Gets 7th Homegrown Stealth Warship</h1><p>29 actual source-rendered frames · 1080 × 1920 · provisional timings · click a frame for native review. Conceptual ship illustrations, not authentic photographs. No audio generated.</p></header><div class="grid">'''+items+'''</div></main><dialog id="viewer"><nav><button id="prev">Previous</button><button id="close">Close</button><button id="next">Next</button></nav><img id="large"><p id="label"></p></dialog><script>const imgs=[...document.querySelectorAll('article img')];let i=0;const d=document.getElementById('viewer');function show(n){i=(n+imgs.length)%imgs.length;document.getElementById('large').src=imgs[i].src;document.getElementById('label').textContent=imgs[i].alt;}imgs.forEach((im,j)=>im.onclick=()=>{show(j);d.showModal()});document.getElementById('prev').onclick=()=>show(i-1);document.getElementById('next').onclick=()=>show(i+1);document.getElementById('close').onclick=()=>d.close();document.addEventListener('keydown',e=>{if(d.open&&e.key==='ArrowRight')show(i+1);if(d.open&&e.key==='ArrowLeft')show(i-1)});</script></html>'''
(B.parent/'BM-007-storyboard-gallery-v4.html').write_text(page)
(B/'script.json').write_text(json.dumps(r.SCRIPTS,indent=2,ensure_ascii=False)+'\n')
(B/'storyboard.json').write_text(json.dumps({'productionCode':'BM-007','revision':'V4','width':1080,'height':1920,'fps':60,'provisionalBounds':r.BOUNDS,'scenes':r.SCENES,'samples':[dict((k,v) for k,v in a.items() if k!='image' and k!='narration') for a in rows],'audio':'not generated; provisional captions','fonts':'Inter fallback'},indent=2)+'\n')
