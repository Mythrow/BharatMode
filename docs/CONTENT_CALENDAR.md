# Content calendar

Owner requests a fresh self-contained HTML calendar on every explicit request plus a concise chat view. Read latest [registry](../content/registry.json); it alone defines stages and actual schedule/report dates. Editorial queue supplies ordering only. Release records provide corroborating metadata, not separate state. Display verified publication dates, dated owner reports (not actual release dates), explicit schedule date/time if supplied, uploaded-unscheduled, active production and ideas separately. Do not promote elapsed schedules or invent dates. Display IST snapshot date, all IDs, month navigation, status counts, source/research links and watch URL if verified.

```sh
python scripts/create_content_calendar.py --repo . --as-of YYYY-MM-DD --output out/Bharat-Mode-content-calendar-YYYY-MM-DD.html
```

Deliver direct HTML link (regular browser if chat displays source) and chat summary; store private snapshots, not public generated artifacts. Previous calendar history: [archive](archive/README.md).
