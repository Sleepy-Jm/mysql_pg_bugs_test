## 1. 可进入改动路径的 SQL 构造

### 1.1 入口链

| 位置 | 说明 |
|---|---|
| `sqlite3Select` · `src/select.c` L4899–4912 | 带 `pPrior` 的复合查询统一进入 `multiSelect` |
| `multiSelect` · `src/select.c` L2248–2250 | 若复合查询本身有 `ORDER BY`，进入 `multiSelectOrderBy`，**不会到达本次改动** |
| `multiSelect` · `src/select.c` L2254 `switch(p->op)` | 改动仅在 `case TK_ALL:`，即 `UNION ALL` |
| `multiSelect` · `src/select.c` L2273–2285 | 新增块位于左臂 `sqlite3Select(... pPrior ...)` 之后、右臂 `sqlite3Select(... p ...)` 之前 |

### 1.2 触发条件

源码直接支持：

- 查询是 `UNION ALL`，不是 `UNION`、`INTERSECT`、`EXCEPT`。
- 复合查询没有顶层 `ORDER BY`；否则早退到 `multiSelectOrderBy`。
- 存在 `LIMIT`，即 `p->iLimit` 寄存器存在。
- 存在 `OFFSET`，即 `p->iOffset` 寄存器存在。
  - 这里 `p->iLimit`、`p->iOffset` 是寄存器编号，`0` 表示不存在。
  - 因此 `LIMIT ... OFFSET ...` 即使 `OFFSET` 运行时值为 0，也会生成这个新增块。

### 1.3 新增块直接语义

目标版本新增块为 `src/select.c` L2276–2285：

```c
if( p->iOffset ){
  int addr2;
  sqlite3VdbeAddOp3(v, OP_Add, p->iLimit, p->iOffset, p->iOffset+1);
  addr2 = sqlite3VdbeAddOp1(v, OP_IfPos, p->iOffset); VdbeCoverage(v);
  sqlite3VdbeAddOp2(v, OP_SCopy, p->iLimit, p->iOffset+1);
  sqlite3VdbeJumpHere(v, addr2);
  addr2 = sqlite3VdbeAddOp1(v, OP_IfPos, p->iLimit); VdbeCoverage(v);
  sqlite3VdbeAddOp2(v, OP_Integer, -1, p->iOffset+1);
  sqlite3VdbeJumpHere(v, addr2);
}
```

它相当于根据当前运行时寄存器值重新计算 `iOffset+1`：

- 先计算 `iLimit + iOffset`。
- 若当前 `iOffset <= 0`，用当前 `iLimit` 覆盖 `iOffset+1`。
- 若当前 `iLimit <= 0`，把 `iOffset+1` 设为 `-1`。
- 否则保持二者之和。

也就是说，它重算了“剩余 LIMIT + 剩余 OFFSET”。

### 1.4 可能消费该寄存器的位置

根据提供的代码：

- `computeLimitRegisters` · `src/select.c` L1791–1863  
  初始化 `iOffset+1` 为 `LIMIT+OFFSET`；注释还说明 `UNION ALL` 会跨多个 SELECT 复用 limit/offset 寄存器。
- `pushOntoSorter` · `src/select.c` L568–587  
  当 SELECT 有 `iLimit` 且 `iOffset` 时，使用 `pSelect->iOffset+1` 作为排序器保留行数。
- `codeOffset` · `src/select.c` L589–604  
  读取 `iOffset` 来跳过 OFFSET 行。

因此，若右臂没有排序，`iOffset+1` 在提供的代码中没有被消费。  
最可能受影响的 SQL 形态是：

> `UNION ALL` + 顶层 `LIMIT`/`OFFSET`，且右臂内部有 `ORDER BY`，从而触发 sorter/pushOntoSorter。

注意：复合顶层的 `ORDER BY` 会走到 `multiSelectOrderBy`，不会进入此路径；这里的 `ORDER BY` 必须是嵌套在右臂内，例如括号子查询或等效形态。

---

## 2. 影响结果可观察性的输入性质

### 2.1 源码直接支持的关系

以下关系可从当前提供的源码中直接推出：

1. **仅 `UNION ALL` 受影响**  
   新增代码在 `TK_ALL` 分支。

2. **必须有 `LIMIT offset` 组合**  
   条件为 `p->iLimit` 且 `p->iOffset` 都存在。

3. **重算发生在左臂之后、右臂之前**  
   因此左臂是否消费了行、是否使 limit/offset 计数器发生变化，会决定右臂开始时 `iOffset+1` 的新值。

4. **新值依赖当前 `iLimit` 和 `iOffset` 的符号**  
   从新增 opcode 可看出：
   - `iOffset <= 0`：`iOffset+1` 被设为 `iLimit`
   - `iLimit <= 0`：`iOffset+1` 被设为 `-1`
   - 两者都正：`iOffset+1` 为两者之和

5. **`pushOntoSorter` 是已展示的唯一 `iOffset+1` 消费者**  
   它只在右臂有排序缓存时才有机会影响右臂行处理。

### 2.2 尚待验证的推断

以下是通过逻辑推演出来的，但还没有被完整源码或执行结果直接证明：

1. **左臂执行确实会改变 `iLimit`/`iOffset` 寄存器**  
   现有代码注释和 opcode 名称暗示 limit/offset 计数器会在输出/跳过时变化，但完整 select loop 源码未给出。

2. **右臂排序结果是最终可观察差异的唯一可能来源**  
   从提供的代码看，`iOffset+1` 只被 `pushOntoSorter` 消费；但不能排除未提供的代码中还有其他消费者。

3. **结果差异不一定出现**  
   因为 `iOffset+1` 在 `pushOntoSorter` 中更像“排序器最多保留多少行”的优化参数。  
   如果旧值偏大，排序器只是多保留一些行，最终 `OFFSET/LIMIT` 仍可能返回相同行。  
   也就是说，这次改动可能只是减少内存/排序器容量，未必改变 SQL 返回结果。

4. **右臂 sorter 保留较多行不会自然导致错误**  
   若 sorter 只会删除排序末尾的行，那么“多保留行”通常不会改变最前面的剩余 `LIMIT+OFFSET` 行。

### 2.3 可区分上述关系的对照

要区分“影响执行”和“影响结果”，应设置以下对照：

| 对照因素 | 目的 |
|---|---|
| 右臂有 `ORDER BY` vs 右臂无 `ORDER BY` | 判断 `iOffset+1` 是否被消费 |
| 复合顶层无 `ORDER BY` vs 有 `ORDER BY` | 确认路径是否进入 `TK_ALL` 新增块 |
| `LIMIT` 正值 vs `LIMIT -1` | 区分 `iLimit <= 0` 分支与无限制 sentinel |
| `OFFSET` 正值 vs `OFFSET 0` | 区分 `iOffset <= 0` 分支与正 OFFSET |
| 左臂行数已吃完 limit vs 左臂未满足 offset vs 左臂恰好满足 offset | 区分右臂开始时剩余 offset/limit 的符号和数值 |
| 左臂 0 行 vs 左臂多行 | 控制左臂对计数器的修改量 |

---

## 3. 独立验证方法及仍然缺少的证据

### 3.1 独立验证结果正确性的方法

1. **手工 oracle 验证**  
   对每个候选查询，构造两个小表或两臂已知有序集合：
   - 手动写出左臂排序后的行序列；
   - 手动写出右臂排序后的行序列；
   - 拼接为 `左臂结果 + 右臂结果`；
   - 按全局 `OFFSET` 和 `LIMIT` 手工截取期望结果。
   
   然后分别在第一父版本和目标版本上执行，判断：
   - 两版本结果是否相同；
   - 目标版本结果是否等于手工期望。

2. **先确认路径，再确认结果**  
   用 `EXPLAIN`/VDBE trace 确认：
   - 新增 `OP_Add`、`OP_SCopy`、`OP_Integer -1` 是否生成；
   - 右臂 `pushOntoSorter` 是否读取 `iOffset+1`；
   - `OP_IfNot` 是否在某些运行中跳过右臂。
   
   但要注意：**路径被执行本身不能作为结果正确性证据**。

3. **等价替代 oracle**  
   对同一组数据，构造一个明确避免此优化的查询，例如：
   - 分别实例化左臂和右臂；
   - 显式拼接；
   - 再应用 `OFFSET`/`LIMIT`。
   
   比较原始查询和等价查询的结果。

4. **边界矩阵验证**  
   优先覆盖以下边界：
   - 左臂行数 0、1、恰好等于 `OFFSET`、超过 `OFFSET` 但不足 `OFFSET+LIMIT`、超过 `OFFSET+LIMIT`；
   - `LIMIT` 为正、为 0、为 -1；
   - `OFFSET` 为正、为 0；
   - 右臂有/无 `ORDER BY`；
   - 多臂 `UNION ALL` 中后臂有 `ORDER BY`。

5. **两版本差异分析**  
   如果两版本结果不同，不能直接判定目标版本有错。  
   应先用手工 oracle 或等价查询判断哪一版本符合 SQL 语义。  
   如果两版本结果相同但 `EXPLAIN` 显示新路径执行，则这次改动可能是性能/内存优化，不是可观察结果变更。

### 3.2 候选数量建议

在 Stage 2 不必穷举 SQL。以当前证据，优先覆盖：

- 3 类形式：
  1. 右臂有 `ORDER BY` 的两臂 `UNION ALL` + `LIMIT/OFFSET`
  2. 左右臂都有 `ORDER BY` 的两臂 `UNION ALL` + `LIMIT/OFFSET`
  3. 多臂 `UNION ALL` + `LIMIT/OFFSET`
- 每类形式下约 5–7 个边界/对照场景。

这样大约可先覆盖 15–21 条可执行 SQL，完整 SQL 留给 Stage 2。

### 3.3 仍然缺少的证据

1. **完整 select loop 源码**  
   尚未提供 `iLimit`、`iOffset` 在输出/跳过过程中如何被修改的代码。

2. **VM opcode 精确语义**  
   特别是 `OP_IfNotZero`、`OP_IfPos`、`OP_IfNeg`、`OP_SCopy` 等 opcode 的精确跳转/赋值行为。

3. **`iOffset+1` 是否还有其他消费者**  
   目前提供的源码只显示 `pushOntoSorter` 使用它；完整源码可能还有其他位置。

4. **两版本实际执行差异**  
   目前只有源码差异，没有实际查询结果对照。

5. **SQLite 对复合 SELECT 臂内 `ORDER BY` + 顶层 `LIMIT/OFFSET` 的精确语义确认**  
   通常可手工推演，但最好用等价查询或官方语义佐证。