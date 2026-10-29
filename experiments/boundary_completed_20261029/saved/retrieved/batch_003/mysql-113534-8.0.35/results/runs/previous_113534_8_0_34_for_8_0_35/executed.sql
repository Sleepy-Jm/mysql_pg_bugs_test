USE `replay_7d24125c45a622ec064841d1`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #113534; source anchors: cmain, c539367
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE `testa` (
  `id` bigint NOT NULL,
  `company_id` bigint DEFAULT NULL,
  `batch_no` bigint DEFAULT NULL,
  `picker` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_picker_query` (`company_id`,(cast(json_extract(`picker`,_utf8mb4'$[*].userName') as char(64) array)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `testb` (
  `id` bigint NOT NULL,
  `company_id` bigint DEFAULT NULL,
  `current_order_batch_no` bigint DEFAULT NULL,
  `history_order_batch_no` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx01_testb` (`company_id`,`current_order_batch_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;                                                                      
  
                                                                    
insert into testa values(1,48005,100,NULL);
insert into testa values(2,48005,101,'[]');
insert into testa values(3,48005,102,'[{"userId": "123456", "userName": "xiaoxu"}]');

insert into testb values(1,48005,101,NULL);
insert into testb values(2,48005,101,NULL);
insert into testb values(3,48005,102,'[123]');
insert into testb values(4,48005,102,'[124]');


select /*+ JOIN_PREFIX(ord, bat) */bat.id                     as batchPkId,        bat.batch_no,        ord.id,ord.history_order_batch_no as orderLevelHistoryBatchNo   from testa bat  inner join testb ord     on ord.current_order_batch_no = bat.batch_no  where bat.company_id = 48005 and ord.company_id=48005 and  bat.batch_no = 101;
select bat.id                     as batchPkId,        bat.batch_no,        ord.id,ord.history_order_batch_no as orderLevelHistoryBatchNo   from testa bat  inner join testb ord     on ord.current_order_batch_no = bat.batch_no  where bat.company_id = 48005 and ord.company_id=48005 and  bat.batch_no = 101;

-- Read-only evidence after the unchanged source SQL, same session.
SELECT * FROM testa FORCE INDEX(PRIMARY) ORDER BY id;
SELECT * FROM testb FORCE INDEX(PRIMARY) ORDER BY id;
EXPLAIN SELECT /*+ JOIN_PREFIX(ord, bat) */ bat.id AS batchPkId,bat.batch_no,ord.id,ord.history_order_batch_no AS orderLevelHistoryBatchNo FROM testa bat INNER JOIN testb ord ON ord.current_order_batch_no=bat.batch_no WHERE bat.company_id=48005 AND ord.company_id=48005 AND bat.batch_no=101;
EXPLAIN SELECT bat.id AS batchPkId,bat.batch_no,ord.id,ord.history_order_batch_no AS orderLevelHistoryBatchNo FROM testa bat INNER JOIN testb ord ON ord.current_order_batch_no=bat.batch_no WHERE bat.company_id=48005 AND ord.company_id=48005 AND bat.batch_no=101;
