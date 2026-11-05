-- MySQL report #113319; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a INT); CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1),(2),(3),(4); INSERT INTO t2 VALUES(1),(2);
SET optimizer_switch='subquery_to_derived=off';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
SET optimizer_switch='subquery_to_derived=on';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
