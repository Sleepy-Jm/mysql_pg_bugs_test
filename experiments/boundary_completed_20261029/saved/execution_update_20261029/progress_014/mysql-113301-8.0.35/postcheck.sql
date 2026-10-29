-- Read-only postchecks for report 113301; run in the same disposable schema/session.
SELECT id_col,time_6,time_0 FROM test_time ORDER BY id_col; SELECT @@sql_mode;
