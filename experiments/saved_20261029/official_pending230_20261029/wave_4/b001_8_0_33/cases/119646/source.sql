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
--Result: `id=2, val=20; id=3, val=30` (2 rows)
SET SESSION optimizer_switch='semijoin=off,derived_merge=off';
SELECT m.id, m.val
FROM t_main m
WHERE m.id IN (SELECT casted_id FROM v_test)
ORDER BY m.id;
