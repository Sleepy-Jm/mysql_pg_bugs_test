-- Read-only postchecks for report 112037; run in the same disposable schema/session.
SELECT a+(SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2) AS result_value FROM t1 ORDER BY a; SELECT a FROM t1 ORDER BY a;
