-- Report #114384; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE IF NOT EXISTS t1(c0 SMALLINT) ;
INSERT INTO t1(c0) VALUES(0.49);
CREATE INDEX i0 ON t1(c0);

SELECT t1.c0 FROM t1 WHERE t1.c0 IN (LOG(0.6261534882548163));

SELECT c0 FROM (SELECT t1.c0, (t1.c0 IN (LOG(0.6261534882548163))) IS TRUE AS flag FROM t1) as t WHERE flag=1;
