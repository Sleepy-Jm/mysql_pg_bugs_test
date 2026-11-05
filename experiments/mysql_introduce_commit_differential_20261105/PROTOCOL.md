# MySQL introduce-commit differential experiment

Run five rounds of ten complete SQL candidates for each confirmed MySQL introduce commit. Round 1 uses commit analysis. Later rounds may use only independently verified `difference` candidates from the immediately preceding round; failed, timed-out, startup-failed, connection-failed, no-difference, and inconclusive candidates are excluded from feedback. Do not repair failed candidates.

Execute each candidate on the exact first parent and target revisions with equivalent data, configuration, and session order. Record result-set differences, success/error outcomes, SQLSTATE or error differences, and crashes separately. Compare result rows without relying on row order when SQL has no `ORDER BY`. Timeouts remain pending review. Startup and connection failures are inconclusive.

The current producer supports serial sessions only: it applies one session's configuration and all of its setup, operations, and cleanup, then proceeds to the next session in `session_order`. Configuration is limited to a single session-scoped `SET` statement. Concurrent schedules and server-level configuration are unsupported; record these as capability gaps and do not count them as executed candidates.

`differential_status` is one of `difference`, `no_difference`, `inconclusive`, or `not_run`. It selects candidates for study and is not an independent bug oracle. Preserve requests, model outputs, SQL, both-version environments and logs, verification attempts, and summaries. Keep each execution in a fresh run directory.

| Case | Version | Parent | Target |
|---|---|---|---|
| Derived-condition charset (`4d2da251cb53`) | 8.0.32 | `e248166db3c95b4fc998ca14cff914f1fdafbe7b` | `4d2da251cb536340d19438cc0039bb2846f9a634` |
| Item property recalculation (`248c7f7c227e`) | 8.0.33 | `15980860ac2639f41dfbda2f7fffb7aeeab32921` | `248c7f7c227e76f3422378ca3b9e10d141dcfc86` |
| Window frame state (`c296cddb93ff`) | 8.0.32 | `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` | `c296cddb93ffc631f9b43d3b1ff769604e7469d7` |
