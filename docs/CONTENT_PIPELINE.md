# Bharat Mode — Permanent Content Registry & Editorial Workflow

> **MANDATORY — Constructive Motion Design (owner approved 25 November 2026):** Animate the formation of meaningful relationships, not merely the movement of finished graphics. When appropriate for the story: (1) timeline/route/path starts at an anchor, types its label/supporting text, draws progressively with a travelling endpoint, settles at destination, then types destination information; (2) connected systems establish the connector/foundation first, then attach components sequentially in a meaningful order; (3) associate typewriter labels with the relevant graphical arrival/assembly and narrated fact, not arbitrary simultaneous reveals; (4) inspect actual intermediate decoded frames during path drawing, docking, label reveals and transitions for collisions, clipping, premature reveals and incorrect sequencing, then inspect settled states. Preserve contextual scene variety, rounded geometry, independent editable layers, subtle lighting, existing V6 branding and +64px caption/progress positions. Do not force timelines or T-shaped diagrams into unrelated stories; use story-appropriate geometry. Inter fallback and simplified dissolve are implementation limitations, not new brand rules.


> **MANDATORY — independent graphic and text motion; owner correction 24 November 2026:** Never flatten the main artwork, labels and statistics into one animated rectangle or move a complete static hero as a substitute for motion design. Build meaningful separate layers: every story text element (headline, kicker, value, callout, label, supporting text) has its own eased entrance/reveal; fixed brand avatar/topic pill are intentional chrome exceptions. Chart bars/lines grow progressively, numeric quantities count toward verified end values, modules/tiles assemble or stagger in, paths draw/connect sequentially and nodes appear with appropriate timing. Continue subtle contextual motion with travelling light pulses, illuminated LEDs, circuit traces or other relevant effects after reveal; avoid flashing, unnecessary ornament or obscuring text. Keep distinct contextual backgrounds, 60fps motion, V6 captions and quiet transitions. Before owner review inspect native decoded frames during reveal, after reveal and near transitions for each scene, including full glyph bounds, artwork/text clipping, safe margins, actual within-hero movement (not merely background or progress bars) and settled end values. Fix clipping at source; do not mask over pixels or defer a known visible defect to the next review.

> **MANDATORY — distinct scene backgrounds, owner correction 24 November 2026:** Each narrative scene must have a visibly different story-specific background composition and contextual motion, not a common decorative base with a changed color, gradient, glow or repeated curve. Theme colors may repeat; the artwork, geometry, depth and movement must change to support the content. A continued beat inside the same scene may retain its environment for continuity. V6 locks the branding/chrome (logo, topic pill, typography, captions and centered chapter progress), not background artwork. Before storyboard delivery, assign a unique scene-level background design ID and show actual native-resolution frames; audit the contact sheet for repeated geometry, not just palette, and verify distinct scene background layers in editable source. Before draft delivery, inspect representative rendered frames and within-scene background motion at native 60fps. If this gate fails, correct the source and regenerate before review. Do not reintroduce the prototype V6 radial glow + ellipse as a universal background. Do not include editorial reference labels.

> **MANDATORY on-screen text rule — owner instruction, 24 November 2026:** Do not add source/reference/editorial meta labels in video frames, storyboards, title cards or hero graphics. Remove phrases such as “Illustrative server architecture,” “Government-reported snapshot,” “Mission-wide figures,” “Source: ...,” report citations, internal evidence labels and production notes. Keep references, provenance, explanatory context and asset-rights notes in the research record and YouTube description. Preserve material factual qualifiers directly in normal story content (e.g. date of measured data, ordered versus deployed, under manufacture, National Supercomputing Mission versus PARAM Rudra) whenever omitting them would mislead. Use clearly schematic artwork rather than simulated real facility footage; where an illustration or synthetic media disclosure is necessary to avoid misleading the audience, use appropriate disclosure, not a generic on-screen reference line. Apply this during storyboard generation and visual QA before rendering. No change to approved V6 chrome, captions or progress bars.

> **MANDATORY storyboard review format — owner instruction, 24 November 2026:** Stage 03 means actual rendered native 1080×1920 still compositions from the proposed production visual source, not prose, text-only tables, generic imagery or approximate mood boards. Show a chronological filmstrip/contact sheet of full frames approximately every five seconds, plus any materially different visual state or scene otherwise missed; label time/scene outside the image. Provide a clickable expandable frame viewer with horizontal thumbnails and previous/next navigation (in-chat when supported, self-contained HTML and direct full-resolution PNG links as fallback). Show actual headline, hero, theme, artwork, labels, logo, caption backing/current-word treatment and progress; mark provisional word timing and any font/asset fallbacks. Retain editable frame/scene sources for the subsequent video and revise those compositions based on owner feedback. Only after storyboard approval animate the same visual layers, add V6 transitions, real acoustic alignment/captions and approved audio, and produce a draft MP4. Do not substitute a written plan for this gate or claim a final video has already been rendered. No spoken Bharat Mode closing for BM-001; visual branding remains.

> **LATEST — dual numbering, owner decision 24 Nov 2026:** All ideas receive a permanent sequential `ID-###` first. Assign a separate `BM-###` production code only on owner selection, using the lowest unused positive number; never recycle an assigned number. Keep a single registry record with both codes, use idea ID for research and production code for new video deliverables. ID-001 / BM-001 PARAM Rudra is selected, at Stage 01 story review. ID-002 ICMR and ID-004 IIT Madras are unselected ideas. ID-003 / BM-003 L&T is owner-confirmed published, URL/date pending; preserve historical BM-0003 files and references without re-rendering. BM-002 is next, then skip BM-003 to BM-004; ID-005 is next idea. Earlier BM-#### identifiers below are legacy references, not new allocations. The story → script → visual storyboard → draft render approval order remains mandatory. `content/registry.json` schema v2 is authoritative; `id` is idea identity, `productionCode` is null until selected, and `legacyId` is read-only historical alias. Use `npm run content:move -- ID-005 in_progress --note "Owner selected story"` for a real selected ID; the allocator assigns its code automatically. No automatic publication.


## Mandatory owner review sequence — 24 November 2026

For every new Short, including existing queued candidates, follow this exact order in the main production chat:

1. **Actual news/story content first.** Present the original development in plain language, event and source dates, primary-source links, verified facts and figures, why it matters, and material caveats. Distinguish announced, ordered, under development, deployed and completed. Do not start with narration or a visual concept. Obtain owner story approval before proceeding.
2. **Narration script second.** Present the complete proposed spoken script, broken into scenes, with estimated duration and factual qualifiers. Obtain owner script approval before advancing.
3. **Visual storyboard third.** Present an actual visual scene-by-scene preview (in-chat HTML/visual panels preferred), showing intended 9:16 composition, theme, on-screen title, hero graphics, motion and transitions, corresponding narration and approximate timing. Text-only planning is not a substitute for a visual preview when supported. Use approved V6 and 24px centered captions. Obtain owner storyboard approval before generating production narration or rendering.
4. **Draft render fourth.** Only after these approvals, use Work Mode for approved free Qwen3-TTS narration and real word alignment, then render the actual reviewable MP4 in the main chat with approved music, native 1080×1920 at 60fps, fresh aligned captions and quality checks. Deliver direct MP4 access and identify it as a draft. Revise based on owner feedback; do not publish.

After draft approval, complete final QA, thumbnail and publishing dashboard, then obtain explicit publication authorization. Record the actual publication URL/date and refresh the content calendar. Record review gates and revisions in existing story research/production notes under the permanent BM ID; do not create a duplicate registry or infer approvals. Do not combine or skip the four owner-facing stages unless the owner explicitly requests it for that episode. Previously published episodes are not reopened. Native-renderer implementation may be developed internally but must not replace the story-first owner-facing sequence. Existing approved branding, V6, audio-only Work boundary, no-new-paid-compute/voice policy, and post-launch QA requirements remain unchanged.


> **Owner update — 24 November 2026:** Caption backing corner radius is **24px** (supersedes 32px); all no-shadow/no-blur, native resolution and direct-alignment requirements remain. The owner requests a refreshed HTML content calendar whenever asked; see [CONTENT_CALENDAR.md](CONTENT_CALENDAR.md). Calendar reflects real publication history, current production, future ideas and explicit schedules only. BM-0003 appears as owner-confirmed published with URL/date pending; no fictitious release dates.


**Owner decision:** 23 November 2026. All topics considered for a Short are tracked **once**, by a permanent `BM-####` ID, across **Idea → In Progress → Published**. This repository is the single source of truth; a research document belongs to each ID.

## Start here

- **Human-readable live log:** [`content/CONTENT_LOG.md`](../content/CONTENT_LOG.md) — automatically rendered tables by stage, with research and story-draft links.
- **Canonical machine-readable ledger:** [`content/registry.json`](../content/registry.json) — permanent IDs, unique source/event keys, stage history, story links and publication metadata. **Do not maintain a second list of IDs elsewhere.**
- **Research for every idea:** [`content/research/BM-####.md`](../content/research/) — original sources, timestamp, why the story matters, claim ledger, caveats, graphics/rights, production checklist and publication history.
- **Script and storyboard:** `stories/<slug>.json` when drafted, with `story.contentId` matching the canonical ID.
- **Daily discovery notes:** `research/daily/YYYY-MM-DD.md` — the scan, rejected leads and rationale. Daily logs are *not* a second content register. Every selected/retained candidate must link to its ID.
- **Publishing queue:** `publishing/queue.json` remains a **sequence of storyboard-ready slugs** for creative-variety review; no ID is created by queue insertion, and this is **not** publication history.

## Status rules

| Stage | Meaning | Minimum evidence | Exit |
|---|---|---|---|
| **Idea** | A sourced, distinct candidate worth considering; no active production commitment | Permanent ID, unique event key, event/source date, primary URL, research sheet | Owner or editor chooses it for a script/video. Move to **In Progress** and log the reason. |
| **In Progress** | Selected for a pilot, script, research, voice, visual development or review; may still need further verification | Research sheet with facts and qualifiers; active production is not an upload approval | Only after **actual upload**, full fact/rights/phone QA, owner approval, YouTube video URL and publication date, move to **Published**. |
| **Published** | A real public YouTube video exists | Real YouTube watch or Shorts link, date, owner publication sign-off | Terminal. Never delete or recycle the ID; later updates become new cross-linked entries. |

There is no automatic publishing. A draft script is not evidence of publication. An uploaded but unpublished/scheduled video should remain **In Progress** until genuinely public. Once a content ID exists, it is **never reused** even if the idea is shelved; keep the record in Idea with a stage note, or add a future `shelved` flag rather than deleting it.

## Daily discovery → dedupe → selection

1. Research genuine new developments and separately record the **event date**, source publication date, as-of date for every statistic, and original primary source URL. A newly resurfaced older article does **not** become a new event.
2. **Before proposing or registering a candidate**, read the whole registry — including **Published** — and search by organization, product, project, aliases, date, release URL and title. Example: `npm run content:find -- "Chennai AI"` or `node scripts/content-registry.mjs find "Vyoma"`.
3. Every content/event uses a unique `storyKey`, e.g. `lt-chennai-ai-b300-additional-order-2026-11-23`. The `topicKey` tracks ongoing coverage of the same broader subject, e.g. `lt-chennai-ai-infrastructure`.
4. If the **same event/announcement** is already represented in any stage, **update that ID's research**, never create another. The validator rejects duplicate IDs, slugs, story keys and primary URLs, and flags near-identical titles.
5. If there is a **genuinely distinct development** in an already-covered topic (e.g. a deployed system a year after an announced order), register a **new** storyKey and original event source, record `relatedIds` referencing prior content and provide a human-readable `distinguishingUpdate`. Otherwise the validator rejects the second record.
6. Preserve other considered candidates in the daily research log even when rejected. Add them to the permanent registry **only if they are credible, meaningfully distinct and genuinely plausible future Shorts** — not every headline in search results.
7. Select the best candidate for work, move it **Idea → In Progress** with a reason and work on its story doc. A user asking to “try this story” is authorization to *develop a pilot*, **not** to publish.

**Important limitation:** automatic source/event/word matching catches exact and likely overlaps but cannot establish universal semantic identity. An editorial comparison remains necessary for paraphrased news, evolving projects and multi-event press releases. The permanent ID and related-event cross-links make missed repetitions visible and auditable.

## Agent-friendly commands (maintainer runs; channel owner is NOT required to install software)

### Check the entire registry before starting
```bash
npm run content:check
npm run content:list
npm run content:find -- "NVIDIA B300"
```

### Create a genuinely new idea
```bash
npm run content:add -- \
  --title "A newly verified discovery" \
  --slug "example-discovery" \
  --story-key "example-lab-2026-11-24-breakthrough" \
  --topic-key "example-lab-project" \
  --primary-source "https://example.org/press-release" \
  --source-date 2026-11-24 \
  --event-date 2026-11-24 \
  --category science \
  --priority medium \
  --aliases "Example Lab,Discovery Name" \
  --note "Why this is meaningfully new"
```
This transaction allocates the next permanent ID, creates a research template and refreshes `CONTENT_LOG.md`. An invalid or duplicate candidate is rejected **before** it reserves an ID. For a distinct later follow-up on an existing topic, add `--related BM-0003 --distinguishing-update "The new 2027 deployment outcome, not the 2026 contract announcement"`.

### Advance a selected story (e.g. after editorial selection)
```bash
npm run content:move -- BM-0004 in_progress --note "Owner chose this for the next script"
```

### Record an actually published video (never for previews)
```bash
npm run content:move -- BM-0003 published \
  --published-at 2026-12-01 \
  --youtube-url "https://www.youtube.com/shorts/ACTUAL_VIDEO_ID" \
  --approved-by-owner \
  --note "Actual public upload confirmed; script, audio, imagery, sources and phone QA approved"
```
The video ID shown is a **placeholder**, not an existing link. `Published` requires an actual 11-character YouTube ID, and the CLI refuses direct `Idea → Published`, missing owner approval, missing publication date or missing URL. Human approval must be real; a CLI flag alone cannot prove it. On publication it removes the story slug from the legacy creative-order queue, but retains the registry record.

### Refresh / verify after manual research edits
```bash
npm run content:sync
npm run content:check
npm run content:test
```
`content:sync` regenerates the dashboard from the JSON ledger. Never hand-edit the generated Markdown table: it will fail the check. The CI workflow invokes `content:check` and the test suite; **the repository's GitHub Actions runners have previously failed before starting steps**, so run outcomes must be inspected rather than assumed green.

## IDs allocated in the initial migration

| ID | Stage | Content |
|---|---|---|
| `BM-0001` | In Progress | PARAM Rudra / supercomputing — existing V6/voice pilot |
| `BM-0002` | Idea | ICMR 100 cumulative technology transfers — draft storyboard exists, but not in active production |
| `BM-0003` | In Progress | **23 Nov 2026 L&T Chennai B300 additional order** — owner selected to try, **not** published |
| `BM-0004` | Idea | IIT Madras sleep and autism facilities — 22 Nov verified backup |

These IDs are permanent across the project's life. The first registered new daily story is **BM-0003**, not BM-0001 because two story drafts already predated the new log.

## Publication and future performance metrics

After YouTube publication, retain YouTube URL, actual publication date and owner approval in `registry.json`; subsequent analytics (views, retention, comments, subscribers) should use **the same ID** rather than creating a second analytics identity. A later materially distinct development gets a new ID, cross-linked to the old one.

## Independent creative safeguards

Continue the approved Qwen3-TTS synthetic narrator and V6 motion system. Changing the content registry **does not approve a video**, change the template, spend voice credits, or auto-upload to YouTube. Research rights and verified development stages remain mandatory.