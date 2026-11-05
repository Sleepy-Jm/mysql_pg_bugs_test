-- MySQL report #112242; source: cmain, c535808
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t0(c0 INT);
INSERT INTO t0(c0) VALUES(1);
CREATE INDEX i0 USING HASH ON t0(c0) INVISIBLE;

SET SESSION optimizer_switch = 'use_invisible_indexes=off';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0); -- {}
SET SESSION optimizer_switch = 'use_invisible_indexes=on';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0);
