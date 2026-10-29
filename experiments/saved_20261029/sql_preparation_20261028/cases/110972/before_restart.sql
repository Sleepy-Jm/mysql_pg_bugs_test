-- Report #110972; source anchors: cmain, c532403, c532454, c532456, c532485
-- Static preparation only; not executed. See case.json before any future isolated run.
SET autocommit=1;
CREATE TABLE t1(name TEXT(10),FULLTEXT INDEX idx(name)) ENGINE=InnoDB;
INSERT INTO t1 VALUES('aaaaa');
INSERT INTO t1 VALUES('bbbbb');
DELETE FROM t1;
