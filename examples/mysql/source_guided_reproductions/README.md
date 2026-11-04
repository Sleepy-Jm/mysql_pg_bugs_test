# 已验证的 MySQL 源码引导样例

这三组是**开发参考样例，不进入独立评测集**。它们展示如何从源码条件形成需求，再生成带独立预期值和对照的 SQL。目标提交均稳定产生错误结果，直接父提交均正确；每个版本三轮，共 18 次脚本执行、150 次检查点观测。本目录只整理已有材料，没有再次生成 SQL 或运行数据库。

本批生成共享同一对话上下文，且窗口案例存在生成前的答案相关实现暴露。使用前请读 [污染审查](../../../experiments/prompt_pipeline_20261104/contamination_review.md)。成功复现成立，但不能把它们作为盲测发现率或独立双阶段模型效果的证据。

## 可直接用作完整示例的提示词

| 样例 | 源码 → 完整需求答案 | 需求 → 完整测试答案 | 目标提交每轮失败检查点 |
|---|---|---|---|
| 字符集与派生条件下推 | [src2req](src2req/derived_condition_charset_4d2da251cb53.txt) | [req2test](req2test/derived_condition_charset_4d2da251cb53.txt) | DCP01_ON；其余 7 项正确 |
| Item 属性重算 | [src2req](src2req/item_property_recalculation_248c7f7c227e.txt) | [req2test](req2test/item_property_recalculation_248c7f7c227e.txt) | PROP_B2_REPEAT、PROP_B4_NO_NULL；其余 6 项正确 |
| 窗口帧状态 | [src2req](src2req/window_frame_state_c296cddb93ff.txt) | [req2test](req2test/window_frame_state_c296cddb93ff.txt) | WIN01、02、04、05、09；其余 4 项正确 |

每个文件都是一个已经填完答案的 `### Example task`，保留完整的源码或需求，以及当时的完整阶段输出。它们不是末尾留空的当前任务模板。我们去掉了历史提示词中的 INTERSECT 示例，将原“当前任务”转为教学示例，并改写开头指令以便独立阅读；只对副本统一 LF 换行，原始证据字节保持不变。

`req2test` 示例保留回答当时的 Execution status（尚未执行）；这是生成时的历史状态。之后的成功复现见下方实测报告，不把运行后发现的错误行追加到模型示例答案中。

## 后续实验如何使用

1. 选择一对示例，取完整 `src2req` 文件，然后追加 `### Current task`、本次独立目标的源码和空的 `# Description`。当前目标不能再是这三个目标或其语义近重复，否则属于开发复用。
2. 源码分析阶段输出完整需求。保留每项源码条件的提交、位置、证据不足之处，并把必须满足的条件与可选构造区分开。
3. 在新上下文中给测试生成阶段完整 `req2test` 示例，追加 `### Current task`、`# Description of requirements`、本次实际分析输出和空的 `# Test`。若要检验两阶段隔离，不能把前一阶段的完整对话、当前目标源码、修复或实测答案一并带入。
4. 从插入数据和 SQL 语义推导预期值，执行前冻结完整提示词、响应、SQL、预期文件及哈希。新建实验目录记录运行；失败后修改 SQL 属于另一次有反馈的尝试，不能覆盖首次结果。

保留示例的正例、正确对照、会话顺序、清理和设置恢复逻辑。特别是 Item 例，截取单条 SELECT 无法替代 PREPARE 后重复执行的整个过程。示例展示完整输入输出格式；将全部三个都拼入新提示词不是必要条件。

这些例子一旦用于提示或检索，就是已暴露的开发数据。评测时应按根因/触发机制分组排除相关目标、修复、父子提交及等价改写；更换常数、表名或别名不能使它们重新成为独立测试。清单中的 `evaluation_eligible=false` 只是明确用途，尚无评测调度器自动执行排除。

## 三组样例应该学到什么

### 字符集与派生条件下推

关键构造是 DISTINCT 派生表中的 `CONCAT(s,'é')`，外层过滤派生别名，使用明确的 utf8mb4 会话与排序规则。主例保留未带 introducer 的多字节字面量，再用下推 OFF、显式 `_utf8mb4`、中文字面量及带单引号字面量等对照区分条件。不是只要 SQL 中出现中文或非 ASCII 字符就足够。

原数据中 id=1、4 应匹配 `aé`，HEX 为 `61C3A9`，字符长度 2、字节长度 3。父提交与正确对照返回两行，目标提交 DCP01_ON 返回空集。条件来自表达式克隆、序列化目标字符集及下推门控；内部字节传播链的解释属于源码推导，未用插桩逐步验证。

[原 SQL](../../../experiments/prompt_pipeline_20261104/generation/sql/derived_condition_charset_4d2da251cb53.sql) · [预期](../../../experiments/prompt_pipeline_20261104/generation/expected/derived_condition_charset_4d2da251cb53.json) · [父结果](../../../experiments/prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/result.json) · [目标结果](../../../experiments/prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/result.json)

### Item 属性重算

关键构造组合了包装后的窗口表达式、IN 子查询左操作数和同一 PREPARE 的重复 EXECUTE。普通裸窗口函数、首次执行或直接查询不足以复现本批失败。普通窗口表达式复用的 A 组全部正确，应当保留这些未失败候选，不能只展示成功片段。

失败检查点的 `wrapped` 预期依次为 `11,31,71,41,NULL,NULL`，目标结果为 `NULL,11,21,41,111,81`；相伴的 IN 结果列仍正确。源码解释涉及属性刷新时窗口信息的传播及后续物化阶段选择；已验证的是结果差异及重复执行条件，没有记录每次刷新时的内部属性位。

[原 SQL](../../../experiments/prompt_pipeline_20261104/generation/sql/item_property_recalculation_248c7f7c227e.sql) · [预期](../../../experiments/prompt_pipeline_20261104/generation/expected/item_property_recalculation_248c7f7c227e.json) · [父结果](../../../experiments/prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/result.json) · [目标结果](../../../experiments/prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/result.json)

### 窗口帧状态

关键构造是需要缓冲、移动下界而上界固定在分区尾部的收缩 ROWS 帧，以 AVG 观察帧内非 NULL 行数。用多元素帧避免 SUM 恰好等于 AVG；DECIMAL 主例和 DOUBLE 的 high_precision OFF/ON 分开。全 NULL、单行、有界帧和累计帧作为边界与对照。

数据 `10,20,30,40` 在 id=2 的 `1 FOLLOWING ... UNBOUNDED FOLLOWING` 帧包含 `30,40`，故平均值为 35，目标返回 70。源码推导指出相对行位置与真实帧大小不一致可导致错误除数；这不是运行时除数的插桩观测。该案例生成前已接触另一版本的 AVG 分母实现，尤其不适合作为未知缺陷的独立发现证据。

[原 SQL](../../../experiments/prompt_pipeline_20261104/generation/sql/window_frame_state_c296cddb93ff.sql) · [预期](../../../experiments/prompt_pipeline_20261104/generation/expected/window_frame_state_c296cddb93ff.json) · [父结果](../../../experiments/prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/result.json) · [目标结果](../../../experiments/prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/result.json)

## 对应关系与离线核对

[manifest.json](manifest.json) 保存每对示例的哈希、原阶段文件与哈希、精确目标/父提交、运行记录、稳定失败和正确对照的 case_id。归档路径相对于 `experiments/prompt_pipeline_20261104/`，示例路径相对于本目录。

[完整历史链](../../../experiments/prompt_pipeline_20261104/lineage.json) · [实测报告](../../../experiments/prompt_pipeline_20261104/runtime/final_report.txt) · [源码机制及证据分级](../../../experiments/prompt_pipeline_20261104/source_mechanisms.md) · [污染审查](../../../experiments/prompt_pipeline_20261104/contamination_review.md)

从仓库根目录运行 `python -X utf8 -B examples/mysql/source_guided_reproductions/build_examples.py --check`，核对六份示例的确定性转换、原阶段文件哈希及 18 轮运行的检查点状态。再运行 `python -X utf8 -B experiments/prompt_pipeline_20261104/verify.py`，从原始 XML 重新核对 150 次观测。两者均离线，不执行 SQL。
