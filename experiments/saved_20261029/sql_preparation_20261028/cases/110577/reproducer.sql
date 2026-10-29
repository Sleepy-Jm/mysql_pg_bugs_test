-- MySQL report #110577; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT CAST(1985 AS YEAR);
CREATE TABLE t5(c1 YEAR AS(CAST(1985 AS YEAR)));
SHOW CREATE TABLE t5;
