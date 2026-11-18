# run_022_stage12_v5 verification

Stage1 used `deepseek-v4-pro`; Stage2 was retried with `deepseek-v4-flash` with direct-output constraints and produced five SQL blocks. Each SQL block was executed on the exact parent and target builds three times in isolated server containers.

| SQL | Candidate | Parent/target result | Repeatability | Notes |
|---|---|---|---|---|
| T1 (`sql_1.sql`) | C1 outer LIKE over UNION derived table | Difference in all 3 rounds | Stable | Explicit introducer matches on both; no-introducer query returns `Ä, Ä` on parent and empty on target. |
| T2 (`sql_2.sql`) | C1 no-introducer/coercion boundary | No difference | Stable | Both queries return `A, A` on both revisions. |
| T3 (`sql_3.sql`) | C1 connection-charset boundary | No difference | Stable but uninformative | `SET NAMES latin1` is paired with UTF-8 query bytes; both sides return empty resultsets without SQL errors. |
| T4 (`sql_4.sql`) | C2 derived-list LIKE cloned by column replacement | Difference in all 3 rounds | Stable | Explicit introducer matches on both; no-introducer query returns `1, 1` on parent and empty on target. |
| T5 (`sql_5.sql`) | C1 ASCII control | No difference | Stable | Both revisions return `abc, abc`. |

The two stable differences are SQL-visible and repeatable. Under the setup's declared `utf8mb4` connection and `utf8mb4_bin` columns, the no-introducer `Ä` literal should match `Ä`; therefore the target-side empty result is a semantic deviation candidate. The explicit-introducer query in the same blocks matches on both revisions, which localizes the difference to the no-introducer branch.

T3 should not be treated as evidence for or against the fix because its connection-character-set change makes the literal encoding dependent on the client input bytes. T2 and T5 are negative results. No claim is made that the internal modified branch was reached: confirming that requires instrumentation of `parse_expression`, the serialized buffer, and the reparsed `Item_string` metadata.

Artifacts: `stage1_output.txt`, `stage2_output_retry2.txt`, `sql_1.sql`–`sql_5.sql`, `server_evidence/`, and `verification_summary.json` in this run directory.
