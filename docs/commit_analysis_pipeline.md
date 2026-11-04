# Commit 分析与候选种子流程 v1

这是独立的新流程。原有 post-change src2req/req2test、Codex 探索、隔离重复生成、
报告主集合和历史 SQL/哈希均保持原样；本流程结果不并入它们的统计。

入口：src/mysql_bugs_test/commit_pipeline.py（Python 标准库）。
新提示词：Prompts/mysql_commit/。没有依赖旧实验的需求、答案或响应。
本次验收是合成案例的工程验证，不是数据库实验或 LLM 效果验证。

## 输入和两个阶段

prepare 从指定的本地 MySQL Git 仓库读取精确 commit、直接父提交、message、
显式白名单生产文件的完整 diff，以及所选 before/after/helper 源码行段。
merge commit 必须显式选择直接父提交。不自动 checkout、联网或收集测试答案。
辅助函数也需显式列入白名单；新增/删除文件不存在的一侧留空即可。
diff 的引用行号是保存的 diff 文本行号；before/after 是原源码行号，两者不可混用。

configs/commit_pipeline_sources.example.json 是待填写的输入示例。版本和提交角色
由筛选材料提供，不从文件日期推测，证据不足时填 unknown。函数名同样可填 unknown。
所有源码片段保存其 revision、路径、起始行和内容哈希。所选 commit 如果是修复提交，
必须标 fix，不能将该运行解释为仅凭引入提交的盲生成。

第一阶段 JSON 的 changes 按不同语义变化拆分，保存版本、父/目标 SHA、改动类型、
模块、位置/函数、facts、affected_features、conditions 和 unknowns。
facts 和 source_supported 条件必须引用 supplied source_id、闭区间行号及逐字 quote。
hypothesis/unknown 可无引用，但不得改称源码事实。程序核查引用文本，不自动证明
自然语言解释正确；semantic_accuracy 始终为 not_evaluated，仍需源码语义审查。
not_sql 或没有可映射条件的分析单独保存，第二阶段记未运行，不强制凑 SQL。

第二阶段只收到分析、版本、输出结构和上一轮合格样例，不拼接原始源码或 diff。
交接视图保留证据定位，去掉 evidence.quote；第一阶段原件不修改。
每个候选包含 condition_ids，以及独立的 setup / operations / cleanup 步骤数组；
步骤包含 session、sql 和 condition_ids，数组顺序就是操作顺序。
configuration 记录配置要求，session_order 标明会话安排；涉及跨阶段交错、同步、
并发或工具不支持的结构须放入 capability_gaps，执行器不得自行扁平化。
expected_observations 描述要观测什么；proposed_oracle 是尚待独立校验的结果推导。
字段检查成功不等于 SQL 可执行，SQL validity 由外部执行证据单独提供。

## 10 × 10 协议

每个 run 只有一次第一阶段分析，最多 10 个有顺序的第二阶段批次，每批请求 10 个
完整候选用例。10 轮不是 10 次独立重复；重复实验应创建新 run。
收到不足 10 个或空批次时保留 shortfall_reasons，不补造、不自动补齐。
请求数、返回数、接受数、执行数分别记录；超量、重复用例或结构错误的原响应仍保留，
整个批次不接受，不能暗中挑出好结果计为成功。

第 1 轮使用默认提示；第 r+1 轮仅使用第 r 轮被独立检测器证据判定为 hit 的样例。
按原候选顺序全部选入（最多 10 个），记录 ID、候选哈希、来源轮和选择原因。
第 r 轮无合格命中时回退默认提示，即使更早轮次存在命中也不回收使用。
oracle 异常候选不能代替目标 hit。没有观测的候选不会进入反馈。
生成不自动执行数据库；每轮需显式登记反馈（可以登记尚未执行），才可继续。

API、格式或引用校验失败会保存 attempt/request/raw response（若取得）和失败阶段。
不自动换模型、重试或覆盖。修订另建 run，旧失败保留；未进行的后续轮次仍显示 not_run。
进程在已有 attempt 后中断而没有 result 时为 interrupted_unknown，不认定 API 成功
或确定没有远端费用；本地请求发送失败不等于证明服务端没有完成。

## 使用顺序

以下命令在本仓库根目录执行。先填写 spec，并选定已有的 MySQL 源码仓库和 SHA。
示例中的 MYSQL_SOURCE_REPO、TARGET_SHA、RUN_ID 需要换成真实值。Windows 如 python
不可用，请改用已安装解释器的绝对路径。

1. 只准备输入，不调用模型：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py prepare --repository MYSQL_SOURCE_REPO --commit TARGET_SHA --spec local/sources.json --output local/material.json

2. 创建新 run 并保存第一阶段请求预览（默认不联网）：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py init --material local/material.json --run local/RUN_ID --run-id RUN_ID

   有已审查的独立检测器时，加 --contracts local/contracts.json。
   没有 contracts 也可生成，但无法将任何样例判为已验证 hit/oracle 命中。
   所有 contracts 在 init 时冻结，不能看到本轮结果后修改阈值。
   初始参数为 deepseek-v4-pro、thinking disabled、temperature 0.7、max_tokens 16384；
   init 可显式调整这些参数，全部进入 manifest。thinking enabled 时温度的实际作用
   以供应商 API 语义为准；别把传入参数等同于供应商确实采用了它。

3. 由环境变量 DEEPSEEK_API_KEY 提供凭据。独立查询可用模型（不生成）：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py models --output local/model_probe.json

4. 显式请求模型，每次 step 只执行一个阶段/批次：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py step --run local/RUN_ID --execute-model

   第一次执行第一阶段；核对其事实、引用与未知信息后，再次执行才是第 1 轮候选。
   不带 --execute-model 只保存/显示下一请求，不联网。
   不允许以旧 Codex 响应冒充此入口的 DeepSeek 响应。

5. 独立执行器验证候选、保存观测，然后登记：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py feedback --run local/RUN_ID --round 1 --input local/observations/round01.json

   若本轮没有执行条件，可以省略 --input，显式将所有候选登记为 not_run/unknown。
   这允许继续默认生成，却不能形成真实反馈效果结论。第 10 轮同样登记反馈。
   重复步骤 4–5 至预算结束，不并行生成有依赖的轮次。

6. 离线读取汇总：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py report --run local/RUN_ID

## 独立观测接口

检测器契约的字段见 configs/commit_pipeline_contracts.example.json。示例故意含未填写的
producer 哈希，直接使用会被拒绝。必须先审查实际观测程序、目标定义和 oracle，再填入
其代码 SHA256、方法、依据和判定字段。代码哈希是身份追溯，不是检测器正确性的证明。

target 方法仅允许 source_instrumentation、branch_coverage、semantic_event；
oracle 方法仅允许 independent_expected、metamorphic、sanitizer、assertion。
eq 为同类型精确比较；gt 为数值阈值比较。oracle 谓词为真表示“异常候选”，不是正常。
不支持将 model_judgment 或 version_difference 当作独立判据。
检测器若不适用、前提不满足或观测不完整，不应提交负值冒充 miss/no_anomaly；
省略相应测量，使其归类为 unobservable/unknown，并在 reason 说明缺口。
对 gt 的计数器必须证明运行完整；未刷新计数不能当作零。

每轮输入形状（省略的候选自动保留未执行；所有路径相对于本文件所在目录）：

~~~json
{
  "run_id": "RUN_ID",
  "round": 1,
  "observations": [{
    "candidate_id": "seed_1",
    "candidate_sha256": "SHA256_OF_CANONICAL_COMPLETE_CANDIDATE",
    "reason": "实际观测或失败、不可观测的原因",
    "execution": {
      "status": "completed",
      "actual_revision": "EXACT_TARGET_SHA",
      "environment": {"version": "ACTUAL_VERSION", "build": "ACTUAL_BUILD", "config": {}},
      "command": ["ACTUAL_RUNNER", "ARGUMENTS"],
      "runner_sha256": "ACTUAL_RUNNER_SHA256",
      "observed_at": "UTC_ISO_TIME",
      "evidence": {"path": "execution.json", "sha256": "FILE_SHA256"}
    },
    "validity": "valid",
    "target": {"contract_id": "target_1", "evidence": {"path": "target.json", "sha256": "FILE_SHA256"}},
    "oracle": {"contract_id": "oracle_1", "evidence": {"path": "oracle.json", "sha256": "FILE_SHA256"}}
  }]
}
~~~

execution.status 为 completed/failed/not_run；validity 为 valid/invalid/unknown。
未执行时不许附加测量。一次异常退出也可能已有有效的分支或 sanitizer 证据，因此
failed 不自动排除观测：执行状态与目标/异常观测分开保存。
execution.evidence 应保存实际执行输入、退出码和日志；runner 必须核对提交的完整
候选（含数据、顺序、会话和配置），不能只执行 SELECT 再宣称已执行完整种子。

target.json / oracle.json 为独立生产者导出的测量封装：

~~~json
{
  "run_id": "RUN_ID", "round": 1,
  "candidate_id": "seed_1", "candidate_sha256": "CANONICAL_CANDIDATE_SHA256",
  "actual_revision": "EXACT_TARGET_SHA", "contract_id": "target_1",
  "producer_sha256": "FROZEN_PRODUCER_CODE_SHA256",
  "method": "branch_coverage", "observed_at": "UTC_ISO_TIME",
  "raw_evidence": [{"path": "trace.txt", "sha256": "RAW_FILE_SHA256"}],
  "measurements": {"target_hit_count": 1}
}
~~~

候选哈希采用 Python canonical JSON：
json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
的 UTF-8 字节 SHA256。完整例子和无网络的生产者模拟见 tests/test_commit_pipeline.py。

导入时逐项核对 run、轮次、候选哈希、精确 revision、契约、producer 身份和原始文件
哈希，然后计算分类。只复制明确引用的证据，保存原字节。下一轮重算这些分类，不信任
可编辑的 hit 标签。相对路径禁止越界。大型原始证据只放 local，不提交 Git。

这些检查验证“所声明观测的完整性和与判据的一致性”，不能证明外部生产者未伪造数据，
也不能替代插桩/覆盖采集的正确性审查。不要把模型生成的 JSON 当测量封装传入。
当前没有真实数据库测量生产者适配器；因此工程测试中的合成 hit 仅为控制流测试。
Bug 状态始终为 not_adjudicated，independent_bug_count 为 null，之后仍需复现与根因复核。

## 模型身份和文件追溯

每次实际生成前 GET /models 验证所请求标识，随后记录原始 catalog、时间和完整请求。
调用 POST /chat/completions，保存原始响应、returned model、provider timestamp、response ID、
usage、请求与响应哈希。returned model 不同或缺失时不接受，不自动切换型号。
供应商未返回具体后端版本时保留未知，不能从别名推断具体训练/部署版本。
/models 可用不等于 completion 已成功，更不等于 SQL 已执行。

官方接口：
- https://api-docs.deepseek.com/api/list-models/
- https://api-docs.deepseek.com/api/create-chat-completion/

目录结构：

~~~text
local/RUN_ID/
  manifest.json, material.json, contracts.json, pipeline_source.py, stage1.txt, stage2.txt
  analysis/request.json, selection.json, attempt.json, models.json, response.json, result.json, analysis.json
  rounds/01..10/
    request.json, selection.json, attempt.json, models.json, response.json, result.json
    candidates.json, observations.json, feedback.json, evidence/
~~~

尚未取得的输出不存在；不是用空成功文件占位。init 不复用现有目录。
运行代码以实际 Git commit、dirty 状态和完整入口脚本快照/哈希共同标识。
提示词、材料与契约冻结。执行代码发生变化需新 run，不在旧 run 内改变含义。

## 验收顺序和当前边界

先审一个 commit 的输入、源码事实与未知信息，再审候选关联、准备/目标操作/预期观测，
最后核对目标检测器和独立 oracle 的证据。合成测试覆盖真实本地 Git diff 提取、
10×10 预算、短批次、引用错误、模型失败、证据绑定、反馈选择和回退。
仓库入口：

    python -X utf8 -B scripts/check_offline.py
    python -X utf8 -B scripts/audit_repository.py

本流程没有启动数据库、确认目标分支、接入变异器或完成四组对照。mutator_status
明确为 not_assessed。完成单案例验收之后，再核对变异器的 seed 导入、语法/数据/
会话/配置能力，保留 capability_gaps；不要将本候选 JSON 直接当作已兼容的 Squirrel 输入。
旧 Codex 探索继续作为前期结果，本流程不会读取其 SQL 充当新生成或真实反馈。
