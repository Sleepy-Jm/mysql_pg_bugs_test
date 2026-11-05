-- MySQL report #111310; source: cmain, c533334, c533335
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
PREPARE p0 FROM 'WITH x(x) AS (SELECT 1 WHERE (SELECT 1, 3) = (SELECT 2, ?)) SELECT 1';
SET @a0 = CAST('2000-1-1 0:0:0' AS DATETIME);
EXECUTE p0 USING @a0;
