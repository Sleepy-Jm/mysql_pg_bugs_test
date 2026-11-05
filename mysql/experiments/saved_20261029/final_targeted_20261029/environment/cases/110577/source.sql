-- Source cmain; remove optional SHOW CREATE after expected DDL failure.
SELECT CAST(1985 AS YEAR);
CREATE TABLE t5(c1 YEAR AS(CAST(1985 AS YEAR)));
