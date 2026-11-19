## T1
依据：`DefineCollation()` 解析 `rules` 并写入 `pg_collation.collicurules`，`make_icu_collator()` 在 `icurules != NULL` 时走 `ucol_openRules()` 分支。本测试用同一 locale 下“无规则 vs 有规则”两个 ICU collation 对同一组字符串排序，验证规则确实改变排序结果，且无规则 collation 保持基线。与其他测试的差异：这是最直接的“规则是否生效”对照，不涉及继承、数据库默认或错误路径。

```sql
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
```

预期结果：`t1_icu_plain` 排序为 `a, m, z`（en 默认顺序）；`t1_icu_rules` 因 `&z < a` 使 a 排在 z 之后，预期为 `m, z, a`（m 与 z 的相对顺序由 en 默认决定，a 被移到 z 之后）。目录对照中 `t1_icu_plain.collicurules` 为 NULL，`t1_icu_rules.collicurules` 为 `&z < a`。仍需以后验证：ICU 版本对 `&z < a` 的具体解析（是否影响 m 与 z 的相对位置），以及 `ucol_openRules()` 是否完整保留 en locale 的默认属性。

## T2
依据：`DefineCollation()` 的 `FROM` 分支从源 collation 复制 `collicurules`（`SysCacheGetAttr(COLLOID, ..., Anum_pg_collation_collicurules, ...)`）。本测试验证 `CREATE COLLATION ... FROM` 继承规则，并验证显式 `RULES` 覆盖继承值。与其他测试的差异：聚焦继承路径与覆盖边界，而非直接创建。

```sql
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
```

预期结果：`t2_inherit.collicurules` 等于 `&z < a`，`t2_override.collicurules` 等于 `&a < z`。`t2_src` 与 `t2_inherit` 排序均为 `z, a`（a 被移到 z 之后）；`t2_override` 排序为 `a, z`（a 在 z 之前，与 en 默认一致，规则不改变顺序）。仍需以后验证：`FROM` 与显式 `RULES` 同时出现时覆盖语义是否如源码所示（`rulesEl` 优先），以及继承时 locale 是否也一并复制。

## T3
依据：`createdb()` 解析 `icu_rules` 并写入 `pg_database.daticurules`；`CheckMyDatabase()` 在 `datlocprovider == COLLPROVIDER_ICU` 时读取并传给 `make_icu_collator()`。本测试验证数据库默认 ICU 规则影响无显式 `COLLATE` 的排序。与其他测试的差异：走数据库级默认 collation 路径，而非显式 collation 对象。

```sql
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
```

预期结果：`t3_db` 中 `ORDER BY v` 使用数据库默认 ICU collation 加规则 `&z < a`，预期排序为 `m, z, a`（a 被移到 z 之后）。目录中 `daticurules` 为 `&z < a`，`datlocprovider` 为 `i`（ICU）。仍需以后验证：`CheckMyDatabase()` 在连接时是否确实加载规则（而非延迟到首次比较），以及 `LOCALE 'C'` 与 `ICU_LOCALE 'en'` 组合下默认 collation 的实际选择。

## T4
依据：`createdb()` 中模板兼容性检查比较 `dbicurules` 与 `src_icurules`，NULL 按空串处理（约 L1111-L1135）；未指定时从模板继承 `src_icurules`（约 L1018-L1020）。本测试验证从带规则模板继承，以及 NULL 与空串在兼容性检查中等价。与其他测试的差异：聚焦模板继承与 NULL/空串等价边界。

```sql
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
```

预期结果：`t4_inherit.daticurules` 为 `&z < a`（继承）；`t4_empty.daticurules` 为 `''`（空串，显式指定）。两者创建均成功，因为兼容性检查将 NULL 与空串视为等价，故 `t4_empty` 不因与模板规则不同而报错。仍需以后验证：`t4_empty` 中空串规则是否在 `make_icu_collator()` 中进入 `ucol_openRules()` 分支并产生与无规则不同的行为（源码显示空串仍进入分支）。

## T5
依据：`make_icu_collator()` 中 `ucol_openRules()` 失败时 `if (U_FAILURE(status)) ERROR`；`DefineCollation()` 创建后调用 `pg_newlocale_from_collation(newoid)` 验证 locale 可加载。本测试验证非法规则字符串在 `CREATE COLLATION` 阶段报错，且合法规则与非法规则形成对照。与其他测试的差异：聚焦错误路径与验证时机，而非排序结果。

```sql
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
```

预期结果：`CREATE COLLATION t5_invalid` 报错（ICU 规则解析失败，`ucol_openRules()` 返回失败状态，`DefineCollation()` 中的 `pg_newlocale_from_collation()` 触发 ERROR），`t5_invalid` 不出现在目录中。`t5_valid` 排序为 `z, a`。目录对照仅返回 `t5_valid` 一行。仍需以后验证：错误是否确实在 `CREATE COLLATION` 阶段触发（而非延迟到首次使用），取决于 `lc_collate_is_c()`/`lc_ctype_is_c()` 对 ICU collation 的返回值；以及具体错误消息内容。

---

说明：以上五个测试分别覆盖（T1）规则生效对照、（T2）`FROM` 继承与覆盖、（T3）数据库默认规则、（T4）模板继承与 NULL/空串等价、（T5）非法规则错误路径，均有源码依据且操作数关系或执行分支不同。T3/T4 涉及 `CREATE DATABASE`，需在非事务上下文中执行且依赖 `template0` 可用；T3 使用 `\c` 切换连接，若测试框架不支持元命令，需改为在目标库中单独执行目标 SELECT。所有预期值基于 SQL 与 ICU 规则语义推导，未执行验证；ICU 版本对规则解析的具体影响、`ucol_getRules()` 返回串的 NUL 终止性、空串规则的实际行为、以及验证触发时机仍需以后用独立 ICU oracle 或实际执行确认。