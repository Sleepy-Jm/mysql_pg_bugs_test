-- Read-only postchecks for report 113358; run in the same disposable schema/session.
SELECT * FROM t1 ORDER BY a; SELECT * FROM t2 ORDER BY a; SELECT @@sql_mode,@@optimizer_switch;
