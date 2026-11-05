USE `replay_ac604c0b80f148074e440c69`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112306; source: cmain, c535975, c536008
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
CREATE TABLE t1(c0 INT);
CREATE TABLE t2(c0 INT, c1 INT, c2 INT);
CREATE TABLE t3(c0 INT, c1 INT, c2 INT);
INSERT IGNORE INTO t3 VALUES(1, 2, 0.1);
INSERT INTO t1 VALUES(-3);

SELECT COUNT(*) FROM t3, t2 INNER JOIN t0 ON t0.c0 RIGHT JOIN t1 ON FALSE WHERE (t0.c0 IS NOT NULL) = (BIT_COUNT(t3.c2)); -- {1}
SELECT /*+ JOIN_SUFFIX(t2, t3)*/ COUNT(*) FROM t3, t2 INNER JOIN t0 ON t0.c0 RIGHT JOIN t1 ON FALSE WHERE (t0.c0 IS NOT NULL) = (BIT_COUNT(t3.c2));

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*) AS n FROM t0; SELECT COUNT(*) AS n FROM t2; SELECT c0 FROM t1; SELECT c0,c1,c2 FROM t3;
