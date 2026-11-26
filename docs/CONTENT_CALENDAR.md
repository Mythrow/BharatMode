# Bharat Mode — Content calendar standard

> **CURRENT — 26 November 2026:** Owner reports BM-004 / ID-005 uploaded on 26 November and scheduled for Friday, 27 November 2026 (IST; exact time and URL not supplied). Remove from active editorial production and queue. BM-002 remains scheduled for 26 November until owner confirms public status. Totals: 2 owner-reported published, 2 scheduled, 0 active productions, 1 unselected idea (ID-004). Next unused production code BM-005, next permanent idea ID-006. Do not auto-promote scheduled releases. Figure reuse rights and music evidence, separate final V6 acceptance and device/YouTube checks remain unverified; upload report is not proof of those checks.


> **CURRENT — 25 November 2026:** ID-005 selected as BM-004 (GalaxEye/Bellatrix 30-satellite propulsion order), Stage 01 story review awaiting owner approval. 2 owner-reported published, 1 scheduled (BM-002, 26 Nov), 1 active (BM-004), 1 idea (ID-004). Next unused production BM-005, next idea ID-006. No change to BM-002 schedule.


> **CURRENT — 25 November 2026:** BM-002 / ID-002 uploaded and scheduled for 26 November 2026, owner confirmed; exact time and URL not supplied. Not published and not active production. BM-001/BM-003 owner-reported published, exact dates/URLs pending. ID-005 GalaxEye/Bellatrix registered as high-priority queued idea; ID-004 remains idea. Counts: 2 published/reported, 1 scheduled, 0 active, 2 ideas. BM-004 next unused production code; ID-006 next idea. Scheduled is an explicit release substatus of in_progress, separate in calendar; do not auto-promote or re-upload.


> **CURRENT — 25 November 2026:** Owner confirmed BM-001 PARAM Rudra published on 25 November 2026 (report date only; actual publication date and public YouTube URL not supplied). Removed from active editorial queue; do not re-upload or reopen. Both BM-001 and BM-003 are owner-confirmed published, 0 active productions, 2 ideas, 0 scheduled; formal published transition awaits real URLs and publication dates. BM-002 remains next available production code; ID-005 next idea. No inference of thumbnail/metadata/rights checks.


> **LATEST — dual numbering, owner decision 24 Nov 2026:** All ideas receive a permanent sequential `ID-###` first. Assign a separate `BM-###` production code only on owner selection, using the lowest unused positive number; never recycle an assigned number. Keep a single registry record with both codes, use idea ID for research and production code for new video deliverables. ID-001 / BM-001 PARAM Rudra is selected, at Stage 01 story review. ID-002 ICMR and ID-004 IIT Madras are unselected ideas. ID-003 / BM-003 L&T is owner-confirmed published, URL/date pending; preserve historical BM-0003 files and references without re-rendering. BM-002 is next, then skip BM-003 to BM-004; ID-005 is next idea. Earlier BM-#### identifiers below are legacy references, not new allocations. The story → script → visual storyboard → draft render approval order remains mandatory. `content/registry.json` schema v2 is authoritative; `id` is idea identity, `productionCode` is null until selected, and `legacyId` is read-only historical alias. Use `npm run content:move -- ID-005 in_progress --note "Owner selected story"` for a real selected ID; the allocator assigns its code automatically. No automatic publication.


Owner request, 24 November 2026: maintain a reusable HTML content calendar and provide a refreshed version whenever asked for the calendar, including past, current and future content status. This is a view of the existing content registry, not a new source of truth or automatic scheduling.

## Data and integrity

- Read the latest `content/registry.json`, `publishing/queue.json`, and per-episode `publishing/BM-####-release-page.json` metadata. Show all permanent IDs, no duplicate tracking.
- **Past / publication history:** formal published records with real YouTube URL and publication date, plus owner-confirmed public releases awaiting formal record reconciliation, distinctly marked. Use actual published date for calendar placement; if only an owner report date is known, show it explicitly as a report, not a confirmed upload date.
- **Current production:** selected in-progress stories, excluding owner-confirmed published episodes awaiting reconciliation. Queue position is editorial order, never an implied scheduled date.
- **Future:** registered ideas, queued candidates and explicitly scheduled future releases if present. Only display a scheduled date if the source record explicitly specifies one (`scheduledAt`). Unscheduled stories have no assigned release date. Event/source/discovery dates are separate from release dates.
- Counts include owner-confirmed publications as a distinct substatus. The underlying registry's Published transition still requires actual URL/date/owner approval. Do not fabricate these or mark metadata QA complete from a calendar view.
- Show IST snapshot date, month calendar with navigation and event legend, stage sections, permanent ID, title, topic, priority, queue order where applicable, event date, research and storyboard links, watch URL when present.
- Generate a fresh self-contained HTML file on every explicit request; provide a plain direct download link. Since ChatGPT's attachment preview may display raw HTML, also provide a concise readable chat view of the same statuses, and note that the file works in a regular browser. No server, paid compute, automatic publishing or external calendar required.
- Keep reusable source in Git; save dated HTML snapshots in private Library. Treat snapshot as read-only, not a live dashboard. Refresh from GitHub before presenting any new one. Calendar does not replace daily research or approved in-chat final-render publishing dashboard.

## Generator

`python scripts/create_content_calendar.py --repo . --as-of YYYY-MM-DD --output out/Bharat-Mode-content-calendar-YYYY-MM-DD.html`

Uses Python standard library and embedded browser JavaScript. Calendar grid uses Monday-first weeks; arrows browse months, Today returns to snapshot month. Source is `scripts/create_content_calendar.py`.

## First snapshot — 24 November 2026

- BM-0003: owner-confirmed published (report dated 24 Nov; exact publication date and URL missing); removed from production queue. Formal registry Published count remains zero until reconciliation. Never re-produce this episode.
- BM-0001: In Progress, high priority, editorial queue #1.
- BM-0002: Idea, medium priority, editorial queue #2; not yet selected for production.
- BM-0004: Idea, medium priority, not queued.
- 1 owner-reported publication, 1 active production, 2 ideas, 0 explicitly scheduled releases. No invented release dates. Source snapshot counts and date classification tested; JS syntax checked. Interactive browser test not performed.
- Actual generated snapshot: private Library `/BharatMode/calendars/Bharat-Mode-content-calendar-2026-11-24.html`, ID `libfile_9ecedade0c74819195b9087232e0ec42`.
