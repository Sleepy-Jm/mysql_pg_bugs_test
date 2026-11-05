# 源码差异、SQL 机制与 src2req 条件

本文件属于**生成结束和运行之后的协调者分析**，没有提供给对话 A 或 B。本次只评价原始隔离生成；有答案知识的补写执行已从本次结论排除。入口见 [README](README.md)，原始逐文件对应见 [lineage.json](lineage.json)，实测见 [原始报告](runtime/REPORT.md) ；被排除记录见 [审计说明](supplemental/README.md)。

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

## 2. Item 属性：原始生成子集未触发

### 材料链与 diff

[A 提示词](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/src2req_start.txt)、[源码](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/inputs/source_excerpt.txt) → [requirements](generation/stage1_src2req/item_property_recalculation_248c7f7c227e/outputs/attempt_001/requirements.txt) → [B 提示词](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/req2test_start.txt) → [原始 SQL](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/outputs/attempt_001/test.sql)、[映射](generation/stage2_req2test/item_property_recalculation_248c7f7c227e/outputs/attempt_001/requirement_mapping.json) → [原始目标结果](runtime/results/248c7f7c227e/trial_1/comparison.json)。

**源码事实。** [diff](source_analysis/item_property_recalculation_248c7f7c227e.patch) 比较 `15980860ac2639f41dfbda2f7fffb7aeeab32921` 与 `248c7f7c227e76f3422378ca3b9e10d141dcfc86`。通用 `Item_func::update_used_tables()` 增加 `m_accum_properties = 0`，然后从普通参数递归合并属性。初始化时的属性若不在此轮遍历中重新补回，就可能丢失。

**A 源码事实与推导。** R4 指出 `Item_in_optimizer.args[0]` 指向 IN 子查询对象，而左操作数另存在 `left_expr`；`fix_left()` 显式合并左表达式属性。R5 指出 IN 重算片段更新 left_expr 和表依赖，却没有显示对应的累积属性合并；A 没有基类完整实现，正确地未把这个缺口写成已证根因。R6 指出 `has_wf()` 参与帧缓存列筛选和参数替换，说明属性变化可能影响数据处理。

**原始实测。** B 只生成了直接 SUM、`1+SUM`、ORDER BY 别名和空帧，父/目标均4/4。普通算术参数可沿正常参数树传播窗口属性；该子集没有形成所关注的 IN 特殊关系，也没有同一预处理语句的重复执行。原始通过不证明 IN 路径正确，更不能写成模型已经复现。

### 本次可支持的结论

A 提取了 R4/R5 的 IN 特殊属性传播关系，但 B 将 C2/C4 的完整候选阻塞，未落实到 SQL。故本次只能判断四个已生成用例未复现，不能评价这些 IN 条件是否足以触发异常。PREPARE 重复执行来自后来的历史案例知识，不是本轮 A 的提取成果，已从本次机制验证证据中排除。内部重算调用、对象关系和属性位变化未插桩。

## 3. 字符集：原始没有生成 SQL，无本次运行证据

### 材料链与 diff

[A 提示词](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/src2req_start.txt)、[源码](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/inputs/source_excerpt.txt) → [requirements](generation/stage1_src2req/derived_condition_charset_4d2da251cb53/outputs/attempt_001/requirements.txt) → [B 提示词](generation/stage2_req2test/derived_condition_charset_4d2da251cb53/req2test_start.txt) → [blocked 记录](generation/stage2_req2test/derived_condition_charset_4d2da251cb53/outputs/attempt_001/requirement_mapping.json)。原始没有 SQL/expected，不能伪造占位成功结果。

**源码事实。** [diff](source_analysis/derived_condition_charset_4d2da251cb53.patch) 比较 `e248166db3c95b4fc998ca14cff914f1fdafbe7b` 与 `4d2da251cb536340d19438cc0039bb2846f9a634`。`parse_expression()` 的打印标志从 `QT_NO_DATA_EXPANSION` 改为 `QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET`。打印后重解析用于表达式克隆。

R1 给出下推资格；R2 指出外层派生列替换时克隆内层表达式；R3 指出打印/重解析；R4 区分有 introducer 时按字面量字符集转换、无 introducer 时按输出 String 的字符集转换；R5 指出无参数 StringBuffer 初始字符集为 binary。这些条件共同指向“克隆时是否保持字符串语义”，不是单纯测试数据库能否存 Unicode。

### 本次可支持的结论

R1–R5 指向“克隆时是否保持字符串语义”的候选机制，但 B 因字符集、防合并方式及控制语法未确认而 blocked。原始实验没有 SQL、预期结果或对应运行输出，因而不能说明这些条件已成功落实，也不能从本次声称验证了漏行机制。

历史知识补写的字符集选择、DISTINCT、具体字面量和下推开关构造，以及补写后得到的空集现象，均不作为本次验证证据。记录只保留在 [已排除审计材料](supplemental/README.md)。若重新评价无答案提示生成能力，需要新的受限生成尝试，不能将这些已知方案补回首次输出。
