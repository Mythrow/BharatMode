"""Offline checks for BM-0003 Qwen production-plan contract (no model inference)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from produce_story_audio import work_plan, REVISION


class ProductionPlanTests(unittest.TestCase):
    def setUp(self):
        self.story=ROOT/'stories/lt-chennai-ai-cluster-order.json'

    def test_six_scenes_bm0003(self):
        p=work_plan(self.story,Path('out/voice/BM-0003'),Path('out/private/verified.wav'),Path('/offline/qwen'),42,240)
        self.assertEqual(p['contentId'],'BM-0003')
        self.assertEqual(p['musicId'],'MUSIC-06')
        self.assertEqual(len(p['steps']),6)
        self.assertEqual(sum(x['plannedDurationSeconds'] for x in p['steps']),48)

    def test_exact_script_in_commands(self):
        p=work_plan(self.story,Path('out/x'),Path('ref.wav'),Path('/model'),42,240)
        for x in p['steps']:
            cmd=x['command']
            self.assertEqual(cmd[cmd.index('--text')+1],x['narration'])
            self.assertEqual(cmd[cmd.index('--model-revision')+1],REVISION)
            self.assertEqual(x['align'][x['align'].index('--text')+1],x['narration'])

    def test_offline_staged_cpu_only(self):
        p=work_plan(self.story,Path('out/x'),Path('ref.wav'),Path('/model'),42,240)
        for x in p['steps']:
            self.assertIn('--staged-cpu',x['command'])
            self.assertEqual(x['command'][x['command'].index('--device')+1],'cpu')
            self.assertFalse(any('api.openai.com' in t or 'elevenlabs.io' in t for t in x['command']))

    def test_reject_missing_permanent_content_id(self):
        src=json.loads(self.story.read_text())
        del src['story']['contentId']
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'story.json';file.write_text(json.dumps(src))
            with self.assertRaises(ValueError):work_plan(file,Path('out'),Path('ref.wav'),Path('/model'),42,240)

    def test_reject_pretending_voice_already_generated(self):
        src=json.loads(self.story.read_text());src['story']['hasVoice']=True
        with tempfile.TemporaryDirectory() as d:
            file=Path(d)/'story.json';file.write_text(json.dumps(src))
            with self.assertRaises(ValueError):work_plan(file,Path('out'),Path('ref.wav'),Path('/model'),42,240)

    def test_claim_caveats_present(self):
        s=json.loads(self.story.read_text())['story']
        self.assertFalse(s['hasVoice'])
        self.assertIn('planned',s['claimStage'])
        self.assertIn('not a confirmed count',s['scenes'][4]['narration'])
        self.assertIn('August',s['scenes'][3]['narration'])


if __name__=='__main__':unittest.main()