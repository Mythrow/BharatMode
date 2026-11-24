#!/usr/bin/env python3
"""Read-only Bharat Mode editorial calendar. No date or publication assumptions."""
import argparse, json, html, calendar
from pathlib import Path
from datetime import date, datetime
from zoneinfo import ZoneInfo

REPO = 'https://github.com/Mythrow/BharatMode/blob/main/'
def read(p): return json.loads(p.read_text(encoding='utf-8'))
def load(root):
    registry=read(root/'content/registry.json'); queue=read(root/'publishing/queue.json')['slugs']
    reports={}
    for path in (root/'publishing').glob('BM-*-release-page.json'):
        p=read(path); reports[p['id']]=p.get('publication',{})
    rows=[]
    for x in registry['items']:
        pub=reports.get(x.get('productionCode'),reports.get(x.get('legacyId'),reports.get(x['id'],{}))); published=x['stage']=='published'; reported=(pub.get('ownerConfirmedPublic') is True or x.get('ownerConfirmedPublic') is True) and not published
        # Schedule only when a real explicit date exists in registry or release metadata.
        scheduled=None if published or reported else x.get('scheduledAt') or pub.get('scheduledAt')
        status='published' if published else 'reported' if reported else 'active' if x['stage']=='in_progress' else 'idea'
        rows.append({**{k:x.get(k) for k in ('id','productionCode','slug','title','stage','priority','category','eventDate','discoveredAt','researchPath','storyPath','youtubeUrl','publishedAt')},'status':status,'reportDate':(pub.get('reportedOn') or x.get('publicationReportedOn')) if reported else None,'scheduledAt':scheduled,'queuePosition':queue.index(x['slug'])+1 if x['slug'] in queue and not (published or reported) else None})
    return rows

def daypart(s):
    if not s: return None
    try: return date.fromisoformat(s[:10]).isoformat()
    except (TypeError, ValueError): return None

def make_page(rows, asof):
    counts={k:sum(r['status']==k for r in rows) for k in ('published','reported','active','idea')}
    esc=lambda s:html.escape(str(s or '—'),quote=True)
    event_map={}
    for r in rows:
        for kind,key in [('published','publishedAt'),('reported','reportDate'),('scheduled','scheduledAt')]:
            if kind in ('published','reported') and r['status']!=kind: continue
            d=daypart(r[key]);
            if d: event_map.setdefault(d,[]).append({'kind':kind,'id':r.get('productionCode') or r['id']})
    labels={'published':'Published','reported':'Published · URL/date pending','active':'In progress','idea':'Idea'}
    cards=[]
    for section, title, desc, statuses in [('past','Publication history','Completed videos, including owner-confirmed publication awaiting reconciliation.',('published','reported')),('current','Current production','Selected stories being developed. Queue position does not establish a deadline.',('active',)),('future','Future stories','Candidates for editorial selection; no automatic publication.',('idea',))]:
        selected=[r for r in rows if r['status'] in statuses]; selected.sort(key=lambda r:(r['queuePosition'] is None,r['queuePosition'] or 999,r['id']))
        cards.append(f'<section id="{section}"><h2>{title} <small>{len(selected)}</small></h2><p class="muted">{desc}</p>')
        if not selected: cards.append('<p class="empty">No stories in this stage.</p>')
        for r in selected:
            pubtext= ('Publication date: '+str(r['publishedAt'])) if r['status']=='published' else ('Owner report: '+str(r['reportDate'])+' · actual upload date and link pending') if r['status']=='reported' else ('Scheduled: '+str(r['scheduledAt']) if r['scheduledAt'] else 'Release date: Not set')
            q=f" · Queue #{r['queuePosition']}" if r['queuePosition'] else (' · Not queued' if r['status']=='idea' else '')
            links=f'<a href="{REPO}{esc(r["researchPath"])}">Research</a>' if r['researchPath'] else ''
            if r['storyPath']: links+=f' <a href="{REPO}{esc(r["storyPath"])}">Storyboard</a>'
            if r['status']=='published' and r['youtubeUrl']: links+=f' <a href="{esc(r["youtubeUrl"])}">Watch Short</a>'
            cards.append(f'<article class="story {r["status"]}"><div class="storyhead"><span class="id">{esc(r["id"])}{(" / "+esc(r["productionCode"])) if r.get("productionCode") else ""}</span><span class="status">{labels[r["status"]]}</span></div><h3>{esc(r["title"])}</h3><p class="muted">{esc(r["category"])} · {esc(r["priority"])} priority{esc(q) if q else ""}</p><p>{esc(pubtext)}</p><p class="muted">News event: {esc(r["eventDate"])} · Registered: {esc(r["discoveredAt"])}</p><div class="links">{links}</div></article>')
        cards.append('</section>')
    metrics=''.join(f'<div><strong>{n}</strong><span>{label}</span></div>' for n,label in [(counts['published']+counts['reported'],'Published / reported'),(counts['active'],'In production'),(counts['idea'],'Ideas'),(sum(bool(r['scheduledAt']) for r in rows),'Scheduled')])
    # Embed only non-sensitive calendar data. Escape script termination.
    events=json.dumps(event_map,ensure_ascii=False).replace('<','\\u003c')
    return TEMPLATE.replace('@@DATE@@',esc(asof)).replace('@@METRICS@@',metrics).replace('@@STORIES@@',''.join(cards)).replace('@@EVENTS@@',events).replace('@@ASOF@@',json.dumps(asof)).replace('@@PENDING@@',str(counts['reported']))

TEMPLATE='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bharat Mode | Editorial calendar</title><style>
:root{color-scheme:light;--ivory:#fff7eb;--navy:#283039;--teal:#117a7a;--orange:#e8752e;--line:#e5d9c9}*{box-sizing:border-box}body{margin:0;background:var(--ivory);color:var(--navy);font:15px/1.5 system-ui,Segoe UI,sans-serif}main{max-width:1220px;margin:auto;padding:32px 26px 48px}header{display:flex;justify-content:space-between;align-items:end;gap:20px;border-bottom:2px solid var(--orange);padding:0 0 22px}header p{margin:0;font-size:12px;letter-spacing:.16em;font-weight:750;color:var(--teal)}h1{font-size:clamp(27px,4vw,44px);margin:5px 0 0;line-height:1.12}h2{font-size:20px;margin:0}h3{font-size:16px;line-height:1.35;margin:12px 0 8px}h2 small{font-size:13px;color:#686762;margin-left:5px}.muted{color:#66665f;font-size:13px;margin:7px 0}.stamp{font-size:13px;text-align:right;color:#66665f}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:22px 0}.metrics div{border:1px solid var(--line);background:#fffdf8;border-radius:12px;padding:14px 18px}.metrics strong{display:block;font-size:30px;color:var(--navy)}.metrics span{font-size:13px;color:#62635f}.panel{border:1px solid var(--line);border-radius:14px;padding:18px;background:#fffdf8}.calhead{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:14px}.calhead button{padding:8px 12px;border:1px solid var(--line);background:white;border-radius:8px;cursor:pointer;color:var(--navy);font:inherit}.calhead button:focus-visible,a:focus-visible{outline:2px solid var(--teal)}.week,.days{display:grid;grid-template-columns:repeat(7,minmax(0,1fr))}.week span{font-size:12px;color:#676b66;padding:8px;text-align:center;font-weight:700}.days>div{min-height:88px;border-top:1px solid var(--line);border-right:1px solid var(--line);padding:7px;overflow-wrap:anywhere}.days>div:nth-child(7n){border-right:0}.days .outside{background:#f6f0e6;color:#9c9487}.days .today{outline:2px solid var(--orange);outline-offset:-2px;background:#fff2df}.event{display:block;font-size:11px;border-radius:4px;padding:3px 5px;margin:4px 0;line-height:1.3;background:#e7f2eb;color:#24573c}.event.reported{background:#f7ead5;color:#825617}.event.scheduled{background:#e1e9f7;color:#314d76}.legend{display:flex;flex-wrap:wrap;gap:12px;margin:12px 0 0;font-size:12px;color:#62635f}.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;background:#5d9770;margin-right:5px}.legend .rep{background:#d6a75b}.legend .sch{background:#6f91c1}.board{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:26px}.story{background:#fffdf8;border:1px solid var(--line);border-left:4px solid #9b9a92;padding:15px;border-radius:10px;margin-top:12px}.story.active{border-left-color:var(--orange)}.story.reported,.story.published{border-left-color:var(--teal)}.storyhead{display:flex;justify-content:space-between;gap:9px;flex-wrap:wrap;font-size:12px}.id{font-weight:800;letter-spacing:.05em}.status{color:#62635f}.story p{margin:7px 0;font-size:13px}.links{display:flex;gap:12px;flex-wrap:wrap;margin-top:13px}a{color:var(--teal);font-size:13px;font-weight:650}.empty{color:#676b66}footer{border-top:1px solid var(--line);margin-top:24px;padding-top:16px;font-size:13px;color:#676b66}@media(max-width:760px){main{padding:20px 12px}header{align-items:start;flex-direction:column}.stamp{text-align:left}.metrics{grid-template-columns:repeat(2,1fr)}.board{grid-template-columns:1fr}.panel{padding:10px}.days>div{min-height:64px;padding:3px}.event{font-size:10px;padding:2px}.calhead button{padding:5px 8px}}@media print{button{display:none}main{padding:0}.story{break-inside:avoid}.days>div{min-height:50px}}
</style></head><body><main><header><div><p>BHARAT MODE / EDITORIAL OPERATIONS</p><h1>Content calendar</h1></div><div class="stamp">Snapshot: @@DATE@@ · IST<br>Read-only · GitHub-backed</div></header><div class="metrics">@@METRICS@@</div><div class="panel"><div class="calhead"><button type="button" id="prev" aria-label="Previous month">←</button><h2 id="month"></h2><div><button type="button" id="today">Today</button> <button type="button" id="next" aria-label="Next month">→</button></div></div><div class="week"><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span></div><div class="days" id="days"></div><div class="legend"><span><i></i>Actual publication date</span><span><i class="rep"></i>Owner publication report (not verified upload date)</span><span><i class="sch"></i>Explicitly scheduled</span></div><p class="muted">Only real publication dates, dated owner reports and explicitly scheduled releases appear in the calendar. News event dates and queue positions are not upload dates.</p><noscript><p>Enable JavaScript for month navigation. All story statuses are available below.</p></noscript></div><div class="board">@@STORIES@@</div><footer>@@PENDING@@ owner-reported publication(s) still require actual YouTube URL/date for formal registry promotion. No release dates have been inferred. <a href="https://github.com/Mythrow/BharatMode/blob/main/content/registry.json">Canonical registry</a> · <a href="https://github.com/Mythrow/BharatMode/blob/main/publishing/queue.json">Editorial queue</a></footer></main><script>
const events=@@EVENTS@@;const asof=@@ASOF@@;let [year,month]=asof.split('-').map(Number);month--;const z=n=>String(n).padStart(2,'0');const monthName=new Intl.DateTimeFormat('en-IN',{month:'long',year:'numeric',timeZone:'UTC'});function render(){document.getElementById('month').textContent=monthName.format(new Date(Date.UTC(year,month,1)));const grid=document.getElementById('days');grid.replaceChildren();const first=new Date(Date.UTC(year,month,1)),offset=(first.getUTCDay()+6)%7;const length=new Date(Date.UTC(year,month+1,0)).getUTCDate();for(let i=0;i<Math.ceil((offset+length)/7)*7;i++){const d=new Date(Date.UTC(year,month,1-offset+i)),key=d.getUTCFullYear()+'-'+z(d.getUTCMonth()+1)+'-'+z(d.getUTCDate());const el=document.createElement('div');if(d.getUTCMonth()!==month)el.classList.add('outside');if(key===asof)el.classList.add('today');el.append(String(d.getUTCDate()));for(const e of events[key]||[]){let tag=document.createElement('span');tag.className='event '+e.kind;tag.textContent=e.id+' · '+({published:'Published',reported:'Reported published',scheduled:'Scheduled'}[e.kind]);el.append(tag);}grid.append(el)}}function move(n){const d=new Date(Date.UTC(year,month+n,1));year=d.getUTCFullYear();month=d.getUTCMonth();render()}document.getElementById('prev').onclick=()=>move(-1);document.getElementById('next').onclick=()=>move(1);document.getElementById('today').onclick=()=>{[year,month]=asof.split('-').map(Number);month--;render()};render();
</script></body></html>'''

def main():
    p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path('.'));p.add_argument('--as-of',default=datetime.now(ZoneInfo('Asia/Kolkata')).date().isoformat());p.add_argument('--output',type=Path,required=True);a=p.parse_args();date.fromisoformat(a.as_of);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(make_page(load(a.repo),a.as_of),encoding='utf-8')
if __name__=='__main__':main()