-- Read-only postchecks for report 111699; run in the same disposable schema/session.
SELECT COUNT(*) AS t0_rows FROM t0; SELECT COUNT(*) AS t1_rows FROM t1; SELECT @@optimizer_switch;
