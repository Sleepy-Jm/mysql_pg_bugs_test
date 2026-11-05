-- Read-only postchecks for report 112911; run in the same disposable schema/session.
SELECT c0 FROM t0 ORDER BY c0; EXPLAIN SELECT /*+ JOIN_ORDER(ra5, ra2, ra1, ra0) SEMIJOIN(DUPSWEEDOUT) */ COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; SHOW WARNINGS;
