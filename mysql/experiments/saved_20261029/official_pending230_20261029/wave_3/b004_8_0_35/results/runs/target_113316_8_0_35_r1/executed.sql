USE `replay_8dc6a3dae20da082686008f0`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #113316; source: cmain, c538619
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t0 (`int_col` int,`bit_col` bit(8) DEFAULT b'0', KEY `ndx_bit_col` (`bit_col` DESC)) partition by hash(int_col) partitions 3;

insert into t0(int_col) values(1);

SELECT bit_col, int_col FROM t0 A WHERE bit_col = '0x00';

alter table t0 drop key ndx_bit_col;

SELECT bit_col, int_col FROM t0 A WHERE bit_col = '0x00';

-- Read-only evidence after the unchanged source SQL, same session.
SHOW WARNINGS;
SELECT int_col,HEX(bit_col) AS stored_hex FROM t0;
