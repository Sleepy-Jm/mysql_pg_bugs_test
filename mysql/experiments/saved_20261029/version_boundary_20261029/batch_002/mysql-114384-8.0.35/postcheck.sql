-- Read-only postchecks for report 114384; run in the same disposable schema/session.
SELECT c0,LOG(0.6261534882548163) AS log_value FROM t1; EXPLAIN SELECT t1.c0 FROM t1 WHERE t1.c0 IN (LOG(0.6261534882548163)); SHOW WARNINGS;
