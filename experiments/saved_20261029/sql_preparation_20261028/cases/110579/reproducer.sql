-- MySQL report #110579; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLEt85 (c0 INT,c4 TEXT);
INSERT INTO t85 VALUES (69,'5'),(-22,'3'),(-24,'8'),(73,'a');
CREATE TABLE t100 (c0 INT);



SELECT 1 FROM t100 RIGHT JOIN t85 USING (c0);
SELECT 1 FROM t100 RIGHT JOIN t85 USING (c0) WHERE t85.c4 NOT BETWEEN -50 AND field(t85.c0, t100.c0);
SELECT 1 FROM t100 RIGHT JOIN t85 USING (c0) WHERE NOT (t85.c4 NOT BETWEEN -50 AND field(t85.c0, t100.c0));
SELECT 1 FROM t100 RIGHT JOIN t85 USING (c0) WHERE (t85.c4 NOT BETWEEN -50 AND field(t85.c0, t100.c0)) IS NULL;
