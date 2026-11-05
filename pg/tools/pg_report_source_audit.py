"""Explicit source review decisions; no inferred SQL or missing-data repair."""
import csv
import hashlib
import json
from pathlib import Path

ROOT=Path('experiments/pg_report_replay_20261104/run_001')
# id | SQL material | disposition | source-grounded gap / execution requirement
DECISIONS='''
17283|not_applicable|adapter_pending|默认 localhost 监听 IPv4/IPv6；有配置现象，无 SQL；需记录本机名称解析和两协议连接结果，不能归因数据库版本。
17284|test_suite|special_build_pending|并发 two-ids 隔离测试各100次，CPPFLAGS=-O0 -DTEST_SUMMARIZE_SERIAL，SerialAdd 断言；普通构建不满足前提。
17288|complete|environment_blocked|原文有 psql COPY 最小命令，明确 Windows 10 崩溃而 Linux 正常；缺对应 Windows 二进制和复现环境。
17289|not_applicable|environment_blocked|Windows 10 意大利语安装器 getlocales 失败；缺该安装器、系统语言及原安装上下文。
17290|not_applicable|environment_blocked|安装缺 libintl-9.dll；没有原安装包及依赖状态，不能以 Linux 源码构建测试替代。
17292|attachment_complete|adapter_pending|buggy.tgz 有 schema/view/219 partitions/index 脚本及计划；原文说明规划超过5小时。须完整附件顺序和有界超时，超时不能标有效未复现。
17300|partial|materials_incomplete|有 textrange 转 textmultirange 崩溃 SQL，未提供 textrange 自定义类型的创建 SQL；不能猜造类型定义。
17304|complete|special_build_pending|select; 与 select union select; 的 psql print.c UBSan 报空指针；必须使用 UBSan 客户端且保留对齐输出模式。
17315|not_applicable|environment_blocked|Raspberry Pi 恢复后缺 ICU 63 共享库；缺原 rsync 系统镜像、库和平台环境。
17331|not_applicable|non_runtime|APT 安装说明 i386 架构警告及文档建议；不是 SQL 运行时异常，历史仓库状态不可当成 PG 版本回放。
17333|not_applicable|environment_blocked|Debian pg_upgradecluster 9.6→14 因重复 data_directory 损坏迁移；缺原 postgresql-common 包版本及完整配置；不运行原破坏性命令。
17336|not_applicable|static_only|logtape.c 性能与 right_offset(unsigned i) 静态代码问题；未给出触发超过4G条目问题的 SQL/数据，不计运行时复现。
17341|not_applicable|static_only|freespace.c 注释216应为256；可核对源代码文字，不计 SQL 或运行时 bug 复现。
17356|not_applicable|environment_blocked|Debian hunspell-hu/pg_updatedicts 编码失败；缺精确字典包版本和对应工具链，不能用任意字典代替。
17357|complete|adapter_pending|完整建表、数据和窗口查询；需比较过滤前后 priority=3 且 n=1 的 id，ORDER BY 的并列值选择无确定性；现象不自动是缺陷。
17358|test_suite|environment_blocked|NetBSD 9.2 --with-uuid=bsd 的 uuid_ossp 测试；服务器为 Linux，未满足平台前提。
17362|embedded_data_complete|environment_blocked|包含 base64/gzip 数据和 ICU 查询；报告明确 CentOS7 RPM 可复现而 OracleLinux8 不可复现，当前 ICU66.1不等同原环境。
17365|partial|environment_blocked|Windows clang-cl13/VS2019 编译 postgres.h 时 stat 重定义；没有完整调用工程及该工具链。
17370|external_extension|materials_incomplete|有 pg_task 固定提交链接，但未给第三进程 SIGSEGV 触发器和完整启动配置；官方解释共享内存在异常重启后失效。
17382|partial|materials_incomplete|有 VACUUM FULL 和零长度文件列表；缺初始数据库、数据和可验证的持续不删除条件，不能猜造等价负载。
17386|partial|materials_incomplete|有 REINDEX CONCURRENTLY/amcheck 错误与页诊断，缺 jobs 完整数据及并发写入序列；诊断 patch 不能等同原工作负载。
17391|test_suite|environment_blocked|OpenBSD7 OpenSSL 与 PG_TEST_EXTRA=ssl 回归失败；缺对应操作系统和SSL环境。
17393|attachment_complete|adapter_pending|官方附件 base_recovery.sh 有完整 PITR 流程；需将路径隔离并保留原集群，不能照抄 rm -rf 清理。
17396|not_applicable|environment_blocked|Patroni RPM 的 python urllib3/etcd 依赖缺失；没有精确原包与仓库快照。
17402|not_applicable|non_runtime|历史 RPM 未签名；正文列11.15/12.10/13.6而字段14.2仍保留入选，不作为14.2 SQL bug。
17406|attachment_partial|materials_incomplete|解压附件后发现缺 public.dictionary_version_incr 函数、v3_city/v3_country/v3_okrug/v3_region_type/v3_federal_district 等外键目标及角色；有表数据和物理索引但不是完整可恢复库。不得删除触发器/约束绕过缺失，更不能以14新建索引代替12→14升级。
17413|partial|materials_incomplete|有分区表/数据/UPDATE，但缺 trash、staging schema 的创建、postgresprod foreign server 和 user mapping 配置；不能补造缺失配置。
17414|not_applicable|non_runtime|询问9.6在RHEL9的软件仓库安装；Version字段14.2不改变正文非14.2 SQL问题的性质。
17424|build_commands|environment_blocked|有 clang -fgnuc-version=0 编译参数和 slock_t 错误；服务器无 clang，原编译器具体版本未给。
17425|not_applicable|environment_blocked|Windows 服务数据目录尾反斜杠解析失败；Linux源码构建不能检验Windows服务参数。
17432|not_applicable|environment_blocked|SLES15SP3 PostGIS3.2.1 依赖 libproj22；缺发行版包环境，非普通 SQL 现象。
17436|dockerfile|environment_blocked|RaspberryPi64 Dockerfile 在 VOLUME 内 RUN initdb 后下一层丢失数据；FROM postgres 未固定 digest，原容器版本和架构缺失。
17437|complete|environment_blocked|pgbench-s20 与 EXPLAIN/JIT 性能归因；当前构建无 LLVM，不能用禁用JIT输出判阴性。
17438|partial|materials_incomplete|生产逻辑复制高负载后挂起；缺 A/B/C/D 的完整DDL、数据、publication/subscription配置和负载时序。
17444|partial|materials_incomplete|VACUUM/amcheck/dump 诊断对应损坏生产表，只有日志，无原始损坏页或生成损坏的完整操作。
17445|external_unavailable|materials_incomplete|三个 paste.opensuse.org 来源已重定向首页或连接失败；网页下载成功不等于恢复原 schema 与成功/失败 SQL。
17448|not_applicable|environment_blocked|Windows10 1703+ large pages/VMMap 行为，需Windows权限和内存环境，Linux不适用。
17456|complete|special_build_pending|完整 ltree schema/trigger/dump/restore；原文明确 server13.6/client14.2，必须保持客户端与服务端角色。
17457|operational_steps|environment_blocked|原场景要求两台主机相同绝对log链接路径却不同物理卷，且删除目标WAL后仍进入rewind；当前单机目录不足以等同该拓扑，缺原可恢复WAL来源和完整启动配置。
17462|pgbench_commands|environment_blocked|pgbench -i -s1 与 -t1000 -c10 -j10 的 valgrind heapam_tuple_lock 无效读取；当前服务器没有valgrind及启用其内存注解的构建。
17466|build_commands|adapter_pending|configure CFLAGS=-DUSE_TOOLS 未自动添加-O2；无 SQL，需核对生成的 CFLAGS，不混入数据库执行数。
17471|not_applicable|environment_blocked|Windows安装器COMSPEC失败；缺原环境变量/安装器和可复现系统状态。
17472|no_sql|materials_incomplete|仅称 jsonb[] 删除失败，未给任何建表、数据、SQL或明确预期输出。
17474|partial|materials_incomplete|INSERT 约100KB却只提供截断前缀；缺 transactions/inputs/output_datas 的DDL和数据及完整触发SQL。
17476|complete_in_reply|environment_blocked|官方回复有完整 PostGIS geometry/GiST 最小SQL及 variable not found 错误；服务器无PostGIS，原扩展版本未明确。
17478|partial|materials_incomplete|13.3→14.1逻辑复制后8亿行并发建索引漏记录；缺表DDL、数据、复制配置与负载，不用合成数据替代。
17481|no_sql|materials_incomplete|只有 pg_stat_statements/CALL 崩溃栈，没有被调用过程和可重放工作负载。
17503|not_applicable|non_runtime|历史 JDBC42.3.6 RPM 签名问题；不是 PostgreSQL SQL运行时现象。
17512|partial|materials_incomplete|Memoize SIGSEGV 与自定义 fixeddecimal 扩展相关，缺完整生产数据和所用扩展构建；不能补造缓存键。
17533|external_workload|materials_incomplete|BenchmarkSQL5.0 配置含10 warehouses和runMins=150000，但缺可审计的崩溃发生阶段与完整原始负载证据；短跑不能证明未复现。
17537|partial|materials_incomplete|statement_timeout 动态更新案例缺 tbl_test DDL，1000ms与10s叙述不一致；不能猜造表和更改原超时判据。
17538|operational_steps|adapter_pending|已连接TCP客户端在 log_hostname=no→yes reload 后断开仍记录IP；需要保留同一会话并观测其断开日志。
17600|not_applicable|environment_blocked|StackBuilder applications-v2.xml 网络/代理错误，缺原代理和安装器配置。
17624|no_sql|materials_incomplete|WSL/Ubuntu18.04创建库等待6小时，无完整命令、日志或初始集群状态。
17667|no_sql|materials_incomplete|描述2022-10-23用WW为43、IW为42，但没有原始SQL；官方解释两种周定义，按严格流程不代写SQL。
17802|partial|environment_blocked|AWS RDS/pglogical 分区复制退出，缺扩展精确版本和完整源/目标DDL、DSN及复制状态。
18507|partial|materials_incomplete|Windows2016 生产视图查询、sharing violation 与0xC0000409日志，缺视图定义/数据/外部文件占用条件。
18531|partial|materials_incomplete|current of+COMMIT过程有SQL，但缺 crm_import.deals 表、etl_deals 函数、数据和CALL参数。
18711|partial|materials_incomplete|过长数据库名连接失败，原JDBC请求/数据库名未给；讨论中的Unicode举例与虚构UX草案不能拼成原场景。
18714|not_applicable|materials_incomplete|Windows安装失败仅一句描述，无具体错误/安装日志和安装器信息。
18718|not_applicable|non_runtime|官网Twitter/X标识建议，非数据库SQL或版本运行时缺陷。
18721|not_applicable|non_runtime|Windows原生psql缺history支持的文档说明请求；没有数据库SQL异常。
18728|partial|materials_incomplete|有等待事件查询和缺Lock后缀的结果，未提供触发这些LWLock的pgbench参数/负载；静态映射可另核对但非忠实动态回放。
18735|complete|environment_blocked|Windows日语SJIS路径与psql元命令，需Windows代码页932/文件系统与相应客户端。
18748|not_applicable|materials_incomplete|声称安装17.2却显示16.3，缺安装包与实际程序路径；版本错配不能算17.2 SQL执行。
18753|partial|materials_incomplete|Windows PITR日志和截断INSERT，缺原基础备份、WAL和完整恢复配置；不能从日志重建原备份。
18754|protocol_steps|materials_incomplete|CopyDone后无法重启逻辑复制，缺客户端协议实现、完整消息顺序、slot及publication配置。
18755|not_applicable|static_only|event trigger 代码用Natts_pg_trigger分配较大数组；静态用常量问题，未给运行时SQL异常。
18759|not_applicable|non_runtime|RHEL10仓库repodata历史404，不是数据库SQL或可由源码版本重放的问题。
18760|build_commands|environment_blocked|Buildroot/Debianbullseye Meson/docbook构建报SGML属性无声明；缺对应完整工具链/DocBook目录环境。
18769|no_sql|materials_incomplete|pg_hba_file_rules 漏ldapscheme字段；有修复讨论，无原HBA规则与查询SQL，不能补造配置。
18770|no_sql|materials_incomplete|仅称 packGraph内存泄漏；没有触发SQL、数据、重复次数或可量化内存oracle。
18783|not_applicable|environment_blocked|macOS Homebrew postmaster became multithreaded，缺macOS运行环境和原启动上下文。
18789|operational_steps|environment_blocked|Patroni4.0.4故障转移删除逻辑slot，缺完整HA配置、时序和状态；不在用户现有HA集群制造故障。
18791|not_applicable|environment_blocked|Windows PostGIS h3.dll编译目标PG15但服务端17，缺原安装包；不是Linux核心SQL场景。
18793|partial|materials_incomplete|crosstab函数有片段但依赖未提供的业务表/类型/数据；varchar返回类型不匹配不能靠猜建表复现。
18794|not_applicable|environment_blocked|WindowsServer2022 pgBouncer安装器用dat_icu_locale失败；缺对应安装器包和调用流程。
18795|not_applicable|environment_blocked|Windows11 Norwegian Bokmål 安装locale失败，缺精确安装器与系统locale环境。
18800|operational_steps|materials_incomplete|pg_combinebackup缺少增量文件，仅有错误消息，无原备份链及manifest，无法忠实重放。
18801|complete|environment_blocked|完整自定义聚合/JIT SQL，要求 LLVM 及 jit_dump_bitcode；当前构建无LLVM，不能按普通查询判阴性。
18805|linked_reproducer|linked_replay_pending|官方讨论明确链接18806为同一项目场景，可引用其来源完整的简化复现；不能算两个独立根因。
18810|log_only|materials_incomplete|有 synchronized_standby_slots=slave reload/logger SIGSEGV日志，但无完整操作步骤；疑似18792同类，不能直接复制其SQL后声称本报告独立复现。
18884|external_screenshots|materials_incomplete|JDBC时区SQL依赖Test_Table与三个外部截图；缺驱动版本/DDL及可验证连接timezone设置。
18886|partial|materials_incomplete|identity重复键为生产状态问题，缺序列当前值、初始数据与导致不同步的完整操作序列。
'''


def main():
    decisions={}
    for line in DECISIONS.strip().splitlines():
        rid,sql,status,note=line.split('|',3);assert rid not in decisions
        decisions[rid]=dict(sql_material_status=sql,review_disposition=status,review_note=note)
    specs=[]
    for p in sorted(ROOT.glob('prepared_specs*.json')):specs+=json.loads(p.read_text(encoding='utf-8'))
    configure_path=ROOT/'configure_results.json'
    configure_results=json.loads(configure_path.read_text(encoding='utf-8')) if configure_path.exists() else []
    rows=[]
    for report in json.loads((ROOT/'frozen_reports.json').read_text(encoding='utf-8')):
        rid=report['report_id'];ss=[s for s in specs if s['report_id']==rid]
        row=dict(report_id=rid,version_field=report['version_field'],source_url=report['source_url'],title=report['title'])
        if ss:row.update(sql_material_status='source_excerpts_prepared',review_disposition='prepared',review_note='已提取有来源的脚本/步骤并冻结场景判据；实际执行结果单列。')
        else:
            assert rid in decisions,rid
            row.update(decisions[rid])
        row['evidence']=[]
        for kind in ['source_text','thread_text']:
            p=ROOT/kind/(rid+'.txt');raw=p.read_bytes();row['evidence'].append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),lines=len(raw.decode('utf-8').splitlines())))
        row['scenario_ids']=[s['scenario_id'] for s in ss]
        row['oracle_status']='frozen' if ss else ('not_sql_runtime' if row['review_disposition'] in ['non_runtime','static_only'] else 'phenomenon_reviewed_execution_oracle_not_frozen')
        row['author_expected_behavior']=[s['oracle']['author_expected_behavior'] for s in ss]
        row['reported_phenomenon']=[s['oracle']['reported_phenomenon'] for s in ss]
        row['unexecuted_main_result']='资料或环境不足，无法判断' if not ss else ''
        if row['review_disposition'] in ['adapter_pending','special_build_pending','linked_replay_pending']:
            row['unexecuted_main_result']='未执行或执行失败';row['execution_substatus']='not_run_preparation_in_progress'
        if rid=='17466' and configure_results:
            row.update(sql_material_status='source_build_commands',review_disposition='prepared_configuration',
                       review_note='有来源的configure参数与冻结oracle；已保存14.1/14.2/14.3构建配置观测，单列计数，不属于SQL或数据库运行时回放。',
                       scenario_ids=['17466_configure'],oracle_status='frozen',unexecuted_main_result='',
                       execution_substatus='configuration_results_saved',
                       configuration_evidence=str(configure_path))
        rows.append(row)
    (ROOT/'source_audit.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    with (ROOT/'source_audit.csv').open('w',encoding='utf-8-sig',newline='') as f:
        keys=list(rows[0]);keys=list(dict.fromkeys(k for row in rows for k in row))
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v for k,v in row.items()} for row in rows)
    from collections import Counter
    print(dict(Counter(r['review_disposition'] for r in rows)))


if __name__=='__main__':main()
