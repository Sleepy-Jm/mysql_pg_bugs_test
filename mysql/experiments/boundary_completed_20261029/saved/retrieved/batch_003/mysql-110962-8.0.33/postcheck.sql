-- Read-only postchecks for report 110962; run in the same disposable schema/session.
SELECT id,s_id,p_id FROM s1 ORDER BY id; SELECT i FROM t1; SELECT @@SESSION.sql_mode;
