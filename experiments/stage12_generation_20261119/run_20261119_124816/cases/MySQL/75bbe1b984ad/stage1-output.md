## 1. 可能进入改动路径的 SQL 构造

候选按“源码可定位的入口 + 分支条件”列出，行号为本文提供的目标版本相关位置。

### 1.1 IN 子查询走 index_subquery / unique_subquery

入口：

- `JOIN::replace_index_subquery()`  
  `sql/sql_optimizer.cc:1202-1263`

进入条件：

- `unit->item` 的 `substype() == Item_subselect::IN_SUBS`
- `primary_tables == 1`
- `where_cond` 非空
- 非 `UNION`
- `order == nullptr && !select_distinct`
- 没有 `group_list`
- 不是已选择 `EXEC_MATERIALIZATION` 的 IN 子查询
- 内层首表不是递归 derived/view
- `having_cond == nullptr` 时，首表访问类型为 `JT_EQ_REF` 或 `JT_REF`，且 `ref().items[0]->item_name.ptr() == in_left_expr_name`
- 或者 `having_cond` 存在时，首表访问类型为 `JT_REF_OR_NULL`，且 `having_cond->created_by_in2exists()`

对应 SQL 形态：

```sql
outer_col IN (SELECT key_col FROM single_innertable WHERE ...)
```

典型为带索引内层表的单表 IN 子查询，优化器可重写为 `index_subquery` 或 `unique_subquery`。

主要改动点：

- 旧代码用 `change_engine()` 保存 `old_engine` 并切换到 `subselect_indexsubquery_engine`。
- 新代码直接 `set_indexsubquery_engine()`，不再保存旧 engine。
- 后续 `Item_subselect::cleanup()` 行为相应改变。

### 1.2 IN 子查询走 materialization + hash semi-join

入口：

- `Item_in_subselect::finalize_materialization_transform()`  
  `sql/item_subselect.cc:464-516`
- `subselect_hash_sj_engine::setup()`  
  `sql/item_subselect.cc:3001-3193`
- `subselect_hash_sj_engine::exec()`  
  `sql/item_subselect.cc:3271-3402`
- `subselect_hash_sj_engine::cleanup()`  
  `sql/item_subselect.cc:3257-3261`

进入条件：

- IN 子查询被优化器选择为 materialization。
- `Item_in_subselect::exec_method == EXEC_MATERIALIZATION`。
- 常见于非相关 IN 子查询，或适合构造临时表加 semi-join 的场景。

对应 SQL 形态：

```sql
outer_col IN (SELECT ... FROM ...)
```

然后优化器选择 `<materialized_subquery>` / hash semi-join。

主要改动点：

- 新代码不再保存 `materialize_engine`，改为直接保存 `unit`。
- `setup()` 中若 `unit->is_prepared()` 为 false，则调用：

```cpp
unit->prepare(thd, result, SELECT_NO_UNLOCK, 0)
```

其中 `result` 来自 `subselect_indexsubquery_engine` 内新的 `Query_result_union *result = nullptr`，而非旧 `subselect_iterator_engine` 的结果对象。

- `cleanup()` 旧代码调用 `materialize_engine->cleanup(thd)`，新代码仅调用 `unit->reset_executed()`。

### 1.3 IN 子查询多次执行：NULL / was_null 重置路径

入口：

- `Item_in_subselect::exec()`  
  `sql/item_subselect.cc:724-766`

旧代码：

```cpp
if (unit->is_executed() && engine->uncacheable())
    null_value = was_null = false;
```

新代码：

```cpp
if (unit->is_executed()) {
    null_value = false;
    was_null = false;
}
```

进入条件：

- 必须是 IN 子查询。
- `unit->is_executed()` 为 true，即同一子查询单元已经被执行过。
- 不影响 `left_expr_cache` 快速短路返回的情形；否则会在短路 return 之前返回。
- 多次执行来源通常是：
  - 外层查询有多行，IN 子查询逐行重执行。
  - prepared statement 或存储程序中的重复执行。
  - 相关子查询中不同外层行触发多次执行。

对应 SQL 形态：

```sql
SELECT ...
FROM outer_table
WHERE outer_col IN (SELECT ... );
```

### 1.4 IN 子查询的可缓存性判断与 used_tables 更新

入口：

- `Item_subselect::is_uncacheable()`  
  `sql/item_subselect.h:210` 附近
- `Item_subselect::update_used_tables()`  
  `sql/item_subselect.cc:784` 附近

旧实现依赖 `engine->uncacheable()`：

- 对 `subselect_iterator_engine`，返回 `unit->uncacheable`。
- 对 `subselect_indexsubquery_engine` / `subselect_hash_sj_engine`，旧 `uncacheable()` 固定返回 `UNCACHEABLE_DEPENDENT`。

新实现改为：

```cpp
bool Item_subselect::is_uncacheable() const { return unit->uncacheable; }
```

```cpp
void Item_subselect::update_used_tables() {
  if (!unit->uncacheable)
    used_tables_cache &= ~subquery->upper_select_const_tables();
}
```

因此，当 IN 子查询已经使用 `indexsubquery_engine` 或 `subselect_hash_sj_engine`，但 `unit->uncacheable == 0` 时，新代码可能清除 `used_tables_cache` 中由外层 const table 贡献的位。

进入条件：

- IN 子查询使用了特殊引擎，尤其是 hash semi-join。
- `unit->uncacheable == 0`，即内层子查询本身不依赖外层。
- 外层查询存在 const table。
- 调用 `update_used_tables()` 时期望重新计算依赖表位图。

对应 SQL 形态：

```sql
SELECT ...
FROM const_or_small_outer
WHERE outer_col IN (SELECT inner_col FROM inner_table ...);
```

### 1.5 已有 `unit->item` 的重新初始化路径

入口：

- `Item_subselect::init()`  
  `sql/item_subselect.cc:133-163`

进入条件：

- 创建 `Item_subselect` 时，`select_lex->master_unit()->item` 已经存在。
- 典型场景可能与 prepared statement、view/derived 重解析、`invalidate_and_restore_select_lex()` 等有关。

旧代码复制并转移 `engine`：

```cpp
engine = unit->item->engine;
unit->item->engine = nullptr;
engine->change_query_result(current_thd, this, result);
```

新代码只移动 `subquery`：

```cpp
subquery = move(unit->item->subquery);
subquery->change_query_result(current_thd, this, result);
```

如果旧 `unit->item` 同时拥有 `indexsubquery_engine`，新代码没有转移该指针。是否可达需进一步验证。

### 1.6 清理与后续重执行

入口：

- `Item_subselect::cleanup()`  
  `sql/item_subselect.cc:302-321`

进入条件：

- 任意子查询执行完成后的清理。
- prepared statement 再次执行前。
- 有 `indexsubquery_engine` 或 `subquery` 存在的子查询。

旧代码保留 `old_engine` 并在清理后恢复：

```cpp
if (old_engine) {
    if (engine) {
      engine->cleanup(current_thd);
      destroy(engine);
    }
    engine = old_engine;
    old_engine = nullptr;
}
if (engine) engine->cleanup(current_thd);
```

新代码：

```cpp
if (indexsubquery_engine) {
    indexsubquery_engine->cleanup(current_thd);
    destroy(indexsubquery_engine);
    indexsubquery_engine = nullptr;
}
if (subquery) subquery->cleanup(current_thd);
```

进入条件：

- 已经创建过 `indexsubquery_engine` 的 IN 子查询。
- 清理后再次执行同一 item。
- 特别值得关注 `subselect_hash_sj_engine` 与 `SubqueryWithResult` 的清理顺序和资源释放是否等价。

### 1.7 EXPLAIN / print 路径

虽不直接证明结果错误，但可用于确认执行路径：

- `Explain::explain_subqueries()`  
  `sql/opt_explain.cc:638` 附近
- `Explain_join::explain_join_type()`  
  `sql/opt_explain.cc:1414` 附近
- `Item_subselect::print()`  
  `sql/item_subselect.cc:800` 附近

可用于验证：

- `unique_subquery` / `index_subquery`
- `<materialized_subquery>`
- `using_temporary`
- `hash_sj_engine` 是否被选择

---

## 2. 到达候选路径后，哪些输入性质可能影响可观察结果

下面对每个候选区分“源码直接支持的关系”“尚待验证的推断”和“可区分两者的对照”。

### 2.1 `Item_in_subselect::exec()` 的 null/was_null 重置

**源码直接支持的关系**

- 旧代码仅当 `unit->is_executed() && engine->uncacheable()` 时重置 `null_value` 和 `was_null`。
- 新代码只要 `unit->is_executed()` 就重置二者。
- 对旧的 `subselect_iterator_engine`，`uncacheable()` 返回 `unit->uncacheable`。因此当 `unit->uncacheable == 0` 时：
  - 旧实现不重置。
  - 新实现会重置。
- 若前一次执行后 `null_value` 或 `was_null` 为 true，新实现可能在下一次执行时把它们清为 false，导致 NULL 语义丢失或改变。

**可能影响可观察结果的输入性质**

- IN 子查询第二次或后续执行。
- 子查询是 cacheable 的，即 `unit->uncacheable == 0`。
- 执行走 `SubqueryWithResult`，而不是旧的 `subselect_indexsubquery_engine` 或 `subselect_hash_sj_engine`。
- 首次执行使 `was_null` 或 `null_value` 为 true：
  - 内层结果包含 NULL 且无匹配。
  - 左表达式为 NULL。
  - 子查询结果为空。
- 第二次执行时左表达式发生变化，且 `left_expr_cache` 未命中，从而不会提前 return。

**尚待验证的推断**

- 实际用户可见差异是否出现，取决于是否有 SQL 满足上述组合。
- 需要确认在执行路径中 `SubqueryWithResult` 的 `result` 对象如何设置 `null_value` / `was_null`，以及 `val_bool()` 是否会因为重置而给出不同布尔值。
- “两版本结果不同”不一定等于“新版本错误”，需人工判断 NULL vs FALSE 是否符合 SQL 语义。

**对照**

- 负对照：子查询只执行一次。
- 负对照：左表达式在第二次执行时与第一次相同，触发 `left_expr_cache` 短路。
- 正对照：cacheable IN 子查询执行两次，左表达式变化，内层结果包含 NULL。
- 引擎对照：uncacheable IN 子查询在旧新版本都重置，因此不应有差异。

---

### 2.2 `is_uncacheable()` / `update_used_tables()` 改用 `unit->uncacheable`

**源码直接支持的关系**

- 旧 `subselect_indexsubquery_engine::uncacheable()` 固定返回 `UNCACHEABLE_DEPENDENT`。
- 旧 `subselect_hash_sj_engine` 继承该行为，因此即使内层子查询不依赖外层，`engine->uncacheable()` 仍非 0。
- 新实现用 `unit->uncacheable`，对非相关 materialized IN 子查询，该值可能为 0。
- 因此：
  - 之前 `update_used_tables()` 不会执行 `used_tables_cache &= ~upper_select_const_tables()`。
  - 新代码可能执行清除。

**可能影响可观察结果的输入性质**

- IN 子查询已经建立 `subselect_hash_sj_engine` 或 `subselect_indexsubquery_engine`。
- `unit->uncacheable == 0`，即内层查询不依赖外层。
- 外层查询包含 const table。
- 子查询 item 的 `used_tables_cache` 被重新计算。

**尚待验证的推断**

- 该变化首先可见于 `EXPLAIN` 或 `OPT_TRACE` 中 `const table` 判定。
- 是否会进一步改变最终结果，取决于优化器是否因此把子查询 item 视为常量或减少依赖，进而改变执行计划。
- 可能只影响性能/计划，不一定影响查询结果。

**对照**

- 负对照：内层子查询是相关子查询，即 `unit->uncacheable != 0`。
- 正对照：非相关 materialized IN 子查询 + 外层 const table。
- 路径对照：同一子查询分别强制走 materialization 与不走 materialization。

---

### 2.3 `subselect_hash_sj_engine` setup / cleanup 的 result 与 unit 处理

**源码直接支持的关系**

- `subselect_hash_sj_engine::setup()` 中，如果 `unit->is_prepared()` 为 false，会以 `result` 调用 `unit->prepare()`。
- 这个 `result` 在重构后来自 `subselect_indexsubquery_engine` 的成员：

```cpp
Query_result_union *result = nullptr;
```

- 本文提供代码中没有看到在 `setup()` 前给它赋值。
- `subselect_hash_sj_engine::cleanup()` 不再调用 `materialize_engine->cleanup()`，也就是不再直接调用旧 iterator engine 的 `result->cleanup()`。
- 不过 `Item_subselect::cleanup()` 后续仍会调用 `subquery->cleanup()`，可能间接完成 `result->cleanup()`。

**可能影响可观察结果的输入性质**

- IN 子查询走 materialization。
- `unit->is_prepared()` 在 `setup()` 时为 false。
- 子查询被清理后再次执行。
- `left_expr` 或内层结果含 NULL，可能依赖 result 对象的 NULL 状态。

**尚待验证的推断**

- 正常路径下，`finalize_materialization_transform()` 发生在优化阶段，unit 通常已经 prepared，因此 `unit->prepare()` 分支可能不会触发。
- prepared statement 或重新解析路径是否会让 unit 处于未 prepared 状态，需要专门测试。
- `result == nullptr` 是否会引发错误或跳过结果绑定，需阅读 `SELECT_LEX_UNIT::prepare()` 或运行时验证。

**对照**

- 负对照：一次性执行的 materialized IN 子查询。
- 正对照：prepared statement 多次 `EXECUTE`，或外层多行导致 hash semi-join 多次执行。
- 状态对照：unit 已 prepared 与未 prepared 的进入路径。

---

### 2.4 `Item_subselect::init()` 中旧 item 已有 `indexsubquery_engine`

**源码直接支持的关系**

- 新代码只移动 `unit->item->subquery`。
- 没有移动或清空 `unit->item->indexsubquery_engine`。
- 如果旧 item 已经拥有 `indexsubquery_engine`，新 item 获得 `subquery`，旧 item 仍保留原 `indexsubquery_engine`。

**可能影响可观察结果的输入性质**

- `unit->item` 已存在。
- 旧 item 是 IN 子查询且已经完成 index_subquery 或 hash_sj 转换。
- 随后新的 `Item_subselect` 对象复用同一个 unit。

**尚待验证的推断**

- 这种场景是否只能通过 prepared statement 重解析或某种内部重写触发，尚不清楚。
- 如果可达，可能出现两个 item 共享 unit 但 engine 状态不一致的问题。

**对照**

- 负对照：`unit->item` 不存在，直接新建 `SubqueryWithResult`。
- 正对照：已有 `unit->item` 且为普通非 IN 子查询。
- 高风险对照：已有 `unit->item` 且为已 materialization 的 IN 子查询。

---

### 2.5 `Item_subselect::cleanup()` 去掉 old_engine 恢复机制

**源码直接支持的关系**

- 旧代码在 cleanup 时如果存在 `old_engine`，会销毁当前 engine 并恢复旧 engine。
- 新代码销毁 `indexsubquery_engine` 后直接置空。
- 这意味着一次清理后，IN 子查询不会自动恢复为普通 iterator engine。

**可能影响可观察结果的输入性质**

- IN 子查询已经被 `replace_index_subquery` 或 `finalize_materialization_transform` 设置了特殊 engine。
- cleanup 后再次使用同一个 item。
- 常见于 prepared statement 多次执行。

**尚待验证的推断**

- 正常语句结束时 item 可能被销毁，不会暴露差异。
- prepared statement 或缓存的计划中可能保留 item 并多次 cleanup，需要测试。

**对照**

- 负对照：一次性查询。
- 正对照：同一 prepared statement 多次 `EXECUTE`。
- 引擎对照：普通非 IN 子查询 vs IN 子查询。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 总体验证方法

1. **双版本差分测试**
   - 对同一组 SQL，在父版本 `6226c1a8ce50c422ad7c649e1216e53bb7248f69` 和目标版本 `75bbe1b984ad4de81d6897e94e740d5839ab3fb0` 上执行。
   - 比较结果集，要求显式 `ORDER BY` 以确保顺序确定。
   - 同时比较 warning/error 情况。

2. **用 EXPLAIN/OPT_TRACE 确认路径**
   - 对每个候选，先用 `EXPLAIN` 验证是否进入：
     - `unique_subquery`
     - `index_subquery`
     - `<materialized_subquery>`
     - `using_temporary`
   - 对关键语句使用 `OPT_TRACE` 查看是否发生 `materialization`、`index_subquery` 改写，以及 `const table` 判断。
   - 路径被执行或两版本执行计划不同，还不足以证明结果错误，必须比较实际结果。

3. **针对 NULL 语义的重点测试**
   - 内层结果含 NULL。
   - 外层左表达式为 NULL。
   - 内层结果为空。
   - IN 结果应为 TRUE / FALSE / UNKNOWN(NUL) 的区分。
   - 至少包含外层 2 行以上，形成多次执行。

4. **针对重复执行和 prepared statement**
   - 使用 `PREPARE` / `EXECUTE` 多次执行。
   - 使用外层表多行触发逐行执行。
   - 对 cacheable / uncacheable 子查询分别测试。
   - 对 hash_sj materialization 场景测试清理后重执行。

5. **人工判定 SQL 语义**
   - 对每个差异结果，根据 NULL 传播、IN 子查询语义判断哪个版本正确，而不是仅判断“结果不同”。

### 3.2 仍缺少的证据

1. **`Item_in_subselect::exec()` 重置差异**
   - 缺一个可复现的 SQL，使：
     - 子查询走 `SubqueryWithResult`。
     - `unit->is_executed()` 为 true。
     - `unit->uncacheable == 0`。
     - 前一次 `null_value`/`was_null` 为 true。
     - 第二次左表达式不同且未命中 `left_expr_cache`。
   - 需要验证新版本是否确实错误地清除了 NULL 标志。

2. **`update_used_tables()` / `is_uncacheable()` 差异**
   - 缺证据表明这个变化会改变最终结果，而不只是 `EXPLAIN` 或计划。
   - 需要比较同一查询在不同数据分布下是否出现结果差异。

3. **`subselect_hash_sj_engine::setup()` 的 `result == nullptr`**
   - 缺证据确认是否存在 `unit` 未 prepared 且 `setup()` 被调用的实际路径。
   - 需要查看 `SELECT_LEX_UNIT::prepare()` 对空 result 的处理，或准备运行时测试。

4. **`subselect_hash_sj_engine::cleanup()` 省略 `materialize_engine->cleanup()`**
   - 缺证据确认是否被后续 `subquery->cleanup()` 完全补偿。
   - 需要通过 prepared statement 多次执行测试资源状态和结果一致性。

5. **`Item_subselect::init()` 移动 `subquery` 但不移动 `indexsubquery_engine`**
   - 缺证据证明该场景可由公开 SQL 触发。
   - 需要确认哪些语句会复用已有 `unit->item`。

6. **旧 `old_engine` 恢复机制移除**
   - 缺证据表明对 prepared statement 或存储程序有用户可见影响。
   - 需要多次执行测试并比较结果。

---

## 建议的 Stage 2 候选优先级

1. **最高优先级**：`Item_in_subselect::exec()` 对 `null_value` / `was_null` 的重置条件变化。
   - 源码差异直接、影响 NULL 语义，且可执行路径清晰。
2. **高优先级**：`is_uncacheable()` / `update_used_tables()` 改用 `unit->uncacheable`。
   - 对 materialized IN 子查询尤其可疑。
3. **中优先级**：`subselect_hash_sj_engine::setup()` 和 `cleanup()` 的 result / unit 处理。
   - 多处源码变化，但正常路径可能不会触发。
4. **低优先级**：`Item_subselect::init()` 与 `cleanup()` 的 old_engine 移除。
   - 需要更专门的重执行或重解析场景。