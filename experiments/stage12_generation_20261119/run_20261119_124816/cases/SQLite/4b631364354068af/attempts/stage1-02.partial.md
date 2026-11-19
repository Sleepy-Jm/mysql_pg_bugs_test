## 1. 可能进入改动路径的 SQL 构造

候选形态首先应满足：

```sql
SELECT ... FROM left
UNION ALL
SELECT ... FROM right
LIMIT <expr> OFFSET <expr>;
```

且 **最外层不能有 ORDER BY**。

代码依据：

- `sqlite3Select` 目标版 `src/select.c:4899-4912`  
  当 `Select.p->pPrior != 0` 时，复合查询进入 `multiSelect()`。

- `multiSelect()` 目标版 `src/select.c:2248-2250`  
  先判断 `p->pOrderBy`。  
  如果外层有 `ORDER BY`，会走 `multiSelectOrderBy()`，不会到达本次修改的 `TK_ALL` 分支。

- `multiSelect()` 目标版 `src/select.c:2254-2255`  
  仅 `p->op == TK_ALL`，即 `UNION ALL`。  
  `TK_UNION`、`TK_EXCEPT`、`TK_INTERSECT` 不进入本次改动。

- `multiSelect()` 目标版 `src/select.c:2273-2285`  
  这是本次新增代码块。条件是：
  - `p->iLimit` 为真，即复合查询存在 `LIMIT`；
  - `p->iOffset` 为真，即复合查询存在 `OFFSET`。

因此，最直接的进入条件是：

> `UNION ALL` 复合查询，带顶层 `LIMIT` 和 `OFFSET`，且顶层没有 `ORDER BY`。

另外还有一个关键分支条件：

- 目标版 `src/select.c:2274` 的 `OP_IfNot p->iLimit`  
  若左子查询执行完后 `LIMIT` 寄存器值为 0，说明 `LIMIT` 已耗尽，会跳过右侧子查询，也跳过新增的重算逻辑。  
  所以实际上进入新增代码的查询还必须满足：

> 左子查询跑完后，剩余 `LIMIT` 不为 0。

例如，对正数 `LIMIT L, OFFSET O`，左子查询行数应小于 `L+O`。  
若左子查询行数已经达到或超过 `L+O`，右子查询会被跳过，本次改动不可见。

---

## 2. 到达后会受输入性质影响的可观察结果

### 2.1 源码中直接支持的关系

新增代码位于：

- `multiSelect()` 目标版 `src/select.c:2276-2285`

其作用是在左子查询执行完后，用当前 `iLimit` 和 `iOffset` 重算 `iOffset+1` 寄存器。

直接可读出的逻辑是：

```c
sqlite3VdbeAddOp3(v, OP_Add, p->iLimit, p->iOffset, p->iOffset+1);
addr2 = sqlite3VdbeAddOp1(v, OP_IfPos, p->iOffset); VdbeCoverage(v);
sqlite3VdbeAddOp2(v, OP_SCopy, p->iLimit, p->iOffset+1);
sqlite3VdbeJumpHere(v, addr2);
addr2 = sqlite3VdbeAddOp1(v, OP_IfPos, p->iLimit); VdbeCoverage(v);
sqlite3VdbeAddOp2(v, OP_Integer, -1, p->iOffset+1);
sqlite3VdbeJumpHere(v, addr2);
```

按常规 VDBE 语义理解，这段代码等价于根据当前 `iLimit` 和 `iOffset` 重新计算 `LIMIT+OFFSET`：

- 若当前 `iOffset` 为正，则 `iOffset+1 = iLimit + iOffset`。
- 若当前 `iOffset` 非正，则先用 `OP_SCopy` 把 `iLimit` 复制到 `iOffset+1`，相当于把负数/零 OFFSET 视为 0。
- 若当前 `iLimit` 非正，则最终把 `iOffset+1` 设为 `-1`，对应“LIMIT 负数表示无上限”的既有处理。

这与 `computeLimitRegisters()` 的初始化逻辑形成对照：

- `computeLimitRegisters()` 目标版 `src/select.c:1791-1863`
- 尤其 `src/select.c:1845-1857` 对负 OFFSET 和负 LIMIT 的处理。

所以从源码层面可以确认：

> 新代码会覆盖左侧执行后留下的 `iOffset+1` 值，而这个寄存器语义是“LIMIT+OFFSET”。

### 2.2 哪些输入性质会影响到达后的寄存器值

到达新增代码时，真正影响行为的不是 SQL 文本本身，而是左子查询执行后两个寄存器中的值：

- `p->iLimit`：剩余还能输出的行数。
- `p->iOffset`：剩余还需要跳过的行数。

这些值又主要取决于：

1. 左子查询返回的行数；
2. 顶层 `LIMIT` 的值；
3. 顶层 `OFFSET` 的值。

按 LIMIT/OFFSET 语义可以推断出以下分区，但这些分区属于“尚待验证的推断”，因为本文未给出非排序路径下 `iLimit`、`iOffset`、`iOffset+1` 的完整递减代码：

| 左子查询行数 `N_left` 与 `L,O` 关系 | 到达新代码时可能状态 | 右子查询是否执行 |
|---|---:|---|
| `N_left < O` | `iOffset > 0`，`iLimit` 大致仍为原 `L` | 执行 |
| `N_left == O` | `iOffset` 可能为 0 或非正，`iLimit` 仍为 `L` | 执行 |
| `O < N_left < L+O` | `iOffset` 非正，`iLimit = L - (N_left - O)` | 执行 |
| `N_left >= L+O` | `iLimit == 0`，`OP_IfNot` 跳过右侧 | 不执行 |

这是复杂度最高、最值得候选查询覆盖的区域。

### 2.3 可能影响可观察结果的性质

#### 2.3.1 左子查询是否部分消耗 OFFSET 或 LIMIT

新增代码只在左子查询执行后有意义。如果左子查询为空，或者左子查询返回行数很少，`iLimit` 和 `iOffset` 可能基本保持初始值，此时重算前后差异可能较小。

重点候选性质：

- 左子查询行数 `< OFFSET`
- 左子查询行数 `== OFFSET`
- 左子查询行数 `> OFFSET` 但 `< OFFSET + LIMIT`
- 左子查询行数 `>= OFFSET + LIMIT`

第三种情况最可能暴露旧版 `iOffset+1` 未随左子查询更新或更新不一致的问题。

#### 2.3.2 左子查询或右子查询是否走排序/排序器路径

`pushOntoSorter()` 目标版 `src/select.c:568-587` 显示：

- 当存在 `iOffset` 时，排序器修剪使用的计数器是 `pSelect->iOffset+1`，而不是 `pSelect->iLimit`。
- 也就是说，`iOffset+1` 的作用之一是控制排序器中保留的行数。

因此，如果左侧或右侧子查询内部存在需要排序的路径，例如自身带 `ORDER BY`，那么 `iOffset+1` 的值可能被排序器消耗。  
旧版没有在左侧执行完后重算，右侧再进入排序路径时可能使用旧值。

这属于高频候选，但需要下一阶段用可执行的 SQL 验证。  
因为从本输入中的源码摘录还无法完全确定：

- SQLite 语法是否允许 `UNION