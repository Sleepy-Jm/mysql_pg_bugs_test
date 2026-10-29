-- MySQL report #111918; source: cmain, c534860
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1 (c0 INT AUTO_INCREMENT UNIQUE KEY);
INSERT INTO t1 VALUES ();
INSERT IGNORE INTO t1 VALUES ();

SELECT 1 FROM t1;
 -- 2 rows
SELECT 1 FROM t1 WHERE (t1.c0 > CAST(X'0B36' AS CHAR));
 -- empty
SELECT 1 FROM t1 WHERE (NOT (t1.c0 > CAST(X'0B36' AS CHAR)));
 -- empty
SELECT 1 FROM t1 WHERE ((t1.c0 > CAST(X'0B36' AS CHAR)) IS NULL);
 -- empty
