-- 准备：两个 ICU collation，同 locale，一个无规则，一个有规则
-- 规则 '&a < z' 使 z 排在 a 之后（在默认 en 排序中 z 本就在 a 之后，
-- 故改用 '&z < a' 使 a 排在 z 之后，产生可观察差异）
CREATE COLLATION t1_icu_plain (provider = icu, locale = 'en');
CREATE COLLATION t1_icu_rules (provider = icu, locale = 'en', rules = '&z < a');

-- 目标 SELECT：分别用两个 collation 排序
SELECT 'plain' AS which, v
FROM (VALUES ('a'), ('z'), ('m')) AS t(v)
ORDER BY v COLLATE t1_icu_plain;

SELECT 'rules' AS which, v
FROM (VALUES ('a'), ('z'), ('m')) AS t(v)
ORDER BY v COLLATE t1_icu_rules;

-- 对照：目录中规则字段
SELECT collname, colliculocale, collicurules
FROM pg_collation
WHERE collname IN ('t1_icu_plain', 't1_icu_rules')
ORDER BY collname;

-- 清理
DROP COLLATION t1_icu_plain;
DROP COLLATION t1_icu_rules;
