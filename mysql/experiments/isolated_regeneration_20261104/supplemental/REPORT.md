# 有答案知识的补充执行报告

本轮响应“把未执行的完成执行”：补齐字符集主候选和 Item IN 主候选。使用历史成功案例知识，不能计为原始隔离生成成功。原始 A/B 文件未修改。可选存储函数及 FIRST/LAST/NTH 扩展不在本轮主案例补齐范围。

执行 ID：`mysql-supplemental-assisted-20261104`；UTC：2026-11-04T11:26:16.807844+00:00 至 2026-11-04T11:27:27.197212+00:00。

| SQL 组 | 父提交通过数（每轮） | 目标提交通过数（每轮） | 复现异常 |
|---|---:|---:|---|
| 字符集 4d2da251cb53 | 6/6 | 5/6 | SC_IMPLICIT_ON 应返回两行，实际空集 |
| Item 属性 248c7f7c227e | 6/6 | 3/6 | SI_REPEAT / SI_NO_NULL / SI_EMPTY 的 wrapped 错误 |

## 执行与预期

两个目标及直接父提交各三轮，共12次完整脚本。每轮独立数据库和连接，预处理语句的多次 EXECUTE 在同一连接内完成。固定容器镜像、无网络、缓存二进制 SHA 与清单验证、共享库只读挂载；详见 results/builds、launch.json 和 summary.json。全部正常退出，实例无 OOM，结果各轮完全一致。

字符集独立预期：id=1、4，aé 的 UTF-8 HEX 为61C3A9、字符数2、字节数3；ASCII ax 为6178、2字符/2字节。Item 沿用 B 数据，窗口 SUM 后加1为 [8,17,29,18,4,NULL]；右集合 [8,29,NULL] 时 IN 为 [1,NULL,1,NULL,NULL,NULL]，删除 NULL 后为 [1,0,1,0,0,NULL]，空集合时全为0。预期在运行前保存，未用运行输出调整。

## 具体错误

### derived_condition_charset_4d2da251cb53

目标 `4d2da251cb536340d19438cc0039bb2846f9a634`。

- SC_IMPLICIT_OFF: pass。
- SC_IMPLICIT_ON: mismatch。
  - {"kind": "row_count", "actual": 0, "expected": 2}
- SC_EXPLICIT_OFF: pass。
- SC_EXPLICIT_ON: pass。
- SC_ASCII_OFF: pass。
- SC_ASCII_ON: pass。
### item_property_recalculation_248c7f7c227e

目标 `248c7f7c227e76f3422378ca3b9e10d141dcfc86`。

- SI_FIRST: pass。
- SI_REPEAT: mismatch。
  - {"row": 0, "column": "wrapped", "actual": null, "expected": 8}
  - {"row": 1, "column": "wrapped", "actual": "3", "expected": 17}
  - {"row": 2, "column": "wrapped", "actual": "10", "expected": 29}
  - {"row": 3, "column": "wrapped", "actual": "24", "expected": 18}
  - {"row": 4, "column": "wrapped", "actual": "47", "expected": 4}
  - {"row": 5, "column": "wrapped", "actual": "39", "expected": null}
- SI_DIRECT: pass。
- SI_NO_NULL: mismatch。
  - {"row": 0, "column": "wrapped", "actual": null, "expected": 8}
  - {"row": 1, "column": "wrapped", "actual": "3", "expected": 17}
  - {"row": 2, "column": "wrapped", "actual": "10", "expected": 29}
  - {"row": 3, "column": "wrapped", "actual": "24", "expected": 18}
  - {"row": 4, "column": "wrapped", "actual": "47", "expected": 4}
  - {"row": 5, "column": "wrapped", "actual": "39", "expected": null}
- SI_EMPTY: mismatch。
  - {"row": 0, "column": "wrapped", "actual": null, "expected": 8}
  - {"row": 1, "column": "wrapped", "actual": "3", "expected": 17}
  - {"row": 2, "column": "wrapped", "actual": "10", "expected": 29}
  - {"row": 3, "column": "wrapped", "actual": "24", "expected": 18}
  - {"row": 4, "column": "wrapped", "actual": "47", "expected": 4}
  - {"row": 5, "column": "wrapped", "actual": "39", "expected": null}
- SI_EMPTY_DIRECT: pass。

行号 row 为0起始。Item 的错误集中于 wrapped，IN 值仍符合冻结预期；不能把它写成 IN 三值逻辑算错。父提交均与独立预期一致。源码解释见 [上级文档](../source_mechanisms.md)。

## 追溯

- `provenance.json` 明确历史案例知识来源；`runtime_plan.json` 记录完整提交、输入哈希和 case 顺序。
- `inputs/<组>/requirement_mapping.json` 关联原始 A 条件，并明确 PREPARE 重复执行属于协调者补充。
- `inputs/<组>/test.sql` 与 expected.json 是本次新输入，不覆盖原始 B 的 blocked 或已有SQL。
- `results/<短SHA>/trial_N/` 保存 submitted.sql、stdout.xml、stderr.txt、parsed.json、comparison.json；所有实验容器已停止并移除。
- 此为无分支插桩的输出复现。共享库来自现有构建目录，哈希记录但未逐提交重编；与原始运行相同的溯源限制适用。
