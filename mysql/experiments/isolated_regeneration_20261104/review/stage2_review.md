# 第二阶段审查与冻结（2026-11-04）

本次为已知三目标的隔离上下文重复生成。审查没有改动生成文件，没有执行数据库；不能写成三组 SQL 均已完整生成或全部通过。

| 目标 | 生成事实 | 审查/运行范围 |
|---|---|---|
| derived_condition_charset | C1–C3 全部 blocked，无 SQL、无 expected.json | 保留失败尝试；无输入可运行。不以旧成功 SQL 补齐。 |
| item_property_recalculation | 4 个检查点，24 行预期；C2、完整 C4 和可选 C5 blocked | 现有 SUM/包装/别名/空帧子集通过静态及 oracle 审查，可作目标/父提交对比；不代表完成全部需求。 |
| window_frame_state | 8 个检查点，105 行预期；可选 C5 blocked | 7 个检查点可判定；WF_UNBOUNDED 的 oracle 精度前提待核验，暂不允许直接据其 mismatch 判 bug。 |

## 需求及 oracle

独立审查程序从实际 SQL 的 INSERT 读取数据，按 UPDATE/后续 INSERT 切换数据状态，再从各查询解析 ROWS 边界，按分区位置枚举成员，处理 NULL、排序与精确算术。24+105=129 行都与生成的数学 oracle 相同，12 个 case_id 与映射一致。程序不执行原构建脚本，也不导入生成器的 oracle 代码。

Item 组仅覆盖 C1、局部 C3、C4 的 NULL/空帧前置数据，没有生成 IN 查询或 PREPARE 重复执行；因此无法用这份 SQL 评价 IN 包装相关需求是否完成。按已知案例补入这些条件会改变首次实验，本次不补写。其“No PREPARE needed”只能理解为当前基线脚本的执行说明，不是证明目标异常不需要重复执行。

字符集组的 blocked 是模型在本次受限协议下的生成结果，不证明相关 SQL 不存在或 MySQL 不支持相应功能。它把版本前提未验证视作阻塞，Item 组也将 IN 路径确认留待补充；两阶段需求边界可能过于依赖先验证可达性。未来若放宽成“允许构造未验证候选”，必须另建协议/attempt，不能悄悄替换本次结果。

### 窗口精度问题：保留为独立待核验项

WF_UNBOUNDED 的 (p=1,id=5) 数学平均是 2460/7，原 expected 写 351.428571。输入为 DECIMAL(10,0)，外层 CAST(... AS DECIMAL(18,6))；脚本没有设置或记录 div_precision_increment。纯数学检查直接舍入到 6 位，未模拟 AVG 的中间结果类型和物化精度。

协调者在 B 完成后补读目标提交的 Item_sum_avg::resolve_type 与 create_tmp_field：精确类型 scale 由输入 decimals 加 div_precincrement 决定，临时 DECIMAL 字段由 Item 类型创建。默认增量 4 时存在先保留 4 位再 CAST 到 6 位的风险；351.428600 是该模型下的结果，不是本次数据库实测值。外层 CAST 本身不能证明未提前损失精度。因此整个 WF_UNBOUNDED 检查点暂存 oracle_hold，其他 7 项的本批数据不受这项数学差异影响。不能看到父版本输出后简单把它抄成 oracle。

来源（审查者事后读取，未提供给 B）：
- https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc （相关片段另存 stage2_precision_source.txt）
- https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_div_precision_increment
- https://dev.mysql.com/doc/refman/8.0/en/window-functions-frames.html

## 输入边界与答案污染

对话“生成 MySQL req2test 用例”只有一轮可返回记录，无更早分页。用户附带的启动文本与保存的 START_req2test.txt 去除首尾空白后相同。全部阶段交接冻结哈希、9 项白名单输入、生成清单记录的输出及生成结束时清单哈希均匹配。

没有观察到 B 读取阶段一源码、旧 SQL、旧 expected、修复、实测报告、Git、网络或其他对话。用户明确提供的启动附件属于授权控制材料，不按禁读答案处理。node_repl 仅导入 Node 标准库；保存的构建脚本读取白名单及自己的输出，未见外部答案获取。自动初始 cwd 实际为 stage1_src2req，首个命令读取启动附件并非递归列举 stage2 根目录元数据，后续还有空输出目录检查；这些偏离已记录，不能称为严格零偏离，但未观察到它们暴露答案内容。

可返回的命令记录有长度上限，部分长写入命令被截断；审查同时读了保留的构建程序并核对清单哈希。context_logs 中保存的是工具可返回的消息/调用/输出快照，不包含隐藏平台上下文和 reasoning，不声称完整捕获内部过程。三目标共享 B 的上下文，模型训练记忆无法排除。结论为 no_observed_answer_content_exposure_with_metadata_deviations，不是“保证无污染”。

生成清单中的 Python unavailable 表示当时尝试的 python/py 入口不可用，不能推广为机器上不存在 Python；后续用 Node 完成生成与静态检查。未见数据库执行反馈。stage2_response.txt 是摘要，不是完整消息记录。

## 冻结与运行准备

所有 21 份阶段输出（含 blocked 记录、构建程序、三个清单）原样冻结；冻结不等于批准全部 oracle。approved_runtime_inputs 保存两组 SQL、expected 和映射的逐字节副本，运行清单显式排除字符集组，标注 WF_UNBOUNDED 的 oracle_hold。

Item 与窗口目标/直接父提交各规划三轮，共 12 次完整脚本执行，执行尚未开始。每轮新连接、新可丢弃 schema，同一 SQL 脚本不得拆成各条独立连接。窗口脚本中途更改数据和精度设置必须按原顺序运行；不得通过 --force 继续执行错误后的语句。

运行前须验证实际构建 SHA、直接父子关系、无补丁状态及二进制哈希；记录同一会话的版本、sql_mode、div_precision_increment 和 windowing_use_high_precision。确认增量为既定默认 4；其他环境另记，不能静默调到 6 只为迎合 expected。必须有能识别结果集序号、NULL、numeric normalization、ordered rows 和 REAL 容差的适配器；当前 runtime_plan.json 是计划，不是假装已接入现有 runner。

允许完整执行窗口脚本并保存所有原始输出；WF_UNBOUNDED 结果只能标 oracle_pending，待独立精度/类型证据解决后另存判定，不能覆盖原 expected。错误、崩溃、超时、缺结果集和 wrong_result 分开记录；无差异如实保留，不为凑三组成功而替换 SQL。后续任何修订均另建 attempt。
