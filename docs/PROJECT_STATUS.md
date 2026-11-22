# Bharat Mode — Project Status / New-Chat Handoff

**THIS IS THE CANONICAL RESUME POINT.**

Last verified: **23 November 2026**. Voice decision approved this date; consult Git history for the latest commit. After a task is completed, update this file *in the same commit as the task*, revise the roadmap, and note the actual GitHub commit and any incomplete checks. GitHub is authoritative; old conversation snippets and historical V1–V5 examples are not.

## What the project is
**Bharat Mode** is a research-led, faceless YouTube Shorts channel highlighting verified Indian discoveries, inventions, builders, science, technology and meaningful national progress. Content should find underreported stories without sensationalizing or claiming unsupported "firsts". Voice, evidence and readable vertical animation are core to the product.

Repository: https://github.com/Mythrow/BharatMode

## Current stage: V6 visuals and Brian narrator APPROVED; production integration NEXT

**Completed and approved by channel owner**
- Channel name: **Bharat Mode**; tagline: **Big Ideas. Real Progress.**
- Brand palette: Classic Saffron `#E8752E`, Warm Ivory `#FFF7EB`, Ocean Teal `#117A7A`, Graphite Navy `#283039`, Deep Charcoal `#0B1018`.
- Typography: **Sora** for headlines/display; **Manrope SemiBold** for reading and captions.
- Exact SVG **badge and avatar** are approved source artwork under `public/brand/`; do not redraw or recolor the logo's internal colors.
- YouTube channel-cover design approved; see [CHANNEL_BANNER.md](CHANNEL_BANNER.md). Verify actual YouTube device crops before relying on it.
- **Official Shorts V6 visual/motion template APPROVED on 23 November 2026** after the final bar-centering adjustment. The source of truth is [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md); reusable visual component is [`src/approved-shorts-template.jsx`](../src/approved-shorts-template.jsx).
- **Progress bar perfectly centered** on 1080px canvas: 84px left + 912px bar + 84px right. A regression checker exists at `scripts/test-approved-template.mjs`.
- Approved look: directional character-by-character headline typing **without cursor**; entrances for text, hero and diagrams; raised hero; 0.34s subtle scene dissolve; topic-only pill; flexible chapter segmentation rather than fixed five-step formula; one-line *centered* phrase-group captions with very light, content-sized translucent backing, ~0.2s word pop from 60% to slight overshoot, transient highlight on spoken word; old phrases disappear.
- Earlier browser HTML preview variants under `previews/html/` are retained as design history. **V6 with symmetric progress** is the only current approved visual baseline.
- **Narrator direction approved 23 November 2026:** **Brian — Deep, Resonant and Comforting**, provider **vidIQ voiceover**, voice ID `nPczCjzI2devNBz1zQrb`. The owner approved its professional sound after hearing a real generated PARAM Rudra audition sample (~12.28 seconds). **Indian accent is not required. No paid voice subscription is authorized at this stage.** See [VOICE_DIRECTION.md](VOICE_DIRECTION.md) and [`config/voice.json`](../config/voice.json).

**Not yet completed / not approved for publication**
- The `BharatShort` production renderer in `src/short.jsx` is **still a legacy renderer**, not yet fully upgraded to approved V6 motion and per-word aligned captions. Its bar alignment has been fixed.
- No end-to-end **voice-aligned, fully rendered, phone-tested** publishable Short has been verified.
- Narrator timbre/identity is approved as Brian. Full-script pronunciation, delivery consistency, word timing and sound-mix QA are pending; vidIQ-mediated commercial use rights still require verification before publication. The existing OpenAI TTS script is **not connected** to this Brian selection.
- Word-level caption timestamps must come from real finalized narration audio (TTS word timestamps or forced alignment), not the manually estimated prototype timings.
- Evidence/rights pipeline, upload-ready sourcing, audio ducking/loudness QA, actual YouTube crop/safe-area QA, and three distinct finished pilots are outstanding.

## Exactly where to resume in the next chat

**NEXT TASK — Implement Brian audio ingestion and accurate word-level caption alignment without buying a voice subscription.**

1. Narrator selection is **done**: Brian via vidIQ voiceover, ID `nPczCjzI2devNBz1zQrb`. No Indian-accent constraint. Existing ~12.28-second generated sample confirms the audition, not full-video QA.
2. Use existing vidIQ account credits only when explicitly warranted; no automatic plan upgrades or paid TTS subscriptions. At this checkpoint, 38 of 150 renewable credits remain, next refill 21 December 2026 IST. Voiceovers cost 28 credits per started 1,000 script characters. This balance is time-sensitive, not a permanent budget guarantee.
3. Implement a provider-independent **final-audio ingest + word-for-word alignment** workflow. The available vidIQ voiceover tool generates MP3 audio but does not supply word-level timestamps. Align against final audio, verify exact word matches, and drive the approved V6 centered grouped captions from real timestamps.
4. Migrate the legacy `src/short.jsx` to V6 without redesign. Integrate Brian narration, original music/SFX and loudness ducking.
5. Confirm the **commercial-use license / relevant voice rights for vidIQ-generated Brian audio before any public/monetized upload**. A free credit allowance is not proof of commercial rights. Fact-check story claims, verify documentary visuals, render and phone-review one complete pilot, then develop two different pilots.
6. Resume broader editorial queue, channel setup, upload packaging and cadence only after first-pilot QA.

**Completed in this checkpoint:** owner approved Brian; configuration and documentation stored. **Not completed:** automated vidIQ-to-render audio transfer, forced alignment, commercial rights verification, full voiced renderer, end-to-end render or phone QA.

Current implementation tracker: [GitHub issue #5 — voice-synced V6 renderer and first pilot](https://github.com/Mythrow/BharatMode/issues/5).

## Non-negotiable workflow preferences
- **The owner does not want to run code or install tools on their device.** Deliver playable HTML/visual reviews directly in ChatGPT with download links whenever feasible.
- **The approved narrator is Brian**, without an Indian-accent requirement. Prefer using existing renewable vidIQ credits for prototyping, **no paid voice subscription** or silent billing upgrades. Check commercial-use rights before publishing.
- Do not make unnecessary previews after explicit visual approval; make minor fixes in source and report the change.
- Preserve the approved badge, avatar and V6 visual baseline unless the owner explicitly requests changes.
- Keep storyline structure flexible and topic-appropriate. No fixed chapter count, title formula or compulsory length.
- Use reputable primary/public sources where possible; store references, source dates, publication-stage qualifiers and claims evidence in research metadata/descriptions. Never imply speculative illustrations are actual footage.
- **Store** code, docs, storyboard/research metadata, licensed asset references, and original music and SFX masters in GitHub.
- **Do not store** generated speech audio or rendered video files in GitHub. Those can be regenerated and provided to the owner as review/download artifacts.
- User's timezone: Asia/Kolkata. Use absolute dates in handoffs where needed.

## Read these files in this order in a new session
1. **This file**: `docs/PROJECT_STATUS.md` — current stage, approvals, next action.
2. [ROADMAP.md](ROADMAP.md) — project-wide sequence and acceptance milestones.
3. [APPROVED_SHORTS_TEMPLATE.md](APPROVED_SHORTS_TEMPLATE.md) — immutable approved design baseline.
4. [PRODUCTION.md](PRODUCTION.md) — existing production scripts and known limitations.
5. [BRAND.md](BRAND.md), [LOGO_DIRECTION.md](LOGO_DIRECTION.md) and relevant story files as needed.
6. [GitHub issue #5](https://github.com/Mythrow/BharatMode/issues/5) for remaining actionable work.

## Handoff convention after each significant change
Update this file and `docs/ROADMAP.md` with:
- **Done:** exactly what was completed and reviewed; link the source or commit.
- **Approved vs proposed:** explicit approval boundary.
- **Verification:** what actually ran/passed and what remains untested.
- **Next:** single immediate action, followed by optional subsequent tasks.
- **Blocked:** any missing tools, accounts, keys, licensing or data.
- Keep the most current status near the top; do not append contradictory “current draft” fragments endlessly.

## One-message prompt to resume anywhere

> Continue the Bharat Mode YouTube Shorts project from https://github.com/Mythrow/BharatMode. First read `docs/PROJECT_STATUS.md`, then `docs/ROADMAP.md` and `docs/APPROVED_SHORTS_TEMPLATE.md`. Respect the approved V6 design, do not ask me to run code locally, and carry out the next unfinished milestone. Update the GitHub status and documentation after completing work.

**Important:** A new chat does **not** automatically fetch or read this GitHub file just because it exists. The prompt above explicitly points it to the authoritative repository. In the Bharat Mode ChatGPT Project, prior context may help, but check this file for the current state rather than trusting a possibly stale summary.
