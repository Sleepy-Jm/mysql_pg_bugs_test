-- Read-only postchecks for report 107424; run in the same disposable schema/session.
SELECT ST_AsText(g1), ST_SRID(g1) FROM t1 ORDER BY ST_AsText(g1);
