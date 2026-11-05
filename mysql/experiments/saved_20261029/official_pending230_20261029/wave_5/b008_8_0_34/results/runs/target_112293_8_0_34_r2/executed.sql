USE `replay_d76e96ac65130d713e51cbb1`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
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

-- Read-only evidence after the unchanged source SQL, same session.
SELECT HEX(b) AS stored_hex FROM t ORDER BY a;
SELECT @@session.internal_tmp_mem_storage_engine;
