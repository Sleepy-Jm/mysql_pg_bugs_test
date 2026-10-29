-- Report #112147; source anchors: cmain, c535553, c535600
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t(a INT,j JSON,INDEX kj((CAST(j AS DATE ARRAY))));
INSERT INTO t VALUES(1,JSON_ARRAY(CAST("2010-10-10" AS DATE),CAST("2010-10-10" AS DATE)));
SELECT * FROM t USE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE DATE'2010-10-10' MEMBER OF(j);
