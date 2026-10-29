-- MySQL report #111722; source: cmain, c534354
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
PREPARE p0 FROM 'CREATE VIEW x(x) AS (WITH y(y) AS (SELECT 1 WHERE ? = 1) SELECT 1)';
SET @a0 = TIME '15:19:32';
EXECUTE p0 USING @a0;
