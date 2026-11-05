-- MySQL report #112037; source: cmain, c535234
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t1(a INT);
INSERT INTO t1 VALUES (1),(2),(3),(4);
ANALYZE TABLE t1;
SET optimizer_switch='subquery_to_derived=on';
EXPLAIN analyze SELECT a + (SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2 ) FROM t1;
