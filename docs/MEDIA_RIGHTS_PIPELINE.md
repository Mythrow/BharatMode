# Bharat Mode — Real Photography, Public Figures, Logos & Rights

**Status:** editorial policy draft and technical plan. Before implementing automated media ingestion, have an editor review and approve the rights policy. This is practical risk management, not legal advice.

## Principle
A programmatically rendered video can display **real photographs, company logos, archival images and genuine public-figure photos**. The editor needs valid rights/reuse basis and accurate context, **not a generated imitation**.

Using a photo found by Google Image Search, in a social post or as a news-site thumbnail does *not* grant permission. Linking to a source, giving credit, cropping or adding an animation does not by itself grant reuse rights.

## Preferred sourcing, in order
1. Photos and diagrams we produce, or directly license with **online-video / commercial reuse and, if applicable, repo redistribution** permitted.
2. File-specific CC0, CC BY or other appropriate Creative Commons/public-domain assets — verify the original file page, attribution and derivative/share-alike rules. Wikimedia Commons is a catalog, **not a blanket license**.
3. Press offices and official photo/media kits with explicit applicable terms. Government sites differ. **PIB says its own site materials may be reproduced without prior approval, but excludes third-party materials and requires accurate reproduction/context and prominent source credit.** Check individual photo ownership/conditions.
4. Licensed news agency / wire images with actual editorial-video license for the intended platforms and territories.
5. If rights cannot be established: use an **original diagram**, a verified data visual, or seek permission. Do not silently scrape a different picture.

Sources:
- PIB copyright policy: https://www.pib.gov.in/content/186_2_Copyright-Policy.aspx?lang=1&reg=5
- Wikimedia Commons reuse: https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia/licenses
- YouTube copyright: https://support.google.com/youtube/answer/2797466

## Public figures: e.g. the Prime Minister
- An authentic, properly reusable photo of the PM speaking at an event may be used **when that event is the subject**. Record photographer, publisher, date, original context, license and any required credit.
- Use exact photo captions such as `Archive photo, date...` or `Photo: PIB / photographer...` as appropriate.
- Don't show an unrelated photo in a way that implies the PM attended an event, announced a policy, endorses Bharat Mode, or said something not verifiably said.
- **No AI-generated photorealistic fake of a real public figure**, no face swap, and no cloned voice impersonation for fictional quotes. The YouTube AI disclosure rule applies to realistic generated/meaningfully altered media; seek editorial review of public-figure depictions.

YouTube AI disclosure: https://support.google.com/youtube/answer/14328491

## Companies and institutional logos
- Prefer an official asset/press kit. Some logos are trademarks and may also have copyright restrictions.
- Using a logo in truthful editorial identification is different from using it as channel branding, but use is contextual and case-specific. **Never imply sponsorship or formal endorsement**.
- Preserve logo proportions, clearspace and required colors; do not redraw as a confusing fake mark.
- For unclear terms, request permission or use the company's name in plain text instead of its protected graphic.
- Never put the company logo inside Bharat Mode's main wordmark or own avatar.

YouTube trademark overview: https://support.google.com/youtube/answer/6154218

## Asset metadata and render process
Each selected photo/logo should have a record in `media/manifest.json`:
```json
{
  "id": "research-event-photo-001",
  "type": "photo",
  "creator": "Photographer or institution",
  "sourceUrl": "https://original-publisher.example/page",
  "license": "Exact permission/license identifier",
  "licenseUrl": "https://license.example/terms",
  "attribution": "Photo: Author / Source; license link",
  "editorialContext": "What it actually depicts, with date",
  "rightsVerified": true,
  "reviewedBy": "Human reviewer",
  "reviewedOn": "YYYY-MM-DD",
  "repoRedistributionAllowed": false,
  "localPath": "public/media/research-event-photo-001.webp"
}
```
The example is **illustrative only** and must never enter the manifest with invented proof.

### Storage policy
- **YES in Git:** our original editable design SVGs, owned diagrams, sound/music masters, story descriptions, attribution/licensing records and media with **explicit redistribution rights**.
- **NO in public Git without permission:** third-party images, purchased editorial photos or company logo files when their licenses forbid public redistribution.
- If an image is cleared **for video use but not public Git redistribution**, store it in private approved asset storage or a local protected media cache; commit only manifest metadata and its acquisition instructions, never a copy.
- Generated voice and rendered video remain excluded as already agreed.

### Deterministic Remotion rendering
1. Research worker finds candidate assets but does not auto-approve them.
2. Rights reviewer verifies each file's license and contextual suitability.
3. Approved file is downloaded/cached at a stable named path, optimized, and checked against expected dimensions/hash.
4. Story references `assetId`, not a random image-search URL.
5. At render time, a local temporary `public/media` working folder is hydrated from cleared assets.
6. Render with `<Img src={staticFile('media/asset-name.webp')} />` inside a photo panel; do not hotlink third-party URLs in production.
7. Attribution goes on-screen where appropriate and in the YouTube description or credits as required by the actual license.
8. Missing rights, missing file, or misleading context **blocks publication**.

Example:
```jsx
import {Img, staticFile} from 'remotion';
export const RealPhoto = ({filename}) => (
  <Img src={staticFile('media/' + filename)}
    style={{width: '100%', height: '100%', objectFit: 'cover'}}
  />
);
```
This component only displays a file; the **asset approval/manifest validator** must prevent unreviewed filenames from being used.

Remotion official `Img` documentation: https://www.remotion.dev/docs/img

## Attribution, AI and truthfulness
- Keep source URL, photographer, license, original date and transformation log.
- Separate visual sourced facts from decorative illustrations with labels when needed.
- Contextual crop, slow pan and framing may be okay under a license, but don't create false implication via editing.
- If AI is used to generate a stylized generic representation, label `Illustration`; don't portray it as real footage.
- Relevant public figures are not inherently off limits; **accurate source and rights matter**.
- Before publishing: independent claim verification + editor license review + a mobile visual review.

## Future implementation milestone
Build `scripts/validate-media.mjs` (schema and file hash checks), licensed asset cache hydrator, safe image crop compositor and automatic credit export **after** the brand/logo typography pass is approved.
