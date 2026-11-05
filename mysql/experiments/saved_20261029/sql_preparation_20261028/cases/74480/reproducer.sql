-- MySQL report #74480; source anchors: cmain, c421771, c435063
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
create table t1(f1 INT,f2 INT,f3 CHAR (10),primary key(f1,f2)) partition by range(f1) subpartition by hash(f2) subpartitions 2 (partition p1 values less than (0),partition p2 values less than (2),partition p3 values less than (2147483647));
RENAME TABLE t1 TO `t2_new..............................................end`;
SELECT 1 AS server_alive;
