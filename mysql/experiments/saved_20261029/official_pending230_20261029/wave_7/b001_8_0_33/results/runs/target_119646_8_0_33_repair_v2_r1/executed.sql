USE `replay_30787640345cdf303741c3a7`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #119646; source anchors: cmain, c555476, c555720
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_optimizer=@@session.optimizer_switch;
DROP TABLE IF EXISTS t_main, t_ref;
CREATE TABLE t_main (id INT, val INT);
CREATE TABLE t_ref (id VARCHAR(10), ref_id INT, val INT);
INSERT INTO t_main VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t_ref VALUES ('1', 1, 100), ('2', 2, 200), ('3', 3, 300);

CREATE OR REPLACE VIEW v_test AS
SELECT CAST(r.id AS UNSIGNED) AS casted_id
FROM t_ref r 
WHERE r.val > 150;

SELECT m.id, m.val
FROM t_main m
WHERE m.id IN (SELECT casted_id FROM v_test)
ORDER BY m.id;
-- Result: `id=2, val=20; id=3, val=30` (2 rows)
SET SESSION optimizer_switch='semijoin=off,derived_merge=off';
SELECT m.id, m.val
FROM t_main m
WHERE m.id IN (SELECT casted_id FROM v_test)
ORDER BY m.id;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS main_rows FROM t_main;
SELECT COUNT(*) AS ref_rows FROM t_ref;
SELECT * FROM v_test;
