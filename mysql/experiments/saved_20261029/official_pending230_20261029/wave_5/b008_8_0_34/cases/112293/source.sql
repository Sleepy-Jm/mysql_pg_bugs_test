-- MySQL report #112293; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t` (
  `a` int(11) DEFAULT NULL,
  `b` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into t values(1,'my_test　'),(2,'my_test');
SELECT HEX(b),b FROM t;
SELECT b FROM t WHERE b='my_test';
set internal_tmp_mem_storage_engine = TempTable;
select b,count(*) from t group by b;
