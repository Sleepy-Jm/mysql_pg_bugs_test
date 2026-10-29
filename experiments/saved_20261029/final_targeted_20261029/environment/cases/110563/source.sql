-- Report #110563; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0 (c0 INT, c1 INT);
INSERT INTO t0(c0,c1) VALUES (43,47),(92,71);



SELECT 1 FROM t0 tx RIGHT JOIN t0 ty ON ty.c0 <=> 1 WHERE ROW(ty.c0, tx.c1) >= ROW(ty.c1, ty.c1);
SELECT CAST(sum(c0) AS SIGNED) FROM (SELECT CAST(ROW(ty.c0, tx.c1) >= ROW(ty.c1, ty.c1) AS SIGNED) FROM t0 tx RIGHT JOIN t0 ty ON ty.c0 <=> 1) t1 (c0);
