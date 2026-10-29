-- MySQL report #112704; source anchors: cmain, c537159, c542013
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION tmp_table_size=1024;
SELECT @@session.tmp_table_size;
WITH v AS (VALUES ROW(RAND(0)), ROW(RAND(1))) SELECT * FROM v AS v1 JOIN v AS v2;
SET SESSION tmp_table_size=16777216;
WITH v AS (VALUES ROW(RAND(0)), ROW(RAND(1))) SELECT * FROM v AS v1 JOIN v AS v2;
