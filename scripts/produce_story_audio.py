#!/usr/bin/env python3
"""Prepare/execute Qwen3 Base speech *per scene* for a vetted Bharat Mode story.

No API requests, subscriptions, credit services, or owner PC setup.
The --execute switch requires official local Qwen3 Base model weights and enough
permitted Work Mode RAM; default dry run never loads Qwen or creates narration.
Do not mistake Qwen output validation for a human pronunciation/ASR review.
"""
from __future__ import annotations
import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STORY = ROOT/'stories/lt-chennai-ai-cluster-order.json'
REVISION='fd4b254389122332181a7c3db7f27e918eec64e3'

def work_plan(story_path:Path, output:Path, reference:Path, model:Path, seed:int, max_new_tokens:int):
    obj=json.loads(story_path.read_text('utf-8'))['story']
    if not obj.get('contentId') or not obj.get('scenes'):
        raise ValueError('Story must carry permanent contentId and nonempty scenes')
    if obj.get('hasVoice'):
        raise ValueError('Production source already claims completed voice; recheck before overwriting')
    if len(obj['scenes'])>12:raise ValueError('Unusually high scene count; inspect production scope')
    out=[]
    for index,scene in enumerate(obj['scenes']):
        text=scene.get('narration','').strip()
        if len(text)<12:raise ValueError(f'Empty/short narration in scene {index}')
        stem=f'{index:02d}'
        wav=output/(stem+'.wav')
        meta=wav.with_suffix('.json')
        command=[sys.executable,str(ROOT/'scripts/qwen_base_voice_test.py'),
                 '--reference',str(reference),'--model',str(model),
                 '--model-revision',REVISION,'--device','cpu','--staged-cpu',
                 '--seed',str(seed+index),'--max-new-tokens',str(max_new_tokens),
                 '--text',text,'--output',str(wav)]
        verify=[sys.executable,str(ROOT/'scripts/validate_qwen_base_output.py'),
                '--audio',str(wav),'--manifest',str(meta),
                '--reference-manifest',str(ROOT/'config/narrator-reference.json')]
        align=[sys.executable,str(ROOT/'scripts/align_qwen_words.py'),
               '--audio',str(wav),'--text',text,
               '--output',str(output/(stem+'-alignment.json')),'--device','cpu']
        out.append({'scene':index,'narration':text,'plannedDurationSeconds':scene['duration'],
                    'wav':str(wav),'command':command,'validate':verify,'align':align})
    return {'contentId':obj['contentId'],'slug':obj['slug'],'musicId':obj.get('musicId'),
            'sourceStory':str(story_path),'officialBaseRevision':REVISION,
            'note':'Nominal scene durations are placeholders until real WAV + word alignment.',
            'steps':out}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--story',type=Path,default=DEFAULT_STORY)
    p.add_argument('--output',type=Path,default=ROOT/'out/voice/BM-0003')
    p.add_argument('--reference',type=Path,default=ROOT/'out/private/bharat-mode-qwen-voice-audition.wav')
    p.add_argument('--model',type=Path,default=Path('/absolute/path/to/offline/qwen-base-model'))
    p.add_argument('--seed',type=int,default=42)
    p.add_argument('--max-new-tokens',type=int,default=240)
    p.add_argument('--execute',action='store_true',help='Run OFFLINE Qwen3 Base only on capable permitted compute')
    p.add_argument('--align',action='store_true',help='Attempt REAL WhisperX acoustic alignment after each successful Base synthesis')
    args=p.parse_args()
    plan=work_plan(args.story,args.output,args.reference,args.model,args.seed,args.max_new_tokens)
    if not args.execute:
        print(json.dumps({'mode':'DRY_RUN_NO_AUDIO_GENERATED',**plan},indent=2))
        return
    if not args.reference.is_file() or not args.model.is_dir():
        p.error('--execute requires the private verified voice reference and official downloaded model weights')
    # Before spending CPU cycles, check the original private WAV checksum.
    subprocess.run([sys.executable,str(ROOT/'scripts/qwen_reference.py'),
                    '--audio',str(args.reference)],check=True)
    args.output.mkdir(parents=True,exist_ok=True)
    for item in plan['steps']:
        print('Generating verified scene',item['scene'],flush=True)
        subprocess.run(item['command'],check=True,cwd=ROOT)
        subprocess.run(item['validate'],check=True,cwd=ROOT)
        if args.align:
            subprocess.run(item['align'],check=True,cwd=ROOT)
    (args.output/'production-plan.json').write_text(json.dumps({
        'story':plan['contentId'],'status':'audio_generated_not_human_approved',
        'steps':[{'scene':x['scene'],'wav':x['wav'],'text':x['narration']} for x in plan['steps']],
        'pending':['independent ASR comparison','proper-name listening','human narration approval','V6 integration']
    },indent=2)+'\n','utf-8')
    print('Audio validation completed; do NOT mark approved or set hasVoice until listening and alignment QA')

if __name__=='__main__':main()