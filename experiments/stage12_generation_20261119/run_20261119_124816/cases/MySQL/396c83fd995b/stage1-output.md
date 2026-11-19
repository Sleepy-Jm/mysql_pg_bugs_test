## 一、哪些 SQL 构造可能进入改动路径？

### 1. 入口与分支条件

改动后的执行路径如下：

| 位置 | 文件 : 函数 | 行号 | 作用 |
|---|---|---|---|
| 临时表创建入口 | `sql/sql_tmp_table.cc` : `create_tmp_table` | 目标版 L1361–L1365 | 创建临时表后调用 `sort_copy_func()` |
| 重排函数 | `sql/sql_tmp_table.cc` : `sort_copy_func` | 目标版 L646–L753 | 对 `copy_func` 数组做 `std::stable_partition` |
| 分区谓词 | `sql/sql_tmp_table.cc` : lambda `without_reference_to_select_expr` | 目标版 L749–L753 | 对每个 `Func_ptr` 调用 `Item::walk()` |
| 被调用的虚函数 | `sql/item.h` : `Item::references_select_expr_of` | 目标版 L2101–L2108 | 默认返回 `false` |
| 真正返回 `true` 的分支 | `sql/item.cc` : `Item_ref::references_select_expr_of` | 目标版 L9564–L9572 | 见下方分支说明 |

`Item_ref::references_select_expr_of()` 返回 `true` 的条件是：

```cpp
if (depended_from)  // 外部引用
{
  if (depended_from == sl) return true;
} else if (context->select_lex == sl)
  return true;
return false;
```

即：

- 当前 `Item_ref` 是一个外部引用，且其 `depended_from` 正好是传入的 `SELECT_LEX *sl`；
- 或者它不是外部引用，但其 `context->select_lex` 是传入的 `sl`。

`walk()` 使用 `enum_walk::SUBQUERY_PREFIX`，因此子查询内部的 `Item_ref` 也会被遍历到。

### 2. 可能进入路径的 SQL 构造

根据提交说明和代码注释，以下 SQL 构造有直接证据支持：

#### 候选 1：SELECT 别名被 GROUP BY / HAVING / ORDER BY 引用

```sql
SELECT a+2 AS x FROM t GROUP BY x+3;
```

证据：  
目标版 `sql/sql_tmp_table.cc` L658–L662 注释明确写道：

> Note that the clauses in (a) are allowed to reference a non-hidden expression through an alias (e.g. "SELECT a+2 AS x GROUP BY x+3").

这里的 `x` 是 SELECT 列表表达式 `a+2` 的别名，内部会生成 `Item_ref`。旧代码已处理这种情况，新代码去掉了 `m_alias_of_expr` 限制，但仍然会命中。

#### 候选 2：IN 子查询转换为相关 EXISTS 子查询后生成的无别名引用

SQL 形状：

```sql
(x, y) IN (SELECT expr1, expr2 FROM ...)
```

这类查询可能被转换为：

```sql
EXISTS (SELECT * ... HAVING x = expr1 AND y = expr2 ...)
```

证据：  
目标版 `sql/sql_tmp_table.cc` L664–L668 注释直接提到：

> The clauses in (b) can reference non-hidden expressions without aliases if they have been generated in a query transformation (for example when transforming an IN subquery to a correlated EXISTS subquery ("(x, y) IN (SELECT expr1, expr2 ...)" -> "EXISTS (SELECT * ... HAVING x = expr1 AND y = expr2 ...")).

这些由查询变换生成的引用可能是 `Item_ref`，且不再是“通过别名”引用，因此旧函数 `contains_alias_of_expr()` 不会命中；新函数 `references_select_expr_of()` 会命中。

#### 候选 3：窗口函数与聚合组合导致隐藏项被物化

证据较弱，主要来自注释：  
目标版 `sql/sql_tmp_table.cc` L741–L750 提到：

> Whereas with window functions, it's possible to have a hidden element be an aggregate (produced by split_sum_func) _and_ be materialized (into a further tmp table)...

该场景可能产生隐藏的聚合项，并且该隐藏项可能引用 select 列表表达式。具体 SQL 形态尚不明确，需要后续构造触发窗口函数、聚合和物化临时表。

---

## 二、到达后哪些输入性质可能影响可观察结果？

### 源码直接支持的关系

1. **是否存在满足条件的 `Item_ref`**  
   只要 `copy_func` 数组中的某个表达式包含满足 `Item_ref::references_select_expr_of()` 返回 `true` 的 `Item_ref`，该元素就会被 `stable_partition` 移到数组末尾。  
   这意味着：如果 `copy_func` 中有一个元素依赖当前 query block 的 select 列表表达式，则它会被推迟求值，从而保证被依赖的表达式先被计算并填充到临时表列中。

2. **引用者与被引用者在数组中的初始顺序**  
   注释明确指出，`copy_funcs()` 按数组顺序求值。如果依赖者先于被依赖者求值，就会读取到尚未填充的临时表列。  
   `stable_partition` 将谓词为 `true` 的元素后置，可以避免这种情况。  
   但如果存在多个后置元素之间的依赖，必须保持它们原来的相对顺序。`stable_partition` 的稳定性保证这一点。

3. **被引用表达式是否非确定性**  
   例如被引用表达式是 `RAND()`、`NOW()` 或依赖当前行值。  
   注释用 `RAND()` 举例：如果 `x` 是 `a+2` 的别名，并且 `a+2` 被计算多次，可能得到不同结果。正确顺序应保证 `a+2` 只被求值一次，别名引用读取缓存的副本。

4. **子查询内的引用**  
   因为 `walk()` 使用 `SUBQUERY_PREFIX`，子查询内部的 `Item_ref` 也会被检测。  
   例如外层 select 别名在子查询中被引用，且当前 query block 是外层，则 `depended_from == sl` 命中。

### 尚待验证的推断

1. **非别名 `Item_ref` 的完整集合**  
   新逻辑去掉了 `m_alias_of_expr` 限制，因此所有满足 `depended_from == sl` 或 `context->select_lex == sl` 的 `Item_ref` 都会被后置。  
   目前直接证据只给出了 IN 子查询转换这一例。其他可能产生非别名 `Item_ref` 引用 select 表达式的查询变换尚未从本文材料中完全列举。

2. **窗口函数 + 聚合物化场景**  
   注释提到窗口函数下可能产生被物化的聚合隐藏项，但没有给出具体 SQL 形态，也没有说明该隐藏项是否总是包含满足条件的 `Item_ref`。该候选需要实际构造验证。

3. **`std::stable_partition` 与 `std::stable_sort` 在本场景下的等价性**  
   提交说明声称：

   > stable_partition() does the same job as stable_sort()  
   > Also, stable_partition() calls the predicate only once on each element

   对于布尔属性排序，两者结果通常等价。但新谓词本身范围扩大，因此可能移动更多元素。移动后的集合内部是否仍满足依赖顺序，需要实际查询验证。

### 能够区分两者的对照

| 对照维度 | 可直接支持 | 需要验证 |
|---|---|---|
| 别名引用 vs 直接表达式 | `GROUP BY x+3` 与 `GROUP BY (a+2)+3` 应结果一致 | 若不一致，说明顺序或求值次数有问题 |
| IN 子查询转换 | 注释给出转换示例 | 需构造触发转换的查询，观察是否生成 `Item_ref` |
| 窗口函数 | 注释提及窗口函数场景 | 需构造窗口 + 聚合 + 物化查询，确认是否命中 |
| 非确定性表达式 | 注释用 `RAND()` 说明重复求值风险 | 可用用户变量或等价改写测试实际行为 |

---

## 三、独立验证结果正确性的方法和仍缺少的证据

### 可用的独立验证方法

1. **确认执行路径**  
   使用 `EXPLAIN FORMAT=TREE` 或 `EXPLAIN ANALYZE` 查看查询计划中是否出现临时表、物化或窗口执行节点。  
   这只能证明路径可能被执行，不能证明结果错误。

2. **语义等价改写对照**  
   对同一查询构造两种写法：  
   - 使用别名引用：`SELECT a+2 AS x FROM t GROUP BY x+3`  
   - 不使用别名：`SELECT a+2 AS x FROM t GROUP BY (a+2)+3`  

   两者语义相同，预期结果应完全一致。  
   若结果不一致，则说明别名引用路径存在求值顺序问题。  
   这可以作为独立正确性判断。

3. **非确定性表达式求值次数检测**  
   利用 MySQL 用户变量，例如：

   ```sql
   SET @cnt := 0;
   SELECT @cnt := @cnt + 1 AS x FROM t GROUP BY x + 1;
   ```

   观察最终 `@cnt` 或结果中 `x` 的重复值，判断别名引用是否被多次求值或读取了未填充列。  
   注意这类测试需要排除每行正常求值的影响。

4. **父版本与目标版本对照**  
   对相同 SQL 在两个版本上执行，比较结果。  
   **但差异本身不足以认定有错**。  
   必须结合语义预期或等价改写结果，判断哪个版本符合预期。

5. **优化器开关对照**  
   对于 IN 子查询转换，可以尝试通过 `optimizer_switch` 关闭相关转换（例如 `subquery_to_derived` 或 `materialization`），比较开启与关闭时的结果。  
   如果结果不同，则可能是查询转换产生的 `Item_ref` 顺序问题。

### 仍缺少的证据

1. **具体可复现的 SQL 用例**  
   目前只有注释中给出的示意 SQL，尚未构造出能稳定触发 `sort_copy_func()` 且谓词返回 `true` 的完整可执行 SQL。

2. **执行计划或内部追踪证据**  
   没有提供 `EXPLAIN` 输出、`optimizer_trace` 或调试日志，证明某个查询确实进入了 `create_tmp_table` → `sort_copy_func` 路径，并且 `copy_func` 数组中存在命中的 `Item_ref`。

3. **两版本结果差异或与预期结果不一致的案例**  
   尚未观察到目标版本与父版本结果不同的具体实例，也没有独立证明某一查询结果违反了 SQL 语义。

4. **对非别名 `Item_ref` 场景的确认**  
   除 IN 子查询转换外，尚不清楚哪些其他查询会生成满足新谓词但旧谓词不满足的 `Item_ref`。

5. **`stable_partition` 扩大移动范围后的顺序正确性验证**  
   新逻辑将更多元素移动到末尾，这些元素之间可能存在未被注释覆盖的依赖。需要实际测试确认没有引入新的未填充列读取问题。