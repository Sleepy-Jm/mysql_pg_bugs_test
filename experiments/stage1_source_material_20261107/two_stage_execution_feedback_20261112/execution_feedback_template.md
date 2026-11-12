# Executed example record

Copy one record per executed SQL example. Replace fields with actual evidence; do not submit this blank template as verified feedback.

- Example ID / originating Stage2 run and candidate ID:
- Evidence label: PATH_REACHED or ANOMALY_OBSERVED (both may apply).
- Parent and target revisions / relevant execution configuration:
- Exact executed SQL, including required setup and data, or its contents plus file hash:
- Path evidence: confirmed / not observed / unverified; identify the target object, source location, selected branch, and evidence file or trace excerpt.
- Outcome evidence: independent expected result, actual result or runtime failure, and evidence file. Record the number of parent/target paired runs and the number that differ when available.
- Attribution to the target change: confirmed / unverified, with supporting evidence when confirmed.
- Demonstrated construction to reuse and questions still unresolved:

PATH_REACHED requires observed path evidence. ANOMALY_OBSERVED requires actual anomaly evidence; it does not establish the path or cause by itself. Syntax/setup failures and output discrepancies without a correctness determination remain diagnostics, not confirmed anomaly examples for the target.

## observations.json input for `feedback_pipeline.py`

The executable input uses one record per SQL candidate. Evidence paths are relative to the archived run directory and are hashed by the adapter before they are copied into feedback.

```json
{
  "cases": [
    {
      "candidate_id": "sql_1",
      "path": {
        "status": "confirmed",
        "object": "Item_string",
        "source_location": "sql/item.cc:3464-3472",
        "branch": "QT_TO_ARGUMENT_CHARSET",
        "evidence_files": ["path_trace.json"]
      },
      "oracle": {
        "status": "anomaly",
        "expected": "...",
        "observed": "...",
        "evidence_files": ["oracle_result.json"]
      },
      "attribution": {"status": "unverified"}
    }
  ]
}
```

`path.status=confirmed` with valid evidence emits `PATH_REACHED`. `oracle.status=anomaly` or `runtime_anomaly` additionally requires `expected`, `observed`, and valid evidence to emit `ANOMALY_OBSERVED`. A parent/target difference without these records is retained as an excluded diagnostic.
