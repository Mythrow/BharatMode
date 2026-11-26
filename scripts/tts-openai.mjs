/**
 * Historical paid TTS experiment; prohibited for routine Bharat Mode production. Uses a configurable speech model; verify
 * the provider's supported model IDs, pricing and usage terms at render time.
 * Generated voice files are not committed.
 */
import fs from 'node:fs';
import path from 'node:path';
throw new Error('Historical paid OpenAI TTS is disabled for Bharat Mode production. Use approved private Qwen3-TTS Base workflow. Any change requires explicit owner approval.');
// Retained implementation for historical reference only.
const input = process.argv[2] || 'stories/param-rudra.json';
const story = JSON.parse(fs.readFileSync(input,'utf8')).story;
const key=process.env.OPENAI_API_KEY;
if (!key) throw new Error('Set OPENAI_API_KEY in your environment (do not commit it).');
const model=process.env.OPENAI_TTS_MODEL || 'gpt-4o-mini-tts';
const voice=process.env.OPENAI_TTS_VOICE || 'marin';
const output=path.join('public','voice',story.slug);
fs.mkdirSync(output,{recursive:true});
for (let i=0;i<story.scenes.length;i++) {
  const scene=story.scenes[i];
  const response=await fetch('https://api.openai.com/v1/audio/speech',{
    method:'POST',
    headers:{Authorization:'Bearer '+key,'Content-Type':'application/json'},
    body:JSON.stringify({
      model,voice,response_format:'wav',input:scene.narration,
      instructions:'Calm, clear, conversational Indian-English science explainer. Optimistic but measured. Avoid sales pitch.'
    })
  });
  if (!response.ok) throw new Error('TTS scene '+i+' HTTP '+response.status+': '+await response.text());
  const bytes=Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(path.join(output,i+'.wav'),bytes);
  console.log('Generated voice scene '+i+' ('+bytes.length+' bytes) for target '+scene.duration+' seconds; manually check timing.');
}
console.log('Review timing and voice quality. Set story.hasVoice=true before render. Disclose synthetic narration.');
