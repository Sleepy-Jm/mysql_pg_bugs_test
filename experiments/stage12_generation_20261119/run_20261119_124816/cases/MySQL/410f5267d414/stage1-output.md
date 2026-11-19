## MySQL 提交分析 · Stage 1

### 1. 哪些 SQL 构造可能进入改动路径？

改动集中在 `Item_func_numhybrid` 的两个取值函数中，只影响 **结果类型为 DECIMAL 的数值混合表达式**。  

| 文件 / 函数 / 行号 | 作用 / 进入条件 |
|---|---|
| `sql/item_func.cc:1508–1541` `Item_num_op::set_numeric_type` | 决定数值二元运算的 `hybrid_type`。进入 `DECIMAL_RESULT` 的条件：两个参数的 `numeric_context_result_type` 都不是 `REAL_RESULT`，且至少有一个是 `DECIMAL_RESULT`。即运算参数中无 FLOAT/DOUBLE，且有 DECIMAL 参与。 |
| `sql/item_func.cc:1739–1740` `Item_func_numhybrid::val_real` | 新增 `my_decimal_round`。仅当 `hybrid_type == DECIMAL_RESULT` 时执行。所有走该分支的表达式都会被舍入到 `decimals` 位再转 `double`。 |
| `sql/item_func.cc:1820–1824` `Item_func_numhybrid::val_decimal` | 新增条件舍入：`val->frac > decimals` 时调用 `my_decimal_round`。仅影响 `hybrid_type == DECIMAL_RESULT` 且 `decimal_op()` 返回非空的小数结果。 |
| `sql/item_func.cc:1693–1703` `Item_func_numhybrid::val_str` | 对照路径：**已有**同样的舍入，说明字符串输出早就是舍入后的结果。 |

**可能进入的 SQL 构造类别**  
- 二元算术运算：`+`, `-`, `*`, `/`, `%`, `MOD` 等。  
- 运算参数中至少一个是 DECIMAL 类型（DECIMAL 列、DECIMAL 常量、返回 DECIMAL 的函数），另一个为 DECIMAL 或 INT，且没有 DOUBLE/FLOAT 操作数。  
- 例如：`DECIMAL列 + INT列`、`DECIMAL列 * DECIMAL列`、`DECIMAL列 / INT列`、`DECIMAL常量 - DECIMAL列` 等。  
- 这些表达式可出现在 `SELECT`、`WHERE`、`ORDER BY`、`INSERT ... SELECT`、`UPDATE` 等任何使用表达式值的上下文中。

**不会进入的常见情况**  
- 操作数包含 `DOUBLE`、`FLOAT`、`REAL` 任一，则 `hybrid_type` 变为 `REAL_RESULT`，不触发本补丁。  
- 两个操作数都是 INT，则 `hybrid_type` 为 `INT_RESULT`，也不触发。  
- 单目数值函数或非 `Item_func_numhybrid` 体系（如聚合函数、字符串函数）通常不在该分支内。

---

### 2. 到达后，哪些输入性质可能影响查询的可观察结果？

#### 源码直接支持的条件与影响

- **触发条件**：`hybrid_type == DECIMAL_RESULT` 且 `decimal_op()` 返回非空。  
- **实际舍入判断**（val_decimal 路径）：`val->frac > this->decimals`，即内部小数结果的实际小数位数大于表达式声明的结果小数位数。  
- **舍入方式**：`my_decimal_round(..., truncate = false, ...)`，即 **HALF_UP 四舍五入**，不是截断。  
- **影响路径**：  
  - `val_real()`：先舍入，再 `my_decimal2double`。影响所有将表达式当作 REAL/DOUBLE 消费的场景。  
  - `val_decimal()`：返回舍入后的 `my_decimal`。影响所有将表达式当作 DECIMAL 消费的场景。  
  - 典型消费点：`Item::save_in_field_inner`（`sql/item.cc:6879–6894`）中，`REAL_RESULT` 调 `val_real()`，`DECIMAL_RESULT` 调 `val_decimal()`，最终存入表字段。  
  - 比较、排序、临时表物化等内部也可能调用这两个方法。

- **可观察差异**：旧版本中 `val_real`/`val_decimal` 直接返回未舍入的 decimal 值，而 `val_str` 早已舍入。因此同一表达式在不同消费方式下可能产生不一致：  
  - 字符串输出（`SELECT expr`）→ 旧版已舍入。  
  - 存入 DOUBLE/DECIMAL 列、参与数值比较、排序等 → 旧版可能未舍入，导致与字符串行为不同。  
  新版本消除了这种不一致。

#### 待验证的推断（尚未由当前证据直接证明）

- **哪些运算组合会产生 `val->frac > decimals`**：  
  - 除法最可能产生额外小数位；乘法也可能；加减法通常不会超过参与运算的最大 scale。  
  - 实际结果取决于 `result_precision()` 如何设置 `decimals`，该函数源码未在材料中提供，因此无法准确预判。  
- **`decimals` 的具体取值**：由 `Item_num_op::result_precision()` 根据操作数精度计算，可能与操作数 scale、运算类型有关。  
- **是否所有这类表达式都会在旧版产生错误结果**：只有内部结果小数位数确实超过声明 scale 且超出的数字在舍入后改变前值时，才会观察到差异。  
- **影响范围**：内部比较、排序等可能使用 `val_real`/`val_decimal`，但具体哪些优化或执行路径会调用它们尚未完全确认。

#### 可用于区分源码直接支持与推断的对照

- **同一表达式不同消费方式对照**：  
  - `SELECT expr`（走 `val_str`，旧版已舍入）  
  - `INSERT INTO ... SELECT expr` 存入 DOUBLE 或 DECIMAL 列（走 `val_real`/`val_decimal`，旧版未舍入）  
  旧版两者不一致，新版应一致。  
- **不同表达式类型对照**：  
  - 含有 DOUBLE 参数时，`hybrid_type` 为 `REAL_RESULT`，不进入补丁，结果不受影响。  
  - 两个 INT 参数时，结果为 INT，不进入补丁。  
  这两种情况可作为“不应受影响”的对照组。  
- **NULL 行为对照**：`decimal_op()` 返回 `nullptr` 时，`val_real` 返回 0.0，`val_decimal` 返回 `nullptr`，均不触发舍入，行为与旧版一致。  

---

### 3. 独立验证结果正确性的方法和仍缺少的证据

#### 独立验证思路

1. **构造候选表达式**：  
   - 优先测试 **除法** 和 **乘法** 中 DECIMAL 与 DECIMAL/INT 的组合。  
   - 使用较小的 DECIMAL scale（如 `DECIMAL(10,2)`）以便人工计算期望值。  
   - 确保参数无 DOUBLE/FLOAT，保证 `hybrid_type` 为 `DECIMAL_RESULT`。  

2. **多路径对照观察**：  
   - 对同一表达式，分别用以下方式消费结果：  
     - `SELECT expr`（字符串输出）  
     - `SELECT expr + 0`（强制数值比较/输出，可能走 `val_real`）  
     - `INSERT INTO t2 DOUBLE_COL SELECT expr`（存为 DOUBLE）  
     - `INSERT INTO t2 DECIMAL_COL SELECT expr`（存为 DECIMAL）  
   - 新旧版本对比这些消费方式的结果差异。  
   - 若旧版字符串路径与数值路径不一致，而新版一致，则强烈提示旧版在 `val_real`/`val_decimal` 上存在错误，新行为更合理。  

3. **独立正确性判断依据**：  
   - MySQL 官方文档对 DECIMAL 表达式结果 scale 的规则：结果小数位数应按声明 scale 舍入（HALF_UP），而不是保留内部全精度。  
   - 表达式本身已有字符串输出路径 `val_str` 的舍入，说明新补丁将 `val_real`/`val_decimal` 对齐，逻辑自洽。  
   - 人工计算：取具体数值构造舍入临界案例（如 `2.005` 舍入到 `2.01`），与新旧版本输出对比。  
   - 标准 SQL 期望：数值结果按目标类型/列定义进行舍入，内部未舍入值的泄漏属于精度错误。  

4. **不应依赖的判据**：  
   - 仅“路径被执行”或“新旧版本结果不同”不能直接认定查询结果有错。  
   - 必须证明旧版行为与标准、文档、字符串路径或其他独立参照不一致，且新版行为符合其中至少一个参照。  

#### 仍缺少的证据

- **具体示例**：尚缺能稳定产生 `val->frac > decimals` 的 SQL 表达式及其输入数据。  
- **`result_precision()` 源码**：未提供，无法确定 `decimals` 的计算规则，从而无法预先筛选出所有可能受影响的表达式。  
- **旧版实际输出**：未运行旧版获取基准结果，不能断言差异确实存在或差异属于错误。  
- **所有消费路径映射**：尚未确认内部比较、排序、临时表等是否确实调用 `val_real`/`val_decimal`，并受此补丁影响。  
- **官方修复意图**：未附提交说明正文，不能确认该补丁是否志在修复已发现的错误，还是仅做了一致性调整。  
- **边界风险**：圆形可能引发 `my_decimal` 进位/溢出（例如 `9.99` 舍入到 `10.00`），需要验证代码是否能正确处理 `E_DEC_FATAL_ERROR` 和精度扩展。  

**候选数量**：基于现有证据，候选至少覆盖 **二元算术运算中 DECIMAL_RESULT 且结果小数位数超过声明 scale 的除法/乘法** 一类；具体数量需在下一阶段通过实际测试筛选。当前不能仅凭代码路径推断出精确数量。