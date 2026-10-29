USE `replay_5a0493350d82ee89a1553593`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113211; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `tb1` (
  `double_col` double DEFAULT NULL,
  `bit_col` bit(8) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb2` (
  `double_col` double DEFAULT NULL,
  `bit_col` bit(8) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb3` (
  `double_col` double DEFAULT NULL,
  `bit_col` bit(8) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into tb1(bit_col) values(0x00),(0xFF),(0xF0),(0xAA),(0x99);
insert into tb2(bit_col) values(0x00),(0xFF),(0xF0),(0xAA),(0x99);
insert into tb3(bit_col) values(0x00),(0xFF),(0xF0),(0xAA),(0x99);
SELECT B.bit_col, B.double_col, (B.double_col, B.bit_col) <=> (SELECT double_col, bit_col FROM tb3 D WHERE D.bit_col NOT BETWEEN true AND D.double_col OR B.bit_col > D.double_col ORDER BY 1,2  LIMIT 1) FROM tb1 A JOIN tb2 B GROUP BY 1,2 ORDER BY 1,2;
SELECT double_col,HEX(bit_col) FROM tb3 D WHERE D.bit_col NOT BETWEEN TRUE AND D.double_col ORDER BY 1,2 LIMIT 1;
SELECT (NULL,b'00000000') <=> (NULL,b'00000000');

-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb1; SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb2; SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb3;
