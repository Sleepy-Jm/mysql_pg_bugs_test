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
