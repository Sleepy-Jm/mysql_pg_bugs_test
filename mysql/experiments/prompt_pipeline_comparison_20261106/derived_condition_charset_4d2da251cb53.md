# 派生表条件下推与字符集：两批实验完整读本

[返回总览](README.md)

首次要求行依赖 CONCAT、无前缀非 ASCII 字面量、DISTINCT 与下推 ON/OFF；DeepSeek Stage 1 偏向显式字符集前缀，Stage 2 使用可折叠的 ASCII 常量 alpha，且没有 DISTINCT。两者均谈到克隆路径，但 DeepSeek 未保留首次暴露异常的构造。

首次：父提交每轮 8/8、目标 7/8；DCP01_ON 目标空集，父提交返回 id=1、4，HEX=61C3A9。DeepSeek：两侧每轮均为两组相同的 4 行结果。

## 0. 共同源码与 Stage 1 正式输入

两批以下文件逐字节一致。源码节选已含精确提交、父提交、源文件、行号、blob、Target observation 与局部范围说明。

DeepSeek 对应副本：[源码](../prompt_pipeline_deepseek_20261105/input_bundle/source-code-data/mysql/derived_condition_charset_4d2da251cb53.txt)、[Stage 1 提示词](../prompt_pipeline_deepseek_20261105/input_bundle/Prompts/mysql/src2req/derived_condition_charset_4d2da251cb53.txt)。

### 目标源码片段与上下文

原件：[derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/input_bundle/source-code-data/mysql/derived_condition_charset_4d2da251cb53.txt)

````text
Target: derived_condition_charset_4d2da251cb53
Target observation: Expression serialization and reparsing while cloning a derived-table expression during condition pushdown
Revision: 4d2da251cb536340d19438cc0039bb2846f9a634
Parent revision: e248166db3c95b4fc998ca14cff914f1fdafbe7b
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/sql_derived.cc
Blob: 85e57e802b720146f09d6a1086e8653e2f1c1258
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/sql_derived.cc
```cpp
550: static Item *parse_expression(THD *thd, Item *item, Query_block *query_block) {
551:   // Set up for parsing item
552:   LEX *const old_lex = thd->lex;
553:   LEX *new_lex = new (thd->mem_root) st_lex_local;
554: 
555:   thd->lex = new_lex;
556:   if (lex_start(thd)) {
557:     thd->lex = old_lex;
558:     return nullptr;  // OOM
559:   }
560:   // Take care not to print the variable index for stored procedure variables.
561:   // Also do not write a cloned stored procedure variable to query logs.
562:   thd->lex->reparse_derived_table_condition = true;
563:   // Get the printout of the expression
564:   StringBuffer<1024> str;
565:   // For printing parameters we need to specify the flag QT_NO_DATA_EXPANSION
566:   // because for a case when statement gets reprepared during execution, we
567:   // still need Item_param::print() to print the '?' rather than the actual data
568:   // specified for the parameter.
569:   // The flag QT_TO_ARGUMENT_CHARSET is required for printing character string
570:   // literals with correct character set introducer.
571:   item->print(thd, &str,
572:               enum_query_type(QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET));
573:   str.append('\0');
574: 
575:   Derived_expr_parser_state parser_state;
```
```cpp
617:   // Get a newly created item from parser
618:   bool result = parse_sql(thd, &parser_state, nullptr);
619: 
620:   thd->lex->reparse_derived_table_condition = false;
621:   // Delete the vector contents:
622:   std::vector<uint>().swap(thd->lex->reparse_derived_table_params_at);
623:   // thd->lex is now in a MEM_ROOT, so we need to delete:
624:   delete thd->lex->sroutines.release();
625: 
626:   // lex_end() would try to destroy sphead if set. So we reset it.
627:   thd->lex->set_sp_current_parsing_ctx(nullptr);
628:   thd->lex->sphead = nullptr;
629:   // End of parsing.
630:   lex_end(thd->lex);
631:   thd->lex = old_lex;
632:   thd->parsing_system_view = parsing_system_view_saved;
633:   if (result) return nullptr;
634: 
635:   return parser_state.result;
```
```cpp
734: Item *Query_block::clone_expression(THD *thd, Item *item) {
735:   Item *cloned_item = parse_expression(thd, item, this);
736:   if (cloned_item == nullptr) return nullptr;
737:   if (item->item_name.is_set())
738:     cloned_item->item_name.set(item->item_name.ptr(), item->item_name.length());
739: 
740:   // Collect details like table reference, field etc from the fields in the
741:   // original expression. Assign it to the corresponding field in the cloned
742:   // expression.
743:   if (copy_field_info(thd, item, cloned_item)) return nullptr;
744:   return resolve_expression(thd, cloned_item, this);
745: }
```
```cpp
976: bool TABLE_LIST::can_push_condition_to_derived(THD *thd) {
977:   Query_expression const *unit = derived_query_expression();
978:   return hint_table_state(thd, this, DERIVED_CONDITION_PUSHDOWN_HINT_ENUM,
979:                           OPTIMIZER_SWITCH_DERIVED_CONDITION_PUSHDOWN) &&  // 1
980:          !unit->has_any_limit() &&                                         // 2
981:          !is_inner_table_of_outer_join() &&                                // 3
982:          !(common_table_expr() &&
983:            (common_table_expr()->references.size() >= 2 ||
984:             common_table_expr()->recursive)) &&   // 4
985:          (thd->lex->set_var_list.elements == 0);  // 5
```

# Code: sql/item.cc
Blob: c23b13dc01f3bb968af124595e991115caac6c49
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/item.cc
```cpp
1042: Item *Item_field::replace_with_derived_expr(uchar *arg) {
1043:   Condition_pushdown::Derived_table_info *dti =
1044:       pointer_cast<Condition_pushdown::Derived_table_info *>(arg);
1045: 
1046:   // This column's table reference should be same as the derived table from
1047:   // where the replacement is retrieved. If not, it is presumed that the
1048:   // column has already been replaced with derived table expression (Maybe
1049:   // there was an earlier reference to the same column in the condition that
1050:   // is being pushed down). There is no need to do anything in such a case.
1051:   TABLE_LIST *derived_table = dti->m_derived_table;
1052:   if (derived_table != table_ref) return this;
1053:   Query_block *query_block = dti->m_derived_query_block;
1054:   return query_block->clone_expression(
1055:       current_thd, query_block->get_derived_expr(field->field_index()));
1056: }
```
```cpp
3426: void Item_string::print(const THD *, String *str,
3427:                         enum_query_type query_type) const {
3428:   if (query_type & QT_NORMALIZED_FORMAT) {
3429:     str->append("?");
3430:     return;
3431:   }
3432: 
3433:   const bool print_introducer =
3434:       (query_type & QT_FORCE_INTRODUCERS) ||
3435:       (!(query_type & QT_WITHOUT_INTRODUCERS) && is_cs_specified());
3436: 
3437:   if (print_introducer) {
3438:     str->append('_');
3439:     str->append(collation.collation->csname);
3440:   }
3441: 
3442:   str->append('\'');
3443: 
3444:   if (query_type & QT_TO_SYSTEM_CHARSET) {
3445:     if (print_introducer) {
3446:       /*
3447:         Because we wrote an introducer, we must print str_value in its
3448:         charset, and the resulting bytes must not be changed until they
3449:         reach the end client.
3450:         But the caller is asking for system_charset_info, and may later
3451:         convert into character_set_results. That means two conversions: we
3452:         must ensure that they don't change our printed bytes.
3453:         So we print str_value in the least common denominator of the three
3454:         charsets involved: ASCII. Non-ASCII characters are printed as \xFF
3455:         sequences (which is ASCII too). This way, our bytes will not be
3456:         changed.
3457:       */
3458:       ErrConvString tmp(str_value.ptr(), str_value.length(), &my_charset_bin);
3459:       str->append(tmp.ptr());
3460:     } else {
3461:       // Convert to system charset.
3462:       convert_and_print(&str_value, str, system_charset_info);
3463:     }
3464:   } else if (query_type & QT_TO_ARGUMENT_CHARSET) {
3465:     if (print_introducer)
3466:       convert_and_print(&str_value, str, collation.collation);
3467:     else
3468:       /*
3469:         Convert the string literals to str->charset(),
3470:         which is typically equal to charset_set_client.
3471:       */
3472:       convert_and_print(&str_value, str, str->charset());
3473:   } else {
3474:     // Caller wants a result in the charset of str_value.
3475:     str_value.print(str);
3476:   }
3477: 
3478:   str->append('\'');
3479: }
```

# Code: include/sql_string.h
Blob: 32d0e43d13248025d980d5acc875e4ed4ff633d3
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/include/sql_string.h
```cpp
629: class StringBuffer : public String {
630:   char buff[buff_sz];
631: 
632:  public:
633:   StringBuffer() : String(buff, buff_sz, &my_charset_bin) { length(0); }
634:   explicit StringBuffer(const CHARSET_INFO *cs) : String(buff, buff_sz, cs) {
635:     length(0);
636:   }
637:   StringBuffer(const char *str, size_t length, const CHARSET_INFO *cs)
638:       : String(buff, buff_sz, cs) {
639:     set(str, length, cs);
```
````

### 共同的完整 Stage 1 提示词（含示例及当前源码）

原件：[derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/src2req/derived_condition_charset_4d2da251cb53.txt)

````text
### Example task
Describe the high-level MySQL test requirements that can reach the specified source target. Focus on the SQL, data, configuration, and operation sequence needed by a test generator. Distinguish source-required conditions from candidate constructions and unresolved reachability. Do not merely explain the implementation or repeat the patch.

# Target and source code
Target: intersect_join
Target observation: JOIN::get_best_combination: select JT_ALL for an INTERSECT/EXCEPT materialized TABLE
Revision: fac72fe1704c542ba476ef065dee03d2c1da83ae
Parent revision: 5d02c10206d5d41b1b7d0558b15acf0955d26ed5
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/sql_optimizer.cc
Blob: 91f067c12f7e26c565814b5f07d4f8ace68b475b
Source: https://github.com/mysql/mysql-server/blob/fac72fe1704c542ba476ef065dee03d2c1da83ae/sql/sql_optimizer.cc
```cpp
3180:     const uint target =
3181:         (remaining_sjm_inner--) > 0 ? inner_target++ : outer_target++;
3182:     JOIN_TAB *const tab = pos->table;
3183:
3184:     best_ref[target] = tab;
3185:     tab->set_idx(target);
3186:     tab->set_position(pos);
3187:     TABLE *const table = tab->table();
3188:     if (tab->type() != JT_CONST && tab->type() != JT_SYSTEM) {
3189:       if (pos->sj_strategy == SJ_OPT_LOOSE_SCAN && tab->range_scan() &&
3190:           used_index(tab->range_scan()) != pos->loosescan_key) {
3191:         /*
3192:           We must use the duplicate-eliminating index, so this QUICK is not
3193:           an option.
3194:         */
3195:         ::destroy(tab->range_scan());
3196:         tab->set_range_scan(nullptr);
3197:       }
3198:       if (table->is_intersect() || table->is_except()) {
3199:         tab->set_type(JT_ALL);  // INTERSECT, EXCEPT can't use ref access yet
3200:       } else if (!pos->key) {
3201:         if (tab->range_scan())
3202:           tab->set_type(calc_join_type(tab->range_scan()));
3203:         else
3204:           tab->set_type(JT_ALL);
3205:       } else {
3206:         // REF or RANGE, clarify later when prefix tables are set for JOIN_TABs
3207:         tab->set_type(JT_REF);
3208:       }
3209:     }
3210:     assert(tab->type() != JT_UNKNOWN);
```

# Description
Target
MySQL revision fac72fe1704c542ba476ef065dee03d2c1da83ae, sql/sql_optimizer.cc:3198-3199: the INTERSECT/EXCEPT materialized-table branch that selects JT_ALL. This is a source-derived candidate, not an executed reproduction.

Source-required conditions
The current JOIN_TAB is neither JT_CONST nor JT_SYSTEM (line 3188). Its TABLE reports is_intersect() or is_except() (line 3198). The branch assigns JT_ALL (line 3199).

Candidate construction
Join a derived table containing INTERSECT ALL with a small outer table on an integer key. Give the left input three copies of 1 and one copy of 2, the right input two copies of 1 and one copy of 3, and the outer table two copies of 1 and one copy of 2. This exposes duplicate multiplicities. The equality join is a candidate for presenting the materialized table as a join input; it does not guarantee a particular optimizer plan. INTERSECT ALL is the concrete demonstration; EXCEPT and DISTINCT are optional separate variants.

Correctness oracle
For each key k, INTERSECT ALL has min(left_count(k), right_count(k)) rows. An equality join multiplies that by outer_count(k). The stated data therefore produces exactly four rows containing 1. Derive this from the inserted data, not from the other server version's output.

Coverage observation
On the specified revision, use a breakpoint or instrumentation at sql/sql_optimizer.cc:3198-3199 and identify the derived TABLE for this query. Record its set-operation flags, incoming JOIN_TAB type, and the JT_ALL assignment. EXPLAIN alone is only a plan clue.

Uncertainty
The local excerpt does not establish the full SQL-to-TABLE construction path. If the query does not reach the target, inspect materialization and join-planning callers before revising the candidate. Coverage and correct output are separate observations.

### Current task
Describe the high-level MySQL test requirements for the following target, following the example's format. Cite the supplied revision, file, and line numbers for source conditions. Keep coverage evidence separate from a correctness oracle. If the local excerpt does not establish a SQL-to-branch mapping, identify the missing caller/helper evidence. Do not invent configuration switches or claim execution. Output only the description for the current task, using: Target; Source-required conditions; Candidate construction; Correctness oracle; Coverage observation; Uncertainty.

# Target and source code
Target: derived_condition_charset_4d2da251cb53
Target observation: Expression serialization and reparsing while cloning a derived-table expression during condition pushdown
Revision: 4d2da251cb536340d19438cc0039bb2846f9a634
Parent revision: e248166db3c95b4fc998ca14cff914f1fdafbe7b
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/sql_derived.cc
Blob: 85e57e802b720146f09d6a1086e8653e2f1c1258
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/sql_derived.cc
```cpp
550: static Item *parse_expression(THD *thd, Item *item, Query_block *query_block) {
551:   // Set up for parsing item
552:   LEX *const old_lex = thd->lex;
553:   LEX *new_lex = new (thd->mem_root) st_lex_local;
554: 
555:   thd->lex = new_lex;
556:   if (lex_start(thd)) {
557:     thd->lex = old_lex;
558:     return nullptr;  // OOM
559:   }
560:   // Take care not to print the variable index for stored procedure variables.
561:   // Also do not write a cloned stored procedure variable to query logs.
562:   thd->lex->reparse_derived_table_condition = true;
563:   // Get the printout of the expression
564:   StringBuffer<1024> str;
565:   // For printing parameters we need to specify the flag QT_NO_DATA_EXPANSION
566:   // because for a case when statement gets reprepared during execution, we
567:   // still need Item_param::print() to print the '?' rather than the actual data
568:   // specified for the parameter.
569:   // The flag QT_TO_ARGUMENT_CHARSET is required for printing character string
570:   // literals with correct character set introducer.
571:   item->print(thd, &str,
572:               enum_query_type(QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET));
573:   str.append('\0');
574: 
575:   Derived_expr_parser_state parser_state;
```
```cpp
617:   // Get a newly created item from parser
618:   bool result = parse_sql(thd, &parser_state, nullptr);
619: 
620:   thd->lex->reparse_derived_table_condition = false;
621:   // Delete the vector contents:
622:   std::vector<uint>().swap(thd->lex->reparse_derived_table_params_at);
623:   // thd->lex is now in a MEM_ROOT, so we need to delete:
624:   delete thd->lex->sroutines.release();
625: 
626:   // lex_end() would try to destroy sphead if set. So we reset it.
627:   thd->lex->set_sp_current_parsing_ctx(nullptr);
628:   thd->lex->sphead = nullptr;
629:   // End of parsing.
630:   lex_end(thd->lex);
631:   thd->lex = old_lex;
632:   thd->parsing_system_view = parsing_system_view_saved;
633:   if (result) return nullptr;
634: 
635:   return parser_state.result;
```
```cpp
734: Item *Query_block::clone_expression(THD *thd, Item *item) {
735:   Item *cloned_item = parse_expression(thd, item, this);
736:   if (cloned_item == nullptr) return nullptr;
737:   if (item->item_name.is_set())
738:     cloned_item->item_name.set(item->item_name.ptr(), item->item_name.length());
739: 
740:   // Collect details like table reference, field etc from the fields in the
741:   // original expression. Assign it to the corresponding field in the cloned
742:   // expression.
743:   if (copy_field_info(thd, item, cloned_item)) return nullptr;
744:   return resolve_expression(thd, cloned_item, this);
745: }
```
```cpp
976: bool TABLE_LIST::can_push_condition_to_derived(THD *thd) {
977:   Query_expression const *unit = derived_query_expression();
978:   return hint_table_state(thd, this, DERIVED_CONDITION_PUSHDOWN_HINT_ENUM,
979:                           OPTIMIZER_SWITCH_DERIVED_CONDITION_PUSHDOWN) &&  // 1
980:          !unit->has_any_limit() &&                                         // 2
981:          !is_inner_table_of_outer_join() &&                                // 3
982:          !(common_table_expr() &&
983:            (common_table_expr()->references.size() >= 2 ||
984:             common_table_expr()->recursive)) &&   // 4
985:          (thd->lex->set_var_list.elements == 0);  // 5
```

# Code: sql/item.cc
Blob: c23b13dc01f3bb968af124595e991115caac6c49
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/sql/item.cc
```cpp
1042: Item *Item_field::replace_with_derived_expr(uchar *arg) {
1043:   Condition_pushdown::Derived_table_info *dti =
1044:       pointer_cast<Condition_pushdown::Derived_table_info *>(arg);
1045: 
1046:   // This column's table reference should be same as the derived table from
1047:   // where the replacement is retrieved. If not, it is presumed that the
1048:   // column has already been replaced with derived table expression (Maybe
1049:   // there was an earlier reference to the same column in the condition that
1050:   // is being pushed down). There is no need to do anything in such a case.
1051:   TABLE_LIST *derived_table = dti->m_derived_table;
1052:   if (derived_table != table_ref) return this;
1053:   Query_block *query_block = dti->m_derived_query_block;
1054:   return query_block->clone_expression(
1055:       current_thd, query_block->get_derived_expr(field->field_index()));
1056: }
```
```cpp
3426: void Item_string::print(const THD *, String *str,
3427:                         enum_query_type query_type) const {
3428:   if (query_type & QT_NORMALIZED_FORMAT) {
3429:     str->append("?");
3430:     return;
3431:   }
3432: 
3433:   const bool print_introducer =
3434:       (query_type & QT_FORCE_INTRODUCERS) ||
3435:       (!(query_type & QT_WITHOUT_INTRODUCERS) && is_cs_specified());
3436: 
3437:   if (print_introducer) {
3438:     str->append('_');
3439:     str->append(collation.collation->csname);
3440:   }
3441: 
3442:   str->append('\'');
3443: 
3444:   if (query_type & QT_TO_SYSTEM_CHARSET) {
3445:     if (print_introducer) {
3446:       /*
3447:         Because we wrote an introducer, we must print str_value in its
3448:         charset, and the resulting bytes must not be changed until they
3449:         reach the end client.
3450:         But the caller is asking for system_charset_info, and may later
3451:         convert into character_set_results. That means two conversions: we
3452:         must ensure that they don't change our printed bytes.
3453:         So we print str_value in the least common denominator of the three
3454:         charsets involved: ASCII. Non-ASCII characters are printed as \xFF
3455:         sequences (which is ASCII too). This way, our bytes will not be
3456:         changed.
3457:       */
3458:       ErrConvString tmp(str_value.ptr(), str_value.length(), &my_charset_bin);
3459:       str->append(tmp.ptr());
3460:     } else {
3461:       // Convert to system charset.
3462:       convert_and_print(&str_value, str, system_charset_info);
3463:     }
3464:   } else if (query_type & QT_TO_ARGUMENT_CHARSET) {
3465:     if (print_introducer)
3466:       convert_and_print(&str_value, str, collation.collation);
3467:     else
3468:       /*
3469:         Convert the string literals to str->charset(),
3470:         which is typically equal to charset_set_client.
3471:       */
3472:       convert_and_print(&str_value, str, str->charset());
3473:   } else {
3474:     // Caller wants a result in the charset of str_value.
3475:     str_value.print(str);
3476:   }
3477: 
3478:   str->append('\'');
3479: }
```

# Code: include/sql_string.h
Blob: 32d0e43d13248025d980d5acc875e4ed4ff633d3
Source: https://github.com/mysql/mysql-server/blob/4d2da251cb536340d19438cc0039bb2846f9a634/include/sql_string.h
```cpp
629: class StringBuffer : public String {
630:   char buff[buff_sz];
631: 
632:  public:
633:   StringBuffer() : String(buff, buff_sz, &my_charset_bin) { length(0); }
634:   explicit StringBuffer(const CHARSET_INFO *cs) : String(buff, buff_sz, cs) {
635:     length(0);
636:   }
637:   StringBuffer(const char *str, size_t length, const CHARSET_INFO *cs)
638:       : String(buff, buff_sz, cs) {
639:     set(str, length, cs);
```

# Description
````

### 输入包中其他上下文与来源

下列文件用于区分模板、示例、种子和正式输入；完整正式提示词已经展示在本读本，不能将包内每个文件都视为实际进入模型上下文。

- [provenance.json](../prompt_pipeline_20261104/generation/input_bundle/provenance.json)
- [README.txt](../prompt_pipeline_20261104/generation/input_bundle/README.txt)
- [optim/mysql.json](../prompt_pipeline_20261104/generation/input_bundle/optim/mysql.json)
- [template-mysql/src2req.txt](../prompt_pipeline_20261104/generation/input_bundle/template-mysql/src2req.txt)
- [template-mysql/req2test.txt](../prompt_pipeline_20261104/generation/input_bundle/template-mysql/req2test.txt)
- [source-code-data/mysql/intersect_join.txt](../prompt_pipeline_20261104/generation/input_bundle/source-code-data/mysql/intersect_join.txt)
- [template-mysql/examples/intersect_join.requirements.txt](../prompt_pipeline_20261104/generation/input_bundle/template-mysql/examples/intersect_join.requirements.txt)
- [template-mysql/examples/intersect_join.test.txt](../prompt_pipeline_20261104/generation/input_bundle/template-mysql/examples/intersect_join.test.txt)
- [Requirements/mysql/req/derived_condition_charset_4d2da251cb53/derived_condition_charset_4d2da251cb53_1.txt](../prompt_pipeline_20261104/generation/input_bundle/Requirements/mysql/req/derived_condition_charset_4d2da251cb53/derived_condition_charset_4d2da251cb53_1.txt)
- [Prompts/mysql/req2test/derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/req2test/derived_condition_charset_4d2da251cb53.txt)

## 1. 首次 Codex

上下文：同一助手共享对话，无独立 API 信封；[生成清单](../prompt_pipeline_20261104/generation/generation_manifest.json)，[上下文审查](../prompt_pipeline_20261104/contamination_review.md)。生成清单中的未执行状态为历史快照，后续执行见本节运行证据。

### Stage 1 输出：测试偏好与需求原文

原件：[derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/stage1_src2req/derived_condition_charset_4d2da251cb53.txt)

````text
Target
Revision 4d2da251cb536340d19438cc0039bb2846f9a634; parent e248166db3c95b4fc998ca14cff914f1fdafbe7b. Exercise cloning of a derived-table output expression during condition pushdown, including Item_string printing with QT_TO_ARGUMENT_CHARSET and subsequent reparsing. The observation chain is Item_field::replace_with_derived_expr (sql/item.cc:1042-1055), Query_block::clone_expression (sql/sql_derived.cc:734-744), and parse_expression (sql/sql_derived.cc:550-575,617-635).

Source-required conditions
The analysis stage extracted these local constraints from the supplied target-revision source:
1. Condition pushdown must be enabled for the derived table. The local eligibility test rejects an inner LIMIT, the inner side of an outer join, multiply referenced or recursive CTEs, and the indicated set_var_list state (sql/sql_derived.cc:976-985). These are local necessary checks, not an exhaustive proof of eligibility.
2. The Item_field being replaced must refer to the same derived table as the pushdown information; otherwise replacement returns early (sql/item.cc:1051-1055). The outer predicate should reference an output alias whose underlying expression contains a string literal.
3. clone_expression must reach item->print and successful parse_sql rather than an error return. The print flags include QT_NO_DATA_EXPANSION and QT_TO_ARGUMENT_CHARSET (sql/sql_derived.cc:564-572,617-635).
4. To exercise Item_string::print, retain a character-string literal in a nonconstant expression. Explicit character-set introducers and implicit literals select different print_introducer branches (sql/item.cc:3433-3439,3464-3472). A default-constructed StringBuffer uses my_charset_bin (include/sql_string.h:629-639); do not assume this particular buffer is initialized with character_set_client merely from the nearby generic comment.

Candidate construction
Use one small ordinary InnoDB table with an integer id and a utf8mb4_bin VARCHAR column. Populate two rows containing 'a', a 'b', an empty string, and NULL. Select DISTINCT id and CONCAT(s, literal) in a derived table; place the filtering predicate on the derived output alias. DISTINCT is a candidate way to keep the derived table materialized. Use no inner LIMIT, outer join, CTE, or user-variable assignment inside the query. Use an ordinary table so the experiment does not depend on additional temporary-table eligibility rules.
Cover four literal constructions: unintroduced UTF-8 'é'; explicitly introduced _utf8mb4'é'; explicitly introduced _utf8mb4'中'; and a literal containing a quote, _utf8mb4'O''Reilly'. Keep the SQL file UTF-8 and the connection utf8mb4. The introducer identifies the bytes' character set; it does not convert incorrectly encoded file bytes. The UTF-8 tests need no non-UTF-8 file encoding.
Use derived_condition_pushdown=off and =on on the same query/data as a control and a candidate target execution. Save and restore the session optimizer setting. Choose a row-dependent CONCAT rather than a constant-only expression, to reduce constant folding of the expression to be cloned. Select HEX(tag), CHAR_LENGTH(tag) and OCTET_LENGTH(tag) so encoding errors are visible without relying on terminal rendering.

Correctness oracle
Compute CONCAT, equality, UTF-8 bytes and lengths directly from the inserted characters. For a suffix 'é', rows whose s='a' must have tag='aé', HEX(tag)=61C3A9, character length 2 and byte length 3. For suffix '中', the corresponding values are 'a中', 61E4B8AD, 2 and 4. For suffix "O'Reilly", they are "aO'Reilly", 614F275265696C6C79, 9 and 9. Both duplicate 'a' source rows must remain because DISTINCT also includes their different ids. A NULL s produces a NULL CONCAT and does not pass equality. Both switch modes must independently satisfy these expected rows; agreement alone is insufficient.

Coverage observation
Record that the target derived table is materialized and its outer alias is pushed down. At the supplied revision, trace Item_field::replace_with_derived_expr to clone_expression and parse_expression. Capture the original expression, Item_string character set, is_cs_specified/print_introducer, print flags, output StringBuffer character set, serialized bytes, parse status and cloned expression. Associate the events with each query id. EXPLAIN or an on/off result difference cannot alone prove the exact printing branch.

Uncertainty
The snippets omit parts of the pushdown traversal, parse-state initialization, conversion helper and surrounding optimizer transformations. They do not guarantee that each SQL candidate reaches cloning or retains its literal through rewrites. A missed target requires analysis of those missing callers/helpers. A parse error may be a target symptom or a generation/configuration error and must be classified with diagnostics. Do not infer a specific server release containing the target commit from its SHA alone. These requirements were produced in this assistant turn from the src2req prompt; no database execution or measured coverage has occurred.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/stage2_req2test/prompts/derived_condition_charset_4d2da251cb53.txt)

````text
### Example task
Generate a self-contained MySQL SQL test and its inputs from the requirements below. Include setup, deterministic queries, independently derived expected results, and cleanup. Explain how to observe the source target separately from checking SQL results.

# Description of requirements
Target
MySQL revision fac72fe1704c542ba476ef065dee03d2c1da83ae, sql/sql_optimizer.cc:3198-3199: the INTERSECT/EXCEPT materialized-table branch that selects JT_ALL. This is a source-derived candidate, not an executed reproduction.

Source-required conditions
The current JOIN_TAB is neither JT_CONST nor JT_SYSTEM (line 3188). Its TABLE reports is_intersect() or is_except() (line 3198). The branch assigns JT_ALL (line 3199).

Candidate construction
Join a derived table containing INTERSECT ALL with a small outer table on an integer key. Give the left input three copies of 1 and one copy of 2, the right input two copies of 1 and one copy of 3, and the outer table two copies of 1 and one copy of 2. This exposes duplicate multiplicities. The equality join is a candidate for presenting the materialized table as a join input; it does not guarantee a particular optimizer plan. INTERSECT ALL is the concrete demonstration; EXCEPT and DISTINCT are optional separate variants.

Correctness oracle
For each key k, INTERSECT ALL has min(left_count(k), right_count(k)) rows. An equality join multiplies that by outer_count(k). The stated data therefore produces exactly four rows containing 1. Derive this from the inserted data, not from the other server version's output.

Coverage observation
On the specified revision, use a breakpoint or instrumentation at sql/sql_optimizer.cc:3198-3199 and identify the derived TABLE for this query. Record its set-operation flags, incoming JOIN_TAB type, and the JT_ALL assignment. EXPLAIN alone is only a plan clue.

Uncertainty
The local excerpt does not establish the full SQL-to-TABLE construction path. If the query does not reach the target, inspect materialization and join-planning callers before revising the candidate. Coverage and correct output are separate observations.

# Test
Prerequisites
Use a disposable, already selected schema on a MySQL build supporting INTERSECT ALL. The source coverage target is revision fac72fe1704c542ba476ef065dee03d2c1da83ae; do not infer that every release has identical source locations. Use a fresh session with no existing objects named wf_demo_a, wf_demo_b, or wf_demo_c.

SQL
```sql
CREATE TEMPORARY TABLE wf_demo_a (k INT NOT NULL);
CREATE TEMPORARY TABLE wf_demo_b (k INT NOT NULL);
CREATE TEMPORARY TABLE wf_demo_c (k INT NOT NULL);
INSERT INTO wf_demo_a VALUES (1), (1), (1), (2);
INSERT INTO wf_demo_b VALUES (1), (1), (3);
INSERT INTO wf_demo_c VALUES (1), (1), (2);

SELECT d.k
FROM (
  SELECT k FROM wf_demo_a
  INTERSECT ALL
  SELECT k FROM wf_demo_b
) AS d
JOIN wf_demo_c AS c ON d.k = c.k
ORDER BY d.k;

DROP TEMPORARY TABLE wf_demo_c;
DROP TEMPORARY TABLE wf_demo_b;
DROP TEMPORARY TABLE wf_demo_a;
```

Expected results and oracle
The SELECT returns four rows, each with k=1. The intersection contains min(3,2)=2 copies of 1 and no other keys; joining the two outer copies produces 2*2=4 rows. Compare row multiplicities, not just distinct values. If setup or the SELECT fails, retain that failure separately; close the session to release remaining temporary tables.

Coverage observation
Observe sql/sql_optimizer.cc:3198-3199 at the specified revision. Identify d's materialized TABLE, verify its is_intersect() flag and nonconstant JOIN_TAB, and record the JT_ALL assignment. The expected result does not itself prove this branch was reached.

Execution status
Authored one-shot demonstration; SQL and branch coverage have not been executed or measured.

### Current task
Generate a new MySQL test that satisfies the following requirements. Follow the example's format, but use the current target's operations and data. Supply complete SQL without placeholders, expected rows with a derivation, cleanup, and a separate coverage observation plan. Use an already selected disposable test schema; use temporary tables when compatible with the target, otherwise use uniquely named ordinary tables and clean up only objects created by the test. Specify session ordering if multiple connections are required. If an essential precondition is unresolved, state it instead of claiming guaranteed coverage. Do not execute the test or describe generated SQL as a reproduced bug. Output only: Prerequisites; SQL; Expected results and oracle; Coverage observation; Execution status.

# Description of requirements
Target
Revision 4d2da251cb536340d19438cc0039bb2846f9a634; parent e248166db3c95b4fc998ca14cff914f1fdafbe7b. Exercise cloning of a derived-table output expression during condition pushdown, including Item_string printing with QT_TO_ARGUMENT_CHARSET and subsequent reparsing. The observation chain is Item_field::replace_with_derived_expr (sql/item.cc:1042-1055), Query_block::clone_expression (sql/sql_derived.cc:734-744), and parse_expression (sql/sql_derived.cc:550-575,617-635).

Source-required conditions
The analysis stage extracted these local constraints from the supplied target-revision source:
1. Condition pushdown must be enabled for the derived table. The local eligibility test rejects an inner LIMIT, the inner side of an outer join, multiply referenced or recursive CTEs, and the indicated set_var_list state (sql/sql_derived.cc:976-985). These are local necessary checks, not an exhaustive proof of eligibility.
2. The Item_field being replaced must refer to the same derived table as the pushdown information; otherwise replacement returns early (sql/item.cc:1051-1055). The outer predicate should reference an output alias whose underlying expression contains a string literal.
3. clone_expression must reach item->print and successful parse_sql rather than an error return. The print flags include QT_NO_DATA_EXPANSION and QT_TO_ARGUMENT_CHARSET (sql/sql_derived.cc:564-572,617-635).
4. To exercise Item_string::print, retain a character-string literal in a nonconstant expression. Explicit character-set introducers and implicit literals select different print_introducer branches (sql/item.cc:3433-3439,3464-3472). A default-constructed StringBuffer uses my_charset_bin (include/sql_string.h:629-639); do not assume this particular buffer is initialized with character_set_client merely from the nearby generic comment.

Candidate construction
Use one small ordinary InnoDB table with an integer id and a utf8mb4_bin VARCHAR column. Populate two rows containing 'a', a 'b', an empty string, and NULL. Select DISTINCT id and CONCAT(s, literal) in a derived table; place the filtering predicate on the derived output alias. DISTINCT is a candidate way to keep the derived table materialized. Use no inner LIMIT, outer join, CTE, or user-variable assignment inside the query. Use an ordinary table so the experiment does not depend on additional temporary-table eligibility rules.
Cover four literal constructions: unintroduced UTF-8 'é'; explicitly introduced _utf8mb4'é'; explicitly introduced _utf8mb4'中'; and a literal containing a quote, _utf8mb4'O''Reilly'. Keep the SQL file UTF-8 and the connection utf8mb4. The introducer identifies the bytes' character set; it does not convert incorrectly encoded file bytes. The UTF-8 tests need no non-UTF-8 file encoding.
Use derived_condition_pushdown=off and =on on the same query/data as a control and a candidate target execution. Save and restore the session optimizer setting. Choose a row-dependent CONCAT rather than a constant-only expression, to reduce constant folding of the expression to be cloned. Select HEX(tag), CHAR_LENGTH(tag) and OCTET_LENGTH(tag) so encoding errors are visible without relying on terminal rendering.

Correctness oracle
Compute CONCAT, equality, UTF-8 bytes and lengths directly from the inserted characters. For a suffix 'é', rows whose s='a' must have tag='aé', HEX(tag)=61C3A9, character length 2 and byte length 3. For suffix '中', the corresponding values are 'a中', 61E4B8AD, 2 and 4. For suffix "O'Reilly", they are "aO'Reilly", 614F275265696C6C79, 9 and 9. Both duplicate 'a' source rows must remain because DISTINCT also includes their different ids. A NULL s produces a NULL CONCAT and does not pass equality. Both switch modes must independently satisfy these expected rows; agreement alone is insufficient.

Coverage observation
Record that the target derived table is materialized and its outer alias is pushed down. At the supplied revision, trace Item_field::replace_with_derived_expr to clone_expression and parse_expression. Capture the original expression, Item_string character set, is_cs_specified/print_introducer, print flags, output StringBuffer character set, serialized bytes, parse status and cloned expression. Associate the events with each query id. EXPLAIN or an on/off result difference cannot alone prove the exact printing branch.

Uncertainty
The snippets omit parts of the pushdown traversal, parse-state initialization, conversion helper and surrounding optimizer transformations. They do not guarantee that each SQL candidate reaches cloning or retains its literal through rewrites. A missed target requires analysis of those missing callers/helpers. A parse error may be a target symptom or a generation/configuration error and must be classified with diagnostics. Do not infer a specific server release containing the target commit from its SHA alone. These requirements were produced in this assistant turn from the src2req prompt; no database execution or measured coverage has occurred.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[derived_condition_charset_4d2da251cb53.txt](../prompt_pipeline_20261104/generation/stage2_req2test/responses/derived_condition_charset_4d2da251cb53.txt)

````text
Prerequisites
Use a MySQL build supporting derived_condition_pushdown, utf8mb4 and utf8mb4_bin; bind source coverage to the target SHA, not an assumed release label. Use a fresh session and an already selected disposable schema with CREATE/DROP privileges. The ordinary table wf_4d2_text must not exist. Read this file as UTF-8; it contains real é and 中 literals. The script saves/restores its optimizer and connection-character-set settings on normal completion. If it aborts, retain diagnostics, close the session and drop only this run's table after confirming it was created by this run.

SQL
```sql
-- UTF-8 file. Run in a fresh session with a selected disposable schema.
-- Target: 4d2da251cb536340d19438cc0039bb2846f9a634.
-- wf_4d2_text must not already exist. No pre-test DROP of unknown objects.
SELECT VERSION() AS server_version, DATABASE() AS test_schema,
       @@SESSION.optimizer_switch AS initial_optimizer_switch;
SET @wf_4d2_optimizer = @@SESSION.optimizer_switch;
SET @wf_4d2_client = @@SESSION.character_set_client;
SET @wf_4d2_results = @@SESSION.character_set_results;
SET @wf_4d2_collation = @@SESSION.collation_connection;
SET NAMES utf8mb4 COLLATE utf8mb4_bin;
CREATE TABLE wf_4d2_text (
  id INT PRIMARY KEY,
  s VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
) ENGINE=InnoDB;
INSERT INTO wf_4d2_text VALUES (1,'a'),(2,'b'),(3,''),(4,'a'),(5,NULL);

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP01_OFF
SELECT 'DCP01_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP01_ON
SELECT 'DCP01_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP02_OFF
SELECT 'DCP02_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP02_ON
SELECT 'DCP02_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP03_OFF
SELECT 'DCP03_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP03_ON
SELECT 'DCP03_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP04_OFF
SELECT 'DCP04_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP04_ON
SELECT 'DCP04_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

-- Cleanup and session restoration after all data results.
DROP TABLE wf_4d2_text;
SET SESSION optimizer_switch = @wf_4d2_optimizer;
SET SESSION character_set_client = @wf_4d2_client;
SET SESSION character_set_results = @wf_4d2_results;
SET SESSION collation_connection = @wf_4d2_collation;
```

Expected results and oracle
Each suffix matches exactly ids 1 and 4, whose input s is 'a'. DISTINCT includes id, so these two rows remain distinct. Compute UTF-8 bytes directly from 'a'+suffix: 61C3A9; 61E4B8AD; or 614F275265696C6C79. Character/byte lengths are 2/3, 2/4, or 9/9. NULL fails equality. Each OFF and ON result must match the independently specified rows, not merely match one another.

DCP01_OFF: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61C3A9", 2, 3], [4, "61C3A9", 2, 3]]
DCP01_ON: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61C3A9", 2, 3], [4, "61C3A9", 2, 3]]
DCP02_OFF: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61C3A9", 2, 3], [4, "61C3A9", 2, 3]]
DCP02_ON: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61C3A9", 2, 3], [4, "61C3A9", 2, 3]]
DCP03_OFF: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61E4B8AD", 2, 4], [4, "61E4B8AD", 2, 4]]
DCP03_ON: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "61E4B8AD", 2, 4], [4, "61E4B8AD", 2, 4]]
DCP04_OFF: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "614F275265696C6C79", 9, 9], [4, "614F275265696C6C79", 9, 9]]
DCP04_ON: columns=['id', 'tag_hex', 'char_len', 'byte_len']; expected=[[1, "614F275265696C6C79", 9, 9], [4, "614F275265696C6C79", 9, 9]]

Coverage observation
For each ON case, identify the materialized derived table and trace sql/item.cc:1051-1055 to sql/sql_derived.cc:734-744 and parse_expression:550-575,617-635. Record Item_string::print at sql/item.cc:3433-3472: introducer decision, literal collation, QT_TO_ARGUMENT_CHARSET, destination StringBuffer charset, serialized bytes and reparse result. Inspect that the implicit and explicit cases take their intended branches. OFF is a path control; it is not a correctness authority. No runtime path is asserted by this generated response.

Execution status
Generated by the current assistant from the saved req2test prompt and its new src2req requirements. No database was connected, SQL executed, or source coverage measured. Expected rows are semantic calculations, not observed results. Retain SQL errors/crashes/missing results as separate observations; do not silently treat them as correct or as confirmed bugs.
````

### 提取后实际执行的完整 SQL

原件：[derived_condition_charset_4d2da251cb53.sql](../prompt_pipeline_20261104/generation/sql/derived_condition_charset_4d2da251cb53.sql)

````sql
-- UTF-8 file. Run in a fresh session with a selected disposable schema.
-- Target: 4d2da251cb536340d19438cc0039bb2846f9a634.
-- wf_4d2_text must not already exist. No pre-test DROP of unknown objects.
SELECT VERSION() AS server_version, DATABASE() AS test_schema,
       @@SESSION.optimizer_switch AS initial_optimizer_switch;
SET @wf_4d2_optimizer = @@SESSION.optimizer_switch;
SET @wf_4d2_client = @@SESSION.character_set_client;
SET @wf_4d2_results = @@SESSION.character_set_results;
SET @wf_4d2_collation = @@SESSION.collation_connection;
SET NAMES utf8mb4 COLLATE utf8mb4_bin;
CREATE TABLE wf_4d2_text (
  id INT PRIMARY KEY,
  s VARCHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
) ENGINE=InnoDB;
INSERT INTO wf_4d2_text VALUES (1,'a'),(2,'b'),(3,''),(4,'a'),(5,NULL);

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP01_OFF
SELECT 'DCP01_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP01_ON
SELECT 'DCP01_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, 'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP02_OFF
SELECT 'DCP02_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP02_ON
SELECT 'DCP02_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'é') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aé' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP03_OFF
SELECT 'DCP03_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP03_ON
SELECT 'DCP03_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'中') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'a中' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

-- CASE DCP04_OFF
SELECT 'DCP04_OFF' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

-- CASE DCP04_ON
SELECT 'DCP04_ON' AS case_id;
SELECT d.id, HEX(d.tag) AS tag_hex,
       CHAR_LENGTH(d.tag) AS char_len, OCTET_LENGTH(d.tag) AS byte_len
FROM (
  SELECT DISTINCT id, CONCAT(s, _utf8mb4'O''Reilly') AS tag
  FROM wf_4d2_text
) AS d
WHERE d.tag = _utf8mb4'aO''Reilly' COLLATE utf8mb4_bin
ORDER BY d.id;

-- Cleanup and session restoration after all data results.
DROP TABLE wf_4d2_text;
SET SESSION optimizer_switch = @wf_4d2_optimizer;
SET SESSION character_set_client = @wf_4d2_client;
SET SESSION character_set_results = @wf_4d2_results;
SET SESSION collation_connection = @wf_4d2_collation;
````

### 独立保存的预期结果与 oracle

原件：[derived_condition_charset_4d2da251cb53.json](../prompt_pipeline_20261104/generation/expected/derived_condition_charset_4d2da251cb53.json)

````json
{
  "target": "derived_condition_charset_4d2da251cb53",
  "row_order": "significant; each data SELECT orders by stable keys",
  "result_protocol": "A one-row case_id result identifies the next data result set. Environment metadata is not a test result. Case labels must be present in the specified order; omitted/error results cannot pass.",
  "null_encoding": "JSON null means SQL NULL, never zero or an empty string",
  "cases": [
    {
      "case_id": "DCP01_OFF",
      "family": "implicit_utf8mb4",
      "pushdown": "off",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61C3A9",
          2,
          3
        ],
        [
          4,
          "61C3A9",
          2,
          3
        ]
      ]
    },
    {
      "case_id": "DCP01_ON",
      "family": "implicit_utf8mb4",
      "pushdown": "on",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61C3A9",
          2,
          3
        ],
        [
          4,
          "61C3A9",
          2,
          3
        ]
      ]
    },
    {
      "case_id": "DCP02_OFF",
      "family": "explicit_utf8mb4",
      "pushdown": "off",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61C3A9",
          2,
          3
        ],
        [
          4,
          "61C3A9",
          2,
          3
        ]
      ]
    },
    {
      "case_id": "DCP02_ON",
      "family": "explicit_utf8mb4",
      "pushdown": "on",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61C3A9",
          2,
          3
        ],
        [
          4,
          "61C3A9",
          2,
          3
        ]
      ]
    },
    {
      "case_id": "DCP03_OFF",
      "family": "explicit_multibyte",
      "pushdown": "off",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61E4B8AD",
          2,
          4
        ],
        [
          4,
          "61E4B8AD",
          2,
          4
        ]
      ]
    },
    {
      "case_id": "DCP03_ON",
      "family": "explicit_multibyte",
      "pushdown": "on",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "61E4B8AD",
          2,
          4
        ],
        [
          4,
          "61E4B8AD",
          2,
          4
        ]
      ]
    },
    {
      "case_id": "DCP04_OFF",
      "family": "embedded_quote",
      "pushdown": "off",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "614F275265696C6C79",
          9,
          9
        ],
        [
          4,
          "614F275265696C6C79",
          9,
          9
        ]
      ]
    },
    {
      "case_id": "DCP04_ON",
      "family": "embedded_quote",
      "pushdown": "on",
      "columns": [
        "id",
        "tag_hex",
        "char_len",
        "byte_len"
      ],
      "comparison": "exact",
      "rows": [
        [
          1,
          "614F275265696C6C79",
          9,
          9
        ],
        [
          4,
          "614F275265696C6C79",
          9,
          9
        ]
      ]
    }
  ]
}
````

### 执行环境、命令与三轮结果

#### 父提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/result.json)。精确 revision：`e248166db3c95b4fc998ca14cff914f1fdafbe7b`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "derived_condition_charset_4d2da251cb53",
  "revision": "e248166db3c95b4fc998ca14cff914f1fdafbe7b",
  "role": "parent",
  "run_id": "e248166db3c9-f2c583c1",
  "started": "2026-11-04T04:02:14.036836+00:00",
  "sql_sha256": "809ffb8ff75d942b989f4d28c4a4c518de8d37735b2d5cae5ae7e6ea80307f56",
  "expected_sha256": "930f11dab8c6ad5540c1c78d9dfe741443714deec801e9e8bfce3c72a1595ce3",
  "runtime_path": "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/e248166db3c9",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-e248166db3c9-f2c583c1",
    "--label",
    "experiment=mysql-three-prompts-20261104-a",
    "--network",
    "none",
    "--cpus",
    "2",
    "--memory",
    "3g",
    "--user",
    "1006:1007",
    "-v",
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a:/work",
    "-v",
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/e248166db3c9:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "e248166db3c9-f2c583c1"
  ],
  "container_id": "97aa33cfa3c7e22db8720c823bb22b53bb45e1a92343b73cf15cf3ce8e3a5558",
  "server_metadata_tsv": "8.0.32-tr\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "b1073c74b37bdd7b0e5a53e4ad853b9de37e5b8b49ab953fff7311d0c1266c37",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 115901,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T04:02:18.611361318Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T04:02:38.229180+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T04:02:35.776725+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-e248166db3c9-f2c583c1",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/e248166db3c9-f2c583c1/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_e248166db3c9_1"
      ],
      "schema": "wf_three_e248166db3c9_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 115901,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:02:18.611361318Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:02:35.988421+00:00",
      "stdout_sha256": "9b2ba2a0fff22f14a8846a835b20d38e97e2ae7d22d8d1c3e8905db98190117f",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T04:02:36.098174+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-e248166db3c9-f2c583c1",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/e248166db3c9-f2c583c1/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_e248166db3c9_2"
      ],
      "schema": "wf_three_e248166db3c9_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 115901,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:02:18.611361318Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:02:36.303520+00:00",
      "stdout_sha256": "7586a74c8e0c92f16d040220f499a0c3c2aa5dc03bf01bedba6c72393a7202f0",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T04:02:36.412137+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-e248166db3c9-f2c583c1",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/e248166db3c9-f2c583c1/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_e248166db3c9_3"
      ],
      "schema": "wf_three_e248166db3c9_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 115901,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:02:18.611361318Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:02:36.708742+00:00",
      "stdout_sha256": "c9069880eef14335b76eb71dfef0b64b59df5f57fa5b6655caf20c43c536864d",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema | initial_optimizer_switch |
| --- | --- | --- |
| 8.0.32-tr | wf_three_e248166db3c9_1 | index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on |

结果集 2：

| case_id |
| --- |
| DCP01_OFF |

结果集 3：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 4：

| case_id |
| --- |
| DCP01_ON |

结果集 5：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 6：

| case_id |
| --- |
| DCP02_OFF |

结果集 7：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 8：

| case_id |
| --- |
| DCP02_ON |

结果集 9：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 10：

| case_id |
| --- |
| DCP03_OFF |

结果集 11：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61E4B8AD | 2 | 4 |
| 4 | 61E4B8AD | 2 | 4 |

结果集 12：

| case_id |
| --- |
| DCP03_ON |

结果集 13：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61E4B8AD | 2 | 4 |
| 4 | 61E4B8AD | 2 | 4 |

结果集 14：

| case_id |
| --- |
| DCP04_OFF |

结果集 15：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 614F275265696C6C79 | 9 | 9 |
| 4 | 614F275265696C6C79 | 9 | 9 |

结果集 16：

| case_id |
| --- |
| DCP04_ON |

结果集 17：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 614F275265696C6C79 | 9 | 9 |
| 4 | 614F275265696C6C79 | 9 | 9 |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/result.json)。精确 revision：`4d2da251cb536340d19438cc0039bb2846f9a634`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "derived_condition_charset_4d2da251cb53",
  "revision": "4d2da251cb536340d19438cc0039bb2846f9a634",
  "role": "target",
  "run_id": "4d2da251cb53-982052d8",
  "started": "2026-11-04T04:03:01.870609+00:00",
  "sql_sha256": "809ffb8ff75d942b989f4d28c4a4c518de8d37735b2d5cae5ae7e6ea80307f56",
  "expected_sha256": "930f11dab8c6ad5540c1c78d9dfe741443714deec801e9e8bfce3c72a1595ce3",
  "runtime_path": "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/4d2da251cb53",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-4d2da251cb53-982052d8",
    "--label",
    "experiment=mysql-three-prompts-20261104-a",
    "--network",
    "none",
    "--cpus",
    "2",
    "--memory",
    "3g",
    "--user",
    "1006:1007",
    "-v",
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a:/work",
    "-v",
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/4d2da251cb53:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "4d2da251cb53-982052d8"
  ],
  "container_id": "1b4a1455ff7a177d7a2fe54e7b8eb886d206a892302005366d7c09466e819009",
  "server_metadata_tsv": "8.0.32-tr\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "f413d2572575abf87da8f22fe8e5a1770cfcbe0367d0b7bbd11f641f413764b8",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 133822,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T04:03:04.090093853Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T04:03:21.304425+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T04:03:16.557507+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-4d2da251cb53-982052d8",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/4d2da251cb53-982052d8/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_4d2da251cb53_1"
      ],
      "schema": "wf_three_4d2da251cb53_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 133822,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:03:04.090093853Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:03:16.782448+00:00",
      "stdout_sha256": "25fd2d2b5b2eb9e4190e5420ee188559084c491694ca7ad0a659ae4477359e91",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T04:03:16.889029+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-4d2da251cb53-982052d8",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/4d2da251cb53-982052d8/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_4d2da251cb53_2"
      ],
      "schema": "wf_three_4d2da251cb53_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 133822,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:03:04.090093853Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:03:17.096523+00:00",
      "stdout_sha256": "accb42eabc485b8ac4a034edc52fb1944f28abe9791be1ecf79aa2c9e4d88b0f",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T04:03:17.198009+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-4d2da251cb53-982052d8",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/4d2da251cb53-982052d8/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_4d2da251cb53_3"
      ],
      "schema": "wf_three_4d2da251cb53_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 133822,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:03:04.090093853Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:03:17.400653+00:00",
      "stdout_sha256": "6cadaba03236f13d910e09034f220d1ebe75d76d4ae9c69a85de0c04c15b25af",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/derived_condition_charset_4d2da251cb53/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema | initial_optimizer_switch |
| --- | --- | --- |
| 8.0.32-tr | wf_three_4d2da251cb53_1 | index_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on |

结果集 2：

| case_id |
| --- |
| DCP01_OFF |

结果集 3：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 4：

| case_id |
| --- |
| DCP01_ON |

结果集 5：空集。

结果集 6：

| case_id |
| --- |
| DCP02_OFF |

结果集 7：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 8：

| case_id |
| --- |
| DCP02_ON |

结果集 9：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61C3A9 | 2 | 3 |
| 4 | 61C3A9 | 2 | 3 |

结果集 10：

| case_id |
| --- |
| DCP03_OFF |

结果集 11：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61E4B8AD | 2 | 4 |
| 4 | 61E4B8AD | 2 | 4 |

结果集 12：

| case_id |
| --- |
| DCP03_ON |

结果集 13：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 61E4B8AD | 2 | 4 |
| 4 | 61E4B8AD | 2 | 4 |

结果集 14：

| case_id |
| --- |
| DCP04_OFF |

结果集 15：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 614F275265696C6C79 | 9 | 9 |
| 4 | 614F275265696C6C79 | 9 | 9 |

结果集 16：

| case_id |
| --- |
| DCP04_ON |

结果集 17：

| id | tag_hex | char_len | byte_len |
| --- | --- | --- | --- |
| 1 | 614F275265696C6C79 | 9 | 9 |
| 4 | 614F275265696C6C79 | 9 | 9 |

判定与环境补充：[逐检查点比较](../prompt_pipeline_20261104/runtime/comparison.json)、[完整执行报告](../prompt_pipeline_20261104/runtime/final_report.txt)、[输入构建执行关联](../prompt_pipeline_20261104/lineage.json)。

## 2. DeepSeek 重跑

Stage 1 实际请求 [stage1_request.json](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage1_request.json)；原始响应 [stage1_response_raw.json](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage1_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

```json
{
  "model": "deepseek-v4-pro",
  "temperature": 0.7,
  "max_tokens": 16384,
  "thinking": {
    "type": "disabled"
  },
  "messages_summary": [
    {
      "role": "user",
      "content_characters": 12830
    }
  ]
}
```

Stage 2 实际请求 [stage2_request.json](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage2_request.json)；原始响应 [stage2_response_raw.json](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage2_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

```json
{
  "model": "deepseek-v4-flash",
  "temperature": 0.7,
  "max_tokens": 16384,
  "thinking": {
    "type": "disabled"
  },
  "messages_summary": [
    {
      "role": "user",
      "content_characters": 10161
    }
  ]
}
```

### Stage 1 输出：测试偏好与需求原文

原件：[stage1_output.txt](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage1_output.txt)

````text
Target: derived_condition_charset_4d2da251cb53

Target observation: Expression serialization and reparsing while cloning a derived-table expression during condition pushdown

Revision: 4d2da251cb536340d19438cc0039bb2846f9a634
Parent revision: e248166db3c95b4fc998ca14cff914f1fdafbe7b
Source repository: https://github.com/mysql/mysql-server

Source-required conditions

The target branch is in `parse_expression()` at sql/sql_derived.cc:571-572, where `item->print()` is called with `QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET`. The printed expression is then reparsed at line 618 via `parse_sql()`, and the resulting `Item` is returned through `clone_expression()` at sql/sql_derived.cc:734-744.

For the charset-specific behavior to be exercised, the expression being cloned must contain at least one `Item_string` whose character set is not the same as the `StringBuffer`'s charset. At sql/sql_derived.cc:564 the `StringBuffer` is constructed with the default constructor, which uses `&my_charset_bin` (include/sql_string.h:633). Therefore, when `Item_string::print()` reaches the `QT_TO_ARGUMENT_CHARSET` branch at sql/item.cc:3464-3472, the `print_introducer` decision at lines 3433-3435 depends on whether the string's collation has `is_cs_specified()` true.

The pushdown path itself requires `TABLE_LIST::can_push_condition_to_derived()` to return true (sql/sql_derived.cc:976-985): the derived table must not have a LIMIT, must not be an inner table of an outer join, must not be a multi-reference or recursive CTE, must have no `SET` variables in the statement, and must be enabled by both the optimizer switch `derived_condition_pushdown` and any applicable hint.

Candidate construction

Create a derived table whose SELECT list contains a string literal with an explicitly specified character set introducer, such as `_utf8mb4'some text'` or `_latin1'value'`, and whose query has no LIMIT. Join this derived table to an outer table, and place a WHERE condition on the outer query that references the derived table's string column in a way that the optimizer can push down into the derived table. A simple equality comparison between the derived string column and a constant, or between the derived string column and an outer table column, is a candidate for pushdown. The derived table must be materialized or merged in a manner that allows condition pushdown to invoke `replace_with_derived_expr()` (sql/item.cc:1042-1055), which calls `clone_expression()` on the derived expression.

To specifically exercise the `QT_TO_ARGUMENT_CHARSET` path, the string literal's introducer charset must differ from `my_charset_bin`; this is the case for any normal character set introducer. The `StringBuffer` at sql/sql_derived.cc:564 uses the default constructor, so its charset is `my_charset_bin`. With `QT_TO_ARGUMENT_CHARSET` set, `Item_string::print()` will take the branch at sql/item.cc:3464-3472. If the string has an introducer (`is_cs_specified()` true), it will print the introducer and convert the value to the string's own collation (line 3465-3466); otherwise it will convert to the `StringBuffer`'s charset, which is binary.

Correctness oracle

After condition pushdown, the result of the query must be identical to the result of the same query with condition pushdown disabled. The pushed-down condition must compare equal strings correctly according to the original comparison semantics, including any character set conversion or collation rules implied by the introducer. For a concrete test, insert data into the outer table and ensure that rows are filtered exactly as they would be if the condition were evaluated in the outer query block. The string literal's character set introducer must survive the print-parse round trip; if it is lost or altered, the comparison may fail or return incorrect rows. The oracle must be derived from the inserted data and the original SQL semantics, not from the output of another server version.

Coverage observation

On the specified revision, set a breakpoint or add instrumentation at sql/sql_derived.cc:571-572 to observe the call to `item->print()` with `QT_TO_ARGUMENT_CHARSET`. Confirm that the item being printed is an `Item_string` with a non-binary character set introducer, and inspect the generated string in `str` before it is reparsed. Then observe the reparsed item at sql/sql_derived.cc:635 and verify that its character set and collation match the original item. The target line is reached only if condition pushdown is actually attempted; if the breakpoint is not hit, EXPLAIN may show whether the condition was pushed down, but it does not directly confirm execution of `clone_expression()`.

Uncertainty

The local excerpt does not establish the full SQL-to-`clone_expression()` mapping. The call chain from a user query to `replace_with_derived_expr()` and then to `clone_expression()` involves condition pushdown logic whose entry points and eligibility checks are not included in the supplied code. The candidate query may not reach the target if the optimizer chooses not to push the condition, or if the derived table is merged rather than materialized. The specific `enum_query_type` flags used in `parse_expression()` are fixed in the source, but whether the printed string actually differs from the original depends on the `Item_string`'s internal state, which is not fully visible from the excerpt. If the target is not reached, inspect the condition pushdown decision path and the derived table materialization plan before revising the candidate.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[stage2_prompt.txt](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage2_prompt.txt)

````text
### Example task
Generate a self-contained MySQL SQL test and its inputs from the requirements below. Include setup, deterministic queries, independently derived expected results, and cleanup. Explain how to observe the source target separately from checking SQL results.

# Description of requirements
Target
MySQL revision fac72fe1704c542ba476ef065dee03d2c1da83ae, sql/sql_optimizer.cc:3198-3199: the INTERSECT/EXCEPT materialized-table branch that selects JT_ALL. This is a source-derived candidate, not an executed reproduction.

Source-required conditions
The current JOIN_TAB is neither JT_CONST nor JT_SYSTEM (line 3188). Its TABLE reports is_intersect() or is_except() (line 3198). The branch assigns JT_ALL (line 3199).

Candidate construction
Join a derived table containing INTERSECT ALL with a small outer table on an integer key. Give the left input three copies of 1 and one copy of 2, the right input two copies of 1 and one copy of 3, and the outer table two copies of 1 and one copy of 2. This exposes duplicate multiplicities. The equality join is a candidate for presenting the materialized table as a join input; it does not guarantee a particular optimizer plan. INTERSECT ALL is the concrete demonstration; EXCEPT and DISTINCT are optional separate variants.

Correctness oracle
For each key k, INTERSECT ALL has min(left_count(k), right_count(k)) rows. An equality join multiplies that by outer_count(k). The stated data therefore produces exactly four rows containing 1. Derive this from the inserted data, not from the other server version's output.

Coverage observation
On the specified revision, use a breakpoint or instrumentation at sql/sql_optimizer.cc:3198-3199 and identify the derived TABLE for this query. Record its set-operation flags, incoming JOIN_TAB type, and the JT_ALL assignment. EXPLAIN alone is only a plan clue.

Uncertainty
The local excerpt does not establish the full SQL-to-TABLE construction path. If the query does not reach the target, inspect materialization and join-planning callers before revising the candidate. Coverage and correct output are separate observations.

# Test
Prerequisites
Use a disposable, already selected schema on a MySQL build supporting INTERSECT ALL. The source coverage target is revision fac72fe1704c542ba476ef065dee03d2c1da83ae; do not infer that every release has identical source locations. Use a fresh session with no existing objects named wf_demo_a, wf_demo_b, or wf_demo_c.

SQL
```sql
CREATE TEMPORARY TABLE wf_demo_a (k INT NOT NULL);
CREATE TEMPORARY TABLE wf_demo_b (k INT NOT NULL);
CREATE TEMPORARY TABLE wf_demo_c (k INT NOT NULL);
INSERT INTO wf_demo_a VALUES (1), (1), (1), (2);
INSERT INTO wf_demo_b VALUES (1), (1), (3);
INSERT INTO wf_demo_c VALUES (1), (1), (2);

SELECT d.k
FROM (
  SELECT k FROM wf_demo_a
  INTERSECT ALL
  SELECT k FROM wf_demo_b
) AS d
JOIN wf_demo_c AS c ON d.k = c.k
ORDER BY d.k;

DROP TEMPORARY TABLE wf_demo_c;
DROP TEMPORARY TABLE wf_demo_b;
DROP TEMPORARY TABLE wf_demo_a;
```

Expected results and oracle
The SELECT returns four rows, each with k=1. The intersection contains min(3,2)=2 copies of 1 and no other keys; joining the two outer copies produces 2*2=4 rows. Compare row multiplicities, not just distinct values. If setup or the SELECT fails, retain that failure separately; close the session to release remaining temporary tables.

Coverage observation
Observe sql/sql_optimizer.cc:3198-3199 at the specified revision. Identify d's materialized TABLE, verify its is_intersect() flag and nonconstant JOIN_TAB, and record the JT_ALL assignment. The expected result does not itself prove this branch was reached.

Execution status
Authored one-shot demonstration; SQL and branch coverage have not been executed or measured.

### Current task
Generate a new MySQL test that satisfies the following requirements. Follow the example's format, but use the current target's operations and data. Supply complete SQL without placeholders, expected rows with a derivation, cleanup, and a separate coverage observation plan. Use an already selected disposable test schema; use temporary tables when compatible with the target, otherwise use uniquely named ordinary tables and clean up only objects created by the test. Specify session ordering if multiple connections are required. If an essential precondition is unresolved, state it instead of claiming guaranteed coverage. Do not execute the test or describe generated SQL as a reproduced bug. Output only: Prerequisites; SQL; Expected results and oracle; Coverage observation; Execution status.

# Description of requirements
Target: derived_condition_charset_4d2da251cb53

Target observation: Expression serialization and reparsing while cloning a derived-table expression during condition pushdown

Revision: 4d2da251cb536340d19438cc0039bb2846f9a634
Parent revision: e248166db3c95b4fc998ca14cff914f1fdafbe7b
Source repository: https://github.com/mysql/mysql-server

Source-required conditions

The target branch is in `parse_expression()` at sql/sql_derived.cc:571-572, where `item->print()` is called with `QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET`. The printed expression is then reparsed at line 618 via `parse_sql()`, and the resulting `Item` is returned through `clone_expression()` at sql/sql_derived.cc:734-744.

For the charset-specific behavior to be exercised, the expression being cloned must contain at least one `Item_string` whose character set is not the same as the `StringBuffer`'s charset. At sql/sql_derived.cc:564 the `StringBuffer` is constructed with the default constructor, which uses `&my_charset_bin` (include/sql_string.h:633). Therefore, when `Item_string::print()` reaches the `QT_TO_ARGUMENT_CHARSET` branch at sql/item.cc:3464-3472, the `print_introducer` decision at lines 3433-3435 depends on whether the string's collation has `is_cs_specified()` true.

The pushdown path itself requires `TABLE_LIST::can_push_condition_to_derived()` to return true (sql/sql_derived.cc:976-985): the derived table must not have a LIMIT, must not be an inner table of an outer join, must not be a multi-reference or recursive CTE, must have no `SET` variables in the statement, and must be enabled by both the optimizer switch `derived_condition_pushdown` and any applicable hint.

Candidate construction

Create a derived table whose SELECT list contains a string literal with an explicitly specified character set introducer, such as `_utf8mb4'some text'` or `_latin1'value'`, and whose query has no LIMIT. Join this derived table to an outer table, and place a WHERE condition on the outer query that references the derived table's string column in a way that the optimizer can push down into the derived table. A simple equality comparison between the derived string column and a constant, or between the derived string column and an outer table column, is a candidate for pushdown. The derived table must be materialized or merged in a manner that allows condition pushdown to invoke `replace_with_derived_expr()` (sql/item.cc:1042-1055), which calls `clone_expression()` on the derived expression.

To specifically exercise the `QT_TO_ARGUMENT_CHARSET` path, the string literal's introducer charset must differ from `my_charset_bin`; this is the case for any normal character set introducer. The `StringBuffer` at sql/sql_derived.cc:564 uses the default constructor, so its charset is `my_charset_bin`. With `QT_TO_ARGUMENT_CHARSET` set, `Item_string::print()` will take the branch at sql/item.cc:3464-3472. If the string has an introducer (`is_cs_specified()` true), it will print the introducer and convert the value to the string's own collation (line 3465-3466); otherwise it will convert to the `StringBuffer`'s charset, which is binary.

Correctness oracle

After condition pushdown, the result of the query must be identical to the result of the same query with condition pushdown disabled. The pushed-down condition must compare equal strings correctly according to the original comparison semantics, including any character set conversion or collation rules implied by the introducer. For a concrete test, insert data into the outer table and ensure that rows are filtered exactly as they would be if the condition were evaluated in the outer query block. The string literal's character set introducer must survive the print-parse round trip; if it is lost or altered, the comparison may fail or return incorrect rows. The oracle must be derived from the inserted data and the original SQL semantics, not from the output of another server version.

Coverage observation

On the specified revision, set a breakpoint or add instrumentation at sql/sql_derived.cc:571-572 to observe the call to `item->print()` with `QT_TO_ARGUMENT_CHARSET`. Confirm that the item being printed is an `Item_string` with a non-binary character set introducer, and inspect the generated string in `str` before it is reparsed. Then observe the reparsed item at sql/sql_derived.cc:635 and verify that its character set and collation match the original item. The target line is reached only if condition pushdown is actually attempted; if the breakpoint is not hit, EXPLAIN may show whether the condition was pushed down, but it does not directly confirm execution of `clone_expression()`.

Uncertainty

The local excerpt does not establish the full SQL-to-`clone_expression()` mapping. The call chain from a user query to `replace_with_derived_expr()` and then to `clone_expression()` involves condition pushdown logic whose entry points and eligibility checks are not included in the supplied code. The candidate query may not reach the target if the optimizer chooses not to push the condition, or if the derived table is merged rather than materialized. The specific `enum_query_type` flags used in `parse_expression()` are fixed in the source, but whether the printed string actually differs from the original depends on the `Item_string`'s internal state, which is not fully visible from the excerpt. If the target is not reached, inspect the condition pushdown decision path and the derived table materialization plan before revising the candidate.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[stage2_output.txt](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/stage2_output.txt)

````text
Prerequisites

Use a disposable, already selected schema on a MySQL build at or near revision 4d2da251cb536340d19438cc0039bb2846f9a634 that supports derived condition pushdown (`derived_condition_pushdown` optimizer switch) and INTERSECT/EXCEPT-independent derived tables. Use a fresh session with no existing objects named `wf_dcp_outer`, `wf_dcp_inner`. Temporary tables are compatible with the target (derived condition pushdown operates on derived tables over any base tables), so use `CREATE TEMPORARY TABLE`. The session must have `optimizer_switch` with `derived_condition_pushdown=on` (default in this revision) and no `SET`-variable references inside the derived subquery (required for `can_push_condition_to_derived()`). Do not execute; coverage is not guaranteed because the optimizer may merge the derived table or decline pushdown.

SQL

```sql
-- Session setup
SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

CREATE TEMPORARY TABLE wf_dcp_inner (
  id INT NOT NULL PRIMARY KEY,
  tag VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

CREATE TEMPORARY TABLE wf_dcp_outer (
  id INT NOT NULL PRIMARY KEY,
  want VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

INSERT INTO wf_dcp_inner VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'gamma'),
  (4, 'delta');

INSERT INTO wf_dcp_outer VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'omega'),
  (4, 'delta');

-- Query under test: derived table has an explicit utf8mb4 introducer on a
-- string literal in its SELECT list; the outer WHERE references the derived
-- column. Pushdown of "d.tag = 'alpha'" into the derived table triggers
-- clone_expression() on the derived expression containing the Item_string.
SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

-- Reference query: same semantics with pushdown disabled.
SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

DROP TEMPORARY TABLE wf_dcp_outer;
DROP TEMPORARY TABLE wf_dcp_inner;
```

Expected results and oracle

Both SELECTs must return exactly the same rows, derived from the inserted data and SQL semantics (not from any server output):

- The derived table projects `id` from `wf_dcp_inner` (ids 1,2,3,4) and the constant `_utf8mb4'alpha'` for every row.
- The outer JOIN on `o.id = d.id` keeps ids 1,2,3,4 (all present in `wf_dcp_outer`).
- The WHERE `d.tag = _utf8mb4'alpha'` compares the constant `'alpha'` (utf8mb4) to `'alpha'` (utf8mb4). utf8mb4_0900_ai_ci is accent- and case-insensitive but `'alpha'` equals `'alpha'` exactly, so all four rows satisfy the predicate.
- Result: four rows, `(1,'alpha'), (2,'alpha'), (3,'alpha'), (4,'alpha')`, in ascending `id` order.

The oracle is the row set above; it must be identical for the pushdown-on and pushdown-off runs. Because the derived column is a constant literal, pushdown of `d.tag = 'alpha'` into the derived table reduces it to `_utf8mb4'alpha' = _utf8mb4'alpha'`, which is TRUE for every derived row; the outer join then filters by `o.id = d.id` as usual. Any deviation (missing rows, wrong tag value, error during print/reparse, or a charset conversion error such as "Cannot convert string") indicates the `QT_TO_ARGUMENT_CHARSET` round trip altered or lost the introducer.

Coverage observation

On the specified revision, set a breakpoint or add instrumentation at `sql/sql_derived.cc:571-572` and run the pushdown-on SELECT. Confirm:

1. The call to `item->print()` is made with `QT_NO_DATA_EXPANSION | QT_TO_ARGUMENT_CHARSET`.
2. The item being printed is an `Item_string` whose collation has `is_cs_specified()` true (utf8mb4 introducer, not `my_charset_bin`), so the `print_introducer` branch at `sql/item.cc:3433-3435` is taken and the `QT_TO_ARGUMENT_CHARSET` branch at `sql/item.cc:3464-3472` executes.
3. Inspect the `StringBuffer` contents (charset `my_charset_bin`) just before `parse_sql()` at line 618: the printed text must include the `_utf8mb4` introducer and the literal value.
4. At `sql/sql_derived.cc:635`, inspect the reparsed `Item` returned through `clone_expression()` (lines 734-744): its charset/collation must match the original `Item_string`'s utf8mb4 collation.

`EXPLAIN` may show whether the condition was pushed into the derived table (look for the pushed predicate in the derived table's `Extra`/`filtered`), but it does not prove the target lines executed. If the breakpoint at 571-572 is not hit, the derived table was likely merged (no materialization) or pushdown was declined; in that case adjust the query (e.g., add an aggregate or `DISTINCT` in the derived table to force materialization, or reference the derived column in a way that prevents merge) and re-run the coverage observation. Coverage and the correctness oracle are independent observations: matching result rows do not by themselves prove the target branch was reached.

Execution status

Authored one-shot demonstration; SQL and branch coverage have not been executed or measured. The candidate may not reach `parse_expression()` if the optimizer merges the derived table or declines condition pushdown; that is an unresolved precondition to be verified during coverage observation, not a claim of guaranteed coverage.
````

### 提取后实际执行的完整 SQL

原件：[generated.sql](../prompt_pipeline_deepseek_20261105/derived_condition_charset_4d2da251cb53/generated.sql)

````sql
-- Session setup
SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

CREATE TEMPORARY TABLE wf_dcp_inner (
  id INT NOT NULL PRIMARY KEY,
  tag VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

CREATE TEMPORARY TABLE wf_dcp_outer (
  id INT NOT NULL PRIMARY KEY,
  want VARCHAR(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
);

INSERT INTO wf_dcp_inner VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'gamma'),
  (4, 'delta');

INSERT INTO wf_dcp_outer VALUES
  (1, 'alpha'),
  (2, 'beta'),
  (3, 'omega'),
  (4, 'delta');

-- Query under test: derived table has an explicit utf8mb4 introducer on a
-- string literal in its SELECT list; the outer WHERE references the derived
-- column. Pushdown of "d.tag = 'alpha'" into the derived table triggers
-- clone_expression() on the derived expression containing the Item_string.
SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

-- Reference query: same semantics with pushdown disabled.
SET SESSION optimizer_switch = 'derived_condition_pushdown=off';

SELECT d.id, d.tag
FROM (
  SELECT id, _utf8mb4'alpha' AS tag
  FROM wf_dcp_inner
) AS d
JOIN wf_dcp_outer AS o ON o.id = d.id
WHERE d.tag = _utf8mb4'alpha'
ORDER BY d.id;

SET SESSION optimizer_switch = 'derived_condition_pushdown=on';

DROP TEMPORARY TABLE wf_dcp_outer;
DROP TEMPORARY TABLE wf_dcp_inner;
````

本批没有独立 expected JSON；预期行在上方 Stage 2 响应。自动汇总主要判断父/目标结果、错误与退出码是否相同，不能等同于首次逐检查点 oracle 审计。

### 执行环境、命令与三轮结果

#### 父提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/result.json)。精确 revision：`e248166db3c95b4fc998ca14cff914f1fdafbe7b`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "e248166db3c95b4fc998ca14cff914f1fdafbe7b",
  "runtime": "[redacted]",
  "mysqld_sha256": "b1073c74b37bdd7b0e5a53e4ad853b9de37e5b8b49ab953fff7311d0c1266c37",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_derived__p_1",
      "started_at_epoch": 1793890825.7962096,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890825.9250102
    },
    {
      "repeat": 2,
      "schema": "ds_derived__p_2",
      "started_at_epoch": 1793890826.0237527,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890826.1569586
    },
    {
      "repeat": 3,
      "schema": "ds_derived__p_3",
      "started_at_epoch": 1793890826.2616603,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890826.3906338
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| id | tag |
| --- | --- |
| 1 | alpha |
| 2 | alpha |
| 3 | alpha |
| 4 | alpha |

结果集 2：

| id | tag |
| --- | --- |
| 1 | alpha |
| 2 | alpha |
| 3 | alpha |
| 4 | alpha |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/result.json)。精确 revision：`4d2da251cb536340d19438cc0039bb2846f9a634`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "4d2da251cb536340d19438cc0039bb2846f9a634",
  "runtime": "[redacted]",
  "mysqld_sha256": "f413d2572575abf87da8f22fe8e5a1770cfcbe0367d0b7bbd11f641f413764b8",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_derived__t_1",
      "started_at_epoch": 1793890847.8961506,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890848.03224
    },
    {
      "repeat": 2,
      "schema": "ds_derived__t_2",
      "started_at_epoch": 1793890848.1363804,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890848.274345
    },
    {
      "repeat": 3,
      "schema": "ds_derived__t_3",
      "started_at_epoch": 1793890848.370296,
      "returncode": 0,
      "stdout_sha256": "7610f66558e8169ec83210a19942ecf9ad4e7ea3d6df96e94af8536c09069621",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1535,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890848.491813
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/derived_condition_charset_4d2da251cb53/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| id | tag |
| --- | --- |
| 1 | alpha |
| 2 | alpha |
| 3 | alpha |
| 4 | alpha |

结果集 2：

| id | tag |
| --- | --- |
| 1 | alpha |
| 2 | alpha |
| 3 | alpha |
| 4 | alpha |

判定与环境补充：[逐轮配对与二进制身份](../prompt_pipeline_deepseek_20261105/server_evidence/summary.json)、[参数及 run_id](../prompt_pipeline_deepseek_20261105/run_manifest.json)、[执行报告](../prompt_pipeline_deepseek_20261105/verification_report.md)。原始远端 runner 未公开，公开包不能还原其完整启动命令；其 SHA256 见导出清单。

