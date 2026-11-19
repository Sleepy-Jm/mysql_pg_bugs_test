-- 准备：带规则的模板数据库
CREATE DATABASE t4_tmpl
  TEMPLATE template0
  LOCALE_PROVIDER icu
  ICU_LOCALE 'en'
  ICU_RULES '&z < a'
  LOCALE 'C'
  ENCODING 'UTF8';

-- 目标 SELECT 1：不指定 ICU_RULES，应继承模板规则
CREATE DATABASE t4_inherit
  TEMPLATE t4_tmpl
  LOCALE_PROVIDER icu
  ICU_LOCALE 'en'
  LOCALE 'C'
  ENCODING 'UTF8';

-- 目标 SELECT 2：显式空串，应与不指定等价（NULL 按空串比较）
CREATE DATABASE t4_empty
  TEMPLATE t4_tmpl
  LOCALE_PROVIDER icu
  ICU_LOCALE 'en'
  ICU_RULES ''
  LOCALE 'C'
  ENCODING 'UTF8';

-- 对照：目录字段
SELECT datname, daticurules
FROM pg_database
WHERE datname IN ('t4_tmpl', 't4_inherit', 't4_empty')
ORDER BY datname;

-- 清理
DROP DATABASE t4_inherit;
DROP DATABASE t4_empty;
DROP DATABASE t4_tmpl;
