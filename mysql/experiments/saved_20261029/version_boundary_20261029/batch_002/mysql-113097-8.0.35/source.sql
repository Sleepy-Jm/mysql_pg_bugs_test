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
