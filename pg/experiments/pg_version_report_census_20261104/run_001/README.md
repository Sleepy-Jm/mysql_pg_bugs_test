# PostgreSQL 官方报告版本字段统计

核对日期：2026-11-04。

## 筛选口径

- 沿用当前 MySQL 流程：只读取报告首帖的 `PostgreSQL version:` 原字段，匹配完整版本号；不凭标题、正文、回复、修复版本或发布日期推断。
- 官方来源为 pgsql-bugs 中带 BUG 编号的表单报告。普通未编号讨论不属于此冻结集合；回复不重复计数。同一根因的不同报告仍按报告分别计数。
- 遍历 2021-11 至 2026-11 的月归档及分页，覆盖 14.1 发布所在月份至核对日；仅纳入报告日期不晚于 2026-11-04 的匹配报告。
- 不展开版本范围或省略写法；不将 14.10/14.20/17.10/17.20 当作目标版本。
- 这是版本字段符合条件的报告统计，不是已确认独立 bug 数。未开展 SQL/oracle 整理、根因去重或数据库重放，所有入选项均为 `not_run`。

## 统计

| 目标版本 | 报告数 | 报告 × 版本项数 |
|---|---:|---:|
| 14.1 | 49 | 49 |
| 14.2 | 42 | 42 |
| 17.1 | 4 | 4 |
| 17.2 | 41 | 41 |
| 14.1-14.2 合计 | 91 | 91 |
| 17.1-17.2 合计 | 45 | 45 |
| 全部（报告去重） | 136 | 136 |

归档覆盖：61/61 个月，129 个页面；发现 2093 个候选首帖 URL，核对 2093 个；获取错误 0 个，字段/编号待核对 0 个。

候选中经发件身份确认的表单原始报告 2066 个；排除沿用 BUG 标题的非表单邮件 27 个。

存在获取错误或字段待核对项时，统计仅为已核实下界，不应称为完整总数。归档公开可见范围之外、删除或未编号的邮件不在此集合中。

## 证据文件

- `report_version_items.csv`：逐报告 × 目标版本表，含原字段、官方链接、快照、SHA-256、执行状态。
- `selected_reports.json` / `scope_items.json`：入选报告和版本项。
- `scope_audit.json`：所有已读取候选的原字段与匹配结果，包含未入选项。
- `archive_inventory.json` / `candidates.json`：目录分页证据与候选 URL；`fetch_errors.json`：获取缺口。
- `indexes/` / `sources/`：原 HTML 字节快照；`summary.json`：机器可读汇总。

## 入选报告

| 编号 | 日期 | Version 原字段 | 标题（官方来源） |
|---|---|---|---|
| 17283 | 2021-11-13 | 14.1 | [BUG #17283: localhost should also include IPv6](https://www.postgresql.org/message-id/17283-ad8b80401ffe779e%40postgresql.org) |
| 17284 | 2021-11-13 | 14.1 | [BUG #17284: Assert failed in SerialAdd() when the summarize_serial mode is engaged](https://www.postgresql.org/message-id/17284-c878f548184aae1f%40postgresql.org) |
| 17288 | 2021-11-17 | 14.1 | [BUG #17288: PSQL bug with COPY command (Windows)](https://www.postgresql.org/message-id/17288-6b58a91025a8a8a3%40postgresql.org) |
| 17289 | 2021-11-17 | 14.1 | [BUG #17289: Postgres 14.1 Windows installer fails with unknown error and terminates](https://www.postgresql.org/message-id/17289-69d89b0dd2c60e41%40postgresql.org) |
| 17290 | 2021-11-17 | 14.1 | [BUG #17290: Error Installation](https://www.postgresql.org/message-id/17290-a559e8daf4fa53c5%40postgresql.org) |
| 17292 | 2021-11-19 | 14.1 | [BUG #17292: view definition containing multiple joins on partitioned table returns invalid explain plan](https://www.postgresql.org/message-id/17292-77f65b65342c5bf0%40postgresql.org) |
| 17294 | 2021-11-20 | 14.1 | [BUG #17294: spgist doesn't support varchar, only text type fields.](https://www.postgresql.org/message-id/17294-8f6c7962ce877edc%40postgresql.org) |
| 17300 | 2021-11-27 | 14.1 | [BUG #17300: Server crashes on deserializing text multirange](https://www.postgresql.org/message-id/17300-dced2d01ddeb1f2f%40postgresql.org) |
| 17302 | 2021-11-28 | 14.1 | [BUG #17302: gist index prevents insertion of some data](https://www.postgresql.org/message-id/17302-dea8025c932a92f1%40postgresql.org) |
| 17304 | 2021-11-30 | 14.1 | [BUG #17304: Test failure with -fsanitize=undefined](https://www.postgresql.org/message-id/17304-e2600940ba8add78%40postgresql.org) |
| 17315 | 2021-12-04 | 14.1 | [BUG #17315: Postgresql needs reinstall after restore](https://www.postgresql.org/message-id/17315-cefb698e069aa044%40postgresql.org) |
| 17318 | 2021-12-06 | 14.1 | [BUG #17318: ERROR: AddressSanitizer: SEGV on unknown address in optimizer](https://www.postgresql.org/message-id/17318-2eb65a3a611d2368%40postgresql.org) |
| 17320 | 2021-12-06 | 14.1 | [BUG #17320: A SEGV in optimizer](https://www.postgresql.org/message-id/17320-70e37868182512ab%40postgresql.org) |
| 17331 | 2021-12-09 | 14.1 | [BUG #17331: Minor change in install steps](https://www.postgresql.org/message-id/17331-488fed0ded0b5b46%40postgresql.org) |
| 17333 | 2021-12-10 | 14.1 | [BUG #17333: pgdg postgresql-common pg_upgradecluster duplicate data_directory in configuration file](https://www.postgresql.org/message-id/17333-a00bcda4fab7c6d4%40postgresql.org) |
| 17334 | 2021-12-12 | 14.1 | [BUG #17334: Assert failed inside computeDistance() on gist index scanning](https://www.postgresql.org/message-id/17334-135f485c21739caa%40postgresql.org) |
| 17335 | 2021-12-13 | 14.1 | [BUG #17335: Duplicate result rows in Gather node when "Suppress Append ... that have a single child" applied](https://www.postgresql.org/message-id/17335-4dc92e1aea3a78af%40postgresql.org) |
| 17336 | 2021-12-14 | 14.1 | [BUG #17336: logtape sort performance and overflow](https://www.postgresql.org/message-id/17336-fc4e522d26a750fd%40postgresql.org) |
| 17339 | 2021-12-19 | 14.1 | [BUG #17339: Assert failed on attempt to detach a sequence concurrently](https://www.postgresql.org/message-id/17339-a9e09aaf38a3457a%40postgresql.org) |
| 17340 | 2021-12-20 | 14.1 | [BUG #17340: Unnest discards rows with empty or null arrays](https://www.postgresql.org/message-id/17340-74d17bbe94cb4190%40postgresql.org) |
| 17341 | 2021-12-21 | 14.1 | [BUG #17341: The comment of the source code is not correct](https://www.postgresql.org/message-id/17341-d913ddb626c5c08c%40postgresql.org) |
| 17344 | 2021-12-25 | 14.1 | [BUG #17344: Assert failed on queiring async_capable foreign table with inheritance](https://www.postgresql.org/message-id/17344-226b78b00de73a7e%40postgresql.org) |
| 17349 | 2021-12-28 | 14.1 | [BUG #17349: Function gen_random_uuid duplicates in pgcrypto and core](https://www.postgresql.org/message-id/17349-24d61e214429e8c1%40postgresql.org) |
| 17351 | 2022-01-01 | 14.1 | [BUG #17351: Altering a composite type created for a partitioned table can lead to a crash](https://www.postgresql.org/message-id/17351-6db1870f3f4f612a%40postgresql.org) |
| 17355 | 2022-01-06 | 14.1 | [BUG #17355: Server crashes on ExecReScanForeignScan in postgres_fdw when accessing foreign partition](https://www.postgresql.org/message-id/17355-de8e362eb7001a96%40postgresql.org) |
| 17356 | 2022-01-06 | 14.1 | [BUG #17356: hunspell-hu dictionary processing error](https://www.postgresql.org/message-id/17356-1979672d506f80d7%40postgresql.org) |
| 17357 | 2022-01-07 | 14.1 | [BUG #17357: When working with the window_function, the Where Clause does not work properly!](https://www.postgresql.org/message-id/17357-02bf57d4d89bf972%40postgresql.org) |
| 17358 | 2022-01-07 | 14.1 | [BUG #17358: While using --with-uuid=bsd option, uuid_ossp test fails on NetBSD 9.2](https://www.postgresql.org/message-id/17358-89806e7420797025%40postgresql.org) |
| 17362 | 2022-01-11 | 14.1 | [BUG #17362: Error "could not find block containing chunk" when using index with icu collation on CentOS 7](https://www.postgresql.org/message-id/17362-63967721ee562fa7%40postgresql.org) |
| 17365 | 2022-01-13 | 14.1 | [BUG #17365: Error: redefinition of 'stat' in win32_port.h when including postgres.h](https://www.postgresql.org/message-id/17365-c58cbf9d0c29586a%40postgresql.org) |
| 17366 | 2022-01-14 | 14.1 | [BUG #17366: Error result returned in timestamp2timestamptz, expected to be off by one hour](https://www.postgresql.org/message-id/17366-8744a901d10fd9d1%40postgresql.org) |
| 17368 | 2022-01-15 | 14.1 | [BUG #17368: Assert failed in GetSafeSnapshot() for SERIALIZABLE READ ONLY DEFERRABLE transaction](https://www.postgresql.org/message-id/17368-98a4f99e8e4b4402%40postgresql.org) |
| 17370 | 2022-01-19 | 14.1 | [BUG #17370: shmem lost on segfault](https://www.postgresql.org/message-id/17370-a42a313cf1589256%40postgresql.org) |
| 17372 | 2022-01-20 | 14.1 | [BUG #17372: Altering statistics during concurrent drop can lead to a server crash](https://www.postgresql.org/message-id/17372-bf3b6e947e35ae77%40postgresql.org) |
| 17382 | 2022-01-26 | 14.1 | [BUG #17382: When vacuum full or vacuumdb - F is executed, a large number of empty files will be generated in the](https://www.postgresql.org/message-id/17382-9b238ae4286aef7d%40postgresql.org) |
| 17385 | 2022-01-28 | 14.1 | [BUG #17385: "RESET transaction_isolation" inside serializable transaction causes Assert at the transaction end](https://www.postgresql.org/message-id/17385-9ee529fb091f0ce5%40postgresql.org) |
| 17386 | 2022-01-28 | 14.1 | [BUG #17386: btree index corruption after reindex concurrently on write heavy table](https://www.postgresql.org/message-id/17386-2227568627fb44ce%40postgresql.org) |
| 17387 | 2022-01-28 | 14.1 | [BUG #17387: Working in PG13 but not in PGH14: array_agg(RECORD)](https://www.postgresql.org/message-id/17387-5dfe54b988444963%40postgresql.org) |
| 17391 | 2022-02-02 | 14.1 | [BUG #17391: While using --with-ssl=openssl and PG_TEST_EXTRA='ssl' options, SSL tests fail on OpenBSD 7.0](https://www.postgresql.org/message-id/17391-304f81bcf724b58b%40postgresql.org) |
| 17393 | 2022-02-03 | 14.1 | [BUG #17393: Delete database after recovery with point-in-time is still missing datafiles](https://www.postgresql.org/message-id/17393-fe5b19a5eb16cf7f%40postgresql.org) |
| 17395 | 2022-02-05 | 14.1 | [BUG #17395: Assert failed on merge join when foreign range partition contains out-of-range value](https://www.postgresql.org/message-id/17395-8c326292078d1a57%40postgresql.org) |
| 17396 | 2022-02-07 | 14.1 | [BUG #17396: Missing pckages to instal Patroni](https://www.postgresql.org/message-id/17396-855e0fe21ed86d17%40postgresql.org) |
| 17402 | 2022-02-10 | 14.2 | [BUG #17402: RPM packages are not signed](https://www.postgresql.org/message-id/17402-f55be83853a4188f%40postgresql.org) |
| 17406 | 2022-02-15 | 14.2 | [BUG #17406: Segmentation fault on GiST index after 14.2 upgrade](https://www.postgresql.org/message-id/17406-71e02820ae79bb40%40postgresql.org) |
| 17409 | 2022-02-16 | 14.2 | [BUG #17409: Unable to alter data type of clustered column which is referenced by foreign key](https://www.postgresql.org/message-id/17409-52871dda8b5741cb%40postgresql.org) |
| 17413 | 2022-02-22 | 14.2 | [BUG #17413: update of partitioned table via postgres_fdw updates to much rows](https://www.postgresql.org/message-id/17413-106983288639aa44%40postgresql.org) |
| 17414 | 2022-02-23 | 14.2 | [BUG #17414: install failed](https://www.postgresql.org/message-id/17414-78e459288f587960%40postgresql.org) |
| 17415 | 2022-02-23 | 14.2 | [BUG #17415: Unable to use underscore as first character in set_config custom parameter](https://www.postgresql.org/message-id/17415-ebdb683d7e09a51c%40postgresql.org) |
| 17416 | 2022-02-23 | 14.2 | [BUG #17416: Server crashes due to python3 stack overflow on executing multiple plpy.rollback() calls](https://www.postgresql.org/message-id/17416-ed8fe5d7213d6c25%40postgresql.org) |
| 17424 | 2022-03-02 | 14.2 | [BUG #17424: Build failed on disabled GNUC in  Clang  environment CFLAGS= -O2  -fgnuc-version=0](https://www.postgresql.org/message-id/17424-75b750d162ef49f4%40postgresql.org) |
| 17425 | 2022-03-04 | 14.2 | [BUG #17425: Postgres service does not start if path to data folder ends with backslash.](https://www.postgresql.org/message-id/17425-98efe3609921ac7d%40postgresql.org) |
| 17428 | 2022-03-07 | 14.2 | [BUG #17428: last_value incorrect for uninitialized sequence](https://www.postgresql.org/message-id/17428-848dee31a3b899ab%40postgresql.org) |
| 17432 | 2022-03-10 | 14.2 | [BUG #17432: libraries are missing when installing postGIS in SLES15 SP3, some are part of SLES15 SP4 some not](https://www.postgresql.org/message-id/17432-526c86ba8fe401a1%40postgresql.org) |
| 17434 | 2022-03-11 | 14.2 | [BUG #17434: CREATE/DROP DATABASE can be executed in the same transaction with other commands](https://www.postgresql.org/message-id/17434-d9f7a064ce2a88a3%40postgresql.org) |
| 17436 | 2022-03-12 | 14.2 | [BUG #17436: Initializing and starting with Dockerfile fails](https://www.postgresql.org/message-id/17436-b8a4a3dd58c54838%40postgresql.org) |
| 17437 | 2022-03-13 | 14.2 | [BUG #17437: time spent in JIT is also attributed to function scan](https://www.postgresql.org/message-id/17437-612ed7f2c30d2ec5%40postgresql.org) |
| 17438 | 2022-03-14 | 14.2 | [BUG #17438: Logical replication hangs on master after huge DB load](https://www.postgresql.org/message-id/17438-2d4d4d7c6d1e8ec4%40postgresql.org) |
| 17443 | 2022-03-21 | 14.2 | [BUG #17443: Select command does not use brin index when enable_seqscan = on](https://www.postgresql.org/message-id/17443-543da4d6744b8ef2%40postgresql.org) |
| 17444 | 2022-03-21 | 14.2 | [BUG #17444: ERROR:  found xmin 215633 from before relfrozenxid 1280585](https://www.postgresql.org/message-id/17444-6e8cf5442b979fcd%40postgresql.org) |
| 17445 | 2022-03-21 | 14.2 | [BUG #17445: "ON CONFLICT" has different behaviors when its param is passed with prepared stmt or hard coded](https://www.postgresql.org/message-id/17445-fb74db6348391e85%40postgresql.org) |
| 17448 | 2022-03-25 | 14.2 | [BUG #17448: In Windows 10, version 1703 and later, huge_pages doesn't work.](https://www.postgresql.org/message-id/17448-0a96583a67edb1f7%40postgresql.org) |
| 17452 | 2022-03-31 | 14.2 | [BUG #17452: IN caluse behaves differently when there is one item comapred to when multiple](https://www.postgresql.org/message-id/17452-d10a023545015922%40postgresql.org) |
| 17454 | 2022-04-02 | 14.2 | [BUG #17454: Using psql without ipv4 address,the inet_server_port do not return PORT.](https://www.postgresql.org/message-id/17454-f120d78fa9c3013d%40postgresql.org) |
| 17456 | 2022-04-05 | 14.2 | [BUG #17456: pg_dump creates dump that does not fully respect operator schema location](https://www.postgresql.org/message-id/17456-484784da23004b59%40postgresql.org) |
| 17457 | 2022-04-06 | 14.2 | [BUG #17457: pg_rewind fatal failure when $PGDATA/log is a soft-link](https://www.postgresql.org/message-id/17457-6441a0e4ec86b911%40postgresql.org) |
| 17462 | 2022-04-11 | 14.2 | [BUG #17462: Invalid memory access in heapam_tuple_lock](https://www.postgresql.org/message-id/17462-9c98a0f00df9bd36%40postgresql.org) |
| 17466 | 2022-04-19 | 14.2 | [BUG #17466: Is it possible to supplement the default compilation options of CFLAGS in configure file？](https://www.postgresql.org/message-id/17466-6ab1e589e78a166a%40postgresql.org) |
| 17471 | 2022-04-29 | 14.2 | [BUG #17471: COMSPEC error](https://www.postgresql.org/message-id/17471-f37c3a3f2405b38a%40postgresql.org) |
| 17472 | 2022-04-29 | 14.2 | [BUG #17472: Jsonb[] operations not working](https://www.postgresql.org/message-id/17472-fb26354b34424baf%40postgresql.org) |
| 17473 | 2022-04-29 | 14.2 | [BUG #17473: Custom range type with timestamp doesn't respect precision](https://www.postgresql.org/message-id/17473-0b8caedccc6ee7b1%40postgresql.org) |
| 17474 | 2022-05-05 | 14.2 | [BUG #17474: Segmentation fault from INSERT ( JumbleExpr )](https://www.postgresql.org/message-id/17474-60868309e99b1fca%40postgresql.org) |
| 17476 | 2022-05-08 | 14.2 | [BUG #17476: ERROR:  "variable not found in subplan target list" when running SELECT COUNT(*)](https://www.postgresql.org/message-id/17476-cf579fc6b204baa2%40postgresql.org) |
| 17477 | 2022-05-09 | 14.2 | [BUG #17477: A crash bug in transformValuesClause()](https://www.postgresql.org/message-id/17477-0af3c6ac6b0a6ae0%40postgresql.org) |
| 17478 | 2022-05-09 | 14.1 | [BUG #17478: Missing documents in the index after CREATE INDEX CONCURRENTLY (but existing in the table)](https://www.postgresql.org/message-id/17478-c422e68d010b951d%40postgresql.org) |
| 17479 | 2022-05-10 | 14.2 | [BUG #17479: "plan should not reference subplan's variable" when calling `grouping` on result of subquery](https://www.postgresql.org/message-id/17479-6260deceaf0ad304%40postgresql.org) |
| 17480 | 2022-05-10 | 14.2 | [BUG #17480: Assertion failure in parse_relation.c](https://www.postgresql.org/message-id/17480-1c9d73565bb28e90%40postgresql.org) |
| 17481 | 2022-05-15 | 14.2 | [BUG #17481: sometime pg_stat_statements coredump](https://www.postgresql.org/message-id/17481-953591f62b3f8a58%40postgresql.org) |
| 17503 | 2022-05-30 | 14.2 | [BUG #17503: Package postgresql-jdbc-42.3.6-1.rhel8.noarch.rpm is not signed](https://www.postgresql.org/message-id/17503-c238692e7927e8a2%40postgresql.org) |
| 17512 | 2022-06-06 | 14.2 | [BUG #17512: Process running query fails with SIGSEV - nodeMemoize.c:349](https://www.postgresql.org/message-id/17512-36fa5fab90f48af9%40postgresql.org) |
| 17533 | 2022-06-25 | 14.2 | [BUG #17533: run benchmarksql test failed](https://www.postgresql.org/message-id/17533-1d85aebc9bcf9bf6%40postgresql.org) |
| 17537 | 2022-07-03 | 14.2 | [BUG #17537: Dynamically updating statement_timeout not affect the insert query right now.](https://www.postgresql.org/message-id/17537-9c5b29383602bca0%40postgresql.org) |
| 17538 | 2022-07-03 | 14.2 | [BUG #17538: Dynamically updating log_hostname not affect the disconnection log](https://www.postgresql.org/message-id/17538-74a88f3ab5b55670%40postgresql.org) |
| 17546 | 2022-07-11 | 14.2 | [BUG #17546: power() function - value is distorted via automatic type cast](https://www.postgresql.org/message-id/17546-d71fe78a505f9f7b%40postgresql.org) |
| 17600 | 2022-08-29 | 14.1 | [BUG #17600: Not able to install PostgreSql in my laptop](https://www.postgresql.org/message-id/17600-a84d5fba3283528b%40postgresql.org) |
| 17624 | 2022-09-29 | 14.1 | [BUG #17624: Creating database is non-ending execution.](https://www.postgresql.org/message-id/17624-40bd8106071a8e89%40postgresql.org) |
| 17667 | 2022-10-27 | 14.1 | [BUG #17667: to_char is used to collect statistics by week](https://www.postgresql.org/message-id/17667-5541f108ca50db84%40postgresql.org) |
| 17698 | 2022-11-25 | 14.2 | [BUG #17698: On SIGTERM, psql terminates, but leaves the statement running](https://www.postgresql.org/message-id/17698-58a6ab8caec496b0%40postgresql.org) |
| 17802 | 2023-02-20 | 14.1 | [BUG #17802: PGLogical getting Terminated](https://www.postgresql.org/message-id/17802-e7555b863e9906d4%40postgresql.org) |
| 18265 | 2024-01-02 | 14.1 | [BUG #18265: jsonb comparison order is inconsistent](https://www.postgresql.org/message-id/18265-fd06fa2f9ad3d1db%40postgresql.org) |
| 18507 | 2024-06-13 | 14.1 | [BUG #18507: See C include file "ntstatus.h" for a description of the hexadecimal value.](https://www.postgresql.org/message-id/18507-60e31665bd72615a%40postgresql.org) |
| 18531 | 2024-07-09 | 14.2 | [BUG #18531: err when using 'current of' with incremental COMMIT](https://www.postgresql.org/message-id/18531-c6dddd33b8555fd2%40postgresql.org) |
| 18711 | 2024-11-16 | 17.1 | [BUG #18711: Attempting a connection with a database name longer than 63 characters now fails](https://www.postgresql.org/message-id/18711-7503ee3e449d2c47%40postgresql.org) |
| 18712 | 2024-11-16 | 17.1 | [BUG #18712: inet value ::2 handling goes not as expected](https://www.postgresql.org/message-id/18712-f787a146022a78e4%40postgresql.org) |
| 18714 | 2024-11-18 | 17.1 | [BUG #18714: error during installation](https://www.postgresql.org/message-id/18714-faaa54e6c969b145%40postgresql.org) |
| 18718 | 2024-11-21 | 17.1 | [BUG #18718: Incorrect Twitter/X Logo Displayed on PostgreSQL Documentation Page](https://www.postgresql.org/message-id/18718-19d3521550f7b12e%40postgresql.org) |
| 18721 | 2024-11-23 | 17.2 | [BUG #18721: Documentation for psql does not specify that the history feature doesn't work](https://www.postgresql.org/message-id/18721-f2f262c937eb6621%40postgresql.org) |
| 18722 | 2024-11-23 | 17.2 | [BUG #18722: Processing arrays with plpgsql raises errors](https://www.postgresql.org/message-id/18722-fd9e645448cc78b4%40postgresql.org) |
| 18728 | 2024-11-27 | 17.2 | [BUG #18728: Inconsistency between  pg_wait_events.name  and pg_stat_activity.wait_event  for LWLocks](https://www.postgresql.org/message-id/18728-450924477056a339%40postgresql.org) |
| 18730 | 2024-12-03 | 17.2 | [BUG #18730: Inequality comparison operators and SMALLINT negative immediate value](https://www.postgresql.org/message-id/18730-0410c43cdb0229d8%40postgresql.org) |
| 18735 | 2024-12-05 | 17.2 | [BUG #18735: Specific multibyte character in psql file path command parameter for Windows](https://www.postgresql.org/message-id/18735-4acdb3998bb9f2b1%40postgresql.org) |
| 18741 | 2024-12-08 | 17.2 | [BUG #18741: Detaching a partition referencing a partitioned table fails with a trigger-related error](https://www.postgresql.org/message-id/18741-e4ef6f7aa8a956cb%40postgresql.org) |
| 18748 | 2024-12-20 | 17.2 | [BUG #18748: Old name version](https://www.postgresql.org/message-id/18748-b02fb92b0021975b%40postgresql.org) |
| 18750 | 2024-12-23 | 17.2 | [BUG #18750: Inappropriate update when it is blocked in RC](https://www.postgresql.org/message-id/18750-e0a79ec68de35cec%40postgresql.org) |
| 18751 | 2024-12-23 | 17.2 | [BUG #18751: Sub-optimal UNION ALL plan](https://www.postgresql.org/message-id/18751-887c7bf4e67e65a7%40postgresql.org) |
| 18753 | 2024-12-24 | 17.2 | [BUG #18753: Unable to Recover a Deleted Database Using PITR](https://www.postgresql.org/message-id/18753-02b5cc4f629e1e5d%40postgresql.org) |
| 18754 | 2024-12-27 | 17.2 | [BUG #18754: Logical replication cannot restart if client sent a copyDone](https://www.postgresql.org/message-id/18754-e49e7bda4eb683d9%40postgresql.org) |
| 18755 | 2024-12-29 | 17.2 | [BUG #18755: Using Natts_pg_trigger rather than Natts_pg_event_trigger for event trigger](https://www.postgresql.org/message-id/18755-daae8f0ea9618715%40postgresql.org) |
| 18758 | 2024-12-30 | 17.2 | [BUG #18758: Incorrect query result caused by ROLLUP operation](https://www.postgresql.org/message-id/18758-7bbeea9719044a29%40postgresql.org) |
| 18759 | 2024-12-30 | 17.2 | [BUG #18759: Missing files](https://www.postgresql.org/message-id/18759-31d4492b7a5f897a%40postgresql.org) |
| 18760 | 2024-12-31 | 17.2 | [BUG #18760: ../doc/src/sgml/postgres.sgml:24: element book: validity error : No declaration for attribute id of](https://www.postgresql.org/message-id/18760-82d1b83da31b898d%40postgresql.org) |
| 18764 | 2025-01-03 | 17.2 | [BUG #18764: server closed the connection unexpectedly](https://www.postgresql.org/message-id/18764-63ad667ea26e877a%40postgresql.org) |
| 18767 | 2025-01-06 | 17.2 | [BUG #18767: Inconsistency in result of a Plpgsql GET DIAGNOSTICS PG_CONTEXT instruction.](https://www.postgresql.org/message-id/18767-e36a4af08c98f883%40postgresql.org) |
| 18769 | 2025-01-09 | 17.2 | [BUG #18769: ldapscheme is not displayed in pg_hba_file_rules](https://www.postgresql.org/message-id/18769-dd8610cbc0405172%40postgresql.org) |
| 18770 | 2025-01-10 | 17.2 | [BUG #18770: The function 'packGraph ' causes a memory leak.](https://www.postgresql.org/message-id/18770-895a62c1890d7491%40postgresql.org) |
| 18771 | 2025-01-11 | 17.2 | [BUG #18771: ICU custom collations with rules ignore collator strength option.](https://www.postgresql.org/message-id/18771-98bb23e455b0f367%40postgresql.org) |
| 18778 | 2025-01-16 | 17.2 | [BUG #18778: Query planning fails in ExecInitExprRec with unrecognized node type](https://www.postgresql.org/message-id/18778-24cd399df6c806af%40postgresql.org) |
| 18780 | 2025-01-19 | 17.2 | [BUG #18780: Bindings types are lost for complex queries](https://www.postgresql.org/message-id/18780-bae540b8dbfe4cdc%40postgresql.org) |
| 18782 | 2025-01-21 | 17.2 | [BUG #18782: Inconsistent behaviour with triggers and row level security - depends on prior number of inserts](https://www.postgresql.org/message-id/18782-c189e15f237f27d6%40postgresql.org) |
| 18783 | 2025-01-23 | 17.2 | [BUG #18783: 2025-01-23 03:55:06.243 GMT [22929] LOG:  postmaster became multithreaded 2025-01-23 03:55:06.243 GM](https://www.postgresql.org/message-id/18783-d1873b95a59b9103%40postgresql.org) |
| 18789 | 2025-01-29 | 17.2 | [BUG #18789: logical replication slots are deleted after failovers](https://www.postgresql.org/message-id/18789-0355be214b97e924%40postgresql.org) |
| 18791 | 2025-02-01 | 17.2 | [BUG #18791: Failed installtion during creation of spatial database](https://www.postgresql.org/message-id/18791-fc17338f329ee773%40postgresql.org) |
| 18792 | 2025-02-03 | 17.2 | [BUG #18792: Segmentaion Fault error when changing new parameter synchronized_standby_slots](https://www.postgresql.org/message-id/18792-1d848ad538b1033c%40postgresql.org) |
| 18793 | 2025-02-04 | 17.2 | [BUG #18793: PLpgSQL Function Returning Type of Table is not match for varchar(n) data type via Return Query](https://www.postgresql.org/message-id/18793-07a72289887f0966%40postgresql.org) |
| 18794 | 2025-02-05 | 17.2 | [BUG #18794: pgBouncer Windows installation error due to a simple sql bug???](https://www.postgresql.org/message-id/18794-2686f53414ec4bdb%40postgresql.org) |
| 18795 | 2025-02-05 | 17.2 | [BUG #18795: Norwegian bokmål crashes again](https://www.postgresql.org/message-id/18795-268389c4e50cbd4e%40postgresql.org) |
| 18800 | 2025-02-07 | 17.2 | [BUG #18800: Error while using pg_combinebackup](https://www.postgresql.org/message-id/18800-8b51806e266e3ffa%40postgresql.org) |
| 18801 | 2025-02-09 | 17.2 | [BUG #18801: JIT recompiles function for each row if custom aggregation function is used](https://www.postgresql.org/message-id/18801-8657563d6f52110b%40postgresql.org) |
| 18802 | 2025-02-11 | 17.2 | [BUG #18802: password field in log](https://www.postgresql.org/message-id/18802-76811f468ad4c4cd%40postgresql.org) |
| 18805 | 2025-02-12 | 17.2 | [BUG #18805: A specific query on a hash partitioned table always causes a "signal 11: Segmentation fault" error.](https://www.postgresql.org/message-id/18805-2477a1f983db961e%40postgresql.org) |
| 18806 | 2025-02-12 | 17.2 | [BUG #18806: When enable_rartitionwise_join is set to ON, the database shuts down abnormally](https://www.postgresql.org/message-id/18806-d70b0c9fdf63dcbf%40postgresql.org) |
| 18810 | 2025-02-13 | 17.2 | [BUG #18810: invalid value for parameter "synchronized_standby_slots" Caused error:"Segmentation fault"](https://www.postgresql.org/message-id/18810-226c754a49ea511f%40postgresql.org) |
| 18812 | 2025-02-14 | 17.2 | [BUG #18812: Conditional rule: inconsistent check for statement](https://www.postgresql.org/message-id/18812-565809b4823e2b68%40postgresql.org) |
| 18829 | 2025-03-02 | 17.2 | [BUG #18829: RAISE NOTICE appends 's' to string in PostgreSQL 17.2](https://www.postgresql.org/message-id/18829-2ed4d964795b3b57%40postgresql.org) |
| 18882 | 2025-04-08 | 17.2 | [BUG #18882: Unexpected write skew at SERIALIZABLE with psycopg2.connect()](https://www.postgresql.org/message-id/18882-d30fd598ffc3fbb2%40postgresql.org) |
| 18884 | 2025-04-08 | 17.2 | [BUG #18884: The CURRENT_TIMESTAMP value being returned in UTC-2.](https://www.postgresql.org/message-id/18884-d97000187e523225%40postgresql.org) |
| 18886 | 2025-04-09 | 17.2 | [BUG #18886: identity duplicate key](https://www.postgresql.org/message-id/18886-7a7ebc1b03f6ad9c%40postgresql.org) |
