USE `replay_fb1ba600c49eee8b1aec2d4b`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #115380; source: cmain, c544466
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t15( id int ,  cc int ,m varchar(8) COLLATE utf8mb4_bin DEFAULT NULL, t text, PRIMARY key(id) ,key(cc), key(m) )  PARTITION BY RANGE  COLUMNS(id) (PARTITION p202008 VALUES LESS THAN (5) ENGINE = InnoDB,
 PARTITION p202009 VALUES LESS THAN (10) ENGINE = InnoDB,
 PARTITION p202012 VALUES LESS THAN (100) ENGINE = InnoDB) ;
 
create table t2( id int  PRIMARY key , cc int  );
insert into t2 values ( 1 , 2);
insert into t2  values (0, 2 );

INSERT INTO `t15` VALUES (4,1,'123','abcdef'),
                         (5,1,'123','abcdef'),
                         (8,2,'122','abcdef'),
                         (9,2,'122','abcdef');


SELECT DISTINCT a.id FROM t15 a,t2 b WHERE b.id<>a.id AND a.cc=1 AND a.m='123';
EXPLAIN UPDATE t15 a,t2 b SET a.t='test' WHERE b.id<>a.id AND a.cc=1 AND a.m='123';
UPDATE t15 a,t2 b SET a.t='test' WHERE b.id<>a.id AND a.cc=1 AND a.m='123';
SELECT id,t FROM t15 ORDER BY id;

-- Read-only postchecks for report 115380; run in the same disposable schema/session.
SELECT id,cc,m,t FROM t15 ORDER BY id; SELECT * FROM t2 ORDER BY id;
