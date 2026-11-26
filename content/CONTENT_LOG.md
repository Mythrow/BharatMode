# Bharat Mode — Content Log

**Canonical register:** [`registry.json`](registry.json) · **Story research:** [`research/`](research/) · **Workflow:** [`docs/CONTENT_PIPELINE.md`](../docs/CONTENT_PIPELINE.md)

Updated: 2026-11-26 (IST) · Permanent IDs: 5 · **Never reassign or delete an ID.**

> This document is generated from `content/registry.json`. Use the registry command to add and move content; run `npm run content:check` before committing. An idea is not a published video.

## Idea (1)

| Idea ID | Production | Title | Event / as-of | Priority | Research | Story draft | Publication |
|---|---|---|---|---|---|---|---|
| **ID-004** | — | IIT Madras inaugurates sleep and autism research facilities | 2026-11-22 | medium | [Research](research/ID-004.md) | — | — |

## In Progress (4)

| Idea ID | Production | Title | Event / as-of | Priority | Research | Story draft | Publication |
|---|---|---|---|---|---|---|---|
| **ID-005** | BM-004 | GalaxEye orders Indian-built propulsion for 30 satellites from Bellatrix | 2026-11-24 | high | [Research](research/ID-005.md) | — | Scheduled 2026-11-27 (owner reported; time/link pending) |
| **ID-003** | BM-003 | L&T expands Chennai AI infrastructure with new B300 order | 2026-11-23 | high | [Research](research/ID-003.md) | [Draft](../stories/lt-chennai-ai-cluster-order.json) | Owner-confirmed published; URL/date pending |
| **ID-001** | BM-001 | PARAM Rudra: India’s supercomputing deployment | 2026-09 | high | [Research](research/ID-001.md) | [Draft](../stories/param-rudra.json) | Owner-confirmed published; URL/date pending |
| **ID-002** | BM-002 | ICMR reaches 100 technology-transfer agreements | 2026-11-17 | medium | [Research](research/ID-002.md) | [Draft](../stories/icmr-tech-transfer.json) | Owner-confirmed published; URL/date pending |

## Published (0)

_No content in this stage._

## Dedupe and stage rules

- Every candidate gets one **never-reused** `ID-###` idea identity and its own fact-checked research sheet. Assign the lowest unused `BM-###` only on selection; preserve both codes permanently.
- A primary event is identified by `storyKey`; source URLs, slug, ID, near-identical titles and the complete registry are checked for duplicates.
- A later distinct event in the **same topic** requires a new `storyKey`, links in `relatedIds`, and `distinguishingUpdate` explaining why it deserves another video.
- **Idea → In Progress → Published** is one-way. A published entry must include the actual YouTube video URL, date and explicit owner publication sign-off.
- The `publishing/queue.json` is an editorial planning order, **not a second content identity system**. It may not contain published or unregistered slugs.
- Automated checks catch exact/obvious overlap, not all semantic paraphrases. A human must check the research sheets and older coverage before approving a new event.

See [content workflow](../docs/CONTENT_PIPELINE.md) for usage.
