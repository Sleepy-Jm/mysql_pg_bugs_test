# Source evidence

仅由本轮白名单节选支持，不交阶段 B。源码选择 method 为重复既有三目标，prior_bug_or_fix_knowledge_used=yes。

|编号|位置|直接事实|推导及边界|
|---|---|---|---|
|R1|sql/sql_derived.cc:976-985|资格函数包含五组布尔门槛|满足它们不证明调用或下推|
|R2|sql/item.cc:1042-1056|比较表引用，相等时按 field_index 克隆派生表达式|外层过滤只是可达候选|
|R3|sql/sql_derived.cc:550-575,617-635,734-745|打印标志、parse_sql、字段信息复制与 resolve|中间代码缺失，不能假定解析环境|
|R4|sql/item.cc:3428-3440,3464-3472|introducer 判定及两条转换目标路径|需要观察实际标志和属性|
|R5|include/sql_string.h:629-639;sql/sql_derived.cc:564|默认缓冲区二进制字符集构造|不等于客户端字符集，不能由注释替代观察|

没有运行证据。注释说明当前实现用途，未见触发 SQL、明确修复结论或当前目标完整答案；不使用既有缺陷记忆作为证据。
