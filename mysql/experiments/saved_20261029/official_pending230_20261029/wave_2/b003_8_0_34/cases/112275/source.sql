-- MySQL report #112275; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TEMPORARY TABLE temp(id INTEGER,name VARCHAR(100));
CREATE TABLE normal(id INTEGER,name VARCHAR(100));
SHOW COLUMNS FROM temp;
SHOW COLUMNS FROM normal;
