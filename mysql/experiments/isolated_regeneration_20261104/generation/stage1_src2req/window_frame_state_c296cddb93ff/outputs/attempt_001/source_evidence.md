# Source evidence

仅供审计，不交阶段 B。人工重复选择既有三目标，prior_bug_or_fix_knowledge_used=yes。未用前组源码作本组证据。

|编号|源码位置|直接事实|推导边界|
|---|---|---|---|
|R1|sql/window.h:477-490,1299-1311|访问行、输出行及帧位置区别；setter|中间位置不自动等于最终帧大小|
|R2|sql/item_sum.cc:410-426|needs_buffer 局部规则和 DISTINCT 限制|汇总逻辑缺失|
|R3|sql/iterators/window_iterators.cc:683-699,1084-1107|策略互斥，primed 分支及移除/新增条件|完整执行可达性未证|
|R4|同文件:789-820|lower_limit 各边界计算|upper 计算缺失|
|R5|同文件:1145-1165|inverse 移除，!new_last_row 的位置及 last 设置|不能据单行赋值断言结果异常|
|R6|同文件:1167-1226|one-row 路径与新末行添加路径的状态设置|调用分类需确认|
|R7|sql/item_sum.cc:2279-2365|AVG 除数与 decimal 计数更新|SUM/init/实际调用次序缺失|
|R8|sql/item_sum.cc:1913-1933|REAL 移动起点受精度选项限制|AVG 经过该检查需验证|

代码边界注释只是局部计算示意；未见当前目标完整 SQL、明确修复结论或完整答案。没有运行证据，没有声称覆盖。
