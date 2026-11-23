/**
 * Derive V6 caption phrases exclusively from actual acoustic alignment output.
 * These pure functions never calculate/fabricate word timestamps. Model output
 * from an unrun aligner or estimated demo timings is NOT a valid input.
 */
export const V6_MAX_PHRASE_WORDS = 4;
export const V6_MAX_PHRASE_CHARS = 27;

export function validateAlignedWords(data) {
  if (data?.source !== 'final-audio-acoustic-alignment' || !Array.isArray(data.words)) {
    throw new Error('Real final-audio alignment is required; synthetic demo timings are not accepted');
  }
  if (data.qa?.exactWordMatch !== true || data.qa?.alignedWords !== data.words.length || !data.audio?.sha256) {
    throw new Error('Audio checksum and exact acoustic word match are required');
  }
  let previousEnd = -1;
  for (const [i, word] of data.words.entries()) {
    const {start, end, text} = word;
    if (!text || !Number.isFinite(start) || !Number.isFinite(end) || start < 0 || end <= start ||
        start + 0.025 < previousEnd || end > data.audio.durationSeconds + 0.025) {
      throw new Error(`Invalid acoustic word timing at ${i}`);
    }
    previousEnd = end;
  }
  return data.words;
}

export function groupAlignedWords(data, opts={}) {
  const words = validateAlignedWords(data);
  const maxWords = opts.maxWords ?? V6_MAX_PHRASE_WORDS;
  const maxChars = opts.maxChars ?? V6_MAX_PHRASE_CHARS;
  const maxPause = opts.maxPause ?? 0.36;
  if (!(maxWords >= 1 && maxChars >= 5)) throw new Error('Invalid phrase size');
  const groups = [];
  let current = [];
  const finish = () => {
    if (!current.length) return;
    const prev = current[current.length-1];
    groups.push({id:`g${groups.length}`,start:current[0].start,end:prev.end,words:current});
    current = [];
  };
  for (const word of words) {
    const nextLen = [...current,word].map(w=>w.text).join(' ').length;
    const pause = current.length ? word.start-current[current.length-1].end : 0;
    if (current.length && (current.length >= maxWords || nextLen > maxChars || pause > maxPause)) finish();
    current.push(word);
    // Prefer ending naturally at sentence punctuation and avoid joining clauses.
    if (/[.!?;:]$/.test(word.text)) finish();
  }
  finish();
  return groups;
}

export function visibleAlignedCaption(groups, second) {
  if (!Number.isFinite(second)) return null;
  const index = groups.findIndex((g,i)=>second >= g.start &&
    second < (groups[i+1]?.start ?? g.end + .30));
  if (index < 0) return null;
  const group = groups[index];
  const seen = group.words.filter(w => second >= w.start);
  const active = seen.length ? group.words.indexOf(seen[seen.length-1]) : -1;
  return {...group, visibleWords:seen.map(w=>({...w,isActive:group.words.indexOf(w)===active,
    ageSeconds:Math.max(0,second-w.start)}))};
}