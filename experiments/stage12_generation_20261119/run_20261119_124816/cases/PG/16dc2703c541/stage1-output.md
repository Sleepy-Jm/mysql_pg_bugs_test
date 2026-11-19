## 1. 可能进入改动路径的 SQL 构造

新增的 `JOIN_RIGHT_ANTI` 是为了支持 **反连接（anti join）的另一种输入顺序**。原 `JOIN_ANTI` 返回左侧输入中没有匹配的行；`JOIN_RIGHT_ANTI` 则是交换左右输入后返回原右侧输入中没有匹配的行，逻辑上仍与原反连接等价。

### 入口 SQL 构造

任何会在 PostgreSQL 规划器中产生 **`JOIN_ANTI`** 的查询都可能进入新路径。典型构造包括：

- `NOT EXISTS (subquery)`
- `NOT IN (subquery)`（在满足安全条件，不引入额外 null 处理时）
- 其他由子查询消去产生的反连接

这些查询原先生成 `JOIN_ANTI`；现在在 `populate_joinrel_with_paths` 的 `JOIN_ANTI` 分支中，额外调用了 `add_paths_to_joinrel(... JOIN_RIGHT_ANTI ...)`，从而可能生成右反连接计划。

### 代码入口与限制条件

| 文件/函数 | 行号（目标版本） | 说明 |
|-----------|------------------|------|
| `src/backend/optimizer/path/joinrels.c` — `populate_joinrel_with_paths` | L928–L930 | 在 `JOIN_ANTI` 分支中新增 `add_paths_to_joinrel(root, joinrel, rel2, rel1, JOIN_RIGHT_ANTI, sjinfo, restrictlist)`。这是唯一的规划器入口。 |
| `src/backend/optimizer/path/joinpath.c` — `match_unsorted_outer` | L1666–L1685 | `JOIN_RIGHT_ANTI` 与 `JOIN_RIGHT`、`JOIN_FULL` 一样：`nestjoinOK = false`，`useallclauses = true`。即 **禁止 nestloop**，merge join 必须使用全部 merge clauses 作为 join clauses。 |
| `src/backend/optimizer/path/joinpath.c` — `select_mergejoin_clauses` | L2305–L2313 | `JOIN_RIGHT_ANTI` 与 `JOIN_RIGHT`、`JOIN_FULL` 一样：如果存在非 mergejoinable 且非常量的 join clause，则 `mergejoin_allowed = false`，因此 **merge join 只允许常量附加条件**。 |
| `src/backend/optimizer/path/joinpath.c` — `hash_inner_and_outer` | L2228–L2236 | `JOIN_RIGHT_ANTI` 与 `JOIN_FULL`、`JOIN_RIGHT` 一样，**不能使用并行 hash join**，因为 match bit 无法跨进程维护。但普通 hash join 路径可用。 |
| `src/backend/optimizer/path/joinpath.c` — `sort_inner_and_outer` | L1262–L1265 | `JOIN_RIGHT_ANTI` 同样被排除在并行 merge join 之外。 |
| `src/backend/optimizer/path/joinpath.c` — `match_unsorted_outer` 并行部分 | L1852–L1856 | `JOIN_RIGHT_ANTI` 同样被排除在并行 nestloop/merge join 之外。 |

### 执行器改动（可能被右反连接路径触达）

| 文件/函数 | 行号 | 关键逻辑 |
|-----------|------|----------|
| `src/backend/executor/nodeHashjoin.c` — `ExecHashJoinImpl` | L519–L522 | 匹配时，`JOIN_RIGHT_ANTI` 不返回元组，并继续扫描当前 bucket 以标记所有匹配的 inner 元组。 |
| `src/backend/executor/nodeHashjoin.c` — `ExecHashJoinImpl` | L572–L598 | `HJ_FILL_INNER_TUPLES` 对 `right/right-anti/full` 均执行未匹配 inner 扫描，生成 `outer` 为 NULL 的填充元组。 |
| `src/backend/executor/nodeHashjoin.c` — `ExecInitHashJoin` | L741–L744 | `JOIN_RIGHT_ANTI` 与 `JOIN_RIGHT` 一样初始化 `hj_NullOuterTupleSlot`。 |
| `src/backend/executor/nodeHashjoin.c` — `ExecHashJoinNewBatch` | L1037–L1040 | 处理 inner batch 时，`right/right-anti/full` join 即使 outer batch 为空也要扫描 inner。 |
| `src/backend/executor/nodeHashjoin.c` — `ExecReScanHashJoin` | L1360–L1363 | 重扫描时，`right/right-anti/full` join 需要重置 inner 元组的 match flags。 |
| `src/backend/executor/nodeMergejoin.c` — `ExecMergeJoin` | L805–L812 | 匹配时，`JOIN_RIGHT_ANTI` 不返回元组，并保持当前 outer 继续扫描 inner。 |
| `src/backend/executor/nodeMergejoin.c` — `ExecMergeJoin` | L1071–L1075 | `JOIN_RIGHT_ANTI` 要求 extra joinquals 为常量，否则 planner 不应生成该计划。 |
| `src/backend/executor/nodeMergejoin.c` — `ExecMergeJoin` | L1340–L1343 | `EXEC_MJ_ENDOUTER` 阶段，`right/right-anti/full` join 需要 null-fill 剩余未匹配 inner。 |
| `src/backend/executor/nodeMergejoin.c` — `ExecInitMergeJoin` | L1562–L1570 | `JOIN_RIGHT_ANTI` 与 `JOIN_RIGHT` 一样初始化 `mj_FillOuter=false`、`mj_FillInner=true` 以及 `mj_NullOuterTupleSlot`。 |

---

## 2. 输入性质对可观察结果的影响

### 源码直接支持的关系

以下输入性质在改动后的执行器或规划器代码中有明确处理，属于**直接支持**：

- **重复匹配**：  
  Hash join 在 `JOIN_RIGHT_ANTI` 匹配分支中 `continue`，可继续扫描当前 bucket，确保一个 left 行匹配多个 right 行时，所有匹配的 right 行都被标记。Merge join 类似，在匹配后 `break` 但状态机继续处理 inner，保证多匹配被标记。

- **未匹配填充**：  
  对于 `JOIN_RIGHT_ANTI`，执行器会扫描未匹配的 inner（即原右表）并使用 NULL outer 填充返回，且 `otherqual` 会在填充时重新评估（和 right join 行为一致）。

- **空输入**：  
  Hash join 的早期退出检查已将 `JOIN_RIGHT_ANTI` 与 right/full join 同样对待：即使 outer 为空，也必须构建 hash 表并扫描未匹配 inner。批处理逻辑也覆盖了 outer 为空但 inner 有元组的情况。

- **批处理 hash join**：  
  未匹配 inner 扫描在 `HJ_FILL_INNER_TUPLES` 阶段执行，跨 batch 处理已有对应逻辑。重扫描时会重置 match flags，避免旧状态影响新执行。

- **非连接条件（otherquals）**：  
  Hash join 和 merge join 都会在返回元组前应用 `otherqual`。在 right anti 中，匹配行不会返回；未匹配 inner 填充行会以 NULL outer 应用 `otherqual`。

- **并行的禁止**：  
  规划器明确禁止 right anti 的并行 hash join 和并行 merge join，因此不会出现 match bit 分片导致的错误。

### 尚待验证的推断

以下关系**不是源码直接断言**，而是基于现有逻辑的推断，需要通过实验验证：

- **逻辑等价性**：`JOIN_RIGHT_ANTI` 应与交换输入后的原 `JOIN_ANTI` 产生完全相同的结果集。该等价性未被显式证明，需通过组合测试验证。

- **NULL 与重复组合**：  
  当 join 列存在 NULL 且某侧有大量重复时，右反连接的 match flag 与 unmatched 扫描是否仍能正确工作，尤其涉及 hash join 的 bucket 内顺序。

- **批处理边角**：  
  当 `work_mem` 导致 hash 表分多个 batch，且未匹配 inner 行分布在多个 batch 中时，最终输出是否完整且不重复。

- **merge join 的 mark/restore 与常量 extra quals**：  
  当存在常量 true/false 的 extra joinqual 时，merge join 的 `mj_SkipMarkRestore` 及 `EXEC_MJ_ENDOUTER` 是否仍正确，尚无直接验证。

- **常量 false 条件**：  
  `populate_joinrel_with_paths` 中 `JOIN_ANTI` 分支的 `restriction_is_constant_false` 检查可能会提前 `mark_dummy_rel`，导致 `JOIN_RIGHT_ANTI` 路径不被生成。这是否会在某些常量 false 条件下造成结果错误或计划缺失，有待验证。

### 用于区分“直接支持”与“推断”的对照

要区分上述关系是真实可靠还是只是推断，需要进行对照实验：

- **强制不同计划形状**：  
  使用 GUC 参数（如 `enable_hashjoin`、`enable_mergejoin`、`enable_nestloop`）控制生成 **LEFT ANTI** 或 **RIGHT ANTI** 计划，比较两者结果。若结果一致，支持等价性；若不一致，则定位到具体 executor 分支。

- **改变输入数据性质**：  
  分别构造包含 NULL、重复、空表、多匹配、异或条件的数据集，观察 RIGHT ANTI 计划是否与 LEFT ANTI 或标准 SQL 参考结果一致。

- **调整 `work_mem`**：  
  在 hash join 中通过设置小 `work_mem` 强制触发多 batch，验证未匹配扫描的正确性。

- **使用 `EXPLAIN` 确认计划**：  
  检查输出计划中包含 `Right Anti` 节点，确保测试确实覆盖了新路径。

---

## 3. 独立验证结果正确性的方法与缺失证据

### 独立验证方法

1. **计划验证**  
   使用 `EXPLAIN` 确认查询使用了 `Right Anti` join 节点，并记录其类型（hash 或 merge）。确保候选 SQL 确实触达新增代码。

2. **结果等价性验证**  
   对同一查询，分别强制生成 LEFT ANTI 计划（如关闭 hash/merge join，使其只能使用 nestloop，或直接改写查询）和 RIGHT ANTI 计划（保留可用的 hash/merge join），比较两者结果集是否完全一致（行序无关）。

3. **参考语义验证**  
   对 anti join 查询改写为标准 SQL 等价形式（例如 `LEFT JOIN ... WHERE right IS NULL`）作为语义参考，与 RIGHT ANTI 计划结果比较。

4. **数据性质组合测试**  
   设计表结构和数据覆盖：
   - 空表
   - 单行
   - 重复行
   - NULL 键值
   - 多行匹配
   - 常量 true/false 附加条件
   - 含非等值连接条件（仅 hash join 可支持；merge join 应被 planner 禁止）
   - 含可排序但非等值的 merge join 条件（如 `<` 或 `>`？注意 merge join 通常需要等值或可排序等值，但 extra quals 可为常量）

5. **批处理与重扫描测试**  
   - 使用小 `work_mem` 强制 hash join 分批。
   - 将 right anti join 放入嵌套循环内，验证 `ExecReScanHashJoin` 是否正确重置 match flags。

6. **对照回归测试**  
   在目标版本和第一父版本上执行相同的 SQL（父版本不支持 right anti，可能生成 LEFT ANTI），比较结果。但需注意：**结果不同不一定说明错误**，必须进一步确认哪个结果符合 SQL 语义。

### 仍缺少的证据

- **尚无任何可执行 SQL 测试结果**。候选测试用例仅停留在结构描述，未实际执行。
- **未验证 planner 在哪些具体查询和数据分布下会实际选择 `JOIN_RIGHT_ANTI`**。需要确认新路径不是死代码，同时了解其选择条件（例如表大小、统计信息、GUC）。
- **未验证执行器所有分支的正确性**：  
  - hash join 的 normal batch、rescan、分批未匹配扫描  
  - merge join 的 `EXEC_MJ_JOINTUPLES`、`EXEC_MJ_ENDOUTER` 及 mark/restore  
  - 空输入、全匹配、零匹配等极端情况
- **未验证逻辑等价性**：即 `JOIN_RIGHT_ANTI` 是否永远与交换输入的 `JOIN_ANTI` 等价，特别是在存在其他过滤条件、重复、NULL 时。
- **未验证常量 false/true 等边角条件的 planner 与 executor 行为**。特别是 planner 的 `restriction_is_constant_false` 检查是否对 right anti 处理恰当。
- **未验证并行相关限制是否完全生效**，即并行 hash/merge join 不会意外生成 right anti 计划。

以上证据需通过下一阶段的完整 SQL 测试补齐。