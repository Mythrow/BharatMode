#!/usr/bin/env python3
"""Build a SINGLE self-contained, browser-playable HTML page for music/voice QA.

For use by Bharat Mode coding/Work agents, not a local user installation step.
Embeds audio bytes as data:audio/mpeg base64 in HTML, with independently pausable
players and supporting context. NEVER commit output HTML if it embeds private,
licensed, user-supplied music or a private narrator. Keep HTML in ignored out/.

Usage:
  python scripts/build_audio_review_html.py --title 'Bharat Mode music check' \
    --track 'Ducked mix=/private/review.mp3' --track 'Music only=/private/music.mp3' \
    --out out/audio-review.html --note 'Owner review only'
"""
import argparse
import base64
import html
import mimetypes
from pathlib import Path

CSS = """
:root{color-scheme:dark;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:#0b1018;color:#fff7eb}
*{box-sizing:border-box}body{margin:0;min-height:100vh;background:radial-gradient(circle at 80% 0%,#15434a 0,transparent 45%),#0b1018}
main{max-width:850px;margin:auto;padding:32px 20px 70px}header span{font-size:11px;letter-spacing:2px;color:#70d3cc;text-transform:uppercase;font-weight:800}
h1{font-size:clamp(25px,4vw,40px);margin:12px 0 7px}p{line-height:1.5;color:#b9c9d1;margin:0 0 20px}
article{background:#171f29;border:1px solid #2d3d4b;border-radius:15px;padding:20px;margin:15px 0}h2{font-size:17px;margin:0 0 8px}
audio{width:100%;height:46px;display:block;margin-top:13px}small{display:block;font-size:12px;color:#adbfca}.foot{margin-top:24px}
"""

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--track',action='append',required=True,help='Title=/path/to/private-audio.mp3 (repeat for each audio track)')
    parser.add_argument('--title',default='Bharat Mode — Audio review')
    parser.add_argument('--note',default='Private review. Pause one player before starting another. No external downloads required.')
    args=parser.parse_args()
    if len(args.track)>12:parser.error('Maximum 12 review tracks')
    players=[]
    for item in args.track:
        if '=' not in item:parser.error('Each --track must have Title=/path format')
        title,name=item.split('=',1)
        path=Path(name)
        if not title.strip() or not path.is_file():parser.error(f'Missing title or file for {item}')
        media_type=mimetypes.guess_type(path.name)[0]
        if media_type not in {'audio/mpeg','audio/wav','audio/x-wav','audio/ogg','audio/mp4'}:parser.error(f'Unsupported audio extension: {path}')
        # Reproducible exact input bytes, not third-party scripts nor remote CDN links.
        src='data:'+media_type+';base64,'+base64.b64encode(path.read_bytes()).decode('ascii')
        players.append('<article><h2>'+html.escape(title)+'</h2><small>'+html.escape(path.suffix[1:].upper())+' · embedded audio, not a download</small><audio controls preload="none" src="'+src+'"></audio></article>')
    result='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(args.title)+'</title><style>'+CSS+'</style></head><body><main><header><span>Bharat Mode · Audio Review</span><h1>'+html.escape(args.title)+'</h1></header><p>'+html.escape(args.note)+'</p>\n'+'\n'.join(players)+'\n<p class="foot">All audio is embedded. This file contains the private audio bytes: share only as intended, and do not commit to public Git.</p></main><script>document.querySelectorAll("audio").forEach(a=>a.addEventListener("play",()=>document.querySelectorAll("audio").forEach(b=>{if(b!==a)b.pause();})));</script></body></html>'
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(result,encoding='utf8')
    print(f'Created {args.out} ({len(players)} playable tracks, {args.out.stat().st_size} bytes)')

if __name__=='__main__':main()