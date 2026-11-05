-- MySQL report #115207; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `so_do_order` (
  `id` bigint NOT NULL,
  `do_doc_no` varchar(50) NOT NULL,
  `order_doc_no` varchar(50) NOT NULL,
  `shop_code` varchar(50) NOT NULL,
  `other_vc_amt` decimal(15,6) NOT NULL,
  `total_actual_af_disc` decimal(15,6) NOT NULL,
  `status` int NOT NULL COMMENT '状态',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_do_doc_no` (`do_doc_no`),
  KEY `idx_order_doc_no` (`order_doc_no`),
  KEY `idx_create_time` (`create_time`),
  KEY `idx_so_do_order_1` (`shop_code`),
  KEY `idx_lmt01` (`last_modify_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `so_do_payment_info` (
  `id` bigint NOT NULL,
  `shop_code` varchar(50) NOT NULL,
  `order_doc_no` varchar(50) NOT NULL,
  `do_doc_no` varchar(50) DEFAULT NULL,
  `pay_actual` decimal(15,6) NOT NULL,
  `pay_type` bigint NOT NULL,
  `ro_doc_no` varchar(50) DEFAULT NULL,
  `status` int NOT NULL DEFAULT '1',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_modify_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_shopcode_1` (`shop_code`,`order_doc_no`,`status`),
  KEY `idx_shopcode_rodocno` (`shop_code`,`ro_doc_no`),
  KEY `idx_ct01` (`create_time`) USING BTREE,
  KEY `idx_lmt01` (`last_modify_time`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

explain
select sdpi.id*-1,sdpi.shop_code, sdpi.do_doc_no, sdpi.ro_doc_no, sdpi.order_doc_no, 47, sdo.other_vc_amt
from so_do_order sdo 
	inner join so_do_payment_info sdpi on sdo.shop_code = sdpi.shop_code and sdo.order_doc_no = sdpi.order_doc_no and sdo.do_doc_no = sdpi.do_doc_no and sdpi.pay_type = 3
	left join so_do_payment_info sdpi2 on sdo.shop_code = sdpi2.shop_code and sdo.order_doc_no = sdpi2.order_doc_no and sdo.do_doc_no = sdpi2.do_doc_no and sdpi.pay_type = 47
where sdo.status not in (30, 32) and sdo.other_vc_amt > 0 and sdo.total_actual_af_disc > sdpi.pay_actual and sdpi2.id is null;
