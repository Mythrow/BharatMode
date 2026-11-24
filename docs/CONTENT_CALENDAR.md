# Bharat Mode — Content calendar standard

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
