-- MySQL report #113298; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0( c1 INTEGER);
INSERT INTO t0 (c1) VALUES (1);
CREATE INDEX i0 ON t0(c1  );

SELECT * FROM t0 WHERE (1/1.5 IN (c1)); -- 1
SELECT * FROM t0 WHERE (NOT (1/1.5 IN (c1))); -- 1

ALTER TABLE t0 DROP INDEX i0;
SELECT * FROM t0 WHERE (1/1.5 IN(c1));
SELECT * FROM t0 WHERE NOT(1/1.5 IN(c1));
