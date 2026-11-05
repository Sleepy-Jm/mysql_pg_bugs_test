-- MySQL report #113060; source: cmain, c537983, c538192
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE `t1` (
  `a` int(11) NOT NULL AUTO_INCREMENT,
  `b` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `c` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`a`),
  KEY `idx_b_l` (`b`),
  KEY `idx_c_l` (`c`)
);

insert into t1(b,c) values ('6RXmcRyA48c0yvZ2I' ,'6RXmcRyA48c0yvZ2I');
insert into t1(b,c) values ('G6UHU26b8dkvwpYiM' ,'G6UHU26b8dkvwpYiM');
insert into t1(b,c) values ('0XS2E55maqch' ,'0XS2E55maqch');
insert into t1(b,c) values ('0qwCMwobKYOcmLyfRXlagA8ukENJv' ,'0qwCMwobKYOcmLyfRXlagA8ukENJv');
insert into t1(b,c) values ('3avxIDL4YPrZVHie4rOiPrK8ZIJwEPqZaioHK' ,'3avxIDL4YPrZVHie4rOiPrK8ZIJwEPqZaioHK');
insert into t1(b,c) values ('5DHC2QScT6P6lXgRtHajXOfztB7ddjYH1LLUC3' ,'5DHC2QScT6P6lXgRtHajXOfztB7ddjYH1LLUC3');
insert into t1(b,c) values ('5pdGQ2NTM3c2uRgCg9NspSE' ,'5pdGQ2NTM3c2uRgCg9NspSE');
insert into t1(b,c) values ('6Bk06GVtwZaKqg01' ,'6Bk06GVtwZaKqg01');
insert into t1(b,c) values ('6VFO4xJPwvxGzReYzVj6dwTSIechnSSCyz9iY' ,'6VFO4xJPwvxGzReYzVj6dwTSIechnSSCyz9iY');
insert into t1(b,c) values ('6hLBs3Rnd5elLLVv1ip3A2U6G1dkIApKDkiCy' ,'6hLBs3Rnd5elLLVv1ip3A2U6G1dkIApKDkiCy');
SELECT AVG(DISTINCT b) FROM t1 FORCE INDEX(PRIMARY);
SHOW WARNINGS;
SELECT AVG(DISTINCT b) FROM t1;
SHOW WARNINGS;
SELECT SUM(DISTINCT b) FROM t1 FORCE INDEX(PRIMARY);
SHOW WARNINGS;
SELECT SUM(DISTINCT b) FROM t1;
SHOW WARNINGS;
