-- MySQL report #8814; source anchors: cmain, c188416, c467094
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
CREATE TABLE t (c1 VARCHAR(10), INDEX (c1(10)), c2 VARCHAR(50), INDEX (c2(50)), b TINYBLOB, INDEX (b(50)), t TINYTEXT, INDEX (t(50))) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SHOW CREATE TABLE t;
ALTER TABLE t MODIFY c1 VARCHAR(50);
SHOW WARNINGS;
SHOW CREATE TABLE t;
SHOW INDEX FROM t;
