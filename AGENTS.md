# 仓库约定

MySQL 与 PostgreSQL 分别位于 mysql/ 和 pg/；各自作为运行工作目录，统计不得混合。mysql/AGENTS.md 继续适用。保留 SQL、原文和历史证据字节及哈希，失败和未知不得改作有效未复现。禁止上传凭据、大型原始日志、数据库目录、镜像和压缩包。默认离线验证，不自动运行服务器实验。

MySQL：在 mysql/ 执行 scripts/check_offline.py 与 scripts/audit_repository.py。PG：在 pg/ 执行 unittest discover -s tests。上传清单与排除规则见 pg/publication_manifest.json。
