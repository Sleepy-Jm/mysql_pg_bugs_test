## 1. 可能进入改动路径的 SQL 构造

改动入口位于 **外层查询对含窗口函数的子查询的过滤条件**，且该过滤条件无法下推到子查询。具体入口与分支条件如下。

### 1.1 入口函数与分支

| 文件 | 函数 | 行号 | 作用 |
|---|---|---|---|
| `src/backend/optimizer/path/allpaths.c` | `set_subquery_pathlist` | 约 L2509–2535 | 对子查询 RTE 上的 `baserestrictinfo` 逐个判断：若 `qual_is_pushdown_safe` 为假，且子查询 `hasWindowFuncs` 为真，则调用 `check_and_push_window_quals`；否则保留 upper qual |
| `src/backend/optimizer/path/allpaths.c` | `check_and_push_window_quals` | 约 L2365–2415 | 只处理二元 `OpExpr`；检查左右任一侧是否为 `Var`，且该 `Var` 对应子查询 targetlist 中的 `WindowFunc`（允许被 `RelabelType` 包裹） |
| `src/backend/optimizer/path/allpaths.c` | `find_window_run_conditions` | L2183–2363 | 调用窗口函数 `prosupport` 判断单调性；检查另一侧是否伪常量；检查 btree 操作符策略是否匹配，并生成 run condition |
| `src/backend/optimizer/plan/planner.c` | `create_one_window_path` | L4282–4300 | 将下层 `WindowClause.runCondition` 累积到顶层 `WindowAgg` 的 qual；标记 `topwindow` |
| `src/backend/optimizer/plan/createplan.c` | `make_windowagg` | L6562–6586 | 将 `runCondition`、`qual`、`topWindow` 写入 `WindowAgg` 计划节点 |
| `src/backend/optimizer/plan/setrefs.c` | `set_windowagg_runcondition_references` | L3094–3147 | 将 run condition 中的 `WindowFunc` 替换为对投影结果的 `Var` 引用 |
| `src/backend/executor/nodeWindowAgg.c` | `ExecWindowAgg` | L2121–2342 | 执行时根据 `runCondition` 和 `qual` 决定是否提前终止、进入 pass-through 或过滤行 |
| `src/backend/executor/nodeWindowAgg.c` | `spool_tuples` | L1248–1315 | 在 pass-through 模式下跳过存储或全部读取当前分区 |
| `src/backend/executor/nodeWindowAgg.c` | `ExecInitWindowAgg` | L2403–2425 | 初始化 run condition、qual、pass-through 模式标记 |
| `src/backend/commands/explain.c` | `ExplainNode` | 约 L1988–2000 | 显示 `WindowAgg` 的 `Filter` 与 `Run Condition` |

### 1.2 必须同时满足的条件

进入改动路径的核心 SQL 构造必须同时满足：

1. **存在子查询**，且子查询包含窗口函数。
2. 外层查询的 `baserestrictinfo` 中存在对该子查询的过滤条件，且 `qual_is_pushdown_safe` 判定为**不能下推**。
3. 该过滤条件是**二元 `OpExpr`**，即 `<`、`<=`、`=`、`>`、`>=` 或与之等价的 btree 操作符。
4. `OpExpr` 的某一侧是 `Var`，并且该 `Var` 直接引用子查询 targetlist 中的某个 `WindowFunc`（可被 `RelabelType` 包裹）。
5. 另一侧必须是 `is_pseudo_constant_clause` 返回真的表达式，即在整个窗口分区内不改变值。
6. 窗口函数必须属于支持列表，且支持函数返回的单调性非 `MONOTONICFUNC_NONE`：
   - `row_number()`
   - `rank()`
   - `dense_rank()`
   - `count(*)`
   - `count(expr)`
7. 操作符的 btree 策略必须与窗口函数单调方向匹配（见下）。

### 1.3 具体构造类别

#### A. 递增窗口函数 + 上界比较

窗口函数：`row_number()`、`rank()`、`dense_rank()`，或 `count(*)`/`count(expr)` 在递增窗口帧下。

窗口函数在操作符左侧时：
- `wfunc < const`
- `wfunc <= const`
- `wfunc = const`（`=` 会转换为 `<=` 并保留原 equal qual）

窗口函数在操作符右侧时：
- `const > wfunc`
- `const >= wfunc`

会导致生成 run condition，且原始上层过滤条件可能被移除（`keep_original = false`）或部分保留。

#### B. 递减窗口函数 + 下界比较

窗口函数：`count(*)`/`count(expr)` 在递减窗口帧下，例如：
```sql
count(*) OVER (ORDER BY a ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
```

窗口函数在操作符左侧时：
- `wfunc > const`
- `wfunc >= const`

窗口函数在操作符右侧时：
- `const < wfunc`
- `const <= wfunc`

#### C. 恒定窗口函数 + 等值比较

窗口函数为 `count(*)`/`count(expr)`，且窗口满足：
- 无 `ORDER BY`，或
- 同时具有 `UNBOUNDED PRECEDING` 和 `UNBOUNDED FOLLOWING`

此时单调性为 `MONOTONICFUNC_BOTH`，等值比较 `wfunc = const` 可直接作为 run condition，且原始 filter 不再保留。

#### D. 带 `PARTITION BY` 的窗口函数

任意上述窗口函数如果带有 `PARTITION BY`，则：
- `use_pass_through = true`，
- run condition 在分区内失效后不会直接终止，而是进入 `WINDOWAGG_PASSTHROUGH_STRICT` 模式，
- 到下一分区时恢复 `WINDOWAGG_RUN`。

#### E. 多个不同 `WindowClause` 产生多层 `WindowAgg`

当查询包含多个不同的窗口定义（即不同的 `WindowClause`）时，会堆叠多个 `WindowAgg` 节点。对于非顶层 `WindowAgg`：
- `topWindow = false`，
- run condition 失效后进入 `WINDOWAGG_PASSTHROUGH` 模式，
- 其 run condition 不会作为该节点的 qual，而是累积到顶层 `WindowAgg` 的 qual。

此类构造可能进入 pass-through 并影响上层窗口函数的输入。

## 2. 到达后影响可观察结果的输入性质

### 2.1 源码直接支持的关系

这些关系可直接从代码分支看出来，属于确定性行为：

| 输入性质 | 影响 | 依据 |
|---|---|---|
| 操作符方向与单调方向是否匹配 | 决定是否生成 run condition；不匹配则不进入改动路径，查询保持原状 | `find_window_run_conditions` 中 `< <= > >=` 分支 |
| 窗口函数是否在支持列表 | 只有 `row_number`、`rank`、`dense_rank`、`count` 可触发 | `pg_proc.dat` 中 `prosupport` 字段；`get_func_support` 检查 |
| 另一侧是否为伪常量 | 若不是伪常量则不生成 run condition | `find_window_run_conditions` 中 `is_pseudo_constant_clause` 检查 |
| 窗口函数列是否有 cast/RelabelType | 代码会剥离一层 RelabelType 后再取 WindowFunc | `find_window_run_conditions` 开头 `while (IsA(wfunc, RelabelType))` |
| 是否有 `PARTITION BY` | 有分区时 `use_pass_through = true`，run condition 失效后进入 `PASSTHROUGH_STRICT` 而非直接终止 | `ExecInitWindowAgg` 中 `use_pass_through = !node->topWindow || node->partNumCols > 0` |
| 是否为顶层 `WindowAgg` | 非顶层进入 `PASSTHROUGH` 且仍返回元组；顶层进入 `PASSTHROUGH_STRICT` 后当前分区内不再返回剩余行 | `ExecWindowAgg` 中状态转换分支 |
| 原始条件是否保留 | `< <= > >=` 匹配时 `keep_original=false`，原始 qual 不保留；`=` 时 `keep_original=true`，原始 equal qual 保留 | `find_window_run_conditions` 中各分支 |
| 窗口函数是否 `MONOTONICFUNC_BOTH` | 等值条件可直接当作 run condition，原始 filter 被移除 | `find_window_run_conditions` 中 `=` 分支 |

### 2.2 尚待验证的推断

这些属于代码间接暗示或未提供的实现细节，需要测试确认：

| 输入性质 | 可能的影响 | 验证必要性 |
|---|---|---|
| 外层另一侧表达式包含 volatile 函数、相关子查询或外部参数 | `is_pseudo_constant_clause` 可能误判为分区内不变，导致 run condition 错误停止 | 高 |
| `count(expr)` 带 `FILTER` 子句 | 支持函数 `int8inc_support` 未显式处理 `FILTER`，其单调性可能仍成立，但需验证 | 中 |
| 窗口帧带 `EXCLUDE` 子句 | `int8inc_support` 只看 `frameOptions`，可能未覆盖 `EXCLUDE` 对行可见性的影响 | 中 |
| 窗口函数结果列被 cast 为不同类型 | run condition 生成时使用剥离 RelabelType 后的 wfunc，可能造成操作符参数类型不匹配 | 中 |
| `get_op_btree_interpretation` 返回多个 interpretation | 循环中 `< <=` 或 `> >=` 分支无条件 `break`，可能仅检查第一个策略，漏掉后续匹配 | 低 |
| 多窗口堆叠时非顶层 pass-through 返回的行 | 行缺少下层窗口函数值，可能影响上层窗口函数计算 | 高 |
| 有 peer 组时 `rank()`/`dense_rank()` 的等值条件 | 转换为 `<=` 后，peer 组内值相同，理论上安全，但需验证边界 | 中 |
| 分区的边界行恰好使 run condition 失效 | 进入 `PASSTHROUGH_STRICT` 后，当前分区剩余行全部不返回；若分区检测有误可能丢行 | 高 |

### 2.3 能区分两者的对照

可构造“不进入改动路径”的等语义查询作为对照，比较结果：

- 将窗口函数替换为**不支持单调性的窗口函数**，例如 `percent_rank()`、`lag()`；
- 使用**非 btree 操作符**，例如 `<>`；
- 使另一侧**不是伪常量**，例如引用子查询中的普通列；
- 用**第一父版本**运行相同查询，对照返回行集合；
- 对相同窗口函数分别构造**匹配方向**和**非匹配方向**的比较，例如 `row_number() > const`（非匹配）与 `row_number() < const`（匹配）。

这些对照可以区分：
- 两个版本结果不同是否由 run condition 造成；
- run condition 是否严格等价于原始 filter；
- pass-through 模式是否影响多层窗口或分区内过滤。

## 3. 独立验证结果正确性的方法及缺少的证据

### 3.1 验证方法

1. **建立语义真值**  
   对每个候选构造，使用小数据集手工计算预期输出行集合。或者将子查询物化（例如 `CREATE TEMP TABLE` / CTE 物化）后再过滤窗口函数结果，得到等价基准。

2. **对照第一父版本**  
   运行同一 SQL 于第一父版本，作为语义正确的参考。目标版本结果与之不一致时，需要人工判定是否为真正的语义错误。

3. **利用 `EXPLAIN` 确认路径已进入**  
   使用 `EXPLAIN (ANALYZE, VERBOSE, COSTS OFF)` 观察 `WindowAgg` 节点是否出现 `Run Condition` 和 `Filter`。若出现，说明该构造已进入改动路径；若没出现，则需要调整输入条件。

4. **边界值测试**  
   常量选择：
   - 等于窗口函数最小值；
   - 等于最大值；
   - 小于最小值；
   - 大于最大值；
   - 恰好位于分区边界两侧；
   - 等于 peer 组重复值。

5. **分区与多层窗口专项测试**  
   - 有 `PARTITION BY` 的多分区数据；
   - 多个不同窗口定义的堆叠；
   - 外层引用第一层窗口函数结果再过滤。

### 3.2 仍缺少的证据

- **实际执行 SQL 的输出结果**：当前仅从代码推断，没有测试结果。
- **`is_pseudo_constant_clause` 的具体实现**：未提供，无法确定其对 volatile/相关子查询/外部参数的处理是否会导致伪常量误判。
- **`get_op_btree_interpretation` 对跨类型运算符的返回细节**：未提供，无法确认循环中的无条件 `break` 是否可能漏掉可用的 btree interpretation。
- **`count` 聚合支持函数与 `FILTER`、`EXCLUDE`、`NULLS FIRST/LAST` 等组合行为的测试证据**：当前实现仅检查 `orderClause` 和三个 frame 标志位，故这些组合是否安全尚需验证。
- **多层 `WindowAgg` 下 pass-through 返回行对上层窗口函数计算正确性的验证**：没有执行结果支撑。
- **复现测试的完整可执行 SQL**：按要求留待下一阶段。

因此，本阶段可以确定的候选构造集中在：  
**支持的 5 类窗口函数 × 匹配的操作符方向 × 有无 PARTITION BY × 是否为多层 WindowAgg** 的组合上。其余涉及 FILTER/CAST/特殊 frame 的组合，尚属推断，不列为强候选。