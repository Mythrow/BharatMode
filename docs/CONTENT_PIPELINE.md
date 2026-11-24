# Bharat Mode — Permanent Content Registry & Editorial Workflow

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