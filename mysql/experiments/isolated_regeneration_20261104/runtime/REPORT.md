# 隔离生成 SQL：对应提交与直接父提交实测报告

**结果：窗口组稳定复现；Item 组已生成子集未复现；字符集组无 SQL，未执行。** 12 次完整脚本均正常退出，无 SQL 错误、超时或 OOM；各版本三轮解析结果完全一致。

窗口目标 c296cddb93ff 的 WF_BASE、WF_NULLS、WF_REAL_LOW 均连续三轮错误，父提交 74c7ccfa27f4 对应用例连续三轮正确。例如 WF_BASE 的 (p=1,id=7) 预期和父提交为 408，目标为 680；(p=1,id=8) 预期和父提交为 450，目标为 600。WF_NULLS 和 WF_REAL_LOW 的对应两行预期均为 420，目标分别为 1260、630。

WF_UNBOUNDED 保持暂缓判定：父提交 (p=1,id=5) 实际值为 351.428600，冻结预期为 351.428571，确认原精度疑点确实影响比较。目标还出现更大差异，但本轮不将整个暂缓用例计入正式复现数，不回写冻结 oracle。

执行 ID：`mysql-isolated-regeneration-20261104-b`；生成 ID：`mysql_three_isolated_regeneration_20261104`。

执行时间（UTC）：2026-11-04T11:17:02.460281+00:00 至 2026-11-04T11:18:28.187117+00:00。

本次只执行对话 B 的冻结输出。未使用历史成功 SQL 补齐缺失用例，也未根据实测修改 SQL 或预期结果。字符集组没有生成 SQL，保持 blocked。

## 执行与判定方法

- 两个可执行组，每组目标提交和直接父提交各三轮，共 12 次完整脚本；每轮独立连接和数据库，脚本在同一连接内顺序执行，遇 SQL 错误停止。
- Docker 固定镜像、无网络、独立数据目录；核对完整 SHA、直接父关系、构建清单的无补丁记录、mysql/mysqld/mysqladmin 二进制哈希。复用构建缓存，未重新编译或做源码分支插桩。
- 原始 SQL 前附加会话元数据查询，记录 version、version_comment、sql_mode、div_precision_increment、windowing_use_high_precision；原始文件和实际提交脚本均记录哈希。
- XML 结果按冻结 case 顺序映射，检查结果集数量和列名；精确数值比较允许显示小数位不同；NULL 精确比较；DOUBLE 平均值按预先冻结的绝对/相对容差比较。
- WF_UNBOUNDED 按运行前审查策略保留 oracle_hold，差异不计作已确认缺陷。
- 执行后复核 34 个冻结文件的 SHA-256，全部未变。

## 每版本结果

| 组 / 版本 | 完整提交 | 完整脚本运行 | 用例判定（每轮） |
|---|---|---|---|
| item_property_recalculation_248c7f7c227e / parent | `15980860ac2639f41dfbda2f7fffb7aeeab32921` | 3/3 完成 | {'pass': 4} |
| item_property_recalculation_248c7f7c227e / target | `248c7f7c227e76f3422378ca3b9e10d141dcfc86` | 3/3 完成 | {'pass': 4} |
| window_frame_state_c296cddb93ff / parent | `74c7ccfa27f482576412300e5f92fd3dbeb54cfa` | 3/3 完成 | {'pass': 7, 'oracle_hold': 1} |
| window_frame_state_c296cddb93ff / target | `c296cddb93ffc631f9b43d3b1ff769604e7469d7` | 3/3 完成 | {'mismatch': 3, 'pass': 4, 'oracle_hold': 1} |

## 逐用例证据

### item_property_recalculation_248c7f7c227e

会话设置：`{"version": "8.0.33", "version_comment": "Source distribution", "sql_mode": "ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION", "div_precision_increment": "4", "windowing_use_high_precision": "1"}`。

- **IP_BASE**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **IP_WRAP**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **IP_REF**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **IP_EMPTY_BASE**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。

### window_frame_state_c296cddb93ff

会话设置：`{"version": "8.0.32", "version_comment": "Source distribution", "sql_mode": "ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION", "div_precision_increment": "4", "windowing_use_high_precision": "1"}`。

- **WF_BASE**：mismatch；目标相对冻结预期 2 处差异；目标与父提交 2 行显示值不同。
  - {"row": 6, "column": "a", "actual": "680.000000", "expected": "408.000000"}
  - {"row": 7, "column": "a", "actual": "600.000000", "expected": "450.000000"}
- **WF_CURRENT**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **WF_UNBOUNDED**：oracle_hold；目标相对冻结预期 5 处差异；目标与父提交 5 行显示值不同。
  - {"row": 3, "column": "a", "actual": "880.000000", "expected": "330.000000"}
  - {"row": 4, "column": "a", "actual": "820.000000", "expected": "351.428571"}
  - {"row": 5, "column": "a", "actual": "780.000000", "expected": "390.000000"}
  - {"row": 6, "column": "a", "actual": "680.000000", "expected": "408.000000"}
  - {"row": 7, "column": "a", "actual": "600.000000", "expected": "450.000000"}
- **WF_CUMULATIVE**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **WF_NULLS**：mismatch；目标相对冻结预期 2 处差异；目标与父提交 2 行显示值不同。
  - {"row": 6, "column": "a", "actual": "1260.000000", "expected": "420.000000"}
  - {"row": 7, "column": "a", "actual": "630.000000", "expected": "420.000000"}
- **WF_EMPTY**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。
- **WF_REAL_LOW**：mismatch；目标相对冻结预期 2 处差异；目标与父提交 2 行显示值不同。
  - {"row": 6, "column": "a", "actual": "1260", "expected": 420}
  - {"row": 7, "column": "a", "actual": "630", "expected": 420}
- **WF_REAL_HIGH**：pass；目标相对冻结预期 0 处差异；目标与父提交 0 行显示值不同。

## 结论边界与材料对应

- 字符集组：没有 SQL，未执行，不能判定已复现或未复现。
- Item 组：只有窗口基础、包装、引用和空帧子集；缺少已被 B 标为 blocked 的 IN 转换等候选。当前生成子集通过不等于已覆盖原缺陷路径。
- 窗口组：以冻结 oracle 的已批准用例判定；精度 hold 独立列出。实际分支覆盖未插桩，不能仅凭结果断言到达某个源码分支。
- 本轮是已知三个目标的隔离上下文重复生成，不是未知缺陷发现实验。运行阶段获得的答案应与后续独立生成阶段隔离。
- `inputs/<组>/test.sql`、`expected.json`、`requirement_mapping.json` 对应冻结 B 输出；`runtime_plan.json` 关联完整提交和候选状态。
- 上游 A/B 文件仍位于实验根目录的 `stage1_src2req/<组>/outputs/attempt_001` 和 `stage2_req2test/<组>/outputs/attempt_001`；可通过 requirement_mapping 和 coordinator 冻结清单追溯。
- `results/<短SHA>/trial_N/stdout.xml`、`stderr.txt`、`parsed.json`、`comparison.json`、`submitted.sql` 保存原始输出、解析、判定和实际输入；`results/builds` 保存构建和共享库哈希。
- `revision_comparison.json` 保存首轮逐行跨版本对比；三轮一致性已检查。

## 环境修复与归档

首次启动目录 mysql-isolated-regeneration-20261104-a 因缺少 libprotobuf-lite.so.3.19.4 在执行 SQL 前失败，记录保留。正式执行使用独立的 -b 目录，将原构建目录中的共享库只读挂载到 /deps，并设置 LD_LIBRARY_PATH；库文件哈希已记录。该修复未修改 MySQL 二进制或冻结 SQL。

正式运行的四个容器均在结束后停止并移除；数据目录和服务日志留在远端独立实验目录。共享库来自现有构建目录，没有逐提交重新构建这些库，具体路径与哈希在 builds 记录中，属于环境溯源限制。
