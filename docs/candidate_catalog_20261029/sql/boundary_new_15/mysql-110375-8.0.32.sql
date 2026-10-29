SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SHOW WARNINGS;
