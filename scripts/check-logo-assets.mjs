/**
 * Protect owner-approved SVG artwork from accidental redesign/replacement.
 * Update these hashes only when the owner explicitly approves a new master.
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const approved = {
  'public/brand/bharat-mode-badge.svg': '03ec4a83ed34255427724c1b3f77dbe7654d5f31f99e081d570d446d8d5707b5',
  'public/brand/bharat-mode-avatar.svg': '0a608f57cb93033a36bce5bd2a7a45bc15bfc3dd26d58478fbf7134d981f818a'
};
for (const [path, expected] of Object.entries(approved)) {
  const file=fs.readFileSync(path);
  const actual=crypto.createHash('sha256').update(file).digest('hex');
  assert.equal(actual,expected,`Owner-approved logo modified: ${path}`);
  const text=file.toString('utf8');
  assert.ok(text.startsWith('<svg') && text.includes('</svg>'),`Invalid SVG: ${path}`);
  assert.ok(!/<script|<image|foreignObject|<text\b|onload=|\bhref=/i.test(text),`Unexpected external or active SVG content: ${path}`);
  console.log(`Approved logo verified: ${path}`);
}
console.log('Bharat Mode final SVG badge and avatar verified.');
