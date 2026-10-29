-- Report #110972; source anchors: cmain, c532403, c532454, c532456, c532485
-- Static preparation only; not executed. See case.json before any future isolated run.
INSERT INTO t1 VALUES('ccccc');
INSERT INTO t1 VALUES('ddddd');
SELECT * FROM t1 WHERE name LIKE '%ccccc%';
SELECT * FROM t1 WHERE MATCH(name) AGAINST('ccccc');
SELECT * FROM t1 WHERE name LIKE '%ddddd%';
SELECT * FROM t1 WHERE MATCH(name) AGAINST('ddddd');
ALTER TABLE t1 ENGINE=InnoDB;
SELECT * FROM t1 WHERE MATCH(name) AGAINST('ddddd');
