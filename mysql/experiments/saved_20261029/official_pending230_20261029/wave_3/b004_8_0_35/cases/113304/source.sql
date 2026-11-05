-- MySQL report #113304; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_mode='';
CREATE TABLE t0(c0 LONGTEXT) ;
INSERT INTO t0(c0) VALUES(0.1);
CREATE TABLE t1(c0 INT ZEROFILL PRIMARY KEY) ;
INSERT IGNORE INTO t1(c0) VALUES(NULL);

SELECT !((LEAST(t0.c0, t1.c0)) || (t1.c0)) FROM t1, t0; -- {0}
SELECT * FROM t1, t0 WHERE !((LEAST(t0.c0, t1.c0)) || (t1.c0)); -- {0000000000, 0.1}
