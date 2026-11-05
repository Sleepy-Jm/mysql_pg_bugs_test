-- MySQL report #112345; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1 (a INT NOT NULL, b INT NOT NULL);
CREATE TABLE t2 (c INT NOT NULL, d INT NOT NULL);
CREATE TABLE t3 (e INT NOT NULL);

explain format=tree SELECT * FROM t1 AS ta
WHERE ta.a IN (SELECT c FROM t2 AS tb
WHERE (SELECT MIN(e) FROM t3 as tc
WHERE tb.d=tc.e) < SOME(SELECT e FROM t3 as tc
WHERE ta.b=tc.e));
explain format=json SELECT * FROM t1 AS ta
WHERE ta.a IN (SELECT c FROM t2 AS tb
WHERE (SELECT MIN(e) FROM t3 as tc
WHERE tb.d=tc.e) < SOME(SELECT e FROM t3 as tc
WHERE ta.b=tc.e));
