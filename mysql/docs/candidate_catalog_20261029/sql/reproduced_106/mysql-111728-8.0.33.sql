-- Report #111728; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE ta(id BIGINT,PRIMARY KEY(id));
INSERT INTO ta(id) VALUES(1801425248110076165);
CREATE TABLE tb(value VARCHAR(50));
INSERT INTO tb(value) VALUES("1801425248110076222");
SELECT value FROM tb WHERE value IN(SELECT id FROM ta);
SELECT value FROM tb WHERE value IN(SELECT /*+no_index(ta)*/ id FROM ta);
