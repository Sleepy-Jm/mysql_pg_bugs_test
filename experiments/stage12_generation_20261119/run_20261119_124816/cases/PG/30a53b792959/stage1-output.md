# PostgreSQL 提交分析 · Stage 1

## 结论摘要

该提交为 ICU collation 增加两类可持久化的自定义排序规则：

- `pg_collation.collicurules`：由 `CREATE COLLATION ... RULES '...'` 写入；
- `pg_database.daticurules`：由 `CREATE DATABASE ... ICU_RULES '...'` 或 `createdb/initdb --icu-rules` 写入。

运行期，当 ICU collation 的 `collicurules` 非空，或数据库默认 collation 的 `daticurules` 非空时，`make_icu_collator()` 会先取得该 locale 的默认 ICU 规则，再附加用户规则，最后用 `ucol_openRules()` 重新构造 collator。因此查询正确性测试的重心应放在：

1. 带 `rules` 的 ICU collation 是否真的按 ICU 规则改变排序/比较/唯一性；
2. 数据库 ICU 默认规则是否影响默认排序；
3. 规则在创建、继承、转储恢复、错误处理中的可观察行为。

---

## 1. 哪些 SQL 构造可能进入改动路径？

下面只列出有源码证据支撑的入口，含文件、函数和行号（目标版本行号，约数）。

### 1.1 `CREATE COLLATION ... (provider = icu, locale = ..., rules = ...)`

**代码入口：**

- `src/backend/commands/collationcmds.c`
  - `DefineCollation()`：
    - 解析 `rules` 选项：`strcmp(defel->defname, "rules") == 0`（约 L101-L103）
    - 从参数提取规则：`if (rulesEl) collicurules = defGetString(rulesEl);`（约 L202-L204）
    - 调用 `CollationCreate()` 并传入 `collicurules`（约 L311-L317）
    - 创建后验证 locale 可加载：`pg_newlocale_from_collation(newoid)`（约 L320-L333）
- `src/backend/catalog/pg_collation.c`
  - `CollationCreate()`：
    - 写入 `pg_collation.collicurules`（约 L195-L200）
- `src/backend/utils/adt/pg_locale.c`
  - `pg_newlocale_from_collation()`：
    - 仅当 `collprovider == COLLPROVIDER_ICU` 时读取 `pg_collation.collicurules`（约 L1639-L1655）
  - `make_icu_collator()`：
    - 当 `icurules != NULL` 时附加规则并调用 `ucol_openRules()`（约 L1423-L1480）

**进入分支的条件：**

- `provider` 必须为 `icu`，即 `collprovider == COLLPROVIDER_ICU`；
- 创建时显式给出非空 `RULES`；
- 或者 `CREATE COLLATION ... FROM existing_collation` 时继承源 collation 的非空 `collicurules`。

### 1.2 `CREATE COLLATION ... FROM existing_collation`

**代码入口：**

- `src/backend/commands/collationcmds.c`
  - `DefineCollation()` 的 `FROM` 分支：
    - 从系统目录复制 `collicurules`（约 L165-L175）：

```c
datum = SysCacheGetAttr(COLLOID, tp, Anum_pg_collation_collicurules, &isnull);
if (!isnull)
    collicurules = TextDatumGetCString(datum);
else
    collicurules = NULL;
```

**进入分支条件：**

- 源 collation 是 ICU provider，并且其 `collicurules` 非空；
- 如果同时显式给出 `RULES`，则可能覆盖继承值（这是需要测试的边界）。

### 1.3 `CREATE DATABASE ... LOCALE_PROVIDER = icu ... ICU_RULES = ...`

**代码入口：**

- `src/backend/commands/dbcommands.c`
  - `createdb()`：
    - 解析 `icu_rules` 选项：`strcmp(defel->defname, "icu_rules") == 0`（约 L779-L784）
    - 提取 `dbicurules = defGetString(dicurules)`（约 L903-L908）
    - 未指定时从模板数据库继承：`if (dbicurules == NULL && dblocprovider == COLLPROVIDER_ICU) dbicurules = src_icurules;`（约 L1018-L1020）
    - 模板兼容性检查：比较 `dbicurules` 与 `src_icurules`，NULL 按空串处理（约 L1111-L1135）
    - 写入 `pg_database.daticurules`（约 L1343-L1348）
- `src/backend/utils/init/postinit.c`
  - `CheckMyDatabase()`：
    - 当 `dbform->datlocprovider == COLLPROVIDER_ICU` 时读取 `daticurules` 并调用 `make_icu_collator()`（约 L421-L437）

**进入分支条件：**

- 新建数据库 locale provider 为 ICU；
- 显式指定 `ICU_RULES`，且非空；
- 或从模板数据库继承了非空 `daticurules`；
- 之后每次连接到该数据库时都会加载规则。

### 1.4 `createdb --icu-rules='...'`

**代码入口：**

- `src/bin/scripts/createdb.c`
  - `main()`：
    - 增加命令行选项 `--icu-rules`（约 L41-L44、L68-L72、L136-L141）
    - 生成 SQL：`ICU_RULES '...'`（约 L236-L241）

该 SQL 随后进入 `createdb()`，路径同 1.3。

### 1.5 `initdb --icu-rules='...'`

**代码入口：**

- `src/bin/initdb/initdb.c`
  - `main()`：
    - 增加 `--icu-rules` 选项（约 L2772-L2775、L2930-L2939）
    - 校验规则仅能与 ICU provider 一起使用（约 L2963-L2967）
  - `bootstrap_template1()`：
    - 替换 `template1` 的 `ICU_RULES` token（约 L1313-L1319）

该路径影响集群初始化后的模板数据库默认规则，不属于纯 SQL 查询路径，但对后续数据库默认排序有影响。

### 1.6 `pg_dump` / restore

**代码入口：**

- `src/bin/pg_dump/pg_dump.c`
  - `dumpDatabase()`：
    - 查询 `daticurules`（约 L2889-L2892、L2904-L2910）
    - 生成 `CREATE DATABASE ... ICU_RULES = '...'`（约 L3001-L3006）
  - `dumpCollation()`：
    - 查询 `collicurules`（约 L13212-L13216、L13233）
    - 生成 `CREATE COLLATION ... rules = '...'`（约 L13302-L13307）

恢复时执行这些 DDL，重新进入 1.1/1.3 的创建路径。

### 1.7 `psql` 描述命令

**代码入口：**

- `src/bin/psql/describe.c`
  - `listAllDbs()`：
    - 数据库列表增加 `ICU Rules` 列（约 L923-L1000）
  - `listCollations()`：
    - collation 列表增加 `ICU Rules` 列（约 L4849-L4920）

这些只影响显示结果，不改变排序语义，但可用于目录验证。

### 1.8 使用带规则 collation 的排序/比较查询

**代码入口：**

- 通用执行器比较路径最终调用 collation 支持函数，后者通过 `pg_newlocale_from_collation()` 获取 collator。
- 本次提交没有修改排序执行器代码，但带规则的 collation 会改变 collator 输出，因此以下 SQL 构造在“显式或隐式使用带规则 ICU collation”时会进入改动路径：
  - `ORDER BY ... COLLATE "rules_collation"`
  - `WHERE col = '...' COLLATE "rules_collation"`，`<`, `>`, `BETWEEN`, `LIKE`
  - `GROUP BY`、`DISTINCT`、`UNION` / `INTERSECT` / `EXCEPT`
  - `CREATE UNIQUE INDEX ... (col COLLATE "rules_collation")`
  - `CREATE TABLE ... (col text COLLATE "rules_collation")`
  - 表达式索引、排他约束、`CHECK` 约束中的字符串比较

**进入分支条件：** 被使用的 collation 必须是 ICU provider 且其 `collicurules` 非空。

---

## 2. 到达后，哪些输入性质可能影响查询的可观察结果？

### 2.1 源码直接支持的关系

这些是代码明确表达的行为，可以作为测试假设：

| 输入性质 | 源码证据 | 可观察结果 |
|---|---|---|
| `collicurules` 非 NULL | `pg_locale.c` `make_icu_collator()` 中 `if (icurules)` 分支 | 只有非空规则才改变 collation 行为 |
| 规则字符串内容 | `ucol_getRules()` + `u_strcat()` 拼接用户规则，再 `ucol_openRules()` | 排序、比较、索引唯一性等受 ICU 规则影响 |
| locale ID | 初始 `ucol_open(iculocstr)` | 默认规则来自该 locale，决定基线排序 |
| 规则字符串必须有效 UTF-8 且无 NUL | `icu_to_uchar(&my_rules, icurules, strlen(icurules))` | 非法 UTF-8 或内嵌 NUL 可能导致截断/错误 |
| `ucol_openRules()` 失败 | `make_icu_collator()` 中 `if (U_FAILURE(status))` ERROR | 非法 ICU 规则导致创建 collation 失败，或数据库连接失败 |
| `dbicurules` 与模板 `src_icurules` 比较 | `dbcommands.c` 中 NULL 替换为 `""` 后比较 | NULL 和空字符串在模板兼容性检查中等价 |
| `daticurules` 非 NULL（含空串） | `CheckMyDatabase()` 读取后传给 `make_icu_collator()` | 空字符串仍会进入规则分支，可能触发 `ucol_openRules()` |
| `provider = libc` 且给 `rules` | `DefineCollation()` 不拒绝，但 `pg_newlocale_from_collation()` 仅在 ICU 分支读取 | libc collation 可能存储规则但排序行为不变 |

### 2.2 尚待验证的推断

这些不是直接由本文代码证明，需要测试确认：

1. **规则叠加的真实语义**：注释说“extract rules of standard collation, add our own rules”，但 ICU 规则存在优先级、冲突、重置关系，简单拼接后的排序结果需要独立 ICU 验证。
2. **`u_strlen(default_rules)` 的安全性**：`ucol_getRules()` 返回长度 `length`，但代码忽略它并调用 `u_strlen(default_rules)`。如果返回的 UChar 串不保证 NUL 终止，可能读越界。
3. **ICU < 54 时属性保留**：旧 ICU 路径先 `ucol_open()` + `icu_set_collation_attributes()`，随后又 `ucol_openRules()`。重新构造时某些 locale 属性可能丢失。
4. **空规则字符串效果**：`icurules=""` 会进入分支，但 `my_rules` 长度为 0，最终 `ucol_openRules()` 产生的 collator 是否与原始 `ucol_open()` 完全一致，尚需验证。
5. **非 ICU provider 的规则处理**：源码未禁止 `CREATE COLLATION ... provider=libc, rules='...'`，但运行时不会读取。它应该报错还是静默忽略，没有源码证据。
6. **`CREATE COLLATION` 验证是否总是触发**：`DefineCollation()` 调用 `pg_newlocale_from_collation()` 位于 `if (!lc_collate_is_c(newoid) || !lc_ctype_is_c(newoid))` 内。对于 ICU collation，该条件是否一定为真，需要验证；否则非法规则可能延迟到首次使用才报错。
7. **规则字符串编码交互**：规则字符串来自 SQL，受数据库编码和 ICU 转换影响；非 ASCII 规则或代理对的行为需要测试。
8. **pg_dump/restore 正确性**：虽然 pg_dump 会输出新选项，但恢复后的排序结果是否一致，需要与原始库比较。
9. **模板继承边界**：`CREATE DATABASE ... TEMPLATE = icu_template` 不指定 `ICU_RULES` 时继承，指定空串时是否与不指定等价，需要验证。

### 2.3 能够区分源码直接支持与推断的对照

- **同 locale 无规则 vs 有规则 collation**  
  创建两个 ICU collation，一个无 `rules`，一个有 `rules`，对同一组字符串排序。如果只有后者与基线不同，且差异方向符合独立 ICU 规则，则支持实现正确。

- **独立 ICU 库作为 oracle**  
  用相同 locale + rules 在独立 ICU 客户端中构造 collator，与 PostgreSQL 的 `ORDER BY COLLATE` 结果比较。这可以区分“规则本身的效果”与“PostgreSQL 实现是否正确”。

- **NULL vs 空字符串规则**  
  比较 `pg_collation.collicurules NULL`、`''`、`'&a < b'` 的目录值和排序行为；再比较 `CREATE DATABASE` 兼容性检查。

- **libc vs ICU provider 带 rules**  
  创建 libc collation with rules 与无 rules 对照；如果排序无变化但目录有规则，说明规则被忽略；如果期望报错，则当前实现可能有缺陷。

- **合法规则 vs 非法规则**  
  合法规则应成功创建并影响排序；非法规则应在 `CREATE COLLATION` 阶段或数据库连接阶段失败。失败时机是源码直接支持的，但具体错误信息需要验证。

- **转储恢复前后对照**  
  对带规则 collation 和数据库执行 `pg_dump`，再恢复到新库，比较 `pg_collation/pg_database` 目录字段和排序结果。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 独立验证方法

1. **使用独立 ICU 库构建预期结果**  
   由于本提交的核心行为是通过 ICU 的 `ucol_getRules()` + `ucol_openRules()` 构造 collator，可以用独立 ICU 客户端（PyICU、C/C++ ICU 程序）对相同 locale + rules 生成排序键或比较结果，作为 PostgreSQL 查询结果的 oracle。  
   注意：必须使用与 PostgreSQL 构建时相同的 ICU 版本。

2. **目录值验证**  
   直接查询 `pg_collation`（`colliculocale`, `collicurules`）和 `pg_database`（`daticulocale`, `daticurules`），确认 DDL 参数被完整存储。  
   对于 psql `\l` 和 `\dO+`，可以检查其显示的 ICU Rules 列是否与实际目录一致。

3. **排序/比较行为验证**  
   对一组精心选择的字符串（包含规则涉及的字符、重音、大小写、标点、数字、组合字符等）执行 `ORDER BY ... COLLATE ...`，与独立 ICU oracle 比较。  
   同时覆盖 `WHERE` 范围过滤、`UNIQUE` 索引去重、`GROUP BY` 分组等。

4. **错误路径验证**  
   使用非法 ICU 规则字符串，确认 PostgreSQL 在 `CREATE COLLATION` 或连接数据库时失败，并检查错误信息是否包含 locale 和 rules。  
   与独立 ICU 对非法规则的错误结果对照。

5. **回归对照**  
   在第一父版本（无 `collicurules/daticurules` 支持）上，对相同 locale 无规则 collation 执行同一组查询；在目标版本上无规则 collation 应产生相同结果。  
   这可以证明新功能没有破坏既有行为，但本身不足以证明新功能正确。

6. **数据库默认 collation 验证**  
   对具有 `daticurules` 的 ICU 数据库执行无显式 `COLLATE` 的排序操作，与独立 ICU oracle 对相同 locale + rules 的结果比对。  
   同时比较无规则 ICU 数据库和有规则 ICU 数据库的默认排序差异。

### 3.2 仍缺少的证据

- **没有提供预期排序结果集**：需要依赖 ICU 文档或独立 ICU 客户端生成预期，无法仅凭提交代码判断某个规则字符串应该产生什么顺序。
- **没有给出 ICU 版本和构建配置**：不同 ICU 版本会改变默认规则和规则解析，缺少版本信息会降低测试可重复性。
- **没有验证 `ucol_getRules()` 返回 UChar 串是否 NUL 终止**：源码使用 `u_strlen(default_rules)`，如果长度混用可能导致越界，这是需要测试验证的潜在内存安全问题。
- **没有验证 `ucol_openRules()` 是否继承所有 locale 属性**：尤其是 ICU `< 54` 的兼容性分支。
- **没有规定非 ICU provider 配合 `rules` 的行为**：应报错还是忽略，源代码和提交说明均未明确。
- **没有明确空规则字符串是否应被视为与无规则等价**：`dbcommands.c` 将 NULL 和 `""` 视为等价，但 `make_icu_collator()` 仍会将空串传入规则分支，可能导致行为差异。
- **没有验证 `CREATE COLLATION` 的验证条件对 ICU collation 是否总是触发规则检查**：如果 `lc_collate_is_c()` 或 `lc_ctype_is_c()` 对 ICU collation 的返回导致跳过验证，非法规则可能延迟到首次使用才报错。
- **没有提供 pg_dump/restore 的完整闭环测试**：虽然代码路径存在，但未验证转储到老版本兼容性、跨版本恢复、以及恢复后排序行为的一致性。
- **没有测试包含非 ASCII 规则字符串或代理对字符的输入**：`icu_to_uchar()` 和 `strlen()` 的组合可能对特殊 Unicode 输入产生未知行为。

---

### 候选测试数量

基于上述证据，下一阶段可优先安排以下类别的候选测试：

1. `CREATE COLLATION` with `rules`（ICU provider）
2. `CREATE COLLATION FROM` 继承带规则 collation
3. `CREATE DATABASE` with `ICU_RULES`
4. `CREATE DATABASE` 从带规则模板继承/冲突校验
5. 使用带规则 collation 的排序/比较/唯一索引查询
6. 使用带 `daticurules` 的数据库默认排序
7. 非法规则字符串的错误路径
8. `pg_dump`/restore 后的目录与行为一致性
9. 非 ICU provider 与 `rules` 的交互
10. `createdb`/`initdb` 命令行入口（若测试环境包含客户端工具）

以上候选均有源码 diff 或提交说明中的明确证据支持，不需要额外假设。完整可执行 SQL 将在下一阶段给出。阶段 1 的核心结论是：**测试应围绕新字段的存储、加载和 ICU 规则的实际排序效果展开，路径被执行或两版结果不同不能单独证明正确性，必须与独立 ICU oracle 或目录语义进行对照。**