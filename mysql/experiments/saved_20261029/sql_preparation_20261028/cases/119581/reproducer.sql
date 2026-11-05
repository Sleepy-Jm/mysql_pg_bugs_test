-- Report #119581; source anchors: cmain, c555368
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE test_floor(d DOUBLE);
INSERT INTO test_floor VALUES(9223372036854775808.0);
SELECT CAST(FLOOR(d) AS SIGNED) FROM test_floor;
SHOW WARNINGS;
SELECT CAST(FLOOR(9223372036854775808.0) AS SIGNED);
SHOW WARNINGS;
SELECT CAST(FLOOR(9223372036854775808.0e0) AS SIGNED);
SHOW WARNINGS;
