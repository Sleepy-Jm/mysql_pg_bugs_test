## 1. 哪些 SQL 构造可能进入改动路径？

本提交的核心变化是：移除运行期/编译期“是否使用 `long double`”的分支，`sqlite3AtoF`、`sqlite3FpDecode`、`sqlite3IntFloatCompare` 中原本可选的 `long double` 路径被删除，统一走已有的 Dekker double-double 路径。因此候选主要来自这三条代码路径的上层 SQL 入口。

| 可能进入的 SQL 构造 | 文件 / 函数 / 行号 | 证据与说明 |
|---|---|---|
| SQL 中的实数文本字面量，如 `1.23`、`1e-40`、`1.234567890123456789e+100` | `src/expr.c` `codeReal` L4169–L4187，其中 L4182 附近调用 `sqlite3AtoF`；目标版 `src/util.c` `sqlite3AtoF` L529–L705，变化集中在 `do_atof_calc:` 后约 L652–L703 | `codeReal` 是附件直接给出的 `sqlite3AtoF` 入口。 |
| 文本到 REAL 的显式/隐式转换 | `src/util.c` `sqlite3AtoF` L529–L705；调用者未在附件中给出，通常类似 `sqlite3VdbeMemNumerify`/`sqlite3VdbeMemCast` | `CAST('...' AS REAL)`、文本与实数比较/运算、插入 REAL affinity 列等很可能进入；具体调用点尚待补全。 |
| 浮点值输出为文本 | `src/printf.c` `sqlite3_str_vappendf` L480–L506 调用 `sqlite3FpDecode`；目标版 `src/util.c` `sqlite3FpDecode` 变化在 L1038–L1087 | 直接支持：`printf('%f/%e/%g', x)`、`format(...)` 等。`CAST(real AS TEXT)` 或 shell 显示 real 是否也走此路径，尚待验证。 |
| 整数与浮点数比较 | `src/vdbeaux.c` `sqlite3IntFloatCompare` L4520–L4542；调用点通常在 VDBE 比较运算，但附件未列 | `integer_column = real_literal`、`int_val < real_val`、`BETWEEN`、`ORDER BY` 等混合 INTEGER/REAL 比较可能进入该函数。 |
| `.testctrl uselongdouble` | `src/shell.c.in` 及 `src/main.c` 中相关代码已删除 | 不是普通 SQL 查询构造，但可用作旧版路径切换/对照测试，新版已不可用。 |

补充说明：`ext/wasm` 中删除的 `SQLITE_USE_LONG_DOUBLE=0` 原本已经强制关闭 long double，因此 wasm 构建路径基本不代表行为变化点。核心候选集中在普通 C 构建中三处数值算法。

---

## 2. 到达后，哪些输入性质可能影响查询的可观察结果？

### 2.1 `sqlite3AtoF`：字符串转 `double`

进入后关键局部量是：

- `s`：解析出的 `u64` 有效数。
- `e`：调整后的十进制指数。
- 旧版分支：`e == 0` 直接赋值；`e != 0` 时按 `SqliteUseLongDouble` 选择 `long double` 或 Dekker。
- 目标版：统一执行 Dekker，没有 `e == 0` 特殊分支。

#### 源码直接支持的候选关系

1. **`s == 0` 路径不变**  
   函数在 `do_atof_calc` 后马上判断 `s == 0`，两版都有，差异候选极低。

2. **`e == 0` 路径低风险，但已发生代码变更**  
   旧版直接 `*pResult = s`；目标版会执行 `rr[0] = (double)s`、`rr[1] = ...`，然后 `*pResult = rr[0]+rr[1]`。  
   从 Dekker 性质看通常结果与 `(double)s` 相同，但这是“推断”，不是本文附件直接证明。故仍可作为低优先候选。

3. **`e != 0` 且原平台会启用 long double 时，候选最强**  
   旧版走 `LONGDOUBLE_TYPE r = (LONGDOUBLE_TYPE)s; while(e...) r *= 1.0e+...L; *pResult = (double)r;`  
   目标版走 double-double。  
   可观察差异应集中在：
   - 有效数 `s` 超过 53 位 binary precision，`(double)s` 产生 residual `rr[1]`；
   - 十进制有效数在 double rounding boundary 附近，即最后一位舍入是 tie 或接近 tie；
   - `e` 非零，因而会进入乘/除 10 的幂循环。

#### 尚待验证的推断

- 并非所有“大有效数 + 非零指数”都会产生差异；需要搜索具体 `(s, e)`。
- `e == 0` 尽管代码形式变了，但是否可观察差异需要独立验证，暂时不提升为高优先候选。
- 溢出路径：旧版有显式 `if( r > 1.7976931348623157081452742373e+308L )`，目标版依赖 Dekker 乘法和 `sqlite3IsNaN` 后兜底。  
  可能影响接近 `DBL_MAX` 的输入，但需要对 C 浮点溢出行为建模才能确定是否会实际改变结果。

#### 可区分两版的对照性质

- 输入形式应为：19 位左右的有效数字 + 非零指数，例如 `s = <接近 2^63 或 2^64>`, `e = <几十/几百>`。
- 对照不应只看两版文本输出是否不同，因为文本输出可能由 `sqlite3FpDecode` 再次引入差异；最好直接观察 `sqlite3AtoF` 得到的 `double`，或用一个不受目标函数影响的 oracle 做比较。

---

### 2.2 `sqlite3FpDecode`：`double` 到十进制文本

该函数负责将 `double r` 缩放到约 `[1e17, 1e19)` 范围并提取十进制数字。  
旧版仍按 `SqliteUseLongDouble` 分支；目标版固定使用 double-double。

#### 源码直接支持的候选关系

1. **输入 `r` 需要经过缩放循环时，候选增强**  
   目标版 `if( rr[0] > 9.223372036854774784e+18 )` 或 `else` 中的 while 循环会多次执行 `dekkerMul2`。  
   `r` 很大或很小的正规/次正规数会执行更多循环，累积误差差异的可能性更高。

2. **最终文本舍入点附近的输入最有可观察性**  
   因为 `sqlite3FpDecode` 只是把 double 转成数字串，上层 `printf.c` 还要按精度舍入。  
   如果某 double 的十进制输出正好处在显示精度舍入中点附近，潜在最后一位变化会直接可见。

#### 尚待验证的推断

- `CAST(real AS TEXT)`、shell 输出 real 通常是否使用 `sqlite3FpDecode`；附件只给出了 `printf.c` 的调用关系。
- 旧版 `long double` 使用的缩放边界是 `1.0e+19`、`1.0e+29`、`1.0e+119` 等；目标版使用 `9.223...` 系列阈值。两者的循环次数和舍入位置不同，但是否改变最终可见结果，需要通过 oracle 验证。
- 次正规数、接近 `DBL_MAX` 的数、接近 `2^63` 的数是有价值的搜索空间，但不能先验确定哪些具体 double 会输出差异。

#### 可区分两版的对照性质

- 同一 double 输入，旧版可能用 long double 缩放出数字串，新版用 double-double。
- 要区分“`sqlite3AtoF` 解析差异”和“`sqlite3FpDecode` 输出差异”，可以直接把已知 double 字面量以 C 或绑定方式传入，避免同时经过 AtoF 解析。

---

### 2.3 `sqlite3IntFloatCompare`：整数与浮点数比较

目标版删除了 `LONGDOUBLE_TYPE x = (LONGDOUBLE_TYPE)i; return (x<r)?...`，改为先范围拦截、再 `(i64)r` 比较、再 `(double)i` 与 `r` 比较。

#### 源码直接支持的候选关系

- 输入为 `i64 i` 和 `double r`，且 `r` 不是 NaN。
- `r` 在 `[-2^63, 2^63)` 范围内时会进入普通逻辑；`r < -2^63` 或 `r >= 2^63` 会走捷径。
- 值得关注的输入性质：
  - `i` 很大，超过 `2^53`，因此 `(double)i` 不能精确表示；
  - `r` 接近整数边界，尤其是正好等于 `2^63`、`-2^63` 或接近这些值；
  - `r` 与 `i` 的小数部分关系决定最终比较。

#### 尚待验证的推断

- 从代码逻辑看，目标版算法在正确实现的前提下应当等价于精确整数与双重浮点值比较；因此该函数可能没有可观察结果变化。
- 旧 long double 路径也可能等价，因此该函数产生的“两版不同”可能不存在，或者只在老平台 long double 异常时存在。
- 仍然建议将其列为低优先候选，因为它是本提交直接改动的行为路径之一。

#### 可区分两版的对照性质

- 精确 oracle 是：把 `r` 还原为其精确表示的实数，然后与整数 `i` 做有理数比较。
- 用 `i` 和 `r` 的组合构造 SQL 比较；但要注意 SQLite 把整数文本存为 INTEGER、实数文本存为 REAL。

---

## 3. 独立验证结果正确性的方法和仍缺少的证据

### 3.1 `sqlite3AtoF` 的独立验证方法

**Oracle：**
- 对输入十进制字符串，计算其精确有理值，然后按 IEEE-754 binary64 round-to-nearest-even 得到期望的 `double`。
- 可使用 Python `float(str)` 或 `decimal.Decimal` + 高精度模拟；但要注意 Python `float` 的行为也需要确认符合平台舍入模式。

**验证步骤：**
1. 生成候选字符串：以接近二进制舍入边界的 `s` 和不同 `e` 组合为主，例如 `s = 2^k ± 1`、`s = 10^19 - 1` 等。
2. 对每个字符串，用独立 oracle 计算期望 `double`。
3. 让 SQLite 解析同一字符串并拿到实际 `double`。
4. 比较实际 `double` 与 oracle 的位模式或精确比较。

**仍缺少的证据：**
- 附件没有给出 `sqlite3AtoF` 除 `codeReal` 外的全部调用点；需要确认哪些 SQL 构造能直接触发想要的十进制字符串。
- 纯 SQL 不一定能无损观察 `double` 位模式；如果只通过 `CAST(... AS TEXT)` 或 `printf(...)` 输出，容易混入 `sqlite3FpDecode` 的影响。
- 需要 C API、测试函数或扩展来直接读取 `sqlite3_column_double`。

---

### 3.2 `sqlite3FpDecode` 的独立验证方法

**Oracle：**
- 对已知 `double r`，按其精确二进制值，依据 `printf.c` 的精度规则计算出期望的十进制文本。
- 可参考 Python `format(r, '.<precision>f/e/g')`，但必须校准 SQLite 的舍入规则和默认精度。

**验证步骤：**
1. 选取极端/边界 `double`：
   - 接近 `DBL_MAX`；
   - 次正规数；
   - `2^63` 附近；
   - 十进制 16/17 位有效数字处存在舍入中点。
2. 通过 C 或绑定方式把已知 double 输入 SQLite，避免先经过 AtoF。
3. 用 `printf('%f', ...)` 或 `CAST` 输出，与 oracle 比较。

**仍缺少的证据：**
- SQLite `printf.c` 中 `etFLOAT`/`etEXP`/`etGENERIC` 的舍入细节尚未在附件中完整给出。
- `CAST(real AS TEXT)`、shell 输出 real 是否严格复用 `sqlite3FpDecode` 尚需调用图确认。
- 现成测试案例不足；需要根据 `sqlite3FpDecode` 的阈值和乘法常数构造边界值。

---

### 3.3 `sqlite3IntFloatCompare` 的独立验证方法

**Oracle：**
- 对每个 `(i, r)`，将 `r` 的精确实数与该整数比较，期望结果为 `<`、`=`、`>` 之一。
- 可用 Python `Fraction.from_float(r)` 或 `r.as_integer_ratio()` 得到精确有理值。

**验证步骤：**
1. 枚举 `i` 在以下区域：
   - `(-2^63, -2^53-1]`
   - `(-2^53, 2^53]`
   - `(2^53, 2^63-1]`
2. 对每个 `i`，选取 `r` 为：
   - `(double)i` 的相邻浮点数；
   - 接整数值附近的浮点数；
   - `-2^63` / `2^63` 边界值。
3. 构造 SQL 比较，如 `<` 谓词或 `CASE`，与 oracle 比较。

**仍缺少的证据：**
- 需要确认测试 SQL 中操作数确实一个被存为 INTEGER，另一个被存为 REAL；若整数文本/绑定参数被转换，会走错路径。
- 旧版 long double 与目标算法可能在所有正常输入上都等价；不能仅凭路径执行就认定有正确性问题。

---

### 3.4 总体仍缺少的证据

1. **完整调用图**  
   附件只有 `codeReal` 和 `printf.c` 的直接调用证据。  
   `sqlite3AtoF`、`sqlite3FpDecode`、`sqlite3IntFloatCompare` 的上层 SQL/VDBE 入口需要补全。

2. **旧版实际启用 long double 的条件**  
   不同平台第一父版本可能 `bUseLongDouble` 不同。  
   如果目标平台旧版本来就测到 `hasHighPrecisionDouble() == 0`，那么该平台两版行为可能基本相同。

3. **从 SQL 到二进制 double 的观察手段**  
   很多 SQL 输出会经过文本格式化，容易把 AtoF 和 FpDecode 的问题混在一起。  
   需要 C API/扩展/VDBE trace 或专门的观察方法。

4. **舍入边界值搜索空间**  
   候选不是“所有浮点数”，而是少数舍入边界附近的值。  
   需要独立搜索程序结合 oracle 筛选出真正可能出错的 `(s, e)` 和 double 值。

5. **正确性与“两版不同”的分离**  
   本提交删除 long double 后，目标版可能与旧版产生差异；但差异可能是旧版错误修正，也可能只是结果变化。  
   必须用独立 oracle 判定，而不是把“路径执行”或“两版输出不同”直接当作查询结果有错。

---

### 候选数量小结

依据附件直接给出的代码路径，建议 Stage 2 聚焦：

- `sqlite3AtoF`：3 类输入候选  
  - `e != 0` 且 `s` 接近 double 舍入边界；  
  - `e != 0` 且结果接近溢出/次正规边界；  
  - `e == 0` 代码形式变化，但低优先。

- `sqlite3FpDecode`：2 类输入候选  
  - 需要多次缩放的大/小 double；  
  - 十进制输出舍入中点附近的 double。

- `sqlite3IntFloatCompare`：1 类低优先候选  
  - 大整数与接近 double 精度边界的实数比较。

以上候选数量以已给出的源码路径为依据；完整 SQL 待下一阶段结合完整调用图和 oracle 搜索生成。