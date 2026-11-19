## 1. 哪些 SQL 构造可能进入改动路径？

核心改动是：`sqlite3CodeRhsOfIN` 在生成 `IN (SELECT ...)` 的 RHS 临时表时，会为子查询 RHS 计算并写入一个 `SubrtnSig` 签名；之后如果再次生成“相同”的 IN 子查询 RHS，则可复用先前的物化结果，而不是重新执行子查询。

### 1.1 直接入口

| SQL 构造 | 源码位置 | 条件 |
|---|---|---|
| `expr IN (SELECT ...)` 且需要物化 RHS 为 ephemeral table | `sqlite3FindInIndex` 目标版 `src/expr.c L3305-L3349`，在 `eType==0` 后调用 `sqlite3CodeRhsOfIN`，位置约 L3347 | 没有可用的既有索引 / 不满足 `IN_INDEX_NOOP` |
| 虚拟表参与 `IN (SELECT ...)` | `sqlite3WhereCodeOneLoopStart` 目标版 `src/wherecode.c L1520-L1545`，满足 `pTerm->eOperator & WO_IN` 且 `mHandleIn` 时调用 `sqlite3CodeRhsOfIN` | `SQLITE_OMIT_VIRTUALTABLE` 未定义时 |

真正的新复用逻辑在：

- `findCompatibleInRhsSubrtn`：`src/expr.c`，新增函数，约 L3424-L3464。
- `sqlite3CodeRhsOfIN`：`src/expr.c`，目标版 L3466-L3714；新逻辑集中在进入复用允许分支的 L3508 附近。

### 1.2 进入新复用路径的源码条件

在 `sqlite3CodeRhsOfIN` 中：

1. 必须可复用：
   - `!ExprHasProperty(pExpr, EP_VarSelect)`：RHS 不是相关子查询。
   - `pParse->iSelfTab==0`：不在 trigger 内部。
2. 只有 RHS 是子查询时才创建 `SubrtnSig`：
   - `ExprUseXSelect(pExpr)` 为真，即 `IN (SELECT ...)`。
   - `(pExpr->x.pSelect->selFlags & SF_All)==0`，即排除 `SF_All` 的 SELECT。
3. 必须存在可匹配的先前物化 RHS：
   - `pParse->bHasSubrtn != 0`。
   - 先前已生成带 `P4_SUBRTNSIG` 的 `OP_BeginSubrtn` 指令。
   - `SubrtnSig.selId` 与当前 `pExpr->x.pSelect->selId` 相同。
   - `SubrtnSig.zAff` 字符串与当前 `exprINAffinity(pParse, pExpr)` 相同。
4. `SubrtnSig` 是在第一次物化 IN RHS 时写入的：
   - `src/expr.c` 中 `sqlite3CodeRhsOfIN` 新逻辑：
     ```c
     pSig->iAddr = pExpr->y.sub.iAddr;
     pSig->regReturn = pExpr->y.sub.regReturn;
     pSig->iTable = iTab;
     sqlite3VdbeChangeP4(v, -1, (const char*)pSig, P4_SUBRTNSIG);
     pParse->bHasSubrtn = 1;
     ```
   - 因此候选 SQL 必须至少包含两个或更多个这样的 `IN (SELECT ...)`。

### 1.3 “同一 selId”的主要来源：predicate push-down

提交说明明确提到：

> especially when the IN operator is duplicated due to predicate push-down.

对应源码链路：

- `sqlite3Select` 调用点：`src/select.c L7705-L7720`
  - 启用 `SQLITE_PushDown`。
  - CTE 条件满足时调用 `pushDownWhereTerms`。
- `pushDownWhereTerms`：`src/select.c L5291-L5322`
  - 用 `sqlite3ExprDup(pParse->db, pWhere, 0)` 复制外层 WHERE 表达式。
- `sqlite3SelectDup`：`src/select.c L1934-L1987`
  - 保留 `selId`：
    ```c
    pNew->selId = p->selId;
    ```

因此最典型的 SQL 构造是：

- 外层查询的 FROM 子句是一个子查询。
- 外层 WHERE 中有 `col IN (SELECT ...)`。
- 该条件满足 `sqlite3ExprIsSingleTableConstraint`，可被 `pushDownWhereTerms` 推入 FROM 子查询内部。
- 推入后，外层和内层各有一个 IN 表达式，但它们的 RHS SELECT 由于 `sqlite3ExprDup` / `sqlite3SelectDup` 保留了相同 `selId`。

### 1.4 候选构造总结

| 候选 | 入口/关键条件 | 依据 |
|---|---|---|
| FROM 子查询 + 外层 WHERE 中的 `IN (SELECT ...)` 被下推 | `sqlite3Select` L7705-L7720 → `pushDownWhereTerms` L5291-L5322 → `sqlite3ExprDup` → `sqlite3SelectDup` 保留 selId | 提交说明和源码路径直接支持 |
| 两个或多个由表达式复制产生的 `IN (SELECT ...)` | `sqlite3CodeRhsOfIN` 新复用逻辑；`findCompatibleInRhsSubrtn` 扫描先前 `OP_BeginSubrtn` | 源码直接支持 |
| 虚拟表列上的 `IN (SELECT ...)` 且 mHandleIn 为真 | `sqlite3WhereCodeOneLoopStart` L1520-L1545 | 源码直接支持 |
| 非相关、非触发器、RHS 非 `SF_All` 的 `IN (SELECT ...)` | `sqlite3CodeRhsOfIN` 中 `EP_VarSelect` / `iSelfTab` / `SF_All` 条件 | 源码直接支持 |

---

## 2. 到达后哪些输入性质可能影响查询的可观察结果？

这里区分三种层级：

- A：源码直接支持的关系。
- B：源码未排除、但尚未完整验证的推断风险。
- C：可以用来区分 A 与 B 的对照。

### 2.1 源码直接支持的关系

| 输入性质 | 源码依据 |
|---|---|
| RHS 必须是子查询，而不是表达式列表 | `pSig` 仅在 `ExprUseXSelect(pExpr)` 分支创建 |
| RHS 不能被标记为 `SF_All` | `(pExpr->x.pSelect->selFlags & SF_All)==0` |
| RHS 不能是相关子查询 | `!ExprHasProperty(pExpr, EP_VarSelect)` |
| 不能处于 trigger 环境 | `pParse->iSelfTab==0` |
| 复用的匹配键是 `selId` 和 `zAff` | `findCompatibleInRhsSubrtn` 中 `pSig->selId` 比较和 `strcmp(zAff)` |
| `zAff` 来自 LHS 与 RHS SELECT 的亲和性计算 | `exprINAffinity`，`src/expr.c L3352-L3384` |
| `selId` 可由 `sqlite3SelectDup` 复制保留 | `src/select.c L1934-L1987` |
| 必须已有 `P4_SUBRTNSIG` 才会尝试查找 | `pParse->bHasSubrtn` 为 1 |

因此，直接可观察的候选特征有：

- 至少有两个 `IN (SELECT ...)`。
- 它们共享同一个 RHS `selId`。
- 它们的 `zAff` 亲和串相同。
- 第一个 IN RHS 已经以带 `SubrtnSig` 的子例程形式物化。

### 2.2 尚待验证的推断风险

#### 风险 1：RHS 非确定函数可导致结果集变化

源码中没有对 volatile / non-deterministic 做检查。

- 若 RHS 子查询包含 `random()`、`date('now')` 等，则多次执行会得到不同 RHS 集合。
- 新逻辑会复用第一次物化结果，因此重复 IN 会共享同一个 RHS 集合。
- 在 predicate push-down 场景中，这可能正是需要的正确性修复；但在其他重复 IN 场景中，是否可复用取决于 SQL 语义。
- 这目前是推断：源码未显式识别 volatile，但也没有给出禁止复用 volatile RHS 的条件。

验证对照：

- 构造一个查询，其中两个 `IN (SELECT random()...)` 共享 `selId`。
- 将新版本结果与“显式物化一次 RHS”的参考查询比较。
- 不能仅拿父子版本结果不同来判断错误。

#### 风险 2：签名未显式包含 collation

`SubrtnSig` 结构为：

```c
struct SubrtnSig {
  int selId;
  char *zAff;
  int iTable;
  int iAddr;
  int regReturn;
};
```

`zAff` 只保存亲和性字符串，不包含 collation。

但是：

- `sqlite3CodeRhsOfIN` 中会使用 `sqlite3BinaryCompareCollSeq` 计算 RHS 临时表的键比较 collation：
  ```c
  pKeyInfo->aColl[i] = sqlite3BinaryCompareCollSeq(
      pParse, p, pEList->a[i].pExpr
  );
  ```
- 这个 `pKeyInfo` 只在第一次物化时设置给 `OP_OpenEphemeral`。
- 后续复用只 `OP_OpenDup` 相同的临时表，不会重新设置 collation。

因此，若两个 IN 的 LHS 有相同 affinity 但不同 collation，且 RHS `selId` 相同，则现有签名可能无法区分。  
这是尚待验证的推断风险。

验证对照：

- 构造相同 `selId`、相同 `zAff`，但 LHS collation 不同的 IN。
- 比较目标版本与一个强制独立物化 RHS 的参考查询结果。
- 需要阶段 2 确认这种 SQL 是否能实际到达该代码路径。

#### 风险 3：`zAff` 是否完整覆盖 LHS/RHS 比较语义

`exprINAffinity` 只返回每个向量位置的 affinity 字符，不包含：

- 字符集/排序规则；
- 其他可能影响比较结果的信息。

因此，凡影响 IN 比较可观察结果的非 affinity 属性，都可能是候选测试点。

#### 风险 4：`selId` 相同的不同 RHS 是否一定语义等价

当前源码支持的是：

- `sqlite3SelectDup` 保留 `selId`。
- `pushDownWhereTerms` 复制 WHERE 表达式。

但对于其他复制路径，是否可能产生同 `selId` 但已发生变化的 SELECT，本文提供的源码片段不足以完整证明。需要阶段 2 通过 `EXPLAIN` / VDBE trace 验证两个 IN 是否真正共享签名。

### 2.3 对照关系表

| 性质 | 源码直接支持 | 尚待验证推断 | 可区分对照 |
|---|---|---|---|
| RHS 为 `IN (SELECT ...)` | 是 | — | 用 RHS 列表 `IN (1,2)` 作为负对照 |
| RHS 非相关、非触发器 | 是 | — | 用相关子查询或 trigger 作为负对照 |
| RHS 非 `SF_All` | 是 | `SF_All` 精确含义需确认 | 用 `UNION ALL` RHS 作为负对照 |
| 至少两个 IN 共享 `selId` | 是；`sqlite3SelectDup` 保留 | 其他复制路径是否全量覆盖未证明 | 用多个手写相同文本 IN 验证通常不会共享 selId |
| `zAff` 相同才复用 | 是 | `zAff` 不足以编码 collation | 同 affinity 不同 collation 查询 |
| RHS 确定性 | 源码无 volatility 检查 | 非确定 RHS 可能被合并求值 | 用 `random()` 等与显式物化一次对照 |
| 结果中 NULL / duplicate 的集合 | 受复用影响 | 是否构成错误取决于语义 | 用确定性 RHS 和参考查询对照 |
| 只用父子版本结果差异判断错误 | 不充分 | — | 必须提供独立 oracle |

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 独立验证路径确实到达

路径被执行本身不能证明结果错误，但能帮助确认候选 SQL 是否命中改动。

验证方式：

- 使用 `EXPLAIN` 或 VDBE 程序查看：
  - 是否出现 `REUSE LIST SUBQUERY`；
  - 是否出现带 `P4_SUBRTNSIG` 的 `OP_BeginSubrtn`；
  - 是否出现 `OP_OpenDup`；
  - 是否只有一个 RHS 子例程。
- 对负对照：
  - RHS 为表达式列表；
  - RHS 为相关子查询；
  - trigger 中 IN；
  - RHS 为 `SF_All`/`UNION ALL`；
  - 单个 IN 没有第二处复用。

这些只证明“路径被命中”，不证明“结果正确”。

### 3.2 结果正确性的独立验证方法

对每一类候选，独立 oracle 思路如下：

1. **predicate push-down 重复 IN**
   - 用禁用 `SQLITE_PushDown` 或等效改写，强制只保留一个 IN。
   - 将目标版本结果与该参考结果比较。
   - 如果 RHS 是确定性的，二者应一致。
   - 如果 RHS 是非确定性的，需要先定义正确语义：例如，逻辑查询只应有一个 IN 条件，不应有两个独立求值的 IN 条件。

2. **非确定 RHS**
   - 使用可控的 `random` 不可行，可改为读取临时表或用户函数并记录调用次数/返回值序列。
   - 参考查询：将 RHS 先显式物化到 CTE 或临时表，再让内外 IN 使用同一结果集。
   - 比较目标版本与本参考查询结果。

3. **collation 差异**
   - 构造两个共享 `selId` 但 LHS collation 不同的 IN。
   - 参考查询：强制两处分别使用各自 collation，或显式物化两个不同 collation 的 RHS 表。
   - 比较目标版本与参考结果。
   - 需要阶段 2 先确认该构造可以到达 `findCompatibleInRhsSubrtn`。

4. **affinity 差异**
   - 参考查询：将 RHS 显式转换为指定 affinity。
   - 检查目标版本是否因 `zAff` 匹配而忽略了某些表示差异。

5. **NULL 和 duplicate**
   - 根据 IN 语义，NULL 和重复值通常不会影响“可观察结果”中的行存在性，但会影响“集合大小”或“重复求值次数”。
   - 更实际的是观察非确定函数调用次数来验证是否合并了求值。

### 3.3 仍缺少的证据

| 缺失证据 | 为什么重要 | 如何获得 |
|---|---|---|
| `SF_All` 具体对应哪些 SQL RHS | 确定负对照范围 | 用 `UNION ALL` RHS 查看 `selFlags` / `EXPLAIN` |
| 除 predicate push-down 外，哪些表达式复制路径会保留 `selId` | 判断风险范围 | 跟踪 `sqlite3SelectDup` 调用点 |
| `exprINAffinity` 的 `zAff` 是否足以区分配对比较语义 | 判断 collation 风险 | 用同 affinity 不同 collation 用例验证 |
| 非确定 RHS 的 IN 在逻辑上应求值一次还是每次求值 | 判断结果正确性 | 查 SQL 语义 / 用参考改写 |
| 在 predicate push-down 路径中，两个 IN 的 `zAff` 是否总是相同 | 确定是否稳定触发复用 | 使用 `EXPLAIN` 查看 RHS 复用 |
| 是否存在相同 `selId` 但不同 collation 的 push-down SQL 能到达新逻辑 | collation 风险是否真实可达 | 阶段 2 构造并跟踪 VDBE |
| 目标版本与父版本结果不同是否由该提交引入 | 不能仅凭版本差异判错 | 结合独立 oracle 和路径证据 |

### 3.4 候选测试类别建议

基于已有源码证据，建议下一阶段聚焦以下候选：

1. **FROM 子查询 + 外层 WHERE `col IN (SELECT ...)`，且该 IN 可被下推到 FROM 子查询内部。**
2. **候选 1 的 RHS 使用非确定函数，测试共享物化是否正确。**
3. **候选 1 的 LHS 使用相同 affinity 但不同 collation，测试签名是否漏掉 collation。**
4. **负对照：RHS 为 `UNION ALL`、RHS 为表达式列表、相关子查询、trigger 内 IN。**
5. **虚拟表 IN 子查询路径，测试新签名是否会影响结果。**

这些候选只限定 SQL 构造模式，完整可执行 SQL 留给下一阶段。