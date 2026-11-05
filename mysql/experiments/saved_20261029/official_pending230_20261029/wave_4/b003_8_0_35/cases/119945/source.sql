-- Report #119945; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_mode=@@session.sql_mode;
SET SQL_MODE='';

DROP TABLE IF EXISTS `t3`;

CREATE TABLE `t3` (
  `c13` mediumblob,
  `c1` tinyint DEFAULT NULL,
  `c2` date DEFAULT NULL,
  `c3` time(6) DEFAULT NULL,
  `c4` datetime(4) DEFAULT NULL,
  `c5` timestamp NOT NULL,
  `c6` year DEFAULT NULL,
  `c7` varchar(159) DEFAULT NULL,
  `c8` varbinary(19),
  `c9` tinyblob,
  `vc1` tinyint GENERATED ALWAYS AS (`c2`) STORED,
  `vc2` datetime(4) GENERATED ALWAYS AS (ifnull(`c5`,NULL)) VIRTUAL,
  `c12` double DEFAULT NULL,
  KEY `i1` ((char_length(`c2`))),
  KEY `i4` (`c3`,((`c1` % 100)) DESC,`c12`) USING BTREE
) engine=innodb DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci STATS_PERSISTENT=0 ROW_FORMAT=DYNAMIC
/*!50100 PARTITION BY KEY (c3,c1)
PARTITIONS 16*/;

INSERT INTO `t3` (`c13`, `c1`, `c2`, `c3`, `c4`, `c5`, `c6`, `c7`, `c8`, `c9`, `c12`) VALUES 
(_binary '.',48,'1997-11-13','10:15:32.000000','2035-03-09 09:20:30.0000','1976-12-31 11:40:33',2010,NULL,_binary 'Q',_binary '.iKDu}%MT.C.@+~W]8&nY&sQf@h}u3',2718911),
(_binary '`jvW',127,NULL,'04:59:46.000000','2033-09-17 00:40:50.0000','2018-08-25 04:59:54',NULL,'k>]$o<!q+e6Y2(~H&[}',_binary 'BpZO$bmsr7[{dtnfvkY',_binary 'W',1.3502190828944468e308),
(_binary '~+#@Yh%@^F-1f@s.`Sy9#^j1qiU!2tijz@LEg$Z<zR$G17j.}7`-J_EXx1lJHot~EN*A@53V.HCaF6L[O5L0R<{.y_S5',-8,'2013-11-25','07:06:22.000000','1992-09-17 03:17:47.0000','1980-07-24 07:30:00',1974,'H',_binary 'INL>nx`gP_mL%[UE*R@',_binary 'A0|hnI$A0yNUc555j|f)FNbIv,YC>ka`9`p&J15x!mN~hMpxZh1$HJGF<]^HtP~?8ld8l<N<S*Hfap`#2}.]|r0QKwT-',2.9097653110417406e38),
(_binary 'B',127,'1992-01-12','09:47:13.000000','1993-07-29 18:46:28.0000','2014-03-18 12:45:22',2009,'H',_binary 'aG7euLszj%Z{7wH_a8u',NULL,24595),
(_binary '4',6,'2024-08-07','18:39:00.000000','2000-04-13 23:33:00.0000','2019-09-14 15:22:28',1999,'^[!M,~>xOn975}sM=^r[?qpQHZkcMW(~{u7!iP{4@a`Q]Q?y_)vj>2n~kIRFE2sZjTN|@-X&YOBP5h(XXzKfproQtZUR',_binary '1#8|x?U-tNRn6swj_Pb',_binary '^*fg',-126);

-- Execute the query first time:
SELECT t3.c8 AS ca1, ta1.vc2 AS ca2, t3.c1 AS ca3 FROM t3 NATURAL JOIN t3 AS ta1;


SELECT t3.c8 AS ca1,ta1.vc2 AS ca2,t3.c1 AS ca3 FROM t3 NATURAL JOIN t3 AS ta1;
DROP INDEX i4 ON t3;
SELECT t3.c8 AS ca1,ta1.vc2 AS ca2,t3.c1 AS ca3 FROM t3 NATURAL JOIN t3 AS ta1;
SELECT t3.c8 AS ca1,ta1.vc2 AS ca2,t3.c1 AS ca3 FROM t3 NATURAL JOIN t3 AS ta1;
