# 三组源码差异、SQL 触发机制与 src2req 关键条件

本文解释 2026-11-04 三组生成 SQL 在目标提交与父提交上的行为差异。运行证据已在仓库提交 `170e762c2b8d82a767c0291fdefe1bcf7f0b5b8e` 归档；本文是其后补充的源码解释，没有新增数据库执行、覆盖插桩或干预实验。

## 阅读方式与证据等级

| 标记 | 含义 | 可以支持的结论 |
|---|---|---|
| **实测已验证** | 已归档的原 SQL、预期值、六个精确构建及三轮输出 | 某检查点在父提交正确、目标提交错误；具体错误行、重复稳定性和已运行对照 |
| **源码事实** | 固定提交的 diff 或函数实现可直接核对 | 改了哪条语句、某函数如何计算或传播属性；不等于该语句已被本次查询执行 |
| **源码推导** | 将 SQL 构造代入源码分支和状态关系 | 对异常的机制解释，以及对内部状态的预测；不是运行时抓取值 |
| **待验证** | 尚缺中间对象、调用序列或分支观测 | 需要插桩、断点或进一步对照才能闭合的因果环节 |

下文“关键条件”指 src2req 据源码选择、且与当前结果相关的测试构造条件。没有逐项最小化/消融实验时，不把它们全部称为严格必要条件。提交原本要修复的报告现象与本次生成 SQL 揭示的回归分别记录；三个目标也不能据此直接计作三个新漏洞或三个独立根因。

完整入口：[实验索引](README.md)、[端到端文件与哈希映射](lineage.json)、[详细实测报告](runtime/final_report.txt)、[逐项比较](runtime/comparison.json)、[150 次观测](runtime/case_results.csv)。

| 组 | 父提交 | 目标提交 | 每轮实测通过数：父 / 目标 |
|---|---|---|---|
| 派生表条件下推与字符集 | `e248166db3c95b4fc998ca14cff914f1fdafbe7b` | `4d2da251cb536340d19438cc0039bb2846f9a634` | 8/8 / 7/8 |
| Item 属性重算 | `15980860ac2639f41dfbda2f7fffb7aeeab32921` | `248c7f7c227e76f3422378ca3b9e10d141dcfc86` | 8/8 / 6/8 |
| 窗口帧状态 | `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` | `c296cddb93ffc631f9b43d3b1ff769604e7469d7` | 9/9 / 4/9 |

三轮的错误检查点及其输出均一致。共 18 次整份脚本运行、150 次检查点观测；126 次符合预期，24 次错误。没有 SQL ERROR、超时、服务器崩溃或 OOM。8 个不同失败检查点不是 8 个独立缺陷。

## 1. 字符集：表达式克隆时改变了字面量的转换路径

### 1.1 对应材料

[src2req 完整提示词](generation/input_bundle/Prompts/mysql/src2req/derived_condition_charset_4d2da251cb53.txt) → [实际分析输出](generation/stage1_src2req/derived_condition_charset_4d2da251cb53.txt) → [实际 req2test 提示词](generation/stage2_req2test/prompts/derived_condition_charset_4d2da251cb53.txt) → [完整测试响应](generation/stage2_req2test/responses/derived_condition_charset_4d2da251cb53.txt) → [完整 SQL](generation/sql/derived_condition_charset_4d2da251cb53.sql) → [预期结果](generation/expected/derived_condition_charset_4d2da251cb53.json)。

实测：[父提交结果](runtime/results/derived_condition_charset_4d2da251cb53/parent/result.json)、[目标提交结果](runtime/results/derived_condition_charset_4d2da251cb53/target/result.json)、[目标第一轮原始输出](runtime/results/derived_condition_charset_4d2da251cb53/target/trial-1.stdout.xml)。主要检查点为 `DCP01_ON`，总报告对应“派生表条件下推/字符集”。

### 1.2 父提交与目标提交的差异

**源码事实。** [提交 4d2da251cb53](https://github.com/mysql/mysql-server/commit/4d2da251cb536340d19438cc0039bb2846f9a634) 在 `parse_expression()` 中加入打印标志：

```diff
- item->print(thd, &str, QT_NO_DATA_EXPANSION);
+ item->print(thd, &str,
+             enum_query_type(QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET));
```

该提交原本处理 UNION 条件下推中的字符集保留问题。改动发生在共用的表达式克隆函数，所以本次测试采用普通派生表，通过同一类打印/重解析过程检验回归，不需要复制原提交测试中的 UNION/LIKE 形状。

**源码事实。** [`Item_string::print()`](https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/item.cc#L3433-L3477) 在新增标志生效时：显式打印字符集前缀的字面量按自身字符集转换，无前缀的字面量按输出 `String` 的字符集转换。调用者使用默认的 `StringBuffer<1024> str`；[默认构造](https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/include/sql_string.h#L628-L639) 设置的是 `my_charset_bin`，并非会话的 `utf8mb4`。

### 1.3 SQL 如何构成相关路径

下面是原测试的核心片段，完整建表、数据和清理见上方 SQL 链接：

```sql
SET NAMES utf8mb4 COLLATE utf8mb4_bin;
SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;
```

**源码推导。** 外层条件引用派生表输出 `d.tag`。下推时，需要将该引用替换为内层表达式，相关分析链为 `Item_field::replace_with_derived_expr` → `Query_block::clone_expression` → `parse_expression`。`CONCAT(s,'é')` 同时保留行依赖和字符串字面量；DISTINCT 阻止普通派生表合并，[`is_mergeable()` 明确排除 DISTINCT](https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/sql_lex.cc#L3785-L3792)。

由此得到待核对的机制链：无前缀字面量进入克隆 → 新标志选择输出缓冲区字符集 → 按 binary 转换 → 转换后的文本重新解析 → 筛选表达式不再保持原字符串语义。它解释了错误可以表现为漏行，而不必在投影结果里显示乱码。

**源码推导，不是已抓取的字节。** `convert_and_print()` 经 `THD::convert_string()` 调用字符集转换。按 [转换实现](https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/item.cc#L10620-L10632) 和 [binary 编码函数](https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/strings/ctype-bin.cc#L232-L248)，UTF-8 的 `C3 A9` 解码为 U+00E9，再编码至 binary 可成为单字节 `E9`，不再保持原 UTF-8 字节。此前未抓取克隆缓冲区和解析后的 Item，不能将此序列列为实测转储。

### 1.4 实测结果与关键条件

**实测已验证。** `DCP01_ON` 在父提交返回 `(1,'61C3A9',2,3)`、`(4,'61C3A9',2,3)`；目标提交返回空集，三轮相同。`DCP01_OFF` 正确；显式 `_utf8mb4'é'` 的 `DCP02_OFF/ON`、中文字面量 `DCP03_OFF/ON` 和带引号字面量 `DCP04_OFF/ON` 也都正确。

| src2req 中的位置 | 提取的条件 | SQL 落实及证据地位 |
|---|---|---|
| Source-required conditions 1 | 下推开启，并避开局部资格限制 | ON/OFF 对照已运行；不使用内部 LIMIT、外连接、CTE、查询内用户变量赋值，帮助保持候选资格 |
| 条件 2 | 外层引用指向同一派生表的输出表达式 | `WHERE d.tag=...` 与 `CONCAT(s,literal)` 构造替换目标；精确调用链未插桩 |
| 条件 3 | 克隆通过打印再解析，带新增标志 | diff 确认标志变化；实际打印字节、解析后对象待观测 |
| 条件 4 | 非常量表达式含字面量；显式/隐式前缀分支不同；默认缓冲区是 binary | `CONCAT(s,'é')` 对比 `CONCAT(s,_utf8mb4'é')`；该对照的结果差异已验证 |
| Candidate construction / oracle | 使用非 ASCII 字符并核对字节、长度 | `é` 暴露编码差异；HEX、长度和两条不同 id 的匹配行用于判定，不是触发操作 |

**待验证。** 记录实际克隆调用、`is_cs_specified/print_introducer`、缓冲区字符集和打印字节、解析后的字面量。现有对照支持机制解释，但没有证明每个候选资格条件都是最小触发所必需。

## 2. Item 属性：通用重算与 IN 左操作数的特殊传播关系

### 2.1 对应材料

[src2req 完整提示词](generation/input_bundle/Prompts/mysql/src2req/item_property_recalculation_248c7f7c227e.txt) → [实际分析输出](generation/stage1_src2req/item_property_recalculation_248c7f7c227e.txt) → [实际 req2test 提示词](generation/stage2_req2test/prompts/item_property_recalculation_248c7f7c227e.txt) → [完整测试响应](generation/stage2_req2test/responses/item_property_recalculation_248c7f7c227e.txt) → [完整 SQL](generation/sql/item_property_recalculation_248c7f7c227e.sql) → [预期结果](generation/expected/item_property_recalculation_248c7f7c227e.json)。

实测：[父提交结果](runtime/results/item_property_recalculation_248c7f7c227e/parent/result.json)、[目标提交结果](runtime/results/item_property_recalculation_248c7f7c227e/target/result.json)、[目标第一轮原始输出](runtime/results/item_property_recalculation_248c7f7c227e/target/trial-1.stdout.xml)。失败检查点为 `PROP_B2_REPEAT`、`PROP_B4_NO_NULL`，总报告对应“Item 属性重算”。

### 2.2 新增清零改变了属性重算的前提

**源码事实。** [提交 248c7f7c227e](https://github.com/mysql/mysql-server/commit/248c7f7c227e76f3422378ca3b9e10d141dcfc86) 在 `Item_func::update_used_tables()` 新增 `m_accum_properties = 0`。下列片段省略与累积属性无关的缓存更新：

```cpp
m_accum_properties = 0;  // 目标提交新增；父提交没有这一行
for (uint i = 0; i < arg_count; i++) {
  args[i]->update_used_tables();
  add_accum_properties(args[i]);
}
```

**源码推导。** 父提交保留已有属性再合并参数属性；目标提交从零重算。这样要求所有应该保留的属性都能沿本轮遍历重新汇总。IN 包装对象存在特殊的左操作数关系，值得针对性测试。

**源码事实。** [`Item_in_optimizer`](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.h#L472-L504) 的 `args[0]` 指向 `Item_in_subselect`，左操作数保存在后者的 `left_expr` 中：

```text
Item_in_optimizer
  └─ args[0] → Item_in_subselect
                   └─ left_expr → 1 + SUM(v) OVER w
```

初始化时 [`fix_left()`](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.cc#L2138-L2177) 显式执行 `add_accum_properties(left)`。但 [`Item_in_optimizer::update_used_tables()`](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.cc#L2410-L2419) 调用通用重算；[`Item_in_subselect::update_used_tables()`](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_subselect.cc#L2537-L2541) 更新左操作数并合并其 used_tables，却没有对应的左操作数累积属性合并。补读的 [基类实现](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_subselect.cc#L820-L827) 也只处理表依赖。

**源码推导。** 在该包装结构进入属性重算时，“先清零、再仅从普通参数合并”可能丢失初始化时从左操作数加入的窗口属性。这是源码中可指出的传播缺口；它与本次错误输出之间仍有执行链需要确认。

### 2.3 SQL 为什么选择窗口、IN 和重复执行

原测试 B 类预处理语句的 SELECT 主体为：

```sql
SELECT g, id,
       1 + SUM(v) OVER w AS wrapped,
       (1 + SUM(v) OVER w) IN (SELECT k FROM wf_248_lookup) AS in_result
FROM wf_248_values
WINDOW w AS (
  PARTITION BY g ORDER BY id
  ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING
)
ORDER BY g,id;
```

**源码推导。** `SUM(...) OVER w` 提供窗口属性，算术包装使属性需要向外传播；`CURRENT ROW AND 1 FOLLOWING` 使计算需要未来行和帧缓存。将表达式直接放在同一查询块的 IN 左侧，保留上述特殊传播关系。用一个 PREPARE 重复 EXECUTE 检查表达式复用；首次执行和直接查询作为已运行对照。

**源码事实。** `has_wf()` 影响实际数据处理。[`CreateFramebufferTable()`](https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/sql_select.cc#L4106-L4144) 用它排除不应保存在帧缓存中的窗口结果字段，也用它决定物化后哪些表达式参数需要替换为输出表字段。源码注释明确指出，恢复窗口结果字段可能覆盖已有的有效数据。

**源码推导。** 因此，丢失窗口属性可能改变帧缓存列筛选或表达式参数替换，进而影响窗口计算结果。该推导说明这不是仅影响 EXPLAIN 展示的标记。现有记录没有确定哪一个对象在何时丢位，也没有确定是哪一步恢复/替换导致本次 `wrapped` 错误，不能把上述消费者中的某一个直接写成已验证根因。

### 2.4 实测定位与关键条件

**实测已验证。** 首次执行 `PROP_B1_PREPARED` 和直接查询 `PROP_B3_DIRECT` 正确；重复执行 `PROP_B2_REPEAT`、删除 lookup 中 NULL 后的 `PROP_B4_NO_NULL` 错误。错误出现在 `wrapped`，对应行如下，三轮一致：

| `(g,id)` | 预期及父提交 | 目标提交的重复执行 |
|---|---:|---:|
| (1,1) | 11 | NULL |
| (1,2) | 31 | 11 |
| (1,3) | 71 | 21 |
| (1,4) | 41 | 41 |
| (2,1) | NULL | 111 |
| (2,2) | NULL | 81 |

两个失败检查点的 `in_result` 均符合原预期。右侧含 NULL 时是 `[1,NULL,1,NULL,NULL,NULL]`，删除后是 `[1,0,1,0,NULL,NULL]`。所以已验证现象是包含 IN 的查询在复用时产生窗口算术列错误，不能写成 IN 三值逻辑错误。右侧 NULL 不是本次异常的必要条件；这不等于已经检验了删除所有输入 NULL 的变体。

| src2req 中的位置 | 提取的条件 | 作用及证据地位 |
|---|---|---|
| Source-required conditions 1 | 通用重算先清空累积属性 | diff 中的核心变化；普通纯常量算术不能测试窗口属性丢失 |
| 条件 3 | `has_wf()` 参与帧缓存筛选和参数替换 | 提供属性错误影响结果的消费者；本次具体调用与对象尚未追踪 |
| 条件 4 | IN 包装对象与 left_expr 的特殊关系 | 决定把窗口表达式直接放在 IN 左侧；补读基类后确认重算缺少对应属性合并 |
| Candidate construction B | 同一个 PREPARE 重复执行，并有首次/直接查询对照 | 已观测到首次正确、重复错误；具体复用与重算调用时序仍待插桩 |
| Correctness oracle | 同时观察 wrapped 和 in_result，并区分 NULL 与 0 | 成功定位到算术列错误，防止误判 IN 的 UNKNOWN |
| 条件 2、Candidate construction A | Item_ref、不同窗口排序、参数变化候选 | A1–A4 均正确，不能列为本次已确认的异常机制 |

**待验证。** 记录 Item_in_optimizer 是否实际出现、其与 left_expr 的对象身份、重算前后属性位、prepared statement 跨执行的重用关系，以及帧缓存/替换/求值次序。尤其要解释 SELECT 中重复出现的 SUM 表达式之间的实际关系，才能把属性缺口与每个 `wrapped` 错值连接起来。当前不能从输出反推 `111`、`81` 来自哪一次具体写入。

## 3. 窗口帧：位置状态与 AVG 分母的语义不一致

### 3.1 对应材料

[src2req 完整提示词](generation/input_bundle/Prompts/mysql/src2req/window_frame_state_c296cddb93ff.txt) → [实际分析输出](generation/stage1_src2req/window_frame_state_c296cddb93ff.txt) → [实际 req2test 提示词](generation/stage2_req2test/prompts/window_frame_state_c296cddb93ff.txt) → [完整测试响应](generation/stage2_req2test/responses/window_frame_state_c296cddb93ff.txt) → [完整 SQL](generation/sql/window_frame_state_c296cddb93ff.sql) → [预期结果](generation/expected/window_frame_state_c296cddb93ff.json)。

实测：[父提交结果](runtime/results/window_frame_state_c296cddb93ff/parent/result.json)、[目标提交结果](runtime/results/window_frame_state_c296cddb93ff/target/result.json)、[目标第一轮原始输出](runtime/results/window_frame_state_c296cddb93ff/target/trial-1.stdout.xml)。失败检查点为 WIN01、WIN02、WIN04、WIN05、WIN09，总报告对应“窗口帧状态”。

### 3.2 修改的状态仍被 AVG 当作帧计数使用

**源码事实。** [提交 c296cddb93ff](https://github.com/mysql/mysql-server/commit/c296cddb93ffc631f9b43d3b1ff769604e7469d7) 原本修复 FIRST_VALUE 等函数的访问状态问题。与本次 AVG 异常最直接相关的是优化 ROWS 路径中的赋值变化。父提交使用：

```cpp
rn_in_frame = upper - lower_limit + 1;
w.set_rowno_in_frame(rn_in_frame);
```

目标提交仍计算 `rows_in_frame = upper - lower_limit + 1`，但在“减去旧首行、无新末行”分支中改为：

```cpp
w.set_rowno_in_frame(current_row - lower_limit + 1);
if (rows_in_frame > 0)
  w.set_is_last_row_in_frame(true);
```

**源码事实。** 该目标版本的 [REAL 和 DECIMAL AVG](https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc#L2279-L2365) 在需要缓存时仍使用 `rowno_in_frame() - m_frame_null_count` 作为分母；分母正值才执行除法，否则保留累计和。这里分析的是目标提交的实现，不能换成后续版本只依赖 `m_count` 的实现。

### 3.3 将 SQL 窗口代入状态公式

主要查询中的窗口是：

```sql
AVG(v_dec) OVER (
  PARTITION BY g ORDER BY id
  ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING
)
```

**源码推导。** `1 FOLLOWING` 使下界移动；`UNBOUNDED FOLLOWING` 使上界固定在末尾。在首轮聚合状态已建立、行可优化且需要移除旧首行时，后续不再添加新末行，进入上述状态赋值分支。[分支守卫及赋值](https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/iterators/window_iterators.cc#L1092-L1164)

第一分区按 id 排序为 `[10,20,30,40]`。以下是代入源码的预测值，而非运行时变量转储：

| 输出行和窗口 | 正确帧 | 正确行数 | 目标赋值 `current_row-lower_limit+1` | 推导结果 | 实测 |
|---|---|---:|---:|---|---|
| id=2，1 FOLLOWING 至末尾 | [30,40] | 2 | 2-3+1=0 | 分母为 0，跳过除法，保留 70 | WIN01/02：35 → 70 |
| id=2，CURRENT ROW 至末尾 | [20,30,40] | 3 | 2-2+1=1 | 90/1=90 | WIN04/05：30 → 90 |
| id=3，CURRENT ROW 至末尾 | [30,40] | 2 | 3-3+1=1 | 70/1=70 | WIN04/05：35 → 70 |

对第二分区 `[NULL,20,NULL,60]` 的 id=2，CURRENT ROW 至末尾包含 `[20,NULL,60]`。正确分母为 `3-1=2`；目标赋值代入得到 `1-1=0`，会保留累计和 80。**实测已验证：** WIN04/05 此行确为预期 40、实际 80。

因此，具体错误数值与该状态/分母失配的静态预测相符；但实际 `row_optimizable`、`inverse`、`rowno_in_frame`、NULL 计数和调用顺序仍未被探针记录。

### 3.4 对照为何有区分力

| 检查点 | 实测已验证 | 源码推导 |
|---|---|---|
| WIN03_REAL_FORWARD_PRECISE | DOUBLE、high_precision=ON 时正确 | REAL 移动下界的逆向优化受高精度设置限制，可避开相关增量路径 |
| WIN06_DEC_BOUNDED、WIN07_REAL_BOUNDED | 1 PRECEDING 至 1 FOLLOWING 正确 | 中间行添加新末行的分支会设置真实帧行数；本数据最后一行的相对位置也等于剩余帧行数。不能推广为所有有界帧都无问题 |
| WIN08_DEC_CUMULATIVE_CONTROL | UNBOUNDED PRECEDING 至 CURRENT ROW 正确 | 源码明确把该帧判为无需缓存，AVG 分母使用自身计数 |
| WIN09_VALUE_FUNCTIONS | 只有 avg_v 错误，FIRST/LAST/NTH_VALUE 正确 | 附加值函数用于检查共享状态，当前 AVG 单独查询已经失败，附加函数不是本次异常所必需 |

相关代码：[REAL 高精度门控](https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc#L1913-L1931)、[非缓冲累计帧判断](https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc#L410-L421)、[添加新末行时的赋值](https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/iterators/window_iterators.cc#L1214-L1226)。DECIMAL 不受这里专门针对 REAL 的高精度门控约束。

### 3.5 src2req 真正起作用的提取

| src2req 中的位置 | 关键条件 | 对 SQL 的影响 |
|---|---|---|
| Source-required conditions 1 | 缓冲窗口 AVG 消费 rowno_in_frame，并且正分母才除 | 选择 AVG 作为观察者，可以产生 SUM/AVG 明显不同的值 |
| 条件 2 | 累计到当前行为非缓冲特例 | 主查询采用其他帧，累计帧单列为对照 |
| 条件 3 | row_optimizable、aggregates_primed；REAL 逆向计算受高精度开关影响 | 分区包含多行，测试后续行；DOUBLE 分别运行 OFF/ON |
| 条件 4 | 移除旧首行且没有新末行时改写状态 | 选择移动下界和固定末尾的收缩帧 |
| 条件 5 | 1 FOLLOWING 可令相对位置为 0，而帧仍非空 | 构造 [30,40] 这类仍有两项的帧，使跳过除法的错误可见 |
| 条件 6 | 值函数和有界帧有其他状态设置 | 分别安排 WIN09 与 WIN06/07，避免只用复杂组合判断主路径 |

**实测解释边界。** 当前复现的是 AVG 回归，不是提交说明中 FIRST_VALUE 原始现象的复现。单元素帧的 SUM 等于 AVG，可能掩盖错误；全 NULL 或空帧输出 NULL，也不足以证明测试到了正分母路径。普通多元素帧用于暴露错误，NULL/单行分区用于检查边界与判定逻辑。

**待验证。** 同步记录窗口身份、输出行、上下界、`row_optimizable`、`aggregates_primed`、`new_last_row`、`inverse`、`rowno_in_frame`、`m_count`、NULL 计数和最终除数，才能把数学代入提升为逐步运行轨迹证据。

## 4. 文档与原证据的关系

实际分析答案是 `generation/stage1_src2req/`；实际第二阶段输入是 `generation/stage2_req2test/prompts/`。原输入包里的种子需求和旧 req2test 仅作来源快照，不代表本次采用的分析输出。上述条件编号均对应实际 src2req 输出中的 Source-required conditions，候选构造和 oracle 则另行标明。

本次补读源码包括字符集转换函数、Item_subselect 基类更新函数等，属于运行后的解释材料。没有回写原 src2req、生成 SQL、预期 JSON 或实测文件，也不把这些后验阅读冒充生成时已提供的上下文。原文件哈希及脱敏映射以 [export_manifest.json](export_manifest.json) 为准。

源码引用固定于完整 MySQL 提交 SHA。行为差异已经由同一原 SQL 的父/子提交对照和三轮重复支持；内部因果链的确认程度按本文标记分别记录。若后续增加插桩、最小化或补丁干预，应另建运行记录并关联原检查点，不覆盖此次证据。
