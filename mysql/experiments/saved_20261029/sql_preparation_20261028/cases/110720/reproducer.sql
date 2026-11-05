-- MySQL report #110720; source anchors: cmain, c531739
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET optimizer_switch = 'hypergraph_optimizer=on';
CREATE TABLE t(x VARCHAR(100), FULLTEXT KEY (x));
INSERT INTO t VALUES ('abc'), ('xyz'), (NULL), ('abc abc'), ('abc xyz');
ANALYZE TABLE t;
prepare stmt1 from "SELECT MATCH (x) AGAINST ('abc') AS score FROM t  GROUP BY score WITH ROLLUP HAVING score > 0";
execute stmt1;
execute stmt1;

DEALLOCATE PREPARE stmt1;
SELECT 1 AS server_alive;
