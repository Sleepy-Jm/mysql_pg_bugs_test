# MySQL 两阶段提示词版本包

本目录包含同一源码目标的两个可对照版本。两者都保留 Stage1 → Stage2 两阶段结构，以及 Stage2 生成五条实质差异化 SQL 的要求。

## 版本

| 版本 | 作用 | 是否接收执行反馈 |
| --- | --- | --- |
| [`two_stage_path_and_failure_20261112`](two_stage_path_and_failure_20261112/README.md) | 无反馈基线。Stage1 交接源码构造和敏感条件，Stage2 直接生成五条 SQL。 | 否 |
| [`two_stage_execution_feedback_20261112`](two_stage_execution_feedback_20261112/README.md) | 反馈版。执行 SQL 后分类路径命中和异常，并把带证据的样例回填到下一轮 Stage2。 | 是 |

## 共同约束

- Stage1 不生成当前案例的完整 SQL，只交付构造关系、输入条件、oracle 和缺失证据。
- Stage2 保留三段输出结构，并要求 T1-T5 具有有依据的实质差异；证据不足时允许报告短缺，不用表面变体凑数。
- 父子输出差异、路径猜测和 SQL 错误不会自动被称为 bug 或成功样例。
- 两个版本均未包含凭据、数据库目录、镜像或大型原始日志。

## 反馈版的额外接口

反馈版的 [`feedback_pipeline.py`](two_stage_execution_feedback_20261112/feedback_pipeline.py) 是离线适配器：它消费已有父/子提交执行器保存的结果目录，不启动数据库、不调用模型。只有下面两类证据可以进入下一轮 Stage2：

- `PATH_REACHED`：目标对象和修改路径有可核验的路径证据；这不代表异常。
- `ANOMALY_OBSERVED`：独立 oracle 有 expected/observed 和可核验的异常证据；路径命中和目标变更归因仍单独记录。

没有路径或独立 oracle 证据的父子差异只作为排除的诊断记录。
