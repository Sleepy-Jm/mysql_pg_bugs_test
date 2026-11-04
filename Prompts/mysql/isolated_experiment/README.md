# 独立新对话实验启动包

本包用于启动两个分开的 MySQL 生成阶段：**完整示例 → 当前源码 → 需求**，以及 **完整示例 → 冻结需求 → SQL/预期**。这里只提供协议和空白模板，没有选定新目标、填写生成答案或运行数据库。

将材料复制到仓库之外的独立工作目录，由协调者准备输入、冻结文件和搬运交接材料。对话 A 只使用阶段一目录，对话 B 只使用阶段二目录。不要把整个仓库、本 README、当前历史对话、污染审查或后验解释一起交给生成对话。

## 文件入口

| 文件 | 使用者与用途 |
|---|---|
| [src2req_start.txt](src2req_start.txt) | 填完占位符后，完整粘贴给新对话 A；同时保存到阶段一根目录 |
| [req2test_start.txt](req2test_start.txt) | 填完占位符后，完整粘贴给新对话 B；同时保存到阶段二根目录 |
| [stage1.allowlist.template.json](templates/stage1.allowlist.template.json) | 阶段一文件级读取白名单，复制为 `allowlist.json` |
| [stage2.allowlist.template.json](templates/stage2.allowlist.template.json) | 阶段二文件级读取白名单，复制为 `allowlist.json` |
| [source_manifest.template.json](templates/source_manifest.template.json) | 目标源码的提交、位置、哈希与选择方式，复制为 `inputs/source_manifest.json` |
| [handoff.template.json](templates/handoff.template.json) | 阶段一完成后由协调者填写，复制为阶段二的 `inputs/handoff.json` |
| [experiment.template.json](templates/experiment.template.json) | 协调者记录选题、示例暴露、阶段上下文和实验范围；不提供给生成阶段 |
| [freeze.template.json](templates/freeze.template.json) | 协调者分别冻结各阶段输入和输出；一份清单对应一个时点，不回写旧记录 |

模板白名单是操作约定，**不是操作系统访问控制或自动验证程序**。需要由协调者实际限制每个阶段的文件/连接器访问，并检查日志。仅更改当前工作目录不会自动禁止读取父目录或其他目录。平台自动附带的项目文件、历史内容和其他不可控上下文也要记录；存在暴露时不再称为清洁尝试。

## 独立实验目录结构

建议创建三个独立工作目录；以下公共父目录只是协调者便于管理的组织方式，不作为两个生成对话的工作区。示例根路径可使用 `C:/mysql-isolated/run_001`，按实际可写位置调整。

```text
run_001/
├── coordinator/                         # 不给两个生成对话访问
│   ├── experiment.json
│   ├── selection_and_overlap_review.md
│   ├── commands.log
│   ├── freezes/
│   │   ├── stage1_attempt_001_inputs.json
│   │   ├── stage1_attempt_001_outputs.json
│   │   ├── stage2_attempt_001_inputs.json
│   │   └── stage2_attempt_001_outputs.json
│   ├── context_logs/                    # 完整消息/可取得的工具记录
│   └── runtime/                         # 两阶段完成并冻结后才存实测
├── stage1_src2req/                       # 对话 A 的唯一实验工作目录
│   ├── src2req_start.txt
│   ├── allowlist.json
│   ├── inputs/
│   │   ├── example_src2req.txt           # 选中的完整异目标示例
│   │   ├── source_excerpt.txt           # 当前目标源码；可以显式增加多份
│   │   └── source_manifest.json
│   └── outputs/attempt_001/
│       ├── requirements.txt
│       ├── source_evidence.md
│       ├── stage1_audit.json
│       └── stage1_response.txt
└── stage2_req2test/                      # 对话 B 的唯一实验工作目录
    ├── req2test_start.txt
    ├── allowlist.json
    ├── inputs/
    │   ├── example_req2test.txt          # 同一开发样例的另一阶段
    │   ├── requirements.txt             # 阶段一输出的逐字节副本
    │   └── handoff.json
    └── outputs/attempt_001/
        ├── test.sql
        ├── expected.json
        ├── oracle.md
        ├── requirement_mapping.json
        ├── stage2_response.txt
        └── generation_manifest.json
```

输出文件由对应阶段生成，不预先放置答案；blocked 时保留原因和审计，不创建伪完整 SQL。`attempt_001` 是初次尝试名，不要求两个阶段以后重试次数相同；交接清单明确记录 from/to attempt。

协调者可先用 PowerShell 建立空目录（将 `$prepRoot` 改为实际可写、尚未使用的位置；不删除或覆盖已有实验）：

```powershell
$prepRoot = 'C:/mysql-isolated/run_001'
$prepDirs = @(
  "$prepRoot/coordinator/freezes",
  "$prepRoot/coordinator/context_logs",
  "$prepRoot/coordinator/runtime",
  "$prepRoot/stage1_src2req/inputs",
  "$prepRoot/stage1_src2req/outputs/attempt_001",
  "$prepRoot/stage2_req2test/inputs",
  "$prepRoot/stage2_req2test/outputs/attempt_001"
)
New-Item -ItemType Directory -Path $prepDirs
```

再按上表复制启动提示词和 JSON 模板并重命名；不要把 `templates/` 整个复制给某个阶段。输出目录不得包含先前尝试内容。

## 填写与冻结顺序

### 1. 协调者选题并准备完整示例

填写 `experiment.json`：experiment_id 标识实验，run_id 标识本次执行链，attempt_id 标识阶段尝试；协议提交为本启动包实际采用的仓库 commit，MySQL 提交另填完整 SHA。生成前确定运行重复次数、比较范围和环境约束，保留失败及 blocked 候选。

从 [开发样例库](../../../examples/mysql/source_guided_reproductions/README.md) 选择一对示例，分别逐字节复制为两个阶段的 `example_src2req.txt`、`example_req2test.txt`，保留其完整输入和完整答案。不要复制样例库 README、运行报告或机制解释给生成阶段。样例中保留“生成时尚未执行”的历史状态不影响格式教学。

选择未暴露的新目标。示例目标、相关修复、父子提交和语义等价触发构造不能当作独立留出目标；仅换常数或表名不构成新的独立目标。重做历史三组应标为 `isolated_regeneration`，不能写为未知缺陷发现。协调者在 `selection_and_overlap_review.md` 记录筛选和已知答案参与程度，不把它传给生成阶段。未完成审查时，`eligible_for_held_out_evaluation` 保持 false。

### 2. 填写阶段一输入，最后填写白名单

准备固定目标提交的源码节选。保留上游代码、原行号和真实省略范围，不能把人工触发建议、修复解释或回归 SQL混入源码包。如果源码原件本身含答案相关内容，记录实际暴露和实验范围，不能隐瞒后仍称无污染。不要用包中已有种子需求替代源码。

所有 `{{...}}` 都必须替换。Windows JSON 路径建议用正斜杠绝对路径，例如 `C:/mysql-isolated/run_001/stage1_src2req`，不要写相对路径或目录通配符。`START_LINE_INTEGER`、`END_LINE_INTEGER` 和重复次数最终写为 JSON 整数，去掉字符串引号；提交 SHA 为完整值，文件 SHA256 为 64 位十六进制。无法取得的模型配置等可写 `unknown`，输入哈希不能用 unknown 绕过核验。

顺序为：源码/示例文件 → source_manifest.json → allowlist.json → 已填好的 src2req_start.txt → 协调者输入冻结清单。先算源码哈希，再填来源清单；来源清单最终保存后再算其哈希填入白名单。白名单与启动提示词的最终哈希在协调者冻结清单中记录，避免自身哈希循环。

一份节选可有多个上游代码块，在 `sections` 中逐项记录；多份源码输入则同时增加 `sources` 和白名单的 `current_source` 条目，使用准确文件路径，不扩大为整个目录。来源选择方式只描述选取过程，不透露具体错误答案；详细选题依据留在协调者目录。

核算单个文件哈希的命令示例（由协调者填写路径，不递归扫描）：

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath 'C:/mysql-isolated/run_001/stage1_src2req/inputs/source_excerpt.txt'
```

冻结文件保存 UTC 时间、准确路径和实际 SHA256。模板中的 `files` 是待填写的条目示意，不表示只记录一个文件；须列出本次全部控制文件和实际输入/输出，不能只记录 SQL。

### 3. 在新对话 A 使用 src2req_start.txt

只为对话 A 提供阶段一目录访问权限，粘贴已填写的启动提示词，不带旧对话摘要。核验白名单后先完整示例，再当前目标。平台自动上下文若突破边界，保留暴露记录并停止清洁尝试。完成后协调者保存可取得的完整消息及工具记录；仅有阶段最终回答不等于保存了全部上下文。

阶段一输出冻结清单包含 requirements、source_evidence、stage1_audit、stage1_response 的哈希。不要为了结果更好而由协调者悄悄改写需求；必要修改属于新 attempt，并保留旧输出及修改来源。

### 4. 仅搬运需求，填写最小交接清单

把冻结的 `requirements.txt` 逐字节复制到阶段二 `inputs/requirements.txt`，核对两份哈希相同。填写 handoff.json 中的输入路径、需求哈希、实验/run/目标 SHA、来源和目标 attempt 及冻结时间。

`requirements_status` 默认为 `pending_review`，确认有可用需求后改为 `ready`；否则填 `blocked`。`exposure_status` 默认为 `not_reviewed`，审查未发现越界才改为 `no_observed_violation`；观察到越界填 `observed_violation`，记录不完整填 `unknown`。仅 `ready` 和 `no_observed_violation` 同时满足才将布尔字段 `ready` 改为 true。该状态是观测结论，不是对训练记忆或隐藏上下文的绝对保证。

交接清单不能加入源码块、修复信息、历史结果、根因结论或指向阶段一目录的读取授权。只保留已有需求的来源标识和预先声明的环境约束；不能根据已知错误临时增加能“保证触发”的条件。部分候选有未决事项时，需求保留这些事项，阶段二逐项 blocked，不删除失败候选。

阶段二输入冻结顺序为：示例/requirements → handoff.json → allowlist.json → req2test_start.txt → 协调者输入冻结清单。白名单中的需求哈希必须与 handoff 的值相同。不要复制 source_manifest、source_evidence、阶段一完整对话或审计正文。

### 5. 在新对话 B 生成并冻结，之后才运行

只为对话 B 提供阶段二目录访问权限，粘贴已填写的 req2test_start.txt。对话 B 不接收前一对话历史；它只能看到允许的格式示例、冻结需求和最小交接清单。

完成后用新的输出冻结清单记录 SQL、expected.json、oracle、mapping、完整阶段回答、generation_manifest 以及使用的算术核验程序/输出；同步记录消息和命令日志。generation_manifest 不记录自身哈希，其最终哈希由协调者记录。SQL 和 oracle 未冻结前不得先运行数据库再回头修答案。

本包不授权或启动数据库执行。之后的实测单独记录 run_id、实际构建 commit/二进制身份、输入哈希、环境和命令；运行反馈不能覆盖生成快照。反馈后改动使用新 attempt_id，指标中区分首次生成与有反馈迭代。

## 三份目录的可见性

| 材料 | 对话 A | 对话 B | 协调者 |
|---|---|---|---|
| 本阶段启动提示词、白名单 | 本阶段可读 | 本阶段可读 | 可读 |
| 完整开发示例 | 仅 src2req 版 | 仅 req2test 版 | 两版可读 |
| 当前源码与来源清单 | 白名单内可读 | 禁读 | 可读 |
| 冻结需求 | 本阶段输出 | 白名单内可读 | 可读/搬运 |
| 最小交接清单 | 不必提供 | 白名单内可读 | 填写/冻结 |
| 阶段一证据文档和完整对话 | 仅本次生成/可见上下文 | 禁读 | 保存/审查 |
| 当前目标修复、旧 SQL、实测和机制解释 | 禁读 | 禁读 | 按预定选题/执行/事后分析规则记录接触时点 |

本包未提供自动隔离工具，也不声称新对话消除了模型预训练记忆。与本批历史实验的关系见 [污染审查](../../../experiments/prompt_pipeline_20261104/contamination_review.md)；该链接仅供协调者了解背景，不纳入阶段白名单。
