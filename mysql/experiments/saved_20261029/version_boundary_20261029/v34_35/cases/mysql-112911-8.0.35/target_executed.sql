USE `replay_096c9b9c770b1ae63d7103a7`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112911; source: cmain, c537525
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 ( c0 INT, PRIMARY KEY ( c0 ) ) ;
CREATE VIEW v0 AS SELECT ra1.c0 ca1 FROM t0 ra0 INNER JOIN t0 ra1 ON ra1.c0 IN ( SELECT ra1.c0 ca0 FROM t0 ra2 ) ;
INSERT INTO t0 VALUES ( 1 ), ( -1 ) ;

SELECT COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 4
SELECT /*+ JOIN_ORDER(ra5, ra2, ra1, ra0) SEMIJOIN(DUPSWEEDOUT) */ COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 8

-- Read-only postchecks for report 112911; run in the same disposable schema/session.
SELECT c0 FROM t0 ORDER BY c0; EXPLAIN SELECT /*+ JOIN_ORDER(ra5, ra2, ra1, ra0) SEMIJOIN(DUPSWEEDOUT) */ COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; SHOW WARNINGS;
