-- MySQL report #113446; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a BIT(1),b INT,c INT);
INSERT INTO t1 VALUES(b'0',23,92),(b'1',293,23);
SELECT a,b FROM t1 ORDER BY a;
SELECT DISTINCT a,b FROM t1 ORDER BY a;
SELECT HEX(a),a+0,b FROM t1 ORDER BY a;
ALTER TABLE t1 ADD KEY ab(a,b);
SELECT DISTINCT a,b FROM t1 ORDER BY a;
