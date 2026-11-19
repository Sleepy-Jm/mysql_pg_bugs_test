# PostgreSQL 提交分析 · Stage 1

以下内容仅基于提供的 diff、提交信息和源码摘录。候选 SQL 构造只给出形态类，可执行 DDL/DML 留到下一阶段。  
判断原则：**计划路径被执行或两个版本计划不同，只说明命中提交；是否真的产生错误结果，必须用独立语义基准验证。**

---

## 1. 可能进入改动路径的 SQL 构造

### 1.1 单子 Append / MergeAppend 节点消除

**入口：**
- `src/backend/optimizer/plan/setrefs.c`
  - `set_plan_refs()` 中的 `T_Append` / `T_MergeAppend` 分支：L909–L918
  - `set_append_references()`：L1298–L1358
  - `set_mergeappend_references()`：L1367–L1390
  - `clean_up_removed_plan_level()`：L1124–L1146
  - `set_subqueryscan_references()` 也改为调用 `clean_up_removed_plan_level()`：约 L1040

**分支条件：**
- `list_length(aplan->appendplans) == 1`
- `list_length(mplan->mergeplans) == 1`
- `trivial_subqueryscan(plan)` 为真时也可能消除 SubqueryScan

**对应 SQL 构造形态：**
- 查询对象是 append relation，但计划期最终只有一个存活 child：
  - 分区表只有一个分区；
  - 分区键上的 `WHERE` 条件使运行时计划剪枝后只剩一个分区；
  - 传统继承父表只有一个子表；
  - 单子 `UNION ALL` 是否可达尚待验证。
- 上面这些查询如果再包含需要上层节点消费 tlist 的结构，尤其可疑：
  - 顶层 `ORDER BY` 使用了未出现在 `SELECT` 输出中的列；
  - `GROUP BY` / `DISTINCT` / window function 使用 `ressortgroupref`；
  - 顶层输出列名来自 append 父表而不是 child 表。

**为什么可能影响可观察结果：**
- `clean_up_removed_plan_level()` 会执行：
  - `child->initPlan = list_concat(parent->initPlan, child->initPlan);`
  - `apply_tlist_labeling(child->targetlist, parent->targetlist);`
- `apply_tlist_labeling()` 不只复制 `resname/resorigtbl/resorigcol`，还复制 `resjunk` 和 `ressortgroupref`。
- 因此可能影响：
  - 最终输出列名；
  - `resjunk` 列是否被隐藏；
  - 上层 `Sort`、`Group`、`WindowAgg` 是否能正确找到排序/分组表达式；
  - initPlan 的合并顺序和求值时机。

---

### 1.2 单子 Append Path 继承子 Path 的 cost/rows/pathkeys

**入口：**
- `src/backend/optimizer/util/pathnode.c`
  - `create_append_path()`：L1275–L1304
  - 分支：`if (list_length(pathnode->subpaths) == 1)`，约 L1282

**分支条件：**
- 创建 `AppendPath` 时传入的 `subpaths` 长度为 1。

**对应 SQL 构造形态：**
- 单子 appendrel 上的有序查询，例如：
  - `SELECT ... FROM partitioned_table WHERE partition_key = const ORDER BY child_indexed_col;`
- 当 child path 本身具有 `pathkeys` 时，新的 `AppendPath` 会继承这些 `pathkeys`、rows、startup_cost、total_cost。

**可能影响的可观察结果：**
- 单子 `AppendPath` 从“始终无序”变成“可以有序”；
- 规划器因此可能省略 `Sort` 节点、选择 MergeJoin 的排序输入等；
- 最终输出顺序直接取决于该路径是否真正满足查询顺序要求。

---

### 1.3 单子 MergeAppend Path 成本继承

**入口：**
- `src/backend/optimizer/util/pathnode.c`
  - `create_merge_append_path()`：L1426–L1446
  - 分支：`if (list_length(subpaths) == 1)`

**分支条件：**
- 创建 `MergeAppendPath` 时 `subpaths` 长度为 1。

**对应 SQL 构造形态：**
- 单子 appendrel 且规划器选择 MergeAppend 路径。
- 同样主要来自的有序查询：
  - `SELECT ... FROM partitioned_table WHERE <剪枝到单分区> ORDER BY <索引列>;`
- 可受 `enable_*`、成本参数、索引存在情况影响。

**可能影响：**
- 单子 `MergeAppendPath` 不再调用 `cost_merge_append()`，而是直接采用子路径的 startup/total cost；
- 可能改变规划器对 MergeAppend 路径的选择；
- 最终 `MergeAppend` 节点在 `setrefs.c` 中仍会因单子被移除。

---

### 1.4 单子 appendrel 的 ordered partial path

**入口：**
- `src/backend/optimizer/path/allpaths.c`
  - `add_paths_to_append_rel()`：L1708–L1745
  - 分支：`if (list_length(live_childrels) == 1)`

**额外条件：**
- `childrel->partial_pathlist` 中存在非最便宜的 partial path；
- 该 partial path 的 `path->pathkeys != NIL`；
- 该 partial path 不是 `linitial(childrel->partial_pathlist)`。

**对应 SQL 构造形态：**
- 单子 appendrel 上的并行有序查询，例如：
  - 分区表剪枝后只剩一个分区；
  - 查询带 `ORDER BY`；
  - child 上有可供有序扫描的索引；
  - 表足够大或并行成本参数降低，使并行路径被考虑。

**可能影响：**
- 新增有序 partial append paths；
- 规划器可能选择 `Gather Merge`，而不是普通 `Gather` + `Sort`；
- 输出顺序仍是 SQL 语义的一部分。

---

### 1.5 ExecSupportsMarkRestore 对单子 Append/MergeAppend 的判定

**入口：**
- `src/backend/executor/execAmi.c`
  - `ExecSupportsMarkRestore()`：L447–L482
  - 新增 `T_Append` 和 `T_MergeAppend` case

**分支条件：**
- `AppendPath->subpaths` 长度为 1；
- 或 `MergeAppendPath->subpaths` 长度为 1；
- 此时返回唯一 child path 的 mark/restore 能力。

**对应 SQL 构造形态：**
- 单子 appendrel 查询作为需要 mark/restore 的路径输入。
- 具体 SQL 场景可能包括：
  - `DECLARE ... SCROLL CURSOR FOR SELECT ... FROM single_child_appendrel ...;`
  - 作为 NestLoop 内侧，规划器需要判断是否要加 Materialize；
  - 其它需要 rescan 或 mark/restore 的路径。

**可能影响：**
- 计划中是否出现 `Materialize`；
- 游标 `FETCH BACKWARD` / `FETCH PRIOR` 的正确性；
- 对内表是否可被重新扫描的判定。

---

### 1.6 SubqueryScan 消除时的标签传播变化

**入口：**
- `src/backend/optimizer/plan/setrefs.c`
  - `set_subqueryscan_references()`：约 L1040
  - 改为调用 `clean_up_removed_plan_level()`

**分支条件：**
- `trivial_subqueryscan(plan)` 判定 SubqueryScan 可以消除。

**对应 SQL 构造形态：**
- 可被消除的平凡 SubqueryScan；
- 尤其当内外层 tlist 的 `resjunk` / `ressortgroupref` 标记不同时，旧代码不传播这些标记，新代码会传播。
- 但当前 `trivial_subqueryscan()` 仍对 resjunk 差异有保守限制，因此该路径的实际暴露面可能有限。

**可能影响：**
- 外层可见列数；
- 隐藏列是否被错误输出；
- 上层的排序/分组表达式匹配。

---

## 2. 输入性质、直接支持关系与尚待验证推断

### 2.1 源码直接支持的关系

以下关系是 diff 中明确写出的条件或赋值，不需要额外推断：

| 源码位置 | 直接支持的关系 |
|---|---|
| `setrefs.c: set_append_references()` | `appendplans` 长度为 1 时，Append 节点被移除，子节点上移 |
| `setrefs.c: set_mergeappend_references()` | `mergeplans` 长度为 1 时，MergeAppend 节点被移除，子节点上移 |
| `setrefs.c: clean_up_removed_plan_level()` | 移除父节点时，合并 initPlan，并用 `apply_tlist_labeling` 传播标签，包括 `resjunk`、`ressortgroupref` |
| `pathnode.c: create_append_path()` | `subpaths` 长度为 1 时，AppendPath 继承 child 的 `rows`、`startup_cost`、`total_cost`、`pathkeys` |
| `pathnode.c: create_merge_append_path()` | `subpaths` 长度为 1 时，MergeAppendPath 继承输入 startup/total cost |
| `allpaths.c: add_paths_to_append_rel()` | `live_childrels` 长度为 1 时，为非最便宜且有序的 child partial paths 创建 append partial paths |
| `execAmi.c: ExecSupportsMarkRestore()` | 单子 Append/MergeAppend path 的 mark/restore 能力等于唯一 child path |

### 2.2 尚待验证的推断

以下是要通过实际规划器行为才能确认是否可达的推断：

- **哪些 SQL 语句会生成单子 Append/MergeAppend 最终节点**  
  推断：单分区、分区剪枝到只剩一个分区、单子继承树。  
  但尚需用 `EXPLAIN` 验证是否存在这种节点。

- **哪些上层节点会真正消费 `ressortgroupref`**  
  推断：`Sort`、`Group`、`WindowAgg`、`Unique` 等。  
  但需要确认单子 Append/MergeAppend 上是否真的有这些节点。

- **哪些 ordered partial path 会实际被加入并被选中**  
  推断：并行查询 + `ORDER BY` + child 索引。  
  但受成本参数、表大小、统计信息影响，需要实际触发。

- **`ExecSupportsMarkRestore` 的单子分支是否被某类 SQL 实际调用**  
  推断：滚动游标、NestLoop 内侧物化决策。  
  但没有本文之外的调用链证据，需要下一阶段跟踪验证。

- **`SubqueryScan` 标签差异是否能在平凡消除场景中暴露出来**  
  推断：某个 `trivial_subqueryscan` 成功消除，同时内外层 `resjunk` 标记不同。  
  但代码注释提到当前限制可能阻止多数这类匹配。

### 2.3 区分“直接支持”和“推断”的对照方法

- 用 `EXPLAIN (VERBOSE, COSTS OFF)` 看最终计划：
  - 是否还存在 `Append` / `MergeAppend`；
  - 是否出现 `Gather Merge`、`Sort`、`Materialize`；
  - 是否出现 SubqueryScan 消除现象。
- 查系统目录确认 appendrel 实际 child 数量：
  - `pg_inherits`
  - `pg_partition_tree`
  - 分区绑定信息
- 建立直接子表的语义等价查询作为对照。
- 观察列描述：使用 `SELECT * ... LIMIT 0` 或客户端元数据接口，确认输出列数量、列名、是否多出隐藏列。
- 对 `ORDER BY` / `GROUP BY` / window 查询，比较实际输出行和顺序。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 独立验证方法

1. **确认计划命中路径**
   - 对每个候选 SQL，在目标版本上运行：
     ```text
     EXPLAIN (VERBOSE, COSTS OFF) ...
     ```
   - 检查是否出现或消失以下节点：
     - 单子 `Append`
     - 单子 `MergeAppend`
     - `Gather Merge`
     - `Sort`
     - `Materialize`
     - 被消除的 `SubqueryScan`
   - 这一步只用于确认代码路径被覆盖，不用于判定结果正确性。

2. **建立语义基准**
   - 对同一个候选，构造一个不经过 append 规划路径的等价查询：
     - 直接查询唯一存活 child 表；
     - 或者使用相同条件但手动限制到 child 表。
   - 基准查询需要在列类型、列顺序、排序表达式上等价。

3. **比较行集和顺序**
   - 使用 `EXCEPT ALL` 双向比较：
     - `candidate EXCEPT ALL baseline`
     - `baseline EXCEPT ALL candidate`
   - 对无序查询，比较 row count 和行集合。
   - 对有序查询，额外比较行顺序。

4. **比较列描述**
   - 检查最终输出列名、列数量。
   - 对 `ORDER BY` 中未选出的列，确认其是隐藏列，不会出现在客户端输出中。
   - 特别关注：
     - `resjunk` 导致的隐藏列；
     - `resname` 错误导致的列名变化；
     - 顶层 tlist 标签从 parent 复制到 child 后的正确性。

5. **聚合 / 窗口 / 分组查询**
   - 将候选查询与直接 child 基准查询的聚合结果逐行比较。
   - 关注是否因为 `ressortgroupref` 不匹配出现“could not find pathkey item to sort”等错误。

6. **游标 / mark/restore 验证**
   - 对涉及 `ExecSupportsMarkRestore` 的候选，使用显式游标：
     ```text
     DECLARE c SCROLL CURSOR FOR ...
     FETCH FORWARD ...
     FETCH BACKWARD ...
     FETCH PRIOR ...
     ```
   - 与直接 child 表游标行为比较。
   - 检查计划中是否出现或消失 `Materialize`，并验证回滚读取的行序和完整性。

7. **两版本对照**
   - 将目标版本和第一父版本的计划做对比。
   - 计划变化只说明触发了提交，不代表结果错误。
   - 如果用上面的基准证明目标版本结果与直接 child 查询一致，则说明语义正确。
   - 如果某个用例两版结果不同，必须再比较基准，才能判断哪一版是对的。

### 3.2 仍缺少的证据

- **提交自带回归测试的完整 SQL 和预期输出**  
  本文没有提供该提交对应的回归测试或基准输出。

- **实际规划器能否稳定生成单子 Append / MergeAppend 节点**  
  需要真实建表、统计信息、成本参数来验证。

- **哪些上层节点会直接暴露 `ressortgroupref` 传播问题**  
  目前推断为 `Sort`、`Group`、`WindowAgg`，但需要 `EXPLAIN VERBOSE` 确认其 tlist 引用。

- **`ExecSupportsMarkRestore` 的调用链**  
  本文没有提供其所有调用方；需要源码索引确认哪些 SQL 特性实际依赖该函数。

- **部分场景是否真正产生用户可见错误**  
  例如：
  - 标签错误可能只影响列名，不影响行数据；
  - `resjunk` 传播可能只影响计划内部，不一定是错误；
  - `ressortgroupref` 传播问题可能只在极其特定的表达式组合中暴露。

- **数据集大小、统计信息和 cost 参数**  
  尤其是触发：
  - 单子 ordered partial path；
  - `Gather Merge`；
  - 单子 `MergeAppend` path；
  这些都需要精确的 `VACUUM ANALYZE`、并行参数和成本设置。

---

## 小结

下一阶段应优先围绕以下 SQL 构造类生成可执行用例：

1. 分区/继承表剪枝到单子，加 `ORDER BY` 非输出列。
2. 分区/继承表剪枝到单子，加 `GROUP BY` / window / distinct。
3. 分区/继承表剪枝到单子，加并行 ordered path。
4. 单子 appendrel 上的滚动游标。
5. 可消除的平凡 SubqueryScan，且内外层 tlist 可能存在 resjunk 差异。

这些候选均有明确代码分支支撑；但每个用例都必须用 `EXPLAIN` 确认路径，并用直接 child 查询建立独立语义基准，才能最终判断正确性。