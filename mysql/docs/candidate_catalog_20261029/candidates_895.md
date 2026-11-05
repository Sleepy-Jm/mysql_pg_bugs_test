# 895 项候选总表

[返回目录](README.md)

按目标版本、bug 编号排序；每项为报告 × 目标版本。状态来自保存证据，本次没有运行数据库。

| 候选项 | Bug | 目标版本 | 标题 | 目标执行状态 | 相邻版本状态 | SQL |
|---|---|---|---|---|---|---|
| mysql-98083-8.0.32 | [98083](https://bugs.mysql.com/bug.php?id=98083) | 8.0.32 | Restarting the computer when deleting the database will cause directory residues | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-101262-8.0.32 | [101262](https://bugs.mysql.com/bug.php?id=101262) | 8.0.32 | performance_schema.binary_log_transaction_compression_stats timestamps | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-106225-8.0.32 | [106225](https://bugs.mysql.com/bug.php?id=106225) | 8.0.32 | select bin("") should return 0 instead of null | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-106737-8.0.32 | [106737](https://bugs.mysql.com/bug.php?id=106737) | 8.0.32 | Wrong SE called to ack clone application if >1 SE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-106750-8.0.32 | [106750](https://bugs.mysql.com/bug.php?id=106750) | 8.0.32 | Some clone tests needlessly marked as Linux-only | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-107109-8.0.32 | [107109](https://bugs.mysql.com/bug.php?id=107109) | 8.0.32 | Optimizer hints doesn't work if client charset is the same with charset of syste | 未复现 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-107109-8.0.32.sql) |
| mysql-107337-8.0.32 | [107337](https://bugs.mysql.com/bug.php?id=107337) | 8.0.32 | IN() does not work correctly for TIME column | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-107337-8.0.32.sql) |
| mysql-107366-8.0.32 | [107366](https://bugs.mysql.com/bug.php?id=107366) | 8.0.32 | Contribution by Tencent: Invalid JSON value, Error_code: 3903 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-107384-8.0.32 | [107384](https://bugs.mysql.com/bug.php?id=107384) | 8.0.32 | the warnings of parsing error of hints are treated as syntax_error when upgrade | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-107424-8.0.32 | [107424](https://bugs.mysql.com/bug.php?id=107424) | 8.0.32 | st_intersects() returns different results with or without spatial index | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-107424-8.0.32.sql) |
| mysql-107715-8.0.32 | [107715](https://bugs.mysql.com/bug.php?id=107715) | 8.0.32 | Multiple SE clone not calling clone_end after mixed clone_begin failure/success | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109289-8.0.32 | [109289](https://bugs.mysql.com/bug.php?id=109289) | 8.0.32 | MySQL 8.0.32 corrupted table causing MySQL to crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109661-8.0.32 | [109661](https://bugs.mysql.com/bug.php?id=109661) | 8.0.32 | mysqlsh 8.0.32 is executed without arguments it try to connect using [client] | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109666-8.0.32 | [109666](https://bugs.mysql.com/bug.php?id=109666) | 8.0.32 | ST_Transform fails when transforming from 4326 to 6350 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109685-8.0.32 | [109685](https://bugs.mysql.com/bug.php?id=109685) | 8.0.32 | mysqldump has incompatibile change in MySQL 8.0.32 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109699-8.0.32 | [109699](https://bugs.mysql.com/bug.php?id=109699) | 8.0.32 | utf8mb4 identifiers stopped working since 8.0.32 release | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-109699-8.0.32.sql) |
| mysql-109700-8.0.32 | [109700](https://bugs.mysql.com/bug.php?id=109700) | 8.0.32 | Fix for #33630199 in 8.0.32 not reflected in the documentation and release notes | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109701-8.0.32 | [109701](https://bugs.mysql.com/bug.php?id=109701) | 8.0.32 | Fix for #33630199 in 8.0.32 introduces regression when --set-gtid-purged=OFF | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109705-8.0.32 | [109705](https://bugs.mysql.com/bug.php?id=109705) | 8.0.32 | Flush table deadlock | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109711-8.0.32 | [109711](https://bugs.mysql.com/bug.php?id=109711) | 8.0.32 | mysqlimport doesn't escape reserved-word table names when used with --delete | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109723-8.0.32 | [109723](https://bugs.mysql.com/bug.php?id=109723) | 8.0.32 | Exists query assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109725-8.0.32 | [109725](https://bugs.mysql.com/bug.php?id=109725) | 8.0.32 | Wrong result for AVG() OVER(ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-109725-8.0.32.sql) |
| mysql-109736-8.0.32 | [109736](https://bugs.mysql.com/bug.php?id=109736) | 8.0.32 | ANY query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109764-8.0.32 | [109764](https://bugs.mysql.com/bug.php?id=109764) | 8.0.32 | Index merge not considered for indexes that have a common prefix | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109767-8.0.32 | [109767](https://bugs.mysql.com/bug.php?id=109767) | 8.0.32 | External Component has thrown an exception | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109796-8.0.32 | [109796](https://bugs.mysql.com/bug.php?id=109796) | 8.0.32 | STR_TO_DATE() invalid input doesn't returns NULL but invalid DATE | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-109796-8.0.32.sql) |
| mysql-109820-8.0.32 | [109820](https://bugs.mysql.com/bug.php?id=109820) | 8.0.32 | optimizer hints in definition of views seem to be ignored | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-109820-8.0.32.sql) |
| mysql-109821-8.0.32 | [109821](https://bugs.mysql.com/bug.php?id=109821) | 8.0.32 | Subquery optimizer error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109824-8.0.32 | [109824](https://bugs.mysql.com/bug.php?id=109824) | 8.0.32 | Bit query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109833-8.0.32 | [109833](https://bugs.mysql.com/bug.php?id=109833) | 8.0.32 | UTF-8 strings are broken when comparing to UNIONs | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-109833-8.0.32.sql) |
| mysql-109836-8.0.32 | [109836](https://bugs.mysql.com/bug.php?id=109836) | 8.0.32 | Decimal retention of results in string type data calculation | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109837-8.0.32 | [109837](https://bugs.mysql.com/bug.php?id=109837) | 8.0.32 | The representation of 0 in division function in computing string | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109840-8.0.32 | [109840](https://bugs.mysql.com/bug.php?id=109840) | 8.0.32 | Analyze then Rollup assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109842-8.0.32 | [109842](https://bugs.mysql.com/bug.php?id=109842) | 8.0.32 | Problems when mod , division function and extremum function are used together | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109845-8.0.32 | [109845](https://bugs.mysql.com/bug.php?id=109845) | 8.0.32 | Inconsistency of the results of the round function | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109873-8.0.32 | [109873](https://bugs.mysql.com/bug.php?id=109873) | 8.0.32 | no need to maintain err in buf_page_init_for_read | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109874-8.0.32 | [109874](https://bugs.mysql.com/bug.php?id=109874) | 8.0.32 | DELETE assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109885-8.0.32 | [109885](https://bugs.mysql.com/bug.php?id=109885) | 8.0.32 | ALTER TABLE doesn't update use_stopword when dropping & recreating | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109891-8.0.32 | [109891](https://bugs.mysql.com/bug.php?id=109891) | 8.0.32 | Contribution by Tencent: insert on duplicate key update would be abnormal | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109893-8.0.32 | [109893](https://bugs.mysql.com/bug.php?id=109893) | 8.0.32 | json_contains always return 1 if candidate array is empty array | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109894-8.0.32 | [109894](https://bugs.mysql.com/bug.php?id=109894) | 8.0.32 | Server diagnostics area error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109917-8.0.32 | [109917](https://bugs.mysql.com/bug.php?id=109917) | 8.0.32 | server crash when execute create table with check constraint in ps mode | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109919-8.0.32 | [109919](https://bugs.mysql.com/bug.php?id=109919) | 8.0.32 | Clone plugin does not support arbitrary length O_DIRECT files | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109920-8.0.32 | [109920](https://bugs.mysql.com/bug.php?id=109920) | 8.0.32 | SEs cannot add to clone data size estimates | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109921-8.0.32 | [109921](https://bugs.mysql.com/bug.php?id=109921) | 8.0.32 | Cannot clone with synchronization across SEs | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109922-8.0.32 | [109922](https://bugs.mysql.com/bug.php?id=109922) | 8.0.32 | SEs do not coordinate clone rollbacks on instance startup | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109926-8.0.32 | [109926](https://bugs.mysql.com/bug.php?id=109926) | 8.0.32 | Clone plugin does not support transactional SEs other than InnoDB | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109934-8.0.32 | [109934](https://bugs.mysql.com/bug.php?id=109934) | 8.0.32 | Configuring a MySQL innodb cluster with MySQL Shell failed in Docker container | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109939-8.0.32 | [109939](https://bugs.mysql.com/bug.php?id=109939) | 8.0.32 | Lists partitions can not be reorganized (must be in consecutive order) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109953-8.0.32 | [109953](https://bugs.mysql.com/bug.php?id=109953) | 8.0.32 | InnoDB checkpoint disabled assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109966-8.0.32 | [109966](https://bugs.mysql.com/bug.php?id=109966) | 8.0.32 | Possible server deadlock on checkpoint | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109977-8.0.32 | [109977](https://bugs.mysql.com/bug.php?id=109977) | 8.0.32 | Contribution by Tencent: semisync plugin may print a negative server id | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109991-8.0.32 | [109991](https://bugs.mysql.com/bug.php?id=109991) | 8.0.32 | Compilation fails on Debug instruction | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109996-8.0.32 | [109996](https://bugs.mysql.com/bug.php?id=109996) | 8.0.32 | There is no local IP address matching the one configured for the local node | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110003-8.0.32 | [110003](https://bugs.mysql.com/bug.php?id=110003) | 8.0.32 | DELETE query does ot work for BIT columns | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110003-8.0.32.sql) |
| mysql-110005-8.0.32 | [110005](https://bugs.mysql.com/bug.php?id=110005) | 8.0.32 | When using union, when the value of the field in the where condition is Chinese | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110005-8.0.32.sql) |
| mysql-110011-8.0.32 | [110011](https://bugs.mysql.com/bug.php?id=110011) | 8.0.32 | inconsistent behavior with group by and order by | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110015-8.0.32 | [110015](https://bugs.mysql.com/bug.php?id=110015) | 8.0.32 | Multi-valued index on JSON array is not used when used in a join | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110042-8.0.32 | [110042](https://bugs.mysql.com/bug.php?id=110042) | 8.0.32 | Optimize table and corruption? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110045-8.0.32 | [110045](https://bugs.mysql.com/bug.php?id=110045) | 8.0.32 | Negative numbers on digests | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110045-8.0.32.sql) |
| mysql-110070-8.0.32 | [110070](https://bugs.mysql.com/bug.php?id=110070) | 8.0.32 | System.NotSupportedException: Character set 'utf8mb3' is not supported by .Net F | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110074-8.0.32 | [110074](https://bugs.mysql.com/bug.php?id=110074) | 8.0.32 | CMake option WITH_DEVELOPER_ENTITLEMENTS not documented in the reference | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110076-8.0.32 | [110076](https://bugs.mysql.com/bug.php?id=110076) | 8.0.32 | VALUES Statement with dependent subquery is wrong | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110076-8.0.32.sql) |
| mysql-110077-8.0.32 | [110077](https://bugs.mysql.com/bug.php?id=110077) | 8.0.32 | Lateral join error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110078-8.0.32 | [110078](https://bugs.mysql.com/bug.php?id=110078) | 8.0.32 | optimize for innodb recovery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110089-8.0.32 | [110089](https://bugs.mysql.com/bug.php?id=110089) | 8.0.32 | Inconsistent results returned when choosing different plans on federated engine | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110091-8.0.32 | [110091](https://bugs.mysql.com/bug.php?id=110091) | 8.0.32 | optimize for innodb recovery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110098-8.0.32 | [110098](https://bugs.mysql.com/bug.php?id=110098) | 8.0.32 | add database message into slow log file | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110101-8.0.32 | [110101](https://bugs.mysql.com/bug.php?id=110101) | 8.0.32 | lock_row_lock_current_waits counter in innodb_metrics goes negative | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110102-8.0.32 | [110102](https://bugs.mysql.com/bug.php?id=110102) | 8.0.32 | Invalid utf8mb4 character string: 'E9' on view with derived table | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110104-8.0.32 | [110104](https://bugs.mysql.com/bug.php?id=110104) | 8.0.32 | Query exception caused by union in 8.0.32 | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110104-8.0.32.sql) |
| mysql-110107-8.0.32 | [110107](https://bugs.mysql.com/bug.php?id=110107) | 8.0.32 | InnoDB Data File Error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110122-8.0.32 | [110122](https://bugs.mysql.com/bug.php?id=110122) | 8.0.32 | Start MySQL 8.0.32 second instance with temporary data directory | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110125-8.0.32 | [110125](https://bugs.mysql.com/bug.php?id=110125) | 8.0.32 | Unexpected query result fetched from an indexed column | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110125-8.0.32.sql) |
| mysql-110129-8.0.32 | [110129](https://bugs.mysql.com/bug.php?id=110129) | 8.0.32 | Wrong explanation in innodb_stats_auto_recalc | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110130-8.0.32 | [110130](https://bugs.mysql.com/bug.php?id=110130) | 8.0.32 | Wrong table-path in Error:1114 and Error:13132 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110144-8.0.32 | [110144](https://bugs.mysql.com/bug.php?id=110144) | 8.0.32 | CREATE TABLE with a large MIN_ROWS on an indexed column causes memory error. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110155-8.0.32 | [110155](https://bugs.mysql.com/bug.php?id=110155) | 8.0.32 | Improve GR error MY-013780 reporting | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110164-8.0.32 | [110164](https://bugs.mysql.com/bug.php?id=110164) | 8.0.32 | mysql-8.0.32-macos13-x86_64.dmg installer hangs/freezes | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110170-8.0.32 | [110170](https://bugs.mysql.com/bug.php?id=110170) | 8.0.32 | ZEROFILL should not change the query result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110177-8.0.32 | [110177](https://bugs.mysql.com/bug.php?id=110177) | 8.0.32 | clear invalid comment in table file and index when upgrade from 57 to 80 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110181-8.0.32 | [110181](https://bugs.mysql.com/bug.php?id=110181) | 8.0.32 | tmp_table_size=51200 causing error that tmp does not exists | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110181-8.0.32.sql) |
| mysql-110194-8.0.32 | [110194](https://bugs.mysql.com/bug.php?id=110194) | 8.0.32 | DD upgrade leaves dictonary tables in temporary schema dd_upgrade_targets_80030 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110200-8.0.32 | [110200](https://bugs.mysql.com/bug.php?id=110200) | 8.0.32 | MySQL Database Bug | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110206-8.0.32 | [110206](https://bugs.mysql.com/bug.php?id=110206) | 8.0.32 | Upgrading MySQL Server from 8.0.27 to 8.0.32 using Installer 1.6.5.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110213-8.0.32 | [110213](https://bugs.mysql.com/bug.php?id=110213) | 8.0.32 | An incorrect query result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110216-8.0.32 | [110216](https://bugs.mysql.com/bug.php?id=110216) | 8.0.32 | failed to compile in static mode | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110217-8.0.32 | [110217](https://bugs.mysql.com/bug.php?id=110217) | 8.0.32 | failed to compile in mysql_release mode | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110218-8.0.32 | [110218](https://bugs.mysql.com/bug.php?id=110218) | 8.0.32 | can not link jemalloc or tcmalloc in debian 11.5 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110227-8.0.32 | [110227](https://bugs.mysql.com/bug.php?id=110227) | 8.0.32 | Upgrade to 8.0 fails due to lost+found directory present in datadir | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110228-8.0.32 | [110228](https://bugs.mysql.com/bug.php?id=110228) | 8.0.32 | pushdown condition Including Chinese convert string error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110232-8.0.32 | [110232](https://bugs.mysql.com/bug.php?id=110232) | 8.0.32 | "Killed" counter is not updated with "log_slow_extra" enabled | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110244-8.0.32 | [110244](https://bugs.mysql.com/bug.php?id=110244) | 8.0.32 | Nesting queries in a projection results in different output | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110244-8.0.32.sql) |
| mysql-110245-8.0.32 | [110245](https://bugs.mysql.com/bug.php?id=110245) | 8.0.32 | Issue with NOT IN | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110250-8.0.32 | [110250](https://bugs.mysql.com/bug.php?id=110250) | 8.0.32 | Right join query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110256-8.0.32 | [110256](https://bugs.mysql.com/bug.php?id=110256) | 8.0.32 | An incorrect query result for an indexed decimal column | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110256-8.0.32.sql) |
| mysql-110276-8.0.32 | [110276](https://bugs.mysql.com/bug.php?id=110276) | 8.0.32 | Method not found: 'Void MySql.Data.MySqlClient.MySqlConnectionStringBuilder..cto | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110281-8.0.32 | [110281](https://bugs.mysql.com/bug.php?id=110281) | 8.0.32 | Incorrect query result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110289-8.0.32 | [110289](https://bugs.mysql.com/bug.php?id=110289) | 8.0.32 | Weired error message when an UPDATE uses EXISTS subquery and is blocked | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110301-8.0.32 | [110301](https://bugs.mysql.com/bug.php?id=110301) | 8.0.32 | Change column wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110305-8.0.32 | [110305](https://bugs.mysql.com/bug.php?id=110305) | 8.0.32 | Export of view statement resulting incorrect syntax | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110306-8.0.32 | [110306](https://bugs.mysql.com/bug.php?id=110306) | 8.0.32 | Incorrect costing in test_if_cheaper_ordering | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110310-8.0.32 | [110310](https://bugs.mysql.com/bug.php?id=110310) | 8.0.32 | BETWEEN query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110322-8.0.32 | [110322](https://bugs.mysql.com/bug.php?id=110322) | 8.0.32 | Binary column primary key query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110332-8.0.32 | [110332](https://bugs.mysql.com/bug.php?id=110332) | 8.0.32 | Different result when using a user variable | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110341-8.0.32 | [110341](https://bugs.mysql.com/bug.php?id=110341) | 8.0.32 | FOUND_ROWS() gives wrong result on prepared query against partitioned table | 其他异常 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-110341-8.0.32.sql) |
| mysql-110343-8.0.32 | [110343](https://bugs.mysql.com/bug.php?id=110343) | 8.0.32 | Reproducible crash with assertion failure when updating | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110345-8.0.32 | [110345](https://bugs.mysql.com/bug.php?id=110345) | 8.0.32 | MySQL crash on MacOS typically when restoring a MySQL 5.7 sql | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110347-8.0.32 | [110347](https://bugs.mysql.com/bug.php?id=110347) | 8.0.32 | Inconsistent blocking of UPDATE and DELETE with the same WHERE clause | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110350-8.0.32 | [110350](https://bugs.mysql.com/bug.php?id=110350) | 8.0.32 | MTR test lock_order.cycle fails | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110354-8.0.32 | [110354](https://bugs.mysql.com/bug.php?id=110354) | 8.0.32 | SELECT Query choose different index return different results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110354-8.0.32.sql) |
| mysql-110371-8.0.32 | [110371](https://bugs.mysql.com/bug.php?id=110371) | 8.0.32 | mysql-test/include/keyring_tests/helper/global_keyring_create_config.inc unused | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110375-8.0.32 | [110375](https://bugs.mysql.com/bug.php?id=110375) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32，union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110375-8.0.32.sql) |
| mysql-110376-8.0.32 | [110376](https://bugs.mysql.com/bug.php?id=110376) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32, union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110376-8.0.32.sql) |
| mysql-110383-8.0.32 | [110383](https://bugs.mysql.com/bug.php?id=110383) | 8.0.32 | After ALTER, TABLESPACE is incorrectly explicit with innodb_file_per_table=0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110384-8.0.32 | [110384](https://bugs.mysql.com/bug.php?id=110384) | 8.0.32 | LIKE query on union result with Unicode characters returns no results | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110384-8.0.32.sql) |
| mysql-110407-8.0.32 | [110407](https://bugs.mysql.com/bug.php?id=110407) | 8.0.32 | mysqld crashed when execute a prepared query against partitioned table | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110415-8.0.32 | [110415](https://bugs.mysql.com/bug.php?id=110415) | 8.0.32 | Unrestricted memory allocation to query causes OOM kill | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110416-8.0.32 | [110416](https://bugs.mysql.com/bug.php?id=110416) | 8.0.32 | mysqld strange exit code | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110421-8.0.32 | [110421](https://bugs.mysql.com/bug.php?id=110421) | 8.0.32 | MySQL server not honoring connection_memory_limit for user created temp tables | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110424-8.0.32 | [110424](https://bugs.mysql.com/bug.php?id=110424) | 8.0.32 | Tomcat App looses DB connection after MySQL crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110429-8.0.32 | [110429](https://bugs.mysql.com/bug.php?id=110429) | 8.0.32 | Incorrect autoinc in imported tablespace after restart server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110434-8.0.32 | [110434](https://bugs.mysql.com/bug.php?id=110434) | 8.0.32 | WHERE condition assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110441-8.0.32 | [110441](https://bugs.mysql.com/bug.php?id=110441) | 8.0.32 | Docker Hub mysql/mysql-server debian tag now missing | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110443-8.0.32 | [110443](https://bugs.mysql.com/bug.php?id=110443) | 8.0.32 | Compiling MySQL 8.0.32 fails with DWITH_INNODB_EXTRA_DEBUG. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110446-8.0.32 | [110446](https://bugs.mysql.com/bug.php?id=110446) | 8.0.32 | main.kill_myisam will assert when install group_replication | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110448-8.0.32 | [110448](https://bugs.mysql.com/bug.php?id=110448) | 8.0.32 | Contribution by Tencent: incorrect result of fulltext search | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110452-8.0.32 | [110452](https://bugs.mysql.com/bug.php?id=110452) | 8.0.32 | mysqldump SEGV | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110459-8.0.32 | [110459](https://bugs.mysql.com/bug.php?id=110459) | 8.0.32 | Derive_merge optimizer missing error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110462-8.0.32 | [110462](https://bugs.mysql.com/bug.php?id=110462) | 8.0.32 | Mysqldump table with virtual column wrong syntax | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110474-8.0.32 | [110474](https://bugs.mysql.com/bug.php?id=110474) | 8.0.32 | Functional Index is not work like generated column and index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110480-8.0.32 | [110480](https://bugs.mysql.com/bug.php?id=110480) | 8.0.32 | XML ExtractValue with XPath using last() function return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110485-8.0.32 | [110485](https://bugs.mysql.com/bug.php?id=110485) | 8.0.32 | FLUSH TABLE FOR EXPORT will lead deadlock | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110487-8.0.32 | [110487](https://bugs.mysql.com/bug.php?id=110487) | 8.0.32 | json array field ignored in multi sort. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110496-8.0.32 | [110496](https://bugs.mysql.com/bug.php?id=110496) | 8.0.32 | Join order assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110500-8.0.32 | [110500](https://bugs.mysql.com/bug.php?id=110500) | 8.0.32 | unable to connect to server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110501-8.0.32 | [110501](https://bugs.mysql.com/bug.php?id=110501) | 8.0.32 | Invalid CREATE TABLE statement | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110519-8.0.32 | [110519](https://bugs.mysql.com/bug.php?id=110519) | 8.0.32 | Wrong Allowed Values range for connection_memory_chunk_size in documentation. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110521-8.0.32 | [110521](https://bugs.mysql.com/bug.php?id=110521) | 8.0.32 | 8.0.32 subquery with utf8mb4 equal case empty result | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110521-8.0.32.sql) |
| mysql-110524-8.0.32 | [110524](https://bugs.mysql.com/bug.php?id=110524) | 8.0.32 | XML ExtractValue with XPath on non-existing attribute wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110527-8.0.32 | [110527](https://bugs.mysql.com/bug.php?id=110527) | 8.0.32 | Analyse histogram assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110533-8.0.32 | [110533](https://bugs.mysql.com/bug.php?id=110533) | 8.0.32 | XA COMMIT may not be recovered after a crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110535-8.0.32 | [110535](https://bugs.mysql.com/bug.php?id=110535) | 8.0.32 | Mysql instance cannot be initialized correctly because autocommit is turned off. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110542-8.0.32 | [110542](https://bugs.mysql.com/bug.php?id=110542) | 8.0.32 | Missing error? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110550-8.0.32 | [110550](https://bugs.mysql.com/bug.php?id=110550) | 8.0.32 | ordering VALUES statement seems not to work as expected | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110550-8.0.32.sql) |
| mysql-110555-8.0.32 | [110555](https://bugs.mysql.com/bug.php?id=110555) | 8.0.32 | Some performance schema tables return invalid rows | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110556-8.0.32 | [110556](https://bugs.mysql.com/bug.php?id=110556) | 8.0.32 | When we use json to build an index, we will get wrong results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110556-8.0.32.sql) |
| mysql-110557-8.0.32 | [110557](https://bugs.mysql.com/bug.php?id=110557) | 8.0.32 | When innodb_disable_sort_file_cache=ON, create a full-text index will fail | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110562-8.0.32 | [110562](https://bugs.mysql.com/bug.php?id=110562) | 8.0.32 | values statement | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110562-8.0.32.sql) |
| mysql-110563-8.0.32 | [110563](https://bugs.mysql.com/bug.php?id=110563) | 8.0.32 | NULL safe equality operator query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110565-8.0.32 | [110565](https://bugs.mysql.com/bug.php?id=110565) | 8.0.32 | Adding a fulltext index causes a "Duplicate entry '0'" for the primary key | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110572-8.0.32 | [110572](https://bugs.mysql.com/bug.php?id=110572) | 8.0.32 | Hypergraph optimizer assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110577-8.0.32 | [110577](https://bugs.mysql.com/bug.php?id=110577) | 8.0.32 | Missing year function? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110579-8.0.32 | [110579](https://bugs.mysql.com/bug.php?id=110579) | 8.0.32 | Right join query with BETWEEN wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110582-8.0.32 | [110582](https://bugs.mysql.com/bug.php?id=110582) | 8.0.32 | After executing 'set role', cannot access the database with "_" in the db name | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110587-8.0.32 | [110587](https://bugs.mysql.com/bug.php?id=110587) | 8.0.32 | Bit with index range query may produce different results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110587-8.0.32.sql) |
| mysql-110588-8.0.32 | [110588](https://bugs.mysql.com/bug.php?id=110588) | 8.0.32 | Timestamp cleanup error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110590-8.0.32 | [110590](https://bugs.mysql.com/bug.php?id=110590) | 8.0.32 | Lateral join assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110594-8.0.32 | [110594](https://bugs.mysql.com/bug.php?id=110594) | 8.0.32 | Race condition between xa recover and xa start on Transaction_ctx object | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110597-8.0.32 | [110597](https://bugs.mysql.com/bug.php?id=110597) | 8.0.32 | Different results from equivalent queries | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110600-8.0.32 | [110600](https://bugs.mysql.com/bug.php?id=110600) | 8.0.32 | optimize for page flush | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110633-8.0.32 | [110633](https://bugs.mysql.com/bug.php?id=110633) | 8.0.32 | Orphaned full-text indexes | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110656-8.0.32 | [110656](https://bugs.mysql.com/bug.php?id=110656) | 8.0.32 | Join query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110658-8.0.32 | [110658](https://bugs.mysql.com/bug.php?id=110658) | 8.0.32 | mysql_binlog_xxx() symbols are not exported in lybmysqlclient.so | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110662-8.0.32 | [110662](https://bugs.mysql.com/bug.php?id=110662) | 8.0.32 | global_connection_memory_limit & connection_memory_limit documented incorrectly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110663-8.0.32 | [110663](https://bugs.mysql.com/bug.php?id=110663) | 8.0.32 | Pagetracking return null data if checkpoint LSN is less than page tracking start | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110668-8.0.32 | [110668](https://bugs.mysql.com/bug.php?id=110668) | 8.0.32 | Innodb crash recovery too slow if have wide table redo during apply phase | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110672-8.0.32 | [110672](https://bugs.mysql.com/bug.php?id=110672) | 8.0.32 | QUOTE function doesn't work as expected on tables that are utf16 | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110672-8.0.32.sql) |
| mysql-110676-8.0.32 | [110676](https://bugs.mysql.com/bug.php?id=110676) | 8.0.32 | mysqld got signal 11 after update from 8.0.31 to 8.0.32 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110677-8.0.32 | [110677](https://bugs.mysql.com/bug.php?id=110677) | 8.0.32 | Prepared statement assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110678-8.0.32 | [110678](https://bugs.mysql.com/bug.php?id=110678) | 8.0.32 | oct query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110696-8.0.32 | [110696](https://bugs.mysql.com/bug.php?id=110696) | 8.0.32 | A Query with utf8 string literal returns empty set. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110701-8.0.32 | [110701](https://bugs.mysql.com/bug.php?id=110701) | 8.0.32 | Unable to connect to localhost in DEV | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110702-8.0.32 | [110702](https://bugs.mysql.com/bug.php?id=110702) | 8.0.32 | In-place upgrading from 5.7.41 to 8.0.32, a table with FK's data is broken | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110703-8.0.32 | [110703](https://bugs.mysql.com/bug.php?id=110703) | 8.0.32 | SQL execute return error "BIGINT UNSIGNED value is out of range" | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110706-8.0.32 | [110706](https://bugs.mysql.com/bug.php?id=110706) | 8.0.32 | Data will be lost when the table structure is rebuilt. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110709-8.0.32 | [110709](https://bugs.mysql.com/bug.php?id=110709) | 8.0.32 | Chinese query conditions unable to return results correctly | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110709-8.0.32.sql) |
| mysql-110720-8.0.32 | [110720](https://bugs.mysql.com/bug.php?id=110720) | 8.0.32 | Contribute by tencent: prepared statement can't execute match+rollup twice. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110733-8.0.32 | [110733](https://bugs.mysql.com/bug.php?id=110733) | 8.0.32 | RESET statement assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110765-8.0.32 | [110765](https://bugs.mysql.com/bug.php?id=110765) | 8.0.32 | Function returns incorrect value inside a session | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110773-8.0.32 | [110773](https://bugs.mysql.com/bug.php?id=110773) | 8.0.32 | group_replication start faild use different ips and same port on same server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110804-8.0.32 | [110804](https://bugs.mysql.com/bug.php?id=110804) | 8.0.32 | sql as "select count(*) from table" can't be logged in the slow query log. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110820-8.0.32 | [110820](https://bugs.mysql.com/bug.php?id=110820) | 8.0.32 | Instance backup lock interferes with Performance Schema TRUNCATE TABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110825-8.0.32 | [110825](https://bugs.mysql.com/bug.php?id=110825) | 8.0.32 | Explicit COLLATE clause output in SHOW CREATE TABLE incorrectly | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110825-8.0.32.sql) |
| mysql-110880-8.0.32 | [110880](https://bugs.mysql.com/bug.php?id=110880) | 8.0.32 | XA COMMIT at before_commit return fail breaks group replication recovery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110889-8.0.32 | [110889](https://bugs.mysql.com/bug.php?id=110889) | 8.0.32 | binlog rotate optimize | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110922-8.0.32 | [110922](https://bugs.mysql.com/bug.php?id=110922) | 8.0.32 | Contribution by Tencent: missing --valgrind option in default.daily-valgrind | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110940-8.0.32 | [110940](https://bugs.mysql.com/bug.php?id=110940) | 8.0.32 | Querying VarChar column using 0 in WHERE clause incorrectly returns ALL ROWS | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110941-8.0.32 | [110941](https://bugs.mysql.com/bug.php?id=110941) | 8.0.32 | mysql server not cleaning up certain queries on TCP disconnections | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110955-8.0.32 | [110955](https://bugs.mysql.com/bug.php?id=110955) | 8.0.32 | Query the union all derived table error: the character set cannot be converted | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110968-8.0.32 | [110968](https://bugs.mysql.com/bug.php?id=110968) | 8.0.32 | Table rewrite happens when increasing a varchar length past 63 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110972-8.0.32 | [110972](https://bugs.mysql.com/bug.php?id=110972) | 8.0.32 | Innodb Fulltext search returns incorrect results when kill and restart mysqld | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111063-8.0.32 | [111063](https://bugs.mysql.com/bug.php?id=111063) | 8.0.32 | Assert: !dummy_big_rec on rollback of delete or update of row_format=compressed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111085-8.0.32 | [111085](https://bugs.mysql.com/bug.php?id=111085) | 8.0.32 | The sql-mode from my.ini is not read | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111088-8.0.32 | [111088](https://bugs.mysql.com/bug.php?id=111088) | 8.0.32 | src tarball made from github repo and provided in src.rpm files is not the same | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111101-8.0.32 | [111101](https://bugs.mysql.com/bug.php?id=111101) | 8.0.32 | Join by index returns incorrect results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111109-8.0.32 | [111109](https://bugs.mysql.com/bug.php?id=111109) | 8.0.32 | mysqld --print-defaults doesn't display set persist variables | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111172-8.0.32 | [111172](https://bugs.mysql.com/bug.php?id=111172) | 8.0.32 | X protocol does not report "too many connections" | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111176-8.0.32 | [111176](https://bugs.mysql.com/bug.php?id=111176) | 8.0.32 | View including union does not work when searching for multi-byte values. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111190-8.0.32 | [111190](https://bugs.mysql.com/bug.php?id=111190) | 8.0.32 | Build fails with LANG=ja_JP.UTF-8 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111231-8.0.32 | [111231](https://bugs.mysql.com/bug.php?id=111231) | 8.0.32 | cannot access a disposed object Progress Bar | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111261-8.0.32 | [111261](https://bugs.mysql.com/bug.php?id=111261) | 8.0.32 | Skip scan results in wrong query results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111272-8.0.32 | [111272](https://bugs.mysql.com/bug.php?id=111272) | 8.0.32 | Inconsistent behaviors on string comparison with/without index | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111272-8.0.32.sql) |
| mysql-111302-8.0.32 | [111302](https://bugs.mysql.com/bug.php?id=111302) | 8.0.32 | Returns OK in Message | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111308-8.0.32 | [111308](https://bugs.mysql.com/bug.php?id=111308) | 8.0.32 | inconsistent query result when different Hash Join order | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111363-8.0.32 | [111363](https://bugs.mysql.com/bug.php?id=111363) | 8.0.32 | If you use "UNION ALL" for items with Japanese double-byte characters in a subqu | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-111363-8.0.32.sql) |
| mysql-111420-8.0.32 | [111420](https://bugs.mysql.com/bug.php?id=111420) | 8.0.32 | DB instance restarted with AWS RDS database | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111435-8.0.32 | [111435](https://bugs.mysql.com/bug.php?id=111435) | 8.0.32 | Hash join results in incorrect query results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111442-8.0.32 | [111442](https://bugs.mysql.com/bug.php?id=111442) | 8.0.32 | misleading startup error message related to GTID configuration | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111476-8.0.32 | [111476](https://bugs.mysql.com/bug.php?id=111476) | 8.0.32 | The value for field update_time of information_schema.tables is lost | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111540-8.0.32 | [111540](https://bugs.mysql.com/bug.php?id=111540) | 8.0.32 | binlog compress optimize | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111554-8.0.32 | [111554](https://bugs.mysql.com/bug.php?id=111554) | 8.0.32 | Index on float column causes confusing results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111610-8.0.32 | [111610](https://bugs.mysql.com/bug.php?id=111610) | 8.0.32 | Apparent corruption of an index page to be written to data file. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111616-8.0.32 | [111616](https://bugs.mysql.com/bug.php?id=111616) | 8.0.32 | Failed to upgrade from 5.7 to 8.0 because of spatial column with BTREE index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111685-8.0.32 | [111685](https://bugs.mysql.com/bug.php?id=111685) | 8.0.32 | ADD PARTITION with DATA DIRECTORY forces relocation of other partitions | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111696-8.0.32 | [111696](https://bugs.mysql.com/bug.php?id=111696) | 8.0.32 | The end range of where clause will clear the index->search_info->hash_analysis | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111700-8.0.32 | [111700](https://bugs.mysql.com/bug.php?id=111700) | 8.0.32 | LIMIT values are not adequately handled in EXPLAIN. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111710-8.0.32 | [111710](https://bugs.mysql.com/bug.php?id=111710) | 8.0.32 | Mysql 8 Role Issue | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111802-8.0.32 | [111802](https://bugs.mysql.com/bug.php?id=111802) | 8.0.32 | Updates to transient stats are not taken into affect for I_S views. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111848-8.0.32 | [111848](https://bugs.mysql.com/bug.php?id=111848) | 8.0.32 | libmysqlclient.a missing on mysql-devel-8.0.32-1.module_el8.8.0+3567+56a616e4.aa | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111851-8.0.32 | [111851](https://bugs.mysql.com/bug.php?id=111851) | 8.0.32 | Spatial index not used for join when field is used in MBRIntersects call | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111878-8.0.32 | [111878](https://bugs.mysql.com/bug.php?id=111878) | 8.0.32 | SELECT ROUND(X,D) result below expection | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111883-8.0.32 | [111883](https://bugs.mysql.com/bug.php?id=111883) | 8.0.32 | SELECT ROUND(X,D) result below expection | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111888-8.0.32 | [111888](https://bugs.mysql.com/bug.php?id=111888) | 8.0.32 | 'alter table xxx import tablespace' lead server crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111899-8.0.32 | [111899](https://bugs.mysql.com/bug.php?id=111899) | 8.0.32 | json generated column null problem | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111991-8.0.32 | [111991](https://bugs.mysql.com/bug.php?id=111991) | 8.0.32 | index merge sometimes return incorrect result | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112012-8.0.32 | [112012](https://bugs.mysql.com/bug.php?id=112012) | 8.0.32 | [Warning] [MY-011825] [InnoDB] | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112037-8.0.32 | [112037](https://bugs.mysql.com/bug.php?id=112037) | 8.0.32 | Contribute by tencent: explain analyze show never executed for materialize | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112037-8.0.32.sql) |
| mysql-112109-8.0.32 | [112109](https://bugs.mysql.com/bug.php?id=112109) | 8.0.32 | The mysql8 client displays hexadecimal data | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112188-8.0.32 | [112188](https://bugs.mysql.com/bug.php?id=112188) | 8.0.32 | Fail to import tablespace after upgrade | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112415-8.0.32 | [112415](https://bugs.mysql.com/bug.php?id=112415) | 8.0.32 | Unable to connect to the server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112421-8.0.32 | [112421](https://bugs.mysql.com/bug.php?id=112421) | 8.0.32 | zero and null value, left or right join result wrong | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112421-8.0.32.sql) |
| mysql-112423-8.0.32 | [112423](https://bugs.mysql.com/bug.php?id=112423) | 8.0.32 | select information_schema.columns use any result error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112673-8.0.32 | [112673](https://bugs.mysql.com/bug.php?id=112673) | 8.0.32 | dump from slave with --dump-slave or --dump-replica option will change binlog | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112874-8.0.32 | [112874](https://bugs.mysql.com/bug.php?id=112874) | 8.0.32 | Mysql fails to rollback after invalid undo record | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112897-8.0.32 | [112897](https://bugs.mysql.com/bug.php?id=112897) | 8.0.32 | next-transaction isolation level has problem if current transaction end by begin | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112965-8.0.32 | [112965](https://bugs.mysql.com/bug.php?id=112965) | 8.0.32 | A warning is issued that the FOUND_ROWS() function is deprecated when used alone | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113054-8.0.32 | [113054](https://bugs.mysql.com/bug.php?id=113054) | 8.0.32 | mysql explain filtered inaccurate when find_in_set function used | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113343-8.0.32 | [113343](https://bugs.mysql.com/bug.php?id=113343) | 8.0.32 | Expression #1 of ORDER BY is not in SELECT / incompatible with DISTINCT (#3065) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113393-8.0.32 | [113393](https://bugs.mysql.com/bug.php?id=113393) | 8.0.32 | MySQL Server locks up randomly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113516-8.0.32 | [113516](https://bugs.mysql.com/bug.php?id=113516) | 8.0.32 | rejoin cluster failure as clone plugin is waiting for table metadata lock | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113518-8.0.32 | [113518](https://bugs.mysql.com/bug.php?id=113518) | 8.0.32 | character set with Chinese character,using storage procedure it report 1300 err | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113537-8.0.32 | [113537](https://bugs.mysql.com/bug.php?id=113537) | 8.0.32 | False match of multibyte chars when checking existence of a control character | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113537-8.0.32.sql) |
| mysql-113640-8.0.32 | [113640](https://bugs.mysql.com/bug.php?id=113640) | 8.0.32 | no need to judge rseg in while loop | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113648-8.0.32 | [113648](https://bugs.mysql.com/bug.php?id=113648) | 8.0.32 | Reduced lock interval for purge_sys->pq_mutex | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113658-8.0.32 | [113658](https://bugs.mysql.com/bug.php?id=113658) | 8.0.32 | Avoid unnecessary copy operations with std::move() | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113663-8.0.32 | [113663](https://bugs.mysql.com/bug.php?id=113663) | 8.0.32 | Crash occurs when applying binlog_transaction_dependency_tracking to slave node. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113688-8.0.32 | [113688](https://bugs.mysql.com/bug.php?id=113688) | 8.0.32 | reduce memory usage for purge | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113771-8.0.32 | [113771](https://bugs.mysql.com/bug.php?id=113771) | 8.0.32 | optimize for row_parse_int_from_field | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113776-8.0.32 | [113776](https://bugs.mysql.com/bug.php?id=113776) | 8.0.32 | optimize for btr_insert_into_right_sibling | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113818-8.0.32 | [113818](https://bugs.mysql.com/bug.php?id=113818) | 8.0.32 | optimize for buf_read_page_low | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113843-8.0.32 | [113843](https://bugs.mysql.com/bug.php?id=113843) | 8.0.32 | prepared json query can not use index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114015-8.0.32 | [114015](https://bugs.mysql.com/bug.php?id=114015) | 8.0.32 | 'Undo log record is to big error' when updating column | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114056-8.0.32 | [114056](https://bugs.mysql.com/bug.php?id=114056) | 8.0.32 | Performance degredation using REGEXP in statement with parameters vs query | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114074-8.0.32 | [114074](https://bugs.mysql.com/bug.php?id=114074) | 8.0.32 | optimize for Writeset_trx_dependency_tracker::get_dependency | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114222-8.0.32 | [114222](https://bugs.mysql.com/bug.php?id=114222) | 8.0.32 | Assertion failure: row0mysql.cc:2332:node->pcur->m_rel_pos == BTR_PCUR_ON | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114267-8.0.32 | [114267](https://bugs.mysql.com/bug.php?id=114267) | 8.0.32 | Getting different results when executing the same SQL statement about json | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114374-8.0.32 | [114374](https://bugs.mysql.com/bug.php?id=114374) | 8.0.32 | InnoDB semaphore wait bug - a thread is waiting for itself? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114400-8.0.32 | [114400](https://bugs.mysql.com/bug.php?id=114400) | 8.0.32 | Create partition table with DATA DIRECTORY execution result is incorrect | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114654-8.0.32 | [114654](https://bugs.mysql.com/bug.php?id=114654) | 8.0.32 | when pstress，mysqld crash Assertion failure: buf0lru.cc:2168 thread 281472055363 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114736-8.0.32 | [114736](https://bugs.mysql.com/bug.php?id=114736) | 8.0.32 | performance_schema.binary_log_transaction_compression_stats with wrong timestamp | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114776-8.0.32 | [114776](https://bugs.mysql.com/bug.php?id=114776) | 8.0.32 | mysqlbinlog cannot print geometry correct | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114809-8.0.32 | [114809](https://bugs.mysql.com/bug.php?id=114809) | 8.0.32 | inconsistent page no in btr_pcur_t's move_to_next_page | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115045-8.0.32 | [115045](https://bugs.mysql.com/bug.php?id=115045) | 8.0.32 | Async connection failover crash on group_replication member | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115047-8.0.32 | [115047](https://bugs.mysql.com/bug.php?id=115047) | 8.0.32 | XA_prepare_log_event holds an invalid XID | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115132-8.0.32 | [115132](https://bugs.mysql.com/bug.php?id=115132) | 8.0.32 | group by with COLLATE return unexpected result | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115244-8.0.32 | [115244](https://bugs.mysql.com/bug.php?id=115244) | 8.0.32 | apply an redo on page in file mysql.ibd caused crashes | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115313-8.0.32 | [115313](https://bugs.mysql.com/bug.php?id=115313) | 8.0.32 | hash join when have index and push condition to driver table lead to table scan | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115351-8.0.32 | [115351](https://bugs.mysql.com/bug.php?id=115351) | 8.0.32 | page tracking cannot find stop point | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115380-8.0.32 | [115380](https://bugs.mysql.com/bug.php?id=115380) | 8.0.32 | Update Multiple table failed when table is partitioned and using MRR path | 证据不足 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-115380-8.0.32.sql) |
| mysql-115843-8.0.32 | [115843](https://bugs.mysql.com/bug.php?id=115843) | 8.0.32 | The incorrect calculation of 'select_limit' led to an incorrect index selection | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115951-8.0.32 | [115951](https://bugs.mysql.com/bug.php?id=115951) | 8.0.32 | ALTER TABLE ... IMPORT TABLESPACE may cause unsafe reads | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116144-8.0.32 | [116144](https://bugs.mysql.com/bug.php?id=116144) | 8.0.32 | Crash during recovery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116167-8.0.32 | [116167](https://bugs.mysql.com/bug.php?id=116167) | 8.0.32 | mysql server was crashed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116221-8.0.32 | [116221](https://bugs.mysql.com/bug.php?id=116221) | 8.0.32 | Corruption of an index tree. Assertion failure: btr0btr.cc:702 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116277-8.0.32 | [116277](https://bugs.mysql.com/bug.php?id=116277) | 8.0.32 | Insert rounds datetime/timestamp fractions instead of truncating | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116454-8.0.32 | [116454](https://bugs.mysql.com/bug.php?id=116454) | 8.0.32 | For mysql8.0.32 DEBUG version,it crash when do sql about ANALYZE TABLE USING DAT | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116515-8.0.32 | [116515](https://bugs.mysql.com/bug.php?id=116515) | 8.0.32 | For mysql8.0.32 version,the skip scan result is different when condition is same | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116566-8.0.32 | [116566](https://bugs.mysql.com/bug.php?id=116566) | 8.0.32 | List partition prune get a wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116795-8.0.32 | [116795](https://bugs.mysql.com/bug.php?id=116795) | 8.0.32 | get_oldest_view cost too much and block other oprator | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116796-8.0.32 | [116796](https://bugs.mysql.com/bug.php?id=116796) | 8.0.32 | get_oldest_view cost too much and block other oprator | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116806-8.0.32 | [116806](https://bugs.mysql.com/bug.php?id=116806) | 8.0.32 | Support flashback | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117132-8.0.32 | [117132](https://bugs.mysql.com/bug.php?id=117132) | 8.0.32 | drived_merge optimization error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117155-8.0.32 | [117155](https://bugs.mysql.com/bug.php?id=117155) | 8.0.32 | drived_merge optimization error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117187-8.0.32 | [117187](https://bugs.mysql.com/bug.php?id=117187) | 8.0.32 | Cannot convert string '\xA0' from binary to utf8mb4 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117328-8.0.32 | [117328](https://bugs.mysql.com/bug.php?id=117328) | 8.0.32 | Innodb FATAL [MY-013622] fsync() returned EIO with [MY-013183] Assertion failure: os0file.cc | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117421-8.0.32 | [117421](https://bugs.mysql.com/bug.php?id=117421) | 8.0.32 | Redundant row-level locking for using order DESC | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117459-8.0.32 | [117459](https://bugs.mysql.com/bug.php?id=117459) | 8.0.32 | Cross DDL operations on MySQL partitioned tables, parallel COUNT(*) does not report errors. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117783-8.0.32 | [117783](https://bugs.mysql.com/bug.php?id=117783) | 8.0.32 | optimizer selects the wrong index due to the "low_limit" mechanism | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117917-8.0.32 | [117917](https://bugs.mysql.com/bug.php?id=117917) | 8.0.32 | InnoDB: Failing assertion: lock->lock_word == X_LOCK_DECR | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117999-8.0.32 | [117999](https://bugs.mysql.com/bug.php?id=117999) | 8.0.32 | crash when json_binary::parse_binary | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118499-8.0.32 | [118499](https://bugs.mysql.com/bug.php?id=118499) | 8.0.32 | .mylogin.cnf covered the command line | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118787-8.0.32 | [118787](https://bugs.mysql.com/bug.php?id=118787) | 8.0.32 | MySQL server crashed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118956-8.0.32 | [118956](https://bugs.mysql.com/bug.php?id=118956) | 8.0.32 | Incorrect result when condition use concat function | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119458-8.0.32 | [119458](https://bugs.mysql.com/bug.php?id=119458) | 8.0.32 | server cannot restart after crash when relay_log_recovery=1 and have both mgr and normal slave | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120185-8.0.32 | [120185](https://bugs.mysql.com/bug.php?id=120185) | 8.0.32 | Assertion Failure in add_key_fields with Nested CTE | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120297-8.0.32 | [120297](https://bugs.mysql.com/bug.php?id=120297) | 8.0.32 | query_term.cc:320 assert(false) crash — UNION query triggers unhandled AccessPath | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120414-8.0.32 | [120414](https://bugs.mysql.com/bug.php?id=120414) | 8.0.32 | InnoDB performance regression because of validate_rec_offset | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120638-8.0.32 | [120638](https://bugs.mysql.com/bug.php?id=120638) | 8.0.32 | The value of Rows_examined is incorrect when there is a query involving a union of derived tables | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-107115-8.0.33 | [107115](https://bugs.mysql.com/bug.php?id=107115) | 8.0.33 | ??at the end of the error mecessage after setting Chinese characters to variable | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109401-8.0.33 | [109401](https://bugs.mysql.com/bug.php?id=109401) | 8.0.33 | Rows_query_log_event truncates query due to treating query as C string | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109668-8.0.33 | [109668](https://bugs.mysql.com/bug.php?id=109668) | 8.0.33 | XCom connection stalled forever in read() syscall over network | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110722-8.0.33 | [110722](https://bugs.mysql.com/bug.php?id=110722) | 8.0.33 | Failed to upgrade from 5.7 to 8.0 because of orphan tmp tables created in 5.6 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110736-8.0.33 | [110736](https://bugs.mysql.com/bug.php?id=110736) | 8.0.33 | Build failure with Homebrew rapidjson installed & symlinked | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110745-8.0.33 | [110745](https://bugs.mysql.com/bug.php?id=110745) | 8.0.33 | Build failure with -DWITH_ZLIB=system | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110748-8.0.33 | [110748](https://bugs.mysql.com/bug.php?id=110748) | 8.0.33 | window function with order by clause may lead to wrong results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110752-8.0.33 | [110752](https://bugs.mysql.com/bug.php?id=110752) | 8.0.33 | el7 aarch64 might return invalid for value cache line causing crash during boot | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110758-8.0.33 | [110758](https://bugs.mysql.com/bug.php?id=110758) | 8.0.33 | mysqldump uses FLUSH TABLES without NO_WRITE_TO_BINLOG option | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110760-8.0.33 | [110760](https://bugs.mysql.com/bug.php?id=110760) | 8.0.33 | uninstalling mysql | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110771-8.0.33 | [110771](https://bugs.mysql.com/bug.php?id=110771) | 8.0.33 | Failed to update NULL to empty value on instant col for REDUNDANT table | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110771-8.0.33.sql) |
| mysql-110774-8.0.33 | [110774](https://bugs.mysql.com/bug.php?id=110774) | 8.0.33 | 'show replica status' set the field_flag of 'Second_Behind_Source' NOTNULL | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110779-8.0.33 | [110779](https://bugs.mysql.com/bug.php?id=110779) | 8.0.33 | IN clause cause pick bad performan index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110795-8.0.33 | [110795](https://bugs.mysql.com/bug.php?id=110795) | 8.0.33 | mysql insert is deadlocked | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110805-8.0.33 | [110805](https://bugs.mysql.com/bug.php?id=110805) | 8.0.33 | Subquery assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110818-8.0.33 | [110818](https://bugs.mysql.com/bug.php?id=110818) | 8.0.33 | ANY assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110819-8.0.33 | [110819](https://bugs.mysql.com/bug.php?id=110819) | 8.0.33 | EXISTS with dependent subquery can return incorrect results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110819-8.0.33.sql) |
| mysql-110847-8.0.33 | [110847](https://bugs.mysql.com/bug.php?id=110847) | 8.0.33 | Prepared SELECT returns different results on consecutive executions. | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110847-8.0.33.sql) |
| mysql-110848-8.0.33 | [110848](https://bugs.mysql.com/bug.php?id=110848) | 8.0.33 | missing considering on order by and limit clause in cost calculation | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110857-8.0.33 | [110857](https://bugs.mysql.com/bug.php?id=110857) | 8.0.33 | invalid NO_INDEX_USED=1 metric when using UNION in queries. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110869-8.0.33 | [110869](https://bugs.mysql.com/bug.php?id=110869) | 8.0.33 | Debug build asserts in innodb.ddl_crash_alter_partition test | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110873-8.0.33 | [110873](https://bugs.mysql.com/bug.php?id=110873) | 8.0.33 | CMake checks for clang 15 need to be updated for Apple clang | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110874-8.0.33 | [110874](https://bugs.mysql.com/bug.php?id=110874) | 8.0.33 | Possible missing query error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110906-8.0.33 | [110906](https://bugs.mysql.com/bug.php?id=110906) | 8.0.33 | Index creation assertion error 3 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110915-8.0.33 | [110915](https://bugs.mysql.com/bug.php?id=110915) | 8.0.33 | Having clause missing scope | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110915-8.0.33.sql) |
| mysql-110918-8.0.33 | [110918](https://bugs.mysql.com/bug.php?id=110918) | 8.0.33 | Optimization not applied for IS NULL on NOT NULL column | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110931-8.0.33 | [110931](https://bugs.mysql.com/bug.php?id=110931) | 8.0.33 | Optimizer Trace contradicts to EXPLAIN contradicts to SHOW STATUS | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110941-8.0.33 | [110941](https://bugs.mysql.com/bug.php?id=110941) | 8.0.33 | mysql server not cleaning up certain queries on TCP disconnections | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110942-8.0.33 | [110942](https://bugs.mysql.com/bug.php?id=110942) | 8.0.33 | There is a discontinuity in the value of the AUTO_INCREMENT field | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110961-8.0.33 | [110961](https://bugs.mysql.com/bug.php?id=110961) | 8.0.33 | Subquery to derived optimizer assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110962-8.0.33 | [110962](https://bugs.mysql.com/bug.php?id=110962) | 8.0.33 | JOIN a table with trigger report unexpected WARNINGS | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110962-8.0.33.sql) |
| mysql-110969-8.0.33 | [110969](https://bugs.mysql.com/bug.php?id=110969) | 8.0.33 | Functional indexes aren't covering | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110971-8.0.33 | [110971](https://bugs.mysql.com/bug.php?id=110971) | 8.0.33 | Optimizer: reverse index scan doesn't affect the cost | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110976-8.0.33 | [110976](https://bugs.mysql.com/bug.php?id=110976) | 8.0.33 | full-text index does not change when ngram parser changed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110977-8.0.33 | [110977](https://bugs.mysql.com/bug.php?id=110977) | 8.0.33 | ANY query with wrong result 2 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110979-8.0.33 | [110979](https://bugs.mysql.com/bug.php?id=110979) | 8.0.33 | Update assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110983-8.0.33 | [110983](https://bugs.mysql.com/bug.php?id=110983) | 8.0.33 | issue with window functions in stored procedures | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-110983-8.0.33.sql) |
| mysql-110984-8.0.33 | [110984](https://bugs.mysql.com/bug.php?id=110984) | 8.0.33 | Subqueries with 'limit 1' cause concat strings to report errors | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-110984-8.0.33.sql) |
| mysql-110988-8.0.33 | [110988](https://bugs.mysql.com/bug.php?id=110988) | 8.0.33 | VIEW call error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110990-8.0.33 | [110990](https://bugs.mysql.com/bug.php?id=110990) | 8.0.33 | Create function misleading error for SUPER privilege and log_bin_trust_function | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110991-8.0.33 | [110991](https://bugs.mysql.com/bug.php?id=110991) | 8.0.33 | After server upgrade it does not start | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110993-8.0.33 | [110993](https://bugs.mysql.com/bug.php?id=110993) | 8.0.33 | Contribution by Tencent: Support instant modify column | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110998-8.0.33 | [110998](https://bugs.mysql.com/bug.php?id=110998) | 8.0.33 | Performance regression with SELECT query when sorting on limited fields | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-110999-8.0.33 | [110999](https://bugs.mysql.com/bug.php?id=110999) | 8.0.33 | Unneeded sort after scanning the index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111011-8.0.33 | [111011](https://bugs.mysql.com/bug.php?id=111011) | 8.0.33 | `mysql_config --libs` returns broken zlib reference | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111019-8.0.33 | [111019](https://bugs.mysql.com/bug.php?id=111019) | 8.0.33 | Erro ao tentar MySql Connections | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111025-8.0.33 | [111025](https://bugs.mysql.com/bug.php?id=111025) | 8.0.33 | Different cost with index hint for same plan | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111027-8.0.33 | [111027](https://bugs.mysql.com/bug.php?id=111027) | 8.0.33 | Multi-column indexes with writest will cause HA_ERR_FOUND_DUPP_KEY | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111043-8.0.33 | [111043](https://bugs.mysql.com/bug.php?id=111043) | 8.0.33 | Table data corrupt after upgrading MySql from 5.7.37 to MySql 8.0.33 version | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111044-8.0.33 | [111044](https://bugs.mysql.com/bug.php?id=111044) | 8.0.33 | Assertion failure in buf0buf.cc::Buf_fetch<T>::read_page() | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111062-8.0.33 | [111062](https://bugs.mysql.com/bug.php?id=111062) | 8.0.33 | Cannot disable TLS in MySQL 8.0.33 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111063-8.0.33 | [111063](https://bugs.mysql.com/bug.php?id=111063) | 8.0.33 | Assert: !dummy_big_rec on rollback of delete or update of row_format=compressed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111067-8.0.33 | [111067](https://bugs.mysql.com/bug.php?id=111067) | 8.0.33 | Query result error | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111067-8.0.33.sql) |
| mysql-111068-8.0.33 | [111068](https://bugs.mysql.com/bug.php?id=111068) | 8.0.33 | Lock failure | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111072-8.0.33 | [111072](https://bugs.mysql.com/bug.php?id=111072) | 8.0.33 | The subquery involves JSON, and the execution result is incorrect. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111074-8.0.33 | [111074](https://bugs.mysql.com/bug.php?id=111074) | 8.0.33 | start replica encounter Slave_SQL_Running NO with MY-013117 (null) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111089-8.0.33 | [111089](https://bugs.mysql.com/bug.php?id=111089) | 8.0.33 | MySqlDataReader in C# does not recognize double backslash correctly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111094-8.0.33 | [111094](https://bugs.mysql.com/bug.php?id=111094) | 8.0.33 | Results ordered incorrectly | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111094-8.0.33.sql) |
| mysql-111097-8.0.33 | [111097](https://bugs.mysql.com/bug.php?id=111097) | 8.0.33 | Query statement results with subqueries are unstable | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111106-8.0.33 | [111106](https://bugs.mysql.com/bug.php?id=111106) | 8.0.33 | MySQL 8.0.33 install fails on Ubuntu 20.04 with FIPS enabled | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111119-8.0.33 | [111119](https://bugs.mysql.com/bug.php?id=111119) | 8.0.33 | order by multiple column desc returns wrong results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111143-8.0.33 | [111143](https://bugs.mysql.com/bug.php?id=111143) | 8.0.33 | Quoting of ints | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111157-8.0.33 | [111157](https://bugs.mysql.com/bug.php?id=111157) | 8.0.33 | Column info missing for view after doing a "table swap" where view uses function | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111158-8.0.33 | [111158](https://bugs.mysql.com/bug.php?id=111158) | 8.0.33 | Query failure | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111178-8.0.33 | [111178](https://bugs.mysql.com/bug.php?id=111178) | 8.0.33 | Unable to set the secondary engine | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111182-8.0.33 | [111182](https://bugs.mysql.com/bug.php?id=111182) | 8.0.33 | buffer pool online resize warning message incorrect | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111190-8.0.33 | [111190](https://bugs.mysql.com/bug.php?id=111190) | 8.0.33 | Build fails with LANG=ja_JP.UTF-8 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111212-8.0.33 | [111212](https://bugs.mysql.com/bug.php?id=111212) | 8.0.33 | compile failed with gcc-10 when lto is enable | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111218-8.0.33 | [111218](https://bugs.mysql.com/bug.php?id=111218) | 8.0.33 | Logic bug: logic equal sqls return different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111219-8.0.33 | [111219](https://bugs.mysql.com/bug.php?id=111219) | 8.0.33 | Logic bug: logic equal sqls return different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111220-8.0.33 | [111220](https://bugs.mysql.com/bug.php?id=111220) | 8.0.33 | Logic bug: logic equal sqls return different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111221-8.0.33 | [111221](https://bugs.mysql.com/bug.php?id=111221) | 8.0.33 | Logic bug: logic equal sqls return different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111242-8.0.33 | [111242](https://bugs.mysql.com/bug.php?id=111242) | 8.0.33 | Replica Issue - ('mysql.infoschema'@'localhost') does not exist | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111255-8.0.33 | [111255](https://bugs.mysql.com/bug.php?id=111255) | 8.0.33 | unnecessary locks cannot be released when use index_merge | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111261-8.0.33 | [111261](https://bugs.mysql.com/bug.php?id=111261) | 8.0.33 | Skip scan results in wrong query results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111262-8.0.33 | [111262](https://bugs.mysql.com/bug.php?id=111262) | 8.0.33 | Query return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111263-8.0.33 | [111263](https://bugs.mysql.com/bug.php?id=111263) | 8.0.33 | Query return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111264-8.0.33 | [111264](https://bugs.mysql.com/bug.php?id=111264) | 8.0.33 | Query return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111265-8.0.33 | [111265](https://bugs.mysql.com/bug.php?id=111265) | 8.0.33 | Return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111266-8.0.33 | [111266](https://bugs.mysql.com/bug.php?id=111266) | 8.0.33 | Can't delete a row | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111268-8.0.33 | [111268](https://bugs.mysql.com/bug.php?id=111268) | 8.0.33 | Different character_set_connection returns inconsistent results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111268-8.0.33.sql) |
| mysql-111272-8.0.33 | [111272](https://bugs.mysql.com/bug.php?id=111272) | 8.0.33 | Inconsistent behaviors on string comparison with/without index | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111272-8.0.33.sql) |
| mysql-111286-8.0.33 | [111286](https://bugs.mysql.com/bug.php?id=111286) | 8.0.33 | SDI has incorrect types for DB_TRX_ID and DB_ROLL_PTR fields | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111290-8.0.33 | [111290](https://bugs.mysql.com/bug.php?id=111290) | 8.0.33 | No matching rows when joining multiple tables on binary/varbinary key | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111290-8.0.33.sql) |
| mysql-111293-8.0.33 | [111293](https://bugs.mysql.com/bug.php?id=111293) | 8.0.33 | Create table partition by hash subquery assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111299-8.0.33 | [111299](https://bugs.mysql.com/bug.php?id=111299) | 8.0.33 | Return incorrect result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111303-8.0.33 | [111303](https://bugs.mysql.com/bug.php?id=111303) | 8.0.33 | MySQL Server crashes when executing query | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111304-8.0.33 | [111304](https://bugs.mysql.com/bug.php?id=111304) | 8.0.33 | The Query Rewrite Plugin mixes-up LIMIT and OFFSET. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111306-8.0.33 | [111306](https://bugs.mysql.com/bug.php?id=111306) | 8.0.33 | AccessPath* MoveCompositeIteratorsFromTablePath(AccessPath*, const Query_block& | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111310-8.0.33 | [111310](https://bugs.mysql.com/bug.php?id=111310) | 8.0.33 | Prepared statement with CTE memory leak | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111324-8.0.33 | [111324](https://bugs.mysql.com/bug.php?id=111324) | 8.0.33 | Return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111325-8.0.33 | [111325](https://bugs.mysql.com/bug.php?id=111325) | 8.0.33 | Inconsistent results in BETWEEN clause with NULL value | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111331-8.0.33 | [111331](https://bugs.mysql.com/bug.php?id=111331) | 8.0.33 | Default collation utf8mb4_0900_ai_ci causes inconsistent results to Korean | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111353-8.0.33 | [111353](https://bugs.mysql.com/bug.php?id=111353) | 8.0.33 | 3x Performance Regression from 5.7 to 8.0 on ALTER TABLE FORCE. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111357-8.0.33 | [111357](https://bugs.mysql.com/bug.php?id=111357) | 8.0.33 | JSON explain assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111373-8.0.33 | [111373](https://bugs.mysql.com/bug.php?id=111373) | 8.0.33 | Assertion `!sl->order_list.first' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111374-8.0.33 | [111374](https://bugs.mysql.com/bug.php?id=111374) | 8.0.33 | Assertion `m_return_field_def.auto_flags == Field::NONE' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111375-8.0.33 | [111375](https://bugs.mysql.com/bug.php?id=111375) | 8.0.33 | Assertion `ha_alter_info->handler_flags & (Alter_inplace_info::ADD_VIRTUAL_COLUM | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111376-8.0.33 | [111376](https://bugs.mysql.com/bug.php?id=111376) | 8.0.33 | Assertion `!thd->lex->is_exec_started() &#124;&#124; thd->lex->is_query_tables_locked()' f | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111377-8.0.33 | [111377](https://bugs.mysql.com/bug.php?id=111377) | 8.0.33 | int mysql_execute_command(THD*, bool): Assertion `!thd->in_sub_stmt' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111379-8.0.33 | [111379](https://bugs.mysql.com/bug.php?id=111379) | 8.0.33 | Assertion `context->query_block == thd->lex->current_query_block()' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111383-8.0.33 | [111383](https://bugs.mysql.com/bug.php?id=111383) | 8.0.33 | Scale assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111395-8.0.33 | [111395](https://bugs.mysql.com/bug.php?id=111395) | 8.0.33 | Missing documentation of new privilege TELEMETRY_LOG_ADMIN in 8.0.33 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111403-8.0.33 | [111403](https://bugs.mysql.com/bug.php?id=111403) | 8.0.33 | Assertion `!col_val->item_expression->null_value' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111404-8.0.33 | [111404](https://bugs.mysql.com/bug.php?id=111404) | 8.0.33 | Assertion `is_prepared()' failed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111406-8.0.33 | [111406](https://bugs.mysql.com/bug.php?id=111406) | 8.0.33 | MySQL Server encounters Assertion Failure when executing query | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111414-8.0.33 | [111414](https://bugs.mysql.com/bug.php?id=111414) | 8.0.33 | HASH JOIN results in wrong query results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111421-8.0.33 | [111421](https://bugs.mysql.com/bug.php?id=111421) | 8.0.33 | Unexpected error when `CHECK` a predicate that is always true | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111421-8.0.33.sql) |
| mysql-111429-8.0.33 | [111429](https://bugs.mysql.com/bug.php?id=111429) | 8.0.33 | Incorrect result when timestamp col apply <=> to the result of subquery | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111429-8.0.33.sql) |
| mysql-111430-8.0.33 | [111430](https://bugs.mysql.com/bug.php?id=111430) | 8.0.33 | Case rpl.rpl_plugin_load cause crash when build with -DWITH_LTO=1 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111431-8.0.33 | [111431](https://bugs.mysql.com/bug.php?id=111431) | 8.0.33 | condition_fanout_filter optimizer wrong result? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111432-8.0.33 | [111432](https://bugs.mysql.com/bug.php?id=111432) | 8.0.33 | c++ Undefined Behavior with clang-16 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111441-8.0.33 | [111441](https://bugs.mysql.com/bug.php?id=111441) | 8.0.33 | bool Sql_cmd_dml::prepare(THD*): Assertion `thd->is_error()' failed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111443-8.0.33 | [111443](https://bugs.mysql.com/bug.php?id=111443) | 8.0.33 | Assertion `has_error == thd->get_stmt_da()->is_error()' failed | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111444-8.0.33 | [111444](https://bugs.mysql.com/bug.php?id=111444) | 8.0.33 | Assertion `inited == NONE &#124;&#124; table->open_by_handler' failed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111445-8.0.33 | [111445](https://bugs.mysql.com/bug.php?id=111445) | 8.0.33 | virtual longlong Item_typecast_signed::val_int(): Assertion `is_nullable()' fail | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111448-8.0.33 | [111448](https://bugs.mysql.com/bug.php?id=111448) | 8.0.33 | MySQL Server encounters Assertion Failure when executing query | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111449-8.0.33 | [111449](https://bugs.mysql.com/bug.php?id=111449) | 8.0.33 | void Diagnostics_area::set_eof_status(THD*): Assertion `!is_set()' failed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111450-8.0.33 | [111450](https://bugs.mysql.com/bug.php?id=111450) | 8.0.33 | Assertion `to->field_ptr() != from->field_ptr()' failed. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111453-8.0.33 | [111453](https://bugs.mysql.com/bug.php?id=111453) | 8.0.33 | sql query with "where time_col not between val1 and null' has diffrent results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111454-8.0.33 | [111454](https://bugs.mysql.com/bug.php?id=111454) | 8.0.33 | select query with json and time column has different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111461-8.0.33 | [111461](https://bugs.mysql.com/bug.php?id=111461) | 8.0.33 | Server crash after running crafted SELECT statement | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111462-8.0.33 | [111462](https://bugs.mysql.com/bug.php?id=111462) | 8.0.33 | Server crash after running crafted SELECT statement | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111469-8.0.33 | [111469](https://bugs.mysql.com/bug.php?id=111469) | 8.0.33 | Build failure with Protobuf 22+ | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111471-8.0.33 | [111471](https://bugs.mysql.com/bug.php?id=111471) | 8.0.33 | Unexpected Error: Memory capacity exceeded | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111474-8.0.33 | [111474](https://bugs.mysql.com/bug.php?id=111474) | 8.0.33 | hypergraph_optimizer SEGV | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111477-8.0.33 | [111477](https://bugs.mysql.com/bug.php?id=111477) | 8.0.33 | If Table contains Floating Point with limited digits, UPDATE may silently fail | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111483-8.0.33 | [111483](https://bugs.mysql.com/bug.php?id=111483) | 8.0.33 | Different truncated result between select and delete | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111484-8.0.33 | [111484](https://bugs.mysql.com/bug.php?id=111484) | 8.0.33 | wrong result when rewriting scalar subquery in json function parameters | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111484-8.0.33.sql) |
| mysql-111485-8.0.33 | [111485](https://bugs.mysql.com/bug.php?id=111485) | 8.0.33 | When subquery_to_derived is on, IN-subq to derived table transformed wrongly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111492-8.0.33 | [111492](https://bugs.mysql.com/bug.php?id=111492) | 8.0.33 | Subquery ref count assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111497-8.0.33 | [111497](https://bugs.mysql.com/bug.php?id=111497) | 8.0.33 | Assertion `m_deque == other.m_deque' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111503-8.0.33 | [111503](https://bugs.mysql.com/bug.php?id=111503) | 8.0.33 | Supported platforms and distributions | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111506-8.0.33 | [111506](https://bugs.mysql.com/bug.php?id=111506) | 8.0.33 | Spatial index cardinality equals to the number of rows of the table. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111508-8.0.33 | [111508](https://bugs.mysql.com/bug.php?id=111508) | 8.0.33 | The query results are inconsistent when different optimizer options are used. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111509-8.0.33 | [111509](https://bugs.mysql.com/bug.php?id=111509) | 8.0.33 | The local server has been stopped and i can't do any work of my project. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111510-8.0.33 | [111510](https://bugs.mysql.com/bug.php?id=111510) | 8.0.33 | nth_value window function call assertion error | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111511-8.0.33 | [111511](https://bugs.mysql.com/bug.php?id=111511) | 8.0.33 | CTE missing scope in set queries | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111527-8.0.33 | [111527](https://bugs.mysql.com/bug.php?id=111527) | 8.0.33 | Assertion `inited == RND' failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111528-8.0.33 | [111528](https://bugs.mysql.com/bug.php?id=111528) | 8.0.33 | Count queries cardinality mismatch | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111538-8.0.33 | [111538](https://bugs.mysql.com/bug.php?id=111538) | 8.0.33 | MySQL 8.0.33 is slower than MySQL 8.0.28 with queries using JOINS | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111559-8.0.33 | [111559](https://bugs.mysql.com/bug.php?id=111559) | 8.0.33 | View with CTE syntax error | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111559-8.0.33.sql) |
| mysql-111562-8.0.33 | [111562](https://bugs.mysql.com/bug.php?id=111562) | 8.0.33 | nth_value window function assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111567-8.0.33 | [111567](https://bugs.mysql.com/bug.php?id=111567) | 8.0.33 | no longer can write to drive | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111570-8.0.33 | [111570](https://bugs.mysql.com/bug.php?id=111570) | 8.0.33 | Looking for inexistent data reports 0 rows examined | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111582-8.0.33 | [111582](https://bugs.mysql.com/bug.php?id=111582) | 8.0.33 | Query is incorrect after importing partition table with a different definition | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111585-8.0.33 | [111585](https://bugs.mysql.com/bug.php?id=111585) | 8.0.33 | Order by aggregate assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111595-8.0.33 | [111595](https://bugs.mysql.com/bug.php?id=111595) | 8.0.33 | Decimal query wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111596-8.0.33 | [111596](https://bugs.mysql.com/bug.php?id=111596) | 8.0.33 | krb5-devel is buildreq for all rpm builds on el* | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111598-8.0.33 | [111598](https://bugs.mysql.com/bug.php?id=111598) | 8.0.33 | SELECT FOR SHARE does not acquire lock correctly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111624-8.0.33 | [111624](https://bugs.mysql.com/bug.php?id=111624) | 8.0.33 | It's storing -0 (Minus Zero) value | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111629-8.0.33 | [111629](https://bugs.mysql.com/bug.php?id=111629) | 8.0.33 | Possible corrupt table? | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111636-8.0.33 | [111636](https://bugs.mysql.com/bug.php?id=111636) | 8.0.33 | Query not using the index even with FORCE INDEX | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111638-8.0.33 | [111638](https://bugs.mysql.com/bug.php?id=111638) | 8.0.33 | Sorting and pagination do not meet expectations | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111647-8.0.33 | [111647](https://bugs.mysql.com/bug.php?id=111647) | 8.0.33 | Blob partial update in undo record may lead potential crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111662-8.0.33 | [111662](https://bugs.mysql.com/bug.php?id=111662) | 8.0.33 | continuous replication delays occur. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111669-8.0.33 | [111669](https://bugs.mysql.com/bug.php?id=111669) | 8.0.33 | Simple Query Times Out | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111685-8.0.33 | [111685](https://bugs.mysql.com/bug.php?id=111685) | 8.0.33 | ADD PARTITION with DATA DIRECTORY forces relocation of other partitions | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111689-8.0.33 | [111689](https://bugs.mysql.com/bug.php?id=111689) | 8.0.33 | optimize for page flush | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111693-8.0.33 | [111693](https://bugs.mysql.com/bug.php?id=111693) | 8.0.33 | Insert assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111699-8.0.33 | [111699](https://bugs.mysql.com/bug.php?id=111699) | 8.0.33 | Incorrect results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111699-8.0.33.sql) |
| mysql-111700-8.0.33 | [111700](https://bugs.mysql.com/bug.php?id=111700) | 8.0.33 | LIMIT values are not adequately handled in EXPLAIN. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111701-8.0.33 | [111701](https://bugs.mysql.com/bug.php?id=111701) | 8.0.33 | Binlog replication optimize | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111702-8.0.33 | [111702](https://bugs.mysql.com/bug.php?id=111702) | 8.0.33 | Alter default value with auto_increment column not report error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111703-8.0.33 | [111703](https://bugs.mysql.com/bug.php?id=111703) | 8.0.33 | INSERT ON DUPLICATE KEY locks INSERT if table have many PRIMARY and UNIQUE key | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111706-8.0.33 | [111706](https://bugs.mysql.com/bug.php?id=111706) | 8.0.33 | Incorrect result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111706-8.0.33.sql) |
| mysql-111709-8.0.33 | [111709](https://bugs.mysql.com/bug.php?id=111709) | 8.0.33 | Error missing tablespace if innodb-validate-tablespace-paths=OFF | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111710-8.0.33 | [111710](https://bugs.mysql.com/bug.php?id=111710) | 8.0.33 | Mysql 8 Role Issue | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111714-8.0.33 | [111714](https://bugs.mysql.com/bug.php?id=111714) | 8.0.33 | Table constraint name ignored | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111717-8.0.33 | [111717](https://bugs.mysql.com/bug.php?id=111717) | 8.0.33 | MySQL InnoDB Cluster Requires Manual RebootClusterFromCompleteOutage | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111720-8.0.33 | [111720](https://bugs.mysql.com/bug.php?id=111720) | 8.0.33 | recv_n_pool_free_frames are not maintained correctly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111722-8.0.33 | [111722](https://bugs.mysql.com/bug.php?id=111722) | 8.0.33 | Create view assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111727-8.0.33 | [111727](https://bugs.mysql.com/bug.php?id=111727) | 8.0.33 | MGR failure detection fail due to the wrong legacy of m_expels_in_progress | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111728-8.0.33 | [111728](https://bugs.mysql.com/bug.php?id=111728) | 8.0.33 | Incorrect result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111728-8.0.33.sql) |
| mysql-111737-8.0.33 | [111737](https://bugs.mysql.com/bug.php?id=111737) | 8.0.33 | Double tick in string literals does not work for CREATE TABLE with NO_BACKSLASH_ | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111737-8.0.33.sql) |
| mysql-111739-8.0.33 | [111739](https://bugs.mysql.com/bug.php?id=111739) | 8.0.33 | The query results are inconsistent. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111755-8.0.33 | [111755](https://bugs.mysql.com/bug.php?id=111755) | 8.0.33 | potential risk of innodb recovey | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111770-8.0.33 | [111770](https://bugs.mysql.com/bug.php?id=111770) | 8.0.33 | group replication lost transaction when import tablespace failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111811-8.0.33 | [111811](https://bugs.mysql.com/bug.php?id=111811) | 8.0.33 | UPDATE statement with JOIN doesn't update any records | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111812-8.0.33 | [111812](https://bugs.mysql.com/bug.php?id=111812) | 8.0.33 | Unable to open '#innodb_redo/#ib_redo31_tmp', no permission | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111855-8.0.33 | [111855](https://bugs.mysql.com/bug.php?id=111855) | 8.0.33 | getTableName() gives empty or null results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111858-8.0.33 | [111858](https://bugs.mysql.com/bug.php?id=111858) | 8.0.33 | mysql.db's MDL acquired by XA recover then blocked initializion of ACL | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111866-8.0.33 | [111866](https://bugs.mysql.com/bug.php?id=111866) | 8.0.33 | executing a rename table statement could cause a transaction to be committed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111872-8.0.33 | [111872](https://bugs.mysql.com/bug.php?id=111872) | 8.0.33 | VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111873-8.0.33 | [111873](https://bugs.mysql.com/bug.php?id=111873) | 8.0.33 | there's no warnings or errors after failed to set validate_password_length to 0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111914-8.0.33 | [111914](https://bugs.mysql.com/bug.php?id=111914) | 8.0.33 | Global replication filters replace channel specific filters | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111936-8.0.33 | [111936](https://bugs.mysql.com/bug.php?id=111936) | 8.0.33 | Use validate_password component failed to create user | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112032-8.0.33 | [112032](https://bugs.mysql.com/bug.php?id=112032) | 8.0.33 | Using C program to execute query and report errors | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112106-8.0.33 | [112106](https://bugs.mysql.com/bug.php?id=112106) | 8.0.33 | InnoDB locks supremum when last record of page is updated | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112108-8.0.33 | [112108](https://bugs.mysql.com/bug.php?id=112108) | 8.0.33 | VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112128-8.0.33 | [112128](https://bugs.mysql.com/bug.php?id=112128) | 8.0.33 | The parameters such as MySQL password_history does not take effect | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112132-8.0.33 | [112132](https://bugs.mysql.com/bug.php?id=112132) | 8.0.33 | The configuration of password_history does not take effect | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112137-8.0.33 | [112137](https://bugs.mysql.com/bug.php?id=112137) | 8.0.33 | parallel read is slow when innodb_use_native_aio = off | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112159-8.0.33 | [112159](https://bugs.mysql.com/bug.php?id=112159) | 8.0.33 | VIEW reference in a SELECT subquery returns different results from using TABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112231-8.0.33 | [112231](https://bugs.mysql.com/bug.php?id=112231) | 8.0.33 | Inconsistent result for OVER() when used in stored procedure over InnoDB table | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-112231-8.0.33.sql) |
| mysql-112252-8.0.33 | [112252](https://bugs.mysql.com/bug.php?id=112252) | 8.0.33 | InnoDB page compression impacts checkpointing | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112255-8.0.33 | [112255](https://bugs.mysql.com/bug.php?id=112255) | 8.0.33 | empty vio->signal_mask in the x plugin causes MySQL cannot handle signal | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112259-8.0.33 | [112259](https://bugs.mysql.com/bug.php?id=112259) | 8.0.33 | Assert when debug_sync_timeout is 0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112319-8.0.33 | [112319](https://bugs.mysql.com/bug.php?id=112319) | 8.0.33 | GROUP_CONCAT with GROUP BY and WHERE clause turns NULL into empty strings. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112372-8.0.33 | [112372](https://bugs.mysql.com/bug.php?id=112372) | 8.0.33 | Select query returns duplicate rows | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112395-8.0.33 | [112395](https://bugs.mysql.com/bug.php?id=112395) | 8.0.33 | The results on the open source 8.0.33 are not as expected. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112460-8.0.33 | [112460](https://bugs.mysql.com/bug.php?id=112460) | 8.0.33 | Inconsistent results of SELECT statement with window functions | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/executed_125/mysql-112460-8.0.33.sql) |
| mysql-112542-8.0.33 | [112542](https://bugs.mysql.com/bug.php?id=112542) | 8.0.33 | MySQL GR does not see tables with GIPK if show_gipk is OFF | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112589-8.0.33 | [112589](https://bugs.mysql.com/bug.php?id=112589) | 8.0.33 | ER_ROW_IS_REFERENCED vs ER_ROW_IS_REFERENCED_2 breaks backwards compatibility | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112779-8.0.33 | [112779](https://bugs.mysql.com/bug.php?id=112779) | 8.0.33 | Not auto rejoin after failing to parse relay log | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112849-8.0.33 | [112849](https://bugs.mysql.com/bug.php?id=112849) | 8.0.33 | When tls_version is empty, warnings in error log should be removed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112876-8.0.33 | [112876](https://bugs.mysql.com/bug.php?id=112876) | 8.0.33 | ICP (Index condition pushdown) causing BIGINT UNSIGNED value out of range error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113061-8.0.33 | [113061](https://bugs.mysql.com/bug.php?id=113061) | 8.0.33 | The result of avg(distinct xx）is different between from primary and secondary | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113061-8.0.33.sql) |
| mysql-113180-8.0.33 | [113180](https://bugs.mysql.com/bug.php?id=113180) | 8.0.33 | Unexpected Results when Using Math Function SIN | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113180-8.0.33.sql) |
| mysql-113185-8.0.33 | [113185](https://bugs.mysql.com/bug.php?id=113185) | 8.0.33 | Unexpected Results when using NULLIF Function in Filter | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113226-8.0.33 | [113226](https://bugs.mysql.com/bug.php?id=113226) | 8.0.33 | ALTER TABLE with comma separated DROP FOREIGN KEY AND ADD FOREIGN KEY throws | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113229-8.0.33 | [113229](https://bugs.mysql.com/bug.php?id=113229) | 8.0.33 | mysqld: Duplicate entry 'mysql/slave_worker_info' for key 'tablespaces.name' | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113288-8.0.33 | [113288](https://bugs.mysql.com/bug.php?id=113288) | 8.0.33 | Explain plan shows dynamic range, but bug causes no chance to use for LEFT JOIN | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113298-8.0.33 | [113298](https://bugs.mysql.com/bug.php?id=113298) | 8.0.33 | Unexpected Results when Using IN for Floating-Point | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113298-8.0.33.sql) |
| mysql-113318-8.0.33 | [113318](https://bugs.mysql.com/bug.php?id=113318) | 8.0.33 | unnest scalar subquery using groupby produces wrong result | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113319-8.0.33 | [113319](https://bugs.mysql.com/bug.php?id=113319) | 8.0.33 | unnesting scalar subquery containing count and having cond produces wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113319-8.0.33.sql) |
| mysql-113446-8.0.33 | [113446](https://bugs.mysql.com/bug.php?id=113446) | 8.0.33 | Query with DISTINCT and ORDER BY on BIT data type returns wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113513-8.0.33 | [113513](https://bugs.mysql.com/bug.php?id=113513) | 8.0.33 | Join reordering regression and inconsistent behavior for SQL involving LEFT JOIN | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113570-8.0.33 | [113570](https://bugs.mysql.com/bug.php?id=113570) | 8.0.33 | composite index with the indexed expression "is not null" not being used | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113812-8.0.33 | [113812](https://bugs.mysql.com/bug.php?id=113812) | 8.0.33 | alter table tablename engine=innodb cause data loss | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113819-8.0.33 | [113819](https://bugs.mysql.com/bug.php?id=113819) | 8.0.33 | when use show engine innodb cannot show correct information | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114246-8.0.33 | [114246](https://bugs.mysql.com/bug.php?id=114246) | 8.0.33 | I can't find any syntax to allow me to specify an index and a limit for DELETE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114273-8.0.33 | [114273](https://bugs.mysql.com/bug.php?id=114273) | 8.0.33 | turn on the binlog compression and load large data to server will cause oom | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114310-8.0.33 | [114310](https://bugs.mysql.com/bug.php?id=114310) | 8.0.33 | Master_compression_algorithm output is wrong | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114438-8.0.33 | [114438](https://bugs.mysql.com/bug.php?id=114438) | 8.0.33 | high memory usage on a MySQL server during query | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114714-8.0.33 | [114714](https://bugs.mysql.com/bug.php?id=114714) | 8.0.33 | Duplicate subquery explain plan output when explain format is tree | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114714-8.0.33.sql) |
| mysql-114799-8.0.33 | [114799](https://bugs.mysql.com/bug.php?id=114799) | 8.0.33 | ERROR 1216 vs ERROR 1452 in MySQL 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114807-8.0.33 | [114807](https://bugs.mysql.com/bug.php?id=114807) | 8.0.33 | Subquery returns more than 1 row | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114970-8.0.33 | [114970](https://bugs.mysql.com/bug.php?id=114970) | 8.0.33 | prev_record_reads() use stale cardinality to calculate after plan enumeration | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115024-8.0.33 | [115024](https://bugs.mysql.com/bug.php?id=115024) | 8.0.33 | MySQL Crash occurs during MySQL Replication stop process | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115208-8.0.33 | [115208](https://bugs.mysql.com/bug.php?id=115208) | 8.0.33 | Last_query_cost could be negative number due to unmatched cost values in JOIN | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115332-8.0.33 | [115332](https://bugs.mysql.com/bug.php?id=115332) | 8.0.33 | Abnormal increase in the Innodb_rows_inserted metric value | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115397-8.0.33 | [115397](https://bugs.mysql.com/bug.php?id=115397) | 8.0.33 | statement_id variable has minimal documentation | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115625-8.0.33 | [115625](https://bugs.mysql.com/bug.php?id=115625) | 8.0.33 | blob supports exceptions after java object serialization | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116012-8.0.33 | [116012](https://bugs.mysql.com/bug.php?id=116012) | 8.0.33 | MySQL8 - mysqld_'--no-monitor' option not working | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116703-8.0.33 | [116703](https://bugs.mysql.com/bug.php?id=116703) | 8.0.33 | `JSON_VALID` has inconsistent behavior for `NULL` | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-116703-8.0.33.sql) |
| mysql-119581-8.0.33 | [119581](https://bugs.mysql.com/bug.php?id=119581) | 8.0.33 | FLOOR function shows inconsistent overflow handling | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119630-8.0.33 | [119630](https://bugs.mysql.com/bug.php?id=119630) | 8.0.33 | Optimizer incorrectly merges derived table with type conversion and WHERE clause, causing wrong query results | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-119630-8.0.33.sql) |
| mysql-119631-8.0.33 | [119631](https://bugs.mysql.com/bug.php?id=119631) | 8.0.33 | CTE with type conversion and WHERE condition in IN/EXISTS subquery returns all rows instead of filtered rows | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-119631-8.0.33.sql) |
| mysql-119646-8.0.33 | [119646](https://bugs.mysql.com/bug.php?id=119646) | 8.0.33 | View + Type Conversion + IN Subquery Returns Wrong Result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-119646-8.0.33.sql) |
| mysql-120713-8.0.33 | [120713](https://bugs.mysql.com/bug.php?id=120713) | 8.0.33 | Optimizer incorrectly prefers ordering index over selective index for ORDER BY … LIMIT 1 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-121062-8.0.33 | [121062](https://bugs.mysql.com/bug.php?id=121062) | 8.0.33 | Prepared statement with USING variables returns empty result against DATE + TIME columns | 其他异常 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-121062-8.0.33.sql) |
| mysql-79813-8.0.34 | [79813](https://bugs.mysql.com/bug.php?id=79813) | 8.0.34 | Boolean values are returned inconsistently with JSON_OBJECT | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-79813-8.0.34.sql) |
| mysql-102586-8.0.34 | [102586](https://bugs.mysql.com/bug.php?id=102586) | 8.0.34 | Foreign Key ON DELETE CASCADE breaks with RBR and multiple-table DELETE. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-104406-8.0.34 | [104406](https://bugs.mysql.com/bug.php?id=104406) | 8.0.34 | The result of querying through the secondary index is incorrect | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111807-8.0.34 | [111807](https://bugs.mysql.com/bug.php?id=111807) | 8.0.34 | SELECT query assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111851-8.0.34 | [111851](https://bugs.mysql.com/bug.php?id=111851) | 8.0.34 | Spatial index not used for join when field is used in MBRIntersects call | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111852-8.0.34 | [111852](https://bugs.mysql.com/bug.php?id=111852) | 8.0.34 | An incorrect number of records is returned | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111888-8.0.34 | [111888](https://bugs.mysql.com/bug.php?id=111888) | 8.0.34 | 'alter table xxx import tablespace' lead server crash | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111891-8.0.34 | [111891](https://bugs.mysql.com/bug.php?id=111891) | 8.0.34 | Assertion failed in table.h: void Table_ref::set_tableno(uint): Assertion `table | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111899-8.0.34 | [111899](https://bugs.mysql.com/bug.php?id=111899) | 8.0.34 | json generated column null problem | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111900-8.0.34 | [111900](https://bugs.mysql.com/bug.php?id=111900) | 8.0.34 | FOREIGN KEY (prefix of parent table's PK/UK) should not have the PK/UK's name. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111917-8.0.34 | [111917](https://bugs.mysql.com/bug.php?id=111917) | 8.0.34 | derived condition pushdown query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111918-8.0.34 | [111918](https://bugs.mysql.com/bug.php?id=111918) | 8.0.34 | Auto increment column query wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-111918-8.0.34.sql) |
| mysql-111952-8.0.34 | [111952](https://bugs.mysql.com/bug.php?id=111952) | 8.0.34 | Row constructor inequality comparison on Primary Key results in full table scan. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111955-8.0.34 | [111955](https://bugs.mysql.com/bug.php?id=111955) | 8.0.34 | Prepared statement with CTE assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111961-8.0.34 | [111961](https://bugs.mysql.com/bug.php?id=111961) | 8.0.34 | MySQL 8.0.34 crashing suddenly | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111965-8.0.34 | [111965](https://bugs.mysql.com/bug.php?id=111965) | 8.0.34 | default NULL column leads to foreign key constraint failure | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111977-8.0.34 | [111977](https://bugs.mysql.com/bug.php?id=111977) | 8.0.34 | sql10637307 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111980-8.0.34 | [111980](https://bugs.mysql.com/bug.php?id=111980) | 8.0.34 | MySQL Server does not read OpenSSL's openssl.cnf file unless ssl-fips-mode=ON | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111983-8.0.34 | [111983](https://bugs.mysql.com/bug.php?id=111983) | 8.0.34 | Assertion failed in field.cc:4963: virtual longlong Field_temporal_with_date_and | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-111986-8.0.34 | [111986](https://bugs.mysql.com/bug.php?id=111986) | 8.0.34 | Unused function dd_process_dd_columns_rec | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112008-8.0.34 | [112008](https://bugs.mysql.com/bug.php?id=112008) | 8.0.34 | Unused macro DBUG_EVALUATE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112022-8.0.34 | [112022](https://bugs.mysql.com/bug.php?id=112022) | 8.0.34 | Compiling with -DWITH_DEBUG=1 and using C++17 resulted in a failure. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112037-8.0.34 | [112037](https://bugs.mysql.com/bug.php?id=112037) | 8.0.34 | Contribute by tencent: explain analyze show never executed for materialize | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112037-8.0.34.sql) |
| mysql-112067-8.0.34 | [112067](https://bugs.mysql.com/bug.php?id=112067) | 8.0.34 | Failed to upgrade the query rewrite plugin installed in 5.7 to 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112084-8.0.34 | [112084](https://bugs.mysql.com/bug.php?id=112084) | 8.0.34 | performance optimization | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112089-8.0.34 | [112089](https://bugs.mysql.com/bug.php?id=112089) | 8.0.34 | libmysqlclient21 8.0.34 introduces new warning output breaking applications | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112105-8.0.34 | [112105](https://bugs.mysql.com/bug.php?id=112105) | 8.0.34 | Create table from prepared statement issues | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112108-8.0.34 | [112108](https://bugs.mysql.com/bug.php?id=112108) | 8.0.34 | VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112116-8.0.34 | [112116](https://bugs.mysql.com/bug.php?id=112116) | 8.0.34 | Add AFTER_IMPORT_PER_TABLE option for deferTableIndexes in util.loadDump | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112117-8.0.34 | [112117](https://bugs.mysql.com/bug.php?id=112117) | 8.0.34 | innodb_print_all_deadlocks does not print header to error log | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112118-8.0.34 | [112118](https://bugs.mysql.com/bug.php?id=112118) | 8.0.34 | Free list record 11234 is above rec heap top 8812 - MySQL Server Not Starting | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112120-8.0.34 | [112120](https://bugs.mysql.com/bug.php?id=112120) | 8.0.34 | FOREIGN KEY: the length of referencing/referenced columns should be compatible. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112137-8.0.34 | [112137](https://bugs.mysql.com/bug.php?id=112137) | 8.0.34 | parallel read is slow when innodb_use_native_aio = off | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112147-8.0.34 | [112147](https://bugs.mysql.com/bug.php?id=112147) | 8.0.34 | Use/Ignore Mutil-value index for MEMBER OF function has differnet result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112147-8.0.34.sql) |
| mysql-112148-8.0.34 | [112148](https://bugs.mysql.com/bug.php?id=112148) | 8.0.34 | Description Failed to upgrade mysql from 8.0.20 to 8.0.34 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112149-8.0.34 | [112149](https://bugs.mysql.com/bug.php?id=112149) | 8.0.34 | Inconsistent results caused by SPACE() function and ''&#124;&#124;'' operations | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112151-8.0.34 | [112151](https://bugs.mysql.com/bug.php?id=112151) | 8.0.34 | Wrong query output type | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112152-8.0.34 | [112152](https://bugs.mysql.com/bug.php?id=112152) | 8.0.34 | Rename user to ''@'%' cause "Access denied" | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112153-8.0.34 | [112153](https://bugs.mysql.com/bug.php?id=112153) | 8.0.34 | ADD COLUMN with expressional DEFAULT does not support online ALTER TABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112154-8.0.34 | [112154](https://bugs.mysql.com/bug.php?id=112154) | 8.0.34 | Slow Queries Exceeding 1 Second in Concurrent Insert Scenario on MySQL 8.0.34 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112158-8.0.34 | [112158](https://bugs.mysql.com/bug.php?id=112158) | 8.0.34 | Calling of stored procedure is not case sensitive | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112172-8.0.34 | [112172](https://bugs.mysql.com/bug.php?id=112172) | 8.0.34 | Left join query null value assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112178-8.0.34 | [112178](https://bugs.mysql.com/bug.php?id=112178) | 8.0.34 | Transaction inconsistency when the undo space truncate is incomplete | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112179-8.0.34 | [112179](https://bugs.mysql.com/bug.php?id=112179) | 8.0.34 | Backslash in string literals does not work for CREATE TABLE with NO_BACKSLASH_ | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112180-8.0.34 | [112180](https://bugs.mysql.com/bug.php?id=112180) | 8.0.34 | "Skip Scan Range Access Method" may lead to incorrect query results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112184-8.0.34 | [112184](https://bugs.mysql.com/bug.php?id=112184) | 8.0.34 | cannot create user if they are listed as creator in views or routines | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112194-8.0.34 | [112194](https://bugs.mysql.com/bug.php?id=112194) | 8.0.34 | Incorrect result when using INNER JOIN with SELECT FROM VIEW together with OR co | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112198-8.0.34 | [112198](https://bugs.mysql.com/bug.php?id=112198) | 8.0.34 | Incorrect multiple equality optimization causes performance degradation | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112198-8.0.34.sql) |
| mysql-112201-8.0.34 | [112201](https://bugs.mysql.com/bug.php?id=112201) | 8.0.34 | Deadlock with show fields, alter, and select | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112212-8.0.34 | [112212](https://bugs.mysql.com/bug.php?id=112212) | 8.0.34 | Subquery to derived result mismatch(HASH JOIN/BNL JOIN result mismatch) | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112212-8.0.34.sql) |
| mysql-112231-8.0.34 | [112231](https://bugs.mysql.com/bug.php?id=112231) | 8.0.34 | Inconsistent result for OVER() when used in stored procedure over InnoDB table | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112231-8.0.34.sql) |
| mysql-112238-8.0.34 | [112238](https://bugs.mysql.com/bug.php?id=112238) | 8.0.34 | Inconsistent results caused by FIELD() | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112242-8.0.34 | [112242](https://bugs.mysql.com/bug.php?id=112242) | 8.0.34 | Unexpected Results by use_invisible_indexes | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112242-8.0.34.sql) |
| mysql-112243-8.0.34 | [112243](https://bugs.mysql.com/bug.php?id=112243) | 8.0.34 | Unexpected Result by subquery_to_derived | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112252-8.0.34 | [112252](https://bugs.mysql.com/bug.php?id=112252) | 8.0.34 | InnoDB page compression impacts checkpointing | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112255-8.0.34 | [112255](https://bugs.mysql.com/bug.php?id=112255) | 8.0.34 | empty vio->signal_mask in the x plugin causes MySQL cannot handle signal | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112256-8.0.34 | [112256](https://bugs.mysql.com/bug.php?id=112256) | 8.0.34 | The event thread_id of source changed after write to local | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112262-8.0.34 | [112262](https://bugs.mysql.com/bug.php?id=112262) | 8.0.34 | tablespace is missing for table innodb_undo_002 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112269-8.0.34 | [112269](https://bugs.mysql.com/bug.php?id=112269) | 8.0.34 | Unexpected Results by the hint JOIN_ORDER | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112269-8.0.34.sql) |
| mysql-112275-8.0.34 | [112275](https://bugs.mysql.com/bug.php?id=112275) | 8.0.34 | "Extra" field has NULL value if table is temporary | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112275-8.0.34.sql) |
| mysql-112280-8.0.34 | [112280](https://bugs.mysql.com/bug.php?id=112280) | 8.0.34 | Incorrect costing of group by loose index scans | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112287-8.0.34 | [112287](https://bugs.mysql.com/bug.php?id=112287) | 8.0.34 | log_slow_replica_statements will be deprecated on 8.0.34 and 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112289-8.0.34 | [112289](https://bugs.mysql.com/bug.php?id=112289) | 8.0.34 | No error seen when unknown column is used in subquery for Update Statement | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112293-8.0.34 | [112293](https://bugs.mysql.com/bug.php?id=112293) | 8.0.34 | Wrong result if non-breaking space is contained in varchar | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112293-8.0.34.sql) |
| mysql-112296-8.0.34 | [112296](https://bugs.mysql.com/bug.php?id=112296) | 8.0.34 | Unexpected Result by NO_BNL | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112296-8.0.34.sql) |
| mysql-112297-8.0.34 | [112297](https://bugs.mysql.com/bug.php?id=112297) | 8.0.34 | Wrong query output type 2 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112306-8.0.34 | [112306](https://bugs.mysql.com/bug.php?id=112306) | 8.0.34 | Unexpected Result by JOIN_SUFFIX | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112306-8.0.34.sql) |
| mysql-112319-8.0.34 | [112319](https://bugs.mysql.com/bug.php?id=112319) | 8.0.34 | GROUP_CONCAT with GROUP BY and WHERE clause turns NULL into empty strings. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112345-8.0.34 | [112345](https://bugs.mysql.com/bug.php?id=112345) | 8.0.34 | Contribute by tencent: Repeated subquery plans were printed in format=tree. | 证据不足 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-112345-8.0.34.sql) |
| mysql-112346-8.0.34 | [112346](https://bugs.mysql.com/bug.php?id=112346) | 8.0.34 | MEMBER_OF with multi-valued index on JSON not used in 99% of situations. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112359-8.0.34 | [112359](https://bugs.mysql.com/bug.php?id=112359) | 8.0.34 | Suspicious 'if' condition in get_current_user() | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112362-8.0.34 | [112362](https://bugs.mysql.com/bug.php?id=112362) | 8.0.34 | WHERE NOT IN with subquery is much slower on 8.1 than 5.7 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112364-8.0.34 | [112364](https://bugs.mysql.com/bug.php?id=112364) | 8.0.34 | Create table like doesn't write the charset on binlog if its created from a temp | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112382-8.0.34 | [112382](https://bugs.mysql.com/bug.php?id=112382) | 8.0.34 | Update mysql server with yum/dnf ensures service is always enabled | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112387-8.0.34 | [112387](https://bugs.mysql.com/bug.php?id=112387) | 8.0.34 | Inconsistent results caused by "UNION ALL" with empty subqueries | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112387-8.0.34.sql) |
| mysql-112389-8.0.34 | [112389](https://bugs.mysql.com/bug.php?id=112389) | 8.0.34 | Inconsistent results caused by a subquery in FROM clause | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-112389-8.0.34.sql) |
| mysql-112424-8.0.34 | [112424](https://bugs.mysql.com/bug.php?id=112424) | 8.0.34 | Crash during background rollback if both prepare and active transaction exist | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112439-8.0.34 | [112439](https://bugs.mysql.com/bug.php?id=112439) | 8.0.34 | Incorrect results when using VALUES statement as derived query | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112439-8.0.34.sql) |
| mysql-112446-8.0.34 | [112446](https://bugs.mysql.com/bug.php?id=112446) | 8.0.34 | Fractured read at SERIALIZABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112460-8.0.34 | [112460](https://bugs.mysql.com/bug.php?id=112460) | 8.0.34 | Inconsistent results of SELECT statement with window functions | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112460-8.0.34.sql) |
| mysql-112461-8.0.34 | [112461](https://bugs.mysql.com/bug.php?id=112461) | 8.0.34 | Assertion `!thd->lex->is_exec_started()' failed in /mysql-8.0.34/sql/item_func.c | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112462-8.0.34 | [112462](https://bugs.mysql.com/bug.php?id=112462) | 8.0.34 | Assertion Failure in home/wx/mysql-8.0.34/sql/sql_derived.cc:1641 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112463-8.0.34 | [112463](https://bugs.mysql.com/bug.php?id=112463) | 8.0.34 | MySQL Delete, Insert Lock Occur | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112464-8.0.34 | [112464](https://bugs.mysql.com/bug.php?id=112464) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/handler.cc:7908 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112465-8.0.34 | [112465](https://bugs.mysql.com/bug.php?id=112465) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_table.cc:12188 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112470-8.0.34 | [112470](https://bugs.mysql.com/bug.php?id=112470) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:642 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112475-8.0.34 | [112475](https://bugs.mysql.com/bug.php?id=112475) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_select.cc:2303 | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-112475-8.0.34.sql) |
| mysql-112478-8.0.34 | [112478](https://bugs.mysql.com/bug.php?id=112478) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:524 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112479-8.0.34 | [112479](https://bugs.mysql.com/bug.php?id=112479) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_executor.cc:4222 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112480-8.0.34 | [112480](https://bugs.mysql.com/bug.php?id=112480) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/handler.cc:2966 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112487-8.0.34 | [112487](https://bugs.mysql.com/bug.php?id=112487) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_optimizer.cc:343 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112491-8.0.34 | [112491](https://bugs.mysql.com/bug.php?id=112491) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_subselect.cc:2415 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112494-8.0.34 | [112494](https://bugs.mysql.com/bug.php?id=112494) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_select.cc:4222 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112495-8.0.34 | [112495](https://bugs.mysql.com/bug.php?id=112495) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_optimizer.cc:8930 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112497-8.0.34 | [112497](https://bugs.mysql.com/bug.php?id=112497) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/field.cc:7108 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112498-8.0.34 | [112498](https://bugs.mysql.com/bug.php?id=112498) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_resolver.cc:183 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112499-8.0.34 | [112499](https://bugs.mysql.com/bug.php?id=112499) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_tmp_table.cc:485 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112500-8.0.34 | [112500](https://bugs.mysql.com/bug.php?id=112500) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:4127 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112501-8.0.34 | [112501](https://bugs.mysql.com/bug.php?id=112501) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:784 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112502-8.0.34 | [112502](https://bugs.mysql.com/bug.php?id=112502) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:1598 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112510-8.0.34 | [112510](https://bugs.mysql.com/bug.php?id=112510) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_const_folding.cc:275 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112512-8.0.34 | [112512](https://bugs.mysql.com/bug.php?id=112512) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:9133 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112513-8.0.34 | [112513](https://bugs.mysql.com/bug.php?id=112513) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item.h:2103 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112514-8.0.34 | [112514](https://bugs.mysql.com/bug.php?id=112514) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_lex.cc:2288 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112516-8.0.34 | [112516](https://bugs.mysql.com/bug.php?id=112516) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item.cc:1202 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112517-8.0.34 | [112517](https://bugs.mysql.com/bug.php?id=112517) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item.cc:8044 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112518-8.0.34 | [112518](https://bugs.mysql.com/bug.php?id=112518) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/item_func.cc:1881 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112521-8.0.34 | [112521](https://bugs.mysql.com/bug.php?id=112521) | 8.0.34 | Abort in /mysql-8.0.34/sql/signal_handler.cc:286 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112523-8.0.34 | [112523](https://bugs.mysql.com/bug.php?id=112523) | 8.0.34 | UPDATE/DELETE not using PRIMARY index (even with FORCE INDEX) - causing locks | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112524-8.0.34 | [112524](https://bugs.mysql.com/bug.php?id=112524) | 8.0.34 | Inconsistent results of UNIX_TIMESTAMP with NULLIF and COALESCE | 其他异常 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-112524-8.0.34.sql) |
| mysql-112527-8.0.34 | [112527](https://bugs.mysql.com/bug.php?id=112527) | 8.0.34 | Inconsistent results caused by REPEAT function | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112527-8.0.34.sql) |
| mysql-112541-8.0.34 | [112541](https://bugs.mysql.com/bug.php?id=112541) | 8.0.34 | Incorrect results when using group by loose index scan | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112557-8.0.34 | [112557](https://bugs.mysql.com/bug.php?id=112557) | 8.0.34 | Inconsistent results of SELECT statement with EXISTS clause | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112557-8.0.34.sql) |
| mysql-112579-8.0.34 | [112579](https://bugs.mysql.com/bug.php?id=112579) | 8.0.34 | Inconsistent results of SELECT with <=> and NULLIF | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112589-8.0.34 | [112589](https://bugs.mysql.com/bug.php?id=112589) | 8.0.34 | ER_ROW_IS_REFERENCED vs ER_ROW_IS_REFERENCED_2 breaks backwards compatibility | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112604-8.0.34 | [112604](https://bugs.mysql.com/bug.php?id=112604) | 8.0.34 | Inconsistent and misleading message when ALTER TABLE fills the disk. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112619-8.0.34 | [112619](https://bugs.mysql.com/bug.php?id=112619) | 8.0.34 | STOP GROUP_REPLICATION on primary during ALTER leads to a confusing message. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112621-8.0.34 | [112621](https://bugs.mysql.com/bug.php?id=112621) | 8.0.34 | Performance degradation from 8.0.30 onwards related to performance_schema | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112639-8.0.34 | [112639](https://bugs.mysql.com/bug.php?id=112639) | 8.0.34 | Missing plugin assertion error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112641-8.0.34 | [112641](https://bugs.mysql.com/bug.php?id=112641) | 8.0.34 | ORDER BY does not work with CREATE TEMPORARY TABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112646-8.0.34 | [112646](https://bugs.mysql.com/bug.php?id=112646) | 8.0.34 | Unable to Start MySQL 8.0.33 on CentOS 7.9 (ARM Architecture) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112647-8.0.34 | [112647](https://bugs.mysql.com/bug.php?id=112647) | 8.0.34 | clang-format 17 errors out on .clang-format | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112660-8.0.34 | [112660](https://bugs.mysql.com/bug.php?id=112660) | 8.0.34 | Got error -1 - 'Unknown error -1' from storage engine | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112661-8.0.34 | [112661](https://bugs.mysql.com/bug.php?id=112661) | 8.0.34 | Got 'Unknown error -1' when create index on table | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112661-8.0.34.sql) |
| mysql-112670-8.0.34 | [112670](https://bugs.mysql.com/bug.php?id=112670) | 8.0.34 | Documentation outdated related ANALYZE TABLE locking | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112694-8.0.34 | [112694](https://bugs.mysql.com/bug.php?id=112694) | 8.0.34 | MYSQL master crashes frequently after upgrade from 8.0.28 to 8.0.34 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112698-8.0.34 | [112698](https://bugs.mysql.com/bug.php?id=112698) | 8.0.34 | Assertion failure in Item_func_like::Item_func_like | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112705-8.0.34 | [112705](https://bugs.mysql.com/bug.php?id=112705) | 8.0.34 | sys.schema_table_statistics reset values upon index addition or removal | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112708-8.0.34 | [112708](https://bugs.mysql.com/bug.php?id=112708) | 8.0.34 | INSERT .. DEFAULT broken when when columns are out of order | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112712-8.0.34 | [112712](https://bugs.mysql.com/bug.php?id=112712) | 8.0.34 | Assertion `!null_value &#124;&#124; is_nullable()' failed in MySQL 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112714-8.0.34 | [112714](https://bugs.mysql.com/bug.php?id=112714) | 8.0.34 | Assertion failure: clone0api.cc:1159:ib::fatal in cloning when undo_x_trunc.log | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112717-8.0.34 | [112717](https://bugs.mysql.com/bug.php?id=112717) | 8.0.34 | Undo log truncation does not finalize when super_read_only=1 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112720-8.0.34 | [112720](https://bugs.mysql.com/bug.php?id=112720) | 8.0.34 | Query triggers an assertion Failure in eval_const_cond | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112737-8.0.34 | [112737](https://bugs.mysql.com/bug.php?id=112737) | 8.0.34 | Conditions refering to const table were not added to RANGE SCAN | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112737-8.0.34.sql) |
| mysql-112738-8.0.34 | [112738](https://bugs.mysql.com/bug.php?id=112738) | 8.0.34 | can't truncate partition when partition_id exceed INT_MAX | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112740-8.0.34 | [112740](https://bugs.mysql.com/bug.php?id=112740) | 8.0.34 | startup message when checking tables | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112757-8.0.34 | [112757](https://bugs.mysql.com/bug.php?id=112757) | 8.0.34 | Comparison on FLOAT column return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112759-8.0.34 | [112759](https://bugs.mysql.com/bug.php?id=112759) | 8.0.34 | Calculation on DOUBLE column return wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112766-8.0.34 | [112766](https://bugs.mysql.com/bug.php?id=112766) | 8.0.34 | Feature req: SOURCE_SSL should default to 1 for replication | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112767-8.0.34 | [112767](https://bugs.mysql.com/bug.php?id=112767) | 8.0.34 | SELECT COUNT(*) degraded performance on 8.0 compared to 5.7 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112768-8.0.34 | [112768](https://bugs.mysql.com/bug.php?id=112768) | 8.0.34 | Inconsistent results when tables are JOINed in a different order | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112770-8.0.34 | [112770](https://bugs.mysql.com/bug.php?id=112770) | 8.0.34 | Assertion `!thd->is_error()' failed in MySQL 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112772-8.0.34 | [112772](https://bugs.mysql.com/bug.php?id=112772) | 8.0.34 | Assertion `is_nullable()' failed in MySQL 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112773-8.0.34 | [112773](https://bugs.mysql.com/bug.php?id=112773) | 8.0.34 | Primary key based query reading more number of pages in 8.0 compared to 5.7 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112780-8.0.34 | [112780](https://bugs.mysql.com/bug.php?id=112780) | 8.0.34 | innodb_temp_data_file_path changed from relative to absolute path in 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112787-8.0.34 | [112787](https://bugs.mysql.com/bug.php?id=112787) | 8.0.34 | regexp/rlike function in routines extreme regression mysql 5.7 to mysql 8 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112798-8.0.34 | [112798](https://bugs.mysql.com/bug.php?id=112798) | 8.0.34 | The configuration value of innodb_buffer_pool_size underflow | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112800-8.0.34 | [112800](https://bugs.mysql.com/bug.php?id=112800) | 8.0.34 | New table are reported as existing in mysql | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112802-8.0.34 | [112802](https://bugs.mysql.com/bug.php?id=112802) | 8.0.34 | Inconsistent results when using INDEX | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112824-8.0.34 | [112824](https://bugs.mysql.com/bug.php?id=112824) | 8.0.34 | Different processing of WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS by INNODB and MYISAM | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112826-8.0.34 | [112826](https://bugs.mysql.com/bug.php?id=112826) | 8.0.34 | Decimal query with wrong result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112873-8.0.34 | [112873](https://bugs.mysql.com/bug.php?id=112873) | 8.0.34 | Locked account is not shown in mysql.user | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112982-8.0.34 | [112982](https://bugs.mysql.com/bug.php?id=112982) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:558 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112983-8.0.34 | [112983](https://bugs.mysql.com/bug.php?id=112983) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:7731 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113036-8.0.34 | [113036](https://bugs.mysql.com/bug.php?id=113036) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/field.cc:4318 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113037-8.0.34 | [113037](https://bugs.mysql.com/bug.php?id=113037) | 8.0.34 | Assertion Failure in /mysql-8.0.34/sql/my_decimal.h:186 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113175-8.0.34 | [113175](https://bugs.mysql.com/bug.php?id=113175) | 8.0.34 | Getting wrong result for locked rows | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113219-8.0.34 | [113219](https://bugs.mysql.com/bug.php?id=113219) | 8.0.34 | Wrong value of auto_increment while executing load data replace | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113256-8.0.34 | [113256](https://bugs.mysql.com/bug.php?id=113256) | 8.0.34 | DATA_FREE displayed wrong when checking "PARTITIONS" table | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113338-8.0.34 | [113338](https://bugs.mysql.com/bug.php?id=113338) | 8.0.34 | return error result with a qubquery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113369-8.0.34 | [113369](https://bugs.mysql.com/bug.php?id=113369) | 8.0.34 | In the hash partition table, the query result is error. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113410-8.0.34 | [113410](https://bugs.mysql.com/bug.php?id=113410) | 8.0.34 | hang creating InnoDB Cluster | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113430-8.0.34 | [113430](https://bugs.mysql.com/bug.php?id=113430) | 8.0.34 | Query slowness in Delete query with many child table | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113431-8.0.34 | [113431](https://bugs.mysql.com/bug.php?id=113431) | 8.0.34 | Metadata locking - Table creation with FK constraint | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113437-8.0.34 | [113437](https://bugs.mysql.com/bug.php?id=113437) | 8.0.34 | connection is not established with server can do anything in sql bench | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113466-8.0.34 | [113466](https://bugs.mysql.com/bug.php?id=113466) | 8.0.34 | MySQL provides Truncated incorrect DOUBLE value: '0A000' error in trigger | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113548-8.0.34 | [113548](https://bugs.mysql.com/bug.php?id=113548) | 8.0.34 | Cloning failing in Mysql Group replication | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113694-8.0.34 | [113694](https://bugs.mysql.com/bug.php?id=113694) | 8.0.34 | misleading error message comparing a spatial column with numeric using < or such | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113819-8.0.34 | [113819](https://bugs.mysql.com/bug.php?id=113819) | 8.0.34 | when use show engine innodb cannot show correct information | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114255-8.0.34 | [114255](https://bugs.mysql.com/bug.php?id=114255) | 8.0.34 | Install Community Edition 8.0.34/35glibc2.28-arm Version error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114434-8.0.34 | [114434](https://bugs.mysql.com/bug.php?id=114434) | 8.0.34 | Passwords in mysql.slave_master_info should be encrypted | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114629-8.0.34 | [114629](https://bugs.mysql.com/bug.php?id=114629) | 8.0.34 | partially upgraded DD | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114650-8.0.34 | [114650](https://bugs.mysql.com/bug.php?id=114650) | 8.0.34 | The prepare statement execution result is wrong, but there is data output | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114694-8.0.34 | [114694](https://bugs.mysql.com/bug.php?id=114694) | 8.0.34 | binlog_transaction_compression not effect on slave | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114792-8.0.34 | [114792](https://bugs.mysql.com/bug.php?id=114792) | 8.0.34 | Gettin erroe while using run my sql script | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115035-8.0.34 | [115035](https://bugs.mysql.com/bug.php?id=115035) | 8.0.34 | View with ORDER BY misses a row | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115085-8.0.34 | [115085](https://bugs.mysql.com/bug.php?id=115085) | 8.0.34 | INDEX using CAST (json_column) AS ARRAY drops rows containing empty array | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115216-8.0.34 | [115216](https://bugs.mysql.com/bug.php?id=115216) | 8.0.34 | range_optimizer_max_mem_size calculation on with large IN queries | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115259-8.0.34 | [115259](https://bugs.mysql.com/bug.php?id=115259) | 8.0.34 | query_rewrite not working in 8.0.34 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115459-8.0.34 | [115459](https://bugs.mysql.com/bug.php?id=115459) | 8.0.34 | global read_only = 1 with read only = 0 on schema level blocks writes to schema | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115464-8.0.34 | [115464](https://bugs.mysql.com/bug.php?id=115464) | 8.0.34 | Cannot connect to server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115542-8.0.34 | [115542](https://bugs.mysql.com/bug.php?id=115542) | 8.0.34 | MY-012872 MySQL Issues crash on long running large table update | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115808-8.0.34 | [115808](https://bugs.mysql.com/bug.php?id=115808) | 8.0.34 | Simple "comment" change operation in partition table should be treat as Metadata | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116430-8.0.34 | [116430](https://bugs.mysql.com/bug.php?id=116430) | 8.0.34 | Concurrent DELETE statements of different rows causing deadlocking | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116852-8.0.34 | [116852](https://bugs.mysql.com/bug.php?id=116852) | 8.0.34 | Difference between JSONPath "$" vs "$[*]" | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-116852-8.0.34.sql) |
| mysql-116983-8.0.34 | [116983](https://bugs.mysql.com/bug.php?id=116983) | 8.0.34 | Master's binary log didn't apply data but write to slave's binary log | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117069-8.0.34 | [117069](https://bugs.mysql.com/bug.php?id=117069) | 8.0.34 | The slave recorded the master's binary log into the binary log without applying it to the data | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117102-8.0.34 | [117102](https://bugs.mysql.com/bug.php?id=117102) | 8.0.34 | Histogram Statistics Analysis cannot apply on standby database | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117337-8.0.34 | [117337](https://bugs.mysql.com/bug.php?id=117337) | 8.0.34 | Transaction Commit Allowed on Blackhole Table After read_only=1 is Enabled | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117419-8.0.34 | [117419](https://bugs.mysql.com/bug.php?id=117419) | 8.0.34 | BEFORE INSERT trigger causes all columns in DEFAULT value expression to be NULL | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117646-8.0.34 | [117646](https://bugs.mysql.com/bug.php?id=117646) | 8.0.34 | InnoDB Purge Process Inefficiency on Idle Serve | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117670-8.0.34 | [117670](https://bugs.mysql.com/bug.php?id=117670) | 8.0.34 | Unknown column '?' in 'group statement' | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118936-8.0.34 | [118936](https://bugs.mysql.com/bug.php?id=118936) | 8.0.34 | Root password | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119807-8.0.34 | [119807](https://bugs.mysql.com/bug.php?id=119807) | 8.0.34 | Generated default values bypass BLOB/TEXT/JSON default value restriction | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119908-8.0.34 | [119908](https://bugs.mysql.com/bug.php?id=119908) | 8.0.34 | GROUP_CONCAT returns corrupted characters when column charset is utf8mb4 and connection charset is gbk | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120974-8.0.34 | [120974](https://bugs.mysql.com/bug.php?id=120974) | 8.0.34 | Client connection kill command doesn't kill process | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-68925-8.0.35 | [68925](https://bugs.mysql.com/bug.php?id=68925) | 8.0.35 | Compatibility issue with mysql history ("\040" instead of space) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-109155-8.0.35 | [109155](https://bugs.mysql.com/bug.php?id=109155) | 8.0.35 | Invalid scan on left join tables of which columns not in distinct output fields | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112767-8.0.35 | [112767](https://bugs.mysql.com/bug.php?id=112767) | 8.0.35 | SELECT COUNT(*) degraded performance on 8.0 compared to 5.7 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112873-8.0.35 | [112873](https://bugs.mysql.com/bug.php?id=112873) | 8.0.35 | Locked account is not shown in mysql.user | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112902-8.0.35 | [112902](https://bugs.mysql.com/bug.php?id=112902) | 8.0.35 | Optimizer in MySQL 8 is significantly slower on dependent subqueries than 5.7 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112907-8.0.35 | [112907](https://bugs.mysql.com/bug.php?id=112907) | 8.0.35 | Assertion `to->field_ptr() != from->field_ptr()' failed in MySQL 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112910-8.0.35 | [112910](https://bugs.mysql.com/bug.php?id=112910) | 8.0.35 | Incorrect results when add an uncorrelated row | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112910-8.0.35.sql) |
| mysql-112911-8.0.35 | [112911](https://bugs.mysql.com/bug.php?id=112911) | 8.0.35 | Inconsistent results when using PRIMARY and DUPSWEEDOUT | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-112911-8.0.35.sql) |
| mysql-112915-8.0.35 | [112915](https://bugs.mysql.com/bug.php?id=112915) | 8.0.35 | CTE double materialization issue | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112935-8.0.35 | [112935](https://bugs.mysql.com/bug.php?id=112935) | 8.0.35 | Different Behaviour Seen Between MyISAM and MEMORY Engine | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112946-8.0.35 | [112946](https://bugs.mysql.com/bug.php?id=112946) | 8.0.35 | INSTANT algo <= 8028 on table in mysql schema leads to corruption post upgrade | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112951-8.0.35 | [112951](https://bugs.mysql.com/bug.php?id=112951) | 8.0.35 | Assertion `fixed' failed in MySQL 8.1.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112964-8.0.35 | [112964](https://bugs.mysql.com/bug.php?id=112964) | 8.0.35 | SELECT COUNT is slow with O_DIRECT | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112979-8.0.35 | [112979](https://bugs.mysql.com/bug.php?id=112979) | 8.0.35 | binlog_transaction_compression_level_zstd bug not fixed in 8.0.35 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112982-8.0.35 | [112982](https://bugs.mysql.com/bug.php?id=112982) | 8.0.35 | Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:558 | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-112983-8.0.35 | [112983](https://bugs.mysql.com/bug.php?id=112983) | 8.0.35 | Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:7731 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113002-8.0.35 | [113002](https://bugs.mysql.com/bug.php?id=113002) | 8.0.35 | innodb.ddl_kill test fails sporadically. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113015-8.0.35 | [113015](https://bugs.mysql.com/bug.php?id=113015) | 8.0.35 | REGEXP curly brackets without escape character works on 5.7 but not in 8.0 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113036-8.0.35 | [113036](https://bugs.mysql.com/bug.php?id=113036) | 8.0.35 | Assertion Failure in /mysql-8.0.34/sql/field.cc:4318 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113037-8.0.35 | [113037](https://bugs.mysql.com/bug.php?id=113037) | 8.0.35 | Assertion Failure in /mysql-8.0.34/sql/my_decimal.h:186 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113046-8.0.35 | [113046](https://bugs.mysql.com/bug.php?id=113046) | 8.0.35 | MTR tests for SELECT fail with ICP, MRR, possibly other flags | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113047-8.0.35 | [113047](https://bugs.mysql.com/bug.php?id=113047) | 8.0.35 | MTR test main.derived_limit fails with small cost differences | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113048-8.0.35 | [113048](https://bugs.mysql.com/bug.php?id=113048) | 8.0.35 | MTR test gis.gis_bugs_crashes fails with a result difference | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113049-8.0.35 | [113049](https://bugs.mysql.com/bug.php?id=113049) | 8.0.35 | MTR test json.array_index fails with a result difference | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113051-8.0.35 | [113051](https://bugs.mysql.com/bug.php?id=113051) | 8.0.35 | Skip instant DDL for empty tables to save row versions | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113056-8.0.35 | [113056](https://bugs.mysql.com/bug.php?id=113056) | 8.0.35 | crashing when giving pwd/not able install again so cannot configure pwd | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113097-8.0.35 | [113097](https://bugs.mysql.com/bug.php?id=113097) | 8.0.35 | query bug racecondition | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113097-8.0.35.sql) |
| mysql-113112-8.0.35 | [113112](https://bugs.mysql.com/bug.php?id=113112) | 8.0.35 | External dependency ext::zlib leads to -lzlib, but shall lead to -lz | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113154-8.0.35 | [113154](https://bugs.mysql.com/bug.php?id=113154) | 8.0.35 | Join using ROW_NUMBER() returns incorrect records | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113154-8.0.35.sql) |
| mysql-113167-8.0.35 | [113167](https://bugs.mysql.com/bug.php?id=113167) | 8.0.35 | After creating the spatial index, ST_Disjoint gives the incorrect answer | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113171-8.0.35 | [113171](https://bugs.mysql.com/bug.php?id=113171) | 8.0.35 | sum(distinct substring()) does not give warnings, while sum(substring() does | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113171-8.0.35.sql) |
| mysql-113173-8.0.35 | [113173](https://bugs.mysql.com/bug.php?id=113173) | 8.0.35 | Crash when using --batch in MySQL command client | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113176-8.0.35 | [113176](https://bugs.mysql.com/bug.php?id=113176) | 8.0.35 | Unexpected errors caused by check constraints | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113176-8.0.35.sql) |
| mysql-113178-8.0.35 | [113178](https://bugs.mysql.com/bug.php?id=113178) | 8.0.35 | Temptable engine leads to performance degradation | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113180-8.0.35 | [113180](https://bugs.mysql.com/bug.php?id=113180) | 8.0.35 | Unexpected Results when Using Math Function SIN | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113180-8.0.35.sql) |
| mysql-113185-8.0.35 | [113185](https://bugs.mysql.com/bug.php?id=113185) | 8.0.35 | Unexpected Results when using NULLIF Function in Filter | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113202-8.0.35 | [113202](https://bugs.mysql.com/bug.php?id=113202) | 8.0.35 | p_s.processlist table does not contain async replica threads after restart | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113205-8.0.35 | [113205](https://bugs.mysql.com/bug.php?id=113205) | 8.0.35 | After swapping the X and Y coordinates, ST_Crosses gives the incorrect answer. | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113206-8.0.35 | [113206](https://bugs.mysql.com/bug.php?id=113206) | 8.0.35 | BIT_OR returns erroneous values | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113207-8.0.35 | [113207](https://bugs.mysql.com/bug.php?id=113207) | 8.0.35 | Potential bug in ST_Contains | 其他异常 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113207-8.0.35.sql) |
| mysql-113208-8.0.35 | [113208](https://bugs.mysql.com/bug.php?id=113208) | 8.0.35 | IMPORT TABLESPACE not friendly with multi-byte characters | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113211-8.0.35 | [113211](https://bugs.mysql.com/bug.php?id=113211) | 8.0.35 | The latest version 8.0 returns abnormal results for complex queries | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113211-8.0.35.sql) |
| mysql-113236-8.0.35 | [113236](https://bugs.mysql.com/bug.php?id=113236) | 8.0.35 | conflicting replica_parallel_workers spec causes parallel_mode misconfig | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113248-8.0.35 | [113248](https://bugs.mysql.com/bug.php?id=113248) | 8.0.35 | Execute alter table heap-use-after-free | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113270-8.0.35 | [113270](https://bugs.mysql.com/bug.php?id=113270) | 8.0.35 | Unable to compile 8.0.35 with DISABLE_PSI_THREAD | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113293-8.0.35 | [113293](https://bugs.mysql.com/bug.php?id=113293) | 8.0.35 | Create table like assertion error | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113298-8.0.35 | [113298](https://bugs.mysql.com/bug.php?id=113298) | 8.0.35 | Unexpected Results when Using IN for Floating-Point | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113298-8.0.35.sql) |
| mysql-113301-8.0.35 | [113301](https://bugs.mysql.com/bug.php?id=113301) | 8.0.35 | using preparation statement to query the time type data, some data is not found | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113301-8.0.35.sql) |
| mysql-113302-8.0.35 | [113302](https://bugs.mysql.com/bug.php?id=113302) | 8.0.35 | Unexpected Result for an Index | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113302-8.0.35.sql) |
| mysql-113303-8.0.35 | [113303](https://bugs.mysql.com/bug.php?id=113303) | 8.0.35 | Explain plan takes forever when there are more joins | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113304-8.0.35 | [113304](https://bugs.mysql.com/bug.php?id=113304) | 8.0.35 | Unexpected Result for LEAST function | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-113304-8.0.35.sql) |
| mysql-113312-8.0.35 | [113312](https://bugs.mysql.com/bug.php?id=113312) | 8.0.35 | Server stall during Alter/Drop table while clearing AHIs from the buffer pool | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113316-8.0.35 | [113316](https://bugs.mysql.com/bug.php?id=113316) | 8.0.35 | When the bit type has an index, the query result is incorrect. | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113316-8.0.35.sql) |
| mysql-113317-8.0.35 | [113317](https://bugs.mysql.com/bug.php?id=113317) | 8.0.35 | Unexpected Result by IF | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113318-8.0.35 | [113318](https://bugs.mysql.com/bug.php?id=113318) | 8.0.35 | unnest scalar subquery using groupby produces wrong result | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113319-8.0.35 | [113319](https://bugs.mysql.com/bug.php?id=113319) | 8.0.35 | unnesting scalar subquery containing count and having cond produces wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113319-8.0.35.sql) |
| mysql-113338-8.0.35 | [113338](https://bugs.mysql.com/bug.php?id=113338) | 8.0.35 | return error result with a qubquery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113347-8.0.35 | [113347](https://bugs.mysql.com/bug.php?id=113347) | 8.0.35 | The merge threshold for index pages is case-sensitive | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113352-8.0.35 | [113352](https://bugs.mysql.com/bug.php?id=113352) | 8.0.35 | User cancel operation times out when stored procedure has multiple SLEEP() calls | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113358-8.0.35 | [113358](https://bugs.mysql.com/bug.php?id=113358) | 8.0.35 | Wrong functional dependency in ONLY_FULL_GROUP_BY mode | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113358-8.0.35.sql) |
| mysql-113366-8.0.35 | [113366](https://bugs.mysql.com/bug.php?id=113366) | 8.0.35 | Incorrect query results involving the date type. | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113369-8.0.35 | [113369](https://bugs.mysql.com/bug.php?id=113369) | 8.0.35 | In the hash partition table, the query result is error. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113387-8.0.35 | [113387](https://bugs.mysql.com/bug.php?id=113387) | 8.0.35 | update with 'and' 'or' causes unexpected behavior | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113405-8.0.35 | [113405](https://bugs.mysql.com/bug.php?id=113405) | 8.0.35 | 'covering index' is not shown entirely in EXPLAIN FORMAT=TREE. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113415-8.0.35 | [113415](https://bugs.mysql.com/bug.php?id=113415) | 8.0.35 | Unknown column, but can get query result in CTE. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113423-8.0.35 | [113423](https://bugs.mysql.com/bug.php?id=113423) | 8.0.35 | Unexpected result appeared | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113424-8.0.35 | [113424](https://bugs.mysql.com/bug.php?id=113424) | 8.0.35 | Unexpected result appeared | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113425-8.0.35 | [113425](https://bugs.mysql.com/bug.php?id=113425) | 8.0.35 | Unexpected result appeared | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113433-8.0.35 | [113433](https://bugs.mysql.com/bug.php?id=113433) | 8.0.35 | Incorrect query results involving the date type. | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113433-8.0.35.sql) |
| mysql-113439-8.0.35 | [113439](https://bugs.mysql.com/bug.php?id=113439) | 8.0.35 | Alter database charset lead to cpu high load | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113440-8.0.35 | [113440](https://bugs.mysql.com/bug.php?id=113440) | 8.0.35 | Table spaces with instant_col information can no longer be imported | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113474-8.0.35 | [113474](https://bugs.mysql.com/bug.php?id=113474) | 8.0.35 | mysql 8.0.35 suddenly has become extremely slow | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113482-8.0.35 | [113482](https://bugs.mysql.com/bug.php?id=113482) | 8.0.35 | innodb_parallel_read_threads>1 makes simple select count more expensive | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113485-8.0.35 | [113485](https://bugs.mysql.com/bug.php?id=113485) | 8.0.35 | Let innodb_dedicated_server set innodb_log_writer_threads based on server size | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113505-8.0.35 | [113505](https://bugs.mysql.com/bug.php?id=113505) | 8.0.35 | Performance schema counter increments make parallel index create slow | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113506-8.0.35 | [113506](https://bugs.mysql.com/bug.php?id=113506) | 8.0.35 | Item_func_conv_charset::eq not correct | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113506-8.0.35.sql) |
| mysql-113507-8.0.35 | [113507](https://bugs.mysql.com/bug.php?id=113507) | 8.0.35 | gipk add column failed | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113514-8.0.35 | [113514](https://bugs.mysql.com/bug.php?id=113514) | 8.0.35 | JSON_OBJECT changes order of keys in output | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113516-8.0.35 | [113516](https://bugs.mysql.com/bug.php?id=113516) | 8.0.35 | rejoin cluster failure as clone plugin is waiting for table metadata lock | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113518-8.0.35 | [113518](https://bugs.mysql.com/bug.php?id=113518) | 8.0.35 | character set with Chinese character,using storage procedure it report 1300 err | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113524-8.0.35 | [113524](https://bugs.mysql.com/bug.php?id=113524) | 8.0.35 | Value in ibuf bitmap page of R-Tree could be incorrect after recovery | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113527-8.0.35 | [113527](https://bugs.mysql.com/bug.php?id=113527) | 8.0.35 | Hash Sum mismatch | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113528-8.0.35 | [113528](https://bugs.mysql.com/bug.php?id=113528) | 8.0.35 | Error installing the server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113531-8.0.35 | [113531](https://bugs.mysql.com/bug.php?id=113531) | 8.0.35 | the convert function seems not work as expected | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113532-8.0.35 | [113532](https://bugs.mysql.com/bug.php?id=113532) | 8.0.35 | Compatibility issue with mysql history ("\040" instead of space) | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113534-8.0.35 | [113534](https://bugs.mysql.com/bug.php?id=113534) | 8.0.35 | table join return Unexpected result when drived table using include join index | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113534-8.0.35.sql) |
| mysql-113535-8.0.35 | [113535](https://bugs.mysql.com/bug.php?id=113535) | 8.0.35 | Drop table in background list will remain file exists in directory | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113536-8.0.35 | [113536](https://bugs.mysql.com/bug.php?id=113536) | 8.0.35 | A character set error is reported when a stored procedure is used. | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113557-8.0.35 | [113557](https://bugs.mysql.com/bug.php?id=113557) | 8.0.35 | Wrong query result on composite multi-valued index + empty array value | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113557-8.0.35.sql) |
| mysql-113562-8.0.35 | [113562](https://bugs.mysql.com/bug.php?id=113562) | 8.0.35 | COLLATION behaves differently if set on CREATE TABLE vs ALTER TABLE | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113578-8.0.35 | [113578](https://bugs.mysql.com/bug.php?id=113578) | 8.0.35 | AVG calculation bug | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113595-8.0.35 | [113595](https://bugs.mysql.com/bug.php?id=113595) | 8.0.35 | Incorrect query result of function TIMESTAMPADD | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113597-8.0.35 | [113597](https://bugs.mysql.com/bug.php?id=113597) | 8.0.35 | Data Dictionary issues when dropping multiple FTS indexes | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113598-8.0.35 | [113598](https://bugs.mysql.com/bug.php?id=113598) | 8.0.35 | Please consider adding GTID in "Timeout waiting for reply". | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113639-8.0.35 | [113639](https://bugs.mysql.com/bug.php?id=113639) | 8.0.35 | Crash when executes test case main.default_as_expr in debug with ps-protocol | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113647-8.0.35 | [113647](https://bugs.mysql.com/bug.php?id=113647) | 8.0.35 | identical tables are checked in HashJoin because of no STOP_AT_MATERIALIZATION | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113649-8.0.35 | [113649](https://bugs.mysql.com/bug.php?id=113649) | 8.0.35 | the result of format function truncated when using cursor | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113649-8.0.35.sql) |
| mysql-113706-8.0.35 | [113706](https://bugs.mysql.com/bug.php?id=113706) | 8.0.35 | InnoDB : Corruption of an index tree which stopped mysqld service | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113718-8.0.35 | [113718](https://bugs.mysql.com/bug.php?id=113718) | 8.0.35 | left join + semijoin + materialization finds false matches | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113730-8.0.35 | [113730](https://bugs.mysql.com/bug.php?id=113730) | 8.0.35 | Unable to connect to MySQL 5.1 database server with MySQL 8 client | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113768-8.0.35 | [113768](https://bugs.mysql.com/bug.php?id=113768) | 8.0.35 | return error with cast | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-113768-8.0.35.sql) |
| mysql-113831-8.0.35 | [113831](https://bugs.mysql.com/bug.php?id=113831) | 8.0.35 | mysql crashes ramdonally during backup | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113839-8.0.35 | [113839](https://bugs.mysql.com/bug.php?id=113839) | 8.0.35 | Cannot elect a new PRIMARY when async connection failover is in use | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113879-8.0.35 | [113879](https://bugs.mysql.com/bug.php?id=113879) | 8.0.35 | An error is reported when the user variable character set is used in the stored | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-113978-8.0.35 | [113978](https://bugs.mysql.com/bug.php?id=113978) | 8.0.35 | Set admin_port in port being used does not throw error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114021-8.0.35 | [114021](https://bugs.mysql.com/bug.php?id=114021) | 8.0.35 | mysqldump --replace produces *some* REPLACE IGNORE statements | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114058-8.0.35 | [114058](https://bugs.mysql.com/bug.php?id=114058) | 8.0.35 | The return value of the CAST(... AS UNSIGNED) expression is out of range. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114072-8.0.35 | [114072](https://bugs.mysql.com/bug.php?id=114072) | 8.0.35 | Group replication slow down existing asynchronous replication | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114125-8.0.35 | [114125](https://bugs.mysql.com/bug.php?id=114125) | 8.0.35 | Parameter set by SET PERSIST is not set to replication threads when restart | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114196-8.0.35 | [114196](https://bugs.mysql.com/bug.php?id=114196) | 8.0.35 | Incorrect query result caused by comparing decimal and float type value | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114196-8.0.35.sql) |
| mysql-114198-8.0.35 | [114198](https://bugs.mysql.com/bug.php?id=114198) | 8.0.35 | Using PERSIST on binlog_transaction_compression partially compresses binary log | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114255-8.0.35 | [114255](https://bugs.mysql.com/bug.php?id=114255) | 8.0.35 | Install Community Edition 8.0.34/35glibc2.28-arm Version error | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114319-8.0.35 | [114319](https://bugs.mysql.com/bug.php?id=114319) | 8.0.35 | [FEATURE] Support 4k ReplicationPassword | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114342-8.0.35 | [114342](https://bugs.mysql.com/bug.php?id=114342) | 8.0.35 | Failed to convert the character string when executing the selection statement. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114378-8.0.35 | [114378](https://bugs.mysql.com/bug.php?id=114378) | 8.0.35 | Incorrect query result caused by CONVERT_TZ | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-114378-8.0.35.sql) |
| mysql-114379-8.0.35 | [114379](https://bugs.mysql.com/bug.php?id=114379) | 8.0.35 | Incorrect query result caused by index and optimizer | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114380-8.0.35 | [114380](https://bugs.mysql.com/bug.php?id=114380) | 8.0.35 | Incorrect query result may caused by TIMESTAMP | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114380-8.0.35.sql) |
| mysql-114381-8.0.35 | [114381](https://bugs.mysql.com/bug.php?id=114381) | 8.0.35 | Incorrect query result may caused by EXISTS and TIMEDIFF | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114381-8.0.35.sql) |
| mysql-114382-8.0.35 | [114382](https://bugs.mysql.com/bug.php?id=114382) | 8.0.35 | Incorrect query result may caused by LOW_PRIORITY | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-114382-8.0.35.sql) |
| mysql-114383-8.0.35 | [114383](https://bugs.mysql.com/bug.php?id=114383) | 8.0.35 | Incorrect query result may caused by DATE and window function | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114384-8.0.35 | [114384](https://bugs.mysql.com/bug.php?id=114384) | 8.0.35 | Incorrect query result may caused by LOG | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114384-8.0.35.sql) |
| mysql-114396-8.0.35 | [114396](https://bugs.mysql.com/bug.php?id=114396) | 8.0.35 | NULL is not treated as 0 for tables partitioned by key | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114475-8.0.35 | [114475](https://bugs.mysql.com/bug.php?id=114475) | 8.0.35 | COUNT(1) vs SUM of partial counts | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114525-8.0.35 | [114525](https://bugs.mysql.com/bug.php?id=114525) | 8.0.35 | log_first_rec_group failed | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114545-8.0.35 | [114545](https://bugs.mysql.com/bug.php?id=114545) | 8.0.35 | performance_schema.processlist tuncates query info | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114550-8.0.35 | [114550](https://bugs.mysql.com/bug.php?id=114550) | 8.0.35 | ROUND(1.2345, 2) and ROUND(1.2345, @TWO) unexpected different results | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114570-8.0.35 | [114570](https://bugs.mysql.com/bug.php?id=114570) | 8.0.35 | Error running mysqldump with tables with big blobs on docker | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114580-8.0.35 | [114580](https://bugs.mysql.com/bug.php?id=114580) | 8.0.35 | Mysql 8.0.35 - The query to get foreign keys are slower than MySQL 8.0.20 | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114775-8.0.35 | [114775](https://bugs.mysql.com/bug.php?id=114775) | 8.0.35 | Outer join condition filtering bug when using scalar subquery | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114775-8.0.35.sql) |
| mysql-114783-8.0.35 | [114783](https://bugs.mysql.com/bug.php?id=114783) | 8.0.35 | Backward scan partition table with multi-valued Indexes may lost some result. | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-114917-8.0.35 | [114917](https://bugs.mysql.com/bug.php?id=114917) | 8.0.35 | Incorrect query result | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-114917-8.0.35.sql) |
| mysql-115220-8.0.35 | [115220](https://bugs.mysql.com/bug.php?id=115220) | 8.0.35 | some assert should not been trigger when innodb_force_recovery is set | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115294-8.0.35 | [115294](https://bugs.mysql.com/bug.php?id=115294) | 8.0.35 | partition table's io wait summary not correct in PERFORMANCE_SCHEMA | 报告现象已复现 | 前版同异常 | [SQL](sql/executed_125/mysql-115294-8.0.35.sql) |
| mysql-115354-8.0.35 | [115354](https://bugs.mysql.com/bug.php?id=115354) | 8.0.35 | MySQL installation fails due to internet connectivity | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115470-8.0.35 | [115470](https://bugs.mysql.com/bug.php?id=115470) | 8.0.35 | The precision of avg () is lost when multiple tables are joined. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115726-8.0.35 | [115726](https://bugs.mysql.com/bug.php?id=115726) | 8.0.35 | A left join with an impossible condition cause unexpected result | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115762-8.0.35 | [115762](https://bugs.mysql.com/bug.php?id=115762) | 8.0.35 | SIGILL in precmd routine with FreeBSD 14.1 on Raspberry Pi 3B+ with latest | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115766-8.0.35 | [115766](https://bugs.mysql.com/bug.php?id=115766) | 8.0.35 | Database page corruption on disk or a failed file read of page | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-115811-8.0.35 | [115811](https://bugs.mysql.com/bug.php?id=115811) | 8.0.35 | Replication Delay consistent at 1 second. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116001-8.0.35 | [116001](https://bugs.mysql.com/bug.php?id=116001) | 8.0.35 | Issue: Inconsistent Timestamp Values After Import | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116058-8.0.35 | [116058](https://bugs.mysql.com/bug.php?id=116058) | 8.0.35 | row_examined in slowlog is not correct when using index_merge | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116834-8.0.35 | [116834](https://bugs.mysql.com/bug.php?id=116834) | 8.0.35 | Replication between MySQL 8.0.35 (master) and MySQL 5.7.44 (slave) fails due to an incompatibility with character sets. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-116864-8.0.35 | [116864](https://bugs.mysql.com/bug.php?id=116864) | 8.0.35 | Index corruption | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117273-8.0.35 | [117273](https://bugs.mysql.com/bug.php?id=117273) | 8.0.35 | some sort is not optimized away by index, if index have part of primary key | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117409-8.0.35 | [117409](https://bugs.mysql.com/bug.php?id=117409) | 8.0.35 | join with crosse table sort is not optimized away by index | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117424-8.0.35 | [117424](https://bugs.mysql.com/bug.php?id=117424) | 8.0.35 | InnoDB Cluster with group_replication_paxos_single_leader=ON unable to process write traffic | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-117598-8.0.35 | [117598](https://bugs.mysql.com/bug.php?id=117598) | 8.0.35 | Wrong sort order for queries with ORDER BY DESC when using range comparison with LIMIT | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118177-8.0.35 | [118177](https://bugs.mysql.com/bug.php?id=118177) | 8.0.35 | Unnecessary filter operator in the execution plan | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118653-8.0.35 | [118653](https://bugs.mysql.com/bug.php?id=118653) | 8.0.35 | The threads waiting for the MDL lock and the threads holding the lock are the same | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118856-8.0.35 | [118856](https://bugs.mysql.com/bug.php?id=118856) | 8.0.35 | json_objectagg throws inappropriate "no null member names" error in unreachable case. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-118957-8.0.35 | [118957](https://bugs.mysql.com/bug.php?id=118957) | 8.0.35 | Documentation says you can use a HEX value for ALTER user passwords, but you can't. | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119436-8.0.35 | [119436](https://bugs.mysql.com/bug.php?id=119436) | 8.0.35 | User Privileges are Missed On Replica Server | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119441-8.0.35 | [119441](https://bugs.mysql.com/bug.php?id=119441) | 8.0.35 | Group replication binds to ipv6 wildcard address | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119796-8.0.35 | [119796](https://bugs.mysql.com/bug.php?id=119796) | 8.0.35 | Encrypted data changes when adding columns | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119859-8.0.35 | [119859](https://bugs.mysql.com/bug.php?id=119859) | 8.0.35 | Inconsistent Query Results Between Partitioned and Non-Partitioned Tables | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-119945-8.0.35 | [119945](https://bugs.mysql.com/bug.php?id=119945) | 8.0.35 | Inconsistent result set on repeated execution of NATURAL JOIN with expression index and KEY partitioning | 执行失败 | 未进入相邻版本集合 | [SQL](sql/executed_125/mysql-119945-8.0.35.sql) |
| mysql-119965-8.0.35 | [119965](https://bugs.mysql.com/bug.php?id=119965) | 8.0.35 | The results of the same query statement are inconsistent when it is executed multiple times. | not_executed | 未进入相邻版本集合 | 未执行；本次未导出 SQL |
| mysql-120437-8.0.35 | [120437](https://bugs.mysql.com/bug.php?id=120437) | 8.0.35 | information_schema.partitions returns UINT64_MAX (18446744073709551615) for DATA_LENGTH of partition dropped during conc | 证据不足 | 未进入相邻版本集合 | 未执行；本次未导出 SQL |

## 逐项内容

### mysql-98083-8.0.32 · Bug #98083

Restarting the computer when deleting the database will cause directory residues

官方版本字段：8.0.16, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #98083](https://bugs.mysql.com/bug.php?id=98083)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Reproducer requires injecting abort() into mysql_rm_db or a controlled host restart during DROP DATABASE. Need target-source instrumented build and isolated crash/restart protocol; ordinary SQL is incomplete.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-101262-8.0.32 · Bug #101262

performance_schema.binary_log_transaction_compression_stats timestamps

官方版本字段：8.0.21, 8.0.32

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #101262](https://bugs.mysql.com/bug.php?id=101262)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain明确触发条件未知，仅提供现有RELAY压缩统计的未来时间戳；需复制源/从拓扑及生成relay事务步骤、日志时间基准，单实例空表查询不能复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-106225-8.0.32 · Bug #106225

select bin("") should return 0 instead of null

官方版本字段：5.7, 8.0, 8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #106225](https://bugs.mysql.com/bug.php?id=106225)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 直接 BIN 空字符串与 BIN(CAST AS UNSIGNED) 是否要求同义，现有原文未提供完整语义论证
- {"point": "BIN 空串与 BIN(CAST 空串 AS UNSIGNED) 是否必须同义。", "evidence": "cmain 显示直接 BIN 返回 NULL、显式 CAST 返回 0 并产生 warning；c519279 仅确认收到报告，未定义转换契约。", "needed": "目标版本 BIN 参数转换规则、SQL mode 与 warning 语义依据。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-106737-8.0.32 · Bug #106737

Wrong SE called to ack clone application if >1 SE

官方版本字段：8.0.28-8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #106737](https://bugs.mysql.com/bug.php?id=106737)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-106750-8.0.32 · Bug #106750

Some clone tests needlessly marked as Linux-only

官方版本字段：8.0.28-8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #106750](https://bugs.mysql.com/bug.php?id=106750)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Report concerns macOS MTR clone tests skipped by linux.inc; needs macOS target build and MTR clone suite, not SQL on Linux instance.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-107109-8.0.32 · Bug #107109

Optimizer hints doesn't work if client charset is the same with charset of syste

官方版本字段：8.0.27, 5.7.37, 8.0.32

状态：未复现；阶段：baseline_preserved

官方报告：[Bug #107109](https://bugs.mysql.com/bug.php?id=107109)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-107109-8.0.32.sql)

### mysql-107337-8.0.32 · Bug #107337

IN() does not work correctly for TIME column

官方版本字段：8.0.27, 5.7, 8.0.29, 8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #107337](https://bugs.mysql.com/bug.php?id=107337)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：8.0.31 与目标 8.0.32 逐语句结果和警告相同：TIME IN 含 NULL/空串的前两查询均为空，另两控制均返回 08:00:00；数据校验为一行且 min/max 均 08:00:00。源 SQL、postcheck、环境关键变量及 optimizer_switch 一致，release/amd64 匹配。前版已有同样异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-107337-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-107337-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-107337-8.0.32.sql)

### mysql-107366-8.0.32 · Bug #107366

Contribution by Tencent: Invalid JSON value, Error_code: 3903

官方版本字段：8.0.18 and prior, 8.0.29, 8.0.30, 8.0.31, 8.0.32

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #107366](https://bugs.mysql.com/bug.php?id=107366)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain为master-slave MTR，要求ROW binlog、复制同步与从库Update_rows 3903；SQL完整但当前单实例不能代替复制HASH_SCAN。需专属双实例及MTR复制驱动。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-107384-8.0.32 · Bug #107384

the warnings of parsing error of hints are treated as syntax_error when upgrade

官方版本字段：8.0.25, 8.0.29, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #107384](https://bugs.mysql.com/bug.php?id=107384)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires pre-8.0.23/8.0.11 initialized data directory then upgrade to target with stored hint routines. Current fresh target-only instance lacks upgrade history.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-107424-8.0.32 · Bug #107424

st_intersects() returns different results with or without spatial index

官方版本字段：8.0.26, 8.0.29, 8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #107424](https://bugs.mysql.com/bug.php?id=107424)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧完整输出及控制相同：无空间索引返回两个小数末位不同的点，建索引后只返回第一个点；两点精度、SRID=4326 及成功建索引均已核对。8.0.31 已有同样异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-107424-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-107424-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-107424-8.0.32.sql)

### mysql-107715-8.0.32 · Bug #107715

Multiple SE clone not calling clone_end after mixed clone_begin failure/success

官方版本字段：8.0.29-8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #107715](https://bugs.mysql.com/bug.php?id=107715)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain仅代码分析，缺可执行触发步骤及两个支持clone的引擎；c523791明确多引擎clone尚不支持，不能把未来接口资源处理问题当现有普通SQL复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109289-8.0.32 · Bug #109289

MySQL 8.0.32 corrupted table causing MySQL to crash

官方版本字段：8.0.30, 8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #109289](https://bugs.mysql.com/bug.php?id=109289)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109661-8.0.32 · Bug #109661

mysqlsh 8.0.32 is executed without arguments it try to connect using [client]

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109661](https://bugs.mysql.com/bug.php?id=109661)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109666-8.0.32 · Bug #109666

ST_Transform fails when transforming from 4326 to 6350

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109666](https://bugs.mysql.com/bug.php?id=109666)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109685-8.0.32 · Bug #109685

mysqldump has incompatibile change in MySQL 8.0.32

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109685](https://bugs.mysql.com/bug.php?id=109685)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109699-8.0.32 · Bug #109699

utf8mb4 identifiers stopped working since 8.0.32 release

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109699](https://bugs.mysql.com/bug.php?id=109699)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：{"normal": "Exactly one žlutý_😀 row survives equality/GROUP BY/HAVING.", "same_target_anomaly": "The query returns empty.", "case_gates": "utf8mb4 source bytes and connection; derived_condition_pushdown=on.", "unknown": "Syntax/unsupported feature errors, failed setup/postcheck, timeouts/OOM/connection errors, mismatching environment, uncomparable plan or any other unexplained result are unknown; never normal.", "conclusion": "Previous normal plus validated target abnormal => observed_new_at_release; same anomaly on previous => pre_existing; otherwise unknown."}

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109699-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109699-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-109699-8.0.32.sql)

### mysql-109700-8.0.32 · Bug #109700

Fix for #33630199 in 8.0.32 not reflected in the documentation and release notes

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109700](https://bugs.mysql.com/bug.php?id=109700)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109701-8.0.32 · Bug #109701

Fix for #33630199 in 8.0.32 introduces regression when --set-gtid-purged=OFF

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109701](https://bugs.mysql.com/bug.php?id=109701)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109705-8.0.32 · Bug #109705

Flush table deadlock

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #109705](https://bugs.mysql.com/bug.php?id=109705)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109711-8.0.32 · Bug #109711

mysqlimport doesn't escape reserved-word table names when used with --delete

官方版本字段：8.0.31, 8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109711](https://bugs.mysql.com/bug.php?id=109711)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109723-8.0.32 · Bug #109723

Exists query assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #109723](https://bugs.mysql.com/bug.php?id=109723)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Target is dynamic_cast assertion explicitly verified only in debug; subquery_to_derived setup and SQL complete, needs WITH_DEBUG target build. ASan/UBSan mentioned but necessity not proven.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109725-8.0.32 · Bug #109725

Wrong result for AVG() OVER(ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109725](https://bugs.mysql.com/bug.php?id=109725)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：{"normal": "Four rows: sums 9,7,4,NULL; counts 3,2,1,0; averages 3,3.5,4,NULL equal SUM/COUNT.", "same_target_anomaly": "Second-row AVG=7 while SUM/COUNT=3.5.", "case_gates": "Four input integers 1..4; div_precision_increment=4.", "unknown": "Syntax/unsupported feature errors, failed setup/postcheck, timeouts/OOM/connection errors, mismatching environment, uncomparable plan or any other unexplained result are unknown; never normal.", "conclusion": "Previous normal plus validated target abnormal => observed_new_at_release; same anomaly on previous => pre_existing; otherwise unknown."}

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109725-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109725-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-109725-8.0.32.sql)

### mysql-109736-8.0.32 · Bug #109736

ANY query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109736](https://bugs.mysql.com/bug.php?id=109736)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Original cmain explicitly says -DWITH_DEBUG=1 -DWITH_ASAN=ON -DWITH_UBSAN=ON; static conditions array missed this. Excluded from ordinary release execution.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109764-8.0.32 · Bug #109764

Index merge not considered for indexes that have a common prefix

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109764](https://bugs.mysql.com/bug.php?id=109764)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109767-8.0.32 · Bug #109767

External Component has thrown an exception

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #109767](https://bugs.mysql.com/bug.php?id=109767)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain仅安装器/连接报错描述；c529352请求日志与截图，c530339因无反馈挂起。缺安装器版本、系统、步骤和异常日志。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109796-8.0.32 · Bug #109796

STR_TO_DATE() invalid input doesn't returns NULL but invalid DATE

官方版本字段：8.0.32, 5.7

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #109796](https://bugs.mysql.com/bug.php?id=109796)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- DATE control returns NULL; STR_TO_DATE and DATE(STR_TO_DATE) both return invalid 2022-04-31 under the requested ANSI,TRADITIONAL mode. Post-execution disk-probe/normal-stop race is separately retained; SQL and diagnostic logs completed before cleanup.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：8.0.31 与 8.0.32 均在已核对的 ANSI/TRADITIONAL 模式下 DATE 返回 NULL，而 STR_TO_DATE 及外包 DATE 返回无效日期 2022-04-31；逐语句输出与警告相同。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109796-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109796-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-109796-8.0.32.sql)

### mysql-109820-8.0.32 · Bug #109820

optimizer hints in definition of views seem to be ignored

官方版本字段：8.0.29, 8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109820](https://bugs.mysql.com/bug.php?id=109820)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧直接 NO_MERGE 查询均为 PRIMARY/DERIVED，保存的视图定义丢失 hint，视图 EXPLAIN 为 SIMPLE/t1；两行数据控制及 1003 提示记录相同，没有将提示语法错误当目标现象。只计 plan_diff，8.0.31 已有。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109820-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109820-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-109820-8.0.32.sql)

### mysql-109821-8.0.32 · Bug #109821

Subquery optimizer error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109821](https://bugs.mysql.com/bug.php?id=109821)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文 WITH_DEBUG/ASan/UBSan，验证评论明确只有 debug 断言 nest->nj_counter>0；当前普通 release 环境不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109824-8.0.32 · Bug #109824

Bit query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109824](https://bugs.mysql.com/bug.php?id=109824)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确WITH_DEBUG=1、ASAN、UBSAN、Boost1.77；当前仅release镜像。不能把stock结果当所述构建已验证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109833-8.0.32 · Bug #109833

UTF-8 strings are broken when comparing to UNIONs

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #109833](https://bugs.mysql.com/bug.php?id=109833)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 直接查询与 UNION 过滤均返回 ERRÖR 一行且无字符转换警告；8.0.32 UNION 过滤为空并有 1300/1366 警告。源数据 HEX、源 SQL、postcheck、关键环境及 optimizer_switch 相同。支持所记录条件下 8.0.31→8.0.32 行为边界，不证明独立根因。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109833-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-109833-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-109833-8.0.32.sql)

### mysql-109836-8.0.32 · Bug #109836

Decimal retention of results in string type data calculation

官方版本字段：8.0.31, 8.0.32, 5.7.41

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #109836](https://bugs.mysql.com/bug.php?id=109836)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c529387说明整数除法返回decimal、字符串除法返回double，舍入不同有类型语义依据；不能把原四条查询显示差异计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109837-8.0.32 · Bug #109837

The representation of 0 in division function in computing string

官方版本字段：8.0.31, 8.0.32, 5.7.41

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #109837](https://bugs.mysql.com/bug.php?id=109837)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original reproducer has duplicate SELECT syntax; signed zero for floating string arithmetic versus integer division has no established wrong-result contract. Need corrected source SQL and numeric/format semantics.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109840-8.0.32 · Bug #109840

Analyze then Rollup assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109840](https://bugs.mysql.com/bug.php?id=109840)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug/ASan/UBSan 构建；空表 ANALYZE HISTOGRAM 后 ROLLUP 触发 distinct>=1 断言；缺对应构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109842-8.0.32 · Bug #109842

Problems when mod , division function and extremum function are used together

官方版本字段：8.0.31, 8.0.32, 5.7.41

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #109842](https://bugs.mysql.com/bug.php?id=109842)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain负零与正零在比较上相等，不足证明LEAST/GREATEST应具有相同显示符号；缺浮点有符号零和返回类型契约，只有收到报告的评论。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109845-8.0.32 · Bug #109845

Inconsistency of the results of the round function

官方版本字段：8.0.31, 8.0.32, 5.7.41

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #109845](https://bugs.mysql.com/bug.php?id=109845)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer c529421 explicitly identifies integer ROUND return type as documented normal behavior; formatting 1 versus 1.00 cannot be treated as Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109873-8.0.32 · Bug #109873

no need to maintain err in buf_page_init_for_read

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #109873](https://bugs.mysql.com/bug.php?id=109873)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain为buf_page_init_for_read冗余err维护代码优化，How to repeat明确read the code；无SQL故障oracle。需要源码级检查，当前目标版本SQL回放不适用。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109874-8.0.32 · Bug #109874

DELETE assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109874](https://bugs.mysql.com/bug.php?id=109874)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain要求重连后DELETE且debug/ASAN/UBSAN；c529471确认debug affected。单连接release环境不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109885-8.0.32 · Bug #109885

ALTER TABLE doesn't update use_stopword when dropping & recreating

官方版本字段：8.0.23, 8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109885](https://bugs.mysql.com/bug.php?id=109885)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需要ngram parser可用及SET GLOBAL innodb_ft_aux_table；全局FTS状态须专用审查，当前普通批不执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109891-8.0.32 · Bug #109891

Contribution by Tencent: insert on duplicate key update would be abnormal

官方版本字段：8.0.30,8.0.31, 8.0.32, 5.7

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #109891](https://bugs.mysql.com/bug.php?id=109891)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- AUTO_INCREMENT exhaustion produces conflicts on both PRIMARY and unique c2. Discussion disputes required ON DUPLICATE outcome; need resolve multi-unique conflict contract before calling error Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109893-8.0.32 · Bug #109893

json_contains always return 1 if candidate array is empty array

官方版本字段：8.0.31, 8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #109893](https://bugs.mysql.com/bug.php?id=109893)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 空候选数组的所有元素条件可为真，c529483倾向文档问题；三条JSON_CONTAINS返回1不能直接判Bug。需先确定空集合包含关系契约。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109894-8.0.32 · Bug #109894

Server diagnostics area error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109894](https://bugs.mysql.com/bug.php?id=109894)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需要 GTID/enforce_GTID/binlog 启动配置、debug、READ ONLY 后 SET GLOBAL BINLOG_CHECKSUM 触发全局轮换；本轮普通实例缺专门配置与全局状态恢复流程。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109917-8.0.32 · Bug #109917

server crash when execute create table with check constraint in ps mode

官方版本字段：8.0, 8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #109917](https://bugs.mysql.com/bug.php?id=109917)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c529530/c529548/c529572确认debug-only；release的3815是合法拒绝而不是该断言现象。缺debug构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109919-8.0.32 · Bug #109919

Clone plugin does not support arbitrary length O_DIRECT files

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109919](https://bugs.mysql.com/bug.php?id=109919)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109920-8.0.32 · Bug #109920

SEs cannot add to clone data size estimates

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109920](https://bugs.mysql.com/bug.php?id=109920)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109921-8.0.32 · Bug #109921

Cannot clone with synchronization across SEs

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109921](https://bugs.mysql.com/bug.php?id=109921)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109922-8.0.32 · Bug #109922

SEs do not coordinate clone rollbacks on instance startup

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109922](https://bugs.mysql.com/bug.php?id=109922)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109926-8.0.32 · Bug #109926

Clone plugin does not support transactional SEs other than InnoDB

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #109926](https://bugs.mysql.com/bug.php?id=109926)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109934-8.0.32 · Bug #109934

Configuring a MySQL innodb cluster with MySQL Shell failed in Docker container

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #109934](https://bugs.mysql.com/bug.php?id=109934)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires populated Docker overlay filesystem plus MySQL Shell clone/addInstance and three-node cluster restart; current isolated single-instance mount layout not equivalent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109939-8.0.32 · Bug #109939

Lists partitions can not be reorganized (must be in consecutive order)

官方版本字段：8.0.32, 5.7.41

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #109939](https://bugs.mysql.com/bug.php?id=109939)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- REORGANIZE非相邻LIST分区报1519的脚本完整，但作者与既有设计/功能请求分类争议未解决；不能把明确正常限制错误计Bug。需要先冻结支持非相邻分区的契约。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109953-8.0.32 · Bug #109953

InnoDB checkpoint disabled assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #109953](https://bugs.mysql.com/bug.php?id=109953)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Debug INNODB_CHECKPOINT_DISABLED and shutdown assertion; functional debug flag necessary, plus controlled shutdown/log capture. Need determine whether debug fault injection intentionally triggers abort before valid defect oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109966-8.0.32 · Bug #109966

Possible server deadlock on checkpoint

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #109966](https://bugs.mysql.com/bug.php?id=109966)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c529702明确debug-only已知行为且Not a bug；INNODB_LOG_CHECKPOINT_NOW配合禁用flush挂起需debug全局状态实验，不能用普通release变量报错判现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109977-8.0.32 · Bug #109977

Contribution by Tencent: semisync plugin may print a negative server id

官方版本字段：8.0.32,5.7.41

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #109977](https://bugs.mysql.com/bug.php?id=109977)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat says read code; missing runtime semisync topology, chosen unsigned server_id, workload, and log oracle. Source patch is not an executable reproducer.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109991-8.0.32 · Bug #109991

Compilation fails on Debug instruction

官方版本字段：8.0.31, 8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #109991](https://bugs.mysql.com/bug.php?id=109991)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109996-8.0.32 · Bug #109996

There is no local IP address matching the one configured for the local node

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #109996](https://bugs.mysql.com/bug.php?id=109996)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires systemd-nspawn three-node cluster and DHCP-delay boot ordering. Cannot emulate as ordinary SQL or change host service/network settings.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110003-8.0.32 · Bug #110003

DELETE query does ot work for BIT columns

官方版本字段：8.0.32, 5.7, 5.6

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110003](https://bugs.mysql.com/bug.php?id=110003)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧 SELECT 命中 id123/HEX1 一行，但 DELETE 删除 0 行；before_count=8、after_count=8、rows_left=8，全部数据控制一致。8.0.31 已有 SELECT/DELETE 不一致。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110003-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110003-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110003-8.0.32.sql)

### mysql-110005-8.0.32 · Bug #110005

When using union, when the value of the field in the where condition is Chinese

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110005](https://bugs.mysql.com/bug.php?id=110005)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL filtered result empty with conversion warning 1300; postcheck confirms the inserted Chinese name row exists.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 UNION ALL 过滤正确返回两行 (1,姜志福)，8.0.32 空集并有转换警告；两侧源数据控制均为一行 (1,姜志福)，关键环境及 optimizer_switch 相同。仅确认相邻版本现象边界，保留与 #109699 的重复报告关联。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110005-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110005-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110005-8.0.32.sql)

### mysql-110011-8.0.32 · Bug #110011

inconsistent behavior with group by and order by

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110011](https://bugs.mysql.com/bug.php?id=110011)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires Sakila payment schema/data and exact SQL mode. Thread provides no frozen dataset and includes disputed grouping semantics; cannot assume sample availability or expected output.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110015-8.0.32 · Bug #110015

Multi-valued index on JSON array is not used when used in a join

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110015](https://bugs.mysql.com/bug.php?id=110015)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c529875将请求定为功能增强，c529893转文档限制；索引未被选择本身不能判Bug，需界定受支持索引使用契约与稳定性能oracle。保留完整数据生成过程但不强行作为错误回放。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110042-8.0.32 · Bug #110042

Optimize table and corruption?

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110042](https://bugs.mysql.com/bug.php?id=110042)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Unsafe durability/checkpoint configuration plus forced shutdown/OPTIMIZE; verifier disputes crash-safety expectation. Need original crash/recovery protocol and accepted oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110045-8.0.32 · Bug #110045

Negative numbers on digests

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110045](https://bugs.mysql.com/bug.php?id=110045)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧第一条 digest 均为 SELECT ? WHERE ? = ?，第二条保留额外 - 为 SELECT ? WHERE ? = - ?。8.0.31 已有同样 metadata_difference，不计 wrong_result。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110045-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110045-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110045-8.0.32.sql)

### mysql-110070-8.0.32 · Bug #110070

System.NotSupportedException: Character set 'utf8mb3' is not supported by .Net F

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110070](https://bugs.mysql.com/bug.php?id=110070)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110074-8.0.32 · Bug #110074

CMake option WITH_DEVELOPER_ENTITLEMENTS not documented in the reference

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110074](https://bugs.mysql.com/bug.php?id=110074)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110076-8.0.32 · Bug #110076

VALUES Statement with dependent subquery is wrong

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110076](https://bugs.mysql.com/bug.php?id=110076)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Two source rows remain; correlated VALUES/MAX returns c1 then NULL instead of c1/c2.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧相关 VALUES/MAX 查询均返回 ID1=c1、ID2=NULL，而 oracle 为 c1/c2；原 SQL 和两侧逐语句输出相同，8.0.31 已有同样异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110076-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110076-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110076-8.0.32.sql)

### mysql-110077-8.0.32 · Bug #110077

Lateral join error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110077](https://bugs.mysql.com/bug.php?id=110077)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug/ASan/UBSan 的 ASSERT_COLUMN_MARKED_FOR_READ；缺对应构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110078-8.0.32 · Bug #110078

optimize for innodb recovery

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110078](https://bugs.mysql.com/bug.php?id=110078)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat is read code; optimization proposal has no workload, data or quantitative target oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110089-8.0.32 · Bug #110089

Inconsistent results returned when choosing different plans on federated engine

官方版本字段：8.0.18, 8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110089](https://bugs.mysql.com/bug.php?id=110089)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c530028明确FEDERATED两端字段不一致属于不受支持用法；原non_id远端unsigned本地signed，不能把结果差异当Bug；且需要双实例FEDERATED环境。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110091-8.0.32 · Bug #110091

optimize for innodb recovery

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110091](https://bugs.mysql.com/bug.php?id=110091)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Read-code optimization proposal; c530079 explicitly says crash recovery tests not run. Missing reproducible workload and expected metric.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110098-8.0.32 · Bug #110098

add database message into slow log file

官方版本字段：Ver 8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110098](https://bugs.mysql.com/bug.php?id=110098)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain为慢日志增强请求，要求每条查询输出database字段；未给出完整sbtest表数据/开启慢日志配置，正常日志省略重复USE不是已定义错误。需功能需求验收oracle与专用日志采集。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110101-8.0.32 · Bug #110101

lock_row_lock_current_waits counter in innodb_metrics goes negative

官方版本字段：5.7.39, 8.0, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110101](https://bugs.mysql.com/bug.php?id=110101)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires three coordinated sessions, lock wait/counter state and global timeout; single-session runner cannot preserve interleaving or metric reset contract.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110102-8.0.32 · Bug #110102

Invalid utf8mb4 character string: 'E9' on view with derived table

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #110102](https://bugs.mysql.com/bug.php?id=110102)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SQL/数据完整但原VIEW使用toto@% definer，缺创建该账户及权限条件；需新隔离实例、utf8mb4客户端和源库、来源明确的definer权限准备。c530012为109699重复。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110104-8.0.32 · Bug #110104

Query exception caused by union in 8.0.32

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110104](https://bugs.mysql.com/bug.php?id=110104)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source UNION control returns (5,测试), outer filtered query is empty with warning1300, pushdown-off control restores (5,测试).

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 原始 UNION 控制、外层过滤及 pushdown-off 控制均返回 (5,测试)；8.0.32 中间过滤为空。源数据、关键环境、初始 optimizer_switch 和 SQL 字节一致，满足前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110104-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110104-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110104-8.0.32.sql)

### mysql-110107-8.0.32 · Bug #110107

InnoDB Data File Error

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110107](https://bugs.mysql.com/bug.php?id=110107)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110122-8.0.32 · Bug #110122

Start MySQL 8.0.32 second instance with temporary data directory

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110122](https://bugs.mysql.com/bug.php?id=110122)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110125-8.0.32 · Bug #110125

Unexpected query result fetched from an indexed column

官方版本字段：8.0.32, 5.7

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110125](https://bugs.mysql.com/bug.php?id=110125)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧错误返回 ZEROFILL 数值零；数据校验均为一行、min/max=0，而负常量不应命中。前版已有同样异常，未把显示补零或弃用警告当 Bug。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110125-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110125-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110125-8.0.32.sql)

### mysql-110129-8.0.32 · Bug #110129

Wrong explanation in innodb_stats_auto_recalc

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110129](https://bugs.mysql.com/bug.php?id=110129)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110130-8.0.32 · Bug #110130

Wrong table-path in Error:1114 and Error:13132

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110130](https://bugs.mysql.com/bug.php?id=110130)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires dedicated quota-limited tmp filesystem and disk-full TempTable/InnoDB spill; need file placement/log oracle and bounded disk exhaustion protocol. Do not fill shared filesystem.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110144-8.0.32 · Bug #110144

CREATE TABLE with a large MIN_ROWS on an indexed column causes memory error.

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110144](https://bugs.mysql.com/bug.php?id=110144)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c530107判Not a bug并指出极大MIN_ROWS，作者称去掉仍可复现但官方不能复现；需区分真实容量限制与错误估算oracle，不能把错误34直接计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110155-8.0.32 · Bug #110155

Improve GR error MY-013780 reporting

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110155](https://bugs.mysql.com/bug.php?id=110155)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110164-8.0.32 · Bug #110164

mysql-8.0.32-macos13-x86_64.dmg installer hangs/freezes

官方版本字段：mysql-8.0.32-macos13-x86_64

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110164](https://bugs.mysql.com/bug.php?id=110164)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- macOS13 x86_64 installer tested on Catalina10.15.7; supported-platform issue. Linux server instance cannot verify GUI installer hang.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110170-8.0.32 · Bug #110170

ZEROFILL should not change the query result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110170](https://bugs.mysql.com/bug.php?id=110170)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- ZEROFILL会影响字符串LIKE转换，原有/无ZEROFILL等价主张未被证明；c530158关闭为Not a bug，需单独厘清谓词及sql_mode语义，不能自动等价判错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110177-8.0.32 · Bug #110177

clear invalid comment in table file and index when upgrade from 57 to 80

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110177](https://bugs.mysql.com/bug.php?id=110177)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110181-8.0.32 · Bug #110181

tmp_table_size=51200 causing error that tmp does not exists

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110181](https://bugs.mysql.com/bug.php?id=110181)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧都在 tmp_table_size=51200 的三个指定 information_schema 查询（executed.sql 第8–10行）返回 1146/42S02，错误明确指向内部 ./tmp/#sql 表；改为16777216 后三查询无错误，最终变量校验成功。临时表连接编号不同不影响相同异常；不是把普通缺表错误或空集作为 Bug。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110181-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110181-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110181-8.0.32.sql)

### mysql-110194-8.0.32 · Bug #110194

DD upgrade leaves dictonary tables in temporary schema dd_upgrade_targets_80030

官方版本字段：8.0.23, 8.0.30, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110194](https://bugs.mysql.com/bug.php?id=110194)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires data directory initialized by <8.0.23 then target upgrade and ibd2sdi inspection; fresh target SQL cannot create the DD upgrade state.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110200-8.0.32 · Bug #110200

MySQL Database Bug

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110200](https://bugs.mysql.com/bug.php?id=110200)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Workbench导出异常，c530228索要debug3日志且无反馈挂起；缺Workbench版本/平台/输入库/异常日志，目标mysqld SQL无法代表该UI故障。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110206-8.0.32 · Bug #110206

Upgrading MySQL Server from 8.0.27 to 8.0.32 using Installer 1.6.5.0

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110206](https://bugs.mysql.com/bug.php?id=110206)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Windows Server2019 Installer1.6.5.0 upgrade from8.0.27 with existing instances; fresh upgrade unreproducible, original configuration/VC runtime missing.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110213-8.0.32 · Bug #110213

An incorrect query result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110213](https://bugs.mysql.com/bug.php?id=110213)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c530252作者质疑比较符优先级后表示可能不是Bug，c530314关闭；缺可靠表达式期望值论证，不能使用原预期{1}直接判错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110216-8.0.32 · Bug #110216

failed to compile in static mode

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110216](https://bugs.mysql.com/bug.php?id=110216)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Build-time protobuf compiler failure with static-libgcc/static-libstdc++, Debian8 GCC8.5 and CMake3.9.6; needs isolated build environment, not running target SQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110217-8.0.32 · Bug #110217

failed to compile in mysql_release mode

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110217](https://bugs.mysql.com/bug.php?id=110217)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110218-8.0.32 · Bug #110218

can not link jemalloc or tcmalloc in debian 11.5

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110218](https://bugs.mysql.com/bug.php?id=110218)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110227-8.0.32 · Bug #110227

Upgrade to 8.0 fails due to lost+found directory present in datadir

官方版本字段：8.0, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110227](https://bugs.mysql.com/bug.php?id=110227)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires5.7 datadir with lost+found/ignore_db_dirs followed by in-place8.0 upgrade. Current target-only scope lacks precursor environment.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110228-8.0.32 · Bug #110228

pushdown condition Including Chinese convert string error

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110228](https://bugs.mysql.com/bug.php?id=110228)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110232-8.0.32 · Bug #110232

"Killed" counter is not updated with "log_slow_extra" enabled

官方版本字段：MySQL 8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110232](https://bugs.mysql.com/bug.php?id=110232)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs slow-log-extra, source test table/data and timed separate-session KILL; only log fragments, no complete bounded workload. Must collect correct slow-log segment rather than treat interrupted query as failure.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110244-8.0.32 · Bug #110244

Nesting queries in a projection results in different output

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110244](https://bugs.mysql.com/bug.php?id=110244)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧第一变体返回 NULL/NULL，外包 SELECT * 变体为空；FRIENDSHIP、LIKES 与空的子查询控制相同，8.0.31 已有同样丢行异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110244-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110244-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110244-8.0.32.sql)

### mysql-110245-8.0.32 · Bug #110245

Issue with NOT IN

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110245](https://bugs.mysql.com/bug.php?id=110245)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110250-8.0.32 · Bug #110250

Right join query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110250](https://bugs.mysql.com/bug.php?id=110250)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文cmain明确-DWITH_DEBUG=1 -DWITH_ASAN=ON -DWITH_UBSAN=ON及Boost1.77；现有release容器不满足冻结原文构建条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110256-8.0.32 · Bug #110256

An incorrect query result for an indexed decimal column

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110256](https://bugs.mysql.com/bug.php?id=110256)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧索引路径为空、无索引控制返回零；数据校验都是一行零，源 SQL、顺序和关键环境相同，8.0.31 已有同样异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110256-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110256-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110256-8.0.32.sql)

### mysql-110276-8.0.32 · Bug #110276

Method not found: 'Void MySql.Data.MySqlClient.MySqlConnectionStringBuilder..cto

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110276](https://bugs.mysql.com/bug.php?id=110276)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110281-8.0.32 · Bug #110281

Incorrect query result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110281](https://bugs.mysql.com/bug.php?id=110281)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official thread disputes mixed string/decimal conversion and filtering versus projection semantics; example complete but oracle remains contested. Do not classify observed mismatch as confirmed Bug without resolving semantics.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110289-8.0.32 · Bug #110289

Weired error message when an UPDATE uses EXISTS subquery and is blocked

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110289](https://bugs.mysql.com/bug.php?id=110289)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110301-8.0.32 · Bug #110301

Change column wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110301](https://bugs.mysql.com/bug.php?id=110301)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 零日期 DATE NOT NULL 的 IS NULL 过滤可能涉及兼容特殊行为，既有正文未排除该解释。
- {"point": "零日期 DATE NOT NULL 的 IS NULL 过滤可能涉及兼容特殊行为，既有正文未排除该解释。", "evidence": "cmain 观察零日期和 WHERE/SUM 差异，c530541 仅确认收到报告。", "needed": "目标 8.0 IS NULL 对零日期的正式语义依据；原始 sql_mode，后续静态判据审查。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110305-8.0.32 · Bug #110305

Export of view statement resulting incorrect syntax

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110305](https://bugs.mysql.com/bug.php?id=110305)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat only says Repeatable; missing view DDL, export tool/version and input schema; verifier asked unanswered.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110306-8.0.32 · Bug #110306

Incorrect costing in test_if_cheaper_ordering

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110306](https://bugs.mysql.com/bug.php?id=110306)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain只有test_if_cheaper_ordering源码分析，作者称可提供测试但未提供；c530544仍请求用例。缺表、数据、查询和成本判据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110310-8.0.32 · Bug #110310

BETWEEN query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110310](https://bugs.mysql.com/bug.php?id=110310)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Original cmain explicitly says -DWITH_DEBUG=1 -DWITH_ASAN=ON -DWITH_UBSAN=ON; static conditions array missed this. Excluded from ordinary release execution.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110322-8.0.32 · Bug #110322

Binary column primary key query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110322](https://bugs.mysql.com/bug.php?id=110322)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文给出 WITH_DEBUG/ASan/UBSan 构建，二进制主键 WHERE/SUM 不一致；需明确匹配构建条件后再排执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110332-8.0.32 · Bug #110332

Different result when using a user variable

官方版本字段：8.0.32, 5.7.41

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110332](https://bugs.mysql.com/bug.php?id=110332)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 用户变量存储 TIME/DATETIME 后变为字符串，现有对照非类型等价；需先明确同类型缓存比较契约
- {"point": "TIME/DATETIME CASE 与用户变量路径可能不是同类型比较。", "evidence": "cmain 给出 1/0 差异及 1292 warning，并提出缓存与 cmp 类型不同；c530590 只有接收/感谢语。", "needed": "目标版 CASE 合并类型、用户变量存储类型及数字比较的契约与同类型控制。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110341-8.0.32 · Bug #110341

FOUND_ROWS() gives wrong result on prepared query against partitioned table

官方版本字段：8.0.32

状态：其他异常；阶段：baseline_preserved

官方报告：[Bug #110341](https://bugs.mysql.com/bug.php?id=110341)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-110341-8.0.32.sql)

### mysql-110343-8.0.32 · Bug #110343

Reproducible crash with assertion failure when updating

官方版本字段：8.0.32-1.el8

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110343](https://bugs.mysql.com/bug.php?id=110343)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original private physical database/corruption state unavailable; logical restore no longer reproduces. Need exact affected datadir or reproducible DDL/data history; stack alone insufficient.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110345-8.0.32 · Bug #110345

MySQL crash on MacOS typically when restoring a MySQL 5.7 sql

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110345](https://bugs.mysql.com/bug.php?id=110345)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110347-8.0.32 · Bug #110347

Inconsistent blocking of UPDATE and DELETE with the same WHERE clause

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110347](https://bugs.mysql.com/bug.php?id=110347)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs two-session transaction schedule with lock evidence; official rationale and reporter lock dump conflict, so blocking difference alone lacks established bug oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110350-8.0.32 · Bug #110350

MTR test lock_order.cycle fails

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #110350](https://bugs.mysql.com/bug.php?id=110350)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 目标为debug源码树MTR lock_order.cycle启动unknown --lock-order-print-txt错误；需该版本MTR套件及lock-order构建配置，SQL客户端不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110354-8.0.32 · Bug #110354

SELECT Query choose different index return different results

官方版本字段：8.0.32, 5.7.41

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110354](https://bugs.mysql.com/bug.php?id=110354)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧 b_idx 返回6行，a_b_idx 返回15行，IGNORE INDEX 也实际返回15行；未把后者写成正常控制。校验均为21行、15个非NULL、b<阈值为6行，时区+08:00、空sql_mode相同。完整两侧结果完全一致，8.0.31 已存在所报告的索引路径不一致。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110354-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110354-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110354-8.0.32.sql)

### mysql-110371-8.0.32 · Bug #110371

mysql-test/include/keyring_tests/helper/global_keyring_create_config.inc unused

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_runtime_source_issue

官方报告：[Bug #110371](https://bugs.mysql.com/bug.php?id=110371)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Unused mysql-test include source file is source-maintenance issue; no server SQL reproducer or execution oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110375-8.0.32 · Bug #110375

upgrade mysql from 8.0.29 to 8.0.32，union error

官方版本字段：8.0.32 linix-generic

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110375](https://bugs.mysql.com/bug.php?id=110375)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- LIKE Chinese-name filter returns both China and France with conversion warning 1300.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 中文 LIKE 仅返回中国且无转换警告；8.0.32 同一常量源查询错误返回中国、法国并有1300警告。两侧 SQL、UTF8 环境及 optimizer_switch 一致。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110375-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110375-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110375-8.0.32.sql)

### mysql-110376-8.0.32 · Bug #110376

upgrade mysql from 8.0.29 to 8.0.32, union error

官方版本字段：8.0.32 linix-generic

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110376](https://bugs.mysql.com/bug.php?id=110376)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- LIKE returns China and France initially; pushdown-off returns only China.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 初始 pushdown-on 和 off 控制都仅返回中国；8.0.32 初始错误返回中国、法国，off 才恢复中国。相同 SQL 与关键环境，符合前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110376-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110376-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110376-8.0.32.sql)

### mysql-110383-8.0.32 · Bug #110383

After ALTER, TABLESPACE is incorrectly explicit with innodb_file_per_table=0

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110383](https://bugs.mysql.com/bug.php?id=110383)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需 innodb_file_per_table=0 全局设置及恢复；ALTER 后错误加入 TABLESPACE innodb_system；暂未建立专用全局配置实例。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110384-8.0.32 · Bug #110384

LIKE query on union result with Unicode characters returns no results

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110384](https://bugs.mysql.com/bug.php?id=110384)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Japanese LIKE returns no rows with warning 1300; ASCII value control returns both rows.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 Unicode LIKE 与 ASCII LIKE 控制均返回两个原始名字；8.0.32 Unicode LIKE 空集、ASCII 控制两行且有1300字符转换警告。数据与字符集条件相同。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110384-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110384-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110384-8.0.32.sql)

### mysql-110407-8.0.32 · Bug #110407

mysqld crashed when execute a prepared query against partitioned table

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110407](https://bugs.mysql.com/bug.php?id=110407)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- PREPARE assertion explicitly debug-only in8.0.32 with original partitioned DATE SQL; release control noncrashing. Need debug image, not merely run ordinary SQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110415-8.0.32 · Bug #110415

Unrestricted memory allocation to query causes OOM kill

官方版本字段：8.0.30, 8.0.31, 8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110415](https://bugs.mysql.com/bug.php?id=110415)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110416-8.0.32 · Bug #110416

mysqld strange exit code

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #110416](https://bugs.mysql.com/bug.php?id=110416)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 报告debug/ASan/UBSan运行SQL后SHUTDOWN退出1，官方退出0并指出临时表设置；需保留启动参数/临时表配置、关机退出码和日志的专属实例。当前无完整原配置。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110421-8.0.32 · Bug #110421

MySQL server not honoring connection_memory_limit for user created temp tables

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110421](https://bugs.mysql.com/bug.php?id=110421)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Memory-engine allocations not tracked by thread PSI keys; report seeks documentation clarification. Needs nonprivileged user, tracking settings and memory workload, plus accepted scope of memory limit.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110424-8.0.32 · Bug #110424

Tomcat App looses DB connection after MySQL crash

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110424](https://bugs.mysql.com/bug.php?id=110424)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110429-8.0.32 · Bug #110429

Incorrect autoinc in imported tablespace after restart server

官方版本字段：8.0.31, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110429](https://bugs.mysql.com/bug.php?id=110429)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires FLUSH FOR EXPORT, controlled ibd/cfg copy, DISCARD/IMPORT and same-datadir restart. Single SQL session cannot satisfy file lifecycle; needs dedicated file/restart harness.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110434-8.0.32 · Bug #110434

WHERE condition assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110434](https://bugs.mysql.com/bug.php?id=110434)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确debug+ASAN+UBSAN触发sql_const_folding断言；release环境不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110441-8.0.32 · Bug #110441

Docker Hub mysql/mysql-server debian tag now missing

官方版本字段：mysql/mysql-server:8.0.32-debian

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110441](https://bugs.mysql.com/bug.php?id=110441)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110443-8.0.32 · Bug #110443

Compiling MySQL 8.0.32 fails with DWITH_INNODB_EXTRA_DEBUG.

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110443](https://bugs.mysql.com/bug.php?id=110443)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Build failure only WITH_INNODB_EXTRA_DEBUG; requires target source and compiler/build workspace. Runtime debug container does not verify compile-time error.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110446-8.0.32 · Bug #110446

main.kill_myisam will assert when install group_replication

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #110446](https://bugs.mysql.com/bug.php?id=110446)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain以补丁修改main.kill_myisam.test并安装group_replication，目标debug !flags.finalized断言；需对应完整MTR脚本、debug构建及插件，不能只运行补丁片段。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110448-8.0.32 · Bug #110448

Contribution by Tencent: incorrect result of fulltext search

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110448](https://bugs.mysql.com/bug.php?id=110448)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires added debug_sync coordination of two concurrent inserts plus ngram parser; original source test uses MTR connection/send/reap. Need actual sync points and concurrent harness, not serialized SQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110452-8.0.32 · Bug #110452

mysqldump SEGV

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110452](https://bugs.mysql.com/bug.php?id=110452)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110459-8.0.32 · Bug #110459

Derive_merge optimizer missing error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110459](https://bugs.mysql.com/bug.php?id=110459)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文明确debug+ASan+UBSan构建，当前release不满足；两侧错误差异还需1055阶段映射，不能把预期报错当失败。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110462-8.0.32 · Bug #110462

Mysqldump table with virtual column wrong syntax

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110462](https://bugs.mysql.com/bug.php?id=110462)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110474-8.0.32 · Bug #110474

Functional Index is not work like generated column and index

官方版本字段：8.0, 8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110474](https://bugs.mysql.com/bug.php?id=110474)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110480-8.0.32 · Bug #110480

XML ExtractValue with XPath using last() function return wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110480](https://bugs.mysql.com/bug.php?id=110480)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official comments classify requested XPath behavior as unsupported/not a bug and suggest different expressions. Need supported XPath semantics; cannot infer bug from cross-product comparison.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110485-8.0.32 · Bug #110485

FLUSH TABLE FOR EXPORT will lead deadlock

官方版本字段：8.0.32, 8.0.39

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110485](https://bugs.mysql.com/bug.php?id=110485)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110487-8.0.32 · Bug #110487

json array field ignored in multi sort.

官方版本字段：5.7,8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110487](https://bugs.mysql.com/bug.php?id=110487)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- JSON array ORDER BY comparison expectations lack accepted type-order contract; source also inserts into undeclared oymy_test schema. Need resolve array ordering semantics and preserve schema selection.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110496-8.0.32 · Bug #110496

Join order assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110496](https://bugs.mysql.com/bug.php?id=110496)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 验证评论限定 debug 的 join order remaining tables 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110500-8.0.32 · Bug #110500

unable to connect to server

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110500](https://bugs.mysql.com/bug.php?id=110500)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 正文仅Workbench日志提示和reconfigure server；c531146索要连接方式/debug3日志，后无反馈。缺可执行步骤、配置及日志。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110501-8.0.32 · Bug #110501

Invalid CREATE TABLE statement

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110501](https://bugs.mysql.com/bug.php?id=110501)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110519-8.0.32 · Bug #110519

Wrong Allowed Values range for connection_memory_chunk_size in documentation.

官方版本字段：8.0.28-8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110519](https://bugs.mysql.com/bug.php?id=110519)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original reproducer mutates GLOBAL connection_memory_chunk_size; need dedicated instance/global-config audit. Worklog says zero disables update, so required oracle is warning1292/clamp1, not ordinary execution failure.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110521-8.0.32 · Bug #110521

8.0.32 subquery with utf8mb4 equal case empty result

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110521](https://bugs.mysql.com/bug.php?id=110521)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION equality on Japanese character returns no rows with warning 1300; source-row postcheck succeeds.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 两个查询分别返回 の 与 (1,の)，源数据校验成功、无转换异常；8.0.32 两查询为空且有1300警告，源数据仍存在。符合相邻版本边界。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110521-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110521-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110521-8.0.32.sql)

### mysql-110524-8.0.32 · Bug #110524

XML ExtractValue with XPath on non-existing attribute wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110524](https://bugs.mysql.com/bug.php?id=110524)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Reporter corrected original query; official c531205 identifies unsupported XPath functionality. No accepted wrong-result oracle for target version.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110527-8.0.32 · Bug #110527

Analyse histogram assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110527](https://bugs.mysql.com/bug.php?id=110527)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain/c531190为debug histogram字符集断言；现脚本还出现CREATE TABLEt0缺空格，与原文CREATE TABLE t0不一致。缺debug且SQL待修正，不能执行原文件标完成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110533-8.0.32 · Bug #110533

XA COMMIT may not be recovered after a crash

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #110533](https://bugs.mysql.com/bug.php?id=110533)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- MTR依赖WITH_DEBUG、DEBUG_SYNC、ROW binlog、多连接、强制崩溃及同datadir恢复；需专属故障注入实例和完整MTR include文件，不可普通单连接SQL替代。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110535-8.0.32 · Bug #110535

Mysql instance cannot be initialized correctly because autocommit is turned off.

官方版本字段：8.0.31, 8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110535](https://bugs.mysql.com/bug.php?id=110535)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires fresh datadir bootstrap with autocommit=OFF, contrasting sys schema initialization; post-start SET autocommit is not equivalent. Need init-time config and startup harness.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110542-8.0.32 · Bug #110542

Missing error?

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110542](https://bugs.mysql.com/bug.php?id=110542)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c531301明确空外表允许优化器跳过子查询求值，1242出现与否可合法不同；原两计划差异不能当Bug，debug标记也不是必要性的证据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110550-8.0.32 · Bug #110550

ordering VALUES statement seems not to work as expected

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110550](https://bugs.mysql.com/bug.php?id=110550)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧直接 VALUES ORDER BY 均错误保留1,5,4顺序，UNION 控制均正确为0,1,4,5；8.0.31 已存在排序现象。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110550-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110550-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110550-8.0.32.sql)

### mysql-110555-8.0.32 · Bug #110555

Some performance schema tables return invalid rows

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110555](https://bugs.mysql.com/bug.php?id=110555)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires source modification adding DEBUG_SYNC after_lf_hash_search, WITH_UNIT_TESTS=0 build and concurrent P_S race harness. Stock debug binary alone lacks injected sync point.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110556-8.0.32 · Bug #110556

When we use json to build an index, we will get wrong results

官方版本字段：8.0.28, 8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110556](https://bugs.mysql.com/bug.php?id=110556)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："PRIMARY=2但多值索引count=1漏掉空数组行"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110556-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110556-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110556-8.0.32.sql)

### mysql-110557-8.0.32 · Bug #110557

When innodb_disable_sort_file_cache=ON, create a full-text index will fail

官方版本字段：8.0.28, 8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110557](https://bugs.mysql.com/bug.php?id=110557)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需 innodb_disable_sort_file_cache=ON 启动参数、ngram parser、OFF 对照及 tmpdir 条件；ALTER FULLTEXT 的 1878 可能是目标，不能当普通流程失败。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110562-8.0.32 · Bug #110562

values statement

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110562](https://bugs.mysql.com/bug.php?id=110562)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："直接VALUES ORDER BY返回原序(1,4),(2,1),(3,3)，派生表ORDER BY正确。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110562-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110562-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110562-8.0.32.sql)

### mysql-110563-8.0.32 · Bug #110563

NULL safe equality operator query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110563](https://bugs.mysql.com/bug.php?id=110563)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Original cmain explicitly says -DWITH_DEBUG=1 -DWITH_ASAN=ON -DWITH_UBSAN=ON; static conditions array missed this. Excluded from ordinary release execution.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110565-8.0.32 · Bug #110565

Adding a fulltext index causes a "Duplicate entry '0'" for the primary key

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110565](https://bugs.mysql.com/bug.php?id=110565)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain表示单独提供dataset，正文无表定义/数据/ALTER完整脚本；需报告附件中的全部.sql及顺序和校验，不能编造FTS数据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110572-8.0.32 · Bug #110572

Hypergraph optimizer assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110572](https://bugs.mysql.com/bug.php?id=110572)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain要求debug+ASan+UBSan及hypergraph_optimizer；验证评论明确8.0.32 debug；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110577-8.0.32 · Bug #110577

Missing year function?

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110577](https://bugs.mysql.com/bug.php?id=110577)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文给出 WITH_DEBUG/ASan/UBSan，生成列 CAST AS YEAR 错误 1305；缺匹配构建条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110579-8.0.32 · Bug #110579

Right join query with BETWEEN wrong result

官方版本字段：8.0.32, 5.7.41

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110579](https://bugs.mysql.com/bug.php?id=110579)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain明确debug/ASAN/UBSAN；源SQL副本CREATE TABLEt85缺空格。缺所述构建且源SQL转换错误待修正。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110582-8.0.32 · Bug #110582

After executing 'set role', cannot access the database with "_" in the db name

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110582](https://bugs.mysql.com/bug.php?id=110582)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires specific role/grants and non-admin connection to escaped underscore schema. Need isolated users, account identity and role activation protocol; privileged single-session replay invalid.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110587-8.0.32 · Bug #110587

Bit with index range query may produce different results

官方版本字段：8.0.27, 8.0.32, 5.7.41

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110587](https://bugs.mysql.com/bug.php?id=110587)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："无索引14行而建索引后为空；IGNORE INDEX恢复14行"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110587-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110587-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110587-8.0.32.sql)

### mysql-110588-8.0.32 · Bug #110588

Timestamp cleanup error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110588](https://bugs.mysql.com/bug.php?id=110588)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug cleanup marker 断言；需记录 ONLY_FULL_GROUP_BY；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110590-8.0.32 · Bug #110590

Lateral join assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110590](https://bugs.mysql.com/bug.php?id=110590)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain/c531380明确debug LATERAL断言；源SQLCREATE TABLEt3缺空格。缺debug并存在脚本转换缺口。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110594-8.0.32 · Bug #110594

Race condition between xa recover and xa start on Transaction_ctx object

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110594](https://bugs.mysql.com/bug.php?id=110594)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110597-8.0.32 · Bug #110597

Different results from equivalent queries

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110597](https://bugs.mysql.com/bug.php?id=110597)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c531587 demonstrates RIGHT JOIN null-extension makes two queries inequivalent. Original minimal case not reproducible; later test.sql attachment required, but even mismatch alone does not establish Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110600-8.0.32 · Bug #110600

optimize for page flush

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #110600](https://bugs.mysql.com/bug.php?id=110600)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 只讨论零页batch跳过dblwr::force_flush优化，How to repeat为read code；无SQL功能故障/稳定性能用例。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110633-8.0.32 · Bug #110633

Orphaned full-text indexes

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110633](https://bugs.mysql.com/bug.php?id=110633)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat N/A; missing physical orphaned FTS state or SQL sequence creating it. Screenshots and1812 error insufficient to reconstruct.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110656-8.0.32 · Bug #110656

Join query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110656](https://bugs.mysql.com/bug.php?id=110656)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- INSERT IGNORE 构造零 DATETIME；MySQL 对零日期 IS NULL 存在兼容语义，需冻结 SQL_MODE/sql_auto_is_null 与此场景的预期规则，再裁定该返回行是否 bug；不能仅以PK非NULL推定。
- {"point": "零 DATETIME 的 IS NULL 兼容语义未确定。", "evidence": "cmain/c531717/c540098 涉及 INSERT IGNORE 产生零值、JOIN USING 和 DATETIME PK；PK 非NULL本身不足以排除零日期兼容规则。", "needed": "目标 SQL_MODE、sql_auto_is_null、实际插入值和零日期/ODBC兼容规则。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110658-8.0.32 · Bug #110658

mysql_binlog_xxx() symbols are not exported in lybmysqlclient.so

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110658](https://bugs.mysql.com/bug.php?id=110658)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110662-8.0.32 · Bug #110662

global_connection_memory_limit & connection_memory_limit documented incorrectly

官方版本字段：8.0.28-8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110662](https://bugs.mysql.com/bug.php?id=110662)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110663-8.0.32 · Bug #110663

Pagetracking return null data if checkpoint LSN is less than page tracking start

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110663](https://bugs.mysql.com/bug.php?id=110663)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110668-8.0.32 · Bug #110668

Innodb crash recovery too slow if have wide table redo during apply phase

官方版本字段：5.7.26, 5.7.29, 8.0.32

状态：证据不足；阶段：reviewed_source_variant_mismatch

官方报告：[Bug #110668](https://bugs.mysql.com/bug.php?id=110668)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Reporter c531599 confirms upstream8.0.32 has no issue; local modified dummy-index caching caused regression. Original modified source unavailable and not stock-target bug evidence.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110672-8.0.32 · Bug #110672

QUOTE function doesn't work as expected on tables that are utf16

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110672](https://bugs.mysql.com/bug.php?id=110672)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："utf16表QUOTE(NULL)转成乱码而latin1正常；NULL位HEX与CHARSET共同证明，不能把SQL NULL当文本NULL"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110672-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110672-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110672-8.0.32.sql)

### mysql-110676-8.0.32 · Bug #110676

mysqld got signal 11 after update from 8.0.31 to 8.0.32

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110676](https://bugs.mysql.com/bug.php?id=110676)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110677-8.0.32 · Bug #110677

Prepared statement assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110677](https://bugs.mysql.com/bug.php?id=110677)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- PREPARE format_bytes(NULL) 的 MYSQL_TYPE_INVALID debug 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110678-8.0.32 · Bug #110678

oct query with wrong result

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110678](https://bugs.mysql.com/bug.php?id=110678)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Target expression compares OCT(date) to generated TINYBLOB from TIME; verifier and reporter disagree on semantics/result. Requires resolving typed comparison oracle plus original debug/sanitizer/startup conditions.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110696-8.0.32 · Bug #110696

A Query with utf8 string literal returns empty set.

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110696](https://bugs.mysql.com/bug.php?id=110696)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110701-8.0.32 · Bug #110701

Unable to connect to localhost in DEV

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110701](https://bugs.mysql.com/bug.php?id=110701)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Only Not able to connect; missing Workbench log, connection endpoint/settings, server startup evidence and reproducible steps.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110702-8.0.32 · Bug #110702

In-place upgrading from 5.7.41 to 8.0.32, a table with FK's data is broken

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110702](https://bugs.mysql.com/bug.php?id=110702)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110703-8.0.32 · Bug #110703

SQL execute return error "BIGINT UNSIGNED value is out of range"

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110703](https://bugs.mysql.com/bug.php?id=110703)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Unsigned subtraction 24-162 correctly raises 1690; c531672 explicitly normal behavior. Do not convert expected range error into Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110706-8.0.32 · Bug #110706

Data will be lost when the table structure is rebuilt.

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110706](https://bugs.mysql.com/bug.php?id=110706)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110709-8.0.32 · Bug #110709

Chinese query conditions unable to return results correctly

官方版本字段：MySQL Community Server 8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110709](https://bugs.mysql.com/bug.php?id=110709)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL view filtered result empty initially, pushdown-off returns the one source cow row.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：8.0.31 初始及 pushdown-off 控制均返回唯一 (1,牛)；8.0.32 初始为空，关闭 pushdown 后恢复同一行。相同 source/postcheck 和环境，满足前版正常目标异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110709-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110709-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110709-8.0.32.sql)

### mysql-110720-8.0.32 · Bug #110720

Contribute by tencent: prepared statement can't execute match+rollup twice.

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110720](https://bugs.mysql.com/bug.php?id=110720)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain要求hypergraph_optimizer=on；c531739/c531741明确普通release返回3999且debug才适用。当前构建不具备该条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110733-8.0.32 · Bug #110733

RESET statement assertion error

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110733](https://bugs.mysql.com/bug.php?id=110733)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original RESET assertion requires debug plus GTID/binlog/replication-related statement sequence; developer unable to reproduce reduced case. Need exact original session protocol and expected assertion, dedicated target startup.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110765-8.0.32 · Bug #110765

Function returns incorrect value inside a session

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110765](https://bugs.mysql.com/bug.php?id=110765)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Missing table1/table2 DDL and data; LIMIT 1 without ORDER BY plus unknown concurrent DML prevents deterministic oracle; later verification still says no repeatable case.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110773-8.0.32 · Bug #110773

group_replication start faild use different ips and same port on same server

官方版本字段：mysql 8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110773](https://bugs.mysql.com/bug.php?id=110773)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110804-8.0.32 · Bug #110804

sql as "select count(*) from table" can't be logged in the slow query log.

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #110804](https://bugs.mysql.com/bug.php?id=110804)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需慢日志启用、min_examined_row_limit、long_query_time及足够长COUNT数据集；正文没有建表/数据/确切阈值与日志控制步骤，不能保证触发原现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110820-8.0.32 · Bug #110820

Instance backup lock interferes with Performance Schema TRUNCATE TABLE

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110820](https://bugs.mysql.com/bug.php?id=110820)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110825-8.0.32 · Bug #110825

Explicit COLLATE clause output in SHOW CREATE TABLE incorrectly

官方版本字段：8.0.32

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110825](https://bugs.mysql.com/bug.php?id=110825)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："第一次仅显式COLLATE，再构造后额外出现CHARACTER SET utf8mb4；元数据相同"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110825-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-110825-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110825-8.0.32.sql)

### mysql-110880-8.0.32 · Bug #110880

XA COMMIT at before_commit return fail breaks group replication recovery

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110880](https://bugs.mysql.com/bug.php?id=110880)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110889-8.0.32 · Bug #110889

binlog rotate optimize

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110889](https://bugs.mysql.com/bug.php?id=110889)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat is read code; binlog rotate optimization has no concrete workload or target-only performance threshold.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110922-8.0.32 · Bug #110922

Contribution by Tencent: missing --valgrind option in default.daily-valgrind

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_runtime_source_issue

官方报告：[Bug #110922](https://bugs.mysql.com/bug.php?id=110922)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer explains integration runner adds valgrind flags automatically; absence from collection file is intentional, no runtime bug oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110940-8.0.32 · Bug #110940

Querying VarChar column using 0 in WHERE clause incorrectly returns ALL ROWS

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110940](https://bugs.mysql.com/bug.php?id=110940)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- String-to-numeric0 conversion is MySQL coercion behavior; result across nonnumeric strings not established defect; official confirms weak typing by design.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110941-8.0.32 · Bug #110941

mysql server not cleaning up certain queries on TCP disconnections

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110941](https://bugs.mysql.com/bug.php?id=110941)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110955-8.0.32 · Bug #110955

Query the union all derived table error: the character set cannot be converted

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_sql_repair_needed

官方报告：[Bug #110955](https://bugs.mysql.com/bug.php?id=110955)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain CREATE t1但INSERT test_t2，表名不一致；需单独修订并保留原文哈希、确认是笔误。其他SQL和utf8mb4要求完整，c532346关联109699。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110968-8.0.32 · Bug #110968

Table rewrite happens when increasing a varchar length past 63

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110968](https://bugs.mysql.com/bug.php?id=110968)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UTF8MB4 VARCHAR63->64 crosses255-byte length storage boundary; copy is expected. Report requests documentation clarification, not wrong result.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110972-8.0.32 · Bug #110972

Innodb Fulltext search returns incorrect results when kill and restart mysqld

官方版本字段：8.0.32

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110972](https://bugs.mysql.com/bug.php?id=110972)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 必须kill -9专属mysqld并恢复同datadir，再对FTS删除标志/新行核对；现脚本只有恢复后阶段，重启/耐久配置与完整FTS协议未建立。保留真实强制终止目的，不执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111063-8.0.32 · Bug #111063

Assert: !dummy_big_rec on rollback of delete or update of row_format=compressed.

官方版本字段：5.7.42, 8.0.31, 8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111063](https://bugs.mysql.com/bug.php?id=111063)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111085-8.0.32 · Bug #111085

The sql-mode from my.ini is not read

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111085](https://bugs.mysql.com/bug.php?id=111085)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c532704指出配置文件并非默认读取位置，应--defaults-file指定；原Windows服务启动参数未知，不能把配置未读直接认Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111088-8.0.32 · Bug #111088

src tarball made from github repo and provided in src.rpm files is not the same

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111088](https://bugs.mysql.com/bug.php?id=111088)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Report concerns generated-file differences between source archives, not a SQL replay. Requires exact source packages and generation/build provenance to establish packaging oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111101-8.0.32 · Bug #111101

Join by index returns incorrect results

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111101](https://bugs.mysql.com/bug.php?id=111101)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Mixed DECIMAL/TEXT index versus scan behavior remains disputed in official comments; normal conversion warnings are not Bug. Need independently established typed comparison semantics and required plan.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111109-8.0.32 · Bug #111109

mysqld --print-defaults doesn't display set persist variables

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111109](https://bugs.mysql.com/bug.php?id=111109)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer states --print-defaults is not the interface for persisted settings; claimed missing-output oracle does not establish a defect.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111172-8.0.32 · Bug #111172

X protocol does not report "too many connections"

官方版本字段：8.0.32, 8.0.36

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111172](https://bugs.mysql.com/bug.php?id=111172)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires mysqlsh X Protocol client, two connections by a non-root account, mysqlx plugin and max_connections setting; ordinary SQL protocol runner cannot validate EOF versus expected 1040.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111176-8.0.32 · Bug #111176

View including union does not work when searching for multi-byte values.

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111176](https://bugs.mysql.com/bug.php?id=111176)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111190-8.0.32 · Bug #111190

Build fails with LANG=ja_JP.UTF-8

官方版本字段：8.0.31, 8.0.32, 8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111190](https://bugs.mysql.com/bug.php?id=111190)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Failure occurs compiling under ja_JP.UTF-8 locale due to readelf parsing; requires frozen source/build toolchain and locale, not database SQL replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111231-8.0.32 · Bug #111231

cannot access a disposed object Progress Bar

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111231](https://bugs.mysql.com/bug.php?id=111231)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Workbench disposed ProgressBar exception has no repeatable steps or client UI state; report explicitly cannot provide repeatable case.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111261-8.0.32 · Bug #111261

Skip scan results in wrong query results

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111261](https://bugs.mysql.com/bug.php?id=111261)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确必须debug并设置GLOBAL innodb_purge_stop_now，需delete-marked跨页未purge及skip scan计划。当前release、普通低资源协议未满足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111272-8.0.32 · Bug #111272

Inconsistent behaviors on string comparison with/without index

官方版本字段：8.0.32, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111272](https://bugs.mysql.com/bug.php?id=111272)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："有前缀索引只返回 1 行，无索引返回 2 行。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111272-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111272-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111272-8.0.32.sql)

### mysql-111302-8.0.32 · Bug #111302

Returns OK in Message

官方版本字段：8.0.32 build 2612062 CE (64 bits)

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111302](https://bugs.mysql.com/bug.php?id=111302)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Slow view UNION report omits schema/data dump and exact SELECT; no executable reproducer or bounded performance oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111308-8.0.32 · Bug #111308

inconsistent query result when different Hash Join order

官方版本字段：8.0.32-debug

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111308](https://bugs.mysql.com/bug.php?id=111308)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111363-8.0.32 · Bug #111363

If you use "UNION ALL" for items with Japanese double-byte characters in a subqu

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #111363](https://bugs.mysql.com/bug.php?id=111363)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- UNION ALL equality on Japanese あ is empty with warning1300 under initial pushdown=on; disabling pushdown returns two identical source rows.

相邻比较：8.0.31 → 8.0.32，前版正常、目标异常。

保存的比较依据：两侧初始 derived_condition_pushdown=on 已实测；8.0.31 初始和 off 控制都返回两行 あ，无转换警告；8.0.32 初始空集并有1300警告，off 才恢复两行。支持 8.0.31→8.0.32 行为边界，保留与 #109699 的重复报告关系。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111363-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-111363-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111363-8.0.32.sql)

### mysql-111420-8.0.32 · Bug #111420

DB instance restarted with AWS RDS database

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111420](https://bugs.mysql.com/bug.php?id=111420)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- AWS RDS busy-website restart report lacks database dump, triggering workload and repeatable resource protocol; cannot reproduce from stack and instance memory sizes alone.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111435-8.0.32 · Bug #111435

Hash join results in incorrect query results

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111435](https://bugs.mysql.com/bug.php?id=111435)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires two_table_data.rar containing exact tbl_1_all_type2index.sql and tbl_2_all_type2index.sql, not present in supplied per-item materials; query/EXPLAIN transcript cannot recreate 107 source rows.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111442-8.0.32 · Bug #111442

misleading startup error message related to GTID configuration

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111442](https://bugs.mysql.com/bug.php?id=111442)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111476-8.0.32 · Bug #111476

The value for field update_time of information_schema.tables is lost

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111476](https://bugs.mysql.com/bug.php?id=111476)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Maintainer specifies information_schema UPDATE_TIME valid only during current server uptime; NULL after restart is expected rather than wrong-result oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111540-8.0.32 · Bug #111540

binlog compress optimize

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111540](https://bugs.mysql.com/bug.php?id=111540)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires exact std_data/binlog_compression.gz, binlog compression settings and event-size measurement; ordinary SQL runner lacks input file and binlog oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111554-8.0.32 · Bug #111554

Index on float column causes confusing results

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111554](https://bugs.mysql.com/bug.php?id=111554)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 同值FLOAT/字符串IF混合比较存在精度与类型转换争议，官方Not a bug且作者承认歧义；需独立类型与索引访问契约后再定错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111610-8.0.32 · Bug #111610

Apparent corruption of an index page to be written to data file.

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111610](https://bugs.mysql.com/bug.php?id=111610)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Reporter cannot repeat corruption; logs identify Percona8.0.32-24 after upgrade and omit triggering data/workload. Need original datadir and reproducible sequence; plain Oracle version does not establish matching provenance.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111616-8.0.32 · Bug #111616

Failed to upgrade from 5.7 to 8.0 because of spatial column with BTREE index

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111616](https://bugs.mysql.com/bug.php?id=111616)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111685-8.0.32 · Bug #111685

ADD PARTITION with DATA DIRECTORY forces relocation of other partitions

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111685](https://bugs.mysql.com/bug.php?id=111685)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111696-8.0.32 · Bug #111696

The end range of where clause will clear the index->search_info->hash_analysis

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111696](https://bugs.mysql.com/bug.php?id=111696)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111700-8.0.32 · Bug #111700

LIMIT values are not adequately handled in EXPLAIN.

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111700](https://bugs.mysql.com/bug.php?id=111700)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires original million-row dataset and calibrated performance/cost oracle; EXPLAIN estimated costs need not rank different execution times. Data generator and controlled timing conditions absent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111710-8.0.32 · Bug #111710

Mysql 8 Role Issue

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111710](https://bugs.mysql.com/bug.php?id=111710)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111802-8.0.32 · Bug #111802

Updates to transient stats are not taken into affect for I_S views.

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111802](https://bugs.mysql.com/bug.php?id=111802)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111848-8.0.32 · Bug #111848

libmysqlclient.a missing on mysql-devel-8.0.32-1.module_el8.8.0+3567+56a616e4.aa

官方版本字段：8.0.32-1

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111848](https://bugs.mysql.com/bug.php?id=111848)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111851-8.0.32 · Bug #111851

Spatial index not used for join when field is used in MBRIntersects call

官方版本字段：8.0.32, 8.0.34, 5.7.43

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111851](https://bugs.mysql.com/bug.php?id=111851)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- EXPLAIN shows Range checked for each record for variable spatial bounds, unlike constant-filter range plan. Plan difference alone does not prove index is unused at runtime; requires validated index-use contract/runtime observation rather than labeling different plans wrong results.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111878-8.0.32 · Bug #111878

SELECT ROUND(X,D) result below expection

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111878](https://bugs.mysql.com/bug.php?id=111878)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111883-8.0.32 · Bug #111883

SELECT ROUND(X,D) result below expection

官方版本字段：8.0.22-8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111883](https://bugs.mysql.com/bug.php?id=111883)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer c534808 explains div_precision_increment and evaluation order; 0.3333 from ROUND(1/3,9) is expected decimal behavior, no accepted defect oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111888-8.0.32 · Bug #111888

'alter table xxx import tablespace' lead server crash

官方版本字段：8.0.32, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111888](https://bugs.mysql.com/bug.php?id=111888)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111899-8.0.32 · Bug #111899

json generated column null problem

官方版本字段：8.0.32, 8.0.34, 5.7.43

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #111899](https://bugs.mysql.com/bug.php?id=111899)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Target error1048 is clear, but normal NOT NULL validation-stage behavior needs a separate oracle review; not blanket execution failure.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111991-8.0.32 · Bug #111991

index merge sometimes return incorrect result

官方版本字段：8.0.32,8.1.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #111991](https://bugs.mysql.com/bug.php?id=111991)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112012-8.0.32 · Bug #112012

[Warning] [MY-011825] [InnoDB]

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #112012](https://bugs.mysql.com/bug.php?id=112012)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c535168明确缺表定义/产生警告的语句；警告可能为新增正常信息。需原DDL、数据、升级流程及错误语义，不以警告出现计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112037-8.0.32 · Bug #112037

Contribute by tencent: explain analyze show never executed for materialize

官方版本字段：8.0.32, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112037](https://bugs.mysql.com/bug.php?id=112037)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：两侧 EXPLAIN ANALYZE 均显示派生表扫描已产生一行，但物化/聚合及其子树为 never executed；实际查询均为11,12,13,14，输入1–4。仅实际计时不同，计划结构及诊断矛盾相同；8.0.31 已有该诊断现象，不计 wrong_result 或性能差异。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-112037-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-112037-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112037-8.0.32.sql)

### mysql-112109-8.0.32 · Bug #112109

The mysql8 client displays hexadecimal data

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112109](https://bugs.mysql.com/bug.php?id=112109)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112188-8.0.32 · Bug #112188

Fail to import tablespace after upgrade

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112188](https://bugs.mysql.com/bug.php?id=112188)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112415-8.0.32 · Bug #112415

Unable to connect to the server

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #112415](https://bugs.mysql.com/bug.php?id=112415)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 正文仅连接帮助请求，How to repeat为i dont understand，后无反馈；缺连接命令/地址类型/错误/客户端日志。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112421-8.0.32 · Bug #112421

zero and null value, left or right join result wrong

官方版本字段：8.0.32

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #112421](https://bugs.mysql.com/bug.php?id=112421)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Both input tables contain exactly decimal zero and NULL. LEFT JOIN returns three rows including an erroneous additional zero/NULL unmatched row; RIGHT JOIN similarly returns three rows.

相邻比较：8.0.31 → 8.0.32，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："Source tables each exactly {0.00,NULL}; LEFT JOIN gives multiset {(0.00,NULL),(0.00,0.00),(NULL,NULL)} as reported. Right-join output retained separately."

边界审查：[experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-112421-8.0.32/review.json](../../experiments/saved_20261029/version_boundary_20261029/v32/cases/mysql-112421-8.0.32/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112421-8.0.32.sql)

### mysql-112423-8.0.32 · Bug #112423

select information_schema.columns use any result error

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #112423](https://bugs.mysql.com/bug.php?id=112423)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 缺56张表定义，且第二查询只按table_name过滤未限制外层schema，不能要求等于第一条按schema计列数；c536223 Not a bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112673-8.0.32 · Bug #112673

dump from slave with --dump-slave or --dump-replica option will change binlog

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112673](https://bugs.mysql.com/bug.php?id=112673)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs configured replica with GTID/binlog plus matching mysqldump and mysqlbinlog; original table definition and exact dump command/database are incomplete. Binlog changes under FLUSH require semantic attribution.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112874-8.0.32 · Bug #112874

Mysql fails to rollback after invalid undo record

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112874](https://bugs.mysql.com/bug.php?id=112874)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Aurora managed upgrade crash has no trigger or datadir; reporter explicitly does not know cause and maintainer identifies Amazon-modified build. Cannot substitute Oracle target release for original environment.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112897-8.0.32 · Bug #112897

next-transaction isolation level has problem if current transaction end by begin

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112897](https://bugs.mysql.com/bug.php?id=112897)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires two/three sessions with pending transaction and NEXT versus SESSION isolation, while official discussion disagrees and changes SET scope. Need preserve exact transaction interleaving and settle scope oracle before replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112965-8.0.32 · Bug #112965

A warning is issued that the FOUND_ROWS() function is deprecated when used alone

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112965](https://bugs.mysql.com/bug.php?id=112965)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- FOUND_ROWS deprecation warning applies independently of SQL_CALC_FOUND_ROWS; official comment rejects claimed warning oracle. Normal warning is not Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113054-8.0.32 · Bug #113054

mysql explain filtered inaccurate when find_in_set function used

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113054](https://bugs.mysql.com/bug.php?id=113054)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113343-8.0.32 · Bug #113343

Expression #1 of ORDER BY is not in SELECT / incompatible with DISTINCT (#3065)

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113343](https://bugs.mysql.com/bug.php?id=113343)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Random Access2016/ODBC8.2 error lacks database dump, exact server SQL and deterministic client interaction; Access query text is not equivalent to transmitted MySQL statements.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113393-8.0.32 · Bug #113393

MySQL Server locks up randomly

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113393](https://bugs.mysql.com/bug.php?id=113393)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Reporter states unknown reproduction and production-only high-write hang after days/weeks; missing deterministic workload/data/configuration. Existing monitor traces cannot replace trigger.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113516-8.0.32 · Bug #113516

rejoin cluster failure as clone plugin is waiting for table metadata lock

官方版本字段：8.0.32, 8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113516](https://bugs.mysql.com/bug.php?id=113516)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires gr_xa_clone_rejoin_failure.test attachment, MTR and Group Replication/clone multi-node topology plus detached XA locking schedule. Single isolated MySQL instance cannot satisfy it.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113518-8.0.32 · Bug #113518

character set with Chinese character,using storage procedure it report 1300 err

官方版本字段：8.0.32, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113518](https://bugs.mysql.com/bug.php?id=113518)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113537-8.0.32 · Bug #113537

False match of multibyte chars when checking existence of a control character

官方版本字段：8.0.32

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #113537](https://bugs.mysql.com/bug.php?id=113537)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113537-8.0.32.sql)

### mysql-113640-8.0.32 · Bug #113640

no need to judge rseg in while loop

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113640](https://bugs.mysql.com/bug.php?id=113640)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Code cleanup of redundant conditional; c539716 confirms discovery only by code reading. No observable SQL bug or performance testcase/oracle provided.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113648-8.0.32 · Bug #113648

Reduced lock interval for purge_sys->pq_mutex

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113648](https://bugs.mysql.com/bug.php?id=113648)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Proposed lock optimization rather than original correctness failure; developer c542842 rejects proposed patch because it introduces a correctness issue. No baseline SQL failure testcase/oracle to replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113658-8.0.32 · Bug #113658

Avoid unnecessary copy operations with std::move()

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #113658](https://bugs.mysql.com/bug.php?id=113658)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- std::move减少trx_rseg_mem_create复制的源码优化，无可重复SQL故障oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113663-8.0.32 · Bug #113663

Crash occurs when applying binlog_transaction_dependency_tracking to slave node.

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113663](https://bugs.mysql.com/bug.php?id=113663)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Concurrent sysbench workload and changing GLOBAL binlog dependency tracking are essential; later c551404 gives 500 threads/60,000 seconds and enabled binary logging. This exceeds current PID/time/concurrency limits and ordinary --skip-log-bin runner. Need bounded approved multi-client reproduction protocol with full binlog settings.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113688-8.0.32 · Bug #113688

reduce memory usage for purge

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #113688](https://bugs.mysql.com/bug.php?id=113688)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 无二级索引时purge内存优化，仅要求read code，缺可执行负载和内存差异阈值。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113771-8.0.32 · Bug #113771

optimize for row_parse_int_from_field

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113771](https://bugs.mysql.com/bug.php?id=113771)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Only code optimization/read-the-code proposal supplied; no SQL-triggered failure or measurable performance oracle. Need an executable testcase and expected observation.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113776-8.0.32 · Bug #113776

optimize for btr_insert_into_right_sibling

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #113776](https://bugs.mysql.com/bug.php?id=113776)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- btr_insert_into_right_sibling计算/调用顺序优化，How to repeat仅read code；无SQL触发与判错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113818-8.0.32 · Bug #113818

optimize for buf_read_page_low

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #113818](https://bugs.mysql.com/bug.php?id=113818)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- sync=true跳过buf_read_page_low部分调用的代码优化，无SQL异常oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113843-8.0.32 · Bug #113843

prepared json query can not use index

官方版本字段：8.0.32, 8.0.36

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113843](https://bugs.mysql.com/bug.php?id=113843)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SQL/data and reported plan distinction complete, but index choice is cost-based and no correctness or performance failure oracle is supplied. Parameterized JSON path may prevent expression-index matching legitimately. Need intended optimizer contract and plan-cost interpretation before classifying a plan difference as Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114015-8.0.32 · Bug #114015

'Undo log record is to big error' when updating column

官方版本字段：8.0.32, 8.036, 8.3

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #114015](https://bugs.mysql.com/bug.php?id=114015)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114056-8.0.32 · Bug #114056

Performance degredation using REGEXP in statement with parameters vs query

官方版本字段：8.0.32, 8.0.22+

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114056](https://bugs.mysql.com/bug.php?id=114056)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114074-8.0.32 · Bug #114074

optimize for Writeset_trx_dependency_tracker::get_dependency

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #114074](https://bugs.mysql.com/bug.php?id=114074)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-code optimization only: use emplace/map operation consolidation. No SQL correctness failure or reproducible timing workload/oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114222-8.0.32 · Bug #114222

Assertion failure: row0mysql.cc:2332:node->pcur->m_rel_pos == BTR_PCUR_ON

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114222](https://bugs.mysql.com/bug.php?id=114222)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114267-8.0.32 · Bug #114267

Getting different results when executing the same SQL statement about json

官方版本字段：8.0.32, 8.0.36

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #114267](https://bugs.mysql.com/bug.php?id=114267)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Missing pt2 DDL; developer c541301 identifies parameter JSON conversion rules as expected. Need schema and verified type contract; normal 3140 not Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114374-8.0.32 · Bug #114374

InnoDB semaphore wait bug - a thread is waiting for itself?

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114374](https://bugs.mysql.com/bug.php?id=114374)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114400-8.0.32 · Bug #114400

Create partition table with DATA DIRECTORY execution result is incorrect

官方版本字段：8.0.32, 8.0.36

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #114400](https://bugs.mysql.com/bug.php?id=114400)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL；原DATA DIRECTORY相对路径/首次启动文件行为需专用新datadir及目录审查，单列安全影响，不尝试改名/绕过。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\114400\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114654-8.0.32 · Bug #114654

when pstress，mysqld crash Assertion failure: buf0lru.cc:2168 thread 281472055363

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114654](https://bugs.mysql.com/bug.php?id=114654)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114736-8.0.32 · Bug #114736

performance_schema.binary_log_transaction_compression_stats with wrong timestamp

官方版本字段：8.0.32, 8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114736](https://bugs.mysql.com/bug.php?id=114736)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114776-8.0.32 · Bug #114776

mysqlbinlog cannot print geometry correct

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114776](https://bugs.mysql.com/bug.php?id=114776)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114809-8.0.32 · Bug #114809

inconsistent page no in btr_pcur_t's move_to_next_page

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114809](https://bugs.mysql.com/bug.php?id=114809)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115045-8.0.32 · Bug #115045

Async connection failover crash on group_replication member

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115045](https://bugs.mysql.com/bug.php?id=115045)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115047-8.0.32 · Bug #115047

XA_prepare_log_event holds an invalid XID

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115047](https://bugs.mysql.com/bug.php?id=115047)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115132-8.0.32 · Bug #115132

group by with COLLATE return unexpected result

官方版本字段：8.0.32

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #115132](https://bugs.mysql.com/bug.php?id=115132)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL；c543692/c543716澄清COUNT与TempTable/MEMORY对照，需之后完整转写。保留不执行。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\115132\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115244-8.0.32 · Bug #115244

apply an redo on page in file mysql.ibd caused crashes

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115244](https://bugs.mysql.com/bug.php?id=115244)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115313-8.0.32 · Bug #115313

hash join when have index and push condition to driver table lead to table scan

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115313](https://bugs.mysql.com/bug.php?id=115313)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115351-8.0.32 · Bug #115351

page tracking cannot find stop point

官方版本字段：mysql-8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115351](https://bugs.mysql.com/bug.php?id=115351)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115380-8.0.32 · Bug #115380

Update Multiple table failed when table is partitioned and using MRR path

官方版本字段：8.0.32, 8.0.37

状态：证据不足；阶段：baseline_preserved

官方报告：[Bug #115380](https://bugs.mysql.com/bug.php?id=115380)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-115380-8.0.32.sql)

### mysql-115843-8.0.32 · Bug #115843

The incorrect calculation of 'select_limit' led to an incorrect index selection

官方版本字段：8.0.32, 8.0.39

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115843](https://bugs.mysql.com/bug.php?id=115843)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115951-8.0.32 · Bug #115951

ALTER TABLE ... IMPORT TABLESPACE may cause unsafe reads

官方版本字段：8.0.32, 8.0.39, 8.4.2

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115951](https://bugs.mysql.com/bug.php?id=115951)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116144-8.0.32 · Bug #116144

Crash during recovery

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116144](https://bugs.mysql.com/bug.php?id=116144)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116167-8.0.32 · Bug #116167

mysql server was crashed

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116167](https://bugs.mysql.com/bug.php?id=116167)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116221-8.0.32 · Bug #116221

Corruption of an index tree. Assertion failure: btr0btr.cc:702

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116221](https://bugs.mysql.com/bug.php?id=116221)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116277-8.0.32 · Bug #116277

Insert rounds datetime/timestamp fractions instead of truncating

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116277](https://bugs.mysql.com/bug.php?id=116277)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116454-8.0.32 · Bug #116454

For mysql8.0.32 DEBUG version,it crash when do sql about ANALYZE TABLE USING DAT

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116454](https://bugs.mysql.com/bug.php?id=116454)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116515-8.0.32 · Bug #116515

For mysql8.0.32 version,the skip scan result is different when condition is same

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116515](https://bugs.mysql.com/bug.php?id=116515)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116566-8.0.32 · Bug #116566

List partition prune get a wrong result

官方版本字段：8.0.32, 8.0.40, 8.4.3, 9.1.0

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #116566](https://bugs.mysql.com/bug.php?id=116566)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SELECT returns correct empty set; reported issue is missed partition-pruning optimization. Need accepted plan/performance oracle; cannot label wrong result. Source also has unterminated version comment.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116795-8.0.32 · Bug #116795

get_oldest_view cost too much and block other oprator

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116795](https://bugs.mysql.com/bug.php?id=116795)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116796-8.0.32 · Bug #116796

get_oldest_view cost too much and block other oprator

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116796](https://bugs.mysql.com/bug.php?id=116796)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116806-8.0.32 · Bug #116806

Support flashback

官方版本字段：8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #116806](https://bugs.mysql.com/bug.php?id=116806)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117132-8.0.32 · Bug #117132

drived_merge optimization error

官方版本字段：8.0.32

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #117132](https://bugs.mysql.com/bug.php?id=117132)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Nondeterministic expressions may be re-evaluated after derived merging; author corrects hint-on result. Need established single-evaluation contract before treating differing UUID/RAND/SYSDATE as defect.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117155-8.0.32 · Bug #117155

drived_merge optimization error

官方版本字段：8.0.32, 8.0.40

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #117155](https://bugs.mysql.com/bug.php?id=117155)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- derived_merge导致非确定函数多次求值的同值期望需契约核验；UUID/RAND/SYSDATE差异不能未经说明直接判Bug，保留源控制hint等待语义确认。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117187-8.0.32 · Bug #117187

Cannot convert string '\xA0' from binary to utf8mb4

官方版本字段：8.0.32, 8.0.39, 8.0.40, 8.4.3

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #117187](https://bugs.mysql.com/bug.php?id=117187)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- CHAR(160) is binary byte A0 and invalid standalone UTF-8; developer c549930 confirms conversion error is correct, later charset workarounds do not make original error a Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117328-8.0.32 · Bug #117328

Innodb FATAL [MY-013622] fsync() returned EIO with [MY-013183] Assertion failure: os0file.cc

官方版本字段：8.0.32-commercial

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117328](https://bugs.mysql.com/bug.php?id=117328)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117421-8.0.32 · Bug #117421

Redundant row-level locking for using order DESC

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117421](https://bugs.mysql.com/bug.php?id=117421)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117459-8.0.32 · Bug #117459

Cross DDL operations on MySQL partitioned tables, parallel COUNT(*) does not report errors.

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117459](https://bugs.mysql.com/bug.php?id=117459)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117783-8.0.32 · Bug #117783

optimizer selects the wrong index due to the "low_limit" mechanism

官方版本字段：8.0.32, 8.0.41

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117783](https://bugs.mysql.com/bug.php?id=117783)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117917-8.0.32 · Bug #117917

InnoDB: Failing assertion: lock->lock_word == X_LOCK_DECR

官方版本字段：8.0.32、5.7.44

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117917](https://bugs.mysql.com/bug.php?id=117917)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117999-8.0.32 · Bug #117999

crash when json_binary::parse_binary

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117999](https://bugs.mysql.com/bug.php?id=117999)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118499-8.0.32 · Bug #118499

.mylogin.cnf covered the command line

官方版本字段：mysql-8.0.32

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #118499](https://bugs.mysql.com/bug.php?id=118499)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118787-8.0.32 · Bug #118787

MySQL server crashed

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #118787](https://bugs.mysql.com/bug.php?id=118787)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118956-8.0.32 · Bug #118956

Incorrect result when condition use concat function

官方版本字段：8.0.32+

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #118956](https://bugs.mysql.com/bug.php?id=118956)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119458-8.0.32 · Bug #119458

server cannot restart after crash when relay_log_recovery=1 and have both mgr and normal slave

官方版本字段：8.0.32, 8.4.4

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #119458](https://bugs.mysql.com/bug.php?id=119458)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120185-8.0.32 · Bug #120185

Assertion Failure in add_key_fields with Nested CTE

官方版本字段：8.0.32-debug

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #120185](https://bugs.mysql.com/bug.php?id=120185)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120297-8.0.32 · Bug #120297

query_term.cc:320 assert(false) crash — UNION query triggers unhandled AccessPath

官方版本字段：8.0.32

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #120297](https://bugs.mysql.com/bug.php?id=120297)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确SET SESSION debug=+d,ast与debug打印dumpAccessPath断言；当前release不支持此变量，普通COUNT UNION成功不能完成该报告验证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120414-8.0.32 · Bug #120414

InnoDB performance regression because of validate_rec_offset

官方版本字段：8.0.32 - 9.7

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #120414](https://bugs.mysql.com/bug.php?id=120414)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120638-8.0.32 · Bug #120638

The value of Rows_examined is incorrect when there is a query involving a union of derived tables

官方版本字段：8.0.32

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #120638](https://bugs.mysql.com/bug.php?id=120638)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-107115-8.0.33 · Bug #107115

??at the end of the error mecessage after setting Chinese characters to variable

官方版本字段：8.0.27, 8.0.28, 8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #107115](https://bugs.mysql.com/bug.php?id=107115)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文要求SET GLOBAL及原始错误包字节/UTF8边界审查；属于全局状态与错误消息编码专门实验，不纳入普通SQL批次。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109401-8.0.33 · Bug #109401

Rows_query_log_event truncates query due to treating query as C string

官方版本字段：8.0.31, 5.7.40, 8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #109401](https://bugs.mysql.com/bug.php?id=109401)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需要启用ROW binlog/rows_query日志，按长度发送真实NUL及读取隔离实例binlog原始载荷；普通mysql文本客户端和当前默认实例未建立这些条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109668-8.0.33 · Bug #109668

XCom connection stalled forever in read() syscall over network

官方版本字段：8.0.27, 8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #109668](https://bugs.mysql.com/bug.php?id=109668)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires three-node GR with SSL and deliberate connection to GR communications port while restarting joiner, verified in c533421. Single network-none instance cannot satisfy topology.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110722-8.0.33 · Bug #110722

Failed to upgrade from 5.7 to 8.0 because of orphan tmp tables created in 5.6

官方版本字段：5.7, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110722](https://bugs.mysql.com/bug.php?id=110722)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110736-8.0.33 · Bug #110736

Build failure with Homebrew rapidjson installed & symlinked

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110736](https://bugs.mysql.com/bug.php?id=110736)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110745-8.0.33 · Bug #110745

Build failure with -DWITH_ZLIB=system

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110745](https://bugs.mysql.com/bug.php?id=110745)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Build-time CMake WITH_ZLIB=system scope failure; needs source build and system zlib development package, not SQL replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110748-8.0.33 · Bug #110748

window function with order by clause may lead to wrong results

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110748](https://bugs.mysql.com/bug.php?id=110748)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c531924指出窗口ROWS UNBOUNDED PRECEDING没有ORDER BY，行序不确定，外层排序不能要求相同累积和；原差异属于允许行为。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110752-8.0.33 · Bug #110752

el7 aarch64 might return invalid for value cache line causing crash during boot

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110752](https://bugs.mysql.com/bug.php?id=110752)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- EL7 aarch64/glibc2.17 cacheline reporting required; current Linux x86 release container cannot reproduce platform-specific startup crash.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110758-8.0.33 · Bug #110758

mysqldump uses FLUSH TABLES without NO_WRITE_TO_BINLOG option

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110758](https://bugs.mysql.com/bug.php?id=110758)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110760-8.0.33 · Bug #110760

uninstalling mysql

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110760](https://bugs.mysql.com/bug.php?id=110760)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110771-8.0.33 · Bug #110771

Failed to update NULL to empty value on instant col for REDUNDANT table

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110771](https://bugs.mysql.com/bug.php?id=110771)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：8.0.32 与目标 8.0.33 均成功执行 UPDATE，但 a=0 的 c 仍为 SQL NULL（c IS NULL=1、LENGTH=NULL），与应更新为空串的 oracle 不符；其余两行和 REDUNDANT 行格式控制一致。两侧关键环境及 optimizer_switch 一致；SHOW TABLE STATUS 的创建/更新时间不同属于各自干净实例的时间记录，不影响此判定。前版已有同样异常，不计为 debug 断言复现。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110771/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110771/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110771-8.0.33.sql)

### mysql-110774-8.0.33 · Bug #110774

'show replica status' set the field_flag of 'Second_Behind_Source' NOTNULL

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110774](https://bugs.mysql.com/bug.php?id=110774)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires replication status plus protocol field flags/Go driver behavior and connection state; plain SHOW text output cannot verify NOTNULL metadata.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110779-8.0.33 · Bug #110779

IN clause cause pick bad performan index

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110779](https://bugs.mysql.com/bug.php?id=110779)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110795-8.0.33 · Bug #110795

mysql insert is deadlocked

官方版本字段：8.0.27, 8.0.33, 5.7.42

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110795](https://bugs.mysql.com/bug.php?id=110795)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires exact two-session duplicate-key INSERT interleaving and lock graph; need concurrency harness and distinction between avoidable deadlock versus valid victim abort.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110805-8.0.33 · Bug #110805

Subquery assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110805](https://bugs.mysql.com/bug.php?id=110805)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 源文要求 debug，且已有 SQL 存在 CREATE TABLEt0 拼接缺空格，与原文 CREATE TABLE t0 不同；不执行该脚本。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110818-8.0.33 · Bug #110818

ANY assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110818](https://bugs.mysql.com/bug.php?id=110818)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain和c532046确认WITH_DEBUG/ASAN/UBSAN；c532047 release NULL为正常对照，不代替debug断言复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110819-8.0.33 · Bug #110819

EXISTS with dependent subquery can return incorrect results

官方版本字段：8.0.16+, 8.0.33

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #110819](https://bugs.mysql.com/bug.php?id=110819)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- EXISTS with initial semijoin=on returns only id2; disabling semijoin returns ids2,3 for the same three source rows.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："Initial semijoin enabled query returns id set {2}; semijoin-off control returns {2,3}. Ignore result order."

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110819/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110819/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110819-8.0.33.sql)

### mysql-110847-8.0.33 · Bug #110847

Prepared SELECT returns different results on consecutive executions.

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110847](https://bugs.mysql.com/bug.php?id=110847)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Two prepared LAST_VALUE executions over uids 100,101 must both return 1,1. Target second returns NULL,NULL; archived preceding version normal in three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110847/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110847/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110847-8.0.33.sql)

### mysql-110848-8.0.33 · Bug #110848

missing considering on order by and limit clause in cost calculation

官方版本字段：8.0.28, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110848](https://bugs.mysql.com/bug.php?id=110848)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110857-8.0.33 · Bug #110857

invalid NO_INDEX_USED=1 metric when using UNION in queries.

官方版本字段：8.0.30, 8.0.33, 5.7.42

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #110857](https://bugs.mysql.com/bug.php?id=110857)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- NO_INDEX_USED 是否应包含 UNION RESULT 临时扫描的指标契约未固定；只能采集指标和计划，不能据计划用了基表索引就宣布计数错。
- {"point": "NO_INDEX_USED 是否包含 UNION RESULT 的临时表扫描未确定。", "evidence": "cmain/c532041 是三个查询及 P_S 指标；源数据只有三行，优化器不保证选择 k_1。", "needed": "固定 instrumentation、当前线程 event_id、实际计划及指标统计范围契约。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110869-8.0.33 · Bug #110869

Debug build asserts in innodb.ddl_crash_alter_partition test

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110869](https://bugs.mysql.com/bug.php?id=110869)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires debug MTR innodb.ddl_crash_alter_partition and ddl_crash_statement.inc forced crash/recovery. Ordinary SQL cannot preserve injected crash phase.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110873-8.0.33 · Bug #110873

CMake checks for clang 15 need to be updated for Apple clang

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110873](https://bugs.mysql.com/bug.php?id=110873)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110874-8.0.33 · Bug #110874

Possible missing query error

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110874](https://bugs.mysql.com/bug.php?id=110874)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Outer-reference COUNT aggregation changes query scope; claimed row-count equivalence contested by verifier. Need scoping oracle before asserting missing error.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110906-8.0.33 · Bug #110906

Index creation assertion error 3

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110906](https://bugs.mysql.com/bug.php?id=110906)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug 功能索引聚合 fixed 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110915-8.0.33 · Bug #110915

Having clause missing scope

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110915](https://bugs.mysql.com/bug.php?id=110915)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：8.0.32 与8.0.33 均在指定 GROUP BY/HAVING 查询报1054/42S22 Unknown column t7.c0 in having clause；两个建表成功且数据控制均为0行，未出现初始化错误。该错误阶段及消息符合冻结 oracle，前版已有相同异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110915/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110915/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110915-8.0.33.sql)

### mysql-110918-8.0.33 · Bug #110918

Optimization not applied for IS NULL on NOT NULL column

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110918](https://bugs.mysql.com/bug.php?id=110918)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110931-8.0.33 · Bug #110931

Optimizer Trace contradicts to EXPLAIN contradicts to SHOW STATUS

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110931](https://bugs.mysql.com/bug.php?id=110931)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110941-8.0.33 · Bug #110941

mysql server not cleaning up certain queries on TCP disconnections

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110941](https://bugs.mysql.com/bug.php?id=110941)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110942-8.0.33 · Bug #110942

There is a discontinuity in the value of the AUTO_INCREMENT field

官方版本字段：5.7.26-log ,8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110942](https://bugs.mysql.com/bug.php?id=110942)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- AUTO_INCREMENT allocation may reserve unused values during INSERT SELECT; gaps alone not defect, verifier explicitly expected behavior.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110961-8.0.33 · Bug #110961

Subquery to derived optimizer assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110961](https://bugs.mysql.com/bug.php?id=110961)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain断言需debug+ASan+UBSan；后续release差异不是此静态断言oracle，不能混同；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110962-8.0.33 · Bug #110962

JOIN a table with trigger report unexpected WARNINGS

官方版本字段：5.7.42, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110962](https://bugs.mysql.com/bug.php?id=110962)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："中间 NULL UPDATE 的两条 1048 被错误保留到后续有效 UPDATE；中间 SELECT 后 SHOW WARNINGS 为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110962/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110962/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110962-8.0.33.sql)

### mysql-110969-8.0.33 · Bug #110969

Functional indexes aren't covering

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110969](https://bugs.mysql.com/bug.php?id=110969)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 只给DESC js与ALTER/EXPLAIN结果，无实际原始数据和性能负载；索引覆盖能力缺契约，需数据/查询成本与功能索引覆盖支持依据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110971-8.0.33 · Bug #110971

Optimizer: reverse index scan doesn't affect the cost

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #110971](https://bugs.mysql.com/bug.php?id=110971)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Equal cost for ASC reverse versus DESC index is optimizer cost-model concern; need accepted target-only cost/performance oracle and complete workload/material review.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110976-8.0.33 · Bug #110976

full-text index does not change when ngram parser changed

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110976](https://bugs.mysql.com/bug.php?id=110976)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- ngram parser及ngram_token_size/stopword配置尚未预检；源需比较INPLACE/COPY/分步重建，普通环境列表未证明该依赖。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110977-8.0.33 · Bug #110977

ANY query with wrong result 2

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #110977](https://bugs.mysql.com/bug.php?id=110977)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 作者TLP/空标量子查询NULL推理与c532441官方判断冲突；须核对ALL与空标量语义，当前不以三条空集直接定Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110979-8.0.33 · Bug #110979

Update assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110979](https://bugs.mysql.com/bug.php?id=110979)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug ROW binlog 条件，且已有 SQL 为 CREATE TABLEt0，与原文有差异；不执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110983-8.0.33 · Bug #110983

issue with window functions in stored procedures

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110983](https://bugs.mysql.com/bug.php?id=110983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Both procedure calls must preserve Aplus=A+1 and Bplus=B+1 on 12 rows. Target second call arithmetic diverges; archived preceding version normal three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110983/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110983/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110983-8.0.33.sql)

### mysql-110984-8.0.33 · Bug #110984

Subqueries with 'limit 1' cause concat strings to report errors

官方版本字段：8031, 5.7.42, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #110984](https://bugs.mysql.com/bug.php?id=110984)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：8.0.32 与8.0.33 均无 LIMIT 的 CONCAT 返回 yyy-xxx，而相同派生查询加 LIMIT 1 在第10行报1267/HY000、消息明确指向 concat 的 utf8mb4_0900_ai_ci/gbk_bin 混合；表内 xxx、CHARSET=gbk、COLLATION=gbk_bin 控制一致，错误不是字符集设置失败。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/110984/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/110984/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-110984-8.0.33.sql)

### mysql-110988-8.0.33 · Bug #110988

VIEW call error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #110988](https://bugs.mysql.com/bug.php?id=110988)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确debug+ASan+UBSan/Boost1.77；现有release不是所述构建；预期1356错误必须映射到成功CREATE后的SELECT，不可泛化报错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110990-8.0.33 · Bug #110990

Create function misleading error for SUPER privilege and log_bin_trust_function

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #110990](https://bugs.mysql.com/bug.php?id=110990)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires users/grants, DEFINER identity, binary log mode and function-creator trust settings. Need dedicated privilege-sensitive multi-login protocol; cannot conclude1419 is Bug in root replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110991-8.0.33 · Bug #110991

After server upgrade it does not start

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #110991](https://bugs.mysql.com/bug.php?id=110991)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- How to repeat明确have no clue；缺升级前datadir、升级顺序/并行任务和包版本配置，单次全新8.0实例启动不等价。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110993-8.0.33 · Bug #110993

Contribution by Tencent: Support instant modify column

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #110993](https://bugs.mysql.com/bug.php?id=110993)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110998-8.0.33 · Bug #110998

Performance regression with SELECT query when sorting on limited fields

官方版本字段：8.0.20+, 8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #110998](https://bugs.mysql.com/bug.php?id=110998)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires wp_ale_posts.sqldump.sql and3min target timings versus old-version baseline; absent dataset and current20s SQL cap; no target-only performance oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-110999-8.0.33 · Bug #110999

Unneeded sort after scanning the index

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #110999](https://bugs.mysql.com/bug.php?id=110999)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111011-8.0.33 · Bug #111011

`mysql_config --libs` returns broken zlib reference

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111011](https://bugs.mysql.com/bug.php?id=111011)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Homebrew build with system libs/zlib then mysql_config --libs; package/build metadata issue, not server SQL. Need matching source/build tooling.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111019-8.0.33 · Bug #111019

Erro ao tentar MySql Connections

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #111019](https://bugs.mysql.com/bug.php?id=111019)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Workbench首页类型错误及Rescan Python模块异常；缺客户端版本、平台/配置/日志和完整重现步骤，mysqld SQL不能代表。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111025-8.0.33 · Bug #111025

Different cost with index hint for same plan

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111025](https://bugs.mysql.com/bug.php?id=111025)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Same execution plan with different estimated costs has no stated accepted cost invariant or bounded runtime oracle; cost divergence alone is not a wrong result.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111027-8.0.33 · Bug #111027

Multi-column indexes with writest will cause HA_ERR_FOUND_DUPP_KEY

官方版本字段：5.7.42, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111027](https://bugs.mysql.com/bug.php?id=111027)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111043-8.0.33 · Bug #111043

Table data corrupt after upgrading MySql from 5.7.37 to MySql 8.0.33 version

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111043](https://bugs.mysql.com/bug.php?id=111043)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- In-place Windows upgrade from 5.7.37 followed by ALTER depends on original datadir, schema/data and exact ALTER, not supplied. Need frozen upgrade state and reproducer.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111044-8.0.33 · Bug #111044

Assertion failure in buf0buf.cc::Buf_fetch<T>::read_page()

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111044](https://bugs.mysql.com/bug.php?id=111044)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111062-8.0.33 · Bug #111062

Cannot disable TLS in MySQL 8.0.33

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111062](https://bugs.mysql.com/bug.php?id=111062)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer explains RSA key files are controlled separately from TLS. Need distinguish intended authentication-key creation from unsupported claimed no-files oracle; startup configuration alone does not establish Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111063-8.0.33 · Bug #111063

Assert: !dummy_big_rec on rollback of delete or update of row_format=compressed.

官方版本字段：5.7.42, 8.0.31, 8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111063](https://bugs.mysql.com/bug.php?id=111063)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111067-8.0.33 · Bug #111067

Query result error

官方版本字段：8.0.25, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111067](https://bugs.mysql.com/bug.php?id=111067)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："首次约 1.8859e-9，ALTER 后 0，ANALYZE 后恢复正分数。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111067/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111067/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111067-8.0.33.sql)

### mysql-111068-8.0.33 · Bug #111068

Lock failure

官方版本字段：8.0.25, 8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111068](https://bugs.mysql.com/bug.php?id=111068)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- ALTER TABLE in connection A implicitly commits its earlier transaction; subsequent insert in connection B is therefore not evidence of a lock failure.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111072-8.0.33 · Bug #111072

The subquery involves JSON, and the execution result is incorrect.

官方版本字段：8.0.33, 5.7.42, 8.0.36

状态：证据不足；阶段：reviewed_attachment_needed

官方报告：[Bug #111072](https://bugs.mysql.com/bug.php?id=111072)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 正文查询与期望完整，缺附件table.txt中的建表/全部JSON和binary输入；已定位官方附件32263，待获取核验。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111074-8.0.33 · Bug #111074

start replica encounter Slave_SQL_Running NO with MY-013117 (null)

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111074](https://bugs.mysql.com/bug.php?id=111074)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Bidirectional replication failure after upgrade has no supplied reproducer; exact topology, replication positions, data and triggering workload are missing.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111089-8.0.33 · Bug #111089

MySqlDataReader in C# does not recognize double backslash correctly

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111089](https://bugs.mysql.com/bug.php?id=111089)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111094-8.0.33 · Bug #111094

Results ordered incorrectly

官方版本字段：8.0.33, 8.0.36

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111094](https://bugs.mysql.com/bug.php?id=111094)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："wä首键查询错误按id2 E/id1 Wä，ka控制按id1/id2；逐布尔值仍与原文一致。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111094/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111094/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111094-8.0.33.sql)

### mysql-111097-8.0.33 · Bug #111097

Query statement results with subqueries are unstable

官方版本字段：8031, 5.7.42, 8.0.33, 8.0.36

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #111097](https://bugs.mysql.com/bug.php?id=111097)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原文要求多次断开重连观察不稳定现象；当前reproducer只有查询，建表数据在分阶段材料，不适合单文件单连接批次。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111106-8.0.33 · Bug #111106

MySQL 8.0.33 install fails on Ubuntu 20.04 with FIPS enabled

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111106](https://bugs.mysql.com/bug.php?id=111106)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111119-8.0.33 · Bug #111119

order by multiple column desc returns wrong results

官方版本字段：8.0.24,8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111119](https://bugs.mysql.com/bug.php?id=111119)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c532798作者承认误用ORDER BY，c532802说明c1唯一时c2排序不改变行序；不是错误结果。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111143-8.0.33 · Bug #111143

Quoting of ints

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111143](https://bugs.mysql.com/bug.php?id=111143)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Quoted numeric DEFAULT in SHOW CREATE TABLE is not governed by sql_quote_show_create identifier quoting; no demonstrated incorrect effective default or accepted formatting contract.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111157-8.0.33 · Bug #111157

Column info missing for view after doing a "table swap" where view uses function

官方版本字段：8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #111157](https://bugs.mysql.com/bug.php?id=111157)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需要 mysql_no_login.so、两个用户/多连接、全局授权；已有脚本只包含后续阶段，缺完整前置与专用权限环境。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111158-8.0.33 · Bug #111158

Query failure

官方版本字段：8.0.25, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111158](https://bugs.mysql.com/bug.php?id=111158)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111178-8.0.33 · Bug #111178

Unable to set the secondary engine

官方版本字段：8.0.25, 8.0.33, 8.3.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111178](https://bugs.mysql.com/bug.php?id=111178)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Uses debug skip_dd_table_access_check to ALTER protected dictionary tables and a test secondary engine. Requires debug dictionary access and original engine; unsupported internal operations need explicit oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111182-8.0.33 · Bug #111182

buffer pool online resize warning message incorrect

官方版本字段：8.0.33, 8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111182](https://bugs.mysql.com/bug.php?id=111182)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111190-8.0.33 · Bug #111190

Build fails with LANG=ja_JP.UTF-8

官方版本字段：8.0.31, 8.0.32, 8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111190](https://bugs.mysql.com/bug.php?id=111190)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Failure occurs compiling under ja_JP.UTF-8 locale due to readelf parsing; requires frozen source/build toolchain and locale, not database SQL replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111212-8.0.33 · Bug #111212

compile failed with gcc-10 when lto is enable

官方版本字段：8.0.30, 8.0.33

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #111212](https://bugs.mysql.com/bug.php?id=111212)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需Debian GCC10.2.1、LTO/PGO及原构建选项，目标protoc std::system_error是构建期故障；SQL运行不能验证。末条无关广告不作为证据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111218-8.0.33 · Bug #111218

Logic bug: logic equal sqls return different results

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111218](https://bugs.mysql.com/bug.php?id=111218)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Inner join with false predicates and scalar subquery projected for every outer row are not equivalent; NULL-filled projection is expected.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111219-8.0.33 · Bug #111219

Logic bug: logic equal sqls return different results

官方版本字段：8.0.33-0ubuntu0.20.04.2

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111219](https://bugs.mysql.com/bug.php?id=111219)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 内连接过滤与SELECT列表标量子查询不等价；后者保留外表行且返回NULL，不能把空集与9行NULL差异判错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111220-8.0.33 · Bug #111220

Logic bug: logic equal sqls return different results

官方版本字段：8.0.33-0ubuntu0.20.04.2

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111220](https://bugs.mysql.com/bug.php?id=111220)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Same inequivalent inner join/scalar subquery error as #111218; c533026 marks duplicate. No valid equality oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111221-8.0.33 · Bug #111221

Logic bug: logic equal sqls return different results

官方版本字段：8.0.33-0ubuntu0.20.04.2

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111221](https://bugs.mysql.com/bug.php?id=111221)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 内连接过滤与投影中标量子查询不等价，外层未过滤会保留10行；原等价主张不成立。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111242-8.0.33 · Bug #111242

Replica Issue - ('mysql.infoschema'@'localhost') does not exist

官方版本字段：5.7.41 and 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111242](https://bugs.mysql.com/bug.php?id=111242)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111255-8.0.33 · Bug #111255

unnecessary locks cannot be released when use index_merge

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111255](https://bugs.mysql.com/bug.php?id=111255)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Index-merge locking report has malformed collation name and punctuation and discusses optimization behavior. Need source correction, exact lock interleaving and accepted excessive-lock oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111261-8.0.33 · Bug #111261

Skip scan results in wrong query results

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111261](https://bugs.mysql.com/bug.php?id=111261)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确必须debug并设置GLOBAL innodb_purge_stop_now，需delete-marked跨页未purge及skip scan计划。当前release、普通低资源协议未满足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111262-8.0.33 · Bug #111262

Query return wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111262](https://bugs.mysql.com/bug.php?id=111262)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- not(a1<4) is null的优先级不能按作者括号意图推定；NOT可能作用于IS NULL整体，10为正常。需冻结解析/布尔契约，原注释0不是可靠oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111263-8.0.33 · Bug #111263

Query return wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111263](https://bugs.mysql.com/bug.php?id=111263)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Aggregate MIN over outer reference can change outer query aggregation scope; claimed ten-row expectation lacks justified scope semantics. Duplicate link to #111265 does not establish oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111264-8.0.33 · Bug #111264

Query return wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111264](https://bugs.mysql.com/bug.php?id=111264)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- WHERE NOT a2筛选与SELECT NOT a2投影不等价，10行0对空集是正常，不能计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111265-8.0.33 · Bug #111265

Return wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111265](https://bugs.mysql.com/bug.php?id=111265)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Claim that empty outer-joined table makes predicate irrelevant is unproven for CHAR(NULL)>-1; official disputes float semantics. Must establish null-extension and CHAR conversion contract before Bug verdict.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111266-8.0.33 · Bug #111266

Can't delete a row

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111266](https://bugs.mysql.com/bug.php?id=111266)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c533133-135指出应IS NULL，=NULL永不为true，作者c533176承认非Bug；另CREATE/INSERT表名不一致。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111268-8.0.33 · Bug #111268

Different character_set_connection returns inconsistent results

官方版本字段：8.0.25, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111268](https://bugs.mysql.com/bug.php?id=111268)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："utf8mb3返回两行而utf8mb4错误为空"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111268/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111268/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111268-8.0.33.sql)

### mysql-111272-8.0.33 · Bug #111272

Inconsistent behaviors on string comparison with/without index

官方版本字段：8.0.32, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111272](https://bugs.mysql.com/bug.php?id=111272)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：Indexed prefix query returns only ^1o while no-index equivalent returns both rows. Preserve combining-mark bytes CD95 and collation; postchecks verify exact two strings.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111272/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111272/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111272-8.0.33.sql)

### mysql-111286-8.0.33 · Bug #111286

SDI has incorrect types for DB_TRX_ID and DB_ROLL_PTR fields

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111286](https://bugs.mysql.com/bug.php?id=111286)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires reading actual .ibd with matching ibd2sdi and deciding internal DB_TRX_ID/DB_ROLL_PTR type representation contract; SQL-only output cannot validate requested internal metadata property.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111290-8.0.33 · Bug #111290

No matching rows when joining multiple tables on binary/varbinary key

官方版本字段：8.0.23, 8.0.33, 5.7

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111290](https://bugs.mysql.com/bug.php?id=111290)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："三个相等16字节连接键且所有表一行时，最终JOIN错误空集。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111290/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111290/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111290-8.0.33.sql)

### mysql-111293-8.0.33 · Bug #111293

Create table partition by hash subquery assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111293](https://bugs.mysql.com/bug.php?id=111293)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 分区子查询断言，原文debug+ASan+UBSan；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111299-8.0.33 · Bug #111299

Return incorrect result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111299](https://bugs.mysql.com/bug.php?id=111299)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- WHERE谓词过滤与投影NOT表达式不等价，原10个非零a2投影0且过滤空集合法；不采用评论中float绝不为0的错误泛化。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111303-8.0.33 · Bug #111303

MySQL Server crashes when executing query

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111303](https://bugs.mysql.com/bug.php?id=111303)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111304-8.0.33 · Bug #111304

The Query Rewrite Plugin mixes-up LIMIT and OFFSET.

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111304](https://bugs.mysql.com/bug.php?id=111304)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需要 Query Rewrite 插件及其全局 rewrite_rules/flush 操作；当前无专门插件配置与恢复流程。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111306-8.0.33 · Bug #111306

AccessPath* MoveCompositeIteratorsFromTablePath(AccessPath*, const Query_block&

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111306](https://bugs.mysql.com/bug.php?id=111306)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Assertion reproducer explicitly uses WITH_DEBUG and specified startup configuration; release success cannot disprove debug assertion. Require matching debug build and startup verification.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111310-8.0.33 · Bug #111310

Prepared statement with CTE memory leak

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111310](https://bugs.mysql.com/bug.php?id=111310)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain要求debug+ASAN/UBSAN/LeakSanitizer并正常关闭捕获56字节String::copy/Item_param泄漏；普通SQL输出/存活不能完成该oracle。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\111310\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111324-8.0.33 · Bug #111324

Return wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111324](https://bugs.mysql.com/bug.php?id=111324)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- String/numeric comparison can use approximate conversion; large literal equality result alone is not valid wrong-result oracle. Developer marks not a bug; need explicit conversion contract.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111325-8.0.33 · Bug #111325

Inconsistent results in BETWEEN clause with NULL value

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111325](https://bugs.mysql.com/bug.php?id=111325)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c533424给出短路逻辑解释：早于NOW的日期使BETWEEN为false，无需NULL判定；不应把IS NULL的0/1差异计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111331-8.0.33 · Bug #111331

Default collation utf8mb4_0900_ai_ci causes inconsistent results to Korean

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111331](https://bugs.mysql.com/bug.php?id=111331)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Korean collation equality is explained as Unicode collation behavior by maintainer. Cross-collation disagreement is not itself a bug oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111353-8.0.33 · Bug #111353

3x Performance Regression from 5.7 to 8.0 on ALTER TABLE FORCE.

官方版本字段：8.0, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111353](https://bugs.mysql.com/bug.php?id=111353)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111357-8.0.33 · Bug #111357

JSON explain assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111357](https://bugs.mysql.com/bug.php?id=111357)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- EXPLAIN JSON assert(0)，原文debug+ASan+UBSan；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111373-8.0.33 · Bug #111373

Assertion `!sl->order_list.first' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111373](https://bugs.mysql.com/bug.php?id=111373)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 验证者明确 release 通过，debug 断言；还需 mysqlx/performance_schema 启动设置。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111374-8.0.33 · Bug #111374

Assertion `m_return_field_def.auto_flags == Field::NONE' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111374](https://bugs.mysql.com/bug.php?id=111374)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain编译WITH_DEBUG且c533481明确debug-only；现release不能检验returns_type断言，受控SQL错误不算报告复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111375-8.0.33 · Bug #111375

Assertion `ha_alter_info->handler_flags & (Alter_inplace_info::ADD_VIRTUAL_COLUM

官方版本字段：8.0.33

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #111375](https://bugs.mysql.com/bug.php?id=111375)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111376-8.0.33 · Bug #111376

Assertion `!thd->lex->is_exec_started() || thd->lex->is_query_tables_locked()' f

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111376](https://bugs.mysql.com/bug.php?id=111376)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 验证者明确 release 通过，debug CTAS/partition 断言；缺对应构建与启动设置。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111377-8.0.33 · Bug #111377

int mysql_execute_command(THD*, bool): Assertion `!thd->in_sub_stmt' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111377](https://bugs.mysql.com/bug.php?id=111377)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain/c533487为debug-only，同时触发器内CREATE FUNCTION ... SONAME尝试加载UDF，涉及插件/文件操作必须单列审查；无库/权限环境，不执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111379-8.0.33 · Bug #111379

Assertion `context->query_block == thd->lex->current_query_block()' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111379](https://bugs.mysql.com/bug.php?id=111379)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- WITH_DEBUG=1，官方评论仅debug受影响；sql_mode NO_ENGINE_SUBSTITUTION；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111383-8.0.33 · Bug #111383

Scale assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111383](https://bugs.mysql.com/bug.php?id=111383)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug AVG(NULLIF(empty YEAR)) decimal precision 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111395-8.0.33 · Bug #111395

Missing documentation of new privilege TELEMETRY_LOG_ADMIN in 8.0.33

官方版本字段：8.0.33-community

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111395](https://bugs.mysql.com/bug.php?id=111395)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111403-8.0.33 · Bug #111403

Assertion `!col_val->item_expression->null_value' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111403](https://bugs.mysql.com/bug.php?id=111403)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确WITH_DEBUG，c533542为debug-only dd_table分区NULL断言；当前release不适用。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111404-8.0.33 · Bug #111404

Assertion `is_prepared()' failed.

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111404](https://bugs.mysql.com/bug.php?id=111404)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- CALL后is_prepared断言，官方评论仅debug受影响；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111406-8.0.33 · Bug #111406

MySQL Server encounters Assertion Failure when executing query

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111406](https://bugs.mysql.com/bug.php?id=111406)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 仅 debug 的 UPDATE safe_update_on_fly 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111414-8.0.33 · Bug #111414

HASH JOIN results in wrong query results

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111414](https://bugs.mysql.com/bug.php?id=111414)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111421-8.0.33 · Bug #111421

Unexpected error when `CHECK` a predicate that is always true

官方版本字段：last commit version in github, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111421](https://bugs.mysql.com/bug.php?id=111421)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：两侧 CREATE TABLE t0(c1 NUMERIC CHECK(true)) 在第6行都报3813/HY000：Column check constraint references other column；第7行 SHOW 的1146仅记录为建表失败的依赖后果。库中 t0_exists=0，干净 schema、源 SQL 和环境一致，8.0.32 已存在恒真 CHECK 的错误拒绝。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111421/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111421/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111421-8.0.33.sql)

### mysql-111429-8.0.33 · Bug #111429

Incorrect result when timestamp col apply <=> to the result of subquery

官方版本字段：8.0.22, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111429](https://bugs.mysql.com/bug.php?id=111429)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象：[[["NULL", "1997-03-04 12:20:00.000000"]], [["NULL", "1997-03-04 12:20:00.000000"], ["NULL", "1998-03-04 12:20:00.000000"], ["NULL", "1999-03-04 12:20:00.000000"]], [["NULL", "1997-03-04 12:20:00.000000"]]]

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111429/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111429/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111429-8.0.33.sql)

### mysql-111430-8.0.33 · Bug #111430

Case rpl.rpl_plugin_load cause crash when build with -DWITH_LTO=1

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #111430](https://bugs.mysql.com/bug.php?id=111430)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需WITH_LTO=1、Debug及-O0编译并运行rpl.rpl_plugin_load；普通release既无原优化构建又无MTR复制测试，需独立编译/套件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111431-8.0.33 · Bug #111431

condition_fanout_filter optimizer wrong result?

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111431](https://bugs.mysql.com/bug.php?id=111431)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- LAG OVER() has no window ORDER BY. Outer ORDER BY does not define LAG input order; optimizer-dependent 1/4 output is not established wrong result.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111432-8.0.33 · Bug #111432

c++ Undefined Behavior with clang-16

官方版本字段：mysql-8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111432](https://bugs.mysql.com/bug.php?id=111432)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111441-8.0.33 · Bug #111441

bool Sql_cmd_dml::prepare(THD*): Assertion `thd->is_error()' failed.

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111441](https://bugs.mysql.com/bug.php?id=111441)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文8.0.33-debug及WITH_DEBUG；堆栈还含OUTFILE变体，不执行该变体；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111443-8.0.33 · Bug #111443

Assertion `has_error == thd->get_stmt_da()->is_error()' failed

官方版本字段：8.0.33

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #111443](https://bugs.mysql.com/bug.php?id=111443)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111444-8.0.33 · Bug #111444

Assertion `inited == NONE || table->open_by_handler' failed.

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111444](https://bugs.mysql.com/bug.php?id=111444)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确debug build；c533656/c533657说明debug断言而release未受影响。缺WITH_DEBUG，不执行替代版。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111445-8.0.33 · Bug #111445

virtual longlong Item_typecast_signed::val_int(): Assertion `is_nullable()' fail

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111445](https://bugs.mysql.com/bug.php?id=111445)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文debug及WITH_DEBUG，目标是Item_typecast_signed断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111448-8.0.33 · Bug #111448

MySQL Server encounters Assertion Failure when executing query

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111448](https://bugs.mysql.com/bug.php?id=111448)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Maintainer confirms debug-only assertion with replication reset/change state. Requires verified target debug build and explicit replication state; release replay cannot satisfy original condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111449-8.0.33 · Bug #111449

void Diagnostics_area::set_eof_status(THD*): Assertion `!is_set()' failed.

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111449](https://bugs.mysql.com/bug.php?id=111449)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- HANDLER 诊断 debug 断言；c535184 明确 does not affect a release；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111450-8.0.33 · Bug #111450

Assertion `to->field_ptr() != from->field_ptr()' failed.

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111450](https://bugs.mysql.com/bug.php?id=111450)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111453-8.0.33 · Bug #111453

sql query with "where time_col not between val1 and null' has diffrent results

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111453](https://bugs.mysql.com/bug.php?id=111453)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires exact 111454.sql/table data attachment and repeated same-session queries after table reload. Saved transcript alone does not contain DDL/data; do not synthesize 113 rows.
- Official exposed attachment is tbl_1_all_type2index.sql, while comments reference111454.sql; reconcile filename/content before execution.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111454-8.0.33 · Bug #111454

select query with json and time column has different results

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #111454](https://bugs.mysql.com/bug.php?id=111454)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 只有对tbl_1_all_type2index的一条查询，缺建表、JSON/time数据及各版本确切输出；c533727确认并不能补足缺失测试数据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111461-8.0.33 · Bug #111461

Server crash after running crafted SELECT statement

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111461](https://bugs.mysql.com/bug.php?id=111461)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs init.sql and case 127.sql referenced as attachments; stack trace and video do not supply SQL initialization or trigger.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111462-8.0.33 · Bug #111462

Server crash after running crafted SELECT statement

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111462](https://bugs.mysql.com/bug.php?id=111462)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111469-8.0.33 · Bug #111469

Build failure with Protobuf 22+

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111469](https://bugs.mysql.com/bug.php?id=111469)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Build-time Protobuf22+ and Abseil linkage issue requires original macOS/Homebrew build toolchain with WITH_PROTOBUF=system, not runtime SQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111471-8.0.33 · Bug #111471

Unexpected Error: Memory capacity exceeded

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111471](https://bugs.mysql.com/bug.php?id=111471)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 设置range_alloc_block_size接近UINT64_MAX后ERROR34是否合理没有确定契约；不能把明确容量错误当逻辑Bug，需核验变量裁剪和预期分配行为。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111474-8.0.33 · Bug #111474

hypergraph_optimizer SEGV

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111474](https://bugs.mysql.com/bug.php?id=111474)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- WITH_DEBUG/ASAN/UBSAN和hypergraph明确必需；原配置4G buffer、放宽secure_file_priv/本地导入及全局启动设置需专门审查，当前2GiB发布实例不满足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111477-8.0.33 · Bug #111477

If Table contains Floating Point with limited digits, UPDATE may silently fail

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #111477](https://bugs.mysql.com/bug.php?id=111477)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需独立FEDERATED双实例和连接定义；正文远端建表/数据完整但本地连接DDL省略、评论标unsupported。需确认目标版本引擎支持和更新语义后测试。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111483-8.0.33 · Bug #111483

Different truncated result between select and delete

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111483](https://bugs.mysql.com/bug.php?id=111483)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SELECT warning versus DELETE error under strict conversion is documented normal distinction; initial schema name t versus t0 also inconsistent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111484-8.0.33 · Bug #111484

wrong result when rewriting scalar subquery in json function parameters

官方版本字段：mysql-8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111484](https://bugs.mysql.com/bug.php?id=111484)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："on侧6行、每个id两次且JSON_SEARCH均NULL"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111484/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111484/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111484-8.0.33.sql)

### mysql-111485-8.0.33 · Bug #111485

When subquery_to_derived is on, IN-subq to derived table transformed wrongly

官方版本字段：mysql-8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111485](https://bugs.mysql.com/bug.php?id=111485)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111492-8.0.33 · Bug #111492

Subquery ref count assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111492](https://bugs.mysql.com/bug.php?id=111492)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug 子查询 m_ref_count 断言；缺 debug（评论关联 110369）。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111497-8.0.33 · Bug #111497

Assertion `m_deque == other.m_deque' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111497](https://bugs.mysql.com/bug.php?id=111497)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确Only debug mode is affected，WITH_DEBUG编译及m_deque断言；现release环境不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111503-8.0.33 · Bug #111503

Supported platforms and distributions

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111503](https://bugs.mysql.com/bug.php?id=111503)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Question about distribution support versus community binaries; no database defect or SQL reproducer is supplied.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111506-8.0.33 · Bug #111506

Spatial index cardinality equals to the number of rows of the table.

官方版本字段：5.7.42, 8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111506](https://bugs.mysql.com/bug.php?id=111506)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111508-8.0.33 · Bug #111508

The query results are inconsistent when different optimizer options are used.

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_attachment_needed

官方报告：[Bug #111508](https://bugs.mysql.com/bug.php?id=111508)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 正文同查询block_nested_loop对照和输出明确，缺test.sql建表/数据；官方附件32373已定位，待获取核验。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111509-8.0.33 · Bug #111509

The local server has been stopped and i can't do any work of my project.

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111509](https://bugs.mysql.com/bug.php?id=111509)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Workbench/server-stopped request supplies neither log attachment nor repeatable steps/schema; referenced duplicates do not replace missing local state.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111510-8.0.33 · Bug #111510

nth_value window function call assertion error

官方版本字段：8.0.33

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #111510](https://bugs.mysql.com/bug.php?id=111510)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111511-8.0.33 · Bug #111511

CTE missing scope in set queries

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111511](https://bugs.mysql.com/bug.php?id=111511)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c542313指出嵌套parenthesized SELECT中的WITH语法非标准且应拒绝；原1146/CTE作用域oracle需要MySQL扩展语法核验，不把任何错误直接算复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111527-8.0.33 · Bug #111527

Assertion `inited == RND' failed

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111527](https://bugs.mysql.com/bug.php?id=111527)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 明确只影响 debug 的 handler inited==RND 断言，release 通过；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111528-8.0.33 · Bug #111528

Count queries cardinality mismatch

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111528](https://bugs.mysql.com/bug.php?id=111528)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires attachment dataset not present in per-item materials; duplicate/group semantics disputed in c533854. Need original attachment and verified cardinality oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111538-8.0.33 · Bug #111538

MySQL 8.0.33 is slower than MySQL 8.0.28 with queries using JOINS

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111538](https://bugs.mysql.com/bug.php?id=111538)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111559-8.0.33 · Bug #111559

View with CTE syntax error

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111559](https://bugs.mysql.com/bug.php?id=111559)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：CREATE VIEW succeeds, but SELECT and SHOW CREATE each emit 1064 near serialized select; same abnormality exists in prior release. Do not treat arbitrary 1064 or setup failure as this bug.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111559/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111559/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111559-8.0.33.sql)

### mysql-111562-8.0.33 · Bug #111562

nth_value window function assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111562](https://bugs.mysql.com/bug.php?id=111562)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain/c533928和c538030将问题限定debug空窗口帧断言，需要WITH_DEBUG/ASAN/UBSAN；不在release中据正常NULL否定该报告。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111567-8.0.33 · Bug #111567

no longer can write to drive

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111567](https://bugs.mysql.com/bug.php?id=111567)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111570-8.0.33 · Bug #111570

Looking for inexistent data reports 0 rows examined

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111570](https://bugs.mysql.com/bug.php?id=111570)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires slow_query_log=ON, log_output=TABLE, long_query_time=0, 1GiB buffer pool and status/Performance Schema metrics protocol. Existing generic SQL replay lacks configured log environment; rows_examined=0 must be interpreted as this instrumentation issue, not wrong rows.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111582-8.0.33 · Bug #111582

Query is incorrect after importing partition table with a different definition

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #111582](https://bugs.mysql.com/bug.php?id=111582)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- MTR需要文件级备份、DISCARD/IMPORT TABLESPACE、分区定义不一致与同datadir文件拷贝；普通SQL不足，需专属文件操作驱动及目录审查。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111585-8.0.33 · Bug #111585

Order by aggregate assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111585](https://bugs.mysql.com/bug.php?id=111585)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official verifier explicitly confirms 8.0.33 debug assertion. Original WITH_DEBUG+ASAN+UBSAN conditions and boost1.77 must be verified; release execution cannot stand in for assertion build.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111595-8.0.33 · Bug #111595

Decimal query wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111595](https://bugs.mysql.com/bug.php?id=111595)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111596-8.0.33 · Bug #111596

krb5-devel is buildreq for all rpm builds on el*

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111596](https://bugs.mysql.com/bug.php?id=111596)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Enterprise Linux RPM krb5-devel build-requirement issue needs package build environment; SQL playback does not test missing BuildRequires.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111598-8.0.33 · Bug #111598

SELECT FOR SHARE does not acquire lock correctly

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111598](https://bugs.mysql.com/bug.php?id=111598)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111624-8.0.33 · Bug #111624

It's storing -0 (Minus Zero) value

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111624](https://bugs.mysql.com/bug.php?id=111624)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- IEEE floating point signed zero is expected; c534093 explicitly explains. GO-delimited transcript also not native mysql script.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111629-8.0.33 · Bug #111629

Possible corrupt table?

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111629](https://bugs.mysql.com/bug.php?id=111629)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111636-8.0.33 · Bug #111636

Query not using the index even with FORCE INDEX

官方版本字段：8.0.33,5.7.41

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111636](https://bugs.mysql.com/bug.php?id=111636)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Maintainer disputes forced-index behavior under range memory limit as expected; their explanation references changed indexed columns inconsistently with supplied col11/col9. Requires resolving oracle, not treating warning/fullscan as bug by itself.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111638-8.0.33 · Bug #111638

Sorting and pagination do not meet expectations

官方版本字段：8.0.33, 8.0.22+

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111638](https://bugs.mysql.com/bug.php?id=111638)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111647-8.0.33 · Bug #111647

Blob partial update in undo record may lead potential crash

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111647](https://bugs.mysql.com/bug.php?id=111647)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- JSON_REMOVE case only shows potential zero-length undo diff; reporter states8.0.33 does not crash. Missing triggering MVCC read/interleaving and allocator-dependent observation; successful UPDATE does not reproduce hypothesized crash.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111662-8.0.33 · Bug #111662

continuous replication delays occur.

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111662](https://bugs.mysql.com/bug.php?id=111662)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c534306解释1秒复制延迟是测量/取整差异而非Bug；缺可重复负载和超出正常延迟的oracle，拓扑也未冻结。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111669-8.0.33 · Bug #111669

Simple Query Times Out

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111669](https://bugs.mysql.com/bug.php?id=111669)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Verified performance issue requires uploaded test_db_bug_111669.zip with minimized real data and configuration; schemas alone omit foreign referenced tables and matching text data. Need bounded time/resource protocol beyond60s.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111685-8.0.33 · Bug #111685

ADD PARTITION with DATA DIRECTORY forces relocation of other partitions

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111685](https://bugs.mysql.com/bug.php?id=111685)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111689-8.0.33 · Bug #111689

optimize for page flush

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111689](https://bugs.mysql.com/bug.php?id=111689)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-only page flush refactoring proposal says read code; no runtime workload or measurable regression oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111693-8.0.33 · Bug #111693

Insert assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111693](https://bugs.mysql.com/bug.php?id=111693)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- VALUES/UNION INSERT断言需debug+ASan+UBSan；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111699-8.0.33 · Bug #111699

Incorrect results

官方版本字段：8.0.28, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111699](https://bugs.mysql.com/bug.php?id=111699)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："P OR Q 返回 9 个 NULL；P 返回 3 个 NULL；Q 为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111699/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111699/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111699-8.0.33.sql)

### mysql-111700-8.0.33 · Bug #111700

LIMIT values are not adequately handled in EXPLAIN.

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111700](https://bugs.mysql.com/bug.php?id=111700)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires original million-row dataset and calibrated performance/cost oracle; EXPLAIN estimated costs need not rank different execution times. Data generator and controlled timing conditions absent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111701-8.0.33 · Bug #111701

Binlog replication optimize

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111701](https://bugs.mysql.com/bug.php?id=111701)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111702-8.0.33 · Bug #111702

Alter default value with auto_increment column not report error

官方版本字段：8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #111702](https://bugs.mysql.com/bug.php?id=111702)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SQL和c534294三行数据完整，但c534347/c534365明确正确规范行为仍需核对；ALTER DEFAULT与MODIFY不一致/1062现象可观察，不能预设哪一方必须拒绝。oracle语义待确认，当前不执行。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111703-8.0.33 · Bug #111703

INSERT ON DUPLICATE KEY locks INSERT if table have many PRIMARY and UNIQUE key

官方版本字段：8.0.33, 5.7.42

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111703](https://bugs.mysql.com/bug.php?id=111703)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111706-8.0.33 · Bug #111706

Incorrect result

官方版本字段：8.0.28, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111706](https://bugs.mysql.com/bug.php?id=111706)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："off3行而on9行，每组复制三次；数值转换警告不是执行失败"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111706/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111706/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111706-8.0.33.sql)

### mysql-111709-8.0.33 · Bug #111709

Error missing tablespace if innodb-validate-tablespace-paths=OFF

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111709](https://bugs.mysql.com/bug.php?id=111709)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需要 SHUTDOWN/重启、通用表空间文件 ts1.ibd、innodb-validate-tablespace-paths=OFF；必须专用实例登记文件归属和重启条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111710-8.0.33 · Bug #111710

Mysql 8 Role Issue

官方版本字段：8.0.32, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111710](https://bugs.mysql.com/bug.php?id=111710)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111714-8.0.33 · Bug #111714

Table constraint name ignored

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111714](https://bugs.mysql.com/bug.php?id=111714)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Named PRIMARY KEY silently uses PRIMARY and DROP CONSTRAINT k0 raises3940; report requests warning. No accepted contract requiring warning or retaining supplied PK name, so expected error alone cannot establish Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111717-8.0.33 · Bug #111717

MySQL InnoDB Cluster Requires Manual RebootClusterFromCompleteOutage

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #111717](https://bugs.mysql.com/bug.php?id=111717)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c534345明确两节点全停为full outage，rebootClusterFromCompleteOutage属于正常恢复流程；原问题是自动化需求而非冻结Bug oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111720-8.0.33 · Bug #111720

recv_n_pool_free_frames are not maintained correctly

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111720](https://bugs.mysql.com/bug.php?id=111720)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source comment versus recv_n_pool_free_frames value mismatch is static documentation issue; no SQL runtime behavior/oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111722-8.0.33 · Bug #111722

Create view assertion error

官方版本字段：8.0.33

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111722](https://bugs.mysql.com/bug.php?id=111722)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain编译debug+ASAN/UBSAN，c534354 release无断言；缺对应构建，参数化CREATE VIEW受控错误不等同复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111727-8.0.33 · Bug #111727

MGR failure detection fail due to the wrong legacy of m_expels_in_progress

官方版本字段：8.0.28, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111727](https://bugs.mysql.com/bug.php?id=111727)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111728-8.0.33 · Bug #111728

Incorrect result

官方版本字段：8.0.28, 8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111728](https://bugs.mysql.com/bug.php?id=111728)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："默认空集，no_index返回1801425248110076222一行"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111728/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111728/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111728-8.0.33.sql)

### mysql-111737-8.0.33 · Bug #111737

Double tick in string literals does not work for CREATE TABLE with NO_BACKSLASH_

官方版本字段：8.0.33-0ubuntu0.22.04.2

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111737](https://bugs.mysql.com/bug.php?id=111737)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：两侧第一次 CREATE/DROP 均成功，仅加入 NO_BACKSLASH_ESCAPES 后第二次 CREATE（第10行）报1064/42000；独立 REGEXP 控制均为0、1，最终 sql_mode 和 tab_exists=0 校验一致。1033 为随后的文件诊断，未替代主错误判定。8.0.32 已存在同样现象。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/111737/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/111737/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111737-8.0.33.sql)

### mysql-111739-8.0.33 · Bug #111739

The query results are inconsistent.

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111739](https://bugs.mysql.com/bug.php?id=111739)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires two attached SQL datasets and controlled restart; nonaggregated datetime selected with GROUP BY set_col under empty SQL mode has unspecified group representative. Need both data and deterministic oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111755-8.0.33 · Bug #111755

potential risk of innodb recovey

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111755](https://bugs.mysql.com/bug.php?id=111755)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111770-8.0.33 · Bug #111770

group replication lost transaction when import tablespace failed

官方版本字段：8.0.30, 8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111770](https://bugs.mysql.com/bug.php?id=111770)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Explicit custom DBUG source injection plus3-node group replication, physical tablespace copies, kill/restart and GTID/binlog comparison; cannot use unmodified single release server.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111811-8.0.33 · Bug #111811

UPDATE statement with JOIN doesn't update any records

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111811](https://bugs.mysql.com/bug.php?id=111811)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Required full database dump is private /support/incoming/mysql-bug-data-111811.zip; no complete public schema/data, and verifier cannot reproduce even resetting valid=0.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111812-8.0.33 · Bug #111812

Unable to open '#innodb_redo/#ib_redo31_tmp', no permission

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111812](https://bugs.mysql.com/bug.php?id=111812)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111855-8.0.33 · Bug #111855

getTableName() gives empty or null results

官方版本字段：8.0.33, 8.1.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111855](https://bugs.mysql.com/bug.php?id=111855)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires Java Connector/J ResultSetMetaData and precise server/driver combination. Later official comment says observed on5.7 only; target8.0 mapping does not establish affected server. SQL result rows alone cannot test getTableName.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111858-8.0.33 · Bug #111858

mysql.db's MDL acquired by XA recover then blocked initializion of ACL

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111858](https://bugs.mysql.com/bug.php?id=111858)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111866-8.0.33 · Bug #111866

executing a rename table statement could cause a transaction to be committed

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111866](https://bugs.mysql.com/bug.php?id=111866)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- RENAME TABLE implicitly commits preceding transaction even when DDL fails; official comments identify normal nontransactional-DDL behavior, so failed rename is not rollback oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111872-8.0.33 · Bug #111872

VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111872](https://bugs.mysql.com/bug.php?id=111872)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111873-8.0.33 · Bug #111873

there's no warnings or errors after failed to set validate_password_length to 0

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111873](https://bugs.mysql.com/bug.php?id=111873)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires deprecated validate_password plugin rather than newer component, global policy manipulation and error-log inspection. Component logging shown by verifier cannot stand in for original plugin behavior.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111914-8.0.33 · Bug #111914

Global replication filters replace channel specific filters

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111914](https://bugs.mysql.com/bug.php?id=111914)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer confirms changing global filters replaces same-type channel filters by documented design; displayed replacement is expected, not a replication bug oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111936-8.0.33 · Bug #111936

Use validate_password component failed to create user

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111936](https://bugs.mysql.com/bug.php?id=111936)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112032-8.0.33 · Bug #112032

Using C program to execute query and report errors

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112032](https://bugs.mysql.com/bug.php?id=112032)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112106-8.0.33 · Bug #112106

InnoDB locks supremum when last record of page is updated

官方版本字段：8.0.33

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112106](https://bugs.mysql.com/bug.php?id=112106)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112108-8.0.33 · Bug #112108

VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112108](https://bugs.mysql.com/bug.php?id=112108)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112128-8.0.33 · Bug #112128

The parameters such as MySQL password_history does not take effect

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112128](https://bugs.mysql.com/bug.php?id=112128)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- NULL user policy columns mean inherit global defaults, as developer explains; NULL storage is expected and does not prove policy unenforced.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112132-8.0.33 · Bug #112132

The configuration of password_history does not take effect

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112132](https://bugs.mysql.com/bug.php?id=112132)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112137-8.0.33 · Bug #112137

parallel read is slow when innodb_use_native_aio = off

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112137](https://bugs.mysql.com/bug.php?id=112137)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires sysbench60million rows, ~2GiB buffer pool, O_DIRECT, native-AIO startup toggle and cold restart; must approve resource envelope and preserve I/O environment rather than substitute tiny dataset.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112159-8.0.33 · Bug #112159

VIEW reference in a SELECT subquery returns different results from using TABLE

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112159](https://bugs.mysql.com/bug.php?id=112159)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112231-8.0.33 · Bug #112231

Inconsistent result for OVER() when used in stored procedure over InnoDB table

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112231](https://bugs.mysql.com/bug.php?id=112231)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：SUM(1) OVER()+0 must remain 1 on both calls over same single id=1. Target second 2; previous version normal in three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/112231/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/112231/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112231-8.0.33.sql)

### mysql-112252-8.0.33 · Bug #112252

InnoDB page compression impacts checkpointing

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112252](https://bugs.mysql.com/bug.php?id=112252)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112255-8.0.33 · Bug #112255

empty vio->signal_mask in the x plugin causes MySQL cannot handle signal

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112255](https://bugs.mysql.com/bug.php?id=112255)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires active mysqlsh X Protocol connection, exact Ubuntu ppoll build and controlled SIGTERM with shutdown log/exit-status oracle; generic SQL cannot exercise signal-delivery condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112259-8.0.33 · Bug #112259

Assert when debug_sync_timeout is 0

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112259](https://bugs.mysql.com/bug.php?id=112259)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Explicitly requires Debug Sync build with debug_sync_timeout=0 and DBUG enabled_commit; release binaries cannot execute the original assertion condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112319-8.0.33 · Bug #112319

GROUP_CONCAT with GROUP BY and WHERE clause turns NULL into empty strings.

官方版本字段：8.0.33, 8.0.34, 8.1.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112319](https://bugs.mysql.com/bug.php?id=112319)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112372-8.0.33 · Bug #112372

Select query returns duplicate rows

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112372](https://bugs.mysql.com/bug.php?id=112372)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires three uploaded dataset files and their roles, including referenced item table. PK uniqueness gives meaningful duplicate oracle, but absent inputs prevent validating claimed repeated/missing entityId; unresolved official comments do not justify inventing rows.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112395-8.0.33 · Bug #112395

The results on the open source 8.0.33 are not as expected.

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112395](https://bugs.mysql.com/bug.php?id=112395)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- FLOAT loses integer/date precision under IEEE representation; developer explicitly identifies expected imprecision. Private table not needed to know requested exact-roundtrip oracle is invalid.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112460-8.0.33 · Bug #112460

Inconsistent results of SELECT statement with window functions

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112460](https://bugs.mysql.com/bug.php?id=112460)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版正常、目标异常。

保存的比较依据：Identical CASE branches must yield c20=17.61 just like direct projection. Target CASE NULL, direct17.61. Previous version normal three repeats.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/112460/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/112460/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112460-8.0.33.sql)

### mysql-112542-8.0.33 · Bug #112542

MySQL GR does not see tables with GIPK if show_gipk is OFF

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112542](https://bugs.mysql.com/bug.php?id=112542)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112589-8.0.33 · Bug #112589

ER_ROW_IS_REFERENCED vs ER_ROW_IS_REFERENCED_2 breaks backwards compatibility

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112589](https://bugs.mysql.com/bug.php?id=112589)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-based privilege/error-code compatibility issue lacks complete users/grants and FK schema/operation matrix. Requires multiaccount ACL test;1217/1451 are expected errors whose code distinction must be deliberately validated.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112779-8.0.33 · Bug #112779

Not auto rejoin after failing to parse relay log

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112779](https://bugs.mysql.com/bug.php?id=112779)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Random packet-drop instruction is not deterministic reproduction. Requires GR topology, bounded network fault schedule and relay-log state; do not alter host network/security settings.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112849-8.0.33 · Bug #112849

When tls_version is empty, warnings in error log should be removed

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112849](https://bugs.mysql.com/bug.php?id=112849)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires startup tls_version empty and fresh error log; exact duplicate104587. Need isolated startup override and log oracle, not runtime SQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112876-8.0.33 · Bug #112876

ICP (Index condition pushdown) causing BIGINT UNSIGNED value out of range error

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112876](https://bugs.mysql.com/bug.php?id=112876)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113061-8.0.33 · Bug #113061

The result of avg(distinct xx）is different between from primary and secondary

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113061](https://bugs.mysql.com/bug.php?id=113061)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："primary avg3.5/sum14，默认avg3.7/sum37；核对EXPLAIN实际索引及十行数据"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/113061/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/113061/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113061-8.0.33.sql)

### mysql-113180-8.0.33 · Bug #113180

Unexpected Results when Using Math Function SIN

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113180](https://bugs.mysql.com/bug.php?id=113180)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象：[[["1", "0"]], [["1", "0"]]]

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/113180/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/113180/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113180-8.0.33.sql)

### mysql-113185-8.0.33 · Bug #113185

Unexpected Results when using NULLIF Function in Filter

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113185](https://bugs.mysql.com/bug.php?id=113185)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Saved Not a Bug status and later reporter clarification; postpone this debate despite clear NULLIF logic.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113226-8.0.33 · Bug #113226

ALTER TABLE with comma separated DROP FOREIGN KEY AND ADD FOREIGN KEY throws

官方版本字段：8.0.33-25

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113226](https://bugs.mysql.com/bug.php?id=113226)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113229-8.0.33 · Bug #113229

mysqld: Duplicate entry 'mysql/slave_worker_info' for key 'tablespaces.name'

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113229](https://bugs.mysql.com/bug.php?id=113229)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113288-8.0.33 · Bug #113288

Explain plan shows dynamic range, but bug causes no chance to use for LEFT JOIN

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113288](https://bugs.mysql.com/bug.php?id=113288)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires uploaded t1/t2 data and execution-time dynamic-range instrumentation. EXPLAIN alone is explicitly insufficient because same displayed plan behaves differently; need exact dump and bounded runtime oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113298-8.0.33 · Bug #113298

Unexpected Results when Using IN for Floating-Point

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113298](https://bugs.mysql.com/bug.php?id=113298)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："有索引时正反谓词均返回1，删索引控制恢复互补"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/113298/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/113298/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113298-8.0.33.sql)

### mysql-113318-8.0.33 · Bug #113318

unnest scalar subquery using groupby produces wrong result

官方版本字段：mysql-8.0.33, 8.0.35, 8.1.0, 8.2.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113318](https://bugs.mysql.com/bug.php?id=113318)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无最终SQL；原文ANALYZE包含未定义t2需后续明确，不补造对象，不重试生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113318\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113319-8.0.33 · Bug #113319

unnesting scalar subquery containing count and having cond produces wrong result

官方版本字段：mysql-8.0.33, 8.0.35, 8.1.0, 8.2.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113319](https://bugs.mysql.com/bug.php?id=113319)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："off正确，on错误为[1,1,0,0]"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/113319/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/113319/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113319-8.0.33.sql)

### mysql-113446-8.0.33 · Bug #113446

Query with DISTINCT and ORDER BY on BIT data type returns wrong result

官方版本字段：8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113446](https://bugs.mysql.com/bug.php?id=113446)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原材料仅显示十六进制/十进制差异，须取得协议字段类型/原始值并确认 DISTINCT 的类型契约才能定 bug
- {"point": "BIT 的数值相同但显示/协议类型不同，缺字段级判据。", "evidence": "cmain 的 0x00/0、0x01/1；c547939 的临时表/索引路径对照；c558079 仅称 9.7 不复现。", "needed": "目标版本协议 field type/flags/原始字节及 DISTINCT 保持类型的规范；不要将显示变化计为数值错误。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113513-8.0.33 · Bug #113513

Join reordering regression and inconsistent behavior for SQL involving LEFT JOIN

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113513](https://bugs.mysql.com/bug.php?id=113513)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SQL and data are complete, but oracle is plan/hint acceptance rather than wrong-result. JOIN_PREFIX resides in outer query block while aliases are inside derived block; need establish intended hint scope and warning interpretation before declaring unchanged plan a bug. No preceding-version comparison authorized.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113570-8.0.33 · Bug #113570

composite index with the indexed expression "is not null" not being used

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113570](https://bugs.mysql.com/bug.php?id=113570)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113812-8.0.33 · Bug #113812

alter table tablename engine=innodb cause data loss

官方版本字段：8.0.33, 8.0.36

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113812](https://bugs.mysql.com/bug.php?id=113812)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original case needs external mysql_random_data_load with unspecified seed/version and repeated purge/online DDL race. Later deterministic 1000-row variant explicitly adds sleep instrumentation to two source locations. Existing release SQL alone cannot establish required race occurrence; need instrumented isolated build or controlled schedule, and record identity/count rather than count drift alone.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113819-8.0.33 · Bug #113819

when use show engine innodb cannot show correct information

官方版本字段：8.0.34, 8.0.33

状态：证据不足；阶段：ready_saved_before_task_interruption

官方报告：[Bug #113819](https://bugs.mysql.com/bug.php?id=113819)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Materials were saved before the owning review task was interrupted; this item was not separately identified as the trigger. No continuation of the interrupted task.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114246-8.0.33 · Bug #114246

I can't find any syntax to allow me to specify an index and a limit for DELETE

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #114246](https://bugs.mysql.com/bug.php?id=114246)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Feature request for combining DELETE index hints with LIMIT; table definitions/data absent and requested syntax is not established as supported. A syntax error would be normal rejection, not Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114273-8.0.33 · Bug #114273

turn on the binlog compression and load large data to server will cause oom

官方版本字段：MySQL8.0.22 to 8.0.33

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #114273](https://bugs.mysql.com/bug.php?id=114273)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原条件300GB导入且binlog压缩，超过当前批次预算；未提供数据集/事务大小/完整配置，后续因无反馈挂起。需原工作负载与独立资源批准。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114310-8.0.33 · Bug #114310

Master_compression_algorithm output is wrong

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114310](https://bugs.mysql.com/bug.php?id=114310)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114438-8.0.33 · Bug #114438

high memory usage on a MySQL server during query

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114438](https://bugs.mysql.com/bug.php?id=114438)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114714-8.0.33 · Bug #114714

Duplicate subquery explain plan output when explain format is tree

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114714](https://bugs.mysql.com/bug.php?id=114714)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："两份同一Select #2 subquery in projection dependent计划完整重复"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/114714/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/114714/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114714-8.0.33.sql)

### mysql-114799-8.0.33 · Bug #114799

ERROR 1216 vs ERROR 1452 in MySQL 8.0

官方版本字段：8.0.33, 8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114799](https://bugs.mysql.com/bug.php?id=114799)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114807-8.0.33 · Bug #114807

Subquery returns more than 1 row

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114807](https://bugs.mysql.com/bug.php?id=114807)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114970-8.0.33 · Bug #114970

prev_record_reads() use stale cardinality to calculate after plan enumeration

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114970](https://bugs.mysql.com/bug.php?id=114970)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115024-8.0.33 · Bug #115024

MySQL Crash occurs during MySQL Replication stop process

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115024](https://bugs.mysql.com/bug.php?id=115024)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115208-8.0.33 · Bug #115208

Last_query_cost could be negative number due to unmatched cost values in JOIN

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115208](https://bugs.mysql.com/bug.php?id=115208)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115332-8.0.33 · Bug #115332

Abnormal increase in the Innodb_rows_inserted metric value

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115332](https://bugs.mysql.com/bug.php?id=115332)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115397-8.0.33 · Bug #115397

statement_id variable has minimal documentation

官方版本字段：8.0.33 and above

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #115397](https://bugs.mysql.com/bug.php?id=115397)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115625-8.0.33 · Bug #115625

blob supports exceptions after java object serialization

官方版本字段：8.0.33

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #115625](https://bugs.mysql.com/bug.php?id=115625)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 缺Java序列化对象字节、Connector/J版本、建表与完整Java代码、jdbcURL；仅GBK连接/对象list描述不足，SQL文本不能替代客户端编码路径。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116012-8.0.33 · Bug #116012

MySQL8 - mysqld_'--no-monitor' option not working

官方版本字段：8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116012](https://bugs.mysql.com/bug.php?id=116012)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116703-8.0.33 · Bug #116703

`JSON_VALID` has inconsistent behavior for `NULL`

官方版本字段：8.0.33, 8.0.40, 8.4.3, 9.1.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #116703](https://bugs.mysql.com/bug.php?id=116703)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：JSON_VALID(NULL column) and JSON_VALID(NULL literal) must both be SQL NULL. Target column0 versus literalNULL; same abnormality exists in prior release.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/116703/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/116703/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-116703-8.0.33.sql)

### mysql-119581-8.0.33 · Bug #119581

FLOOR function shows inconsistent overflow handling

官方版本字段：8.0.33

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #119581](https://bugs.mysql.com/bug.php?id=119581)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- DOUBLE与DECIMAL溢出错误/警告是否必须统一，原文只记录不同现象。
- {"point": "DOUBLE与DECIMAL溢出错误/警告是否必须统一，原文只记录不同现象。", "evidence": "c555368已澄清是DECIMAL vs DOUBLE，不是列vs常量；未给目标版本统一预期规则。", "needed": "目标版本CAST/FLOOR溢出契约或修复说明；DOUBLE同类型控制实测输出。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119630-8.0.33 · Bug #119630

Optimizer incorrectly merges derived table with type conversion and WHERE clause, causing wrong query results

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #119630](https://bugs.mysql.com/bug.php?id=119630)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："默认派生 IN 错返全部三个主表行各两次，共 6 行；两个控制均只有 (2,20)。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/119630/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/119630/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-119630-8.0.33.sql)

### mysql-119631-8.0.33 · Bug #119631

CTE with type conversion and WHERE condition in IN/EXISTS subquery returns all rows instead of filtered rows

官方版本字段：8.0.33

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #119631](https://bugs.mysql.com/bug.php?id=119631)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-119631-8.0.33.sql)

### mysql-119646-8.0.33 · Bug #119646

View + Type Conversion + IN Subquery Returns Wrong Result

官方版本字段：8.0.33

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #119646](https://bugs.mysql.com/bug.php?id=119646)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.32 → 8.0.33，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："目标返回全部id1/2/3各两次，共6行；控制应恢复两行"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v33/cases/119646/review.json](../../experiments/saved_20261029/version_boundary_20261029/v33/cases/119646/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-119646-8.0.33.sql)

### mysql-120713-8.0.33 · Bug #120713

Optimizer incorrectly prefers ordering index over selective index for ORDER BY … LIMIT 1

官方版本字段：8.0.24, 8.0.33

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #120713](https://bugs.mysql.com/bug.php?id=120713)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-121062-8.0.33 · Bug #121062

Prepared statement with USING variables returns empty result against DATE + TIME columns

官方版本字段：8.0.33

状态：其他异常；阶段：baseline_preserved

官方报告：[Bug #121062](https://bugs.mysql.com/bug.php?id=121062)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-121062-8.0.33.sql)

### mysql-79813-8.0.34 · Bug #79813

Boolean values are returned inconsistently with JSON_OBJECT

官方版本字段：5.7.10, 8.0.0, 5.7.43, 8.0.34, 8.1.0

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #79813](https://bugs.mysql.com/bug.php?id=79813)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- All three JSON objects contain numeric can_edit 1/0/1 while direct TRUE/FALSE values are JSON booleans, matching the official report observation. This is report-level observation reproduction, not independent defect confirmation.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：获明确批准后仅重试一次：8.0.33 返回三个 JSON 对象，can_edit 为数值1/0/1，is_true/is_false 为 JSON 布尔值；与8.0.34完整输出相同。源 SQL/postcheck、release/amd64及关键环境相同。前版已有该报告的 JSON 类型现象；原启动超时记录保留，不能据此声称独立新缺陷。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-79813-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-79813-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-79813-8.0.34.sql)

### mysql-102586-8.0.34 · Bug #102586

Foreign Key ON DELETE CASCADE breaks with RBR and multiple-table DELETE.

官方版本字段：8.1.0, 8.0.34, 8.0.23, 5.7.33

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #102586](https://bugs.mysql.com/bug.php?id=102586)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires primary/replica topology with row-based binlog and applier error1032 after multi-table cascading DELETE; isolated single instance cannot reproduce replication outcome.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-104406-8.0.34 · Bug #104406

The result of querying through the secondary index is incorrect

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #104406](https://bugs.mysql.com/bug.php?id=104406)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111807-8.0.34 · Bug #111807

SELECT query assertion error

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111807](https://bugs.mysql.com/bug.php?id=111807)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain和c534510明确debug构建触发unsigned_flag断言，当前发布镜像条件不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111851-8.0.34 · Bug #111851

Spatial index not used for join when field is used in MBRIntersects call

官方版本字段：8.0.32, 8.0.34, 5.7.43

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111851](https://bugs.mysql.com/bug.php?id=111851)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- EXPLAIN shows Range checked for each record for variable spatial bounds, unlike constant-filter range plan. Plan difference alone does not prove index is unused at runtime; requires validated index-use contract/runtime observation rather than labeling different plans wrong results.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111852-8.0.34 · Bug #111852

An incorrect number of records is returned

官方版本字段：8.0.30, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111852](https://bugs.mysql.com/bug.php?id=111852)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111888-8.0.34 · Bug #111888

'alter table xxx import tablespace' lead server crash

官方版本字段：8.0.32, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111888](https://bugs.mysql.com/bug.php?id=111888)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111891-8.0.34 · Bug #111891

Assertion failed in table.h: void Table_ref::set_tableno(uint): Assertion `table

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111891](https://bugs.mysql.com/bug.php?id=111891)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires init.sql/case.sql with individually audited expected initialization errors plus target8.0.34 debug build; explicit debug assertion confirmed, stack alone lacks full SQL initialization.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111899-8.0.34 · Bug #111899

json generated column null problem

官方版本字段：8.0.32, 8.0.34, 5.7.43

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #111899](https://bugs.mysql.com/bug.php?id=111899)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Target error1048 is clear, but normal NOT NULL validation-stage behavior needs a separate oracle review; not blanket execution failure.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111900-8.0.34 · Bug #111900

FOREIGN KEY (prefix of parent table's PK/UK) should not have the PK/UK's name.

官方版本字段：5.7.43, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111900](https://bugs.mysql.com/bug.php?id=111900)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111917-8.0.34 · Bug #111917

derived condition pushdown query with wrong result

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111917](https://bugs.mysql.com/bug.php?id=111917)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确debug+ASan+UBSan及Boost1.77；当前release不满足原文构建。还需记录PIPES_AS_CONCAT模式。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111918-8.0.34 · Bug #111918

Auto increment column query wrong result

官方版本字段：8.1.0, 8.0.34, 5.7.43

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #111918](https://bugs.mysql.com/bug.php?id=111918)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："原 SELECT 返回两行，P、NOT P、P IS NULL 三个分区查询均为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-111918-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-111918-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-111918-8.0.34.sql)

### mysql-111952-8.0.34 · Bug #111952

Row constructor inequality comparison on Primary Key results in full table scan.

官方版本字段：8.0, 8.0.34, 8.0.45, 5.7.43, 8.1.0, 8.4, 8.4.8

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #111952](https://bugs.mysql.com/bug.php?id=111952)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Complete3million-row plan/performance comparison needs approved data-load time/disk/memory envelope and handler-counter instrumentation; existing small-case SQL replay cannot preserve scale by silently shrinking data.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111955-8.0.34 · Bug #111955

Prepared statement with CTE assertion error

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #111955](https://bugs.mysql.com/bug.php?id=111955)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain要求debug/ASAN/UBSAN；c535625也将CTE prepared assertion限定debug。当前环境不足。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\111955\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111961-8.0.34 · Bug #111961

MySQL 8.0.34 crashing suddenly

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111961](https://bugs.mysql.com/bug.php?id=111961)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111965-8.0.34 · Bug #111965

default NULL column leads to foreign key constraint failure

官方版本字段：8.0.34, 5.7.43

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #111965](https://bugs.mysql.com/bug.php?id=111965)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Composite FK containing NULL suppresses reference checking by defined semantics; c535065 corrects initial Verified. Successful NULL insert is not a Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111977-8.0.34 · Bug #111977

sql10637307

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #111977](https://bugs.mysql.com/bug.php?id=111977)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111980-8.0.34 · Bug #111980

MySQL Server does not read OpenSSL's openssl.cnf file unless ssl-fips-mode=ON

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #111980](https://bugs.mysql.com/bug.php?id=111980)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111983-8.0.34 · Bug #111983

Assertion failed in field.cc:4963: virtual longlong Field_temporal_with_date_and

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #111983](https://bugs.mysql.com/bug.php?id=111983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs init.sql from mysql-bug-data-111890.zip and case.sql plus actual8.0.34 debug build. Generic release SQL cannot validate debug read-set assertion, and tolerated generated setup errors require explicit audit.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-111986-8.0.34 · Bug #111986

Unused function dd_process_dd_columns_rec

官方版本字段：8.0.34,8.1.0

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #111986](https://bugs.mysql.com/bug.php?id=111986)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 仅unused dd_process_dd_columns_rec函数清理，复现方式grep，缺SQL可观测故障。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112008-8.0.34 · Bug #112008

Unused macro DBUG_EVALUATE

官方版本字段：8.0.34, 8.1.0

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112008](https://bugs.mysql.com/bug.php?id=112008)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Unused DBUG_EVALUATE macro is source-only cleanup request (grep for it); no runtime defect oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112022-8.0.34 · Bug #112022

Compiling with -DWITH_DEBUG=1 and using C++17 resulted in a failure.

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112022](https://bugs.mysql.com/bug.php?id=112022)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- C++17 compilation error requires WITH_DEBUG=1 WITH_LOCK_ORDER=ON, specifiedCMake3.27.1/GCC11/Boost1.77 and source revision; runtime replay not applicable.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112037-8.0.34 · Bug #112037

Contribute by tencent: explain analyze show never executed for materialize

官方版本字段：8.0.32, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112037](https://bugs.mysql.com/bug.php?id=112037)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：8.0.33 与8.0.34 的派生表扫描都已产生一行，物化/聚合子树却均标为 never executed；实际查询11–14、源数据1–4相同。计划结构与诊断矛盾一致，仅实际计时不同；前版已有该诊断现象，不作为 wrong_result 或性能退化。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112037-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112037-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112037-8.0.34.sql)

### mysql-112067-8.0.34 · Bug #112067

Failed to upgrade the query rewrite plugin installed in 5.7 to 8.0

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112067](https://bugs.mysql.com/bug.php?id=112067)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112084-8.0.34 · Bug #112084

performance optimization

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112084](https://bugs.mysql.com/bug.php?id=112084)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- __restrict optimization contribution explicitly has no performance experiment yet. Missing workload, release-build benchmark and accepted improvement oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112089-8.0.34 · Bug #112089

libmysqlclient21 8.0.34 introduces new warning output breaking applications

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112089](https://bugs.mysql.com/bug.php?id=112089)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112105-8.0.34 · Bug #112105

Create table from prepared statement issues

官方版本字段：8.1.0, 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112105](https://bugs.mysql.com/bug.php?id=112105)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原SQL生成分片中断，当前报告无最终SQL/判定器且限制未定位到单报告；保留队列，不重试生成。cmain的首次1486是预期，重复执行意外成功与debug断言须后续分开。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\112105\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112108-8.0.34 · Bug #112108

VIEW reference in a SELECT subquery returns different results between 5.7 & 8.0

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112108](https://bugs.mysql.com/bug.php?id=112108)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112116-8.0.34 · Bug #112116

Add AFTER_IMPORT_PER_TABLE option for deferTableIndexes in util.loadDump

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112116](https://bugs.mysql.com/bug.php?id=112116)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112117-8.0.34 · Bug #112117

innodb_print_all_deadlocks does not print header to error log

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112117](https://bugs.mysql.com/bug.php?id=112117)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112118-8.0.34 · Bug #112118

Free list record 11234 is above rec heap top 8812 - MySQL Server Not Starting

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112118](https://bugs.mysql.com/bug.php?id=112118)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Crash-on-startup requires original corrupted datadir and hosting/resource configuration; supplied log is not a reproducer. Out-of-memory must not be labeled target defect without causal evidence.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112120-8.0.34 · Bug #112120

FOREIGN KEY: the length of referencing/referenced columns should be compatible.

官方版本字段：Any, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112120](https://bugs.mysql.com/bug.php?id=112120)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112137-8.0.34 · Bug #112137

parallel read is slow when innodb_use_native_aio = off

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112137](https://bugs.mysql.com/bug.php?id=112137)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires sysbench60million rows, ~2GiB buffer pool, O_DIRECT, native-AIO startup toggle and cold restart; must approve resource envelope and preserve I/O environment rather than substitute tiny dataset.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112147-8.0.34 · Bug #112147

Use/Ignore Mutil-value index for MEMBER OF function has differnet result

官方版本字段：8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112147](https://bugs.mysql.com/bug.php?id=112147)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："USE返回a=1但IGNORE为空；DATE字面量IGNORE仍返回a=1"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112147-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112147-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112147-8.0.34.sql)

### mysql-112148-8.0.34 · Bug #112148

Description Failed to upgrade mysql from 8.0.20 to 8.0.34

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112148](https://bugs.mysql.com/bug.php?id=112148)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112149-8.0.34 · Bug #112149

Inconsistent results caused by SPACE() function and ''||'' operations

官方版本字段：8.0.34, 5.7.43, 5.6, 5.5

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #112149](https://bugs.mysql.com/bug.php?id=112149)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- CASE包含字符串分支，而简化后可能为数值OR，比较类型是否等价未确定。
- {"point": "CASE包含字符串分支，而简化后可能为数值OR，比较类型是否等价未确定。", "evidence": "cmain 的 THEN P 与 ELSE i&#124;&#124;~、对照删除CASE；未提供类型契约证明。", "needed": "目标MySQL的CASE/NULLIF类型推导规则及相同sql_mode下类型元数据/转换warnings。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112151-8.0.34 · Bug #112151

Wrong query output type

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112151](https://bugs.mysql.com/bug.php?id=112151)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires protocol column metadata collection (--column-type-info), and expected SHORT versus LONG promotion contract is unestablished. Debug/sanitizer merely reported, necessity not proven.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112152-8.0.34 · Bug #112152

Rename user to ''@'%' cause "Access denied"

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112152](https://bugs.mysql.com/bug.php?id=112152)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112153-8.0.34 · Bug #112153

ADD COLUMN with expressional DEFAULT does not support online ALTER TABLE

官方版本字段：8.0.34,8.1.0

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112153](https://bugs.mysql.com/bug.php?id=112153)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112154-8.0.34 · Bug #112154

Slow Queries Exceeding 1 Second in Concurrent Insert Scenario on MySQL 8.0.34

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112154](https://bugs.mysql.com/bug.php?id=112154)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires dual-primary replication, JMeter SeaSQL_insert10table_batch.jmx,50connections and10table schema/data with30min calibrated comparisons. Missing complete reproducible workload/environment and bounded protocol.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112158-8.0.34 · Bug #112158

Calling of stored procedure is not case sensitive

官方版本字段：8.0.13, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112158](https://bugs.mysql.com/bug.php?id=112158)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 需 Linux lower_case_table_names=0 以及独占 db1/DB1 两个大小写不同 schema，并核对源环境 by_expr_ignore_charset 设置；普通单 schema runner 未声明这些对象的清理归属。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112172-8.0.34 · Bug #112172

Left join query null value assertion error

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112172](https://bugs.mysql.com/bug.php?id=112172)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain和c535597为debug/ASAN/UBSAN的is_nullable断言；当前release不满足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112178-8.0.34 · Bug #112178

Transaction inconsistency when the undo space truncate is incomplete

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112178](https://bugs.mysql.com/bug.php?id=112178)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires source-injected30s sleep in undo truncation hook, DBUG crash/restart and concurrent transactions. Missing exact SQL/schema and deterministic interleaving; ordinary server lacks required injection.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112179-8.0.34 · Bug #112179

Backslash in string literals does not work for CREATE TABLE with NO_BACKSLASH_

官方版本字段：8.0.34-0ubuntu0.22.04.1

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112179](https://bugs.mysql.com/bug.php?id=112179)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112180-8.0.34 · Bug #112180

"Skip Scan Range Access Method" may lead to incorrect query results

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112180](https://bugs.mysql.com/bug.php?id=112180)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112184-8.0.34 · Bug #112184

cannot create user if they are listed as creator in views or routines

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112184](https://bugs.mysql.com/bug.php?id=112184)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires orphan-definer view/routine state from original mysqlsh dump, exact account grants including SET_USER_ID, and restore steps. Error4006 may be permission enforcement; absent dump and privilege context prevent definitive oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112194-8.0.34 · Bug #112194

Incorrect result when using INNER JOIN with SELECT FROM VIEW together with OR co

官方版本字段：8.0.34

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #112194](https://bugs.mysql.com/bug.php?id=112194)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- {"point": "哪种derived_merge设置触发的历史叙述互相矛盾。", "evidence": "c535821与c535885给出相反的开/关表格。", "needed": "后续每种开关分别记录实际计划和输出；不据旧描述跳过任一配置。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112198-8.0.34 · Bug #112198

Incorrect multiple equality optimization causes performance degradation

官方版本字段：8.0, 8.0.34

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #112198](https://bugs.mysql.com/bug.php?id=112198)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Plan observation only: left hash join rewrites extra condition to t1.a>0 and scans hash-build t2 without the t2.a>0 filter. No measured performance or wrong-result claim.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："EXPLAIN left hash join has extra condition t1.a > 0 and hash build child scans t2 without t2.a > 0 filter, matching cmain. Do not infer actual measured performance degradation from empty tables."

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112198-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112198-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112198-8.0.34.sql)

### mysql-112201-8.0.34 · Bug #112201

Deadlock with show fields, alter, and select

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #112201](https://bugs.mysql.com/bug.php?id=112201)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 两会话SHOW FIELDS/ALTER/SELECT死锁顺序已给，但缺a表定义、隔离级别、异步阻塞同步和死锁观测协议；普通单连接不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112212-8.0.34 · Bug #112212

Subquery to derived result mismatch(HASH JOIN/BNL JOIN result mismatch)

官方版本字段：8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112212](https://bugs.mysql.com/bug.php?id=112212)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："关闭为空，开启后错误返回 BIN(c1),c3 两行 (1010,1)、(1111,3)。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112212-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112212-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112212-8.0.34.sql)

### mysql-112231-8.0.34 · Bug #112231

Inconsistent result for OVER() when used in stored procedure over InnoDB table

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112231](https://bugs.mysql.com/bug.php?id=112231)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：Three historical predecessor runs and target evidence show the same source-bound anomaly; SQL and absent postcheck identical, recorded environment comparable.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112231-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112231-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112231-8.0.34.sql)

### mysql-112238-8.0.34 · Bug #112238

Inconsistent results caused by FIELD()

官方版本字段：5.5, 5.6, 5.7.43, 8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112238](https://bugs.mysql.com/bug.php?id=112238)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- CASE branches alter expression type: STRING_RESULT versus INT_RESULT changes FIELD comparison coercion. c535985 explains; value simplification is not type-preserving, hence no established equal-output oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112242-8.0.34 · Bug #112242

Unexpected Results by use_invisible_indexes

官方版本字段：8.1.0, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112242](https://bugs.mysql.com/bug.php?id=112242)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："off为空、on错误返回1。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112242-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112242-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112242-8.0.34.sql)

### mysql-112243-8.0.34 · Bug #112243

Unexpected Result by subquery_to_derived

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112243](https://bugs.mysql.com/bug.php?id=112243)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112252-8.0.34 · Bug #112252

InnoDB page compression impacts checkpointing

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112252](https://bugs.mysql.com/bug.php?id=112252)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112255-8.0.34 · Bug #112255

empty vio->signal_mask in the x plugin causes MySQL cannot handle signal

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112255](https://bugs.mysql.com/bug.php?id=112255)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires active mysqlsh X Protocol connection, exact Ubuntu ppoll build and controlled SIGTERM with shutdown log/exit-status oracle; generic SQL cannot exercise signal-delivery condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112256-8.0.34 · Bug #112256

The event thread_id of source changed after write to local

官方版本字段：8.0.30 and above, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112256](https://bugs.mysql.com/bug.php?id=112256)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112262-8.0.34 · Bug #112262

tablespace is missing for table innodb_undo_002

官方版本字段：8.0.19,8.0.26,8.0.30,8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112262](https://bugs.mysql.com/bug.php?id=112262)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112269-8.0.34 · Bug #112269

Unexpected Results by the hint JOIN_ORDER

官方版本字段：8.1.0, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112269](https://bugs.mysql.com/bug.php?id=112269)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："默认查询有一行，JOIN_ORDER(t2,t0) 后为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112269-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112269-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112269-8.0.34.sql)

### mysql-112275-8.0.34 · Bug #112275

"Extra" field has NULL value if table is temporary

官方版本字段：8.0.34, 8.0.11

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112275](https://bugs.mysql.com/bug.php?id=112275)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："临时表两个Extra是真SQL NULL（客户端NULL标记），普通表对应Extra为空字符串。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112275-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112275-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112275-8.0.34.sql)

### mysql-112280-8.0.34 · Bug #112280

Incorrect costing of group by loose index scans

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112280](https://bugs.mysql.com/bug.php?id=112280)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-level loose-index-scan costing proposal has read-code reproducer and illustrative formulas only; missing full schema/data and accepted measurable runtime/cost oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112287-8.0.34 · Bug #112287

log_slow_replica_statements will be deprecated on 8.0.34 and 8.1.0

官方版本字段：8.0.34, 8.1.0

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112287](https://bugs.mysql.com/bug.php?id=112287)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112289-8.0.34 · Bug #112289

No error seen when unknown column is used in subquery for Update Statement

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112289](https://bugs.mysql.com/bug.php?id=112289)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112293-8.0.34 · Bug #112293

Wrong result if non-breaking space is contained in varchar

官方版本字段：8.0, 8.0.34, 5.7.43

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112293](https://bugs.mysql.com/bug.php?id=112293)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："WHERE返回两行但TempTable GROUP BY分为两个count=1组"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112293-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112293-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112293-8.0.34.sql)

### mysql-112296-8.0.34 · Bug #112296

Unexpected Result by NO_BNL

官方版本字段：8.1.0, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112296](https://bugs.mysql.com/bug.php?id=112296)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："默认查询返回一个 NULL，NO_BNL(t0) 查询返回 1、2。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112296-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112296-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112296-8.0.34.sql)

### mysql-112297-8.0.34 · Bug #112297

Wrong query output type 2

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112297](https://bugs.mysql.com/bug.php?id=112297)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires protocol metadata and established MIN/derived type promotion contract (TINY versus LONGLONG); no authoritative expected type in report. Debug presence alone not necessary condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112306-8.0.34 · Bug #112306

Unexpected Result by JOIN_SUFFIX

官方版本字段：8.1.0, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112306](https://bugs.mysql.com/bug.php?id=112306)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："无hint COUNT1，JOIN_SUFFIX(t2,t3)后COUNT0。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112306-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112306-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112306-8.0.34.sql)

### mysql-112319-8.0.34 · Bug #112319

GROUP_CONCAT with GROUP BY and WHERE clause turns NULL into empty strings.

官方版本字段：8.0.33, 8.0.34, 8.1.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112319](https://bugs.mysql.com/bug.php?id=112319)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112345-8.0.34 · Bug #112345

Contribute by tencent: Repeated subquery plans were printed in format=tree.

官方版本字段：8.0.34

状态：证据不足；阶段：baseline_preserved

官方报告：[Bug #112345](https://bugs.mysql.com/bug.php?id=112345)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-112345-8.0.34.sql)

### mysql-112346-8.0.34 · Bug #112346

MEMBER_OF with multi-valued index on JSON not used in 99% of situations.

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112346](https://bugs.mysql.com/bug.php?id=112346)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- INSERT LOTS OF RANDOM DATA placeholder is not reproducible dataset; exact data, statistics and index-eligibility oracle needed. RAND per-row semantics cannot imply same plan as constant.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112359-8.0.34 · Bug #112359

Suspicious 'if' condition in get_current_user()

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_non_sql_code_review

官方报告：[Bug #112359](https://bugs.mysql.com/bug.php?id=112359)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain明确没有nullptr可达测试，只是get_current_user的if代码可疑；缺SQL触发路径，不可构造未证实的空指针调用。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112362-8.0.34 · Bug #112362

WHERE NOT IN with subquery is much slower on 8.1 than 5.7

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112362](https://bugs.mysql.com/bug.php?id=112362)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs exact10million-row dump linked via Google Drive plus loading/resource budget. Original speedup uses5.7 comparison outside current scope; target-only plan comparison requires approved frozen dataset.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112364-8.0.34 · Bug #112364

Create table like doesn't write the charset on binlog if its created from a temp

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112364](https://bugs.mysql.com/bug.php?id=112364)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112382-8.0.34 · Bug #112382

Update mysql server with yum/dnf ensures service is always enabled

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112382](https://bugs.mysql.com/bug.php?id=112382)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112387-8.0.34 · Bug #112387

Inconsistent results caused by "UNION ALL" with empty subqueries

官方版本字段：5.6, 5.7, 8.0.0-8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112387](https://bugs.mysql.com/bug.php?id=112387)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："带空 UNION ALL 分支查询为空，移除空分支后返回 NULL。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112387-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112387-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112387-8.0.34.sql)

### mysql-112389-8.0.34 · Bug #112389

Inconsistent results caused by a subquery in FROM clause

官方版本字段：5.7, 8.0.0 - 8.0.34

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #112389](https://bugs.mysql.com/bug.php?id=112389)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-112389-8.0.34.sql)

### mysql-112424-8.0.34 · Bug #112424

Crash during background rollback if both prepare and active transaction exist

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112424](https://bugs.mysql.com/bug.php?id=112424)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Explicit source patch adds sleep_before_trx_recovery_rollback and needs debug crash/restart plus two sessions; must retain injected original condition and not substitute release.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112439-8.0.34 · Bug #112439

Incorrect results when using VALUES statement as derived query

官方版本字段：8.1, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112439](https://bugs.mysql.com/bug.php?id=112439)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象：[[["1"], ["2"], ["3"]], [["1"], ["2"]]]

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112439-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112439-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112439-8.0.34.sql)

### mysql-112446-8.0.34 · Bug #112446

Fractured read at SERIALIZABLE

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112446](https://bugs.mysql.com/bug.php?id=112446)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112460-8.0.34 · Bug #112460

Inconsistent results of SELECT statement with window functions

官方版本字段：8.0.33, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112460](https://bugs.mysql.com/bug.php?id=112460)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：Three historical predecessor runs and target evidence show the same source-bound anomaly; SQL and absent postcheck identical, recorded environment comparable.

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112460-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112460-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112460-8.0.34.sql)

### mysql-112461-8.0.34 · Bug #112461

Assertion `!thd->lex->is_exec_started()' failed in /mysql-8.0.34/sql/item_func.c

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112461](https://bugs.mysql.com/bug.php?id=112461)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112462-8.0.34 · Bug #112462

Assertion Failure in home/wx/mysql-8.0.34/sql/sql_derived.cc:1641

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112462](https://bugs.mysql.com/bug.php?id=112462)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 仅 debug create_materialized_table 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112463-8.0.34 · Bug #112463

MySQL Delete, Insert Lock Occur

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112463](https://bugs.mysql.com/bug.php?id=112463)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Initial SQL duplicates PK1 and later output differs from inserts; subsequent lock discussion disputes gap-lock expectations. Need corrected dataset and agreed READ COMMITTED delete/unique-check gap-lock oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112464-8.0.34 · Bug #112464

Assertion Failure in /mysql-8.0.34/sql/handler.cc:7908

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112464](https://bugs.mysql.com/bug.php?id=112464)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536321确认debug build，c536322明确release not affected；缺debug，不能以release执行代替handler断言验证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112465-8.0.34 · Bug #112465

Assertion Failure in /mysql-8.0.34/sql/sql_table.cc:12188

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112465](https://bugs.mysql.com/bug.php?id=112465)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文明确only debug build affected，ALTER断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112470-8.0.34 · Bug #112470

Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:642

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112470](https://bugs.mysql.com/bug.php?id=112470)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112475-8.0.34 · Bug #112475

Assertion Failure in /mysql-8.0.34/sql/sql_select.cc:2303

官方版本字段：8.0.34

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #112475](https://bugs.mysql.com/bug.php?id=112475)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-112475-8.0.34.sql)

### mysql-112478-8.0.34 · Bug #112478

Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:524

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112478](https://bugs.mysql.com/bug.php?id=112478)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112479-8.0.34 · Bug #112479

Assertion Failure in /mysql-8.0.34/sql/sql_executor.cc:4222

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112479](https://bugs.mysql.com/bug.php?id=112479)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug replace_embedded_rollup_references 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112480-8.0.34 · Bug #112480

Assertion Failure in /mysql-8.0.34/sql/handler.cc:2966

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112480](https://bugs.mysql.com/bug.php?id=112480)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536428和c536429确认debug ha_rnd_next inited==RND断言；当前release不具备构建条件。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112487-8.0.34 · Bug #112487

Assertion Failure in /mysql-8.0.34/sql/sql_optimizer.cc:343

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112487](https://bugs.mysql.com/bug.php?id=112487)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 官方评论明确8.0.34 debug，目标query_tables_locked断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112491-8.0.34 · Bug #112491

Assertion Failure in /mysql-8.0.34/sql/item_subselect.cc:2415

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112491](https://bugs.mysql.com/bug.php?id=112491)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- debug !sl->order_list.first 断言，验证与内部重复号均保留；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112494-8.0.34 · Bug #112494

Assertion Failure in /mysql-8.0.34/sql/sql_select.cc:4222

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112494](https://bugs.mysql.com/bug.php?id=112494)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536371确认debug build及having_cond位图断言；当前release缺所需构建，不将RAND输出当正确性oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112495-8.0.34 · Bug #112495

Assertion Failure in /mysql-8.0.34/sql/sql_optimizer.cc:8930

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112495](https://bugs.mysql.com/bug.php?id=112495)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 官方评论明确8.0.34 debug，目标test_if_ref断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112497-8.0.34 · Bug #112497

Assertion Failure in /mysql-8.0.34/sql/field.cc:7108

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112497](https://bugs.mysql.com/bug.php?id=112497)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536374 验证仅 debug 的 Field_blob::val_real read_set 断言；缺 debug；保留原反斜线字符串。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112498-8.0.34 · Bug #112498

Assertion Failure in /mysql-8.0.34/sql/sql_resolver.cc:183

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112498](https://bugs.mysql.com/bug.php?id=112498)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536375确认debug sql_resolver断言；c539431修复移除断言但不代表当前8.0版本已修复。当前构建不足。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112499-8.0.34 · Bug #112499

Assertion Failure in /mysql-8.0.34/sql/sql_tmp_table.cc:485

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112499](https://bugs.mysql.com/bug.php?id=112499)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 官方评论明确8.0.34 debug，目标create_tmp_field断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112500-8.0.34 · Bug #112500

Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:4127

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112500](https://bugs.mysql.com/bug.php?id=112500)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536379 验证 debug dump_leaf_key offset<reclength 断言；缺 debug；RAND 值变化不是目标。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112501-8.0.34 · Bug #112501

Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:784

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112501](https://bugs.mysql.com/bug.php?id=112501)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原SQL生成工具分片中断，未有SQL交付；不重试转写。c536378还确认debug构建条件；f32622是栈附件而非缺SQL。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\112501\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112502-8.0.34 · Bug #112502

Assertion Failure in /mysql-8.0.34/sql/item_sum.cc:1598

官方版本字段：8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112502](https://bugs.mysql.com/bug.php?id=112502)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112510-8.0.34 · Bug #112510

Assertion Failure in /mysql-8.0.34/sql/sql_const_folding.cc:275

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112510](https://bugs.mysql.com/bug.php?id=112510)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536396/c536398 验证 debug analyze_int_field_constant 精度断言；c536577 说明是过强断言，不能用 release 没有断言判未复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112512-8.0.34 · Bug #112512

Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:9133

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112512](https://bugs.mysql.com/bug.php?id=112512)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536402确认debug setup_fields !thd->is_error断言；原SQL完整但当前缺debug构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112513-8.0.34 · Bug #112513

Assertion Failure in /mysql-8.0.34/sql/item.h:2103

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112513](https://bugs.mysql.com/bug.php?id=112513)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 官方评论明确8.0.34 debug，目标m_nullable断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112514-8.0.34 · Bug #112514

Assertion Failure in /mysql-8.0.34/sql/sql_lex.cc:2288

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112514](https://bugs.mysql.com/bug.php?id=112514)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536405 验证 debug Query_expression::exclude_tree 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112516-8.0.34 · Bug #112516

Assertion Failure in /mysql-8.0.34/sql/item.cc:1202

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112516](https://bugs.mysql.com/bug.php?id=112516)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536410确认debug may_evaluate_const断言；原CTAS SQL完整，正常SQL受控错误不能代替该断言，缺debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112517-8.0.34 · Bug #112517

Assertion Failure in /mysql-8.0.34/sql/item.cc:8044

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112517](https://bugs.mysql.com/bug.php?id=112517)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 官方评论明确8.0.34 debug，目标Item_ref::fix_fields断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112518-8.0.34 · Bug #112518

Assertion Failure in /mysql-8.0.34/sql/item_func.cc:1881

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112518](https://bugs.mysql.com/bug.php?id=112518)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536414 验证 debug Item_typecast_signed::val_int is_nullable 断言；缺 debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112521-8.0.34 · Bug #112521

Abort in /mysql-8.0.34/sql/signal_handler.cc:286

官方版本字段：8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112521](https://bugs.mysql.com/bug.php?id=112521)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c536420/c536421确认debug temptable::Handler::index_first的abort；当前发布构建不足，不能仅凭连接成功否定。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112523-8.0.34 · Bug #112523

UPDATE/DELETE not using PRIMARY index (even with FORCE INDEX) - causing locks

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112523](https://bugs.mysql.com/bug.php?id=112523)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112524-8.0.34 · Bug #112524

Inconsistent results of UNIX_TIMESTAMP with NULLIF and COALESCE

官方版本字段：5.7, 8.0.0, 8.0.34

状态：其他异常；阶段：baseline_preserved

官方报告：[Bug #112524](https://bugs.mysql.com/bug.php?id=112524)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-112524-8.0.34.sql)

### mysql-112527-8.0.34 · Bug #112527

Inconsistent results caused by REPEAT function

官方版本字段：8.0.11, 8.0.34, 8.1.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112527](https://bugs.mysql.com/bug.php?id=112527)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："嵌套CASE为2并警告，简化CASE为3；须核对警告是报告REPEAT长度问题，而非环境容量上限"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112527-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112527-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112527-8.0.34.sql)

### mysql-112541-8.0.34 · Bug #112541

Incorrect results when using group by loose index scan

官方版本字段：8.1, 8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112541](https://bugs.mysql.com/bug.php?id=112541)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Complete source needs debug force_lis_for_group_by plus global innodb_purge_stop_now. These debug controls are functional prerequisites to preserve deleted records and force exact loose-index scan; ordinary release insufficient.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112557-8.0.34 · Bug #112557

Inconsistent results of SELECT statement with EXISTS clause

官方版本字段：8.0.27,8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112557](https://bugs.mysql.com/bug.php?id=112557)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："TRUE AND EXISTS 返回 NULL、NULL，简化为 EXISTS 后返回 0、NULL。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112557-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112557-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112557-8.0.34.sql)

### mysql-112579-8.0.34 · Bug #112579

Inconsistent results of SELECT with <=> and NULLIF

官方版本字段：8.0.14 - 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112579](https://bugs.mysql.com/bug.php?id=112579)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原SQL生成分片受工具中断而无交付SQL；保留未完成队列，不重新转写。原文两个数据行及多重集差分需待获可执行交付后核验。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\112579\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112589-8.0.34 · Bug #112589

ER_ROW_IS_REFERENCED vs ER_ROW_IS_REFERENCED_2 breaks backwards compatibility

官方版本字段：8.0.33, 8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112589](https://bugs.mysql.com/bug.php?id=112589)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-based privilege/error-code compatibility issue lacks complete users/grants and FK schema/operation matrix. Requires multiaccount ACL test;1217/1451 are expected errors whose code distinction must be deliberately validated.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112604-8.0.34 · Bug #112604

Inconsistent and misleading message when ALTER TABLE fills the disk.

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112604](https://bugs.mysql.com/bug.php?id=112604)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112619-8.0.34 · Bug #112619

STOP GROUP_REPLICATION on primary during ALTER leads to a confusing message.

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112619](https://bugs.mysql.com/bug.php?id=112619)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires single-primary Group Replication topology plus131072 widened rows, concurrent ALTER FORCE and STOP GROUP_REPLICATION with timing; single ordinary instance cannot represent condition.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112621-8.0.34 · Bug #112621

Performance degradation from 8.0.30 onwards related to performance_schema

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112621](https://bugs.mysql.com/bug.php?id=112621)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112639-8.0.34 · Bug #112639

Missing plugin assertion error

官方版本字段：8.1.0, 8.0.34, 5.7.43

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112639](https://bugs.mysql.com/bug.php?id=112639)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Explicit WITH_DEBUG/ASAN/UBSAN build and startup thread_handling=loaded-dynamically while plugin absent. Target is startup assertion, not SQL error; requires matching startup environment.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112641-8.0.34 · Bug #112641

ORDER BY does not work with CREATE TEMPORARY TABLE

官方版本字段：8.0.28, 5.7.43, 8.0.34, 8.1.0

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #112641](https://bugs.mysql.com/bug.php?id=112641)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c536764明确内层ORDER BY与外层LIMIT不保证共同求值，优化器可消除排序；返回1不是冻结Bug判据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112646-8.0.34 · Bug #112646

Unable to Start MySQL 8.0.33 on CentOS 7.9 (ARM Architecture)

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112646](https://bugs.mysql.com/bug.php?id=112646)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- CentOS7aarch64 startup issue duplicates110752. Original text/version/package steps differ8.0.33/34/8.1.0; need precise matching target package and ARM/glibc hardware environment.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112647-8.0.34 · Bug #112647

clang-format 17 errors out on .clang-format

官方版本字段：8.0.34,8.1.0

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #112647](https://bugs.mysql.com/bug.php?id=112647)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 目标为clang-format17解析源码树.clang-format重复key错误；需要该版本源码文件与clang-format17，SQL回放不适用，不能把格式工具故障称数据库运行Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112660-8.0.34 · Bug #112660

Got error -1 - 'Unknown error -1' from storage engine

官方版本字段：8.1.0, 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112660](https://bugs.mysql.com/bug.php?id=112660)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112661-8.0.34 · Bug #112661

Got 'Unknown error -1' when create index on table

官方版本字段：8.1.0, 8.0.34

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112661](https://bugs.mysql.com/bug.php?id=112661)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：8.0.33 与8.0.34 均成功建 ARCHIVE 表，SHOW CREATE/SHOW ENGINES 确认引擎；随后指定 CREATE INDEX（第7行）报1030/HY000 Unknown error -1。普通不支持 BTREE 的3502提示、建表日期截断1292单独保留；判定依据是相同内部错误诊断，非普通能力拒绝，亦非 wrong_result。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112661-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112661-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112661-8.0.34.sql)

### mysql-112670-8.0.34 · Bug #112670

Documentation outdated related ANALYZE TABLE locking

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112670](https://bugs.mysql.com/bug.php?id=112670)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112694-8.0.34 · Bug #112694

MYSQL master crashes frequently after upgrade from 8.0.28 to 8.0.34

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112694](https://bugs.mysql.com/bug.php?id=112694)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112698-8.0.34 · Bug #112698

Assertion failure in Item_func_like::Item_func_like

官方版本字段：8.1.0, 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112698](https://bugs.mysql.com/bug.php?id=112698)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL；c536914确认debug Item_func_like解析阶段断言且原对象依赖须澄清；不补造v0/v1，不重试生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\112698\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112705-8.0.34 · Bug #112705

sys.schema_table_statistics reset values upon index addition or removal

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112705](https://bugs.mysql.com/bug.php?id=112705)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Counter reset after index DDL is observable but report lacks accepted counter-persistence contract. DDL may reset per-table instrumentation; require resolve whether reset violates documented behavior before counting Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112708-8.0.34 · Bug #112708

INSERT .. DEFAULT broken when when columns are out of order

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #112708](https://bugs.mysql.com/bug.php?id=112708)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- INSERT列顺序与默认表达式依赖存在评论解释前后矛盾（c536960/c537043）；需先核验目标版本默认表达式求值契约，不能按[3,4]预设判错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112712-8.0.34 · Bug #112712

Assertion `!null_value || is_nullable()' failed in MySQL 8.1.0

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112712](https://bugs.mysql.com/bug.php?id=112712)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文8.1 debug，官方补证8.0.34 debug，目标unsigned nullable断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112714-8.0.34 · Bug #112714

Assertion failure: clone0api.cc:1159:ib::fatal in cloning when undo_x_trunc.log

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112714](https://bugs.mysql.com/bug.php?id=112714)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Needs exact undo_1_trunc.log file, donor/receiver clone plugin, receiver super_read_only history and datadir/restart sequence. Reporter and verifier disagree; generic datadir or fabricated truncation file cannot substitute.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112717-8.0.34 · Bug #112717

Undo log truncation does not finalize when super_read_only=1

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112717](https://bugs.mysql.com/bug.php?id=112717)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112720-8.0.34 · Bug #112720

Query triggers an assertion Failure in eval_const_cond

官方版本字段：8.1.0, 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112720](https://bugs.mysql.com/bug.php?id=112720)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112737-8.0.34 · Bug #112737

Conditions refering to const table were not added to RANGE SCAN

官方版本字段：8.0, 8.0.34

状态：报告现象已复现；阶段：executed_reproduced

官方报告：[Bug #112737](https://bugs.mysql.com/bug.php?id=112737)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Plan observation only: covering PRIMARY index range retains a=2 and 2<=b but lacks upper b<=4; residual filter retains the upper condition. No measured performance or wrong-result claim.

相邻比较：8.0.33 → 8.0.34，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："Covering index range scan has a=2 and lower bound2<=b but omits upper b<=4, while filter above scan retains t2.b<=cache(2+2)."

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112737-8.0.34/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112737-8.0.34/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112737-8.0.34.sql)

### mysql-112738-8.0.34 · Bug #112738

can't truncate partition when partition_id exceed INT_MAX

官方版本字段：8.0.30, 8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112738](https://bugs.mysql.com/bug.php?id=112738)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112740-8.0.34 · Bug #112740

startup message when checking tables

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112740](https://bugs.mysql.com/bug.php?id=112740)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Startup log thread-number enhancement requires200k-table datadir and prolonged startup; no complete schema/data generator or approved disk/time budget. Logging readability is not SQL-result defect.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112757-8.0.34 · Bug #112757

Comparison on FLOAT column return wrong result

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #112757](https://bugs.mysql.com/bug.php?id=112757)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- FLOAT1.01与精确十进制字面量比较可能受二进制舍入影响，c537066判Not a bug；不能把空集当Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112759-8.0.34 · Bug #112759

Calculation on DOUBLE column return wrong result

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112759](https://bugs.mysql.com/bug.php?id=112759)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Repeated DOUBLE additions produce IEEE rounding; official c537069 explicitly expected. 1.1300000000000001 must not count as Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112766-8.0.34 · Bug #112766

Feature req: SOURCE_SSL should default to 1 for replication

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112766](https://bugs.mysql.com/bug.php?id=112766)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112767-8.0.34 · Bug #112767

SELECT COUNT(*) degraded performance on 8.0 compared to 5.7

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112767](https://bugs.mysql.com/bug.php?id=112767)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112768-8.0.34 · Bug #112768

Inconsistent results when tables are JOINed in a different order

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112768](https://bugs.mysql.com/bug.php?id=112768)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer c537093 explains error-producing JSON expression is never evaluated with empty-first join. Error versus no error is permissible evaluation-order behavior, not defect oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112770-8.0.34 · Bug #112770

Assertion `!thd->is_error()' failed in MySQL 8.1.0

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112770](https://bugs.mysql.com/bug.php?id=112770)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain/c537089为debug-asan的Sql_cmd_dml::prepare断言，c537090明确release not affected；缺所需debug环境。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112772-8.0.34 · Bug #112772

Assertion `is_nullable()' failed in MySQL 8.1.0

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112772](https://bugs.mysql.com/bug.php?id=112772)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文8.1 debug，官方补证8.0.34 debug，目标signed is_nullable断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112773-8.0.34 · Bug #112773

Primary key based query reading more number of pages in 8.0 compared to 5.7

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112773](https://bugs.mysql.com/bug.php?id=112773)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112780-8.0.34 · Bug #112780

innodb_temp_data_file_path changed from relative to absolute path in 8.0

官方版本字段：8.0.34, 8.1.0

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112780](https://bugs.mysql.com/bug.php?id=112780)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112787-8.0.34 · Bug #112787

regexp/rlike function in routines extreme regression mysql 5.7 to mysql 8

官方版本字段：8.0.34, 8.1.0

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #112787](https://bugs.mysql.com/bug.php?id=112787)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112798-8.0.34 · Bug #112798

The configuration value of innodb_buffer_pool_size underflow

官方版本字段：8.1, 8.0.34

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #112798](https://bugs.mysql.com/bug.php?id=112798)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需两次SET GLOBAL buffer_pool_size=UINT64_MAX并检查underflow；会触发全局内存调整，需专用资源上限/恢复及确认是变量下溢而非OOM，普通批次不适合。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112800-8.0.34 · Bug #112800

New table are reported as existing in mysql

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #112800](https://bugs.mysql.com/bug.php?id=112800)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Only says create a table and error1050; exact CREATE, prior schema state and proof table absent are missing. Existing-table error is normal unless contradictory state demonstrated.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112802-8.0.34 · Bug #112802

Inconsistent results when using INDEX

官方版本字段：8.1.0, 8.0.34

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112802](https://bugs.mysql.com/bug.php?id=112802)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112824-8.0.34 · Bug #112824

Different processing of WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS by INNODB and MYISAM

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #112824](https://bugs.mysql.com/bug.php?id=112824)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 正文仅source CREATE.sql/select-innodb.sql/select-myiasm.sql；c537307仍索要两个select文件。需附件全部SQL与完整顺序，不能猜测WHERE表达式。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112826-8.0.34 · Bug #112826

Decimal query with wrong result

官方版本字段：8.1.0, 8.0.34

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112826](https://bugs.mysql.com/bug.php?id=112826)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain明确WITH_DEBUG/ASAN/UBSAN及Boost1.77；旧case漏记构建依赖。当前release不能作为原条件重放，保留待专用构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112873-8.0.34 · Bug #112873

Locked account is not shown in mysql.user

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112873](https://bugs.mysql.com/bug.php?id=112873)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112982-8.0.34 · Bug #112982

Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:558

官方版本字段：8.0.34, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112982](https://bugs.mysql.com/bug.php?id=112982)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112983-8.0.34 · Bug #112983

Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:7731

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112983](https://bugs.mysql.com/bug.php?id=112983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c537781/c537782 区分 release 与 debug；同名 CTE 的 sql_base 断言需要 debug，普通 release 无断言不构成否证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113036-8.0.34 · Bug #113036

Assertion Failure in /mysql-8.0.34/sql/field.cc:4318

官方版本字段：8.0.34, 8.0.35, 8.1.0, 8.2.0

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #113036](https://bugs.mysql.com/bug.php?id=113036)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c537920确认8.0.35 debug Field_double::val_real断言；无ORDER BY的LIMIT结果本身不能代替崩溃oracle。缺debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113037-8.0.34 · Bug #113037

Assertion Failure in /mysql-8.0.34/sql/my_decimal.h:186

官方版本字段：8.0.34, 8.0.35, 8.1.0, 8.2.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113037](https://bugs.mysql.com/bug.php?id=113037)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official assertion reproduction confirms8.0.35 debug build; release query result or normal errors do not establish decimal assertion. Requires target debug build with original SQL and startup verification.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113175-8.0.34 · Bug #113175

Getting wrong result for locked rows

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_environment_and_oracle_gap

官方报告：[Bug #113175](https://bugs.mysql.com/bug.php?id=113175)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 两会话锁等待交错完整但c538273质疑是否实际索引访问；需冻结隔离级别、索引计划、阻塞握手和当前读语义，单连接不能验证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113219-8.0.34 · Bug #113219

Wrong value of auto_increment while executing load data replace

官方版本字段：MySQL8.0.34，MySQL8.2.0

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113219](https://bugs.mysql.com/bug.php?id=113219)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires semisync primary/replica,50k initial rows and LOAD DATA physical file. Exact seed rows missing; auto-increment reservation gaps/metadata differences do not imply replication failure, as later comments clarify.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113256-8.0.34 · Bug #113256

DATA_FREE displayed wrong when checking "PARTITIONS" table

官方版本字段：8.0.34

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113256](https://bugs.mysql.com/bug.php?id=113256)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- DATA_FREE 的表级估算与分区级统计是否须严格相等需要契约确认，不能单凭原数值差异自动判 bug
- {"point": "表级与分区级 DATA_FREE 的统计时间/口径及误差要求尚未冻结。", "evidence": "cmain 是 40,000 次 INSERT 与分区0/表级4194304差异；c538485 确认历史 Information Schema bug，但不能替代目标版测量契约。", "needed": "目标统计缓存、ANALYZE 时机、页布局及 TABLES/PARTITIONS DATA_FREE 口径；记录过程循环替换 shell 循环的影响。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113338-8.0.34 · Bug #113338

return error result with a qubquery

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #113338](https://bugs.mysql.com/bug.php?id=113338)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain要求附件建表/数据，c538679更正表名tt0/tt1；正文无DDL/DML，需对应附件及订正查询，不得拼造数据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113369-8.0.34 · Bug #113369

In the hash partition table, the query result is error.

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113369](https://bugs.mysql.com/bug.php?id=113369)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- YEAR/INT隐式比较与常量折叠后类型转换的规范性边界。
- {"point": "YEAR/INT隐式比较与常量折叠后类型转换的规范性边界。", "evidence": "c539471解释CAST(61 AS YEAR)=2061，同时记录删除id=61反而有行，尚未给最终契约。", "needed": "目标8.0比较转换规则和计划/表达式类型证据；后续用原式与控制分别保存输出。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113410-8.0.34 · Bug #113410

hang creating InnoDB Cluster

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113410](https://bugs.mysql.com/bug.php?id=113410)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Four-node InnoDB Cluster/mysqlsh sandbox hang depends on WSL and external 4.sh/log attachments; normal Linux did not reproduce in c539135. Need attachment, matching WSL/MySQL Shell versions and cluster topology; isolated single-server SQL is insufficient.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113430-8.0.34 · Bug #113430

Query slowness in Delete query with many child table

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113430](https://bugs.mysql.com/bug.php?id=113430)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113431-8.0.34 · Bug #113431

Metadata locking - Table creation with FK constraint

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113431](https://bugs.mysql.com/bug.php?id=113431)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c539029 explicitly identifies FK metadata-lock wait as expected corrected behavior; reporter accepts clarification. Do not count normal MDL waiting as Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113437-8.0.34 · Bug #113437

connection is not established with server can do anything in sql bench

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #113437](https://bugs.mysql.com/bug.php?id=113437)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 只有Workbench自动日志位置提示，无连接步骤或错误内容；c539024请求资料后挂起，需要wb.log/连接配置/版本。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113466-8.0.34 · Bug #113466

MySQL provides Truncated incorrect DOUBLE value: '0A000' error in trigger

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113466](https://bugs.mysql.com/bug.php?id=113466)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Trigger calls multiple missing stored procedures, and workflow_item schema/data and triggering INSERT are absent. c539186 explicitly requests complete table definitions/content/statements. Cannot invent these dependencies.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113548-8.0.34 · Bug #113548

Cloning failing in Mysql Group replication

官方版本字段：8.0.34-26

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113548](https://bugs.mysql.com/bug.php?id=113548)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113694-8.0.34 · Bug #113694

misleading error message comparing a spatial column with numeric using < or such

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113694](https://bugs.mysql.com/bug.php?id=113694)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Geometry comparison error is expected rejection and c539866 explicitly closes Not a Bug; complaint concerns wording and transformed operator. Original query also contains broken identifier whitespace. Cannot call ordinary error1210 a defect without accepted message contract.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113819-8.0.34 · Bug #113819

when use show engine innodb cannot show correct information

官方版本字段：8.0.34, 8.0.33

状态：证据不足；阶段：ready_saved_before_task_interruption

官方报告：[Bug #113819](https://bugs.mysql.com/bug.php?id=113819)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Materials were saved before the owning review task was interrupted; this item was not separately identified as the trigger. No continuation of the interrupted task.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114255-8.0.34 · Bug #114255

Install Community Edition 8.0.34/35glibc2.28-arm Version error

官方版本字段：8.0.34/35

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #114255](https://bugs.mysql.com/bug.php?id=114255)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 故障是aarch64 64KiB页系统加载glibc2.28包中OpenSSL ELF；需原8.0.34/35 ARM包与64KiB页Linux，x86容器或重编译替换库不等价。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114434-8.0.34 · Bug #114434

Passwords in mysql.slave_master_info should be encrypted

官方版本字段：8.0.34

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #114434](https://bugs.mysql.com/bug.php?id=114434)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114629-8.0.34 · Bug #114629

partially upgraded DD

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114629](https://bugs.mysql.com/bug.php?id=114629)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114650-8.0.34 · Bug #114650

The prepare statement execution result is wrong, but there is data output

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #114650](https://bugs.mysql.com/bug.php?id=114650)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- SET @a syntax error leaves previous variable value unchanged; following EXECUTE is a separate statement. Later rows are normal retained session state, not evidence of faulty PREPARE.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114694-8.0.34 · Bug #114694

binlog_transaction_compression not effect on slave

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114694](https://bugs.mysql.com/bug.php?id=114694)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114792-8.0.34 · Bug #114792

Gettin erroe while using run my sql script

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114792](https://bugs.mysql.com/bug.php?id=114792)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115035-8.0.34 · Bug #115035

View with ORDER BY misses a row

官方版本字段：8.0.34, 8.3

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #115035](https://bugs.mysql.com/bug.php?id=115035)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115085-8.0.34 · Bug #115085

INDEX using CAST (json_column) AS ARRAY drops rows containing empty array

官方版本字段：8.0.34, 8.4.0

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #115085](https://bugs.mysql.com/bug.php?id=115085)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原报告要求10000行gist数据，本地冻结正文只含两行。
- {"point": "原报告要求10000行gist数据，本地冻结正文只含两行。", "evidence": "cmain的gist链接及Load up the table with 10000 rows；c543556补充空数组行。", "needed": "本地已存完整数据附件或后续取得的带SHA版本；当前小数据实际计划不保证触发。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115216-8.0.34 · Bug #115216

range_optimizer_max_mem_size calculation on with large IN queries

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115216](https://bugs.mysql.com/bug.php?id=115216)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115259-8.0.34 · Bug #115259

query_rewrite not working in 8.0.34

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115259](https://bugs.mysql.com/bug.php?id=115259)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115459-8.0.34 · Bug #115459

global read_only = 1 with read only = 0 on schema level blocks writes to schema

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115459](https://bugs.mysql.com/bug.php?id=115459)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115464-8.0.34 · Bug #115464

Cannot connect to server

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115464](https://bugs.mysql.com/bug.php?id=115464)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115542-8.0.34 · Bug #115542

MY-012872 MySQL Issues crash on long running large table update

官方版本字段：8.0.34-26

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115542](https://bugs.mysql.com/bug.php?id=115542)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115808-8.0.34 · Bug #115808

Simple "comment" change operation in partition table should be treat as Metadata

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #115808](https://bugs.mysql.com/bug.php?id=115808)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 明确feature request，REORGANIZE含分区变更且需MDL；阻塞DML本属已说明行为，缺支持无阻塞元数据变更的现有契约。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116430-8.0.34 · Bug #116430

Concurrent DELETE statements of different rows causing deadlocking

官方版本字段：8.0.34, 8.0.40

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116430](https://bugs.mysql.com/bug.php?id=116430)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116852-8.0.34 · Bug #116852

Difference between JSONPath "$" vs "$[*]"

官方版本字段：8.0.34, 8.0.40

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #116852](https://bugs.mysql.com/bug.php?id=116852)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-116852-8.0.34.sql)

### mysql-116983-8.0.34 · Bug #116983

Master's binary log didn't apply data but write to slave's binary log

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116983](https://bugs.mysql.com/bug.php?id=116983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117069-8.0.34 · Bug #117069

The slave recorded the master's binary log into the binary log without applying it to the data

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117069](https://bugs.mysql.com/bug.php?id=117069)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117102-8.0.34 · Bug #117102

Histogram Statistics Analysis cannot apply on standby database

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #117102](https://bugs.mysql.com/bug.php?id=117102)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 三行数据及ANALYZE HISTOGRAM明确，需独立主从复制与同步后两侧COLUMN_STATISTICS检查；单实例不能验证复制遗漏。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117337-8.0.34 · Bug #117337

Transaction Commit Allowed on Blackhole Table After read_only=1 is Enabled

官方版本字段：8.0.34-26, 8.0.41

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117337](https://bugs.mysql.com/bug.php?id=117337)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117419-8.0.34 · Bug #117419

BEFORE INSERT trigger causes all columns in DEFAULT value expression to be NULL

官方版本字段：8.0.34, 8.0.41, 8.4.4, 9.2.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #117419](https://bugs.mysql.com/bug.php?id=117419)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117646-8.0.34 · Bug #117646

InnoDB Purge Process Inefficiency on Idle Serve

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117646](https://bugs.mysql.com/bug.php?id=117646)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117670-8.0.34 · Bug #117670

Unknown column '?' in 'group statement'

官方版本字段：8.0.34, 8.0.41

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #117670](https://bugs.mysql.com/bug.php?id=117670)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Target 8.0.34 correctly rejects qualified outer alias a.sdate; c551187 says earlier erroneous name resolution was fixed. Normal 1054 on target is not reported defect.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118936-8.0.34 · Bug #118936

Root password

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #118936](https://bugs.mysql.com/bug.php?id=118936)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119807-8.0.34 · Bug #119807

Generated default values bypass BLOB/TEXT/JSON default value restriction

官方版本字段：8.0.34

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #119807](https://bugs.mysql.com/bug.php?id=119807)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Expression defaults on TEXT/BLOB/JSON explicitly allowed; c555848 quotes distinction. Successful expression default is normal behavior, not bypass Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119908-8.0.34 · Bug #119908

GROUP_CONCAT returns corrupted characters when column charset is utf8mb4 and connection charset is gbk

官方版本字段：8.0.34

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #119908](https://bugs.mysql.com/bug.php?id=119908)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120974-8.0.34 · Bug #120974

Client connection kill command doesn't kill process

官方版本字段：8.0.34-26

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #120974](https://bugs.mysql.com/bug.php?id=120974)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-68925-8.0.35 · Bug #68925

Compatibility issue with mysql history ("\040" instead of space)

官方版本字段：5.6.10, 5.5.29, 8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #68925](https://bugs.mysql.com/bug.php?id=68925)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-109155-8.0.35 · Bug #109155

Invalid scan on left join tables of which columns not in distinct output fields

官方版本字段：8.0.18, 8.0.31, 8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #109155](https://bugs.mysql.com/bug.php?id=109155)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Complete small SQL illustrates redundant scans but claim is performance regression versus old iterator; no frozen target-only cost/handler threshold or 60000-row customer data. Need target-only performance oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112767-8.0.35 · Bug #112767

SELECT COUNT(*) degraded performance on 8.0 compared to 5.7

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112767](https://bugs.mysql.com/bug.php?id=112767)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112873-8.0.35 · Bug #112873

Locked account is not shown in mysql.user

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112873](https://bugs.mysql.com/bug.php?id=112873)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112902-8.0.35 · Bug #112902

Optimizer in MySQL 8 is significantly slower on dependent subqueries than 5.7

官方版本字段：8.0.31, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112902](https://bugs.mysql.com/bug.php?id=112902)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112907-8.0.35 · Bug #112907

Assertion `to->field_ptr() != from->field_ptr()' failed in MySQL 8.1.0

官方版本字段：8.1.0, 8.0.35, 8.2

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112907](https://bugs.mysql.com/bug.php?id=112907)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 原文8.1-debug-asan，官方补证8.0.35 debug，目标field_conv_with_cache断言；现有release容器不满足所述构建，不安装debug/Sanitizer。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112910-8.0.35 · Bug #112910

Incorrect results when add an uncorrelated row

官方版本字段：8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112910](https://bugs.mysql.com/bug.php?id=112910)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：获明确批准后仅重试一次：8.0.34 单行 VALUES 查询为空，但两行 VALUES 过滤错误返回(a,0)；直接 CAST 控制为0.0625，div_precision=4。与8.0.35完整逐语句输出相同，关键环境一致，前版已有相同异常。原启动超时记录单独保留。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112910-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112910-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112910-8.0.35.sql)

### mysql-112911-8.0.35 · Bug #112911

Inconsistent results when using PRIMARY and DUPSWEEDOUT

官方版本字段：8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #112911](https://bugs.mysql.com/bug.php?id=112911)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："无提示为 4，有提示为 8。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112911-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-112911-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-112911-8.0.35.sql)

### mysql-112915-8.0.35 · Bug #112915

CTE double materialization issue

官方版本字段：8.1.0, 8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #112915](https://bugs.mysql.com/bug.php?id=112915)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer explicitly identifies1137 from repeated TEMPORARY table access as documented limitation; requested CTE materialization enhancement is not evidence of wrong result.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112935-8.0.35 · Bug #112935

Different Behaviour Seen Between MyISAM and MEMORY Engine

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112935](https://bugs.mysql.com/bug.php?id=112935)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112946-8.0.35 · Bug #112946

INSTANT algo <= 8028 on table in mysql schema leads to corruption post upgrade

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #112946](https://bugs.mysql.com/bug.php?id=112946)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires datadir created with pre8.0.29 INSTANT columns in mysql schema then upgraded; current target fresh tables lack historical physical state. Need isolated8.0.28 preparation environment and upgrade protocol; no previous-version comparison run in current scope.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112951-8.0.35 · Bug #112951

Assertion `fixed' failed in MySQL 8.1.0

官方版本字段：8.1.0, 8.0.35, 8.2.0

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112951](https://bugs.mysql.com/bug.php?id=112951)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain及c537633明确debug的Item_sum::aggregate_check_group fixed断言，release不受影响；当前缺debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112964-8.0.35 · Bug #112964

SELECT COUNT is slow with O_DIRECT

官方版本字段：8.0, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #112964](https://bugs.mysql.com/bug.php?id=112964)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112979-8.0.35 · Bug #112979

binlog_transaction_compression_level_zstd bug not fixed in 8.0.35

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_environment_and_materials_gap

官方报告：[Bug #112979](https://bugs.mysql.com/bug.php?id=112979)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需要binlog压缩启用及可重复同一工作负载比较zstd3/22；正文无数据生成/事务边界/基线清零，压缩率近似不足作判据，原关联报告109199不可访问。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112982-8.0.35 · Bug #112982

Assertion Failure in /mysql-8.0.34/sql/sql_derived.cc:558

官方版本字段：8.0.34, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #112982](https://bugs.mysql.com/bug.php?id=112982)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-112983-8.0.35 · Bug #112983

Assertion Failure in /mysql-8.0.34/sql/sql_base.cc:7731

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #112983](https://bugs.mysql.com/bug.php?id=112983)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c537781/c537782 区分 release 与 debug；同名 CTE 的 sql_base 断言需要 debug，普通 release 无断言不构成否证。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113002-8.0.35 · Bug #113002

innodb.ddl_kill test fails sporadically.

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113002](https://bugs.mysql.com/bug.php?id=113002)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Original innodb.ddl_kill MTR test requires matching debug test tree, debug-sync semantics and up to100 repetitions; single SQL session lacks harness scheduling/expected1317 handling.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113015-8.0.35 · Bug #113015

REGEXP curly brackets without escape character works on 5.7 but not in 8.0

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113015](https://bugs.mysql.com/bug.php?id=113015)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113036-8.0.35 · Bug #113036

Assertion Failure in /mysql-8.0.34/sql/field.cc:4318

官方版本字段：8.0.34, 8.0.35, 8.1.0, 8.2.0

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #113036](https://bugs.mysql.com/bug.php?id=113036)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- c537920确认8.0.35 debug Field_double::val_real断言；无ORDER BY的LIMIT结果本身不能代替崩溃oracle。缺debug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113037-8.0.35 · Bug #113037

Assertion Failure in /mysql-8.0.34/sql/my_decimal.h:186

官方版本字段：8.0.34, 8.0.35, 8.1.0, 8.2.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113037](https://bugs.mysql.com/bug.php?id=113037)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official assertion reproduction confirms8.0.35 debug build; release query result or normal errors do not establish decimal assertion. Requires target debug build with original SQL and startup verification.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113046-8.0.35 · Bug #113046

MTR tests for SELECT fail with ICP, MRR, possibly other flags

官方版本字段：8.0.35, 8.2.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113046](https://bugs.mysql.com/bug.php?id=113046)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113047-8.0.35 · Bug #113047

MTR test main.derived_limit fails with small cost differences

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113047](https://bugs.mysql.com/bug.php?id=113047)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- MTR derived_limit expected-output floating-cost discrepancy depends on Xcode15.0.1 build and matching test result; official change test-only. No wrong-result runtime oracle; requires original toolchain/test harness.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113048-8.0.35 · Bug #113048

MTR test gis.gis_bugs_crashes fails with a result difference

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113048](https://bugs.mysql.com/bug.php?id=113048)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113049-8.0.35 · Bug #113049

MTR test json.array_index fails with a result difference

官方版本字段：8.0.35, 8.2.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113049](https://bugs.mysql.com/bug.php?id=113049)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Real wrong-result issue depends on Clang15/16/17 or Xcode15 std::sort implementation; official binaries may pass. Requires matching compiler-built target and original json.array_index MTR inputs; ASAN is not inherently required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113051-8.0.35 · Bug #113051

Skip instant DDL for empty tables to save row versions

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113051](https://bugs.mysql.com/bug.php?id=113051)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113056-8.0.35 · Bug #113056

crashing when giving pwd/not able install again so cannot configure pwd

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113056](https://bugs.mysql.com/bug.php?id=113056)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113097-8.0.35 · Bug #113097

query bug racecondition

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113097](https://bugs.mysql.com/bug.php?id=113097)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："原始查询为空，关闭 derived_condition_pushdown 后返回该行。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113097-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113097-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113097-8.0.35.sql)

### mysql-113112-8.0.35 · Bug #113112

External dependency ext::zlib leads to -lzlib, but shall lead to -lz

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113112](https://bugs.mysql.com/bug.php?id=113112)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Build metadata error from WITH_ZLIB=SYSTEM links -lzlib rather than -lz; requires CMake/build toolchain and generated mysqlclient.pc/mysql_config, not runtimeSQL.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113154-8.0.35 · Bug #113154

Join using ROW_NUMBER() returns incorrect records

官方版本字段：8.2.0, 8.1.0, 8.0.35

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #113154](https://bugs.mysql.com/bug.php?id=113154)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113154-8.0.35.sql)

### mysql-113167-8.0.35 · Bug #113167

After creating the spatial index, ST_Disjoint gives the incorrect answer

官方版本字段：8.2.0, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113167](https://bugs.mysql.com/bug.php?id=113167)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113171-8.0.35 · Bug #113171

sum(distinct substring()) does not give warnings, while sum(substring() does

官方版本字段：8.0.35-0ubuntu0.22.04.1

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113171](https://bugs.mysql.com/bug.php?id=113171)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："普通 SUM 返回 0 且有转换 warning，SUM DISTINCT 返回 0 却不报告 warning。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113171-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113171-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113171-8.0.35.sql)

### mysql-113173-8.0.35 · Bug #113173

Crash when using --batch in MySQL command client

官方版本字段：8.2.0, 8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113173](https://bugs.mysql.com/bug.php?id=113173)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113176-8.0.35 · Bug #113176

Unexpected errors caused by check constraints

官方版本字段：8.1.0, 8.0.35

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #113176](https://bugs.mysql.com/bug.php?id=113176)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113176-8.0.35.sql)

### mysql-113178-8.0.35 · Bug #113178

Temptable engine leads to performance degradation

官方版本字段：8.0, 8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113178](https://bugs.mysql.com/bug.php?id=113178)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Full performance reproducer generates large RAND-based tables, needs tmp_table_size1GiB and baseline query324s versus MEMORY68s. Requires approved memory/disk/time budget and repeatable workload snapshot; small-case timeout cannot establish performance regression.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113180-8.0.35 · Bug #113180

Unexpected Results when Using Math Function SIN

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113180](https://bugs.mysql.com/bug.php?id=113180)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象：[[["1", "0"]], [["1", "0"]]]

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113180-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113180-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113180-8.0.35.sql)

### mysql-113185-8.0.35 · Bug #113185

Unexpected Results when using NULLIF Function in Filter

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113185](https://bugs.mysql.com/bug.php?id=113185)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 现有静态SQL与oracle齐备；该官方目标版本的适用性和实际环境仍待预检，尚未排期。
- 追加原文审查：Saved Not a Bug status and later reporter clarification; postpone this debate despite clear NULLIF logic.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113202-8.0.35 · Bug #113202

p_s.processlist table does not contain async replica threads after restart

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #113202](https://bugs.mysql.com/bug.php?id=113202)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需两个异步复制节点及从库重启，比较I_S/P_S线程并STOP/START REPLICA控制；单实例没有该线程生命周期。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113205-8.0.35 · Bug #113205

After swapping the X and Y coordinates, ST_Crosses gives the incorrect answer.

官方版本字段：8.2.0, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113205](https://bugs.mysql.com/bug.php?id=113205)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113206-8.0.35 · Bug #113206

BIT_OR returns erroneous values

官方版本字段：8.0.27, 8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113206](https://bugs.mysql.com/bug.php?id=113206)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Numeric BIT_OR converts to unsigned 64-bit; -1 maps to all ones. Developer c538355 explicitly normal behavior.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113207-8.0.35 · Bug #113207

Potential bug in ST_Contains

官方版本字段：8.2.0, 8.0.35, 8.1.0

状态：其他异常；阶段：baseline_preserved

官方报告：[Bug #113207](https://bugs.mysql.com/bug.php?id=113207)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113207-8.0.35.sql)

### mysql-113208-8.0.35 · Bug #113208

IMPORT TABLESPACE not friendly with multi-byte characters

官方版本字段：ALL, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113208](https://bugs.mysql.com/bug.php?id=113208)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113211-8.0.35 · Bug #113211

The latest version 8.0 returns abnormal results for complex queries

官方版本字段：8.0.35, 8.1.0, 8.2.0

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #113211](https://bugs.mysql.com/bug.php?id=113211)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113211-8.0.35.sql)

### mysql-113236-8.0.35 · Bug #113236

conflicting replica_parallel_workers spec causes parallel_mode misconfig

官方版本字段：8.0.35-0ubuntu0.22.04.1

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113236](https://bugs.mysql.com/bug.php?id=113236)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Step4 explicitly lacks how to generate anonymous-GTID event with out-of-order sequence_number. Also needs8.0.26source/8.0.35replica configuration; missing triggering binlog prevents deterministic replay.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113248-8.0.35 · Bug #113248

Execute alter table heap-use-after-free

官方版本字段：8.2.0, 8.0.35

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #113248](https://bugs.mysql.com/bug.php?id=113248)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- cmain 明确 WITH_DEBUG/ASan/UBSan、Boost 1.77；重复 EXECUTE ALTER 的 heap-use-after-free 需对应 sanitizer 日志，缺构建。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113270-8.0.35 · Bug #113270

Unable to compile 8.0.35 with DISABLE_PSI_THREAD

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113270](https://bugs.mysql.com/bug.php?id=113270)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113293-8.0.35 · Bug #113293

Create table like assertion error

官方版本字段：8.2.0, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113293](https://bugs.mysql.com/bug.php?id=113293)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原工具中断未生成SQL状态；原文还要求debug/ASAN/UBSAN与标识符编码，不重试转写或替换字符。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113293\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113298-8.0.35 · Bug #113298

Unexpected Results when Using IN for Floating-Point

官方版本字段：8.0.33, 8.1.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113298](https://bugs.mysql.com/bug.php?id=113298)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："有索引时正反谓词均返回1，删索引控制恢复互补"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113298-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113298-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113298-8.0.35.sql)

### mysql-113301-8.0.35 · Bug #113301

using preparation statement to query the time type data, some data is not found

官方版本字段：8.0.35, 8.0.31

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113301](https://bugs.mysql.com/bug.php?id=113301)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："带参数的 TIME(0) 查询没有记录；TIME(6) 混合参数与字面值查询漏掉字面值对应行，而字面量控制完整。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113301-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113301-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113301-8.0.35.sql)

### mysql-113302-8.0.35 · Bug #113302

Unexpected Result for an Index

官方版本字段：8.2.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113302](https://bugs.mysql.com/bug.php?id=113302)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："添加索引后错返(1,0)"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113302-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113302-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113302-8.0.35.sql)

### mysql-113303-8.0.35 · Bug #113303

Explain plan takes forever when there are more joins

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113303](https://bugs.mysql.com/bug.php?id=113303)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113304-8.0.35 · Bug #113304

Unexpected Result for LEAST function

官方版本字段：8.2.0, 8.0.35

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #113304](https://bugs.mysql.com/bug.php?id=113304)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-113304-8.0.35.sql)

### mysql-113312-8.0.35 · Bug #113312

Server stall during Alter/Drop table while clearing AHIs from the buffer pool

官方版本字段：8.0.35, 8.1.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113312](https://bugs.mysql.com/bug.php?id=113312)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires HammerDB4.4,3500warehouses,256concurrentworkers,128GiBRAM,92GiBbuffer pool and64GiBlog with prolongedload. Far beyond small-case bounds; preserve original scale until explicit resource approval.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113316-8.0.35 · Bug #113316

When the bit type has an index, the query result is incorrect.

官方版本字段：8.0.35, 8.1.0, 8.2.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113316](https://bugs.mysql.com/bug.php?id=113316)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："有索引空集，删索引后返回bit00/int1并有转换警告"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113316-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113316-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113316-8.0.35.sql)

### mysql-113317-8.0.35 · Bug #113317

Unexpected Result by IF

官方版本字段：8.0.35, 8.1.0, 8.2.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113317](https://bugs.mysql.com/bug.php?id=113317)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113318-8.0.35 · Bug #113318

unnest scalar subquery using groupby produces wrong result

官方版本字段：mysql-8.0.33, 8.0.35, 8.1.0, 8.2.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113318](https://bugs.mysql.com/bug.php?id=113318)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无最终SQL；原文ANALYZE包含未定义t2需后续明确，不补造对象，不重试生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113318\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113319-8.0.35 · Bug #113319

unnesting scalar subquery containing count and having cond produces wrong result

官方版本字段：mysql-8.0.33, 8.0.35, 8.1.0, 8.2.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113319](https://bugs.mysql.com/bug.php?id=113319)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："off正确，on错误为[1,1,0,0]"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113319-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113319-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113319-8.0.35.sql)

### mysql-113338-8.0.35 · Bug #113338

return error result with a qubquery

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：reviewed_materials_gap

官方报告：[Bug #113338](https://bugs.mysql.com/bug.php?id=113338)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- cmain要求附件建表/数据，c538679更正表名tt0/tt1；正文无DDL/DML，需对应附件及订正查询，不得拼造数据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113347-8.0.35 · Bug #113347

The merge threshold for index pages is case-sensitive

官方版本字段：all version, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113347](https://bugs.mysql.com/bug.php?id=113347)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113352-8.0.35 · Bug #113352

User cancel operation times out when stored procedure has multiple SLEEP() calls

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113352](https://bugs.mysql.com/bug.php?id=113352)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Cancel timeout is a client operation during multiple SLEEP calls; maintainer disputes bug and no exact client cancel protocol is specified. Need agreed cancellation contract and client timing instead of treating expected interruption/timeout as Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113358-8.0.35 · Bug #113358

Wrong functional dependency in ONLY_FULL_GROUP_BY mode

官方版本字段：8.0, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113358](https://bugs.mysql.com/bug.php?id=113358)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：两侧无 GROUP BY 控制均为(1,2)、(1,1)；subquery_to_derived=off 的 GROUP BY 在第15行正常报1055，on 却错误接受并返回(1,2)。输入表及 ONLY_FULL_GROUP_BY/on 状态校验一致。目标现象是 on 的错误接受，而非 off 的正常1055；8.0.34 已有相同异常。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113358-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113358-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113358-8.0.35.sql)

### mysql-113366-8.0.35 · Bug #113366

Incorrect query results involving the date type.

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113366](https://bugs.mysql.com/bug.php?id=113366)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL且DATE/未定型字符串/数值语义须谨慎；保留缺口队列，不推定两个表达式类型等价。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113366\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113369-8.0.35 · Bug #113369

In the hash partition table, the query result is error.

官方版本字段：8.0.34, 8.0.35

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113369](https://bugs.mysql.com/bug.php?id=113369)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- YEAR/INT隐式比较与常量折叠后类型转换的规范性边界。
- {"point": "YEAR/INT隐式比较与常量折叠后类型转换的规范性边界。", "evidence": "c539471解释CAST(61 AS YEAR)=2061，同时记录删除id=61反而有行，尚未给最终契约。", "needed": "目标8.0比较转换规则和计划/表达式类型证据；后续用原式与控制分别保存输出。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113387-8.0.35 · Bug #113387

update with 'and' 'or' causes unexpected behavior

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #113387](https://bugs.mysql.com/bug.php?id=113387)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c538848明确SET右侧AND/OR合法布尔表达式；用AND替代逗号是用户语义错误，不能把正常更新结果当Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113405-8.0.35 · Bug #113405

'covering index' is not shown entirely in EXPLAIN FORMAT=TREE.

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113405](https://bugs.mysql.com/bug.php?id=113405)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113415-8.0.35 · Bug #113415

Unknown column, but can get query result in CTE.

官方版本字段：8.0, 8.0.35

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #113415](https://bugs.mysql.com/bug.php?id=113415)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 未知t.id位于未引用CTE，需核验MySQL未引用CTE的解析/名字解析契约；仅收到报告不足证明必须报1054，暂不定错。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113423-8.0.35 · Bug #113423

Unexpected result appeared

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113423](https://bugs.mysql.com/bug.php?id=113423)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- DISTINCT alters materialization/type conversion and cardinality; temporal bitwise conversion contract not established, official c538980 disputes bug. Need typed oracle rather than asserting entire queries equivalent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113424-8.0.35 · Bug #113424

Unexpected result appeared

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113424](https://bugs.mysql.com/bug.php?id=113424)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113425-8.0.35 · Bug #113425

Unexpected result appeared

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113425](https://bugs.mysql.com/bug.php?id=113425)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Temporal bitwise operator/HAVING alias evaluation has disputed expected type conversion; official c538982 rejects alleged mismatch. Need resolve oracle before attributing observed 94/86 to Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113433-8.0.35 · Bug #113433

Incorrect query results involving the date type.

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113433](https://bugs.mysql.com/bug.php?id=113433)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："第一查询返回1913/61，追加相同id约束及字面量61比较均为空"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113433-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113433-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113433-8.0.35.sql)

### mysql-113439-8.0.35 · Bug #113439

Alter database charset lead to cpu high load

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113439](https://bugs.mysql.com/bug.php?id=113439)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 20,000-table ALTER DATABASE performance experiment requires 2 GiB buffer pool plus overhead, high open-file/table-cache limits, repeated timings and profiling. Current 2 GiB container/20-second SQL budget cannot match this. CPU use alone is not correctness oracle; hardware and improvement baseline remain unanswered in c539106.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113440-8.0.35 · Bug #113440

Table spaces with instant_col information can no longer be imported

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113440](https://bugs.mysql.com/bug.php?id=113440)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113474-8.0.35 · Bug #113474

mysql 8.0.35 suddenly has become extremely slow

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113474](https://bugs.mysql.com/bug.php?id=113474)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113482-8.0.35 · Bug #113482

innodb_parallel_read_threads>1 makes simple select count more expensive

官方版本字段：8.0.35, 8.2.0

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113482](https://bugs.mysql.com/bug.php?id=113482)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Performance issue requires sysbench 1.0.20 data generation (10M rows, ~2 GiB file), cold buffer pool and repeated parallel_read_threads timings/IO measurements. Dataset plus InnoDB files exceeds current 2 GiB per-case budget, and 2 CPU cap cannot reproduce 8-thread hardware conditions; no wall-time oracle frozen.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113485-8.0.35 · Bug #113485

Let innodb_dedicated_server set innodb_log_writer_threads based on server size

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113485](https://bugs.mysql.com/bug.php?id=113485)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113505-8.0.35 · Bug #113505

Performance schema counter increments make parallel index create slow

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113505](https://bugs.mysql.com/bug.php?id=113505)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113506-8.0.35 · Bug #113506

Item_func_conv_charset::eq not correct

官方版本字段：8.0,8.0.35, 8.1.0, 8.2.0

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113506](https://bugs.mysql.com/bug.php?id=113506)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："带 latin1 投影顺序为 你好、中午好；不带投影为 中午好、你好。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113506-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113506-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113506-8.0.35.sql)

### mysql-113507-8.0.35 · Bug #113507

gipk add column failed

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113507](https://bugs.mysql.com/bug.php?id=113507)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无最终SQL；GIPK会话设置与原1235错误属于待交付转写，不重新生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113507\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113514-8.0.35 · Bug #113514

JSON_OBJECT changes order of keys in output

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #113514](https://bugs.mysql.com/bug.php?id=113514)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- JSON对象key无顺序语义，c539317明确预期行为并关联100974；不能把key顺序变化计Bug。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113516-8.0.35 · Bug #113516

rejoin cluster failure as clone plugin is waiting for table metadata lock

官方版本字段：8.0.32, 8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113516](https://bugs.mysql.com/bug.php?id=113516)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires gr_xa_clone_rejoin_failure.test attachment, MTR and Group Replication/clone multi-node topology plus detached XA locking schedule. Single isolated MySQL instance cannot satisfy it.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113518-8.0.35 · Bug #113518

character set with Chinese character,using storage procedure it report 1300 err

官方版本字段：8.0.32, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113518](https://bugs.mysql.com/bug.php?id=113518)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113524-8.0.35 · Bug #113524

Value in ibuf bitmap page of R-Tree could be incorrect after recovery

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113524](https://bugs.mysql.com/bug.php?id=113524)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Only code reasoning supplied; reporter says hard to repeat without instrumentation. c539529 explicitly requests testcase satisfying branch conditions. Missing SQL/data, deterministic crash schedule and page-level oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113527-8.0.35 · Bug #113527

Hash Sum mismatch

官方版本字段：8.0.35-1debian12

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113527](https://bugs.mysql.com/bug.php?id=113527)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113528-8.0.35 · Bug #113528

Error installing the server

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113528](https://bugs.mysql.com/bug.php?id=113528)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Windows 11 MSI installer/service initialization problem, not SQL server replay. Need exact installer, my.ini, pre-existing data/service state and Windows logs; Linux container cannot meet platform conditions.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113531-8.0.35 · Bug #113531

the convert function seems not work as expected

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113531](https://bugs.mysql.com/bug.php?id=113531)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113532-8.0.35 · Bug #113532

Compatibility issue with mysql history ("\040" instead of space)

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113532](https://bugs.mysql.com/bug.php?id=113532)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113534-8.0.35 · Bug #113534

table join return Unexpected result when drived table using include join index

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113534](https://bugs.mysql.com/bug.php?id=113534)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："JOIN_PREFIX(ord,bat)只返回ord.id1，无提示返回id1、2；须记录真实计划"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113534-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113534-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113534-8.0.35.sql)

### mysql-113535-8.0.35 · Bug #113535

Drop table in background list will remain file exists in directory

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #113535](https://bugs.mysql.com/bug.php?id=113535)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source-code hypothesis about background DROP/file retention has no reproducible thread schedule. Official concurrent DROP attempts were normal. Need schema/data and deterministic schedule that queues background drop plus filesystem oracle.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113536-8.0.35 · Bug #113536

A character set error is reported when a stored procedure is used.

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113536](https://bugs.mysql.com/bug.php?id=113536)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113557-8.0.35 · Bug #113557

Wrong query result on composite multi-valued index + empty array value

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113557](https://bugs.mysql.com/bug.php?id=113557)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："USE索引为空而IGNORE返回a1"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113557-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113557-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113557-8.0.35.sql)

### mysql-113562-8.0.35 · Bug #113562

COLLATION behaves differently if set on CREATE TABLE vs ALTER TABLE

官方版本字段：8.2.0, 8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #113562](https://bugs.mysql.com/bug.php?id=113562)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- ALTER TABLE default collation does not change existing column collation; c539540 explains and reporter acknowledges. Two tables have different column collations, so sort difference is normal.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113578-8.0.35 · Bug #113578

AVG calculation bug

官方版本字段：5.7.44, 8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113578](https://bugs.mysql.com/bug.php?id=113578)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113595-8.0.35 · Bug #113595

Incorrect query result of function TIMESTAMPADD

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113595](https://bugs.mysql.com/bug.php?id=113595)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无最终SQL；原文DROP DATABASE原目录操作未直接移植，后续需专属schema范围；不重试生成。c539572标Duplicate须保留。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113595\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113597-8.0.35 · Bug #113597

Data Dictionary issues when dropping multiple FTS indexes

官方版本字段：8.0.35

状态：证据不足；阶段：environment_task_interrupted

官方报告：[Bug #113597](https://bugs.mysql.com/bug.php?id=113597)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Environment review task interrupted by content restriction; report-specific cause unknown. Existing requirements retained; saved reassessment is provisional and no database run was attempted.
- 完整oracle要求读取隔离数据目录FTS文件与information_schema.FILES交叉核对；当前SQL仅字典部分，缺专用文件审查/目录定位及权限预检。不执行部分后冒充完整复现。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113598-8.0.35 · Bug #113598

Please consider adding GTID in "Timeout waiting for reply".

官方版本字段：8.2.0, 8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113598](https://bugs.mysql.com/bug.php?id=113598)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113639-8.0.35 · Bug #113639

Crash when executes test case main.default_as_expr in debug with ps-protocol

官方版本字段：8.0.35

状态：证据不足；阶段：held_original_queue

官方报告：[Bug #113639](https://bugs.mysql.com/bug.php?id=113639)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 缺少被调用的main.default_as_expr实际测试文件及include链。
- {"point": "缺少被调用的main.default_as_expr实际测试文件及include链。", "evidence": "cmain只有MTR命令和异常栈；已检查的本地资料没有该文件。", "needed": "各目标版本带SHA的测试文件和依赖，确认准确触发步骤后才能转写SQL与清理。"}
- SQL、oracle、语义或依赖条件仍有缺口，尚不能判断报告现象。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113647-8.0.35 · Bug #113647

identical tables are checked in HashJoin because of no STOP_AT_MATERIALIZATION

官方版本字段：8.0.35,8.2.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113647](https://bugs.mysql.com/bug.php?id=113647)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113649-8.0.35 · Bug #113649

the result of format function truncated when using cursor

官方版本字段：8.0.31, 8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113649](https://bugs.mysql.com/bug.php?id=113649)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："游标字符串截成约 60 字节，直接 FORMAT 结果长数百字节，same_bytes=0。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113649-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113649-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113649-8.0.35.sql)

### mysql-113706-8.0.35 · Bug #113706

InnoDB : Corruption of an index tree which stopped mysqld service

官方版本字段：mysql Ver 8.0.35 for Linux on 86_64

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113706](https://bugs.mysql.com/bug.php?id=113706)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113718-8.0.35 · Bug #113718

left join + semijoin + materialization finds false matches

官方版本字段：8.0.35, 8.0.36, 8.3.0

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #113718](https://bugs.mysql.com/bug.php?id=113718)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL/检测器；后续需核对semi-join materialization提示实际生效；不重试生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\113718\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113730-8.0.35 · Bug #113730

Unable to connect to MySQL 5.1 database server with MySQL 8 client

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113730](https://bugs.mysql.com/bug.php?id=113730)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113768-8.0.35 · Bug #113768

return error with cast

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #113768](https://bugs.mysql.com/bug.php?id=113768)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：两侧指定元组 NOT IN 查询在第8行报1690/22003，消息均指向 cast(BIGINT最大值 as double)；直接 CAST 控制却成功返回有限 DOUBLE，加载数据为两个 BIGINT 边界值、sql_mode 不含 REAL_AS_FLOAT。8.0.34 已有同样错误转换现象，普通数据加载或模式错误已排除。

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113768-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-113768-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-113768-8.0.35.sql)

### mysql-113831-8.0.35 · Bug #113831

mysql crashes ramdonally during backup

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #113831](https://bugs.mysql.com/bug.php?id=113831)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113839-8.0.35 · Bug #113839

Cannot elect a new PRIMARY when async connection failover is in use

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #113839](https://bugs.mysql.com/bug.php?id=113839)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 需两个GR集群和受管异步failover通道，切换DR主节点UDF时3910；当前单实例无拓扑与通道，须专用多节点方案。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113879-8.0.35 · Bug #113879

An error is reported when the user variable character set is used in the stored

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #113879](https://bugs.mysql.com/bug.php?id=113879)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-113978-8.0.35 · Bug #113978

Set admin_port in port being used does not throw error

官方版本字段：8.0.35, 8.0.36

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #113978](https://bugs.mysql.com/bug.php?id=113978)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- admin_port conflict is a startup/socket-binding diagnostic issue. Requires controlled occupied port inside dedicated namespace, admin_address/startup configuration and startup-log oracle. Ordinary no-network SQL runner cannot exercise it; original admin_address is also absent.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114021-8.0.35 · Bug #114021

mysqldump --replace produces *some* REPLACE IGNORE statements

官方版本字段：8.0.35 (at least), 8.0.36

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #114021](https://bugs.mysql.com/bug.php?id=114021)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114058-8.0.35 · Bug #114058

The return value of the CAST(... AS UNSIGNED) expression is out of range.

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #114058](https://bugs.mysql.com/bug.php?id=114058)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- CAST AS UNSIGNED is unsigned integer conversion, not TINYINT UNSIGNED merely because source is TINYINT. 2^64-30 is expected; official rejects.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114072-8.0.35 · Bug #114072

Group replication slow down existing asynchronous replication

官方版本字段：8.0.35-27

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114072](https://bugs.mysql.com/bug.php?id=114072)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114125-8.0.35 · Bug #114125

Parameter set by SET PERSIST is not set to replication threads when restart

官方版本字段：8.0.35,8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114125](https://bugs.mysql.com/bug.php?id=114125)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114196-8.0.35 · Bug #114196

Incorrect query result caused by comparing decimal and float type value

官方版本字段：8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114196](https://bugs.mysql.com/bug.php?id=114196)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："WHERE错误返回0行值"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114196-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114196-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114196-8.0.35.sql)

### mysql-114198-8.0.35 · Bug #114198

Using PERSIST on binlog_transaction_compression partially compresses binary log

官方版本字段：8.0.35, 8.0.36

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #114198](https://bugs.mysql.com/bug.php?id=114198)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires two-node GTID asynchronous replication, SET PERSIST and restart, source transactions and binary-log compression inspection. Existing single no-network instance with binlog disabled cannot satisfy topology/persistence conditions. Target version must be selected from frozen item, not example8.0.36.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114255-8.0.35 · Bug #114255

Install Community Edition 8.0.34/35glibc2.28-arm Version error

官方版本字段：8.0.34/35

状态：证据不足；阶段：reviewed_environment_gap

官方报告：[Bug #114255](https://bugs.mysql.com/bug.php?id=114255)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 故障是aarch64 64KiB页系统加载glibc2.28包中OpenSSL ELF；需原8.0.34/35 ARM包与64KiB页Linux，x86容器或重编译替换库不等价。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114319-8.0.35 · Bug #114319

[FEATURE] Support 4k ReplicationPassword

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #114319](https://bugs.mysql.com/bug.php?id=114319)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114342-8.0.35 · Bug #114342

Failed to convert the character string when executing the selection statement.

官方版本字段：8.0.35, 8.0.36

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #114342](https://bugs.mysql.com/bug.php?id=114342)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c542310明确二进制F1F2不是有效utf8，LIKE转换3854属于正常错误；不能将无错误作为唯一正确oracle。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114378-8.0.35 · Bug #114378

Incorrect query result caused by CONVERT_TZ

官方版本字段：8.0, 8.0.35

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #114378](https://bugs.mysql.com/bug.php?id=114378)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-114378-8.0.35.sql)

### mysql-114379-8.0.35 · Bug #114379

Incorrect query result caused by index and optimizer

官方版本字段：8.0.27, 8.0.35, 8.0.21

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114379](https://bugs.mysql.com/bug.php?id=114379)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114380-8.0.35 · Bug #114380

Incorrect query result may caused by TIMESTAMP

官方版本字段：8.0.13, 8.0.35, 8.0.36

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114380](https://bugs.mysql.com/bug.php?id=114380)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："第一返回-2，第二为空；不能将转换warning直接判执行失败"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114380-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114380-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114380-8.0.35.sql)

### mysql-114381-8.0.35 · Bug #114381

Incorrect query result may caused by EXISTS and TIMEDIFF

官方版本字段：8.0.19,8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114381](https://bugs.mysql.com/bug.php?id=114381)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："直接 WHERE 返回 c0=1，IS TRUE 变体为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114381-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114381-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114381-8.0.35.sql)

### mysql-114382-8.0.35 · Bug #114382

Incorrect query result may caused by LOW_PRIORITY

官方版本字段：8.0.11, 8.0.35, 8.0.36

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #114382](https://bugs.mysql.com/bug.php?id=114382)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-114382-8.0.35.sql)

### mysql-114383-8.0.35 · Bug #114383

Incorrect query result may caused by DATE and window function

官方版本字段：8.0.23,8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #114383](https://bugs.mysql.com/bug.php?id=114383)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114384-8.0.35 · Bug #114384

Incorrect query result may caused by LOG

官方版本字段：8.0.15,8.0.35, 8.0.36

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114384](https://bugs.mysql.com/bug.php?id=114384)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："直接 WHERE 返回 0，IS TRUE 变体为空。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114384-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114384-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114384-8.0.35.sql)

### mysql-114396-8.0.35 · Bug #114396

NULL is not treated as 0 for tables partitioned by key

官方版本字段：8.0.22, 8.0.35, 8.0.36

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #114396](https://bugs.mysql.com/bug.php?id=114396)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Source demonstrates KEY partition NULL/zero difference from quoted manual, but need distinguish documentation error from implementation defect and freeze expected KEY hashing contract. Do not equate observed partition separation with independent database Bug.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114475-8.0.35 · Bug #114475

COUNT(1) vs SUM of partial counts

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_special_environment

官方报告：[Bug #114475](https://bugs.mysql.com/bug.php?id=114475)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Windows-specific performance test requires 3M+ rows/10GB, long timings exceeding current limits; later comments disagree fixed version. Needs resource/platform protocol, not Linux small-data substitute.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114525-8.0.35 · Bug #114525

log_first_rec_group failed

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114525](https://bugs.mysql.com/bug.php?id=114525)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114545-8.0.35 · Bug #114545

performance_schema.processlist tuncates query info

官方版本字段：8.0.35, 8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114545](https://bugs.mysql.com/bug.php?id=114545)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114550-8.0.35 · Bug #114550

ROUND(1.2345, 2) and ROUND(1.2345, @TWO) unexpected different results

官方版本字段：8.0.35, 8.0.36

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114550](https://bugs.mysql.com/bug.php?id=114550)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114570-8.0.35 · Bug #114570

Error running mysqldump with tables with big blobs on docker

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #114570](https://bugs.mysql.com/bug.php?id=114570)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114580-8.0.35 · Bug #114580

Mysql 8.0.35 - The query to get foreign keys are slower than MySQL 8.0.20

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #114580](https://bugs.mysql.com/bug.php?id=114580)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114775-8.0.35 · Bug #114775

Outer join condition filtering bug when using scalar subquery

官方版本字段：8.0.35, 8.0.36

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114775](https://bugs.mysql.com/bug.php?id=114775)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："外连接失配行仍被当作常量 c，错误返回 a/b 等结果。"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114775-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114775-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114775-8.0.35.sql)

### mysql-114783-8.0.35 · Bug #114783

Backward scan partition table with multi-valued Indexes may lost some result.

官方版本字段：mysql-8.0.35, 8.0.36

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #114783](https://bugs.mysql.com/bug.php?id=114783)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 原工具中断无SQL；保留反向索引扫描提示与index_condition_pushdown配置缺口，不重试生成。
- 预审声明的文件不存在：cleanup_path = <USER_HOME>\Documents\Codex\2026-10-26\mysql-bug-collect-py-c-users\outputs\普通SQL静态准备_20261029\cases\114783\cleanup.sql

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-114917-8.0.35 · Bug #114917

Incorrect query result

官方版本字段：8.0.35, 8.0.37, 8.4

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #114917](https://bugs.mysql.com/bug.php?id=114917)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："错误多出10:59:59、12:00:00、20:59:59、23:23:59共13组"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114917-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-114917-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-114917-8.0.35.sql)

### mysql-115220-8.0.35 · Bug #115220

some assert should not been trigger when innodb_force_recovery is set

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #115220](https://bugs.mysql.com/bug.php?id=115220)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115294-8.0.35 · Bug #115294

partition table's io wait summary not correct in PERFORMANCE_SCHEMA

官方版本字段：5.7+,8.0.35

状态：报告现象已复现；阶段：baseline_preserved

官方报告：[Bug #115294](https://bugs.mysql.com/bug.php?id=115294)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

相邻比较：8.0.34 → 8.0.35，前版同异常。

保存的比较依据：前版完整逐语句结果、警告及数据控制与已核验目标版一致；仅替换自动生成的隔离库标识用于比较，未删除计划、数值或诊断差异。源 SQL/postcheck、release 构建、架构、关键环境及 optimizer_switch 相同。冻结报告现象："等值/全扫计数增长，PRIMARY range及IN真实返回3/2行但P_S读取计数增量为0"

边界审查：[experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-115294-8.0.35/review.json](../../experiments/saved_20261029/version_boundary_20261029/v34_35/cases/mysql-115294-8.0.35/review.json)；历史基线：[experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json](../../experiments/saved_20261029/version_boundary_20261029/local_status_20261029/stage_status.json)

SQL：[查看已执行 SQL](sql/executed_125/mysql-115294-8.0.35.sql)

### mysql-115354-8.0.35 · Bug #115354

MySQL installation fails due to internet connectivity

官方版本字段：5.7.42, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115354](https://bugs.mysql.com/bug.php?id=115354)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115470-8.0.35 · Bug #115470

The precision of avg () is lost when multiple tables are joined.

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #115470](https://bugs.mysql.com/bug.php?id=115470)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 使用非MySQL官方hermes引擎且字符串到double近似误差，c545934明确Not a bug；不能当AVG逻辑Bug，也不能擅自替换引擎。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115726-8.0.35 · Bug #115726

A left join with an impossible condition cause unexpected result

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_semantic_ambiguity

官方报告：[Bug #115726](https://bugs.mysql.com/bug.php?id=115726)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Developer c545924 explains zero-DATETIME ODBC IS NULL extension only for simple WHERE; extra predicate intentionally changes extension application. Also original SQL mode needed for NULL insertion.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115762-8.0.35 · Bug #115762

SIGILL in precmd routine with FreeBSD 14.1 on Raspberry Pi 3B+ with latest

官方版本字段：8.4.0, 8.1.0, 8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115762](https://bugs.mysql.com/bug.php?id=115762)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115766-8.0.35 · Bug #115766

Database page corruption on disk or a failed file read of page

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115766](https://bugs.mysql.com/bug.php?id=115766)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-115811-8.0.35 · Bug #115811

Replication Delay consistent at 1 second.

官方版本字段：8.0.35-27

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #115811](https://bugs.mysql.com/bug.php?id=115811)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116001-8.0.35 · Bug #116001

Issue: Inconsistent Timestamp Values After Import

官方版本字段：8.0.35/8.0.39

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #116001](https://bugs.mysql.com/bug.php?id=116001)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116058-8.0.35 · Bug #116058

row_examined in slowlog is not correct when using index_merge

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116058](https://bugs.mysql.com/bug.php?id=116058)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116834-8.0.35 · Bug #116834

Replication between MySQL 8.0.35 (master) and MySQL 5.7.44 (slave) fails due to an incompatibility with character sets.

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116834](https://bugs.mysql.com/bug.php?id=116834)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-116864-8.0.35 · Bug #116864

Index corruption

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #116864](https://bugs.mysql.com/bug.php?id=116864)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117273-8.0.35 · Bug #117273

some sort is not optimized away by index, if index have part of primary key

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117273](https://bugs.mysql.com/bug.php?id=117273)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117409-8.0.35 · Bug #117409

join with crosse table sort is not optimized away by index

官方版本字段：8.0.35, 8.0.41

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117409](https://bugs.mysql.com/bug.php?id=117409)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117424-8.0.35 · Bug #117424

InnoDB Cluster with group_replication_paxos_single_leader=ON unable to process write traffic

官方版本字段：8.0.35,8.4.2,8.0.40

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #117424](https://bugs.mysql.com/bug.php?id=117424)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-117598-8.0.35 · Bug #117598

Wrong sort order for queries with ORDER BY DESC when using range comparison with LIMIT

官方版本字段：8.0.35, 8.0.41, 8.4.4

状态：证据不足；阶段：reviewed_missing_materials

官方报告：[Bug #117598](https://bugs.mysql.com/bug.php?id=117598)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Requires attached employee_payment data at sufficient cardinality to select LOW LIMIT path; DDL and query supplied but cannot invent exact data. Need official attachment and plan evidence.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118177-8.0.35 · Bug #118177

Unnecessary filter operator in the execution plan

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #118177](https://bugs.mysql.com/bug.php?id=118177)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118653-8.0.35 · Bug #118653

The threads waiting for the MDL lock and the threads holding the lock are the same

官方版本字段：8.0.35, 9.3.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #118653](https://bugs.mysql.com/bug.php?id=118653)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118856-8.0.35 · Bug #118856

json_objectagg throws inappropriate "no null member names" error in unreachable case.

官方版本字段：8.0.35

状态：证据不足；阶段：reviewed_oracle_ambiguity

官方报告：[Bug #118856](https://bugs.mysql.com/bug.php?id=118856)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- c554090明确聚合参数在外层IF前求值，NULL JSON key3158属于正常错误；不能把条件分支未取当免于聚合求值证据。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-118957-8.0.35 · Bug #118957

Documentation says you can use a HEX value for ALTER user passwords, but you can't.

官方版本字段：8.0.35

状态：证据不足；阶段：official_body_access_restricted

官方报告：[Bug #118957](https://bugs.mysql.com/bug.php?id=118957)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Official report request returned HTTP 403; no complete report in searched existing local/server snapshots. Human action: provide official description, How to repeat, all comments and referenced attachments.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119436-8.0.35 · Bug #119436

User Privileges are Missed On Replica Server

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #119436](https://bugs.mysql.com/bug.php?id=119436)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119441-8.0.35 · Bug #119441

Group replication binds to ipv6 wildcard address

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #119441](https://bugs.mysql.com/bug.php?id=119441)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119796-8.0.35 · Bug #119796

Encrypted data changes when adding columns

官方版本字段：8.0.35

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #119796](https://bugs.mysql.com/bug.php?id=119796)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119859-8.0.35 · Bug #119859

Inconsistent Query Results Between Partitioned and Non-Partitioned Tables

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #119859](https://bugs.mysql.com/bug.php?id=119859)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 既有 SQL 生成分片被工具提示中断，此项无最终 SQL；只读核对现有 case/限制记录，未重试或改写生成。提示为 This content was flagged for possible cybersecurity risk；未识别报告特异触发因素，不能声称本报告本身被单独限制。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-119945-8.0.35 · Bug #119945

Inconsistent result set on repeated execution of NATURAL JOIN with expression index and KEY partitioning

官方版本字段：8.0.35

状态：执行失败；阶段：baseline_preserved

官方报告：[Bug #119945](https://bugs.mysql.com/bug.php?id=119945)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- Existing results and logs retained without replay.

SQL：[查看已执行 SQL](sql/executed_125/mysql-119945-8.0.35.sql)

### mysql-119965-8.0.35 · Bug #119965

The results of the same query statement are inconsistent when it is executed multiple times.

官方版本字段：8.0.35

状态：not_executed；阶段：held_original_queue

官方报告：[Bug #119965](https://bugs.mysql.com/bug.php?id=119965)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- 保留原分片工具中断队列：缺已完成SQL/最终oracle；限制未定位到本报告，不推定本报告触发限制，不重试生成。

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。

### mysql-120437-8.0.35 · Bug #120437

information_schema.partitions returns UINT64_MAX (18446744073709551615) for DATA_LENGTH of partition dropped during conc

官方版本字段：8.0.35, 8.4.8, 9.3.0, 9.7.0

状态：证据不足；阶段：review_not_completed_task_interrupted

官方报告：[Bug #120437](https://bugs.mysql.com/bug.php?id=120437)

当前结果依据：[experiments/saved_20261029/final_targeted_20261029/current_results.json](../../experiments/saved_20261029/final_targeted_20261029/current_results.json)

保存的结论或待处理原因：

- The assigned review task was interrupted before a complete saved per-report review. No fabricated material or environment gap; human source review remains required.

本项未执行；SQL 准备程度、缺正文、环境要求和未知状态以原始记录为准，本次不补造 SQL。
