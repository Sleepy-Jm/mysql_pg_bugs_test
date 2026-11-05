本组全部候选 blocked，未生成 test.sql 或 expected.json。
阻塞来自冻结需求未提供并要求按目标版本验证的可执行前提，不是断言存在缺陷，也不把未测覆盖本身当作 SQL 不合法的证据。
补充材料须由协调者在新 attempt 冻结；本阶段不查源码、网络或阶段一目录代补。
没有固定合法编码/转换配置，无法逐项给出非 ASCII 字符、字节和比较真值，故不伪造独立 oracle。

覆盖观察计划（仅转述需求）
R1：记录下推门槛；R2：记录 derived_table/table_ref、field_index 与克隆对象；R3：记录打印标志、字节、parse_sql 结果；R4/R5：记录 is_cs_specified、collation、缓冲区和解析端字符集，分别确认 introducer 分支。EXPLAIN 仅为线索；未确认可达。

database_executed=false
coverage_status=not_measured
reproduction_status=unknown
