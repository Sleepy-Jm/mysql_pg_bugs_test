USE `replay_9aefa80e786a8c1e3ddf2d46`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #112475; source anchors: cmain, c536346
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 REPLACE AS SELECT -89 AS c14 ORDER BY c14 ;
INSERT INTO t0 VALUES ( DEFAULT ) , ( DEFAULT ) ;
ALTER TABLE t0 RENAME TO t1 ;
INSERT INTO t1 VALUES ( 12 ) , ( 121 ) ;
SELECT t1 . c14 AS c25 FROM ( SELECT t1 . c14 AS c31 FROM ( SELECT CONVERT ( c14 = RAND ( ) IN ( SIGN ( -54 ) & RAND ( ) LIKE CASE -47 WHEN TRUE THEN -94 WHEN -16 THEN 107 ELSE -44 END , -6351076902139315214 , -68 ) , BINARY ) AS c58 FROM t1 ) AS t2 JOIN t1 ON + EXISTS ( SELECT t1 . c14 AS c33 FROM t1 WHERE c58 = ASCII ( -97 ) << t1 . c14 + -119 GROUP BY c14 , c14 ) , t1 AS t3 JOIN t1 AS t4 ON REVERSE ( t3 . c14 ) ) AS t5 JOIN t1 ON t5 . c31 = t5 . c31 ;

-- Read-only postcheck appended after unchanged source SQL.
SELECT c14,COUNT(*) AS n FROM t1 GROUP BY c14 ORDER BY c14;
