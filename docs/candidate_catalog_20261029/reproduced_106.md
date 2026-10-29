# 106 项报告现象复现 SQL

[返回目录](README.md)

按目标版本、bug 编号排序；每项为报告 × 目标版本。状态来自保存证据，本次没有运行数据库。

| 候选项 | Bug | 目标版本 | 标题 | 目标执行状态 | 相邻版本状态 | SQL |
|---|---|---|---|---|---|---|
| mysql-107337-8.0.32 | [107337](https://bugs.mysql.com/bug.php?id=107337) | 8.0.32 | IN() does not work correctly for TIME column | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-107337-8.0.32.sql) |
| mysql-107424-8.0.32 | [107424](https://bugs.mysql.com/bug.php?id=107424) | 8.0.32 | st_intersects() returns different results with or without spatial index | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-107424-8.0.32.sql) |
| mysql-109699-8.0.32 | [109699](https://bugs.mysql.com/bug.php?id=109699) | 8.0.32 | utf8mb4 identifiers stopped working since 8.0.32 release | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-109699-8.0.32.sql) |
| mysql-109725-8.0.32 | [109725](https://bugs.mysql.com/bug.php?id=109725) | 8.0.32 | Wrong result for AVG() OVER(ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-109725-8.0.32.sql) |
| mysql-109796-8.0.32 | [109796](https://bugs.mysql.com/bug.php?id=109796) | 8.0.32 | STR_TO_DATE() invalid input doesn't returns NULL but invalid DATE | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-109796-8.0.32.sql) |
| mysql-109820-8.0.32 | [109820](https://bugs.mysql.com/bug.php?id=109820) | 8.0.32 | optimizer hints in definition of views seem to be ignored | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-109820-8.0.32.sql) |
| mysql-109833-8.0.32 | [109833](https://bugs.mysql.com/bug.php?id=109833) | 8.0.32 | UTF-8 strings are broken when comparing to UNIONs | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-109833-8.0.32.sql) |
| mysql-110003-8.0.32 | [110003](https://bugs.mysql.com/bug.php?id=110003) | 8.0.32 | DELETE query does ot work for BIT columns | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110003-8.0.32.sql) |
| mysql-110005-8.0.32 | [110005](https://bugs.mysql.com/bug.php?id=110005) | 8.0.32 | When using union, when the value of the field in the where condition is Chinese | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110005-8.0.32.sql) |
| mysql-110045-8.0.32 | [110045](https://bugs.mysql.com/bug.php?id=110045) | 8.0.32 | Negative numbers on digests | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110045-8.0.32.sql) |
| mysql-110076-8.0.32 | [110076](https://bugs.mysql.com/bug.php?id=110076) | 8.0.32 | VALUES Statement with dependent subquery is wrong | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110076-8.0.32.sql) |
| mysql-110104-8.0.32 | [110104](https://bugs.mysql.com/bug.php?id=110104) | 8.0.32 | Query exception caused by union in 8.0.32 | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110104-8.0.32.sql) |
| mysql-110125-8.0.32 | [110125](https://bugs.mysql.com/bug.php?id=110125) | 8.0.32 | Unexpected query result fetched from an indexed column | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110125-8.0.32.sql) |
| mysql-110181-8.0.32 | [110181](https://bugs.mysql.com/bug.php?id=110181) | 8.0.32 | tmp_table_size=51200 causing error that tmp does not exists | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110181-8.0.32.sql) |
| mysql-110244-8.0.32 | [110244](https://bugs.mysql.com/bug.php?id=110244) | 8.0.32 | Nesting queries in a projection results in different output | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110244-8.0.32.sql) |
| mysql-110256-8.0.32 | [110256](https://bugs.mysql.com/bug.php?id=110256) | 8.0.32 | An incorrect query result for an indexed decimal column | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110256-8.0.32.sql) |
| mysql-110354-8.0.32 | [110354](https://bugs.mysql.com/bug.php?id=110354) | 8.0.32 | SELECT Query choose different index return different results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110354-8.0.32.sql) |
| mysql-110375-8.0.32 | [110375](https://bugs.mysql.com/bug.php?id=110375) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32，union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110375-8.0.32.sql) |
| mysql-110376-8.0.32 | [110376](https://bugs.mysql.com/bug.php?id=110376) | 8.0.32 | upgrade mysql from 8.0.29 to 8.0.32, union error | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110376-8.0.32.sql) |
| mysql-110384-8.0.32 | [110384](https://bugs.mysql.com/bug.php?id=110384) | 8.0.32 | LIKE query on union result with Unicode characters returns no results | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110384-8.0.32.sql) |
| mysql-110521-8.0.32 | [110521](https://bugs.mysql.com/bug.php?id=110521) | 8.0.32 | 8.0.32 subquery with utf8mb4 equal case empty result | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110521-8.0.32.sql) |
| mysql-110550-8.0.32 | [110550](https://bugs.mysql.com/bug.php?id=110550) | 8.0.32 | ordering VALUES statement seems not to work as expected | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110550-8.0.32.sql) |
| mysql-110556-8.0.32 | [110556](https://bugs.mysql.com/bug.php?id=110556) | 8.0.32 | When we use json to build an index, we will get wrong results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110556-8.0.32.sql) |
| mysql-110562-8.0.32 | [110562](https://bugs.mysql.com/bug.php?id=110562) | 8.0.32 | values statement | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110562-8.0.32.sql) |
| mysql-110587-8.0.32 | [110587](https://bugs.mysql.com/bug.php?id=110587) | 8.0.32 | Bit with index range query may produce different results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110587-8.0.32.sql) |
| mysql-110672-8.0.32 | [110672](https://bugs.mysql.com/bug.php?id=110672) | 8.0.32 | QUOTE function doesn't work as expected on tables that are utf16 | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110672-8.0.32.sql) |
| mysql-110709-8.0.32 | [110709](https://bugs.mysql.com/bug.php?id=110709) | 8.0.32 | Chinese query conditions unable to return results correctly | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110709-8.0.32.sql) |
| mysql-110825-8.0.32 | [110825](https://bugs.mysql.com/bug.php?id=110825) | 8.0.32 | Explicit COLLATE clause output in SHOW CREATE TABLE incorrectly | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110825-8.0.32.sql) |
| mysql-111272-8.0.32 | [111272](https://bugs.mysql.com/bug.php?id=111272) | 8.0.32 | Inconsistent behaviors on string comparison with/without index | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111272-8.0.32.sql) |
| mysql-111363-8.0.32 | [111363](https://bugs.mysql.com/bug.php?id=111363) | 8.0.32 | If you use "UNION ALL" for items with Japanese double-byte characters in a subqu | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-111363-8.0.32.sql) |
| mysql-112037-8.0.32 | [112037](https://bugs.mysql.com/bug.php?id=112037) | 8.0.32 | Contribute by tencent: explain analyze show never executed for materialize | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112037-8.0.32.sql) |
| mysql-112421-8.0.32 | [112421](https://bugs.mysql.com/bug.php?id=112421) | 8.0.32 | zero and null value, left or right join result wrong | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112421-8.0.32.sql) |
| mysql-110771-8.0.33 | [110771](https://bugs.mysql.com/bug.php?id=110771) | 8.0.33 | Failed to update NULL to empty value on instant col for REDUNDANT table | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110771-8.0.33.sql) |
| mysql-110819-8.0.33 | [110819](https://bugs.mysql.com/bug.php?id=110819) | 8.0.33 | EXISTS with dependent subquery can return incorrect results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110819-8.0.33.sql) |
| mysql-110847-8.0.33 | [110847](https://bugs.mysql.com/bug.php?id=110847) | 8.0.33 | Prepared SELECT returns different results on consecutive executions. | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110847-8.0.33.sql) |
| mysql-110915-8.0.33 | [110915](https://bugs.mysql.com/bug.php?id=110915) | 8.0.33 | Having clause missing scope | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110915-8.0.33.sql) |
| mysql-110962-8.0.33 | [110962](https://bugs.mysql.com/bug.php?id=110962) | 8.0.33 | JOIN a table with trigger report unexpected WARNINGS | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110962-8.0.33.sql) |
| mysql-110983-8.0.33 | [110983](https://bugs.mysql.com/bug.php?id=110983) | 8.0.33 | issue with window functions in stored procedures | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-110983-8.0.33.sql) |
| mysql-110984-8.0.33 | [110984](https://bugs.mysql.com/bug.php?id=110984) | 8.0.33 | Subqueries with 'limit 1' cause concat strings to report errors | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-110984-8.0.33.sql) |
| mysql-111067-8.0.33 | [111067](https://bugs.mysql.com/bug.php?id=111067) | 8.0.33 | Query result error | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111067-8.0.33.sql) |
| mysql-111094-8.0.33 | [111094](https://bugs.mysql.com/bug.php?id=111094) | 8.0.33 | Results ordered incorrectly | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111094-8.0.33.sql) |
| mysql-111268-8.0.33 | [111268](https://bugs.mysql.com/bug.php?id=111268) | 8.0.33 | Different character_set_connection returns inconsistent results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111268-8.0.33.sql) |
| mysql-111272-8.0.33 | [111272](https://bugs.mysql.com/bug.php?id=111272) | 8.0.33 | Inconsistent behaviors on string comparison with/without index | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111272-8.0.33.sql) |
| mysql-111290-8.0.33 | [111290](https://bugs.mysql.com/bug.php?id=111290) | 8.0.33 | No matching rows when joining multiple tables on binary/varbinary key | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111290-8.0.33.sql) |
| mysql-111421-8.0.33 | [111421](https://bugs.mysql.com/bug.php?id=111421) | 8.0.33 | Unexpected error when `CHECK` a predicate that is always true | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111421-8.0.33.sql) |
| mysql-111429-8.0.33 | [111429](https://bugs.mysql.com/bug.php?id=111429) | 8.0.33 | Incorrect result when timestamp col apply <=> to the result of subquery | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111429-8.0.33.sql) |
| mysql-111484-8.0.33 | [111484](https://bugs.mysql.com/bug.php?id=111484) | 8.0.33 | wrong result when rewriting scalar subquery in json function parameters | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111484-8.0.33.sql) |
| mysql-111559-8.0.33 | [111559](https://bugs.mysql.com/bug.php?id=111559) | 8.0.33 | View with CTE syntax error | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111559-8.0.33.sql) |
| mysql-111699-8.0.33 | [111699](https://bugs.mysql.com/bug.php?id=111699) | 8.0.33 | Incorrect results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111699-8.0.33.sql) |
| mysql-111706-8.0.33 | [111706](https://bugs.mysql.com/bug.php?id=111706) | 8.0.33 | Incorrect result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111706-8.0.33.sql) |
| mysql-111728-8.0.33 | [111728](https://bugs.mysql.com/bug.php?id=111728) | 8.0.33 | Incorrect result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111728-8.0.33.sql) |
| mysql-111737-8.0.33 | [111737](https://bugs.mysql.com/bug.php?id=111737) | 8.0.33 | Double tick in string literals does not work for CREATE TABLE with NO_BACKSLASH_ | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111737-8.0.33.sql) |
| mysql-112231-8.0.33 | [112231](https://bugs.mysql.com/bug.php?id=112231) | 8.0.33 | Inconsistent result for OVER() when used in stored procedure over InnoDB table | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-112231-8.0.33.sql) |
| mysql-112460-8.0.33 | [112460](https://bugs.mysql.com/bug.php?id=112460) | 8.0.33 | Inconsistent results of SELECT statement with window functions | 报告现象已复现 | 前版正常、目标异常 | [SQL](sql/reproduced_106/mysql-112460-8.0.33.sql) |
| mysql-113061-8.0.33 | [113061](https://bugs.mysql.com/bug.php?id=113061) | 8.0.33 | The result of avg(distinct xx）is different between from primary and secondary | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113061-8.0.33.sql) |
| mysql-113180-8.0.33 | [113180](https://bugs.mysql.com/bug.php?id=113180) | 8.0.33 | Unexpected Results when Using Math Function SIN | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113180-8.0.33.sql) |
| mysql-113298-8.0.33 | [113298](https://bugs.mysql.com/bug.php?id=113298) | 8.0.33 | Unexpected Results when Using IN for Floating-Point | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113298-8.0.33.sql) |
| mysql-113319-8.0.33 | [113319](https://bugs.mysql.com/bug.php?id=113319) | 8.0.33 | unnesting scalar subquery containing count and having cond produces wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113319-8.0.33.sql) |
| mysql-114714-8.0.33 | [114714](https://bugs.mysql.com/bug.php?id=114714) | 8.0.33 | Duplicate subquery explain plan output when explain format is tree | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114714-8.0.33.sql) |
| mysql-116703-8.0.33 | [116703](https://bugs.mysql.com/bug.php?id=116703) | 8.0.33 | `JSON_VALID` has inconsistent behavior for `NULL` | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-116703-8.0.33.sql) |
| mysql-119630-8.0.33 | [119630](https://bugs.mysql.com/bug.php?id=119630) | 8.0.33 | Optimizer incorrectly merges derived table with type conversion and WHERE clause, causing wrong query results | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-119630-8.0.33.sql) |
| mysql-119646-8.0.33 | [119646](https://bugs.mysql.com/bug.php?id=119646) | 8.0.33 | View + Type Conversion + IN Subquery Returns Wrong Result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-119646-8.0.33.sql) |
| mysql-79813-8.0.34 | [79813](https://bugs.mysql.com/bug.php?id=79813) | 8.0.34 | Boolean values are returned inconsistently with JSON_OBJECT | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-79813-8.0.34.sql) |
| mysql-111918-8.0.34 | [111918](https://bugs.mysql.com/bug.php?id=111918) | 8.0.34 | Auto increment column query wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-111918-8.0.34.sql) |
| mysql-112037-8.0.34 | [112037](https://bugs.mysql.com/bug.php?id=112037) | 8.0.34 | Contribute by tencent: explain analyze show never executed for materialize | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112037-8.0.34.sql) |
| mysql-112147-8.0.34 | [112147](https://bugs.mysql.com/bug.php?id=112147) | 8.0.34 | Use/Ignore Mutil-value index for MEMBER OF function has differnet result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112147-8.0.34.sql) |
| mysql-112198-8.0.34 | [112198](https://bugs.mysql.com/bug.php?id=112198) | 8.0.34 | Incorrect multiple equality optimization causes performance degradation | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112198-8.0.34.sql) |
| mysql-112212-8.0.34 | [112212](https://bugs.mysql.com/bug.php?id=112212) | 8.0.34 | Subquery to derived result mismatch(HASH JOIN/BNL JOIN result mismatch) | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112212-8.0.34.sql) |
| mysql-112231-8.0.34 | [112231](https://bugs.mysql.com/bug.php?id=112231) | 8.0.34 | Inconsistent result for OVER() when used in stored procedure over InnoDB table | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112231-8.0.34.sql) |
| mysql-112242-8.0.34 | [112242](https://bugs.mysql.com/bug.php?id=112242) | 8.0.34 | Unexpected Results by use_invisible_indexes | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112242-8.0.34.sql) |
| mysql-112269-8.0.34 | [112269](https://bugs.mysql.com/bug.php?id=112269) | 8.0.34 | Unexpected Results by the hint JOIN_ORDER | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112269-8.0.34.sql) |
| mysql-112275-8.0.34 | [112275](https://bugs.mysql.com/bug.php?id=112275) | 8.0.34 | "Extra" field has NULL value if table is temporary | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112275-8.0.34.sql) |
| mysql-112293-8.0.34 | [112293](https://bugs.mysql.com/bug.php?id=112293) | 8.0.34 | Wrong result if non-breaking space is contained in varchar | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112293-8.0.34.sql) |
| mysql-112296-8.0.34 | [112296](https://bugs.mysql.com/bug.php?id=112296) | 8.0.34 | Unexpected Result by NO_BNL | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112296-8.0.34.sql) |
| mysql-112306-8.0.34 | [112306](https://bugs.mysql.com/bug.php?id=112306) | 8.0.34 | Unexpected Result by JOIN_SUFFIX | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112306-8.0.34.sql) |
| mysql-112387-8.0.34 | [112387](https://bugs.mysql.com/bug.php?id=112387) | 8.0.34 | Inconsistent results caused by "UNION ALL" with empty subqueries | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112387-8.0.34.sql) |
| mysql-112439-8.0.34 | [112439](https://bugs.mysql.com/bug.php?id=112439) | 8.0.34 | Incorrect results when using VALUES statement as derived query | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112439-8.0.34.sql) |
| mysql-112460-8.0.34 | [112460](https://bugs.mysql.com/bug.php?id=112460) | 8.0.34 | Inconsistent results of SELECT statement with window functions | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112460-8.0.34.sql) |
| mysql-112527-8.0.34 | [112527](https://bugs.mysql.com/bug.php?id=112527) | 8.0.34 | Inconsistent results caused by REPEAT function | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112527-8.0.34.sql) |
| mysql-112557-8.0.34 | [112557](https://bugs.mysql.com/bug.php?id=112557) | 8.0.34 | Inconsistent results of SELECT statement with EXISTS clause | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112557-8.0.34.sql) |
| mysql-112661-8.0.34 | [112661](https://bugs.mysql.com/bug.php?id=112661) | 8.0.34 | Got 'Unknown error -1' when create index on table | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112661-8.0.34.sql) |
| mysql-112737-8.0.34 | [112737](https://bugs.mysql.com/bug.php?id=112737) | 8.0.34 | Conditions refering to const table were not added to RANGE SCAN | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112737-8.0.34.sql) |
| mysql-112910-8.0.35 | [112910](https://bugs.mysql.com/bug.php?id=112910) | 8.0.35 | Incorrect results when add an uncorrelated row | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112910-8.0.35.sql) |
| mysql-112911-8.0.35 | [112911](https://bugs.mysql.com/bug.php?id=112911) | 8.0.35 | Inconsistent results when using PRIMARY and DUPSWEEDOUT | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-112911-8.0.35.sql) |
| mysql-113097-8.0.35 | [113097](https://bugs.mysql.com/bug.php?id=113097) | 8.0.35 | query bug racecondition | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113097-8.0.35.sql) |
| mysql-113171-8.0.35 | [113171](https://bugs.mysql.com/bug.php?id=113171) | 8.0.35 | sum(distinct substring()) does not give warnings, while sum(substring() does | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113171-8.0.35.sql) |
| mysql-113180-8.0.35 | [113180](https://bugs.mysql.com/bug.php?id=113180) | 8.0.35 | Unexpected Results when Using Math Function SIN | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113180-8.0.35.sql) |
| mysql-113298-8.0.35 | [113298](https://bugs.mysql.com/bug.php?id=113298) | 8.0.35 | Unexpected Results when Using IN for Floating-Point | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113298-8.0.35.sql) |
| mysql-113301-8.0.35 | [113301](https://bugs.mysql.com/bug.php?id=113301) | 8.0.35 | using preparation statement to query the time type data, some data is not found | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113301-8.0.35.sql) |
| mysql-113302-8.0.35 | [113302](https://bugs.mysql.com/bug.php?id=113302) | 8.0.35 | Unexpected Result for an Index | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113302-8.0.35.sql) |
| mysql-113316-8.0.35 | [113316](https://bugs.mysql.com/bug.php?id=113316) | 8.0.35 | When the bit type has an index, the query result is incorrect. | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113316-8.0.35.sql) |
| mysql-113319-8.0.35 | [113319](https://bugs.mysql.com/bug.php?id=113319) | 8.0.35 | unnesting scalar subquery containing count and having cond produces wrong result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113319-8.0.35.sql) |
| mysql-113358-8.0.35 | [113358](https://bugs.mysql.com/bug.php?id=113358) | 8.0.35 | Wrong functional dependency in ONLY_FULL_GROUP_BY mode | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113358-8.0.35.sql) |
| mysql-113433-8.0.35 | [113433](https://bugs.mysql.com/bug.php?id=113433) | 8.0.35 | Incorrect query results involving the date type. | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113433-8.0.35.sql) |
| mysql-113506-8.0.35 | [113506](https://bugs.mysql.com/bug.php?id=113506) | 8.0.35 | Item_func_conv_charset::eq not correct | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113506-8.0.35.sql) |
| mysql-113534-8.0.35 | [113534](https://bugs.mysql.com/bug.php?id=113534) | 8.0.35 | table join return Unexpected result when drived table using include join index | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113534-8.0.35.sql) |
| mysql-113557-8.0.35 | [113557](https://bugs.mysql.com/bug.php?id=113557) | 8.0.35 | Wrong query result on composite multi-valued index + empty array value | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113557-8.0.35.sql) |
| mysql-113649-8.0.35 | [113649](https://bugs.mysql.com/bug.php?id=113649) | 8.0.35 | the result of format function truncated when using cursor | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113649-8.0.35.sql) |
| mysql-113768-8.0.35 | [113768](https://bugs.mysql.com/bug.php?id=113768) | 8.0.35 | return error with cast | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-113768-8.0.35.sql) |
| mysql-114196-8.0.35 | [114196](https://bugs.mysql.com/bug.php?id=114196) | 8.0.35 | Incorrect query result caused by comparing decimal and float type value | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114196-8.0.35.sql) |
| mysql-114380-8.0.35 | [114380](https://bugs.mysql.com/bug.php?id=114380) | 8.0.35 | Incorrect query result may caused by TIMESTAMP | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114380-8.0.35.sql) |
| mysql-114381-8.0.35 | [114381](https://bugs.mysql.com/bug.php?id=114381) | 8.0.35 | Incorrect query result may caused by EXISTS and TIMEDIFF | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114381-8.0.35.sql) |
| mysql-114384-8.0.35 | [114384](https://bugs.mysql.com/bug.php?id=114384) | 8.0.35 | Incorrect query result may caused by LOG | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114384-8.0.35.sql) |
| mysql-114775-8.0.35 | [114775](https://bugs.mysql.com/bug.php?id=114775) | 8.0.35 | Outer join condition filtering bug when using scalar subquery | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114775-8.0.35.sql) |
| mysql-114917-8.0.35 | [114917](https://bugs.mysql.com/bug.php?id=114917) | 8.0.35 | Incorrect query result | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-114917-8.0.35.sql) |
| mysql-115294-8.0.35 | [115294](https://bugs.mysql.com/bug.php?id=115294) | 8.0.35 | partition table's io wait summary not correct in PERFORMANCE_SCHEMA | 报告现象已复现 | 前版同异常 | [SQL](sql/reproduced_106/mysql-115294-8.0.35.sql) |

## 逐项内容

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_107337_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-107337-8.0.32.sql)；SHA256：`285744a112e07dc34e0aab8ea532cff83e6cd7d8135a75f39cf9d690094d6499`。

```sql
-- MySQL report #107337; source anchors: cmain, c522679, c554592
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t(a TIME);
INSERT INTO t VALUES('08:00:00');
SELECT * FROM t WHERE a IN ('08:00:00',NULL);
SELECT * FROM t WHERE a IN ('08:00:00','');
SELECT * FROM t WHERE a IN ('08:00:00','07:59:59');
SELECT * FROM t WHERE a IN (TIME'08:00:00',NULL);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_107337_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L1)
- `target_107337_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_107424_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-107424-8.0.32.sql)；SHA256：`206d33024f7e9eb393fb0b334f447d1daa6372c2423323b88596da010b05b2ac`。

```sql
-- MySQL report #107424; source: cmain, c522894, c531290
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1(g1 GEOMETRY NOT NULL SRID 4326);
INSERT INTO t1 VALUES(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326));
INSERT INTO t1 VALUES(ST_GeomFromText('point(-6.124932923690693 23.43701608651874)',4326));
SELECT ST_AsText(g1) FROM t1 WHERE ST_Intersects(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326),g1);
CREATE SPATIAL INDEX spidx ON t1(g1);
SELECT ST_AsText(g1) FROM t1 WHERE ST_Intersects(ST_GeomFromText('point(-6.124932923690693 23.43701608651873)',4326),g1);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_107424_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b001_8_0_32/results/records.jsonl#L1)
- `target_107424_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b004_8_0_32/results/records.jsonl#L1)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_109699_8_0_32_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-109699-8.0.32.sql)；SHA256：`6d3714af281c13ceb2cff741a4c8b164b2deaf63f5ff76d4b46379ed60c38fee`。

```sql
SET NAMES utf8mb4;
CREATE TABLE `employee` (
  `id` INT UNSIGNED AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) DEFAULT NULL,
  `surname` VARCHAR(255) DEFAULT NULL,
  `retired` TINYINT(1) DEFAULT NULL,
  PRIMARY KEY(`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE `utf8mb4_unicode_ci` ENGINE = InnoDB;

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (1, 'Oliver', 'Smith', 0);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (2, 'Jack', 'Williams', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (3, 'Harry', 'Taylor', 1);

insert into `employee` (
  `id`, `name`, `surname`, `retired`
)
values
  (4, 'Charlie', 'Lee', 0);

select
  *
from
  (
    select
      'žlutý_😀' `❤`
  ) `🚀`
where
  `❤` = 'žlutý_😀'
group by
  `🚀`.`❤`
having
  (`❤` = 'žlutý_😀');
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_109699_8_0_32_target_r1`，实际版本 8.0.32，completed；[records.jsonl:61](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L61)
- `candidate_109699_8_0_32_target_r2`，实际版本 8.0.32，completed；[records.jsonl:62](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L62)
- `candidate_109699_8_0_32_target_r3`，实际版本 8.0.32，completed；[records.jsonl:63](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L63)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_109725_8_0_32_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-109725-8.0.32.sql)；SHA256：`c99c4e02d242a02a8417c4ad59e0c738268ccea9a25c06d6e0a624cf849dcc9a`。

```sql
SET NAMES utf8mb4;
CREATE TABLE t (
    n INTEGER
);

INSERT INTO t VALUES (1), (2), (3), (4);

SELECT n
     , SUM(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "sum(n)"
     , COUNT(*) OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "count(n)"
     , AVG(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "avg(n)"
     , SUM(n)   OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
     / COUNT(*) OVER(ORDER BY n ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING) AS "sum(n)/count(n)"
  FROM t
 ORDER BY n;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_109725_8_0_32_target_r1`，实际版本 8.0.32，completed；[records.jsonl:67](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L67)
- `candidate_109725_8_0_32_target_r2`，实际版本 8.0.32，completed；[records.jsonl:68](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L68)
- `candidate_109725_8_0_32_target_r3`，实际版本 8.0.32，completed；[records.jsonl:69](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L69)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_109796_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-109796-8.0.32.sql)；SHA256：`d0f8b3ae5ecef0a6046355587dec7d729d6af92fcec6a1ea3b84677037bc8b0d`。

```sql
SET @@sql_mode = 'ANSI,TRADITIONAL';
SELECT @@sql_mode;
SELECT DATE('2022-04-31');
SELECT STR_TO_DATE('2022-04-31', '%Y-%m-%d');
SELECT DATE(STR_TO_DATE('2022-04-31', '%Y-%m-%d'));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_109796_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-109796-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_109820_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-109820-8.0.32.sql)；SHA256：`2c7c47ce44f8b56be25c83b5c2b74cdd653a55aacb54e96b3dcf651557ef8fac`。

```sql
-- MySQL report #109820; source anchors: cmain, c529314
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(id INT);
INSERT INTO t1 VALUES(1),(2);
EXPLAIN SELECT /*+ NO_MERGE() */ * FROM (SELECT * FROM t1) dt;
SHOW WARNINGS;
CREATE VIEW v_1 AS SELECT /*+ NO_MERGE() */ * FROM (SELECT * FROM t1) dt;
SHOW CREATE VIEW v_1;
EXPLAIN SELECT * FROM v_1;
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_109820_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L5)
- `target_109820_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_109833_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-109833-8.0.32.sql)；SHA256：`c2ab8c2e0bb8cda8fba5938660b1026031a012c44e5c89969f542a84b06cb2ff`。

```sql
-- MySQL report #109833; source anchors: cmain, c529335, c529371
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
CREATE TABLE `vals0` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals0` VALUES ('OK');

CREATE TABLE `vals1` (
  `k` VARCHAR(8) CHARSET utf8mb4 COLLATE utf8mb4_bin NOT NULL PRIMARY KEY
);
INSERT INTO `vals1` VALUES ('ERRÖR');

-- this works as expected
SELECT * FROM `vals1` WHERE `k` = 'ERRÖR';

-- this works as expected
-- Original undefined view_vals control omitted; use the complete derived query below.

-- this returns empty result set, and a warning about converting D6 to utf8
SELECT * FROM (SELECT `v0`.`k` AS `k` FROM `vals0` AS `v0` UNION ALL SELECT `v1`.`k` AS `k` FROM `vals1` as `v1`) AS `a` WHERE `a`.`k` = 'ERRÖR';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_109833_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L6)
- `target_109833_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110003_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110003-8.0.32.sql)；SHA256：`3fde0b1f14d16379aeec78a51507c7460258299053b602d5fbe47a578098ea44`。

```sql
-- MySQL report #110003; source anchors: cmain, c529853, c529854
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(id INT NOT NULL AUTO_INCREMENT,val BIT(1) NOT NULL DEFAULT b'0',PRIMARY KEY(id,val)) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8mb4;
INSERT INTO t1(val) VALUES(0),(1);
INSERT INTO t1(val) SELECT val FROM t1;
INSERT INTO t1(val) SELECT val FROM t1;
SELECT id,HEX(val) FROM t1 WHERE id='123' AND val='1';
SELECT COUNT(*) AS before_count FROM t1;
DELETE FROM t1 WHERE id='123' AND val='1';
SELECT ROW_COUNT() AS deleted_count;
SELECT COUNT(*) AS after_count FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110003_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L2)
- `target_110003_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L2)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110005_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110005-8.0.32.sql)；SHA256：`92a443eb1d53f97e643b57d22d717a4ae07853524bba722568f2a6dff044d77a`。

```sql
CREATE TABLE test (id int unsigned auto_increment key,name varchar(50)) ENGINE=INNODB;
INSERT INTO test(id,name) VALUES(1,'姜志福');
SELECT * FROM (SELECT * FROM test UNION ALL SELECT * FROM test) a WHERE id=1 AND name='姜志福';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110005_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110005-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110045_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110045-8.0.32.sql)；SHA256：`9ff8b78de3615e238befcf3ea402a9f8224bbf2144a2ed963dcf71c53e94ed00`。

```sql
-- MySQL report #110045; source: cmain, c554980
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = 1');
SELECT STATEMENT_DIGEST_TEXT('SELECT -1 WHERE 1 = -1');
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110045_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L7)
- `target_110045_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L3)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110076_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110076-8.0.32.sql)；SHA256：`673b8b75b23682816afefb2497af1797e0d85ac12aa8ef0a6ed5a8886bb56fff`。

```sql
CREATE TABLE mytable(ID INTEGER NOT NULL,a VARCHAR(4) NOT NULL,b VARCHAR(4) NOT NULL,c VARCHAR(3) NOT NULL);
INSERT INTO mytable(ID,a,b,c) VALUES (1,'a1','b1','c1');
INSERT INTO mytable(ID,a,b,c) VALUES (2,'a2','b2','c2');
SELECT ID,(SELECT MAX(col1) FROM (VALUES ROW(a),ROW(b),ROW(c)) AS x(col1)) AS max FROM mytable;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110076_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_002/mysql-110076-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110104_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110104-8.0.32.sql)；SHA256：`71734de210b5a41c9acbcc03293d6bbc4ca45683f61b2967465c2dcb937f4c6f`。

```sql
SET NAMES utf8mb4;
CREATE TABLE test_1(id INT,NAME VARCHAR(100));
CREATE TABLE test_2(id INT,NAME VARCHAR(100));
INSERT INTO test_1 VALUES(1,'aaa'),(2,'bbb'),(3,'ccc'),(4,'ddd'),(5,'测试');
INSERT INTO test_2 VALUES(11,'eee');
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp;
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT * FROM test_1 WHERE NAME='测试' UNION SELECT * FROM test_2 WHERE NAME='bbb') tmp WHERE NAME='测试';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110104_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110104-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110125_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110125-8.0.32.sql)；SHA256：`f05f1c1d4b06b75cd025fe4108ddbb152c978fbe0a8b3d6ec3ede96bf7454fa8`。

```sql
-- MySQL report #110125; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DOUBLE ZEROFILL) ;
CREATE INDEX i0 ON t0(c0 DESC);
INSERT DELAYED IGNORE INTO t0(c0) VALUES(0);

SELECT c0 FROM t0 WHERE (IFNULL(-1123870957, '')) IN (t0.c0); -- 0
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110125_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:3](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L3)
- `target_110125_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:3](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L3)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110181_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110181-8.0.32.sql)；SHA256：`9d2e36e6f9520bc4591cc5825adcf8aa1b70ba738c7d30797ef04b1d35e7e959`。

```sql
-- MySQL report #110181; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET SESSION tmp_table_size=51200;
SELECT @@session.tmp_table_size;
SELECT * FROM information_schema.APPLICABLE_ROLES;
SELECT * FROM information_schema.ADMINISTRABLE_ROLE_AUTHORIZATIONS;
SELECT * FROM information_schema.ROLE_TABLE_GRANTS;
SET SESSION tmp_table_size=16777216;
SELECT * FROM information_schema.APPLICABLE_ROLES;
SELECT * FROM information_schema.ADMINISTRABLE_ROLE_AUTHORIZATIONS;
SELECT * FROM information_schema.ROLE_TABLE_GRANTS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110181_8_0_32_r1`，实际版本 8.0.32，completed_with_sql_errors；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110244_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110244-8.0.32.sql)；SHA256：`ae338e367328c07a119cc4515e23bc4eb9070a0c5fd0b8f18fd0388a119441a5`。

```sql
-- MySQL report #110244; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE FRIENDSHIP (
  USER1_ID INTEGER, 
  USER2_ID INTEGER,
  PRIMARY KEY (USER1_ID, USER2_ID)
);
INSERT INTO FRIENDSHIP VALUES (1, 0);

CREATE TABLE LIKES (
  USER_ID INTEGER, 
  PAGE_ID INTEGER,
  PRIMARY KEY (USER_ID, PAGE_ID)
);
INSERT INTO LIKES VALUES (2, 0);

-- Q1
SELECT * FROM (SELECT B.USER_ID, B.PAGE_ID FROM FRIENDSHIP A LEFT JOIN LIKES B 
ON (A.USER2_ID=B.USER_ID OR A.USER1_ID=B.USER_ID) 
WHERE (A.USER1_ID=1 OR A.USER2_ID=1) ) TMP 
WHERE PAGE_ID NOT IN ( SELECT DISTINCT(PAGE_ID) FROM LIKES WHERE USER_ID=1);

-- Q2
SELECT * FROM (
SELECT * FROM (SELECT B.USER_ID, B.PAGE_ID FROM FRIENDSHIP A LEFT JOIN LIKES B 
ON (A.USER2_ID=B.USER_ID OR A.USER1_ID=B.USER_ID) 
WHERE (A.USER1_ID=1 OR A.USER2_ID=1) ) TMP 
WHERE PAGE_ID NOT IN ( SELECT DISTINCT(PAGE_ID) FROM LIKES WHERE USER_ID=1)
) AS T;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110244_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:4](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L4)
- `target_110244_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:4](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110256_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110256-8.0.32.sql)；SHA256：`9fd9dff23772f83a96715c9dad0aff71975e1aa21b5653326d5c5b4234697cd7`。

```sql
-- Report #110256; source anchors: cmain, c530389
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c0 DECIMAL) ;
INSERT DELAYED IGNORE INTO t0(c0) VALUES('');
CREATE INDEX i0 ON t0(c0 DESC);
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0")); 
DROP INDEX i0 ON t0;
SELECT ALL t0.c0 FROM t0 WHERE (t0.c0) = (LEAST('1507214118', "0W*-+	U0"));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110256_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:5](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L5)
- `target_110256_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:5](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L5)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110354_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110354-8.0.32.sql)；SHA256：`8b17b5df2ed8b8d39afc0757ff757bb6ed597d08579859cfcb77e0cfb67fed5c`。

```sql
-- Report #110354; source anchors: cmain, f32102
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_old_mode=@@session.sql_mode, @case_old_tz=@@session.time_zone;
SET SESSION sql_mode='';
SET SESSION time_zone='+08:00';
# prepare table and data
CREATE TABLE tt(a timestamp, b time, KEY b_idx(b), KEY a_b_idx(a,b));
INSERT INTO tt VALUES('2020-12-01 10:00:00', '02:59:59.000000');
INSERT INTO tt VALUES('2020-11-01 10:00:00', '03:59:59.000000');
INSERT INTO tt VALUES('2020-10-01 10:00:00', '04:59:59.000000');
INSERT INTO tt VALUES('2020-09-01 10:00:00', '05:59:59.000000');
INSERT INTO tt VALUES('2020-08-01 10:00:00', '06:59:59.000000');
INSERT INTO tt VALUES('2020-07-01 10:00:00', '07:59:59.000000');
INSERT INTO tt VALUES('2020-05-06 10:00:00', '08:59:59.000000');
INSERT INTO tt VALUES('2020-04-04 10:00:00', '20:59:59.000000');
INSERT INTO tt VALUES('2020-03-02 10:00:00', '09:09:59.000000');
INSERT INTO tt VALUES('2020-02-03 10:00:00', '10:59:59.000000');
INSERT INTO tt VALUES('2020-01-01 10:00:00', '23:23:59.000000');
INSERT INTO tt VALUES('2020-01-01 10:00:00', '01:59:59.000000');
INSERT INTO tt VALUES('2020-01-01 00:00:01', '12:00:00.000000');
INSERT INTO tt VALUES('2008-10-02 12:20:00', NULL);
INSERT INTO tt VALUES('1999-09-02 12:20:00', NULL);
INSERT INTO tt VALUES('1998-09-02 12:20:00', NULL);
INSERT INTO tt VALUES('1997-09-02 12:20:00', NULL);
INSERT INTO tt VALUES('1995-09-02 12:20:00', NULL);
INSERT INTO tt VALUES('1992-03-04 12:20:00', NULL);
INSERT INTO tt VALUES('1970-01-01 08:00:01', '24:59:59.000000');
INSERT INTO tt VALUES('0000-00-00 00:00:00', '00:00:00.000000');

# return 6 rows 
SELECT * FROM tt FORCE INDEX(b_idx) WHERE b NOT BETWEEN '06:59:59.000000' AND NULL;
# return 15 rows
SELECT * FROM tt FORCE INDEX(a_b_idx) WHERE b NOT BETWEEN '06:59:59.000000' AND NULL;
SELECT * FROM tt IGNORE INDEX(b_idx,a_b_idx) WHERE b NOT BETWEEN '06:59:59.000000' AND NULL;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110354_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L8)
- `target_110354_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L4)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110375_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110375-8.0.32.sql)；SHA256：`27e05069c1b7dd202709b9327f9c9973f04298f682df9bd7bd4f98ae345fd329`。

```sql
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110375_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110375-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110376_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110376-8.0.32.sql)；SHA256：`4e613f0b1fbe17c3e3421522d95e3766cab9ea3424322c395e379ff8ab951668`。

```sql
SET NAMES utf8mb4;
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT '中国' AS corporation UNION ALL SELECT '法国' AS corporation) t WHERE t.corporation LIKE '%中国%';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110376_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110376-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110384_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110384-8.0.32.sql)；SHA256：`a8bb7e34d631b0706918c04bb1ce39f44c528cbc5a9e201a2f9f828919422faf`。

```sql
CREATE TABLE t1 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
CREATE TABLE t2 (Name VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);
INSERT INTO t1(Name) VALUES ('valueテスト');
INSERT INTO t2(Name) VALUES ('テストvalue');
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%テスト%';
SHOW WARNINGS;
SELECT Name FROM (SELECT Name FROM t1 UNION SELECT Name FROM t2) derived WHERE Name LIKE '%value%';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110384_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110384-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110521_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110521-8.0.32.sql)；SHA256：`5472b343730bedbe7f1624b7e2fc1897935dce97bc571f282dc7843c2052bd13`。

```sql
SELECT * FROM (SELECT "の" AS v) tbl WHERE tbl.v = "の";
SHOW WARNINGS;
CREATE TABLE tbl(id INT PRIMARY KEY,v VARCHAR(30)) DEFAULT CHARSET utf8mb4;
INSERT INTO tbl VALUES (1,'の');
SELECT * FROM (SELECT * FROM tbl UNION SELECT * FROM tbl) t WHERE t.v='の';
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110521_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-110521-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 3 次；下列默认 SQL 对应 target_110550_8_0_32_r3。

[下载独立 SQL](sql/reproduced_106/mysql-110550-8.0.32.sql)；SHA256：`5c04416579fad7db3829e60d8449c7ed3b53125d23738bfb0c7601ff04972928`。

```sql
-- MySQL report #110550; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) ORDER BY column_1;
VALUES ROW(1,1,1), ROW(5,5,5), ROW(4,4,4) UNION VALUES ROW(0,0,0) ORDER BY column_1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110550_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L1)
- `target_110550_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/retrieved/results_confirmation/records.jsonl#L1)
- `target_110550_8_0_32_r3`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/retrieved/results_confirmation/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110556_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110556-8.0.32.sql)；SHA256：`ce50faa8ec7c3cb8b19bdeb7ed38cbbedcc23cf3b47e834476eacbf1ffd71f65`。

```sql
-- MySQL report #110556; source anchors: cmain, c556442
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE test1(md_id INT NOT NULL AUTO_INCREMENT,member_id INT NOT NULL,mid INT NOT NULL,expand_info JSON NOT NULL,PRIMARY KEY(md_id) USING BTREE,UNIQUE INDEX member_id(mid ASC,member_id ASC) USING BTREE) ENGINE=InnoDB;
INSERT INTO test1 VALUES(1,1,1,'[1]'),(2,2,1,'[]');
ALTER TABLE test1 ADD INDEX test_index(mid,(CAST(expand_info AS CHAR(20) ARRAY)));
SELECT COUNT(*) FROM test1 FORCE INDEX(PRIMARY) WHERE mid=1;
SELECT COUNT(*) FROM test1 FORCE INDEX(test_index) WHERE mid=1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110556_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:9](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L9)
- `target_110556_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L5)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110562_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110562-8.0.32.sql)；SHA256：`fb8c915466e69d7bfc191914ba85ecefa57253a6ddb84bfec2cab59aca84aa24`。

```sql
-- MySQL report #110562; source anchors: cmain, c531648
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
VALUES ROW(1,4),ROW(2,1),ROW(3,3) ORDER BY column_1;
SELECT * FROM (VALUES ROW(1,4),ROW(2,1),ROW(3,3)) AS t ORDER BY column_1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110562_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110587_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110587-8.0.32.sql)；SHA256：`06a182e34cf67a06497adca046bd42eec423db1bb3c2beffbdfc9554f039b91d`。

```sql
-- MySQL report #110587; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode = '';
CREATE TABLE t5(c1  BIT(16) NOT NULL, c2  BIT(16));
INSERT IGNORE INTO t5 VALUES (95, 46), (31, 438), (61, 152), (78, 123), (88, 411), (122, 118), (0, 177),(75, 42), (108, 67), (79, 349), (59, 188), (69, 206), (49, 345), (118, 380),(111, 368), (94, 468), (56, 379), (77, 133), (29, 399), (9, 363), (23, 36),(116, 390), (119, 368), (87, 351), (123, 411), (24, 398), (34, 202), (28, 499),(30, 83), (5, 178), (60, 343), (4, 245), (104, 280), (106, 446), (127, 403),(44, 307), (68, 454), (57, 135);
SELECT HEX(c1) FROM t5 WHERE c1 BETWEEN '16' AND '64';
ALTER TABLE t5 ADD KEY idx(c1);
SELECT HEX(c1) FROM t5 WHERE c1 BETWEEN '16' AND '64';
SELECT HEX(c1) FROM t5 IGNORE INDEX(idx) WHERE c1 BETWEEN '16' AND '64';
EXPLAIN FORMAT=TREE SELECT c1 FROM t5 WHERE c1 BETWEEN '16' AND '64';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110587_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:10](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b001_8_0_32/results/records.jsonl#L10)
- `target_110587_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b001_8_0_32/results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110672_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110672-8.0.32.sql)；SHA256：`0d01d40c93f1c58fe22bee3e7f88f8e290b0f1588633d2ba7722479bc8c1b069`。

```sql
-- MySQL report #110672; source anchors: cmain, c531731
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE LATIN1_TABLE (
  COLUMN1 varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO LATIN1_TABLE (COLUMN1) VALUES (NULL);
INSERT INTO LATIN1_TABLE (COLUMN1) VALUES ('NOTNULL');

SELECT QUOTE(COLUMN1) FROM LATIN1_TABLE; -- returns NULL, and 'NOTNULL' as expected.

CREATE TABLE UTF16_TABLE (
  COLUMN1 varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

INSERT INTO UTF16_TABLE (COLUMN1) VALUES (NULL);
INSERT INTO UTF16_TABLE (COLUMN1) VALUES ('NOTNULL');

SELECT QUOTE(COLUMN1) FROM UTF16_TABLE; -- returns Japanese/Mojibake and 'NOTNULL'.
SELECT HEX(QUOTE(COLUMN1)),CHARSET(QUOTE(COLUMN1)),QUOTE(COLUMN1) IS NULL FROM UTF16_TABLE;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110672_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b002_8_0_32/results/records.jsonl#L1)
- `target_110672_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b002_8_0_32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110709_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110709-8.0.32.sql)；SHA256：`6ddde2027837ab32fad197918fcc6eadc4a9199a4196ed340d3eaa006febd523`。

```sql
SET NAMES utf8mb4;
CREATE TABLE TEST_01 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_01(编号,动物) VALUES(1,'牛');
CREATE TABLE TEST_02 (编号 INT(2),动物 VARCHAR(20));
INSERT INTO TEST_02(编号,动物) VALUES(2,'羊');
CREATE VIEW TEST_V AS SELECT 编号,动物 FROM TEST_01 UNION ALL SELECT 编号,动物 FROM TEST_02;
SELECT * FROM TEST_V WHERE 动物='牛';
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM TEST_V WHERE 动物='牛';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110709_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110709-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110825_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110825-8.0.32.sql)；SHA256：`26ea4352c9f5601ab4205a9b6be2808b9d5aaa55580d7d477309cc7b535984be`。

```sql
-- MySQL report #110825; source anchors: cmain
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t(v VARCHAR(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
SHOW CREATE TABLE t;
SELECT COLUMN_NAME,CHARACTER_SET_NAME,COLLATION_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t';
DROP TABLE t;
CREATE TABLE t(v VARCHAR(100) COLLATE utf8mb4_unicode_ci NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
SHOW CREATE TABLE t;
SELECT COLUMN_NAME,CHARACTER_SET_NAME,COLLATION_NAME FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='t';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110825_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b002_8_0_32/results/records.jsonl#L2)
- `target_110825_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b002_8_0_32/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111272_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111272-8.0.32.sql)；SHA256：`9337a13bcfeb5db00d4aa506dea161301d133c51ba62b18c697a512b71d73aa5`。

```sql
-- MySQL report #111272; source anchors: cmain, c533174
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
-- case 1
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT, KEY i0 (c1(1)));
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 1

-- case 2
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT);
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 2
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111272_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b001_8_0_32/results/records.jsonl#L2)
- `target_111272_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b004_8_0_32/results/records.jsonl#L2)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_111363_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-111363-8.0.32.sql)；SHA256：`208affe805f33811274e0b4ce06d0e2427cf63dbec3715a82153f125621085e2`。

```sql
SET NAMES utf8mb4;
SELECT @@optimizer_switch;
CREATE TABLE TEST01(A VARCHAR(4));
INSERT INTO TEST01(A) VALUES ('あ');
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';
SHOW WARNINGS;
SET optimizer_switch='derived_condition_pushdown=off';
SELECT * FROM (SELECT A FROM TEST01 UNION ALL SELECT A FROM TEST01) SUB WHERE SUB.A='あ';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111363_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_005/mysql-111363-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112037_8_0_32_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112037-8.0.32.sql)；SHA256：`80244524e0223fd701016c298f6cd5fc9a6176f413bea29b8a41060be585e438`。

```sql
-- MySQL report #112037; source: cmain, c535234
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t1(a INT);
INSERT INTO t1 VALUES (1),(2),(3),(4);
ANALYZE TABLE t1;
SET optimizer_switch='subquery_to_derived=on';
EXPLAIN analyze SELECT a + (SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2 ) FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112037_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b001_8_0_32/results/records.jsonl#L3)
- `target_112037_8_0_32_r2`，实际版本 8.0.32，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b004_8_0_32/results/records.jsonl#L3)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112421_8_0_32_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112421-8.0.32.sql)；SHA256：`65ceedd66bfd1485ca43fa8f0e9b79e733e9ca6e996294df9c5dd80d662870a0`。

```sql
CREATE TABLE test1 (id decimal(12,2));
INSERT INTO test1 VALUES (0.00),(NULL);
CREATE TABLE test2 (id decimal(12,2));
INSERT INTO test2 VALUES (0.00),(NULL);
SELECT * FROM test1;
SELECT * FROM test2;
SELECT * FROM test1 c LEFT JOIN test2 d ON c.id=d.id;
SELECT * FROM test1 c RIGHT JOIN test2 d ON c.id=d.id;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112421_8_0_32_r1`，实际版本 8.0.32，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-112421-8.0.32/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110771_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110771-8.0.33.sql)；SHA256：`82a85b2ef71b6b1602402a0b20094b151400a0e3ec1a6028ad77a6e813f9a060`。

```sql
-- MySQL report #110771; source anchors: cmain, c533650, c546398
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t1(a INT,b INT,KEY(b)) ENGINE=InnoDB ROW_FORMAT=REDUNDANT;
INSERT INTO t1 VALUES(0,0),(1,1),(2,2);
ALTER TABLE t1 ADD COLUMN c VARCHAR(25) DEFAULT NULL,ALGORITHM=INSTANT;
UPDATE t1 SET c='' WHERE a=0;
SELECT a,b,c,c IS NULL,LENGTH(c) FROM t1 ORDER BY a;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110771_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_6/b001_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110819_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110819-8.0.33.sql)；SHA256：`592c0efb0bbf0c16d5791210199c08c99cf964437447693825edb650491f2ba8`。

```sql
CREATE DATABASE bug_db;
CREATE TABLE bug_db.bug_t(id INT NOT NULL AUTO_INCREMENT, col_str VARCHAR(255), col_int INT, PRIMARY KEY (id), INDEX col_str (col_str), INDEX col_int_ind (col_int));
INSERT INTO bug_db.bug_t(id,col_str,col_int) VALUES (1,"a",1),(2,"a",1),(3,"a",1);
SELECT @@SESSION.optimizer_switch;
SELECT id FROM bug_db.bug_t t1 WHERE EXISTS (SELECT 1 FROM bug_db.bug_t t2 WHERE t1.id > t2.id AND t1.col_str=t2.col_str AND t1.col_int=t2.col_int);
SET optimizer_switch='semijoin=off';
SELECT id FROM bug_db.bug_t t1 WHERE EXISTS (SELECT 1 FROM bug_db.bug_t t2 WHERE t1.id > t2.id AND t1.col_str=t2.col_str AND t1.col_int=t2.col_int);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110819_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_004/mysql-110819-8.0.33/results/records.jsonl#L1)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_110847_8_0_33_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-110847-8.0.33.sql)；SHA256：`c5b3b43bd6f65d90cf5d645eff7ae24d33fea1053da272b85fb4f6d53aed9061`。

```sql
CREATE DATABASE IF NOT EXISTS window_lag_bug;
USE window_lag_bug; 
DROP TABLE IF EXISTS `data_table`;
CREATE TABLE IF NOT EXISTS `data_table` (`uid` INT) ENGINE=InnoDB;
INSERT INTO `data_table` (`uid`) VALUES (100), (101);

PREPARE stmt1 FROM "SELECT (LAST_VALUE(a.`uid`) OVER `outer_window`) = a.`uid` as `result`
FROM 
	(	
		SELECT 
		LAG(`uid`) OVER `inner_window` AS `uid_lag`,
		`uid` AS `uid`
		FROM data_table
		WINDOW `inner_window` AS (ORDER BY `uid`)
	) AS a 
	WINDOW `outer_window` AS (ORDER BY a.`uid`)
";
EXECUTE stmt1;
EXECUTE stmt1;
SELECT VERSION();
DROP DATABASE window_lag_bug;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_110847_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:157](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L157)
- `candidate_110847_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:158](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L158)
- `candidate_110847_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:159](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L159)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110915_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110915-8.0.33.sql)；SHA256：`bf1cdfafb3002a004b134dc7d29be18779c8c16de66f0685514ed6205431f34e`。

```sql
-- MySQL report #110915; source anchors: cmain, c532281
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE t0(c0 INT,c1 INT,c2 INT);
CREATE TABLE t7(c0 INT,c1 INT,c2 INT);
SELECT 1 FROM t0 JOIN t7 ON TRUE GROUP BY t7.c0,t0.c0 HAVING t7.c0=1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110915_8_0_33_r1`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_110962_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-110962-8.0.33.sql)；SHA256：`d53e871fa41c3569f123bd9d2bbb2640231e621333abb76401c95230fbf4a580`。

```sql
-- MySQL report #110962; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
set sql_mode = "";




CREATE TABLE `s1` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) NOT NULL,
  `p_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1;

CREATE TABLE `t1` (
  `i` int(11) DEFAULT NULL
) ENGINE=InnoDB;

INSERT INTO s1 (p_id, s_id) VALUES (1, 1);
INSERT INTO s1 (p_id, s_id) VALUES (1, 1);
SELECT * FROM s1;

INSERT INTO t1 VALUES (1);
DELIMITER ;;
CREATE TRIGGER trg_s1 before INSERT ON `s1` FOR EACH ROW
IF 1 THEN
SET @sum = @sum + 1;
END IF ;;
DELIMITER ;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=0, null, p_id) WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, null, p_id) WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, 3, p_id) WHERE t.i=1;
SHOW WARNINGS;
select * from  t1 t JOIN s1 s ON s.s_id =t.i WHERE t.i=1;
SHOW WARNINGS;
UPDATE t1 t JOIN s1 s ON s.s_id =t.i SET p_id = IF(1=1, 3, p_id) WHERE t.i=1;
show warnings;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110962_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b002_8_0_33/results/records.jsonl#L1)
- `target_110962_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b005_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_110983_8_0_33_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-110983-8.0.33.sql)；SHA256：`550eac49593a675f236dad80a3cec1563c59f6747f2a047648558e0eccd6a7fc`。

```sql
CREATE TABLE table1(id INT);
INSERT INTO table1 VALUES(1),(2),(3),(4),(5),(6),(7),(8),(9),(10),(11),(12);
DELIMITER $$
CREATE PROCEDURE test2()
BEGIN
SELECT count(*) over(rows between 5 preceding and 5 following) AS A,
count(*) over(rows between 5 preceding and 5 following)+1 AS Aplus,
count(*) over() AS B, count(*) over()+1 AS Bplus FROM table1;
END$$
DELIMITER ;
CALL test2();
CALL test2();
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_110983_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:166](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L166)
- `candidate_110983_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:167](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L167)
- `candidate_110983_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:168](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L168)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_110984_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-110984-8.0.33.sql)；SHA256：`ae50e8c09aaecd2f4953e3bf9c9d6983eeb1820dbf20c1390521524320f72bac`。

```sql
-- MySQL report #110984; source anchors: cmain, c544757
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;
CREATE TABLE t1(flowid VARCHAR(32)) CHARSET=gbk COLLATE=gbk_bin;
INSERT INTO t1 VALUES('xxx');
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1) AS alias;
SELECT CONCAT(abc,flowid) FROM (SELECT 'yyy-' AS abc,flowid FROM t1 LIMIT 1) AS alias;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_110984_8_0_33_r1`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111067_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111067-8.0.33.sql)；SHA256：`981da26e89fa63dde72fa97ba57654734a2666818b2e9ff08ea34473e77c15a8`。

```sql
-- MySQL report #111067; source anchors: cmain, c532705
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a CHAR(10), fulltext(a)) ENGINE = InnoDB;
INSERT INTO t1 VALUES('aaa15');
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ALTER TABLE t1 ADD COLUMN y INT;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
ANALYZE TABLE t1;
SELECT MATCH(a) AGAINST('aaa1* aaa14 aaa16' IN BOOLEAN MODE) FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111067_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b002_8_0_33/results/records.jsonl#L2)
- `target_111067_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b005_8_0_33/results/records.jsonl#L2)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_111094_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-111094-8.0.33.sql)；SHA256：`43fcfbfe45bdf29964734386dcdf454669fc09865339b30599f4f5cdce6e4b5e`。

```sql
-- Report #111094; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE order_test (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	val varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_cs NOT NULL,
	PRIMARY KEY (id),
	KEY val(val)
);

INSERT INTO order_test (val) VALUES ('Wä'), ('E');

-- Incorrect order
SELECT *, val = 'wä', val = 'Wä', val = 'E'
FROM order_test
ORDER BY val = 'wä' DESC, val = 'Wä' DESC, val = 'E' DESC;

-- Expected order control
SELECT *, val = 'ka', val = 'Wä', val = 'E'
FROM order_test
ORDER BY val = 'ka' DESC, val = 'Wä' DESC, val = 'E' DESC;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111094_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111268_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111268-8.0.33.sql)；SHA256：`d52266731b46d957da2452f70984900092e2ed72abb9413ba2eb9195f874bbf9`。

```sql
-- MySQL report #111268; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t(id INT,c1 VARCHAR(10) COLLATE utf8mb4_bin) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
INSERT INTO t VALUES(1,'abc'),(2,'abc ');
SET character_set_connection=utf8mb3;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';
SET character_set_connection=utf8mb4;
SELECT * FROM t WHERE c1='abc' AND c1='abc ';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111268_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L6)
- `target_111268_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b003_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111272_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111272-8.0.33.sql)；SHA256：`9337a13bcfeb5db00d4aa506dea161301d133c51ba62b18c697a512b71d73aa5`。

```sql
-- MySQL report #111272; source anchors: cmain, c533174
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET NAMES utf8mb4;
-- case 1
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT, KEY i0 (c1(1)));
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 1

-- case 2
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (c1 TINYTEXT);
INSERT INTO t1 VALUES ("͕fB-'"),("^1o");
SELECT c1 FROM t1 WHERE c1 > ("?ykFo|1"); -- 2
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111272_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b002_8_0_33/results/records.jsonl#L3)
- `target_111272_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b005_8_0_33/results/records.jsonl#L3)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_111290_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-111290-8.0.33.sql)；SHA256：`4151b87f7ab433e3c79edda77ce65535005735287cf83e5ef51b2cab6922ad2e`。

```sql
-- MySQL report #111290; source anchors: cmain, c533278, c535147
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
DROP TABLE IF EXISTS `foos`;
DROP TABLE IF EXISTS `bars`;
DROP TABLE IF EXISTS `parents`;

CREATE TABLE `parents` (
  `id` binary(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `foos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `parent_id` varbinary(16) NOT NULL,
  `text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_foos_on_parent_id` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12345 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

CREATE TABLE `bars` (
  `id` binary(16) NOT NULL,
  `parent_id` varbinary(16) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_bars_on_parent_id` (`parent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- Create some test data
INSERT INTO parents VALUES (0x93222796caba43ca979f5c96eb6898b7);
INSERT INTO foos (parent_id, text) SELECT parents.id, 'correct output' FROM parents;
INSERT INTO bars (id, parent_id) SELECT 0x79cea9ab6fe14a8ebdfed711a7727763, parents.id FROM parents;

-- Reproduce the problem:
SELECT foos.text
FROM foos
JOIN parents ON parents.id = foos.parent_id
JOIN bars ON bars.parent_id = parents.id
WHERE bars.parent_id = 0x93222796caba43ca979f5c96eb6898b7;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111290_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L4)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_111421_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-111421-8.0.33.sql)；SHA256：`dfb623557b25c8e910a6471ea268d5ec89fdd7a44d63cd94fa660d14764348c5`。

```sql
-- MySQL report #111421; source: cmain, c533592
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c1 NUMERIC CHECK (true));
SHOW CREATE TABLE t0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111421_8_0_33_r1`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_1/b003_8_0_33/results/records.jsonl#L5)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111429_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111429-8.0.33.sql)；SHA256：`ee8fbe1997d03bb28ba58f60a5c43a621c299d7045a5b07ee8ef71df70088bbc`。

```sql
-- MySQL report #111429; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET time_zone='+00:00';
CREATE TABLE bugtest (
  `id_col` int NOT NULL AUTO_INCREMENT,
  `timestamp_col` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
   `binary_col` binary(11) DEFAULT NULL,
   UNIQUE KEY (`id_col`),
   KEY `ndx_timestamp_col` (`timestamp_col`),
   KEY `ndx_binary_col` (`binary_col`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO bugtest VALUES (1,'1995-03-04 12:20:00.000000',_binary 'aaa'), (2,'1996-03-04 12:20:00.000000',_binary 'bbb'), (3,'1997-03-04 12:20:00.000000',NULL), (4,'1998-03-04 12:20:00.000000',NULL), (5,'1999-03-04 12:20:00.000000',NULL);

SELECT binary_col,timestamp_col FROM bugtest WHERE (binary_col,timestamp_col) <=> (NULL,'1997-03-04 12:20:00.000000') ORDER BY 1 limit 10;

SELECT binary_col,timestamp_col FROM bugtest WHERE (binary_col,timestamp_col) <=> (SELECT binary_col,timestamp_col FROM bugtest ORDER BY 1,2 LIMIT 1) ORDER BY 1 limit 10;

SELECT binary_col,timestamp_col FROM bugtest ORDER BY 1,2 LIMIT 1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111429_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:6](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L6)
- `target_111429_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:6](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111484_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111484-8.0.33.sql)；SHA256：`f6b6fed90f16eba37904ddd9df7ed6ebee670f00b905fcd6f0435decb246adb8`。

```sql
-- MySQL report #111484; source: cmain, c533732
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION optimizer_switch='subquery_to_derived=off';
create table t_doc (id int, doc JSON );
insert into t_doc values
  (1, '{"match11": "eleven", "match12": "element", "notMatch": "elven" }' ),
  (2, '{"match21": "eleven", "match22": "element", "notMatch": "elven" }' ),
  (3, '{"match31": "tw%elve", "match32": "tw%ilight", "notMatch": "twitter" }' );

create table t_search_string (id int, search_string varchar(20) );
insert into t_search_string values
  (1, 'ele%' ),
  (2, 'ele%' ),
  (3, 'tw|%%' );

select t.id, json_search( doc, 'all', (select search_string from t_search_string s where s.id = t.id), '|' )
from t_doc t order by id;
SET SESSION optimizer_switch='subquery_to_derived=on';
select t.id, json_search( doc, 'all', (select search_string from t_search_string s where s.id = t.id), '|' ) from t_doc t order by id;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111484_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L1)
- `target_111484_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_111559_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-111559-8.0.33.sql)；SHA256：`5256f04bbcc7cb02ebcfba4af174fd312223958cae01ca318aa7e7adc091134b`。

```sql
-- MySQL report #111559; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE VIEW v0 (c0) AS (WITH x(x) AS (SELECT 1), y(y) AS (SELECT 1) SELECT 1 FROM x);
SELECT 1 FROM v0;
SHOW CREATE VIEW v0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111559_8_0_33_r1`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:2](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111699_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111699-8.0.33.sql)；SHA256：`1ac9baa1a1c9181de1f80462d394fb7f60f05c9c30e0b888e3a6aaf15ed25118`。

```sql
-- MySQL report #111699; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t0` (
  `c0` text
);

CREATE TABLE `t1` (
  `c0` tinyint(3) unsigned zerofill,
  `c1` float DEFAULT NULL,
  UNIQUE KEY `c0` (`c0`)
);

INSERT INTO `t0` VALUES ('292269042'),(''),(NULL),('IcK5A'),(NULL),('z)]s'),('292269042'),('4f*T');

INSERT INTO `t1` VALUES (255,NULL),(NULL,0),(NULL,292269000),(000,NULL),(NULL,NULL);
SET optimizer_switch='subquery_to_derived=on';
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t1.c1 IN (SELECT t0.c0 AS ref1 FROM t0 )) OR (t0.c0);
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t1.c1 IN (SELECT t0.c0 AS ref1 FROM t0 ));
SELECT t1.c0 AS ref0 FROM t1 LEFT OUTER JOIN t0 ON t1.c1 = t0.c0 WHERE (t0.c0);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111699_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b002_8_0_33/results/records.jsonl#L4)
- `target_111699_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b005_8_0_33/results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111706_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111706-8.0.33.sql)；SHA256：`7eb5355ebddf6e49273169ac4ab47196a2e62b9950619bbc4adf5e4113475f46`。

```sql
-- MySQL report #111706; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t0` (
  `c0` text
);

CREATE TABLE `t1` (
  `c0` tinyint(3) unsigned zerofill,
  `c1` float DEFAULT NULL,
  UNIQUE KEY `c0` (`c0`)
);

INSERT INTO `t0` VALUES ('292269042'),(''),(NULL),('IcK5A'),(NULL),('z)]s'),('292269042'),('4f*T');

INSERT INTO `t1` VALUES (255,NULL),(NULL,0),(NULL,292269000),(000,NULL),(NULL,NULL);
SET optimizer_switch='subquery_to_derived=off';
SELECT * FROM t1 LEFT OUTER JOIN t0 ON t1.c1=t0.c0 WHERE t1.c1 IN (SELECT MIN(tin.c0) FROM t0 AS tin GROUP BY c0);
SET optimizer_switch='subquery_to_derived=on';
SELECT * FROM t1 LEFT OUTER JOIN t0 ON t1.c1=t0.c0 WHERE t1.c1 IN (SELECT MIN(tin.c0) FROM t0 AS tin GROUP BY c0);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111706_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L2)
- `target_111706_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111728_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111728-8.0.33.sql)；SHA256：`8a7d669e69f4a0f643d7b50a9c0ece83065f4b2aaf3d81342b330fe630de44cd`。

```sql
-- Report #111728; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE ta(id BIGINT,PRIMARY KEY(id));
INSERT INTO ta(id) VALUES(1801425248110076165);
CREATE TABLE tb(value VARCHAR(50));
INSERT INTO tb(value) VALUES("1801425248110076222");
SELECT value FROM tb WHERE value IN(SELECT id FROM ta);
SELECT value FROM tb WHERE value IN(SELECT /*+no_index(ta)*/ id FROM ta);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111728_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L3)
- `target_111728_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111737_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111737-8.0.33.sql)；SHA256：`e21144f6869de0feb07f57322af3204eecb1ee76d3403e376ba58d93108efed3`。

```sql
-- MySQL report #111737; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE TABLE tab(col VARCHAR(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,CONSTRAINT cons CHECK(col REGEXP '''+')) ENGINE=InnoDB;
DROP TABLE tab;
SET sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION,NO_BACKSLASH_ESCAPES';
CREATE TABLE tab(col VARCHAR(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,CONSTRAINT cons CHECK(col REGEXP '''+')) ENGINE=InnoDB;
SELECT 'aaa' REGEXP '''+';
SELECT 'a''aa' REGEXP '''+';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111737_8_0_33_r1`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b002_8_0_33/results/records.jsonl#L5)
- `target_111737_8_0_33_r2`，实际版本 8.0.33，completed_with_sql_errors；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b005_8_0_33/results/records.jsonl#L5)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112231_8_0_33_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-112231-8.0.33.sql)；SHA256：`9f19682601cca5cfe9a5b3b69b4e24e5b7952c95fb7ec7f260e3b5d73e2c912d`。

```sql
DROP TEMPORARY TABLE IF EXISTS tbTestBad2;
CREATE TEMPORARY TABLE tbTestBad2 (id int unsigned) ENGINE InnoDB;
INSERT INTO tbTestBad2 SELECT 1 AS id;

DROP PROCEDURE IF EXISTS spTestBad;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS spTestBad()
  BEGIN
    SELECT 1, (SUM( 1 ) OVER()) + 0 FROM tbTestBad2 ;
    SELECT * FROM tbTestBad2;
  END$$
DELIMITER ;

CALL spTestBad();
CALL spTestBad();
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112231_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:175](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L175)
- `candidate_112231_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:176](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L176)
- `candidate_112231_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:177](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L177)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112460_8_0_33_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-112460-8.0.33.sql)；SHA256：`ec07f399b75c41b712de132bbc2ad717567e88317b1cbf27b8c5d93b80454677`。

```sql


create table t2 (vkey int, pkey int, c19 int, c20 double, c22 int);
insert into t2 values (135, 145000, -13, 17.61, 0);


select  
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0, 
  case when ((LAST_VALUE(ref_0.pkey) over (partition by ref_0.c19 order by ref_0.vkey desc, ref_0.pkey desc)) in (select  
          ref_0.c22 as c_0
        from 
          t2 as ref_8
        )) then ref_0.c20 else ref_0.c20 end
       as c_1 
from 
  t2 as ref_0
order by c_1 desc;
select
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0,
  ref_0.c20 as c_1
from
  t2 as ref_0
order by c_1 desc;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112460_8_0_33_target_r1`，实际版本 8.0.33，completed；[records.jsonl:184](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L184)
- `candidate_112460_8_0_33_target_r2`，实际版本 8.0.33，completed；[records.jsonl:185](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L185)
- `candidate_112460_8_0_33_target_r3`，实际版本 8.0.33，completed；[records.jsonl:186](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L186)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113061_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113061-8.0.33.sql)；SHA256：`7e10c2c4f542d686fdf4881e199dfc9dfcf98b284a86dc52aa35ab42b955ac0e`。

```sql
-- MySQL report #113061; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t1` (
  `a` int(11) NOT NULL AUTO_INCREMENT,
  `b` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `c` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`a`),
  KEY `idx_b_l` (`b`),
  KEY `idx_c_l` (`c`)
);

insert into t1(b,c) values ('6RXmcRyA48c0yvZ2I' ,'6RXmcRyA48c0yvZ2I');
insert into t1(b,c) values ('G6UHU26b8dkvwpYiM' ,'G6UHU26b8dkvwpYiM');
insert into t1(b,c) values ('0XS2E55maqch' ,'0XS2E55maqch');
insert into t1(b,c) values ('0qwCMwobKYOcmLyfRXlagA8ukENJv' ,'0qwCMwobKYOcmLyfRXlagA8ukENJv');
insert into t1(b,c) values ('3avxIDL4YPrZVHie4rOiPrK8ZIJwEPqZaioHK' ,'3avxIDL4YPrZVHie4rOiPrK8ZIJwEPqZaioHK');
insert into t1(b,c) values ('5DHC2QScT6P6lXgRtHajXOfztB7ddjYH1LLUC3' ,'5DHC2QScT6P6lXgRtHajXOfztB7ddjYH1LLUC3');
insert into t1(b,c) values ('5pdGQ2NTM3c2uRgCg9NspSE' ,'5pdGQ2NTM3c2uRgCg9NspSE');
insert into t1(b,c) values ('6Bk06GVtwZaKqg01' ,'6Bk06GVtwZaKqg01');
insert into t1(b,c) values ('6VFO4xJPwvxGzReYzVj6dwTSIechnSSCyz9iY' ,'6VFO4xJPwvxGzReYzVj6dwTSIechnSSCyz9iY');
insert into t1(b,c) values ('6hLBs3Rnd5elLLVv1ip3A2U6G1dkIApKDkiCy' ,'6hLBs3Rnd5elLLVv1ip3A2U6G1dkIApKDkiCy');


select avg(distinct b) from t1 force index(primary);
select avg(distinct b) from t1;
select sum(distinct b) from t1 force index(primary);
select sum(distinct b) from t1;
SELECT DISTINCT b,b+0 FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113061_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L4)
- `target_113061_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113180_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113180-8.0.33.sql)；SHA256：`3d684c4086b5e384f172ee9750314c66cdafb75fb8ad8e1858b2ba649e841747`。

```sql
-- MySQL report #113180; source: cmain, c538271, c538297
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT, c1 INT, PRIMARY KEY(c0));
INSERT INTO t0(c0, c1) VALUES (1, 0);
CREATE UNIQUE INDEX i1 ON t0(c1 , c0 );

SELECT * FROM t0 WHERE SIN(1150199883)=c1; -- 1 0
SELECT * FROM t0 WHERE NOT SIN(1150199883)=c1; -- 1 0
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113180_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:7](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L7)
- `target_113180_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:7](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L7)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113298_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113298-8.0.33.sql)；SHA256：`8721f79806ab7291909b91680646707ee8ff864531cdabfc6de94554b23bb23c`。

```sql
-- MySQL report #113298; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0( c1 INTEGER);
INSERT INTO t0 (c1) VALUES (1);
CREATE INDEX i0 ON t0(c1  );

SELECT * FROM t0 WHERE (1/1.5 IN (c1)); -- 1
SELECT * FROM t0 WHERE (NOT (1/1.5 IN (c1))); -- 1

ALTER TABLE t0 DROP INDEX i0;
SELECT * FROM t0 WHERE (1/1.5 IN(c1));
SELECT * FROM t0 WHERE NOT(1/1.5 IN(c1));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113298_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L5)
- `target_113298_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L5)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113319_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113319-8.0.33.sql)；SHA256：`8950b345f19cbdeafd261ce04be0659d4f5afd62bf4a1247542ac5677db558b6`。

```sql
-- MySQL report #113319; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a INT); CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1),(2),(3),(4); INSERT INTO t2 VALUES(1),(2);
SET optimizer_switch='subquery_to_derived=off';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
SET optimizer_switch='subquery_to_derived=on';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113319_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L6)
- `target_113319_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114714_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114714-8.0.33.sql)；SHA256：`60eae9fb11ec02b91391b08144415d179222c263cb47d0e3345ea9a84747a4e9`。

```sql
-- MySQL report #114714; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1 (a INT, b INT);
INSERT INTO t1 VALUES (4, 40), (1, 10), (2, 20), (2, 20), (3, 30);

CREATE TABLE t2 SELECT DISTINCT a FROM t1;

ANALYZE TABLE t1, t2;


 EXPLAIN FORMAT=TREE SELECT (SELECT t2.a FROM t2 WHERE t2.a = t1.a) aa, b, COUNT(b) FROM t1 GROUP BY aa, b ORDER BY -aa, -b;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114714_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b001_8_0_33/results/records.jsonl#L2)
- `target_114714_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b012_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_116703_8_0_33_r1。

[下载独立 SQL](sql/reproduced_106/mysql-116703-8.0.33.sql)；SHA256：`3a92e1b91d3987beb7697ec48fc061509d6c10201e99376c4211408838e5654e`。

```sql
-- MySQL report #116703; source: cmain, c548706
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(col INT);
INSERT INTO t VALUES(NULL);
SELECT JSON_VALID(t.col) FROM t;
SELECT JSON_VALID(NULL);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_116703_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:3](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_119630_8_0_33_r2。

[下载独立 SQL](sql/reproduced_106/mysql-119630-8.0.33.sql)；SHA256：`309cf56b153d9baa937c0953d63357cf3c5a07203b70507ad114681860ed4ae4`。

```sql
-- MySQL report #119630; source: cmain, c555462, c555698, c555719
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
-- Step 1: Create test tables
DROP TABLE IF EXISTS t_bug_mat1, t_bug_mat2;
CREATE TABLE t_bug_mat1 (id INT, val INT);
CREATE TABLE t_bug_mat2 (id VARCHAR(20), num_val INT);
INSERT INTO t_bug_mat1 VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t_bug_mat2 VALUES ('1', 10), ('2', 25), ('4', 40);


SELECT id, val FROM t_bug_mat1 
WHERE id IN (SELECT CAST(id AS UNSIGNED) FROM t_bug_mat2 WHERE num_val > 15)
ORDER BY id;
SELECT t1.id, t1.val  FROM t_bug_mat1 t1 WHERE t1.id IN (   SELECT /*+ NO_MERGE(subq) */ casted_id FROM (     SELECT CAST(id AS UNSIGNED) AS casted_id      FROM t_bug_mat2      WHERE num_val > 15   ) AS subq ) ORDER BY t1.id;
SELECT t1.id, t1.val FROM t_bug_mat1 t1 WHERE t1.id IN (   SELECT casted_id FROM (     SELECT CAST(id AS UNSIGNED) AS casted_id FROM t_bug_mat2 WHERE num_val > 15   ) AS subq ) ORDER BY t1.id;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_119630_8_0_33_r1`，实际版本 8.0.33，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b002_8_0_33/results/records.jsonl#L7)
- `target_119630_8_0_33_r2`，实际版本 8.0.33，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b007_8_0_33/results/records.jsonl#L7)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_119646_8_0_33_repair_v2_r1。

[下载独立 SQL](sql/reproduced_106/mysql-119646-8.0.33.sql)；SHA256：`ee2a214801f790ed5fb9f9fc274366ad3752af94a324e5b9a74a079ef077bc12`。

本项曾执行多个输入版本，全部保留：

- [ee2a214801f790ed5fb9f9fc274366ad3752af94a324e5b9a74a079ef077bc12](sql/executed_125/mysql-119646-8.0.33.sql)
- [f2fbd86d00bbd3693afff1340e473fc17b865071a600378c1bbbc0bd896a6a89](sql/executed_125/mysql-119646-8.0.33-f2fbd86d00bb.sql)

```sql
-- Report #119646; source anchors: cmain, c555476, c555720
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_optimizer=@@session.optimizer_switch;
DROP TABLE IF EXISTS t_main, t_ref;
CREATE TABLE t_main (id INT, val INT);
CREATE TABLE t_ref (id VARCHAR(10), ref_id INT, val INT);
INSERT INTO t_main VALUES (1, 10), (2, 20), (3, 30);
INSERT INTO t_ref VALUES ('1', 1, 100), ('2', 2, 200), ('3', 3, 300);

CREATE OR REPLACE VIEW v_test AS
SELECT CAST(r.id AS UNSIGNED) AS casted_id
FROM t_ref r 
WHERE r.val > 150;

SELECT m.id, m.val
FROM t_main m
WHERE m.id IN (SELECT casted_id FROM v_test)
ORDER BY m.id;
-- Result: `id=2, val=20; id=3, val=30` (2 rows)
SET SESSION optimizer_switch='semijoin=off,derived_merge=off';
SELECT m.id, m.val
FROM t_main m
WHERE m.id IN (SELECT casted_id FROM v_test)
ORDER BY m.id;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_119646_8_0_33_r1`，实际版本 8.0.33，client_error；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b001_8_0_33/results/records.jsonl#L3)
- `target_119646_8_0_33_repair_v2_r1`，实际版本 8.0.33，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_7/b001_8_0_33/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_79813_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-79813-8.0.34.sql)；SHA256：`048934fe87d77de5ff4a6c69ac076c3d74890599a5a86d9ce759917635378360`。

```sql
CREATE DATABASE temp;
USE temp;
CREATE TABLE temp.user (user_id INT(11) UNSIGNED NOT NULL,department_id INT(11) UNSIGNED NOT NULL,user_name VARCHAR(32) DEFAULT NULL,is_active BOOL NOT NULL DEFAULT 1);
INSERT INTO temp.user (user_id,department_id,user_name,is_active) VALUES (1,1,'test user 1',TRUE),(2,1,'test user 2',FALSE),(3,2,'test user 3',TRUE);
SELECT JSON_OBJECT('can_edit',IF(user.is_active = "1",TRUE,FALSE),'is_true',TRUE,'is_false',FALSE) AS exception_comments FROM temp.user;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_79813_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_003/mysql-79813-8.0.34/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_111918_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-111918-8.0.34.sql)；SHA256：`f02ef5773033f662b4ff6b1b89caf75144281c3684d7d982705efc34155ba0a6`。

```sql
-- MySQL report #111918; source: cmain, c534860
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t1 (c0 INT AUTO_INCREMENT UNIQUE KEY);
INSERT INTO t1 VALUES ();
INSERT IGNORE INTO t1 VALUES ();

SELECT 1 FROM t1;
 -- 2 rows
SELECT 1 FROM t1 WHERE (t1.c0 > CAST(X'0B36' AS CHAR));
 -- empty
SELECT 1 FROM t1 WHERE (NOT (t1.c0 > CAST(X'0B36' AS CHAR)));
 -- empty
SELECT 1 FROM t1 WHERE ((t1.c0 > CAST(X'0B36' AS CHAR)) IS NULL);
 -- empty
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_111918_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L4)
- `target_111918_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112037_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112037-8.0.34.sql)；SHA256：`80244524e0223fd701016c298f6cd5fc9a6176f413bea29b8a41060be585e438`。

```sql
-- MySQL report #112037; source: cmain, c535234
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t1(a INT);
INSERT INTO t1 VALUES (1),(2),(3),(4);
ANALYZE TABLE t1;
SET optimizer_switch='subquery_to_derived=on';
EXPLAIN analyze SELECT a + (SELECT SUM(a) FROM (SELECT a FROM t1 GROUP BY a) t2 ) FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112037_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L5)
- `target_112037_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112147_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112147-8.0.34.sql)；SHA256：`5491c511c068a2763c8b2d7c54ae8fbb186e93a46fdbffcee23e6f28f71cac75`。

```sql
-- Report #112147; source anchors: cmain, c535553, c535600
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t(a INT,j JSON,INDEX kj((CAST(j AS DATE ARRAY))));
INSERT INTO t VALUES(1,JSON_ARRAY(CAST("2010-10-10" AS DATE),CAST("2010-10-10" AS DATE)));
SELECT * FROM t USE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE "2010-10-10" MEMBER OF(j);
SELECT * FROM t IGNORE INDEX(kj) WHERE DATE'2010-10-10' MEMBER OF(j);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112147_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b003_8_0_34/results/records.jsonl#L3)
- `target_112147_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b008_8_0_34/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112198_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112198-8.0.34.sql)；SHA256：`860d1436207f04c7efc1edd1d421a14dcd10a62dfeab06efc1f73ca3d26d1c4d`。

```sql
CREATE TABLE t1(a int,b int,c varchar(100));
CREATE TABLE t2(a int,b int,c varchar(100));
EXPLAIN FORMAT=TREE SELECT * FROM t1 LEFT JOIN t2 ON t1.a=t2.a AND t2.a>0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112198_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_006/mysql-112198-8.0.34/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112212_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112212-8.0.34.sql)；SHA256：`c407e87df363b1873a31ea53141d87ea1876da2e026c02d99e1dafc8d6a3b2af`。

```sql
-- MySQL report #112212; source: cmain, c535747
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION optimizer_switch='subquery_to_derived=off';
CREATE TABLE type1(c1 bit(8), c2 json, c3 int, c4 json);
INSERT INTO type1 VALUES(b'1010', '{"key1": "value1", "key2": "value2"}', 1, '["key1"]');
INSERT INTO type1 VALUES(b'1011', '{"key1": "value1", "key2": "value2"}', 2, '["key2", "key22"]');
INSERT INTO type1 VALUES(b'1111', '{"key3": "value3", "key3": "value3"}', 3, '{"key3": 3}');
INSERT INTO type1 VALUES(null, null, null, '["key4"]');
CREATE TABLE type2(c1 bit(8), c2 json, c3 int, c4 varchar(20));
INSERT INTO type2 VALUES(b'1010', '{"key1": "value1", "key2": "value2"}', 1, "key1");
INSERT INTO type2 VALUES(b'1100', '{"key2": "value2", "key2": "value2"}', 2, "key2");
INSERT INTO type2 VALUES(b'1100', '{"key2": "value2", "key2": "value2"}', 2, "key22");
INSERT INTO type2 VALUES(b'1111', '{"key3": "value3", "key3": "value3"}', 3, "key3");
INSERT INTO type2 VALUES(null, null, null, "key4");

SELECT BIN(c1), c3 FROM type1 where c2 = (select var_pop(c2) from type2 where type2.c1 = type1.c1);

set @@optimizer_switch='subquery_to_derived=on';

SELECT BIN(c1), c3 FROM type1 where c2 = (select var_pop(c2) from type2 where type2.c1 = type1.c1);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112212_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L6)
- `target_112212_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L3)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112231_8_0_34_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-112231-8.0.34.sql)；SHA256：`9f19682601cca5cfe9a5b3b69b4e24e5b7952c95fb7ec7f260e3b5d73e2c912d`。

```sql
DROP TEMPORARY TABLE IF EXISTS tbTestBad2;
CREATE TEMPORARY TABLE tbTestBad2 (id int unsigned) ENGINE InnoDB;
INSERT INTO tbTestBad2 SELECT 1 AS id;

DROP PROCEDURE IF EXISTS spTestBad;

DELIMITER $$
CREATE PROCEDURE IF NOT EXISTS spTestBad()
  BEGIN
    SELECT 1, (SUM( 1 ) OVER()) + 0 FROM tbTestBad2 ;
    SELECT * FROM tbTestBad2;
  END$$
DELIMITER ;

CALL spTestBad();
CALL spTestBad();
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112231_8_0_34_target_r1`，实际版本 8.0.34，completed；[records.jsonl:268](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L268)
- `candidate_112231_8_0_34_target_r2`，实际版本 8.0.34，completed；[records.jsonl:269](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L269)
- `candidate_112231_8_0_34_target_r3`，实际版本 8.0.34，completed；[records.jsonl:270](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L270)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112242_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112242-8.0.34.sql)；SHA256：`f6168796b4265c7e800bb950ee944ec62c3e73ff05441d312844fe402637da96`。

```sql
-- MySQL report #112242; source: cmain, c535808
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
CREATE TABLE t0(c0 INT);
INSERT INTO t0(c0) VALUES(1);
CREATE INDEX i0 USING HASH ON t0(c0) INVISIBLE;

SET SESSION optimizer_switch = 'use_invisible_indexes=off';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0); -- {}
SET SESSION optimizer_switch = 'use_invisible_indexes=on';
SELECT t0.c0 FROM t0 WHERE COALESCE(0.6) IN (t0.c0);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112242_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112269_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112269-8.0.34.sql)；SHA256：`19a46ad336f48c2ceb1624cb63c73ee4713645abc42afd096e72fe61bea0e9ce`。

```sql
-- MySQL report #112269; source: cmain, c535878
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 DECIMAL UNIQUE);
CREATE TABLE t2(c0 FLOAT, c1 TEXT);
CREATE INDEX i0 ON t2(c1(1));

INSERT INTO t0 VALUES(1);
INSERT INTO t2 VALUES(NULL, '1j');

SELECT * FROM t0, t2 WHERE t2.c1 = t0.c0;  -- {1|NULL|1j}
SELECT /*+ JOIN_ORDER(t2, t0)*/ * FROM t0, t2 WHERE t2.c1 = t0.c0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112269_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L7)
- `target_112269_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L4)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112275_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112275-8.0.34.sql)；SHA256：`7c61c25396bbd3380fdf80fee90ce5ccc51cb55353ead47155b4057ffd3df77c`。

```sql
-- MySQL report #112275; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TEMPORARY TABLE temp(id INTEGER,name VARCHAR(100));
CREATE TABLE normal(id INTEGER,name VARCHAR(100));
SHOW COLUMNS FROM temp;
SHOW COLUMNS FROM normal;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112275_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112293_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112293-8.0.34.sql)；SHA256：`fe67df94c572dca8d448022e5180f0880eb77ac773cbd298d6a0bc87a98fa845`。

```sql
-- MySQL report #112293; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t` (
  `a` int(11) DEFAULT NULL,
  `b` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

insert into t values(1,'my_test　'),(2,'my_test');
SELECT HEX(b),b FROM t;
SELECT b FROM t WHERE b='my_test';
set internal_tmp_mem_storage_engine = TempTable;
select b,count(*) from t group by b;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112293_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b003_8_0_34/results/records.jsonl#L4)
- `target_112293_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b008_8_0_34/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112296_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112296-8.0.34.sql)；SHA256：`24a2ba9176e437566581742e9dc778a9ae9b0219eac1d9aa1f0b582ea5e2af68`。

```sql
-- MySQL report #112296; source: cmain, c535940, c539425
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
CREATE TABLE t1(c0 INT);
CREATE TABLE t2(c0 INT);
REPLACE INTO t0(c0) VALUES(1), (2);
INSERT INTO t2(c0) VALUES(3);

SELECT t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000); -- {NULL}
SELECT /*+ NO_BNL(t0)*/ t0.c0 FROM t0 LEFT JOIN t1 ON FALSE RIGHT JOIN t2 ON (t1.c0 IS NOT NULL) IN (t2.c0 = 1000);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112296_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L8)
- `target_112296_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L5)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112306_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112306-8.0.34.sql)；SHA256：`3a6b5deb63b5c732a9fe83eb0731254f49ae32fa48e4d0e713ef119b2aa60cee`。

```sql
-- MySQL report #112306; source: cmain, c535975, c536008
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT);
CREATE TABLE t1(c0 INT);
CREATE TABLE t2(c0 INT, c1 INT, c2 INT);
CREATE TABLE t3(c0 INT, c1 INT, c2 INT);
INSERT IGNORE INTO t3 VALUES(1, 2, 0.1);
INSERT INTO t1 VALUES(-3);

SELECT COUNT(*) FROM t3, t2 INNER JOIN t0 ON t0.c0 RIGHT JOIN t1 ON FALSE WHERE (t0.c0 IS NOT NULL) = (BIT_COUNT(t3.c2)); -- {1}
SELECT /*+ JOIN_SUFFIX(t2, t3)*/ COUNT(*) FROM t3, t2 INNER JOIN t0 ON t0.c0 RIGHT JOIN t1 ON FALSE WHERE (t0.c0 IS NOT NULL) = (BIT_COUNT(t3.c2));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112306_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112387_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112387-8.0.34.sql)；SHA256：`f6db980e19657f28577b6e0bb678185083fa10e3ecdf2082806921afa7f73fc6`。

```sql
-- Report #112387; source anchors: cmain, c536188
-- Static preparation only; not executed. See case.json before any future isolated run.
create table t0 (c4 double);
create table t1 (c8 varchar(200));
insert into t1 values (null);
insert into t0 values (-66.49);
insert into t0 values (null);

-- Test case 1

select * from t0
where
not (null in (
    select 1 from (select 1) as subq where false
    union all
    select
        ref_5.c8 as c_0
      from
        t1 as ref_5
      where t0.c4 >= t0.c4));


-- Test case 2
select * from t0
where
not (null in (
    select
        ref_5.c8 as c_0
      from
        t1 as ref_5
      where t0.c4 >= t0.c4));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112387_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:9](../../experiments/saved_20261029/official_pending230_20261029/wave_2/b003_8_0_34/results/records.jsonl#L9)
- `target_112387_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b006_8_0_34/results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112439_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112439-8.0.34.sql)；SHA256：`bac460860b644a6364abc1f580e1acc61296d1f347e1aacf16dfe7e1161b4c3b`。

```sql
-- MySQL report #112439; source: cmain, c536279
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t(i INT PRIMARY KEY);
INSERT INTO t VALUES(1),(2),(3);
SELECT * FROM t WHERE i IN(VALUES ROW(1),ROW(2));
SELECT * FROM t WHERE i IN(SELECT 1 UNION SELECT 2);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112439_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:8](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L8)
- `target_112439_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:8](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L8)

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

目标版本实际执行 3 次；下列默认 SQL 对应 candidate_112460_8_0_34_target_r3。

[下载独立 SQL](sql/reproduced_106/mysql-112460-8.0.34.sql)；SHA256：`ec07f399b75c41b712de132bbc2ad717567e88317b1cbf27b8c5d93b80454677`。

```sql


create table t2 (vkey int, pkey int, c19 int, c20 double, c22 int);
insert into t2 values (135, 145000, -13, 17.61, 0);


select  
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0, 
  case when ((LAST_VALUE(ref_0.pkey) over (partition by ref_0.c19 order by ref_0.vkey desc, ref_0.pkey desc)) in (select  
          ref_0.c22 as c_0
        from 
          t2 as ref_8
        )) then ref_0.c20 else ref_0.c20 end
       as c_1 
from 
  t2 as ref_0
order by c_1 desc;
select
  case when true then null else (DENSE_RANK() over (partition by ref_0.pkey order by ref_0.vkey desc, ref_0.pkey asc)) end as c_0,
  ref_0.c20 as c_1
from
  t2 as ref_0
order by c_1 desc;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `candidate_112460_8_0_34_target_r1`，实际版本 8.0.34，completed；[records.jsonl:277](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L277)
- `candidate_112460_8_0_34_target_r2`，实际版本 8.0.34，completed；[records.jsonl:278](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L278)
- `candidate_112460_8_0_34_target_r3`，实际版本 8.0.34，completed；[records.jsonl:279](../../experiments/saved_20261029/execution/retrieved/mysql_replay_20261028_a/results/records.jsonl#L279)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112527_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112527-8.0.34.sql)；SHA256：`edf0da6458bcca406a7ede9f6961d1e4a4f14480543908a958aca0aac6020a31`。

```sql
-- Report #112527; source anchors: cmain, c536451
-- Static preparation only; not executed. See case.json before any future isolated run.
create table t1 (vkey int, pkey int);
insert into t1 values (3, 13000);
insert into t1 values (5, 15000);
insert into t1 values (28, 38000);

-- Query1

select  
  count(*) as c_1
from 
  t1 as ref_0
where (REPEAT(REPEAT(case when (null <= ref_0.vkey) then (null) else (case when false then ('o#W4O') else ('o#W4O') end) end, ref_0.vkey), ref_0.pkey)) >= 'i';


SHOW WARNINGS;


select  
  count(*) as c_1
from 
  t1 as ref_0
where (REPEAT(REPEAT(case when (null <= ref_0.vkey) then (null) else ('o#W4O') end, ref_0.vkey), ref_0.pkey)) >= 'i';


SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112527_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b003_8_0_34/results/records.jsonl#L6)
- `target_112527_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b008_8_0_34/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112557_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112557-8.0.34.sql)；SHA256：`e652b7e0e3354bdc3fdd797ea77fbca28373f74e8fe06351571a1c76910c7ff9`。

```sql
-- MySQL report #112557; source: cmain, c536507, c537445, c537488, c537535, c538930, c546013
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t1 (vkey int, pkey int, c5 int, c7 varchar(200));
insert into t1 values (20, 30000, 59, null);
insert into t1 values (59, 69000, null, null);
select  
  ref_0.c5 >= (case when (true and exists (
        select  
              ref_2.pkey as c_3
            from 
              t1 as ref_2
            where ref_2.vkey between ref_0.c5 and ref_0.c5
        )) then null else (case when (FIRST_VALUE('') over (partition by ref_0.c7 order by ref_0.vkey asc, ref_0.pkey desc) >= null) then null else ref_0.pkey end
        ) end
      ) as c_6
from 
  t1 as ref_0;
select  
  ref_0.c5 >= (case when (exists (
        select  
              ref_2.pkey as c_3
            from 
              t1 as ref_2
            where ref_2.vkey between ref_0.c5 and ref_0.c5
        )) then null else (case when (FIRST_VALUE('') over (partition by ref_0.c7 order by ref_0.vkey asc, ref_0.pkey desc) >= null) then null else ref_0.pkey end
        ) end
      ) as c_6
from 
  t1 as ref_0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112557_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b003_8_0_34/results/records.jsonl#L7)
- `target_112557_8_0_34_r2`，实际版本 8.0.34，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b008_8_0_34/results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112661_8_0_34_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112661-8.0.34.sql)；SHA256：`f38d1ecaf443123bd83543d170737d3dcd4a48159f707850b71c167f6b0752de`。

```sql
-- MySQL report #112661; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE table1 ( v0 TEXT NOT NULL , v1 TINYTEXT , v2 VARCHAR(255) DEFAULT 'v21' , v3 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , v4 TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , v5 FLOAT NOT NULL DEFAULT 1450916748.971549286 , v6 LONGTEXT NOT NULL , v7 DATE NOT NULL DEFAULT '1983-03-19 15:11:54.823209' ) ENGINE = ARCHIVE CHARACTER SET=latin1 COLLATE=latin1_bin;
CREATE INDEX index0 ON table1 (v4) USING BTREE;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112661_8_0_34_r1`，实际版本 8.0.34，completed_with_sql_errors；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b003_8_0_34/results/records.jsonl#L8)
- `target_112661_8_0_34_r2`，实际版本 8.0.34，completed_with_sql_errors；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b008_8_0_34/results/records.jsonl#L5)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_112737_8_0_34_r1。

[下载独立 SQL](sql/reproduced_106/mysql-112737-8.0.34.sql)；SHA256：`430abedb4ef004b10fef5ee6b62c4cb379dace16afa0eb00dae3dc0205cb7f11`。

```sql
CREATE TABLE t1(a INTEGER,b INTEGER,PRIMARY KEY(a));
CREATE TABLE t2(a INTEGER,b INTEGER,PRIMARY KEY(a,b));
INSERT INTO t1 VALUES(1,1),(2,2);
INSERT INTO t2 VALUES(2,1),(2,2),(2,3),(2,4);
ANALYZE TABLE t1,t2;
EXPLAIN FORMAT=TREE SELECT t1.b FROM t1 JOIN t2 WHERE t1.a=t2.a AND t2.a=2 AND t2.b>=t1.b AND t2.b<=t1.b+2;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112737_8_0_34_r1`，实际版本 8.0.34，completed；[records.jsonl:1](../../experiments/saved_20261029/final_targeted_20261029/retrieved/batch_006/mysql-112737-8.0.34/results/records.jsonl#L1)

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

目标版本实际执行 3 次；下列默认 SQL 对应 target_112910_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112910-8.0.35.sql)；SHA256：`8082e0692bbf3ee3e9d0487312baa31eb486920257a113866f37ee07f590f222`。

```sql
-- Report #112910; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
SELECT * FROM ( VALUES ROW ( 'a', 0 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: empty

SELECT * FROM ( VALUES ROW ( 'a', 0 ), ROW ( 'b', 1 ) ) t0 WHERE t0.column_1 = ( CAST( 1/16 AS DOUBLE PRECISION ) ) ; -- expected: empty, actually: 1 row
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112910_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:4](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L4)
- `target_112910_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:10](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L10)
- `target_112910_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:10](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L10)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_112911_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-112911-8.0.35.sql)；SHA256：`6ea3aba4c9886f4880a50cd9695ed3a7f0c14c55f7820f431e62db66b0a5fdf7`。

```sql
-- MySQL report #112911; source: cmain, c537525
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0 ( c0 INT, PRIMARY KEY ( c0 ) ) ;
CREATE VIEW v0 AS SELECT ra1.c0 ca1 FROM t0 ra0 INNER JOIN t0 ra1 ON ra1.c0 IN ( SELECT ra1.c0 ca0 FROM t0 ra2 ) ;
INSERT INTO t0 VALUES ( 1 ), ( -1 ) ;

SELECT COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 4
SELECT /*+ JOIN_ORDER(ra5, ra2, ra1, ra0) SEMIJOIN(DUPSWEEDOUT) */ COUNT(*) FROM t0 ra5 LEFT JOIN v0 ra6 ON ra6.ca1 = ra5.c0; -- result: 8
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_112911_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L1)
- `target_112911_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113097_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113097-8.0.35.sql)；SHA256：`c9bbba8d95f5b94d1ef2fc55e054f562fac7521f8ee3d9c95ab52ae1a65089a4`。

```sql
-- Report #113097; source anchors: cmain, c538086, c553120, c553157
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_optimizer=@@session.optimizer_switch;
CREATE TABLE temp (createdAt datetime, timezone varchar(64));

INSERT INTO temp VALUES ('2022-02-15 16:47:12', null);

SELECT
  *
FROM
  (
    SELECT
      coalesce(timezone, '+00:00') tz,
      convert_tz(createdAt, '+00:00', (select tz)) ca,
      if(createdAt, if((select 1) = 1, 1, 1), 1) random
    FROM temp
  ) aux
   WHERE ca = '2022-02-15 16:47:12';
SET SESSION optimizer_switch='derived_condition_pushdown=off';
SELECT
  *
FROM
  (
    SELECT
      coalesce(timezone, '+00:00') tz,
      convert_tz(createdAt, '+00:00', (select tz)) ca,
      if(createdAt, if((select 1) = 1, 1, 1), 1) random
    FROM temp
  ) aux
   WHERE ca = '2022-02-15 16:47:12';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113097_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L2)
- `target_113097_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113171_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113171-8.0.35.sql)；SHA256：`918205b3d593785db925b010490c96f383187a3f0f12b7744cb7c892692d1ad0`。

```sql
-- MySQL report #113171; source: cmain, c538259, c544161
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SELECT @@SESSION.sql_mode;
SELECT SUM(SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;
SELECT SUM(DISTINCT SUBSTRING('text',1,3)) FROM dual;
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113171_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L3)
- `target_113171_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113180_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113180-8.0.35.sql)；SHA256：`3d684c4086b5e384f172ee9750314c66cdafb75fb8ad8e1858b2ba649e841747`。

```sql
-- MySQL report #113180; source: cmain, c538271, c538297
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 INT, c1 INT, PRIMARY KEY(c0));
INSERT INTO t0(c0, c1) VALUES (1, 0);
CREATE UNIQUE INDEX i1 ON t0(c1 , c0 );

SELECT * FROM t0 WHERE SIN(1150199883)=c1; -- 1 0
SELECT * FROM t0 WHERE NOT SIN(1150199883)=c1; -- 1 0
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113180_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:9](../../experiments/saved_20261029/official_research_20261029/confirmation_batch/initial_evidence/records.jsonl#L9)
- `target_113180_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:9](../../experiments/saved_20261029/official_research_20261029/confirmation_results/records.jsonl#L9)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113298_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113298-8.0.35.sql)；SHA256：`8721f79806ab7291909b91680646707ee8ff864531cdabfc6de94554b23bb23c`。

```sql
-- MySQL report #113298; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0( c1 INTEGER);
INSERT INTO t0 (c1) VALUES (1);
CREATE INDEX i0 ON t0(c1  );

SELECT * FROM t0 WHERE (1/1.5 IN (c1)); -- 1
SELECT * FROM t0 WHERE (NOT (1/1.5 IN (c1))); -- 1

ALTER TABLE t0 DROP INDEX i0;
SELECT * FROM t0 WHERE (1/1.5 IN(c1));
SELECT * FROM t0 WHERE NOT(1/1.5 IN(c1));
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113298_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L5)
- `target_113298_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113301_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113301-8.0.35.sql)；SHA256：`1acb50a454e8c3aafa0458ab4c786ed36ac3b717abdc017a66182a4374576f62`。

```sql
-- MySQL report #113301; source: cmain, c538587, c554594
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE test_time(id_col int,`time_6` time(6) DEFAULT '01:01:01.000000', `time_0` time);
insert into test_time(id_col,time_6,time_0) values
(31,'07:59:59.000000', '07:59:59'),
(32,'07:59:59.000000', '07:59:59'),
(51,'00:00:00.000000', '00:00:00'),
(52,'00:00:00.000000', '00:00:00'),
(71,'06:06:06.000000', '06:06:06'),
(72,'06:06:06.000000', '06:06:06');

prepare stmt from "SELECT id_col,time_6,time_0 FROM test_time WHERE test_time.time_6 IN (?, '06:06:06.000000','00:00:00');";
set @time_val='07:59:59';
execute stmt USING @time_val;
SELECT id_col,time_6,time_0 FROM test_time WHERE time_6 IN ('07:59:59','06:06:06.000000','00:00:00');
DEALLOCATE PREPARE stmt;
PREPARE stmt0 FROM "SELECT id_col,time_6,time_0 FROM test_time WHERE time_0 IN (?, '06:06:06.000000','00:00:00');";
EXECUTE stmt0 USING @time_val;
SELECT id_col,time_6,time_0 FROM test_time WHERE time_0 IN ('07:59:59','06:06:06.000000','00:00:00');
DEALLOCATE PREPARE stmt0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113301_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L5)
- `target_113301_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L5)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_113302_8_0_35_r1。

[下载独立 SQL](sql/reproduced_106/mysql-113302-8.0.35.sql)；SHA256：`3b5c6a28f673d10046b795464c2091472aaf0da9c4c277052f5216efeecb1c35`。

```sql
-- MySQL report #113302; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t0(c0 INT, c1 INT);
INSERT INTO t0(c1, c0) VALUES(0, 1);

SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- empty result
CREATE INDEX i0 ON t0(c1);
SELECT * FROM t0 WHERE t0.c1 IN (GREATEST(0.1, 0.2)); -- {1|0}
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113302_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L5)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113316_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113316-8.0.35.sql)；SHA256：`0af4eba7413774e64298a6be9d6417911f709e7524ced8fae1d6a570a7fba1db`。

```sql
-- MySQL report #113316; source: cmain, c538619
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t0 (`int_col` int,`bit_col` bit(8) DEFAULT b'0', KEY `ndx_bit_col` (`bit_col` DESC)) partition by hash(int_col) partitions 3;

insert into t0(int_col) values(1);

SELECT bit_col, int_col FROM t0 A WHERE bit_col = '0x00';

alter table t0 drop key ndx_bit_col;

SELECT bit_col, int_col FROM t0 A WHERE bit_col = '0x00';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113316_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L6)
- `target_113316_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113319_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113319-8.0.35.sql)；SHA256：`8950b345f19cbdeafd261ce04be0659d4f5afd62bf4a1247542ac5677db558b6`。

```sql
-- MySQL report #113319; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE t1(a INT); CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1),(2),(3),(4); INSERT INTO t2 VALUES(1),(2);
SET optimizer_switch='subquery_to_derived=off';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
SET optimizer_switch='subquery_to_derived=on';
SELECT (SELECT COUNT(1) AS cnt FROM t2 WHERE t2.a=t1.a HAVING cnt>0) FROM t1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113319_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L7)
- `target_113319_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113358_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113358-8.0.35.sql)；SHA256：`92550133a96e028316c052d602e1ac2369c62955139573b9e1ec98f59f0e53bc`。

```sql
-- MySQL report #113358; source: cmain, c538763, c538769, c538772
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET @old_sql_mode=@@SESSION.sql_mode;
SET @old_optimizer_switch=@@SESSION.optimizer_switch;
SET SESSION sql_mode=CONCAT_WS(',',NULLIF(@@SESSION.sql_mode,''),'ONLY_FULL_GROUP_BY');
CREATE TABLE t1(a INT,b INT,c INT);
CREATE TABLE t2(a INT);
INSERT INTO t1 VALUES(1,1,1),(2,1,1);
INSERT INTO t2 VALUES(1),(2),(1);
SET SESSION optimizer_switch='subquery_to_derived=off';
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1;
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1 GROUP BY b;
SET SESSION optimizer_switch='subquery_to_derived=on';
SELECT b,(SELECT COUNT(t.a) FROM t2 AS t WHERE t.a=t1.a) AS c FROM t1 GROUP BY b;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113358_8_0_35_r1`，实际版本 8.0.35，completed_with_sql_errors；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L6)
- `target_113358_8_0_35_r2`，实际版本 8.0.35，completed_with_sql_errors；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113433_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113433-8.0.35.sql)；SHA256：`4a7789d2a8588ae0141ecab35834c9bc4367332ddfea17114942e0d5114b72f8`。

```sql
-- MySQL report #113433; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `tt` (
  `id_col` int NOT NULL,
  `bigint_col` bigint NOT NULL,
  `year_col` year DEFAULT NULL,
  KEY `ndx_year_col` (`year_col` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT into tt values (61,-9223372036854775808,'1913');

SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col;
SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col AND A.id_col = 61;
SELECT A.year_col, A.id_col FROM tt A WHERE 61 < A.year_col;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113433_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L8)
- `target_113433_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L4)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113506_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113506-8.0.35.sql)；SHA256：`589d29868642fce6e03b4bad27e2fd4ebd8b6478a04bbeae55f64b3488938eb0`。

```sql
-- MySQL report #113506; source: cmain, c539290, c539293, c539294, c539322, c544157
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
SET NAMES utf8mb4;
CREATE TABLE t1(a CHAR(10) CHARACTER SET utf8mb4);
INSERT INTO t1 VALUES('你好'),('中午好');
SELECT a,CONVERT(a USING latin1) FROM t1 ORDER BY CONVERT(a USING utf8mb4);
SELECT a FROM t1 ORDER BY CONVERT(a USING utf8mb4);
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113506_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L7)
- `target_113506_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L7)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113534_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113534-8.0.35.sql)；SHA256：`8805dc79707800e64ed1d4ccf328e2b0497d6de87ee60ef6d6c9a806682a3934`。

```sql
-- Report #113534; source anchors: cmain, c539367
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE `testa` (
  `id` bigint NOT NULL,
  `company_id` bigint DEFAULT NULL,
  `batch_no` bigint DEFAULT NULL,
  `picker` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_picker_query` (`company_id`,(cast(json_extract(`picker`,_utf8mb4'$[*].userName') as char(64) array)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `testb` (
  `id` bigint NOT NULL,
  `company_id` bigint DEFAULT NULL,
  `current_order_batch_no` bigint DEFAULT NULL,
  `history_order_batch_no` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx01_testb` (`company_id`,`current_order_batch_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;                                                                      
  
                                                                    
insert into testa values(1,48005,100,NULL);
insert into testa values(2,48005,101,'[]');
insert into testa values(3,48005,102,'[{"userId": "123456", "userName": "xiaoxu"}]');

insert into testb values(1,48005,101,NULL);
insert into testb values(2,48005,101,NULL);
insert into testb values(3,48005,102,'[123]');
insert into testb values(4,48005,102,'[124]');


select /*+ JOIN_PREFIX(ord, bat) */bat.id                     as batchPkId,        bat.batch_no,        ord.id,ord.history_order_batch_no as orderLevelHistoryBatchNo   from testa bat  inner join testb ord     on ord.current_order_batch_no = bat.batch_no  where bat.company_id = 48005 and ord.company_id=48005 and  bat.batch_no = 101;
select bat.id                     as batchPkId,        bat.batch_no,        ord.id,ord.history_order_batch_no as orderLevelHistoryBatchNo   from testa bat  inner join testb ord     on ord.current_order_batch_no = bat.batch_no  where bat.company_id = 48005 and ord.company_id=48005 and  bat.batch_no = 101;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113534_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:9](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L9)
- `target_113534_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L5)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113557_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113557-8.0.35.sql)；SHA256：`240dce608910aa3dcdc6c6278d8261ea2d1e898a84418bdf2fbba9733109abe9`。

```sql
-- MySQL report #113557; source: cmain, c539454
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
create table t(a int, d json, index iad(a, (cast(d->'$.b' as signed array))));
insert into t value(1,'{"b":[]}'), (2,'{"b":[]}');
select * from t use index (iad) where a = 1;
select * from t ignore index (iad) where a = 1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113557_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:10](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b004_8_0_35/results/records.jsonl#L10)
- `target_113557_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b009_8_0_35/results/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113649_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113649-8.0.35.sql)；SHA256：`c902e36dce6c26741a63f23d9eee1acdc2ae6ba57db137db8baa7e8bcc7e040b`。

```sql
-- MySQL report #113649; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DELIMITER //
CREATE PROCEDURE demo(out a varchar(1024))
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE cur1 CURSOR FOR SELECT format(-1.7976931348623157E+307,256);
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN cur1;
  read_loop: LOOP
    FETCH cur1 INTO a;
    IF done THEN
      LEAVE read_loop;
    END IF;
  END LOOP;
  CLOSE cur1;
END//
DELIMITER ;
CALL demo(@hello);
SHOW WARNINGS;
SELECT @hello,LENGTH(@hello),FORMAT(-1.7976931348623157E+307,256),LENGTH(FORMAT(-1.7976931348623157E+307,256)),CAST(@hello AS BINARY)=CAST(FORMAT(-1.7976931348623157E+307,256) AS BINARY) AS same_bytes;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113649_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L8)
- `target_113649_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:8](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L8)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_113768_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-113768-8.0.35.sql)；SHA256：`54b5c9112cb8d8331011c104b20ab51c06d47635e57d1f3980dd0d6abc181527`。

```sql
-- MySQL report #113768; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
create table tb(a bigint);
insert into tb values(9223372036854775807),(-9223372036854775808);
SELECT 1 FROM tb A WHERE (A.a, A.a) NOT IN  ((CAST(9223372036854775807 AS REAL),CAST(110 AS SIGNED INTEGER)),(CAST(92 AS REAL),CAST(NULL AS SIGNED INTEGER)));
SELECT CAST(9223372036854775807 AS REAL);
SHOW WARNINGS;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_113768_8_0_35_r1`，实际版本 8.0.35，completed_with_sql_errors；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b003_8_0_35/results/records.jsonl#L4)
- `target_113768_8_0_35_r2`，实际版本 8.0.35，completed_with_sql_errors；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b013_8_0_35/results/records.jsonl#L1)

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

目标版本实际执行 1 次；下列默认 SQL 对应 target_114196_8_0_35_r1。

[下载独立 SQL](sql/reproduced_106/mysql-114196-8.0.35.sql)；SHA256：`d84afdd04b68c65f61b8eea0555b1e83a25602410506c2344e29c3ad0b334ed6`。

```sql
-- MySQL report #114196; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE IF NOT EXISTS t0(c0 DECIMAL);
REPLACE INTO t0(c0) VALUES(0.1);

SELECT t0.c0 FROM t0 WHERE t0.c0 <= - 0.8;

SELECT (t0.c0 <= - 0.8) IS TRUE AS flag FROM t0;
SELECT * FROM t0;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114196_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:6](../../experiments/saved_20261029/replay_20261029_first_batch/official_scope/confirmation/initial_evidence/records.jsonl#L6)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114380_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114380-8.0.35.sql)；SHA256：`2d842d2a1c8d7ae7b16c341f7a318932e46bb78915ae6e60ec07dbbdc2e3e65b`。

```sql
-- Report #114380; source anchors: cmain, c541693
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE t0(c1 FLOAT) ;
INSERT INTO t0(c1) VALUES(0.1);

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1 FROM t0) as t WHERE f1;

SELECT f1 FROM (SELECT (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) AS f1, (LEAST('-2',  EXISTS (SELECT 1 WHERE FALSE), CAST(t0.c1 AS SIGNED), TIMESTAMP('2024-03-17'))) IS TRUE AS flag FROM t0) as t WHERE flag=1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114380_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:5](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b003_8_0_35/results/records.jsonl#L5)
- `target_114380_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:2](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b013_8_0_35/results/records.jsonl#L2)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114381_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114381-8.0.35.sql)；SHA256：`bca37d1ba9d1698c410c63a962f919501d25b1f9a880c74f0c46da5d981800e7`。

```sql
-- MySQL report #114381; source: cmain, c541692
-- Static preparation only. NOT EXECUTED. Read case.json; use a fresh isolated case schema.
CREATE TABLE t0(c0 DOUBLE) ;
CREATE TABLE t1 LIKE t0;
INSERT IGNORE INTO t1(c0) VALUES(1);
INSERT INTO t0(c0) VALUES(0.1);

SELECT t1.c0 AS _c0 FROM t1, t0 WHERE (( EXISTS (SELECT 1 )) < ((NOT t0.c0))) IN (((t1.c0) XOR ("")) / (TIMEDIFF('3939-09-13 16:49:10.309835', '4722-09-08 23:55:52.675528')));
SELECT _c0 FROM (SELECT t1.c0 AS _c0, ((( EXISTS (SELECT 1 )) < ((NOT t0.c0))) IN (((t1.c0) XOR ("")) / (TIMEDIFF('3939-09-13 16:49:10.309835', '4722-09-08 23:55:52.675528')))) IS TRUE AS flag FROM t1, t0) as t WHERE flag=1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114381_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:9](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L9)
- `target_114381_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:9](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L9)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114384_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114384-8.0.35.sql)；SHA256：`2783e706d186416f6187325c9e147c27a1b8b0c47a6c8d1e4f5dabfcff4b659f`。

```sql
-- Report #114384; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE IF NOT EXISTS t1(c0 SMALLINT) ;
INSERT INTO t1(c0) VALUES(0.49);
CREATE INDEX i0 ON t1(c0);

SELECT t1.c0 FROM t1 WHERE t1.c0 IN (LOG(0.6261534882548163));

SELECT c0 FROM (SELECT t1.c0, (t1.c0 IN (LOG(0.6261534882548163))) IS TRUE AS flag FROM t1) as t WHERE flag=1;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114384_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:10](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b005_8_0_35/results/records.jsonl#L10)
- `target_114384_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:10](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b010_8_0_35/results/records.jsonl#L10)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114775_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114775-8.0.35.sql)；SHA256：`1cf4e5812f6c3ed238595ff8659e74b3c0857f85b905c87ce09d20028778cffa`。

```sql
-- Report #114775; source anchors: cmain
-- Static preparation only; not executed. See case.json before any future isolated run.
create table main (id varchar(10));
insert into main values ('a');
insert into main values ('b');

create table dummy (id varchar(10));
insert into dummy values ('c');
insert into dummy values ('d');

create table seq  (id varchar(10));
insert into seq values ('e');
insert into seq values ('f');

select 'main' tab, id from main union all
select 'dummy' tab, id from dummy union all
select 'seq' tab, id from seq ;

/* 2) 오류 케이스 쿼리 */
select main_id
     , max_val
	 , dummy_ID
  from (
        select main.Id  as main_id
             , (
                select id
                  from seq
                 where seq.id = main.id
                ) as max_val -- 해당 구문 제외하면 정상
             , dummy.ID as dummy_ID
          from main
          left outer join (select 'c' as ID
                              from dummy
							) dummy
               on dummy.ID = main.id 
  where main.Id in ('a','b')
    ) test
WHERE dummy_ID = 'c' ;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114775_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_3/b006_8_0_35/results/records.jsonl#L1)
- `target_114775_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:1](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b011_8_0_35/results/records.jsonl#L1)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_114917_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-114917-8.0.35.sql)；SHA256：`24cc259ce7e8eab2c067c9473f45c2a61c498d625a3c9f17fd4b81c4abe2dcf4`。

```sql
-- MySQL report #114917; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `time_col` time(6) DEFAULT NULL,
  `mediumint_col` mediumint DEFAULT NULL,
  KEY `ndx_mediumint_col` (`mediumint_col` DESC),
  KEY `ndx_time_col` (`time_col` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `test` VALUES (NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,NULL),(NULL,NULL),(NULL,NULL),(NULL,NULL),(NULL,NULL),('23:23:59.000000',-8388608),('23:23:59.000000',-8388608),('23:23:59.000000',-8388608),('23:23:59.000000',-8388608),('23:23:59.000000',-8388608),('20:59:59.000000',-8388608),('20:59:59.000000',-8388608),('20:59:59.000000',-8388608),('20:59:59.000000',-8388608),('20:59:59.000000',-8388608),('08:59:59.000000',-8388608),('08:59:59.000000',-8388608),('08:59:59.000000',-8388608),('08:59:59.000000',-8388608),('08:59:59.000000',-8388608),('10:59:59.000000',-8388608),('10:59:59.000000',-8388608),('10:59:59.000000',-8388608),('10:59:59.000000',-8388608),('10:59:59.000000',-8388608),('07:59:59.000000',-8388608),('07:59:59.000000',-8388608),('07:59:59.000000',-8388608),('07:59:59.000000',-8388608),('07:59:59.000000',-8388608),('01:59:59.000000',-8388608),('01:59:59.000000',-8388608),('01:59:59.000000',-8388608),('01:59:59.000000',-8388608),('01:59:59.000000',-8388608),('06:59:59.000000',-8388608),('06:59:59.000000',-8388608),('06:59:59.000000',-8388608),('06:59:59.000000',-8388608),('06:59:59.000000',-8388608),('03:59:59.000000',-8388608),('03:59:59.000000',-8388608),('03:59:59.000000',-8388608),('03:59:59.000000',-8388608),('03:59:59.000000',-8388608),('09:09:59.000000',-8388608),('09:09:59.000000',-8388608),('09:09:59.000000',-8388608),('09:09:59.000000',-8388608),('09:09:59.000000',-8388608),('05:59:59.000000',-8388608),('05:59:59.000000',-8388608),('05:59:59.000000',-8388608),('05:59:59.000000',-8388608),('05:59:59.000000',-8388608),('04:59:59.000000',-8388608),('04:59:59.000000',-8388608),('04:59:59.000000',-8388608),('04:59:59.000000',-8388608),('04:59:59.000000',-8388608),('02:59:59.000000',-8388608),('02:59:59.000000',-8388608),('02:59:59.000000',-8388608),('02:59:59.000000',-8388608),('02:59:59.000000',-8388608),(NULL,1),(NULL,1),(NULL,1),(NULL,1),(NULL,1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1),('12:00:00.000000',1);

SELECT time_col, mediumint_col
FROM test
WHERE time_col IS NOT UNKNOWN
	AND time_col NOT BETWEEN '06:59:59.000000' AND NULL
	OR time_col < '10:59:59.000000'
GROUP BY 1, 2
ORDER BY 1, 2;
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_114917_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:6](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b003_8_0_35/results/records.jsonl#L6)
- `target_114917_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:3](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b013_8_0_35/results/records.jsonl#L3)

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

目标版本实际执行 2 次；下列默认 SQL 对应 target_115294_8_0_35_r2。

[下载独立 SQL](sql/reproduced_106/mysql-115294-8.0.35.sql)；SHA256：`b311a1f870a48dc48806e0c2985372706431fa1a3bc1c2ac6a1318cd541497e3`。

```sql
-- MySQL report #115294; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `t` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `col1` int DEFAULT NULL,
  `col2` varchar(20) DEFAULT NULL,
  `partition_key` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`,`partition_key`),
  KEY `idx_col2` (`col2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/*!50100 PARTITION BY RANGE (to_days(`partition_key`))
(PARTITION p20240528 VALUES LESS THAN (739400) ENGINE = InnoDB,
 PARTITION p20240529 VALUES LESS THAN (739401) ENGINE = InnoDB,
 PARTITION p20240530 VALUES LESS THAN (739402) ENGINE = InnoDB,
 PARTITION p20240531 VALUES LESS THAN (739403) ENGINE = InnoDB,
 PARTITION p20240601 VALUES LESS THAN (739404) ENGINE = InnoDB,
 PARTITION p20240602 VALUES LESS THAN (739405) ENGINE = InnoDB,
 PARTITION p20240603 VALUES LESS THAN (739406) ENGINE = InnoDB,
 PARTITION p20240604 VALUES LESS THAN (739407) ENGINE = InnoDB,
 PARTITION p20240605 VALUES LESS THAN (739408) ENGINE = InnoDB,
 PARTITION p20240606 VALUES LESS THAN (739409) ENGINE = InnoDB,
 PARTITION p20240607 VALUES LESS THAN (739410) ENGINE = InnoDB,
 PARTITION p20240608 VALUES LESS THAN (739411) ENGINE = InnoDB,
 PARTITION p20240609 VALUES LESS THAN (739412) ENGINE = InnoDB,
 PARTITION p20240610 VALUES LESS THAN (739413) ENGINE = InnoDB,
 PARTITION p20240611 VALUES LESS THAN (739414) ENGINE = InnoDB,
 PARTITION p20240612 VALUES LESS THAN (739415) ENGINE = InnoDB,
 PARTITION p20240613 VALUES LESS THAN (739416) ENGINE = InnoDB,
 PARTITION p20240614 VALUES LESS THAN (739417) ENGINE = InnoDB,
 PARTITION p20240615 VALUES LESS THAN (739418) ENGINE = InnoDB,
 PARTITION p20240616 VALUES LESS THAN (739419) ENGINE = InnoDB,
 PARTITION p20240617 VALUES LESS THAN (739420) ENGINE = InnoDB,
 PARTITION p20240618 VALUES LESS THAN (739421) ENGINE = InnoDB,
 PARTITION pMax VALUES LESS THAN MAXVALUE ENGINE = InnoDB) */;
INSERT INTO t VALUES(NULL,1,'abc','2024-06-12'),(NULL,2,'abc','2024-06-12'),(NULL,3,'abc','2024-06-12'),(NULL,1,'bcd','2024-06-11'),(NULL,2,'bcd','2024-06-11'),(NULL,2,'bcd','2024-06-10');
SELECT NAME,ENABLED,TIMED FROM performance_schema.setup_instruments WHERE NAME='wait/io/table/sql/handler';
SELECT OBJECT_SCHEMA,OBJECT_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_table WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
SELECT OBJECT_SCHEMA,OBJECT_NAME,INDEX_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_index_usage WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
EXPLAIN SELECT * FROM t WHERE id=1;
SELECT * FROM t WHERE id=1;
SELECT OBJECT_SCHEMA,OBJECT_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_table WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
SELECT OBJECT_SCHEMA,OBJECT_NAME,INDEX_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_index_usage WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
EXPLAIN SELECT * FROM t;
SELECT * FROM t;
SELECT OBJECT_SCHEMA,OBJECT_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_table WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
SELECT OBJECT_SCHEMA,OBJECT_NAME,INDEX_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_index_usage WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
EXPLAIN SELECT * FROM t WHERE id<=3;
SELECT * FROM t WHERE id<=3;
SELECT OBJECT_SCHEMA,OBJECT_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_table WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
SELECT OBJECT_SCHEMA,OBJECT_NAME,INDEX_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_index_usage WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
EXPLAIN SELECT * FROM t WHERE id IN(1,2);
SELECT * FROM t WHERE id IN(1,2);
SELECT OBJECT_SCHEMA,OBJECT_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_table WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
SELECT OBJECT_SCHEMA,OBJECT_NAME,INDEX_NAME,COUNT_STAR,COUNT_READ,COUNT_FETCH FROM performance_schema.table_io_waits_summary_by_index_usage WHERE OBJECT_SCHEMA=DATABASE() AND OBJECT_NAME='t';
```

目标执行记录（完整字段和所有重复证据位置见同名 JSON）：

- `target_115294_8_0_35_r1`，实际版本 8.0.35，completed；[records.jsonl:7](../../experiments/saved_20261029/official_pending230_20261029/wave_4/b003_8_0_35/results/records.jsonl#L7)
- `target_115294_8_0_35_r2`，实际版本 8.0.35，completed；[records.jsonl:4](../../experiments/saved_20261029/official_pending230_20261029/wave_5/b013_8_0_35/results/records.jsonl#L4)
