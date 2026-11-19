-- 准备：源 collation 带规则
CREATE COLLATION t2_src (provider = icu, locale = 'en', rules = '&z < a');

-- 目标 SELECT 1：FROM 继承，不指定 rules
CREATE COLLATION t2_inherit FROM t2_src;

-- 目标 SELECT 2：FROM 继承但显式覆盖 rules
CREATE COLLATION t2_override FROM t2_src (rules = '&a < z');

-- 对照：目录字段
SELECT collname, collicurules
FROM pg_collation
WHERE collname IN ('t2_src', 't2_inherit', 't2_override')
ORDER BY collname;

-- 行为对照：继承者应与源排序一致
SELECT 'src' AS which, v FROM (VALUES ('a'), ('z')) t(v)
ORDER BY v COLLATE t2_src;
SELECT 'inherit' AS which, v FROM (VALUES ('a'), ('z')) t(v)
ORDER BY v COLLATE t2_inherit;
SELECT 'override' AS which, v FROM (VALUES ('a'), ('z')) t(v)
ORDER BY v COLLATE t2_override;

-- 清理
DROP COLLATION t2_override;
DROP COLLATION t2_inherit;
DROP COLLATION t2_src;
