# PG 全部报告处理与相邻版本对照

证据快照 UTC：2026-11-05T04:09:16.431368+00:00

冻结集合 136 份报告，逐项均保留。具备已冻结执行场景的报告 68 份；缺必要资料/平台/判据或不适用运行时回放的报告 68 份。
场景×版本项 210，已执行 210 项。报告、场景、版本项和执行次数不可混计。

这里的复现指报告描述的现象，包含符合设计的行为及客户端/配置问题，不能直接当作确认的数据库bug。前版也出现现象，只能排除该目标小版本首次引入该现象；不能证明它从未由更早版本变更引入。
前版未出现、目标版出现，只形成候选版本区间；确认新引入bug还需核对前提、重复复现与定位提交/根因。后版不再出现也不直接证明修复根因。
不同构建场景分别比较；17456固定13.6服务端，对比14.x客户端。旧尝试及superseded记录保留，现行统计按显式替代关系排除。

## 目标版本按报告汇总

|主结果|报告数|
|---|---:|
|已复现报告现象|63|
|资料或环境不足，无法判断|71|
|有效重放后未复现|2|

多场景报告的汇总采用：有任一场景复现则记“已复现报告现象”，详细表仍保留其他场景的异常及缺口；这不表示其他场景完成。

## 相邻版本判断（按独立执行场景）

|判断|场景数|
|---|---:|
|前一相邻版本已有报告现象；不支持目标小版本新引入|63|
|目标版本有效重放未出现报告现象；原因未确定，不能判断引入|2|
|目标版本判定或执行不完整；引入边界无法判断|5|

## 本轮重点对照

|报告/场景|前版|目标版|后版|
|---|---|---|---|
|18810_nocassert|17.1：复现报告现象|17.2：复现报告现象|17.3：有效未复现|
|18801_module_count_revision1|17.1：复现报告现象|17.2：复现报告现象|17.3：复现报告现象|
|17437_main|14.1：无法判断|14.2：无法判断|14.3：无法判断|
|17424_main|14.1：复现报告现象|14.2：复现报告现象|14.3：复现报告现象|
|18792_linked_config_nocassert|17.1：复现报告现象|17.2：复现报告现象|17.3：有效未复现|
|17462_instrumented|14.1：复现报告现象|14.2：复现报告现象|14.3：有效未复现|

## 文件入口

- `all_report_results.csv`：全部136份报告，包括未执行项和具体缺口。
- `all_execution_results.csv`：目标版、前版、后版的环境、oracle、实际现象、阶段和证据路径。
- `version_comparison.csv`：每个场景的三版本对照和引入/消失边界判断。
- `execution_snapshot.json`：服务器原始结果，保留原判定。
- `source_audit.csv`：逐份来源及缺口审查。
- `continuation_20261104/initial_server_snapshot.json`：本轮继续执行前的服务器快照。

## 继续执行的修订与限制

- 18801：首次把每模块优化前/后两个bitcode文件重复计数；依据LLVM源码及报告示例改为统计未优化模块文件，保留总文件数。原SQL与10001判据不变，旧尝试显式替代，三版本重新执行。
- 17462：首次构建的--with-valgrind被PG14忽略，缺USE_VALGRIND，阴性无效。改用源码要求的-DUSE_VALGRIND并验证预处理宏，旧尝试不计有效未复现；原负载及oracle不变。
- 17462原文指向1e0dfd166b3，其主题为增加Valgrind缓冲区访问检测。官方回复明确区分“检测开始报告”与更早存在的底层缺陷，不据此宣称缺陷由该提交引入。
- 17437仅有定性时间归因描述，无明确量化阈值；保留原SQL及JIT开/关完整观测，主结果仍无法判断，不按输出事后编造阈值。
- 18792链接的官方讨论明确给出直接修改postgresql.conf并重载的步骤；该关联场景与原ALTER SYSTEM路径分列，不补造复制槽。18792/18810可能同根因，不计为两个独立bug。
- clang/LLVM/Valgrind及debug/cassert差异均记录在各执行证据中；Linux执行不能验证原Windows/macOS/HA拓扑场景。

## 尚未执行的报告及缺口

|报告|来源/环境缺口|
|---|---|
|17288|原文有 psql COPY 最小命令，明确 Windows 10 崩溃而 Linux 正常；缺对应 Windows 二进制和复现环境。|
|17289|Windows 10 意大利语安装器 getlocales 失败；缺该安装器、系统语言及原安装上下文。|
|17290|安装缺 libintl-9.dll；没有原安装包及依赖状态，不能以 Linux 源码构建测试替代。|
|17300|有 textrange 转 textmultirange 崩溃 SQL，未提供 textrange 自定义类型的创建 SQL；不能猜造类型定义。|
|17315|Raspberry Pi 恢复后缺 ICU 63 共享库；缺原 rsync 系统镜像、库和平台环境。|
|17331|APT 安装说明 i386 架构警告及文档建议；不是 SQL 运行时异常，历史仓库状态不可当成 PG 版本回放。|
|17333|Debian pg_upgradecluster 9.6→14 因重复 data_directory 损坏迁移；缺原 postgresql-common 包版本及完整配置；不运行原破坏性命令。|
|17336|logtape.c 性能与 right_offset(unsigned i) 静态代码问题；未给出触发超过4G条目问题的 SQL/数据，不计运行时复现。|
|17341|freespace.c 注释216应为256；可核对源代码文字，不计 SQL 或运行时 bug 复现。|
|17356|Debian hunspell-hu/pg_updatedicts 编码失败；缺精确字典包版本和对应工具链，不能用任意字典代替。|
|17358|NetBSD 9.2 --with-uuid=bsd 的 uuid_ossp 测试；服务器为 Linux，未满足平台前提。|
|17365|Windows clang-cl13/VS2019 编译 postgres.h 时 stat 重定义；没有完整调用工程及该工具链。|
|17370|有 pg_task 固定提交链接，但未给第三进程 SIGSEGV 触发器和完整启动配置；官方解释共享内存在异常重启后失效。|
|17382|有 VACUUM FULL 和零长度文件列表；缺初始数据库、数据和可验证的持续不删除条件，不能猜造等价负载。|
|17386|有 REINDEX CONCURRENTLY/amcheck 错误与页诊断，缺 jobs 完整数据及并发写入序列；诊断 patch 不能等同原工作负载。|
|17391|OpenBSD7 OpenSSL 与 PG_TEST_EXTRA=ssl 回归失败；缺对应操作系统和SSL环境。|
|17396|Patroni RPM 的 python urllib3/etcd 依赖缺失；没有精确原包与仓库快照。|
|17402|历史 RPM 未签名；正文列11.15/12.10/13.6而字段14.2仍保留入选，不作为14.2 SQL bug。|
|17406|解压附件后发现缺 public.dictionary_version_incr 函数、v3_city/v3_country/v3_okrug/v3_region_type/v3_federal_district 等外键目标及角色；有表数据和物理索引但不是完整可恢复库。不得删除触发器/约束绕过缺失，更不能以14新建索引代替12→14升级。|
|17413|有分区表/数据/UPDATE，但缺 trash、staging schema 的创建、postgresprod foreign server 和 user mapping 配置；不能补造缺失配置。|
|17414|询问9.6在RHEL9的软件仓库安装；Version字段14.2不改变正文非14.2 SQL问题的性质。|
|17425|Windows 服务数据目录尾反斜杠解析失败；Linux源码构建不能检验Windows服务参数。|
|17432|SLES15SP3 PostGIS3.2.1 依赖 libproj22；缺发行版包环境，非普通 SQL 现象。|
|17436|RaspberryPi64 Dockerfile 在 VOLUME 内 RUN initdb 后下一层丢失数据；FROM postgres 未固定 digest，原容器版本和架构缺失。|
|17438|生产逻辑复制高负载后挂起；缺 A/B/C/D 的完整DDL、数据、publication/subscription配置和负载时序。|
|17444|VACUUM/amcheck/dump 诊断对应损坏生产表，只有日志，无原始损坏页或生成损坏的完整操作。|
|17445|三个 paste.opensuse.org 来源已重定向首页或连接失败；网页下载成功不等于恢复原 schema 与成功/失败 SQL。|
|17448|Windows10 1703+ large pages/VMMap 行为，需Windows权限和内存环境，Linux不适用。|
|17457|原场景要求两台主机相同绝对log链接路径却不同物理卷，且删除目标WAL后仍进入rewind；当前单机目录不足以等同该拓扑，缺原可恢复WAL来源和完整启动配置。|
|17471|Windows安装器COMSPEC失败；缺原环境变量/安装器和可复现系统状态。|
|17472|仅称 jsonb[] 删除失败，未给任何建表、数据、SQL或明确预期输出。|
|17474|INSERT 约100KB却只提供截断前缀；缺 transactions/inputs/output_datas 的DDL和数据及完整触发SQL。|
|17476|官方回复有完整 PostGIS geometry/GiST 最小SQL及 variable not found 错误；服务器无PostGIS，原扩展版本未明确。|
|17478|13.3→14.1逻辑复制后8亿行并发建索引漏记录；缺表DDL、数据、复制配置与负载，不用合成数据替代。|
|17481|只有 pg_stat_statements/CALL 崩溃栈，没有被调用过程和可重放工作负载。|
|17503|历史 JDBC42.3.6 RPM 签名问题；不是 PostgreSQL SQL运行时现象。|
|17512|Memoize SIGSEGV 与自定义 fixeddecimal 扩展相关，缺完整生产数据和所用扩展构建；不能补造缓存键。|
|17533|BenchmarkSQL5.0 配置含10 warehouses和runMins=150000，但缺可审计的崩溃发生阶段与完整原始负载证据；短跑不能证明未复现。|
|17537|statement_timeout 动态更新案例缺 tbl_test DDL，1000ms与10s叙述不一致；不能猜造表和更改原超时判据。|
|17600|StackBuilder applications-v2.xml 网络/代理错误，缺原代理和安装器配置。|
|17624|WSL/Ubuntu18.04创建库等待6小时，无完整命令、日志或初始集群状态。|
|17667|描述2022-10-23用WW为43、IW为42，但没有原始SQL；官方解释两种周定义，按严格流程不代写SQL。|
|17802|AWS RDS/pglogical 分区复制退出，缺扩展精确版本和完整源/目标DDL、DSN及复制状态。|
|18507|Windows2016 生产视图查询、sharing violation 与0xC0000409日志，缺视图定义/数据/外部文件占用条件。|
|18531|current of+COMMIT过程有SQL，但缺 crm_import.deals 表、etl_deals 函数、数据和CALL参数。|
|18711|过长数据库名连接失败，原JDBC请求/数据库名未给；讨论中的Unicode举例与虚构UX草案不能拼成原场景。|
|18714|Windows安装失败仅一句描述，无具体错误/安装日志和安装器信息。|
|18718|官网Twitter/X标识建议，非数据库SQL或版本运行时缺陷。|
|18721|Windows原生psql缺history支持的文档说明请求；没有数据库SQL异常。|
|18728|有等待事件查询和缺Lock后缀的结果，未提供触发这些LWLock的pgbench参数/负载；静态映射可另核对但非忠实动态回放。|
|18735|Windows日语SJIS路径与psql元命令，需Windows代码页932/文件系统与相应客户端。|
|18748|声称安装17.2却显示16.3，缺安装包与实际程序路径；版本错配不能算17.2 SQL执行。|
|18753|Windows PITR日志和截断INSERT，缺原基础备份、WAL和完整恢复配置；不能从日志重建原备份。|
|18754|CopyDone后无法重启逻辑复制，缺客户端协议实现、完整消息顺序、slot及publication配置。|
|18755|event trigger 代码用Natts_pg_trigger分配较大数组；静态用常量问题，未给运行时SQL异常。|
|18759|RHEL10仓库repodata历史404，不是数据库SQL或可由源码版本重放的问题。|
|18760|Buildroot/Debianbullseye Meson/docbook构建报SGML属性无声明；缺对应完整工具链/DocBook目录环境。|
|18769|pg_hba_file_rules 漏ldapscheme字段；有修复讨论，无原HBA规则与查询SQL，不能补造配置。|
|18770|仅称 packGraph内存泄漏；没有触发SQL、数据、重复次数或可量化内存oracle。|
|18783|macOS Homebrew postmaster became multithreaded，缺macOS运行环境和原启动上下文。|
|18789|Patroni4.0.4故障转移删除逻辑slot，缺完整HA配置、时序和状态；不在用户现有HA集群制造故障。|
|18791|Windows PostGIS h3.dll编译目标PG15但服务端17，缺原安装包；不是Linux核心SQL场景。|
|18793|crosstab函数有片段但依赖未提供的业务表/类型/数据；varchar返回类型不匹配不能靠猜建表复现。|
|18794|WindowsServer2022 pgBouncer安装器用dat_icu_locale失败；缺对应安装器包和调用流程。|
|18795|Windows11 Norwegian Bokmål 安装locale失败，缺精确安装器与系统locale环境。|
|18800|pg_combinebackup缺少增量文件，仅有错误消息，无原备份链及manifest，无法忠实重放。|
|18884|JDBC时区SQL依赖Test_Table与三个外部截图；缺驱动版本/DDL及可验证连接timezone设置。|
|18886|identity重复键为生产状态问题，缺序列当前值、初始数据与导致不同步的完整操作序列。|
