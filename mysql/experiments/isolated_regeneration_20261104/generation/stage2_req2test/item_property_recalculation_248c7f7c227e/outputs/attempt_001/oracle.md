单连接，已选择可丢弃 schema；临时表名必须空闲。要求目标构建支持给出的窗口语法；这是执行前提，并未在数据库验证。没有修改会话设置，不需要 PREPARE 或重执行。

独立计算
p=1 按 id 为 [2,5,11,17]；p=2 为 [3,NULL]。键 (p,id) 唯一，全部输入行各出现一次。
IP_BASE 的 [当前,后一行] 帧依次为 {1,2},{2,3},{3,4},{4} 及 {1,2},{2}。忽略 NULL 求和得到 7,16,28,17,3,NULL。
IP_WRAP 对这些数学和加 1，得到 8,17,29,18,4,NULL；NULL+1 仍 NULL。
IP_REF 按 calc 降序，NULL 在最后，再以 p,id 破同分：29,18,17,8,4,NULL，对应 (1,3),(1,4),(1,2),(1,1),(2,1),(2,2)。别名排序不改变每行窗口值。
IP_EMPTY_BASE 的帧只有后一行：p=1 为 {2},{3},{4},{}；p=2 为 {2},{}。结果为 5,11,17,NULL,NULL,NULL；非空全 NULL 帧和空帧的 SUM 都为 NULL。
整数和很小，没有精度损失、字符集或近似容差。JSON null 表示 SQL NULL；比较数值和行重数，不强制客户端 DECIMAL 文本格式。以上由行枚举计算，直接窗口对照不是唯一 oracle。

覆盖观察计划（只用冻结需求）
R1/R2：记录普通函数 update_used_tables 调用前后属性位、参数与 used_tables；包含算术函数不证明调用过重算。
R3：对 IP_REF 确认 Item_ref 身份、ref_item、depended_from，区分相关/非相关分支，别名不是对象类型证据。
R6：记录 needs_buffering、引用切片、source_fields/orig_fields 与临时字段映射，两处 has_wf 消费点的身份和动作。FOLLOWING 帧是缓冲候选，不保证最终路径。
R4/R5 的 IN 对象和 R7 的存储程序支线未生成，不声称覆盖。EXPLAIN 仅为线索；本阶段所有实际分支可达性未确认。

执行：database_executed=false；coverage_status=not_measured；reproduction_status=unknown。
