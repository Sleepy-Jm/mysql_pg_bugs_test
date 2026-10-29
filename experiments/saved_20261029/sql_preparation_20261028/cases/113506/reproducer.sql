-- MySQL report #113506; source: cmain, c539290, c539293, c539294, c539322, c544157
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET NAMES utf8mb4;
CREATE TABLE t1(a CHAR(10) CHARACTER SET utf8mb4);
INSERT INTO t1 VALUES('你好'),('中午好');
SELECT a,CONVERT(a USING latin1) FROM t1 ORDER BY CONVERT(a USING utf8mb4);
SELECT a FROM t1 ORDER BY CONVERT(a USING utf8mb4);
