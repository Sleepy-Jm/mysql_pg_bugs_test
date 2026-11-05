-- MySQL report #111067; source anchors: cmain, c532705
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a CHAR(10), fulltext(a)) ENGINE = InnoDB;
INSERT INTO t1 VALUES('aaa15');
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ALTER TABLE t1 ADD COLUMN y INT;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ANALYZE TABLE t1;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
