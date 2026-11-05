# DeepSeek 重跑：三组 MySQL 提交差异测试（2026-11-05）

本目录归档三组源码到测试的两阶段 DeepSeek 重跑及父提交/目标提交服务器验证，与 2026-11-04 实验分开保存，未覆盖已有文件。

- 阶段一请求模型：DeepSeek V4 Pro；阶段二请求模型：DeepSeek V4 Flash。接口返回阶段二模型名为 deepseek-flash；没有独立确认两个名称的版本别名关系。
- 参数：temperature 0.7、max_tokens 16384、thinking disabled；三组独立运行，没有共享对话历史。
- 每份 SQL 在对应父提交和目标提交上各运行三轮，共 18 次完整脚本执行、9 组逐轮比较。
- 三组均成功执行，XML 可解析，无 SQL 错误；9 组均为 no_observed_difference。
- 未做源码分支插桩，不能确认生成 SQL 是否触及目标修改路径。SQL 与原实验的关键触发构造存在差异，详见 verification_report.md。

目录包含原输入包、阶段请求/响应与生成 SQL、服务器客户端 XML/stderr、结果摘要、脱敏后的运行清单和导出哈希清单。服务器容器日志、远端传输元数据、远端执行脚本及只涉及启动失败的初次运行未公开；相对文件名和 SHA256 记录于 export_manifest.json。

输入材料来自记录中的提交 00fcb55c1b43140835bcd65d4c7349532ed1fda3；WhiteFox 模板固定于参考提交 fadce4b16df62f362662754ee8e9745b478a643c。公开副本未改动生成 SQL、模型请求/响应和逐轮客户端输出。

离线复核：python -X utf8 -B verify_export.py
