# Commit 分析与候选种子流程 v1

这是独立的新流程。原有 post-change src2req/req2test、Codex 探索、隔离重复生成、
报告主集合和历史 SQL/哈希均保持原样；本流程结果不并入它们的统计。

入口：src/mysql_bugs_test/commit_pipeline.py（Python 标准库）。
新提示词：Prompts/mysql_commit/。没有依赖旧实验的需求、答案或响应。
本次验收是合成案例的工程验证，不是数据库实验或 LLM 效果验证。

## 输入和两个阶段

prepare 从指定的本地 MySQL Git 仓库读取精确 commit、直接父提交、message、
生产文件的完整 diff，以及 before/after/helper 源码行段。不传 --spec 时自动选择
本次修改的 C/C++、头文件和语法文件，排除测试等目录；--spec 可保留显式范围选择，
也可只给 version/commit_role 而省略 sources，继续使用自动选择。
merge commit 必须显式选择直接父提交。不自动 checkout、联网或收集测试答案。
辅助函数也需显式列入白名单；新增/删除文件不存在的一侧留空即可。
diff 的引用行号是保存的 diff 文本行号；before/after 是原源码行号，两者不可混用。

commit_metadata 会自动提供四类信息：

| 信息 | 提取方式与边界 |
|---|---|
| 修改位置 | Git 文件状态和零上下文 diff 的 before/after 行号、行数；属于直接证据 |
| 相关函数 | 根据修改位置定位常见 C/C++ 函数定义；注明 lexical_candidate，不能当成编译器 AST 绑定 |
| 数据库模块 | 根据 MySQL 源码路径给出 module hint，例如 InnoDB、优化器、窗口执行；标为 heuristic |
| 改动类型 | 自动记录文件新增/删除/修改，以及条件、返回表达式、调用/签名、常量等语法提示；语义类型留给 LLM 结合证据判断 |

自动源码上下文以修改区域和包围函数为主，每个片段最多 240 行；超限会记录截断，
保留修改位置附近内容。宏、模板、operator、复杂构造函数等不能可靠定位时保留 unknown。
这不是完整调用图；不凭路径或词法匹配证明执行语义。纯测试/文档提交没有允许的生产
源码时，prepare 明确报无生产源码，不生成虚构的 SQL 材料。

configs/commit_pipeline_sources.example.json 是待填写的输入示例。版本和提交角色
由筛选材料提供，不从文件日期推测，证据不足时填 unknown。函数名同样可填 unknown。
所有源码片段保存其 revision、路径、起始行和内容哈希。所选 commit 如果是修复提交，
必须标 fix，不能将该运行解释为仅凭引入提交的盲生成。

第一阶段输出增加顶层 commit_status，限定三类：introduce（引入）、fix（修复）、
unknown（未知），并以 commit_status_reason 保存判断依据或未知原因。这里的引入/修复
针对目标缺陷或异常行为，不能仅凭增加代码或功能判为引入。证据不足、冲突，或同一
提交混合引入与修复而无法给出明确目标级判断时，标 unknown。输入 commit_role 保留为
筛选来源记录；输出状态是分析判断，不代表缺陷已经实测确认。该标识随分析交给第二阶段。

第一阶段 JSON 的 changes 按不同语义变化拆分，保存版本、父/目标 SHA、改动类型、
模块、位置/函数、facts、affected_features、conditions 和 unknowns。
facts 和 source_supported 条件必须引用 supplied source_id、闭区间行号及逐字 quote。
hypothesis/unknown 可无引用，但不得改称源码事实。程序核查引用文本，不自动证明
自然语言解释正确；semantic_accuracy 始终为 not_evaluated，仍需源码语义审查。
not_sql 或没有可映射条件的分析单独保存，第二阶段记未运行，不强制凑 SQL。

## 材料不足与源码补充

第一阶段必填 material_status：sufficient / partial / insufficient。
sufficient 指足以构造有用的候选，不是已经证明触发；此时 missing_materials 为空。
partial 或 insufficient 时必须给出 missing_materials，包含 request_id、needed、reason、
kind、revision，以及可定位的 path/symbol 或 start_line/end_line：

- definition：补函数/辅助函数定义，symbol 必填，path 可选。
- callers：查找调用位置及包围函数，symbol 必填；结果只是词法调用候选。
- source_range：按路径和闭区间行号补源码。
- unknown：目前不能用源码定位的配置、运行条件或其他缺口，保留 unresolved。

revision 只能是 before、after、both，对应原冻结父提交和目标提交，不能写 HEAD、
后续版本或任意修复 SHA。补充不读取已知复现、回归测试、旧实验答案。
insufficient 时 step 返回 awaiting_source_material，不发起第二阶段生成。
partial 仍允许生成带未知项的假设候选，但可以先执行补充以减少缺口。

从已完成第一阶段的 run 自动读取请求并补源码（不调用模型、不执行数据库）：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py supplement --run local/RUN_ID --repository MYSQL_SOURCE_REPO --output local/enriched_material.json

程序从原 revision 搜索所需定义/调用位置并读取实际源码，逐项记录命中位置、
source_id、哈希、缺口及来源请求。每次补充最多 1600 行、12 个新片段，每片段最多
400 行；超限、多个候选、源码不存在或符号无法解析均保留说明。已提供的范围不重复
添加。supplied_for_reanalysis 仅表示提供了可供重读的源码，不等于问题已解决。

使用新材料建立新 run，再执行第一阶段；补充不改写旧输入、需求或响应：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py init --material local/enriched_material.json --run local/RUN_ID_context2 --run-id RUN_ID_context2
    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py step --run local/RUN_ID_context2 --execute-model

若有检测器契约，init 时重新传入原契约文件。新材料保存 parent_run_id、原材料哈希、
分析输出哈希、补充请求和新增片段。是否充分由重新分析决定；没有新源码或仍有缺口时
如实保留，不循环调用模型来凑出“充分”。没有具体待补充 run 时，不声称已经补过真实案例。

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

以下命令在本仓库根目录执行。选定已有的 MySQL 源码仓库和 SHA；spec 可选。
示例中的 MYSQL_SOURCE_REPO、TARGET_SHA、RUN_ID 需要换成真实值。Windows 如 python
不可用，请改用已安装解释器的绝对路径。

1. 只准备输入，不调用模型：

    python -X utf8 -B src/mysql_bugs_test/commit_pipeline.py prepare --repository MYSQL_SOURCE_REPO --commit TARGET_SHA --output local/material.json

   若需提供版本/角色或指定源码范围，再加 --spec local/sources.json。

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
  manifest.json, material.json, contracts.json, pipeline_source.py, context_source.py, stage1.txt, stage2.txt
  analysis/request.json, selection.json, attempt.json, models.json, response.json, result.json, analysis.json
  rounds/01..10/
    request.json, selection.json, attempt.json, models.json, response.json, result.json
    candidates.json, observations.json, feedback.json, evidence/
~~~

尚未取得的输出不存在；不是用空成功文件占位。init 不复用现有目录。
运行代码以实际 Git commit、dirty 状态和入口脚本、源码上下文模块的快照/哈希共同标识。
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
