-- T1 (C1, exploratory): scalar subquery inside a WHERE function; post-replacement root is Item_func.
-- Sensitive: root has PROP_SUBQUERY before replacement, none after. Observable: residual has_subquery() in trace/EXPLAIN.
DROP TABLE IF EXISTS t1_outer, t1_inner;
CREATE TABLE t1_outer (id INT PRIMARY KEY, v INT NOT NULL);
CREATE TABLE t1_inner (id INT PRIMARY KEY, w INT NOT NULL);
INSERT INTO t1_outer VALUES (1,10),(2,20),(3,30);
INSERT INTO t1_inner VALUES (1,5),(2,25),(3,35);
-- Target: WHERE expression is a function over a scalar subquery.
SELECT id, v FROM t1_outer
 WHERE (v + (SELECT w FROM t1_inner WHERE t1_inner.id = t1_outer.id)) > 20;
-- Contrast: same predicate without subquery (no replace_subquery_in_expr path).
SELECT id, v FROM t1_outer WHERE v + 5 > 20;
-- Diagnostic: trace to inspect residual subquery handling on the post-replacement item.
SET optimizer_trace='enabled=on';
SELECT id, v FROM t1_outer
 WHERE (v + (SELECT w FROM t1_inner WHERE t1_inner.id = t1_outer.id)) > 20;
SELECT TRACE FROM information_schema.OPTIMIZER_TRACE;
SET optimizer_trace='enabled=off';
DROP TABLE t1_outer, t1_inner;

