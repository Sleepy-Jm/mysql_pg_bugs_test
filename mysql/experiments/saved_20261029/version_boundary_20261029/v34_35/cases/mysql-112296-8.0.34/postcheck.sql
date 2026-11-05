-- Read-only postchecks for report 112296; run in the same disposable schema/session.
SELECT * FROM t0; SELECT COUNT(*) AS t1_rows FROM t1; SELECT * FROM t2;
