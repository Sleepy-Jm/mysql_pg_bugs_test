-- Read-only postchecks for report 113506; run in the same disposable schema/session.
SELECT a,HEX(a),CHARSET(a),COLLATION(a) FROM t1 ORDER BY a; SELECT @@character_set_connection,@@collation_connection;
