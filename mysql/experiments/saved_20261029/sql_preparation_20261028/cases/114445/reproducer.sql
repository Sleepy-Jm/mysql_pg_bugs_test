-- MySQL report #114445; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SELECT _binary 'a' COLLATE `binary`;
CREATE TABLE t0(c0 VARCHAR(32) AS (_binary 'a' COLLATE `binary`));
SHOW CREATE TABLE t0;
