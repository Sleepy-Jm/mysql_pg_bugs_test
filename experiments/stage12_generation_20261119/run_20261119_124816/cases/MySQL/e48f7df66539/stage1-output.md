# MySQL 提交分析 · Stage 1

本提交的核心变化是：临时表行拷贝不再区分 `Item_field` 与其他 `Item`，统一走 `items_to_copy` / `copy_funcs()`；同时移除 `Temp_table_param::field_count`，字段计数并入 `func_count`。因此，所有需要把查询结果或中间结果写入临时表、且源表达式为字段的路径都可能进入改动路径。

---

## 1. 哪些 SQL 构造可能进入改动路径？

下面按证据强度排列。行号优先使用目标版本 `e48f7df6653…` 中的位置。

### 1.1 派生表 / CTE 物化

- **入口文件/函数**：`sql/sql_executor.cc`
  - `GetAccessPathForDerivedTable()`，约 L1515 附近，调用 `NewMaterializeAccessPath()`，`copy_items=true`。
- **执行文件/函数**：`sql/composite_iterators.cc`
  - `MaterializeIterator::MaterializeQueryBlock()`，L818–835，由 `copy_fields_and_funcs()` 改为 `copy_funcs()`。
- **SQL 形状**：
  - `SELECT ... FROM (SELECT ...) AS d`
  - `WITH ... AS (...) SELECT ...`
  - 需要物化派生表或 CTE 的场景（无法合并到外层查询时）。

### 1.2 UNION / 多查询块合并物化

- **入口文件/函数**：`sql/sql_union.cc`
  - `Query_expression::setup_materialization()`，L853 附近，设置 `query_block.copy_items = true`。
- **执行文件/函数**：同上 `MaterializeIterator::MaterializeQueryBlock()`。
- **SQL 形状**：
  - `SELECT ... UNION [ALL] SELECT ...`
  - 多个查询块被物化到临时表的场景。

### 1.3 半连接物化（semijoin materialization）

- **入口文件/函数**：`sql/sql_executor.cc`
  - `GetTableAccessPath()`，L1604 附近，使用 `sjm->table_param`，`copy_items_in_materialize=true`。
- **执行文件/函数**：同上 `MaterializeIterator::MaterializeQueryBlock()`。
- **SQL 形状**：
  - `SELECT ... WHERE outer_col IN (SELECT ... FROM t2 ...)`
  - 优化器选择半连接物化时。

### 1.4 聚合 DISTINCT 内部临时表

- **文件/函数**：`sql/item_sum.cc`
  - `Aggregator_distinct::add()`，L1229 附近：删除 `copy_fields(tmp_table_param, thd)`，仅保留 `copy_funcs(tmp_table_param, thd)`。
- **SQL 形状**：
  - `SELECT COUNT(DISTINCT col), SUM(DISTINCT col), AVG(DISTINCT col) FROM t`
  - 任何需要去重聚合参数的聚合函数。

### 1.5 `GROUP_CONCAT`

- **文件/函数**：`sql/item_sum.cc`
  - `Item_func_group_concat::add()`，L4265 附近：删除 `copy_fields()`，仅保留 `copy_funcs()`。
- **SQL 形状**：
  - `SELECT GROUP_CONCAT(col) FROM t`
  - `SELECT GROUP_CONCAT(DISTINCT col ORDER BY col2) FROM t`

### 1.6 窗口函数

- **文件/函数**：
  - `sql/window_iterators.cc`
    - `bring_back_frame_row()`，L491–492：从 `copy_fields(out_param)` 改为 `copy_funcs(out_param, CFT_FIELDS)`。
    - `WindowIterator::Read()`，L1568 附近：从 `copy_fields_and_funcs(..., CFT_HAS_NO_WF)` 改为 `copy_funcs(..., CFT_HAS_NO_WF)`。
    - `BufferingWindowIterator::Read()`，L1677 附近：同上。
  - `sql/sql_tmp_table.cc`
    - `create_tmp_table()`，L1479–1497：新增 `from_item` 数组，非窗口临时表只填充 `items_to_copy`；窗口临时表同时保留 `copy_fields`。
- **SQL 形状**：
  - `SELECT ... OVER (PARTITION BY ... ORDER BY ...) FROM t`
  - 带窗口帧、`NTH_VALUE`、`LEAD/LAG` 等需要回填字段的窗口函数。

### 1.7 `GROUP BY` 临时表聚合

- **文件/函数**：
  - `sql/composite_iterators.cc`
    - `TemptableAggregateIterator::Init()`，L1041 附近：从 `copy_fields()` 改为 `copy_funcs(..., CFT_FIELDS)`。
  - `sql/sql_select.cc`
    - `count_field_types()`：删除 `field_count` 计数，字段和参数统一计入 `func_count`。
    - `JOIN::make_tmp_tables_info()`，L4353 附近：清理和计数时不再单独维护 `field_count`。
  - `sql/sql_tmp_table.cc`
    - `create_tmp_table()`：字段复制列表从 `copy_fields` 改为 `items_to_copy`。
- **SQL 形状**：
  - `SELECT group_col, SUM(x) FROM t GROUP BY group_col`
  - 走“临时表 + 聚合”计划的查询（可由 `EXPLAIN` 确认 `Using temporary`）。

### 1.8 普通物化到临时表：`DISTINCT`、`ORDER BY`、流式写临时表等

- **文件/函数**：
  - `sql/composite_iterators.cc`
    - `StreamingIterator::Read()`，L969–970：从 `copy_fields_and_funcs()` 改为 `copy_funcs()`。
  - `sql/sql_executor.cc`
    - `UnqualifiedCountIterator::Read()`，L5156 附近：从 `copy_fields_and_funcs()` 改为 `copy_funcs()`。
    - `JOIN::create_root_access_path_for_join()`，L2831、L3017、L3063 附近：多处 `NewMaterializeAccessPath()` 使用 `copy_items` 标志。
  - `sql/sql_tmp_table.cc`
    - `create_tmp_table()`：新增 `from_item`，并填充 `items_to_copy`。
- **SQL 形状**：
  - `SELECT DISTINCT ... FROM t`
  - `SELECT ... FROM t ORDER BY ...` 需要临时表物化时
  - `SELECT COUNT(*) ...` 走 `UnqualifiedCountIterator` 时

### 1.9 `INFORMATION_SCHEMA` / `SHOW`

- **文件/函数**：`sql/sql_show.cc`
  - `create_schema_table()`，L4354 附近：`tmp_table_param->func_count = field_count`（旧代码为 `field_count = field_count`）。
- **执行**：后续 `create_tmp_table()` 受影响。
- **SQL 形状**：
  - `SELECT ... FROM INFORMATION_SCHEMA.xxx`
  - `SHOW ...` 走 schema table 物化时。

### 1.10 多表 `UPDATE`

- **文件/函数**：`sql/sql_update.cc`
  - `Query_result_update::optimize()`，L2196 附近：`tmp_param->func_count = temp_fields.size()`（旧代码为 `field_count`）。
- **SQL 形状**：
  - `UPDATE multi_table AS a JOIN ... SET ...` 需要临时表存储字段时。

### 1.11 待确认：`subselect_hash_sj_engine::exec()` 删除 `tmp_param`

- **文件/函数**：
  - `sql/item_subselect.cc`
    - `subselect_hash_sj_engine::exec()`，L3462 附近删除设置 `tmp_param` 的代码。
  - `sql/item_subselect.h`
    - 删除成员 `Temp_table_param *tmp_param`。
- **SQL 形状**：
  - `IN (SELECT ...)` 使用 hash semijoin 时。
- **注意**：当前 diff 只显示了删除，未显示后续使用 `tmp_param` 的上下文，因此这一条是否产生可观察影响仍需要进一步确认。

---

## 2. 到达后，哪些输入性质可能影响查询的可观察结果？

### 2.1 核心机制变化

旧机制中，`ConvertItemsToCopy()` 遇到 `Item_field` 会生成 `Copy_field`，走 `copy_fields()`。`Copy_field` 直接操作源 `Field` 和目标 `Field`，不经过 `Item` 求值。

新机制中，所有字段都进入 `items_to_copy`，执行 `copy_funcs()` 时统一调用：

```cpp
item->save_in_field(func.result_field(), /*no_conversions=*/true);
```

即使 `item` 是 `Item_field`，也先通过 `Item::val_*()` 得到值，再保存到目标字段。`CFT_FIELDS` 则进一步限制只复制 `Item::FIELD_ITEM`，用于窗口输出等只关心字段的上下文。

因此，输入性质影响主要来自“`Copy_field` 直接复制”和“`Item_field::save_in_field()` 求值后保存”的差异。

### 2.2 可能影响可观察结果的输入性质

| 输入性质 | 说明 |
|---|---|
| 字段类型 | 尤其字符串/BINARY/BLOB/TEXT/JSON/GEOMETRY/BIT/时间日期/ENUM/SET |
| 类型长度、精度、溢出、截断 | `save_in_field()` 可能触发转换检查或截断；旧 `Copy_field` 直接复制可能不检查 |
| 字符集/校对规则 | 不同字符集字段之间复制，`Item` 保存可能发生字符集转换 |
| `NULL` 语义 | `Item_field` 求值和 `Field` 位复制在 `NULL` 处理上是否完全一致 |
| 严格模式 `sql_mode` | 严格模式下，转换错误可能由警告升级为错误；旧路径可能不报错 |
| 虚拟列 / 生成列 | `Item_field` 可能触发生成列计算，而 `Copy_field` 直接复制存储值 |
| 外部引用 | 子查询物化中，`Item_field` 指向外层字段时，求值与直接复制是否存在差异 |
| 窗口函数输出组合 | `CFT_FIELDS` 只复制 `Item_field`，非字段表达式不会在该步骤复制，可能与旧的 `copy_fields()` 行为不完全一致 |
| `UNION` 各分支字段类型不一致 | 物化结果表字段类型可能与分支源字段类型不同，转换路径变化更容易暴露 |

### 2.3 源码直接支持的关系

这些可以从 diff 直接读出，不需要运行即可确认：

- 派生表/CTE、UNION、半连接物化、聚合 DISTINCT、`GROUP_CONCAT`、窗口函数、`GROUP BY` 临时表聚合等路径中，字段复制从 `copy_fields()` 改成 `copy_funcs()` 或 `copy_funcs(CFT_FIELDS)`。
- `ConvertItemsToCopy()` 现在把所有 `Item` 加入 `items_to_copy`，包括原先走 `copy_fields` 的 `Item_field`。
- `create_tmp_table()` 新增 `from_item` 数组，并在非窗口临时表中只填充 `items_to_copy`。
- 窗口临时表仍保留 `copy_fields`，主要用于帧缓冲反向复制。
- `Temp_table_param::field_count` 被移除，相关计数合并到 `func_count`。

### 2.4 尚待验证的推断

以下属于“可能影响结果”的推断，需要运行时验证：

- 不同字段类型在 `Copy_field` 与 `Item_field::save_in_field()` 下是否产生相同的值、警告和错误。
- `no_conversions=true` 是否能完全消除转换差异，尤其在跨类型、跨字符集场景。
- 严格模式下截断/溢出检测的变化是否真的产生用户可见差异。
- `NULL` 和虚拟列/外部引用场景是否发生行为变化。
- 窗口函数 `CFT_FIELDS` 复制是否对所有窗口查询都正确。
- `subselect_hash_sj_engine::exec()` 删除 `tmp_param` 之后，是否会影响依赖外层临时表上下文的子查询执行。
- 计数方式变化是否会导致某些特殊场景临时表列数错误或 OOM。

### 2.5 区分“源码支持”与“推断”的对照方法

- **源码支持**：直接检查调用点、函数实现和数据结构变化即可确认。
- **推断**：需要在父版本和目标版本上运行相同查询，比较结果、警告和错误；同时用 `EXPLAIN FORMAT=TREE` 确认路径确实经过上述改动函数。
- 若两版结果不同，**不能直接认定哪一版正确**，必须用独立预期结果或等价查询判断正确性。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 推荐验证方法

1. **双版本构建**
   - 构建第一父版本 `865e108e048e…` 和目标版本 `e48f7df6653…`。
   - 对每组候选 SQL，在两版上执行并记录结果、警告、错误码。

2. **确认执行路径命中目标代码**
   - 对每个查询执行 `EXPLAIN FORMAT=TREE`。
   - 确认出现 `Materialize`、`Temp table aggregate`、`Window`、`Duplicate elimination` 等节点。
   - 确保查询确实走 `MaterializeIterator`、`TemptableAggregateIterator`、`WindowIterator` 或 `StreamingIterator` 等受影响路径。

3. **构造结果正确性独立判断**
   - 小数据集下手工计算预期结果。
   - 使用等价但走不同路径的 SQL 验证，例如将物化派生表改写为显式临时表或 `JOIN`。
   - 使用 `CAST` 明确类型转换预期值。
   - 比较标准 SQL 语义，判断两版差异哪个正确。

4. **字段类型覆盖矩阵**
   - 在候选路径中至少覆盖：
     - 整数、定点数、浮点数
     - `BIT`
     - `CHAR/VARCHAR`、`BINARY/VARBINARY`
     - `BLOB/TEXT`
     - `JSON`
     - `GEOMETRY`
     - `DATE/DATETIME/TIMESTAMP`
     - `ENUM/SET`
     - `NULL` 值
   - 重点关注不同字符集、不同长度/精度、截断和溢出场景。

5. **关注严格模式和警告**
   - 比较 `sql_mode` 为默认、`STRICT_TRANS_TABLES`、`STRICT_ALL_TABLES`、`NO_ZERO_DATE`、`ERROR_FOR_DIVISION_BY_ZERO` 时的行为。
   - 通过 `SHOW WARNINGS` 检查两版在转换、截断上的差异。

6. **窗口函数专项验证**
   - 重点验证：
     - `PARTITION BY` / `ORDER BY` 字段类型
     - 窗口函数参数为字段或表达式
     - `LEAD/LAG`、`NTH_VALUE` 等需要帧回填的函数
     - 多个窗口函数共存且输出到不同临时表

### 3.2 仍缺少的证据

- **完整可执行 SQL 尚未准备**：本轮只给出构造形状，需要下一阶段细化为具体查询。
- **类型敏感差异尚未实际运行**：尚未证明哪些字段类型组合会暴露 `Copy_field` 与 `Item::save_in_field()` 的行为差异。
- **`subselect_hash_sj_engine::exec()` 影响未知**：当前材料未展示删除 `tmp_param` 后是否有代码仍依赖它，需要进一步阅读源码或执行 `IN` 子查询验证。
- **计数变化是否引入边界错误未知**：`field_count` 合并到 `func_count` 后，`INFORMATION_SCHEMA`、多表 `UPDATE`、隐藏字段等特殊场景是否受影响，缺乏运行证据。
- **窗口函数 `CFT_FIELDS` 的覆盖范围未验证**：特别是窗口输出表中非 `Item_field` 表达式是否会在其他阶段被正确复制。
- **严格模式下的错误/警告变化缺少系统测试**：需要确认差异是否只是诊断信息变化，还是真正语义变化。

---

### 候选数量总结

- **有明确调用点证据的候选**：10 类  
  （派生表/CTE、UNION、半连接物化、聚合 DISTINCT、`GROUP_CONCAT`、窗口函数、`GROUP BY` 临时表聚合、普通物化、`INFORMATION_SCHEMA`/`SHOW`、多表 `UPDATE`）

- **有删除证据但需进一步确认的候选**：1 类  
  （`subselect_hash_sj_engine::exec()` 删除 `tmp_param`）

下一阶段可以基于这些候选构造最小可复现查询，并在双版本上验证。