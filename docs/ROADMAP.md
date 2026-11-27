# Bharat Mode — engineering roadmap

Release state is maintained exclusively in the [registry](../content/registry.json). This page is the engineering/operational backlog.

| Milestone | Status / acceptance |
|---|---|
| Brand and official avatar/banner | Approved; retain exact bytes, verify phone/TV crop separately. |
| Narrator and MUSIC-06 B | Approved identity and reference mix; story-specific QA and private rights proof remain separate. |
| Editorial gates and permanent ID registry | In use; release-state reconciliation and validation hardening in audit PR #6. |
| Reusable native renderer | Incomplete until actual 60fps production render with verified acoustic alignment, independent story motion, exact timeline, visual and audio QA. See [issue #5](https://github.com/Mythrow/BharatMode/issues/5). |
| Recoverable production packages | Require source, structured script, cue maps, alignment, assets/checksums, render environment and QA for each new Short. Recover prior bundles without regenerating releases. |
| Publishing | Chat-first dashboard; owner controls YouTube; record factual release evidence. |
| Analytics and cadence | First 24h/7d comparable windows, retention when available, one editorial variable per test. Review after ~10 published Shorts; Home tab remains deferred. |
| Dependency reproducibility | Generate/verify dependency lock in an authorized networked environment; no fake lockfile. Run full test suite and renderer integration checks. |

Never modify earlier videos to satisfy a new template change. [Prior milestone decisions](archive/README.md).
