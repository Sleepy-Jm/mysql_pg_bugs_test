-- 准备：创建一个带 ICU_RULES 的数据库（需在 template0 基础上，避免模板冲突）
-- 注意：CREATE DATABASE 不能在事务块内执行
CREATE DATABASE t3_db
  TEMPLATE template0
  LOCALE_PROVIDER icu
  ICU_LOCALE 'en'
  ICU_RULES '&z < a'
  LOCALE 'C'
  ENCODING 'UTF8';

-- 目标 SELECT：在 t3_db 中无显式 COLLATE 排序
\c t3_db
SELECT v FROM (VALUES ('a'), ('z'), ('m')) t(v) ORDER BY v;

-- 对照：目录字段
SELECT datname, datlocprovider, daticulocale, daticurules
FROM pg_database WHERE datname = 't3_db';

-- 清理（回到原库后删除）
\c postgres
DROP DATABASE t3_db;
