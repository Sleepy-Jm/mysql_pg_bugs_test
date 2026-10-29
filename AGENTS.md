# 项目约定

主集合为官方 Version 字段明确命中的 MySQL Server 报告 × 版本；历史探索集合单列。保留失败、未执行与未知。reproduced 为报告现象复现，不能称独立根因或新漏洞。新版本须显式扩展 runner 白名单及测试。原始 SQL 字节和旧证据哈希不得悄悄重写。

修改后执行 scripts/check_offline.py 与 scripts/audit_repository.py。默认只做离线工作，不连接服务器或执行数据库。禁止上传凭据、原始大日志、数据库目录、镜像和压缩包。实验必须记录 run_id、实际 commit、输入哈希、环境和命令。
