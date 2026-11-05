MySQL 三个引入提交的两阶段提示词
生成日期：2026-11-04

参考格式
https://github.com/Sleepy-Jm/mysql_bugs_test/tree/main/Prompts
模板固定版本：fadce4b16df62f362662754ee8e9745b478a643c

沿用参考仓库的 WhiteFox one-shot 两阶段格式，共 6 份完整提示词。
两个模板、INTERSECT ALL 示例及 build_whitefox_prompts.py 均原样复制；
已按参考仓库固定版本核对 Git blob。英文指令和章节标题与原模板保持一致。

三个目标
1. 4d2da251cb536340d19438cc0039bb2846f9a634
   derived_condition_charset_4d2da251cb53
   派生表条件下推中的表达式克隆、字符串打印与字符集转换。
2. 248c7f7c227e76f3422378ca3b9e10d141dcfc86
   item_property_recalculation_248c7f7c227e
   Item 累积属性重算、窗口表达式复用，以及 IN 左操作数的属性传播。
   需求中分别安排重复执行与 IN 包装两类候选，不将它们视为同一根因。
3. c296cddb93ffc631f9b43d3b1ff769604e7469d7
   window_frame_state_c296cddb93ff
   优化 ROWS 窗口帧中的位置状态及 AVG 除数计算。
   使用该引入提交的源码；未沿用参考仓库中以较晚修复版本为目标的源码片段。

直接使用
每个目标都有以下两个文件，均已填充完成，没有待替换的模板占位符：
  Prompts/mysql/src2req/<目标名>.txt
  Prompts/mysql/req2test/<目标名>.txt

第一阶段 src2req：整份发送给模型，以源码为输入生成测试需求。
当前任务只含固定提交的源码、定位信息和观察目标；不附当前目标的需求答案。
输出章节为 Target / Source-required conditions / Candidate construction /
Correctness oracle / Coverage observation / Uncertainty。

第二阶段 req2test：整份发送给模型，以需求为输入生成完整 SQL 测试。
当前任务只含需求，不重复附上当前目标的实现代码。
输出章节为 Prerequisites / SQL / Expected results and oracle /
Coverage observation / Execution status。

附带的第二阶段提示词使用本次根据源码编写的种子需求，位置为：
  Requirements/mysql/req/<目标名>/<目标名>_1.txt
这些种子需求不是运行本包第一阶段提示词后获得的独立模型输出。
若要完整运行两阶段流程，请先保存实际第一阶段输出，替换相应需求文件，
然后重新生成第二阶段提示词。不要把当前种子需求当作模型能力评测的结果。

离线重新生成（需要 Python 3.9 或更新版本，标准库即可）
在本目录执行：
  python scripts/build_whitefox_prompts.py
  python scripts/build_whitefox_prompts.py --check

源码与定位
source-code-data/mysql/ 内含三个目标的源码片段和共用示例。
目标片段均来自对应引入提交，标注父提交、文件 Git blob、真实行号和链接。
provenance.json 保存模板版本、源码 blob 与选取的行号区间。
源码片段已经过完整文件 Git blob 校验；本包不附 MySQL 完整源码仓库。
如需从持有相应源码对象的本地 Git 仓库重新生成片段：
  python scripts/build_source_excerpts.py --git-dir /path/to/mysql-server/.git
  python scripts/build_source_excerpts.py --git-dir /path/to/mysql-server/.git --check
脚本不自动联网补取对象；缺少对象时会报错。
也可用 --snapshot-dir 指向 <完整提交 SHA>/<上游文件路径> 布局的源码缓存。

验证范围
本包核对了参考模板、源码版本与行号、六份提示词的渲染结果及阶段输入隔离。
本次没有运行提示词调用、没有执行新生成 SQL，也没有测量目标分支覆盖率。
需求中的 SQL 形态是待验证的候选；实际结果判据与覆盖观测分别列出。
这里提供的是三个代码变更目标的测试生成提示词，不表示一个提示词已经覆盖
此前全部 15 个报告，也不表示同一提交对应的多个报告一定是同一根因。
