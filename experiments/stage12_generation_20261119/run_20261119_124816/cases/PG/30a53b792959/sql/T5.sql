-- 准备：合法规则 collation 作为对照
CREATE COLLATION t5_valid (provider = icu, locale = 'en', rules = '&z < a');

-- 目标 SELECT 1：非法规则应报错（未闭合的 & 关系）
-- 预期：ERROR，创建失败
CREATE COLLATION t5_invalid (provider = icu, locale = 'en', rules = '&z <');

-- 目标 SELECT 2：合法规则 collation 可正常使用
SELECT v FROM (VALUES ('a'), ('z')) t(v) ORDER BY v COLLATE t5_valid;

-- 对照：目录中只有合法 collation
SELECT collname, collicurules
FROM pg_collation
WHERE collname IN ('t5_valid', 't5_invalid')
ORDER BY collname;

-- 清理
DROP COLLATION t5_valid;
