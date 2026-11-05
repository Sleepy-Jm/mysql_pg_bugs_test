# WhiteFox 风格的 MySQL 两阶段提示词

新对话实验使用 [独立实验启动包](mysql/isolated_experiment/README.md)：包含 src2req/req2test 启动提示词、阶段目录结构、文件白名单、最小交接清单及冻结模板。先由协调者填好输入，再分别交给两个新对话。

后续实验可选用 [三对已验证案例的完整示范](../examples/mysql/source_guided_reproductions/README.md)，再追加独立目标的当前任务；这些案例限定为开发参考。请同时阅读 [答案污染审查](../experiments/prompt_pipeline_20261104/contamination_review.md)，避免将已暴露目标再次当作独立评测。

已完成的三组生成与实测另见 [端到端实验索引](../experiments/prompt_pipeline_20261104/README.md)：逐组链接实际两阶段输入输出、SQL、预期值及目标/父提交的三轮执行证据。该归档保留当时模板快照；下述两个示例目标及离线生成清单保持各自范围。

条件如何转化为触发 SQL、哪些结论已验证，见 [三组源码机制解释](../experiments/prompt_pipeline_20261104/source_mechanisms.md)。

本目录按 WhiteFox 的 `Prompts/{compiler}/src2req/{name}.txt` 与 `req2test/{name}.txt` 组织，将目标改为 MySQL 源码路径。每份提示词都先提供 **完整示例任务、示例输入、示例答案**，然后提出 **当前任务、当前输入、待续写的答案标记**。

参考：[WhiteFox 仓库](https://github.com/ise-uiuc/WhiteFox)、[源码分析模板](https://github.com/ise-uiuc/WhiteFox/blob/main/template-torch/starcoder-src2nl-pattern.txt)、[测试生成模板](https://github.com/ise-uiuc/WhiteFox/blob/main/template-torch/starcoder-nl2test-oneshot-pattern.txt)。这里重新编写 MySQL 提示词和示例，沿用其 one-shot 结构与按目标实例化的方法。

## 目录及输入输出

```text
template-mysql/
  src2req.txt                  # 分析模板：完整示例＋当前源码任务
  req2test.txt                 # 生成模板：完整示例＋当前需求任务
  examples/
    intersect_join.requirements.txt
    intersect_join.test.txt    # 完整 SQL、输入、预期结果及清理
source-code-data/mysql/        # 固定提交的源码节选与来源记录
optim/mysql.json               # 示例、目标、源码和需求的路径映射
Requirements/mysql/req/
  <name>/<name>_1.txt           # 可独立编辑或用分析输出替换的需求
Prompts/mysql/
  src2req/<name>.txt            # 可直接发送给分析 LLM 的完整输入
  req2test/<name>.txt           # 可直接发送给生成 LLM 的完整输入
scripts/build_whitefox_prompts.py
```

`src2req` 要求根据源码条件构造高层测试需求，末尾为 `# Description`；`req2test` 要求将需求落实为 SQL、数据、预期结果和覆盖观测计划，末尾为 `# Test`。前面的 Description/Test 是示例答案，最后一个标记后的内容才是模型应生成的当前答案。文件末尾留空是有意的，不是缺少示例。

当前提供两个目标、共四份已填充提示词：

| 目标 | 源码与任务 | 两阶段提示词 |
|---|---|---|
| `partition_pruning_lock_state` | `prune_partitions` 中锁状态对范围分析参数的影响 | [源码→需求](mysql/src2req/partition_pruning_lock_state.txt) / [需求→测试](mysql/req2test/partition_pruning_lock_state.txt) |
| `window_avg_frame_count` | REAL/DECIMAL 窗口 AVG 使用累计行数计算分母 | [源码→需求](mysql/src2req/window_avg_frame_count.txt) / [需求→测试](mysql/req2test/window_avg_frame_count.txt) |

公共示例为 `INTERSECT ALL` 派生表与外表连接：提供真实源码节选、需求说明，以及手工推导得到四行 `1` 的完整 SQL。示例与两个当前目标不同，避免将当前目标的答案放入其源码分析提示词。`src2req` 的当前任务只读取当前源码，不读取当前需求；`req2test` 只读取需求，不拼接当前实现源码。

## 离线生成与使用

在仓库根目录运行（仅使用 Python 标准库）：

```powershell
python -X utf8 -B scripts/build_whitefox_prompts.py
python -X utf8 -B scripts/build_whitefox_prompts.py --check
```

1. 将 `src2req/<name>.txt` 的完整文本发送给分析 LLM。
2. 审阅输出中的源码条件、候选构造和缺失上下文，将当前任务的需求正文保存到 `Requirements/mysql/req/<name>/<name>_1.txt`。
3. 再次运行生成脚本，刷新对应 `req2test/<name>.txt`。
4. 将其完整文本发送给生成 LLM，获得 SQL 和判定说明。新生成内容先保存到 `local/` 审阅；本目录没有把自由文本自动转换成现有 runner 的 manifest。

新增目标时，保存带 revision、文件和行号的源码输入，准备对应需求文件，在 `optim/mysql.json` 的 `targets` 中增加路径映射后重新生成。`--check` 验证提交的提示词与模板、源码、需求完全一致，并检测多出的旧目标文件。普通生成只更新清单中的目标；删除目标后应显式删除它的两份旧提示词。

## 内容来源与验证范围

两个需求文件是根据工作区已有源码分析材料重新整理的种子需求，**不是本次调用 LLM 的结果**。示例 SQL 也是人工编写的格式演示。本次没有调用模型、执行 SQL 或测量分支覆盖。已有的 895 项报告集合和历史执行证据保持原有范围；这些新候选不进入其统计。

源码绑定的提交、blob 和行号见 [源码说明](../source-code-data/mysql/README.md)。局部源码条件不自动证明 SQL 能触达该分支，因此格式分别要求记录源码必要条件、候选映射、正确性 oracle 和覆盖证据。生成 SQL 后仍需按仓库 [工作流程](../docs/workflow.md) 准备独立执行记录。
