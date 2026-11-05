-- MySQL report #41996; source anchors: c204603, c255377
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(c BIGINT,KEY(c),a INT) ENGINE=InnoDB;
INSERT INTO t1 VALUES(2,2);
DELETE t1 FROM t1 a,t1 WHERE a.a=t1.c;
SELECT COUNT(*) FROM t1;
SELECT 1 AS server_alive;
