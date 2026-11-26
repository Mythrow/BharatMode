# Bharat Mode

**Big Ideas. Real Progress.** Research-led, faceless YouTube Shorts about verified Indian achievements, inventions and measurable progress.

## Start here

| Information | Authoritative source |
|---|---|
| Next action and blockers | [Current project status](docs/PROJECT_STATUS.md) |
| Permanent content IDs and release stages | [Registry](content/registry.json); generated [content log](content/CONTENT_LOG.md) |
| Editorial approval and dedupe workflow | [Content pipeline](docs/CONTENT_PIPELINE.md) |
| Brand and approved visual rules | [Brand](docs/BRAND.md), [approved template](docs/APPROVED_SHORTS_TEMPLATE.md) |
| Production and private asset recovery | [Production guide](docs/PRODUCTION.md), [recovery standard](docs/PRODUCTION_REPRODUCIBILITY.md) |
| Audio configuration | [Voice](config/voice.json), [narrator reference](config/narrator-reference.json), [music](config/music.json) |
| Publishing fields and release-specific QA | [Publishing](docs/PUBLISHING_PAGE.md), per-release JSON in [publishing/](publishing/) |
| Calendar and analytics | [Calendar](docs/CONTENT_CALENDAR.md), [analytics](docs/ANALYTICS_TRACKING.md) |
| Engineering backlog | [Roadmap](docs/ROADMAP.md) |
| Historical decisions and visual studies | [Archive index](docs/archive/README.md) |

Agents must read [AGENTS.md](AGENTS.md). No automatic publication.

## Maintenance

Node 22 and Python 3.12 recommended. Run `npm run content:check`, `npm run content:test`, `npm run validate` and the complete `npm run check` suite (see validation workflow). Remotion dependencies are needed for video work, not the dependency-free ledger checks. Historical motion studies and sample render commands are previews only, not release output. Do not regenerate existing Shorts.

## Layout

- `content/` permanent registry, generated log and research evidence; `stories/` structured story briefs.
- `src/` editable renderer and visual studies; `scripts/` validators and generation/QA utilities.
- `public/brand/` protected approved SVGs and banner; `public/music/` and `public/sfx/` historical original demo assets, not the approved soundtrack.
- `config/` approved audio settings; `publishing/` release records; `analytics/` dated snapshots.
- `previews/html/` historical browser demos, no private licensed content.
- `docs/` current standards, archive index and historical visual references.

Private narration, soundtrack, licensed-only media, keys, render outputs and private review HTML do not belong in public Git.
