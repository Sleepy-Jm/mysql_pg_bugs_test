-- MySQL report #119572; source: cmain, c555362, c555363, c557880
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_trace=@@SESSION.optimizer_trace;
SET optimizer_trace="enabled=on";
CREATE TABLE t1 (dc2 DECIMAL(16,10));
INSERT INTO t1 VALUES (1.1111111111);

PREPARE s FROM 'SELECT dc2+? FROM t1';
SET @a=1.12345678901234;
EXECUTE s USING @a;

-- trigger reprepare
ALTER TABLE t1 COMMENT='force reprepare';

EXECUTE s USING @a;  -- crash here
