-- Report #114382; source anchors: cmain, c541572, c541690
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE IF NOT EXISTS t1(c0 TINYINT(199)) ;
INSERT LOW_PRIORITY IGNORE INTO t1(c0) VALUES (1950654919);

SELECT f1 FROM (SELECT (LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) AS f1 FROM t1) as t WHERE (f1) & (921571774);

SELECT f1 FROM (SELECT (LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) AS f1, ((LEAST(CURDATE(), (- (t1.c0)), (~ (t1.c0)),  EXISTS (SELECT 1))) & (921571774)) IS TRUE AS flag FROM t1) as t WHERE flag=1;
