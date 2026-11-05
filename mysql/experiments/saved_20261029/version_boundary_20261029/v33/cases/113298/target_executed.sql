USE `replay_10a9229cc5bc6bce4f5461dd`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113298; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0( c1 INTEGER);
INSERT INTO t0 (c1) VALUES (1);
CREATE INDEX i0 ON t0(c1  );

SELECT * FROM t0 WHERE (1/1.5 IN (c1)); -- 1
SELECT * FROM t0 WHERE (NOT (1/1.5 IN (c1))); -- 1

ALTER TABLE t0 DROP INDEX i0;
SELECT * FROM t0 WHERE (1/1.5 IN(c1));
SELECT * FROM t0 WHERE NOT(1/1.5 IN(c1));

-- Read-only evidence after the unchanged source SQL, same session.
SELECT c1,1/1.5 AS computed_fraction,(1/1.5 IN(c1)) AS predicate_value FROM t0;
