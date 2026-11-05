-- MySQL report #112149; source: cmain, c535561
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT @@SESSION.sql_mode;
SELECT NULLIF(SPACE(5), CASE WHEN FALSE THEN ('P') ELSE ('i' || '~') END) AS c_4;
SHOW WARNINGS;
SELECT NULLIF(SPACE(5), ('i' || '~')) AS c_4;
SHOW WARNINGS;
