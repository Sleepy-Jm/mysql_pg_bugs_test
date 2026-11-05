-- MySQL report #110209; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION sql_generate_invisible_primary_key=OFF;
CREATE TABLE t0(c0 char(1) PRIMARY KEY );
INSERT INTO t0 VALUES ('1');
SELECT * FROM t0 WHERE (- ((~ (((t0.c0) IS NULL))))); -- 1

DROP TABLE t0;
-- case 2
CREATE TABLE t0(c0 char(1));
INSERT INTO t0 VALUES ('1');
SELECT * FROM t0 WHERE (- ((~ (((t0.c0) IS NULL))))); -- ERROR 1690 (22003): BIGINT value is out of range in '-(~((`test`.`t0`.`c0` is null)))'
