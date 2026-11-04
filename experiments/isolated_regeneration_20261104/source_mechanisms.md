# 源码差异、SQL 机制与 src2req 条件

本文件属于**生成结束和运行之后的协调者分析**，没有提供给对话 A 或 B。原始隔离生成与后续有答案知识的补充实验分开统计。入口见 [README](README.md)，原始逐文件对应见 [lineage.json](lineage.json)，实测见 [原始报告](runtime/REPORT.md) 和 [补充报告](supplemental/REPORT.md)。

证据分为四类：**源码事实**是固定提交的实现或 diff；**源码推导**是将 SQL 代入实现的预测；**实测**是保存的输出；**待验证**包括没有插桩的对象身份、分支和中间状态。错值与公式吻合支持机制，但不是已经抓取到内部变量。以下不宣称三个新漏洞，也不将每个失败用例计为独立根因。

## 1. 窗口帧：原始隔离生成成功复现

### 材料链

[A 提示词](generation/stage1_src2req/window_frame_state_c296cddb93ff/src2req_start.txt) + [实际源码输入](generation/stage1_src2req/window_frame_state_c296cddb93ff/inputs/source_excerpt.txt) → [A requirements](generation/stage1_src2req/window_frame_state_c296cddb93ff/outputs/attempt_001/requirements.txt) → [B 提示词](generation/stage2_req2test/window_frame_state_c296cddb93ff/req2test_start.txt) + [交接需求](generation/stage2_req2test/window_frame_state_c296cddb93ff/inputs/requirements.txt) → [SQL](generation/stage2_req2test/window_frame_state_c296cddb93ff/outputs/attempt_001/test.sql)、[预期](generation/stage2_req2test/window_frame_state_c296cddb93ff/outputs/attempt_001/expected.json)、[条件映射](generation/stage2_req2test/window_frame_state_c296cddb93ff/outputs/attempt_001/requirement_mapping.json) → [父提交首轮](runtime/results/74c7ccfa27f4/trial_1/comparison.json)、[目标首轮](runtime/results/c296cddb93ff/trial_1/comparison.json)。其他两轮在相邻目录。

### 改动与消费者

**源码事实。** [完整生产源码 diff](source_analysis/window_frame_state_c296cddb93ff.patch) 比较 `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` 与 `c296cddb93ffc631f9b43d3b1ff769604e7469d7`。优化 ROWS 帧移除旧首行、没有新末行的分支，原来设置 `rowno_in_frame = upper - lower_limit + 1`；目标改成 `current_row - lower_limit + 1`。前者是帧总行数，后者是当前输出行相对帧起点的位置。目标仍在非空帧设置 last 标志并调用 framing 函数。

同一目标源码 `Item_sum_avg` 的 REAL/DECIMAL 路径在缓冲情况下仍以 `rowno_in_frame() - m_frame_null_count` 为除数，正除数才执行除法。字段被当作“位置”更新，却被 AVG 消费为“帧数量”，构成需要测试的语义冲突。相关行号和代码直接保留在上述 A 输入中（window_iterators.cc:1145–1165、item_sum.cc:2279–2365）。

### 为什么本轮有界帧能触发

主查询是 `AVG(v) OVER (PARTITION BY p ORDER BY id ROWS BETWEEN 2 PRECEDING AND 3 FOLLOWING)`。第一分区为 `[60,180,120,300,240,420,360,540,480]`，id 唯一，v 为 DECIMAL(10,0)。在分区中部，删除旧行后还能加入新行；到尾部，上界超过分区末尾，帧下界仍移动，出现“只删除、不添加”的候选路径。

**源码推导与实测对照：**

| 当前 id | 帧 id | 帧和 | 正确除数 | 目标公式预测除数 | 预期 / 父提交 | 目标实测 |
|---|---|---:|---:|---:|---:|---:|
| 7 | 5–9 | 2040 | 5 | 7−5+1=3 | 408 | 680 |
| 8 | 6–9 | 1800 | 4 | 8−6+1=3 | 450 | 600 |
| 9 | 7–9 | 1380 | 3 | 9−7+1=3 | 460 | 460 |

这也解释了为什么最后一行反而正确：两个公式在该行偶然相等，并不表示前面的错误不存在。2040/3=680、1800/3=600 与目标三轮结果一致；中间状态没有直接观测。

`WF_NULLS` 把 id=2、5、8 改为 NULL。id=7 的帧有两个 NULL，非 NULL 值为 `[420,360,480]`，和为1260、正确非 NULL 数为3；目标公式预测 `3−2=1`，返回1260。id=8 的帧有一个 NULL，目标公式预测 `3−1=2`，返回630；两行正确答案都为420。`WF_REAL_LOW` 对 DOUBLE 且关闭高精度采用同样数据，出现相同错误；`WF_REAL_HIGH` 通过。精度选项限制可优化路径这一源码事实支持差异解释，但未插桩证明具体优化分支。

### A 提取的关键条件如何落实

| requirements 条件 | SQL 选择 | 对机制的作用与证据 |
|---|---|---|
| R1、R5 | 有界移动帧，关注分区尾部 | 区分输出行位置与帧大小；尾部错值实测符合位置公式 |
| R2 | AVG、显式 ROWS、非 DISTINCT、后置边界 | 构造需要缓冲的候选；无界前置到当前行为对照 |
| R3、R4 | 九行、前置2行/后置3行、唯一顺序键 | 为聚合状态建立后“移除且无新末行”创造条件；内部 primed/优化资格仍待观测 |
| R6 | CURRENT ROW 上界对照 | 区分有新末行的赋值路径；该用例实际通过 |
| R7 | AVG 消费位置；先全非 NULL，再加入 NULL | 可手工核算帧和及分母；三组错误值与预测一致 |
| R8 | DOUBLE 分别设置高精度0/1；DECIMAL 主候选 | 低精度错、高精度对，提供已运行路径对照 |

`WF_UNBOUNDED` 仍为 oracle_hold：父提交一行返回351.428600，原 expected 为351.428571；中间 DECIMAL 精度与最终 CAST 的问题已有[运行前审查](review/stage2_review.md)。不能为增加成功数而事后改 expected。FIRST/LAST/NTH 是 A 的可选 C5，并非本次 AVG 触发的必需 SQL 成分，未补入。

## 2. Item 属性：原始子集未触发，补充 IN / 复用路径

### 材料链与 diff

[A 提示词](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/src2req_start.txt)、[源码](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/inputs/source_excerpt.txt) → [requirements](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/outputs/attempt_001/requirements.txt) → [B 提示词](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/req2test_start.txt) → [原始 SQL](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/outputs/attempt_001/test.sql)、[映射](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/outputs/attempt_001/requirement_mapping.json) → [原始目标结果](runtime/results/248c7f7c227e/trial_1/comparison.json)。

**源码事实。** [diff](source_analysis/item_property_recalculation_248c7f7c227e.patch) 比较 `15980860ac2639f41dfbda2f7fffb7aeeab32921` 与 `248c7f7c227e76f3422378ca3b9e10d141dcfc86`。通用 `Item_func::update_used_tables()` 增加 `m_accum_properties = 0`，然后从普通参数递归合并属性。初始化时的属性若不在此轮遍历中重新补回，就可能丢失。

**A 源码事实与推导。** R4 指出 `Item_in_optimizer.args[0]` 指向 IN 子查询对象，而左操作数另存在 `left_expr`；`fix_left()` 显式合并左表达式属性。R5 指出 IN 重算片段更新 left_expr 和表依赖，却没有显示对应的累积属性合并；A 没有基类完整实现，正确地未把这个缺口写成已证根因。R6 指出 `has_wf()` 参与帧缓存列筛选和参数替换，说明属性变化可能影响数据处理。

**原始实测。** B 只生成了直接 SUM、`1+SUM`、ORDER BY 别名和空帧，父/目标均4/4。普通算术参数可沿正常参数树传播窗口属性；该子集没有形成所关注的 IN 特殊关系，也没有同一预处理语句的重复执行。原始通过不证明 IN 路径正确，更不能写成模型已经复现。

### 补充构造及知识来源

[补充 SQL](supplemental/inputs/item_property_recalculation_248c7f7c227e/test.sql) 与 [预期](supplemental/inputs/item_property_recalculation_248c7f7c227e/expected.json) 沿用 B 数据：第一分区 `[2,5,11,17]`，第二分区 `[3,NULL]`。`CURRENT ROW AND 1 FOLLOWING` 的 SUM 为 `[7,16,28,17,3,NULL]`，加1为 `[8,17,29,18,4,NULL]`。

补充将 `(1+SUM(v) OVER w)` 直接置于 IN 左侧，并同时投影 wrapped；右侧初始为 `[8,29,NULL]`。因此 IN 预期为 `[1,NULL,1,NULL,NULL,NULL]`。删除右侧 NULL 后为 `[1,0,1,0,0,NULL]`；清空右侧后全部为0，包括 NULL 左值。以同一个 PREPARE 做首次、重复、删除 NULL 后和空集合执行，并有直接查询对照。

R1/R2/R4/R5/R6 和 C2/C4 支持 IN/窗口/缓冲关系；**重复 PREPARE 是协调者从历史已知成功案例补充的操作，不能追认成原始 A 已提取的条件**。其意义是检查重算与表达式复用，而不是给普通直接查询增加无关复杂度。补充结果和具体错误行见[补充报告](supplemental/REPORT.md)。即使出现错值，实际对象属性丢失时刻、共享 SUM 对象关系、帧缓存写入次序仍需断点或插桩确认。

## 3. 字符集：原始无 SQL，补充后检验打印再解析

上一节 Item 的**补充实测**为：父提交三轮6/6、目标三轮3/6。SI_FIRST、SI_DIRECT、SI_EMPTY_DIRECT 正确；SI_REPEAT、SI_NO_NULL、SI_EMPTY 的 wrapped 均从 `[8,17,29,18,4,NULL]` 变为 `[NULL,3,10,24,47,39]`，而 in_result 仍与预期一致。这把本次已验证现象限定为包含 IN 的查询复用时窗口包装列错误，而非 IN 真/假/未知逻辑错误。右侧无 NULL 甚至为空仍出现同类 wrapped 错误，说明这两个右侧数据特征没有消除本轮现象；尚不能从错值反推出具体缓存写入来源。

### 材料链与 diff

[A 提示词](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/src2req_start.txt)、[源码](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/inputs/source_excerpt.txt) → [requirements](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/outputs/attempt_001/requirements.txt) → [B 提示词](generation/stage2_req2test/derived_condition_charset_4d2da251cb53/req2test_start.txt) → [blocked 记录](generation/stage2_req2test/derived_condition_charset_4d2da251cb53/outputs/attempt_001/requirement_mapping.json)。原始没有 SQL/expected，不能伪造占位成功结果。

**源码事实。** [diff](source_analysis/derived_condition_charset_4d2da251cb53.patch) 比较 `e248166db3c95b4fc998ca14cff914f1fdafbe7b` 与 `4d2da251cb536340d19438cc0039bb2846f9a634`。`parse_expression()` 的打印标志从 `QT_NO_DATA_EXPANSION` 改为 `QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET`。打印后重解析用于表达式克隆。

R1 给出下推资格；R2 指出外层派生列替换时克隆内层表达式；R3 指出打印/重解析；R4 区分有 introducer 时按字面量字符集转换、无 introducer 时按输出 String 的字符集转换；R5 指出无参数 StringBuffer 初始字符集为 binary。这些条件共同指向“克隆时是否保持字符串语义”，不是单纯测试数据库能否存 Unicode。

### 补充 SQL 为什么有区分力

[补充 SQL](supplemental/inputs/derived_condition_charset_4d2da251cb53/test.sql) 固定 `SET NAMES utf8mb4 COLLATE utf8mb4_bin`，数据为 `(1,'a'),(2,'b'),(3,''),(4,'a'),(5,NULL)`。内层 `SELECT DISTINCT id, CONCAT(s,'é') AS tag`，外层过滤 `tag=_utf8mb4'aé'`。DISTINCT 防止普通派生表合并，保留表达式下推的候选路径；非恒定列 s 避免整个表达式只是常量。SELECT DISTINCT 包含唯一 id，所以不会把两条匹配记录合成一条。

**独立语义预期。** id=1、4 均得到 `aé`：HEX=61C3A9、字符数2、字节数3；其他行不匹配。开启或关闭下推必须保持这两行结果。显式 `_utf8mb4'é'` 控制 introducer 分支；ASCII `'x'` 检查普通路径不变。预期直接由输入字符/字节和等值关系推导，不以父提交充当答案。

**源码推导。** 无 introducer 的非 ASCII 字面量经新增标志进入输出缓冲区字符集转换，再被解析；这可能改变克隆表达式的编码语义，导致过滤漏行。显式前缀保持表达式字符集，ASCII 在相关转换下不显现同样的字节差异。实际打印字节、解析后 Item 和转换警告未记录，因此不能声称已抓取具体乱码字节。

**补充实测。** 父提交三轮6/6，目标三轮5/6；仅 `SC_IMPLICIT_ON` 从预期两行变为空集。其余五个开关/前缀/ASCII 对照均正确。这支持上述机制，尚不等于每项条件都是经最小化证明的必要条件。

原始 B 因无法确认字符集、防合并与控制语法而 blocked；补充使用历史案例中的具体字符集、DISTINCT 和下推控制知识解决了设计前提。故这是**有答案知识的补充执行成功**，不能改写为原始隔离模型独立生成成功。可选存储函数和 FIRST/LAST/NTH 扩展没有被当作三个主案例必须补齐的执行项。
