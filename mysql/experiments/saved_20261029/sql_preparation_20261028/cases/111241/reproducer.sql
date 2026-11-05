-- MySQL report #111241; source anchors: cmain, c533082
-- Static preparation only. NOT EXECUTED. See case.json for conditions and oracle.
CREATE TABLE t0(c0 BOOL);
INSERT INTO t0 VALUES (true);

SELECT MIN(t0.c0) FROM t0 ;  # 1

SELECT t0.c0 FROM t0 WHERE (('0')NOT REGEXP((((t0.c0))NOT LIKE(CASE t0.c0 WHEN 76 THEN 0.7 ELSE t0.c0 END )))AND( t0.c0 IN ((1))));  # 1

SELECT t0.c0 FROM t0 WHERE (('0')NOT REGEXP((((t0.c0))NOT LIKE(CASE t0.c0 WHEN 76 THEN 0.7 ELSE t0.c0 END )))AND( t0.c0 IN (SELECT MIN(t0.c0) FROM t0 )));  # empty result
