# Bharat Mode — permanent content registry and editorial workflow

## Authority

[registry.json](../content/registry.json) is the canonical content and release ledger; [CONTENT_LOG.md](../content/CONTENT_LOG.md) and calendar are generated views. [queue.json](../publishing/queue.json) is only editorial order. Release-page JSON stores exact proposed publishing fields, media hashes and episode-specific approval/evidence. Never maintain a competing list of counts in workflow docs.

Every candidate receives one permanent sequential ID-###, a distinct storyKey, topicKey, actual event date, source date, primary source, aliases and dedicated research sheet. Assign lowest unused BM-### only when the owner selects it; legacy BM-#### aliases are read-only. Never reuse IDs or delete old items. For a related but distinct event link relatedIds and explain distinguishingUpdate. Check all stages, canonical source URLs, title/aliases and actual research, not just matching words.

## Freshness-first research

Start at the current IST calendar date. Check actual event date separately from reporting date; a republication is not a new event. If today's verified candidates are insufficiently compelling widen to yesterday, then earlier dates (seven days by default; older only with explicit justification). Prefer verified substantive achievement, measurable stakes, original primary sources, meaningful visual potential and clear planned/deployed distinctions. Register only distinct verified ideas; explain the widened search. Present the actual evidence and news hook, not a rendering plan.

## Mandatory owner review sequence — 24 November 2026

1. Actual verified news, primary sources, claim ledger, caveats and editorial angle → owner selection/review.
2. Complete narration script (no spoken Bharat Mode tagline) → explicit owner approval.
3. Actual native 1080×1920 source-rendered visual storyboard (roughly five-second chronological frames plus all meaningful states, clickable viewer or HTML/PNG fallback, provisional timing/fallbacks disclosed) → owner approval. No image-generated imitation or text-only substitute.
4. Work generates audio only; main conversation renders approved source with actual aligned captions, cue-led story motion and approved music. Deliver actual draft MP4 for feedback. Final render and thumbnail approval, QA, rights, publishing package and explicit publication authorization remain separate.

Do not skip or combine gates without owner direction. See [production](PRODUCTION.md), [template](APPROVED_SHORTS_TEMPLATE.md), [recovery](PRODUCTION_REPRODUCIBILITY.md) and [publishing](PUBLISHING_PAGE.md). Never reopen existing published videos.

## Release stages

| Stage | Evidence |
|---|---|
| idea | Registered verified candidate; no production code. |
| in_progress | Explicit owner selection; production code assigned. |
| uploaded | Owner reports upload, dated record; not proof of schedule or public visibility. |
| scheduled | Owner reports upload and explicit schedule date; record exact time only if known (IST). |
| published_owner_reported | Dated explicit owner report of public visibility; URL and actual publication date may remain null. |
| published | Real public YouTube video URL, actual publication date, explicit owner sign-off and independent verification evidence/date. |

Stages advance, never regress; historical reports may legitimately skip unknown intermediate stages. A scheduled date passing does not imply publication. Release reports are not separate approval of render, thumbnail, rights or device checks. Record only actual evidence; a report date is not a publication date.

## Maintainer commands (owner need not run locally)

```sh
npm run content:check
npm run content:test
npm run content:find -- "topic or ID"
npm run content:add -- --title "Verified title" --slug unique-slug --story-key unique-event-key --topic-key topic-key --primary-source https://example.org/source --event-date YYYY-MM-DD --source-date YYYY-MM-DD
npm run content:move -- ID-XXX in_progress --note "Owner selected"
npm run content:move -- ID-XXX uploaded --reported-on YYYY-MM-DD --uploaded-at YYYY-MM-DD --note "Owner reports upload"
npm run content:move -- ID-XXX scheduled --reported-on YYYY-MM-DD --uploaded-at YYYY-MM-DD --scheduled-at YYYY-MM-DD --schedule-time HH:MM --note "Owner reports schedule"
npm run content:move -- ID-XXX published_owner_reported --reported-on YYYY-MM-DD --note "Owner confirms public"
npm run content:move -- ID-XXX published --published-at YYYY-MM-DD --youtube-url REAL_URL --approved-by-owner --verified-on YYYY-MM-DD --verification-evidence "Actual independent observation" --note "Evidence reconciled"
npm run content:sync
npm run check
```

For a release transition reconcile the matching release-page JSON in the same commit and preserve all QA flags. Calendar reflects registry only; see [calendar](CONTENT_CALENDAR.md). Collect comparable analytics; see [analytics](ANALYTICS_TRACKING.md). Historical migration decisions: [archive](archive/README.md).
