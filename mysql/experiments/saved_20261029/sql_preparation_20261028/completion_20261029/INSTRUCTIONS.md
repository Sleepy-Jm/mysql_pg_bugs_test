# 2026-10-29 继续整理：仅静态工作

先读取上级 PREPARATION_CONTRACT.md。以本文件和用户本轮要求为最新约定；现有 174 份 case 与 SQL 均不覆盖，必要更正以本目录单独审查记录表示。分片 1 的 119 份全部保留。

剩余清单 remaining_0/1/2.json，共 183 份。每份逐一阅读 inputs/<id>.json/.txt 的原文、评论及 test_spec。没有原始数据/附件/关键步骤时不要编造。可把文字中明确定义的建表/数值转写为 SQL，但须注明来源。仅自动抽取不等于语义核对。一次可以处理若干份，但不能因数量多省略检查。

在 cases/<id>/ 新建记录。除旧约定字段外，增加：

```
"preparation_assessment": {
  "sql_completeness": "complete | partial | unavailable",
  "oracle_sufficiency": "sufficient | uncertain | unavailable",
  "runtime_verification": "not_executed"
},
"execution_conditions": [
  {"kind": "debug_build | plugin | multi_connection | restart | heavy_resource | file_access | privilege_change | global_configuration | platform | other", "detail": "具体条件与来源", "requires_review": true}
],
"uncertainties": [
  {"point": "具体不确定点", "evidence": "锚点和原文依据", "needed": "还需材料或后续决策"}
],
"safety_review": {"required": false, "reasons": [], "restriction": null}
```

旧四种状态仍可用，新增 needs_safety_review 和 blocked_tool_restriction。SQL 完整但涉及文件访问、权限变化等影响的用例单列安全待审；保留真实目的和操作说明，不把敏感步骤改名掩盖，不为避开限制改写。环境条件与 SQL/判定完整性分开，debug 条件本身不等于 SQL 缺失。

不运行任何数据库、客户端、容器或服务器操作；不安装组件，不连接网络服务。只读已有文件，写准备材料和静态验证结果。如某个报告确实受工具限制，记录报告编号、失败步骤和原提示，并继续不受影响的静态资料整理；不要改写/改名绕过限制。此前分片整体失败没有报告定位，不能编造某个报告是原因。

每个分片保存 completion_20261029/worker_<n>_review.json，含逐报告结论、来源锚点、SQL 文件映射和本轮新限制（如有）。不要覆盖别人的分片或共享汇总文件。辅助代码仅用 worker_<n> 前缀，不执行以前的批量生成脚本以免覆盖既有产物。
