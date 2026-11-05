-- MySQL report #113171; source: cmain, c538259, c544161
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT @@SESSION.sql_mode;
SELECT SUM(SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;
SELECT SUM(DISTINCT SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;
