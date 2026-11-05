-- MySQL report #112439; source: cmain, c536279
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(i INT PRIMARY KEY);
INSERT INTO t VALUES(1),(2),(3);
SELECT * FROM t WHERE i IN(VALUES ROW(1),ROW(2));
SELECT * FROM t WHERE i IN(SELECT 1 UNION SELECT 2);
