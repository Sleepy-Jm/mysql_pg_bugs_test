USE `replay_127650c23c60f891f69fffad`;
SET time_zone="+00:00";
SELECT @@sql_mode AS __preflight_sql_mode,@@character_set_client AS __preflight_charset_client,@@character_set_connection AS __preflight_charset_connection,@@collation_connection AS __preflight_collation,@@time_zone AS __preflight_time_zone,@@div_precision_increment AS __preflight_div_precision,@@auto_increment_increment AS __preflight_autoincrement,@@auto_increment_offset AS __preflight_offset;
-- Report #113097; source anchors: cmain, c538086, c553120, c553157
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_optimizer=@@session.optimizer_switch;
CREATE TABLE temp (createdAt datetime, timezone varchar(64));

INSERT INTO temp VALUES ('2022-02-15 16:47:12', null);

SELECT
  *
FROM
  (
    SELECT
      coalesce(timezone, '+00:00') tz,
      convert_tz(createdAt, '+00:00', (select tz)) ca,
      if(createdAt, if((select 1) = 1, 1, 1), 1) random
    FROM temp
  ) aux
   WHERE ca = '2022-02-15 16:47:12';
SET SESSION optimizer_switch='derived_condition_pushdown=off';
SELECT
  *
FROM
  (
    SELECT
      coalesce(timezone, '+00:00') tz,
      convert_tz(createdAt, '+00:00', (select tz)) ca,
      if(createdAt, if((select 1) = 1, 1, 1), 1) random
    FROM temp
  ) aux
   WHERE ca = '2022-02-15 16:47:12';

-- Read-only postchecks for report 113097; run in the same disposable schema/session.
SELECT createdAt,timezone FROM temp; SELECT CONVERT_TZ('2022-02-15 16:47:12','+00:00','+00:00') AS fixed_offset_control; SELECT @case_optimizer;
