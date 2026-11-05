MySQL 三组提示词：实际需求输出与 SQL 生成结果
日期：2026-11-04（Asia/Shanghai）

本次由当前 Codex 助手完成两个阶段：先阅读指定 src2req 提示词并写出三份新需求，再把新需求填入原 req2test 模板，生成三份完整测试响应及可单独使用的 SQL 文件。没有调用其他模型 API，也没有运行数据库。这是同一对话中的两阶段生成，不是隔离双模型实验。

一、直接查看的文件

1. 派生表表达式克隆与字符集
   SQL：sql/derived_condition_charset_4d2da251cb53.sql
   src2req 输出：stage1_src2req/derived_condition_charset_4d2da251cb53.txt
   预期结果：expected/derived_condition_charset_4d2da251cb53.json
   8 个结果检查点：隐式 é、显式 utf8mb4 é、多字节 中、带单引号 O'Reilly，分别在条件下推 OFF/ON 下运行。用 HEX 和字符/字节长度判定，两个输入行应保留。

2. Item 属性重算
   SQL：sql/item_property_recalculation_248c7f7c227e.sql
   src2req 输出：stage1_src2req/item_property_recalculation_248c7f7c227e.txt
   预期结果：expected/item_property_recalculation_248c7f7c227e.json
   8 个结果检查点：窗口 SUM 外层算术表达式的预处理重复执行、改变绑定参数、直接查询；以及窗口表达式作为 IN 左操作数的重复执行、直接查询、移除右侧 NULL。两类候选分别记录。

3. 优化 ROWS 窗口帧状态
   SQL：sql/window_frame_state_c296cddb93ff.sql
   src2req 输出：stage1_src2req/window_frame_state_c296cddb93ff.txt
   预期结果：expected/window_frame_state_c296cddb93ff.json
   9 个结果检查点：DECIMAL/DOUBLE 的前向、当前至末尾、有界滑动帧；DOUBLE 高精度开关对照；非缓冲累计帧对照；AVG 与 FIRST_VALUE/LAST_VALUE/NTH_VALUE 的组合。数据含普通、混合 NULL、全 NULL、单行四种分区。

25 是标记的数据结果集数量，不是 25 个已触达分支、复现报告或独立缺陷。

二、两阶段衔接与来源

input_bundle/ 保存用户指定输入包的完整字节副本，包括旧种子需求和旧 req2test；22 条原 SHA256 校验全部通过。原目录没有修改。
stage1_src2req/ 是本次真正写出的六段式分析回答，分别包含 Target / Source-required conditions / Candidate construction / Correctness oracle / Coverage observation / Uncertainty。
stage2_req2test/prompts/ 是用新回答重新填充的三份第二阶段输入。
stage2_req2test/responses/ 是本次生成的完整五段式回答，包含前提、完整 SQL、逐案例预期结果、覆盖观测和执行状态。其中 SQL 代码块与 sql/ 下的文件一致。
generation_manifest.json 记录每个阶段输入/输出及 SQL/预期结果的 SHA256。

保留输入包固定于 fadce4b 的原模板和完整示例；没有静默升级模板。第二阶段当前需求使用本次 src2req 输出，不使用输入包的旧种子答案。分析绑定各自引入提交，未把后来的修复源码混入窗口帧目标。当前对话中两个阶段共享上下文，不宣称严格盲测。

三、如何使用 SQL 与预期结果

每份 SQL 在一个新的连接内完整执行，先选择已有、可丢弃的测试 schema。不要将 PREPARE/EXECUTE 拆到不同连接。脚本开头输出版本与环境信息，随后每个数据查询前都有单行 case_id 标签；按标签将下一份数据结果与 expected/ 中同名案例比较。环境信息与标签自身不计入 25 份数据结果。

脚本没有待补全的表名、数据或 SQL 模板参数。Item 用例中的 ? 是 PREPARE 的真实绑定参数，后续 EXECUTE USING 已提供值。

字符集文件是 UTF-8，包含真实 é、中文字和引号字面量，并设置 utf8mb4 会话字符集。它创建一张普通表，须保证 wf_4d2_text 不存在；结束时删除该表并恢复会话设置。另两组使用临时表，结束时释放临时表/预处理语句，窗口测试恢复精度设置。若中途报错，保留错误及最后一个 case_id，关闭会话释放临时对象；普通表仅在确认由本次成功创建后清理。脚本没有先行删除同名未知表。

expected JSON 中 null 是 SQL NULL；不得当作 0 或空字符串。Item IN 用例在右侧包含 NULL 时，不匹配结果应为 NULL；删除右侧 NULL 后才可能为 0。数值按值比较，忽略显示上的尾随零；窗口 DECIMAL 按显式六位小数转换的数学预期精确比较，DOUBLE 允许转换后绝对误差 0.000001，NULL 位置必须一致。所有数据 SELECT 有稳定输出顺序。

SQL 执行错误、缺失结果、崩溃、未触达及错误结果分别记录，不自动等同于新漏洞。指定源码分支的覆盖必须按每份完整响应中的观测位置确认，静态解析和结果正确都不能证明覆盖。

四、已完成的验证

validation.json：通过。
- 3 条输入→需求→新提示词→完整响应→SQL 的哈希与内容链检查。
- 25 个 case_id、输出列与结果顺序匹配。
- 从实际 SQL 的 INSERT 数据独立重新计算字符集结果、窗口帧结果和 IN 三值逻辑，核对全部预期行。
- SQLGlot 30.17.0 按 MySQL 方言静态解析普通 SQL 和 PREPARE 内部 SELECT。
- SQLGlot 没有完整支持此处 PREPARE/EXECUTE/DEALLOCATE 控制语法，因此这些控制语句单独检查格式、创建/释放顺序、占位符数量及参数赋值；不能把此项称作服务器语法验收。
- 创建与清理对象配对检查。

没有连接或执行 MySQL，没有验证服务器接受性、分支覆盖、性能或引入提交归因，也没有新增历史复现统计。

五、离线复核

在本目录执行：
  python -X utf8 -B validate.py
依赖 sqlglot，当前验证版本 30.17.0。验证脚本不连接数据库或网络。

prepare_prompts.py --input <原提示词目录> 可重新核对/复制输入并用 stage1_src2req/ 回答填充第二阶段；build_tests.py 可重新输出本次已编写的 SQL、完整响应和 oracle。这两个脚本是文本构建程序，不会重新调用 LLM。

SQL 构造时辅助核对的官方文档（不是运行证据）：
https://dev.mysql.com/doc/refman/8.0/en/derived-condition-pushdown-optimization.html
https://dev.mysql.com/doc/refman/8.0/en/window-function-optimization.html
https://dev.mysql.com/doc/refman/8.0/en/window-function-restrictions.html
https://dev.mysql.com/doc/refman/8.0/en/charset-introducer.html
