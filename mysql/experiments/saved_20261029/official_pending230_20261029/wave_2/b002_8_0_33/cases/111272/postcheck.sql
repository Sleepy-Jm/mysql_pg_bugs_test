-- Read-only postchecks for report 111272; run in the same disposable schema/session.
SELECT HEX(c1) FROM t1 ORDER BY HEX(c1); SELECT @@collation_connection,@@collation_database,@@sql_mode;
