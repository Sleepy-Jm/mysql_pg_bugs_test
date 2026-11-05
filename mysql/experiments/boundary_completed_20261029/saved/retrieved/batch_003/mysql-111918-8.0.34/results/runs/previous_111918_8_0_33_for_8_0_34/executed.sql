USE `replay_26e8339df9fada30152b2613`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #111918; source: cmain, c534860
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1 (c0 INT AUTO_INCREMENT UNIQUE KEY);
INSERT INTO t1 VALUES ();
INSERT IGNORE INTO t1 VALUES ();

SELECT 1 FROM t1;
 -- 2 rows
SELECT 1 FROM t1 WHERE (t1.c0 > CAST(X'0B36' AS CHAR));
 -- empty
SELECT 1 FROM t1 WHERE (NOT (t1.c0 > CAST(X'0B36' AS CHAR)));
 -- empty
SELECT 1 FROM t1 WHERE ((t1.c0 > CAST(X'0B36' AS CHAR)) IS NULL);
 -- empty

-- Read-only postchecks for report 111918; run in the same disposable schema/session.
SELECT c0 FROM t1 ORDER BY c0; SELECT HEX(CAST(X'0B36' AS CHAR));
