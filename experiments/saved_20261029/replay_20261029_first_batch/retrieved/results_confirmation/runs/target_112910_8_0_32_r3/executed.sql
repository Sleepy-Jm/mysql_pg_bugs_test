USE `replay_b6782b3bb1f8185a38320d0b`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #112910; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
SELECT * FROM ( VALUES ROW ( 'a', 0 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: empty

SELECT * FROM ( VALUES ROW ( 'a', 0 ), ROW ( 'b', 1 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: 1 row
