# PostgreSQL · 9d9c02ccd1ae 取材说明

本文件供研究者核查。每次提交给模型的正文只有[对应的模型输入](../../model-inputs/PG/9d9c02ccd1ae.md)。

## 版本与范围

上游 Git 目标为 [9d9c02ccd1aea8e9131d8f4edb21bf1687e40782](https://github.com/postgres/postgres/commit/9d9c02ccd1aea8e9131d8f4edb21bf1687e40782)。按顺序登记的父节点为 [2f4d0d67994b](https://github.com/postgres/postgres/tree/2f4d0d67994b32320487784afab7ab997d331bb5)。补丁与源码前后对照固定使用第一父节点。

## 取材依据

主片段对齐执行器投影后的处理。上下文选取运行条件的构造、一个内置窗口函数回调与路径传递。其他内置函数及节点读写模板省略。

补丁保留这次更改的 22 个生产实现、接口、运行时目录数据或相应构建文件。下表中的“节选”仅指额外的前后版本与上下文。生产补丁的文件范围为 「src/backend/commands/explain.c」，「src/backend/executor/nodeWindowAgg.c」，「src/backend/nodes/copyfuncs.c」，「src/backend/nodes/equalfuncs.c」，「src/backend/nodes/outfuncs.c」，「src/backend/nodes/readfuncs.c」，「src/backend/optimizer/path/allpaths.c」，「src/backend/optimizer/plan/createplan.c」，「src/backend/optimizer/plan/planner.c」，「src/backend/optimizer/plan/setrefs.c」，「src/backend/optimizer/util/pathnode.c」，「src/backend/utils/adt/int8.c」，「src/backend/utils/adt/windowfuncs.c」，「src/include/catalog/catversion.h」，「src/include/catalog/pg_proc.dat」，「src/include/nodes/execnodes.h」，「src/include/nodes/nodes.h」，「src/include/nodes/parsenodes.h」，「src/include/nodes/pathnodes.h」，「src/include/nodes/plannodes.h」，「src/include/nodes/supportnodes.h」，「src/include/optimizer/pathnode.h」。

| 用途 | 固定源码及位置 | 为什么取这一段 |
|---|---|---|
| 核心位置 · ExecWindowAgg · 投影与返回 | [src/backend/executor/nodeWindowAgg.c L2231–L2239](https://github.com/postgres/postgres/blob/2f4d0d67994b32320487784afab7ab997d331bb5/src/backend/executor/nodeWindowAgg.c#L2231-L2239) | 来自引入补丁修改位置。 |
| 核心位置 · ExecWindowAgg · 投影与返回 | [src/backend/executor/nodeWindowAgg.c L2265–L2342](https://github.com/postgres/postgres/blob/9d9c02ccd1aea8e9131d8f4edb21bf1687e40782/src/backend/executor/nodeWindowAgg.c#L2265-L2342) | 来自引入补丁修改位置。 |
| 补充上下文 · find_window_run_conditions | [src/backend/optimizer/path/allpaths.c L2183–L2363](https://github.com/postgres/postgres/blob/9d9c02ccd1aea8e9131d8f4edb21bf1687e40782/src/backend/optimizer/path/allpaths.c#L2183-L2363) | 本提交新增该函数，将窗口函数支持回调的信息与比较运算符组合成 WindowClause.runCondition。保留三组运算符分支与赋值。 |
| 补充上下文 · window_row_number_support | [src/backend/utils/adt/windowfuncs.c L92–L111](https://github.com/postgres/postgres/blob/9d9c02ccd1aea8e9131d8f4edb21bf1687e40782/src/backend/utils/adt/windowfuncs.c#L92-L111) | 按 SupportRequestWFuncMonotonic 类型可在同一提交中定位一个完整的内置支持回调。 |
| 补充上下文 · create_one_window_path | [src/backend/optimizer/plan/planner.c L4282–L4300](https://github.com/postgres/postgres/blob/9d9c02ccd1aea8e9131d8f4edb21bf1687e40782/src/backend/optimizer/plan/planner.c#L4282-L4300) | 沿 WindowClause.runCondition 定位到窗口路径的构造处，可见顶层标记与中间层条件的传递。 |

## 输入边界与校验

保留标题、优化目标、接口设计及支持的函数范围。原消息中的完整 SQL、具体示例阈值及相应运行过程未进入输入。已移除落款和 Discussion 链接。 实际收录的提交说明行号为 1–4, 20–36, 64–67。

从原始改动中排除的文件共 2 个。src/test/regress/expected/window.out、src/test/regress/sql/window.sql。

生产源码及其注释按固定版本保留。源码注释自带的 SQL 可作为模型可见的提示。

上下文按引入补丁的修改位置、直接调用、状态传递或同一接口的分支选择。模型输入未附后续修复、报告文本、测试语料、预期结果文件或历史实验输出。

已在第一父版本原始字节上应用筛出的生产补丁，并逐文件核对结果与目标版本相同。保留了 2 段核心前后代码、3 段补充上下文。模型输入为 69,593 字节，SHA-256 为 3bf05300839d35bdaa0bf4a4f53d1725ae9a1eb5d518bcc7bab36ae75657387a。

提交说明中的整条查询已移除。生产代码自身注释仍可能描述窗口计算示例，这两类来源按统一口径处理。
