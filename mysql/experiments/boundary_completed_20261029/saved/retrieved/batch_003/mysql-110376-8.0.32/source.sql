SET NAMES utf8mb4;
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
