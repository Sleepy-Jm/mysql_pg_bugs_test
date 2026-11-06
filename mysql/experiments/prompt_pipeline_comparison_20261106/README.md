# 首次实验与 DeepSeek 重跑：逐阶段输入输出对照

整理日期：2026-11-06。首次指 `prompt_pipeline_20261104`，重跑指 `mysql_three_prompt_deepseek_20261105_run_002`。本文从现有归档整理，未新增模型调用或数据库实验，未修改历史证据。

## 总体结果与阅读入口

| 目标 | 首次父提交 / 目标提交每轮通过数 | DeepSeek 重跑 | 完整逐阶段读本 |
|---|---|---|---|
| 派生表条件下推与字符集 | 8/8 / 7/8 | 父/目标三轮均无差异 | [派生表条件下推与字符集](derived_condition_charset_4d2da251cb53.md) |
| Item 属性重算 | 8/8 / 6/8 | 父/目标三轮均无差异 | [Item 属性重算](item_property_recalculation_248c7f7c227e.md) |
| 窗口帧状态 | 9/9 / 4/9 | 父/目标三轮均无差异 | [窗口帧状态](window_frame_state_c296cddb93ff.md) |

首次共 18 次脚本执行、150 次检查点观测，其中 24 次错误观测来自 8 个不同失败检查点，每个重复三轮；检查点数不等于独立缺陷数。DeepSeek 共 18 次脚本执行、9 组父/目标配对，均为 `no_observed_difference`。两批统计单位不同，不能把 150 和 9 直接比较为命中率。

## 每一步保存了什么

| 步骤 | 输入 | 输出 | 本次整理方式 |
|---|---|---|---|
| 0 固定材料 | 精确目标/父提交、源码节选、模板与 INTERSECT ALL 示例 | 输入包、哈希 | 各读本全文展示源码与共同 Stage 1 提示词，并验证两批字节一致 |
| 1 src2req | Stage 1 完整提示词；DeepSeek 实际 API messages | 测试偏好/需求：目标、源码条件、构造、oracle、覆盖观测、不确定性 | 两批原文全文保留；分别概括差异 |
| 2 req2test | 同一模板和示例，填入各自新 Stage 1 输出 | 完整响应（SQL、预期行、覆盖建议、执行状态） | 两批实际提示词、完整响应与提取 SQL 全文展示；旧种子不冒充实际输入 |
| 3 运行 | SQL、首次独立 expected JSON、精确构建、命令与 schema | 父/目标各三轮 XML、stderr、返回码和结果元数据 | 第一轮两侧结果转为可读表，所有三轮 XML/stderr/JSON 均有链接和哈希 |
| 4 判断 | 运行结果、首次语义 oracle / 重跑配对比较 | 首次逐检查点正确性；重跑结果/错误/退出码差异 | 保留原口径，不将无差异等同于分支覆盖或不存在缺陷 |

## 上下文与可比性

两批三个目标的 Stage 1 提示词和目标源码节选逐字节一致。模板参考提交为 `fadce4b16df62f362662754ee8e9745b478a643c`；输入包内的 Requirements 和旧 req2test 带人工种子，实际第二阶段均填入本次 Stage 1 输出。输入包存在文件不等于模型读过文件。

首次由同一 Codex 助手在共享聊天上下文直接完成两阶段，没有独立模型 API；归档没有可还原完整模型隐含上下文的独立请求信封。窗口案例生成前曾接触另一版本相关 AVG 分母实现。详见 [首次上下文审查](../prompt_pipeline_20261104/contamination_review.md)。首次可作为源码引导的开发复现样例，不能作无污染盲测。

DeepSeek 保存实际请求/响应；每次请求只含归档 messages，三组无共享对话历史。Stage 1 请求/返回 `deepseek-v4-pro`；Stage 2 请求 `deepseek-v4-flash`、返回 `deepseek-flash`，版本别名未独立确认。参数 temperature=0.7、max_tokens=16384、thinking=disabled。首次没有对应的独立 API 参数记录，不能补造同参数实验。

两批都未插桩测量目标源码分支。首次有稳定行为差异，DeepSeek 没有差异；这说明本次重跑未复现首次效果，但上下文、生成方式及 SQL 均改变，不能仅据此断言模型是唯一原因。

## 逐案例差异

### 派生表条件下推与字符集

首次要求行依赖 CONCAT、无前缀非 ASCII 字面量、DISTINCT 与下推 ON/OFF；DeepSeek Stage 1 偏向显式字符集前缀，Stage 2 使用可折叠的 ASCII 常量 alpha，且没有 DISTINCT。两者均谈到克隆路径，但 DeepSeek 未保留首次暴露异常的构造。

首次：父提交每轮 8/8、目标 7/8；DCP01_ON 目标空集，父提交返回 id=1、4，HEX=61C3A9。DeepSeek：两侧每轮均为两组相同的 4 行结果。

### Item 属性重算

首次要求把窗口表达式放在 IN 左侧，并在同一个 PREPARE 上重复 EXECUTE，另有直接查询对照；DeepSeek Stage 1 和 Stage 2 转为窗口 SUM 的参数内部包含 IN 子查询，以及存储函数参数。表达式树方向与生命周期压力都改变了。

首次：父提交每轮 8/8、目标 6/8；两个检查点错误，详见下方结果表。DeepSeek：两侧每轮均为两组相同的 5 行结果。

### 窗口帧状态

首次从 lower_limit=current_row+1 推导前向缩小帧，要求 1 FOLLOWING..UNBOUNDED FOLLOWING、DECIMAL/DOUBLE、高精度开关及其他帧对照；DeepSeek Stage 1 选择 1 PRECEDING..CURRENT ROW，Stage 2 沿用整数列和后向两行帧。

首次：父提交每轮 9/9、目标 4/9；5 个检查点错误。DeepSeek：两侧每轮均为相同的 8 行结果。

整理新增勘误：DeepSeek Stage 1 将 (1,NULL,3) 的第三行后向两行帧 AVG 写成 3/2=1.5；实际帧为 (NULL,3)，非 NULL 计数为 1，正确值为 3。Stage 2 已写成 3.0000，父/目标 XML 也均为 3.0000。此处保留两阶段原文，不静默修正历史回答。

## 归档边界与复核

每份读本均展示全部正式提示词、目标源码、两阶段输出和完整 SQL；执行部分展示两侧第一轮完整结果，并链接全部三轮原始文件。Markdown 是阅读副本，原始字节与 SHA256 以链接原件和 `evidence_index.json` 为准。目录内 `build_readers.py` 可从历史归档重新生成这些读本。

首次完整聊天上下文没有作为独立模型请求公开保存；重跑早期参数未冻结的部分试跑、缺依赖且未执行 SQL 的启动失败批次及原始服务大日志不进入成功执行统计，也不在本读本冒充可访问原件。排除项见两批 export_manifest.json。

本次整理没有新增服务器实验。复核可在首次目录执行 `verify.py`、重跑目录执行 `verify_export.py`；本目录的证据索引用于定位全部引用原件及其 SHA256。
