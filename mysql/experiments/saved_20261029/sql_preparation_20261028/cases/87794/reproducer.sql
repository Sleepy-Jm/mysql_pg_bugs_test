-- MySQL report #87794; source anchors: cmain, c464661
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE simpletable (value FLOAT);
INSERT INTO simpletable VALUES (1223484);
INSERT INTO simpletable VALUES (1223482);

SELECT * FROM simpletable WHERE value = 1223480;
SELECT * FROM simpletable WHERE value = 1223482;
SELECT * FROM simpletable WHERE value = 1223484;

SELECT value, value+0 FROM simpletable;
SELECT MIN(value), MAX(value) FROM simpletable;
