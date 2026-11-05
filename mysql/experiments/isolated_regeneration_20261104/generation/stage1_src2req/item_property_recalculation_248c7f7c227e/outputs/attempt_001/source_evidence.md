# Source evidence

仅供审计，不交阶段 B。selection.method 表示既有目标重复选择，prior_bug_or_fix_knowledge_used=yes。

|编号|源码位置|直接事实|推导边界|
|---|---|---|---|
|R1|sql/item_func.cc:708-719|清空后从普通参数重建属性|调用时机未知|
|R2|sql/item.h:3179-3218,3443-3465|位操作、has_wf、属性范围注释|不能跨子查询套用属性|
|R3|sql/item.h:5747-5755|引用条件递归，保留 rollup 后合并|被引用对象刷新时机未知|
|R4|sql/item_cmpfunc.h:472-504;sql/item_cmpfunc.cc:2138-2153,2173-2193,2410-2419|包装关系、fix 阶段合并、重算及 NULL 分支|SQL 不保证选择该包装|
|R5|sql/item_subselect.cc:2537-2541|基类调用、left_expr 更新、表位合并|基类缺失，禁止据缺省片段推断属性丢失|
|R6|sql/sql_select.cc:4106-4147,4654-4687|临时表和切片，buffering 门槛，has_wf 过滤与重写|需插桩确认源/临时对象对应|
|R7|sql/item_func.cc:8410-8415|重设 stored program 位|独立可选覆盖|

片段中的示意表达式用于解释对象重写，不视为当前目标完整触发答案；未发现明确修复结论或触发复现。没有运行或覆盖证据。
