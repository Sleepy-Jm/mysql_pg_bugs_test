-- MySQL report #80681; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET @@session.tmp_table_size =4294967295;
create TABLE t1(a varchar(334)character set utf16 key);
INSERT INTO t1 VALUES(1),(2),(3),(4),(5),(6), (7),(8),(9),(10),(11),(12),(13),(14),(15),(16),(17),(18),(19),(20);
UPDATE t1 AS ta1,t1 AS ta2 SET ta1.a='aaaaaaaaaaaaaaaa';
