-- Read-only postchecks for report 114381; run in the same disposable schema/session.
SELECT * FROM t0; SELECT * FROM t1; SELECT TIMEDIFF('3939-09-13 16:49:10.309835','4722-09-08 23:55:52.675528'); SHOW WARNINGS;
