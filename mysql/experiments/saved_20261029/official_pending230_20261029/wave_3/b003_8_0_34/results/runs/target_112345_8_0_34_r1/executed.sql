USE `replay_73dbce5095d78091a1a4a1c8`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #112345; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1 (a INT NOT NULL, b INT NOT NULL);
CREATE TABLE t2 (c INT NOT NULL, d INT NOT NULL);
CREATE TABLE t3 (e INT NOT NULL);

explain format=tree SELECT * FROM t1 AS ta
WHERE ta.a IN (SELECT c FROM t2 AS tb
WHERE (SELECT MIN(e) FROM t3 as tc
WHERE tb.d=tc.e) < SOME(SELECT e FROM t3 as tc
WHERE ta.b=tc.e));
explain format=json SELECT * FROM t1 AS ta
WHERE ta.a IN (SELECT c FROM t2 AS tb
WHERE (SELECT MIN(e) FROM t3 as tc
WHERE tb.d=tc.e) < SOME(SELECT e FROM t3 as tc
WHERE ta.b=tc.e));

-- No additional postcheck required by the reviewed oracle.
