## 1. 可能进入改动路径的 SQL 构造

> 所有候选路径的前提是：编译时定义了 `SQLITE_COUNTOFVIEW_OPTIMIZATION`，且运行时 `OptimizationEnabled(db, SQLITE_QueryFlattener|SQLITE_CountOfView)` 为真。该开关位置在 `src/sqliteInt.h` 的 `SQLITE_CountOfView` 位定义及 `OptimizationEnabled()` 宏附近，`src/select.c` 调用点在 `sqlite3Select()` 中新增块，约目标版本 L5411–L5417。

### 1.1 `countOfViewOptimization()` 的入口条件

文件：`src/select.c`  
函数：`countOfViewOptimization()`，新增于约 L5020–L5100。

进入该优化的外层查询必须同时满足：

- 外层查询是聚合查询：`(p->selFlags & SF_Aggregate)!=0`
- 外层结果列只有一列：`p->pEList->nExpr==1`
- 该列表达式是聚合函数：`pExpr->op==TK_AGG_FUNCTION`
- 函数名是 `count`，大小写不敏感：`sqlite3_stricmp(...,"count")`
- 必须是 `count(*)`：`pExpr->x.pList==0`
- `FROM` 子句只有一项：`p->pSrc->nSrc==1`
- 该项是一个子查询：`pSrc->a[0].pSelect != 0`
- 该子查询是复合查询：`pSub->pPrior != 0`

因此最基本的 SQL 形状是：

```sql
SELECT count(*)
FROM (SELECT ... UNION ALL SELECT ...)
```

### 1.2 复合子查询各项的循环检查

同一个函数中的 `do/while` 循环对每个复合项检查：

- 对于所有仍有 `pPrior` 的项，算子必须是 `TK_ALL`：

  ```c
  if( pSub->op!=TK_ALL && pSub->pPrior ) return 0;
  ```

  即复合算子必须是 `UNION ALL`。

- 每个项不能有 `WHERE`：

  ```c
  if( pSub->pWhere ) return 0;
  ```

- 每个项不能是聚合查询：

  ```c
  if( pSub->selFlags & SF_Aggregate ) return 0;
  ```

这些检查覆盖的 SQL 构造是：内层项上没有 `WHERE`，复合算子为 `UNION ALL`，内层项不是聚合查询。

### 1.3 代码未检查但可能仍进入的构造

从函数体直接可以看出，以下构造没有被检查，因此它们可能使查询进入优化路径：

| 位置 | 未检查项 | SQL 构造 |
|---|---|---|
| 内层每个复合项 | 未检查 `SF_Distinct` | 内层 `SELECT DISTINCT` |
| 内层每个复合项 | 未检查 `pSub->pGroupBy` | 内层 `GROUP BY` |
| 内层每个复合项 | 未检查 `pSub->pHaving` | 内层 `HAVING` |
| 内层每个复合项 | 未检查 `pSub->pLimit` / `pSub->pOffset` | 内层 `LIMIT` / `OFFSET` |
| 内层每个复合项 | 未检查 `pSub->pOrderBy` | 内层 `ORDER BY` |
| 外层查询 | 未检查 `p->pWhere` | 外层 `WHERE` |
| 外层查询 | 未检查 `p->pGroupBy` / `p->pHaving` | 外层 `GROUP BY` / `HAVING` |
| 外层查询 | 未检查 `SF_Distinct` | 外层 `DISTINCT` |
| 外层查询 | 未检查 `p->pOrderBy` / `p->pLimit` / `p->pOffset` | 外层 `ORDER BY` / `LIMIT` / `OFFSET` |

这些“未检查但可能进入”的项是下一阶段查询正确性测试的主要候选来源。

---

## 2. 到达后，哪些输入性质可能影响可观察结果？

### 2.1 源码直接支持的关系

对于以下“安全形态”，代码本身和注释一致地给出了直接支持：

```sql
SELECT count(*)
FROM (
    SELECT ... FROM t1
    UNION ALL
    SELECT ... FROM t2
)
```

即：

- 复合算子为 `UNION ALL`
- 各项没有 `WHERE`
- 各项不是聚合查询
- 外层是简单 `count(*)`

源码中直接构造的结果是：

```sql
SELECT (SELECT count(*) FROM t1) + (SELECT count(*) FROM t2)
```

这是直接由转换代码产生的。  
因此，在该受限形态下，结果应当等于各项行数之和。

### 2.2 尚待验证的推断关系

以下输入属性会影响行数或分组语义，但 `countOfViewOptimization()` 没有直接检查它们。它们是否真的能到达该函数，取决于 SQLite 前期的解析、`SF_*` 标志位设置以及语法是否允许。

#### 高风险：内层 `DISTINCT`

原查询：

```sql
SELECT count(*)
FROM (
    SELECT DISTINCT x FROM t1
    UNION ALL
    SELECT y FROM t2
)
```

原始语义是：`count(*)` 统计 `t1` 去重后的 `x` 值数量，再加上 `t2` 行数。

但代码替换后，第一个内层项变成大致：

```sql
SELECT count(*) FROM t1
```

这会统计 `t1` 物理行数，而不是去重后的 `x` 值数量。  
如果 `t1` 存在重复 `x`，优化前后结果不同。

源码依据：  
循环只检查了 `pSub->pWhere` 和 `SF_Aggregate`，没有检查 `pSub->selFlags & SF_Distinct`。

#### 高风险：外层 `WHERE`

原查询：

```sql
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
)
WHERE x > 0
```

原始语义是：先对 `UNION ALL` 结果执行 `WHERE x > 0`，再统计行数。

优化函数没有检查或清除外层 `p->pWhere`。转换后外层 `pSrc` 被替换为空 `SrcList`，`pWhere` 保留。  
结果可能是列引用失效、查无此列，或过滤条件没有按原始语义应用。

#### 高风险：外层 `GROUP BY` / `HAVING`

原查询可能形如：

```sql
SELECT count(*)
FROM (
    SELECT x FROM t1
    UNION ALL
    SELECT y FROM t2
)
GROUP BY x
HAVING count(*) > 1
```

原始语义是按 `x` 分组后计数并过滤。

函数没有检查外层 `p->pGroupBy`、`p->pHaving`，转换时只执行了：

```c
p->pEList->a[0].pExpr = pExpr;
p->selFlags &= ~SF_Aggregate;
```

外层分组和 `HAVING` 没有被同步改写。  
这可能导致分组语义被破坏、`HAVING` 中的 `count(*)` 引用失效，或产生不同的分组输出。

#### 中高风险：内层 `GROUP BY` / `HAVING`

如果内层项带 `GROUP BY`：

```sql
SELECT count(*)
FROM (
    SELECT x FROM t1 GROUP BY x
    UNION ALL
    SELECT y FROM t2
)
```

代码没有检查 `pSub->pGroupBy`。  
如果 `SF_Aggregate` 没有因为 `GROUP BY` 被设置，则该查询可能进入优化。  
转换后内层项会变成类似：

```sql
SELECT count(*) FROM t1 GROUP BY x
```

这作为标量子查询存在时，如果返回多行，可能触发运行时错误，或只取第一行；如果是无分组但带 `HAVING`，又可能过滤掉唯一的聚合行。  
语义不再等价。

源码依据：  
代码直接不检查 `pSub->pGroupBy` 和 `pSub->pHaving`；同时本摘录没有给出 `SF_Aggregate` 对 `GROUP BY` 的直接定义，因此需验证它是否会被 `SF_Aggregate` 拦截。

#### 中高风险：内层 `LIMIT` / `OFFSET`

如果 SQLite 语法允许复合查询的每个项带 `LIMIT` / `OFFSET`，例如：

```sql
SELECT count(*)
FROM (
    SELECT x FROM t1 LIMIT 5
    UNION ALL
    SELECT y FROM t2
)
```

原始语义中，第一个项只贡献最多 5 行。

函数没有检查 `pSub->pLimit` 或 `pSub->pOffset`。  
转换后可能变成：

```sql
SELECT (SELECT count(*) FROM t1 LIMIT 5)
     + (SELECT count(*) FROM t2)
```

如果内层聚合项只返回一行，`LIMIT 5` 不减少行数；`LIMIT 0` 或 `OFFSET` 可能导致标量子查询返回零行，使加法结果变成 `NULL`。  
因此该项需要验证 SQLite 是否允许复合项携带 `LIMIT/OFFSET`，以及标量子查询零行时的具体行为。

#### 较低风险：内层 `ORDER BY` 单独出现

单独的内层 `ORDER BY` 不影响 `COUNT(*)` 的行数，只影响顺序。  
但在与内层 `LIMIT`/`OFFSET` 结合时会变得重要。

#### 较低风险：外层 `DISTINCT`

外层 `DISTINCT` 对单行 `count(*)` 结果通常没有影响。  
但如果与外层 `GROUP BY` 组合，多个组产生相同 `count(*)` 值时，`DISTINCT` 会改变输出行数。  
由于外层 `GROUP BY` 已经未被检查，`DISTINCT` 也需要作为组合场景验证。

#### 较低风险：外层 `ORDER BY` / `LIMIT` / `OFFSET`

外层只有一个计数结果行时，`LIMIT 0` 可能仍得到零行，`LIMIT 1` 得到一行。  
但如果外层 `ORDER BY` 引用旧子查询列，转换后可能列引用失效。  
该风险级别低于外层 `WHERE` / `GROUP BY`。

### 2.3 能区分“源码直接支持”和“尚待验证推断”的对照

- **正面对照**：  
  使用无 `WHERE`、无 `GROUP BY`、无 `HAVING`、无 `DISTINCT`、无 `LIMIT/OFFSET` 的 `UNION ALL` 子查询：

  ```sql
  SELECT count(*)
  FROM (
      SELECT x FROM t1
      UNION ALL
      SELECT y FROM t2
  )
  ```

  预期结果可直接由 `(SELECT count(*) FROM t1) + (SELECT count(*) FROM t2)` 给出。

- **逐项加噪声对照**：  
  在正面对照基础上，单独加入某个未检查构造，例如只加入内层 `DISTINCT`，保持其他条件不变。  
  通过比较“优化开启”“优化关闭”以及手工计算值，可以区分这是否只是路径变化，还是真的产生可观察错误。

- **数据对照**：  
  对于 `DISTINCT` / `GROUP BY`，需要准备包含重复行和 `NULL` 的数据。  
  对于 `LIMIT` / `OFFSET`，需要准备空表和行数不足表，观察标量子查询零行是否导致 `NULL` 传播。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 独立验证方法

#### 方法一：手工语义结果

为每个候选查询建立小型表，手动计算语义结果。  
例如：

- 内层 `DISTINCT`：手工数去重值数量，而不是物理行数。
- 外层 `WHERE`：手工统计满足条件的 `UNION ALL` 行数。
- 外层 `GROUP BY`：手工列出每个组的 `count(*)`。

这些手工结果作为“正确结果基准”。

#### 方法二：关闭优化作为对照

同一构建中，通过 SQLite 的优化开关关闭 `SQLITE_CountOfView` 位：

```c
sqlite3_test_control(SQLITE_TESTCTRL_OPTIMIZATIONS, SQLITE_CountOfView);
```

然后执行同一查询。  
这用于确认查询是否真的因该优化而产生差异。  
但正如题目所述，仅“两版结果不同”仍不足以认定有错；差异必须与手工语义结果一起判断。

#### 方法三：使用等价形式作为独立预期

对于安全形态，预期可由：

```sql
SELECT (SELECT count(*) FROM t1) + (SELECT count(*) FROM t2)
```

直接给出。

对于复杂形态，例如外层 `WHERE`，可以写一个等价的非优化查询，例如先物化 `UNION ALL` 再计数，作为比较基准。

#### 方法四：确认路径被执行

可以使用 `SELECTTRACE` 中新增的 0x400 跟踪输出：

```c
if( sqlite3SelectTrace & 0x400 ){
    SELECTTRACE(0x400,pParse,p,("After count-of-view optimization:\n"));
}
```

或 `EXPLAIN` / VDBE 输出，确认查询确实进入了 `countOfViewOptimization()`。  
但这只能用于说明“路径到达”，不能用于判断结果正确性。

### 3.2 仍缺少的证据

1. **内层 `GROUP BY` / `HAVING` 是否会被 `SF_Aggregate` 拦截？**  
   本摘录没有给出 `SF_Aggregate` 的定义。如果 `GROUP BY` 或 `HAVING` 会设置 `SF_Aggregate`，那么循环中的：

   ```c
   if( pSub->selFlags & SF_Aggregate ) return 0;
   ```

   可能已经拒绝部分候选；否则这些候选能进入优化。

2. **复合项是否允许携带 `LIMIT` / `OFFSET` / `ORDER BY`？**  
   这取决于 SQLite 语法解析，本文没有提供语法部分。  
   如果语法上不允许，则对应候选不成立。

3. **标量子查询返回零行或多行时的行为。**  
   例如内层 `GROUP BY` 被转换后产生多行，或内层 `LIMIT 0` 导致零行时，在 `TK_PLUS` 表达式中是报错、取第一行，还是产生 `NULL` 传播。  
   本摘录没有给出相关执行语义。

4. **外层 `WHERE` / `GROUP BY` / `HAVING` 在 `pSrc` 被清空后的具体解释。**  
   代码中转换后 `pTabList = p->pSrc`，而 `pSrc` 是一个空 `SrcList`。  
   如果外层还保留 `pWhere`，后续 `sqlite3WhereBegin()` 会如何处理空 `FROM` 和列引用，尚无源码证据。

5. **外层 `DISTINCT`、`ORDER BY`、`LIMIT/OFFSET` 联合变化。**  
   单行 `count(*)` 场景下这些构造可能无害，但组合外层 `GROUP BY` 后可能产生差异。  
   需要下一阶段用多组数据验证。

6. **`pExpr->x.pList==0` 是否严格对应于 `count(*)`。**  
   本摘录未显示 `count()` 语法是否合法，以及其 `x.pList` 表示是否与 `count(*)` 相同。  
   这会影响是否只有 `count(*)` 能进入，还是某些无参数 `count()` 形式也可能进入。

7. **`where.c` 中调试断言变更。**  
   该变更只是 `SQLITE_DEBUG` 下断言条件从 `m==MASKBIT(ii)` 放宽为 `m>=mx`。  
   它不直接影响查询结果，但如果下一阶段使用 debug 构建，可能需要确认该断言不会隐藏其他问题。