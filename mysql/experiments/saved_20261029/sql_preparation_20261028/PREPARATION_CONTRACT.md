# 本轮 SQL 准备约定

范围冻结为 selected_tasks.json 的 1,109 个报告×版本项、357 份报告。本轮不运行数据库，不把脚本准备视为复现或独立 bug 证据。原始报告在 inputs/<id>.json/.txt；JSON 包含完整历史评论及各版本已保存的 test_spec。

## 每份报告的交付

在 cases/<id>/ 下写 case.json，必要 SQL 和说明。只修改本人 assignment 文件列出的目录。case.json 必须包含：

```
{
  "report_id": "123",
  "title": "...",
  "source_sha256": "从 inputs JSON 复制",
  "source_anchors": ["cmain"],
  "target_versions": ["8.0.32"],
  "status": "prepared_static | blocked_source_gap | blocked_environment | blocked_semantics",
  "execution_status": "not_executed",
  "scripts": [{"path": "reproducer.sql", "role": "reproducer"}, {"path": "cleanup.sql", "role": "cleanup"}],
  "checks": {
    "schema": {"status": "complete | not_needed | blocked", "detail": "具体对象与来源"},
    "data": {"status": "complete | not_needed | blocked", "detail": "完整 INSERT / 明确可重建的数据；无须表时说明"},
    "sequence": {"status": "complete | blocked", "detail": "mysql 客户端选项、delimiter、事务、是否须 --force 等"},
    "oracle": {"status": "complete | blocked", "detail": "具体预期值、关系或错误/连接存活约束；不能笼统抄写"},
    "cleanup": {"status": "complete | not_needed | blocked", "detail": "精确清理对象，或必须销毁一次性实例及原因"}
  },
  "oracle": {"kind": "wrong_result | error_difference | crash | plan_diff | ...", "expected": "...", "failure": "...", "limitations": "..."},
  "requirements": ["..."],
  "transformations": ["逐项记载人工补齐/格式转换；保留导致问题的错误语句"],
  "blockers": ["阻塞时写可操作、基于具体原文的缺口"],
  "version_notes": {"8.0.32": "适用性/特殊参数；不是本地验证"},
  "source_reading": "核对过的原文锚点、相关补充评论及局限"
}
```

prepared_static 仅指已完成静态人工核对、可交给后续隔离回放，不表示已执行。其五项 checks 不得 blocked；必须有 SQL 与具体 oracle。原文证据不足不能编造完整性。各版本 test_spec 若不同必须保留 version_notes 或分别输出变体。

## SQL 要求

- mysql 命令行可用；明确是否需 --force、DELIMITER、二进制字符集/SQL mode。不得把提示符、结果表、MTR 指令或自然语言当 SQL。
- 建表、数据、触发语句必须齐全并按原序；可以根据文字描述重建合理 schema/data，但须逐项记载 inferred/synthesized，不能称其为原始完整用例。无法忠实还原则阻塞。
- 按报告绑定源锚点；SQL 开头注释来源和静态准备状态。不同版本/修正版/负对照不要混成一个原始用例。故意错误语句必须保留，正常 SQL 错误本身不是 crash bug。
- 默认由未来 runner 分配全新隔离 schema 并选中它，SQL 内写对象；如必须固定库名/系统库/global变量/账号/插件/文件/服务重启，必须声明 disposable_instance 环境并明确恢复或销毁实例。不要触碰现有库。只准备文件，本轮不执行。
- cleanup.sql 使用本用例精确对象名的 DROP ... IF EXISTS；实例级影响只允许在一次性实例运行并销毁实例。不使用无边界通配删除。涉及函数、过程、事件、视图、临时表要完整清理。
- 来源只有附件而附件缺失、没有关键建表/数据/动作、触发依赖明确并发/复制/升级等，标记具体阻塞；已有可核对部分仍保存为 annotated draft，不标可执行。
- 不用脚本批量猜测 SQL 就宣称逐份审核完成。自动提取只用于辅助，必须查看来源并逐例作语义决定。
