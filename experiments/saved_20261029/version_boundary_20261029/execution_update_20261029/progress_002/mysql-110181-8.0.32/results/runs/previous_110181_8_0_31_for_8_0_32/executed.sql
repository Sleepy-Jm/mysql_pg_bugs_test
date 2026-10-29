USE `replay_1ea87e4d0e3690c06cc7a05b`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- MySQL report #110181; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION tmp_table_size=51200;
SELECT @@session.tmp_table_size;
SELECT * FROM information_schema.APPLICABLE_ROLES;
SELECT * FROM information_schema.ADMINISTRABLE_ROLE_AUTHORIZATIONS;
SELECT * FROM information_schema.ROLE_TABLE_GRANTS;
SET SESSION tmp_table_size=16777216;
SELECT * FROM information_schema.APPLICABLE_ROLES;
SELECT * FROM information_schema.ADMINISTRABLE_ROLE_AUTHORIZATIONS;
SELECT * FROM information_schema.ROLE_TABLE_GRANTS;

-- Read-only postcheck appended after unchanged source SQL.
SELECT @@session.tmp_table_size AS final_tmp_table_size;
