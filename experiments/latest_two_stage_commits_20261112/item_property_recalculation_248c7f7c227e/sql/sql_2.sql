-- T2 (C1, exploratory): scalar subquery inside a SELECT-list function; exercises the SELECT-expression
-- caller at sql_resolver.cc:7654-7693 (rollup unwrap not used here). Same sensitive property as T1.
DROP TABLE IF EXISTS t2_outer, t2_inner;
CREATE TABLE t2_outer (id INT PRIMARY KEY, v INT NOT NULL);
CREATE TABLE t2_inner (id INT PRIMARY KEY, w INT NOT NULL);
INSERT INTO t2_outer VALUES (1,10),(2,20),(3,30);
INSERT INTO t2_inner VALUES (1,5),(2,25),(3,35);
-- Target: SELECT-list function over scalar subquery.
SELECT id, (v + (SELECT w FROM t2_inner WHERE t2_inner.id = t2_outer.id)) AS s
  FROM t2_outer ORDER BY id;
-- Contrast: same SELECT-list function without subquery.
SELECT id, (v + 5) AS s FROM t2_outer ORDER BY id;
SET optimizer_trace='enabled=on';
SELECT id, (v + (SELECT w FROM t2_inner WHERE t2_inner.id = t2_outer.id)) AS s
  FROM t2_outer ORDER BY id;
SELECT TRACE FROM information_schema.OPTIMIZER_TRACE;
SET optimizer_trace='enabled=off';
DROP TABLE t2_outer, t2_inner;

