# Item 属性重算：两批实验完整读本

[返回总览](README.md)

首次要求把窗口表达式放在 IN 左侧，并在同一个 PREPARE 上重复 EXECUTE，另有直接查询对照；DeepSeek Stage 1 和 Stage 2 转为窗口 SUM 的参数内部包含 IN 子查询，以及存储函数参数。表达式树方向与生命周期压力都改变了。

首次：父提交每轮 8/8、目标 6/8；两个检查点错误，详见下方结果表。DeepSeek：两侧每轮均为两组相同的 5 行结果。

## 0. 共同源码与 Stage 1 正式输入

两批以下文件逐字节一致。源码节选已含精确提交、父提交、源文件、行号、blob、Target observation 与局部范围说明。

DeepSeek 对应副本：[源码](../prompt_pipeline_deepseek_20261105/input_bundle/source-code-data/mysql/item_property_recalculation_248c7f7c227e.txt)、[Stage 1 提示词](../prompt_pipeline_deepseek_20261105/input_bundle/Prompts/mysql/src2req/item_property_recalculation_248c7f7c227e.txt)。

### 目标源码片段与上下文

原件：[item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/input_bundle/source-code-data/mysql/item_property_recalculation_248c7f7c227e.txt)

````text
Target: item_property_recalculation_248c7f7c227e
Target observation: Accumulated Item property recalculation across ordinary arguments, references and IN-subquery wrappers, and its use by window materialization
Revision: 248c7f7c227e76f3422378ca3b9e10d141dcfc86
Parent revision: 15980860ac2639f41dfbda2f7fffb7aeeab32921
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/item_func.cc
Blob: 31b9dfba5f1fc85c2383f49175759daad498d990
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_func.cc
```cpp
708: void Item_func::update_used_tables() {
709:   used_tables_cache = get_initial_pseudo_tables();
710:   not_null_tables_cache = 0;
711:   m_accum_properties = 0;
712: 
713:   for (uint i = 0; i < arg_count; i++) {
714:     args[i]->update_used_tables();
715:     used_tables_cache |= args[i]->used_tables();
716:     if (null_on_null) not_null_tables_cache |= args[i]->not_null_tables();
717:     add_accum_properties(args[i]);
718:   }
719: }
```
```cpp
8410: void Item_func_sp::update_used_tables() {
8411:   Item_func::update_used_tables();
8412: 
8413:   /* This is reset by Item_func::update_used_tables(). */
8414:   set_stored_program();
8415: }
```

# Code: sql/item.h
Blob: 314cef5c0d21116ee66b303ed55fb3eb6ef115b2
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item.h
```cpp
3179:  protected:
3180:   /// Set accumulated properties for an Item
3181:   void set_accum_properties(const Item *item) {
3182:     m_accum_properties = item->m_accum_properties;
3183:   }
3184: 
3185:   /// Add more accumulated properties to an Item
3186:   void add_accum_properties(const Item *item) {
3187:     m_accum_properties |= item->m_accum_properties;
3188:   }
3189: 
3190:   /// Set the "has subquery" property
3191:   void set_subquery() { m_accum_properties |= PROP_SUBQUERY; }
3192: 
3193:   /// Set the "has stored program" property
3194:   void set_stored_program() { m_accum_properties |= PROP_STORED_PROGRAM; }
3195: 
3196:  public:
3197:   /// @return true if this item or any of its descendants contains a subquery.
3198:   bool has_subquery() const { return m_accum_properties & PROP_SUBQUERY; }
3199: 
3200:   /// @return true if this item or any of its descendants refers a stored func.
3201:   bool has_stored_program() const {
3202:     return m_accum_properties & PROP_STORED_PROGRAM;
3203:   }
3204: 
3205:   /// @return true if this item or any of its descendants is an aggregated func.
3206:   bool has_aggregation() const { return m_accum_properties & PROP_AGGREGATION; }
3207: 
3208:   /// Set the "has aggregation" property
3209:   void set_aggregation() { m_accum_properties |= PROP_AGGREGATION; }
3210: 
3211:   /// Reset the "has aggregation" property
3212:   void reset_aggregation() { m_accum_properties &= ~PROP_AGGREGATION; }
3213: 
3214:   /// @return true if this item or any of its descendants is a window func.
3215:   bool has_wf() const { return m_accum_properties & PROP_WINDOW_FUNCTION; }
3216: 
3217:   /// Set the "has window function" property
3218:   void set_wf() { m_accum_properties |= PROP_WINDOW_FUNCTION; }
```
```cpp
3443:  protected:
3444:   /**
3445:     Set of properties that are calculated by accumulation from underlying items.
3446:     Computed by constructors and fix_fields() and updated by
3447:     update_used_tables(). The properties are accumulated up to the root of the
3448:     current item tree, except they are not accumulated across subqueries and
3449:     functions.
3450:   */
3451:   static constexpr uint8 PROP_SUBQUERY = 0x01;
3452:   static constexpr uint8 PROP_STORED_PROGRAM = 0x02;
3453:   static constexpr uint8 PROP_AGGREGATION = 0x04;
3454:   static constexpr uint8 PROP_WINDOW_FUNCTION = 0x08;
3455:   /**
3456:     Set if the item or one or more of the underlying items contains a
3457:     ROLLUP expression. The rolled up expression itself is not so marked.
3458:   */
3459:   static constexpr uint8 PROP_ROLLUP_EXPR = 0x10;
3460:   /**
3461:     Set if the item or one or more of the underlying items is a GROUPING
3462:     function.
3463:   */
3464:   static constexpr uint8 PROP_GROUPING_FUNC = 0x20;
3465:   uint8 m_accum_properties;
```
```cpp
5738:   Item *get_tmp_table_item(THD *thd) override;
5739:   table_map used_tables() const override {
5740:     if (depended_from != nullptr) return OUTER_REF_TABLE_BIT;
5741:     const table_map map = ref_item()->used_tables();
5742:     if (map != 0) return map;
5743:     // rollup constant: ensure it is non-constant by returning RAND_TABLE_BIT
5744:     if (has_rollup_expr()) return RAND_TABLE_BIT;
5745:     return 0;
5746:   }
5747:   void update_used_tables() override {
5748:     if (depended_from == nullptr) ref_item()->update_used_tables();
5749:     /*
5750:       Reset all flags except rollup, since we do not mark the rollup expression
5751:       itself.
5752:     */
5753:     m_accum_properties &= PROP_ROLLUP_EXPR;
5754:     add_accum_properties(ref_item());
5755:   }
```

# Code: sql/item_cmpfunc.h
Blob: 2630dac95545351e0a578c4ee70f728e7604a1bd
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.h
```cpp
472: /*
473:   Item_in_optimizer(Item_in_subselect(...))
474: 
475:   Item_in_optimizer is used to wrap an instance of Item_in_subselect. This
476:   class does the following:
477:    - Evaluate the left expression and store it in Item_cache_* object (to
478:      avoid re-evaluating it many times during subquery execution)
479:    - Shortcut the evaluation of "NULL IN (...)" to NULL in the cases where we
480:      don't care if the result is NULL or FALSE.
481: 
482:    args[0] keeps a reference to the Item_in_subselect object.
483: 
484:   NOTE
485:     It is not quite clear why the above listed functionality should be
486:     placed into a separate class called 'Item_in_optimizer'.
487: */
488: 
489: class Item_in_optimizer final : public Item_bool_func {
490:  private:
491:   Item_cache *cache{nullptr};
492:   /**
493:     Stores the value of "NULL IN (SELECT ...)" for uncorrelated subqueries:
494:       UNKNOWN - "NULL in (SELECT ...)" has not yet been evaluated
495:       FALSE   - result is FALSE
496:       TRUE    - result is NULL
497:   */
498:   int result_for_null_param{UNKNOWN};
499: 
500:  public:
501:   Item_in_optimizer(Item_in_subselect *item)
502:       : Item_bool_func(pointer_cast<Item *>(item)) {
503:     set_subquery();
504:   }
```

# Code: sql/item_cmpfunc.cc
Blob: 57c367f4470d918ab9f3ed89899c6cb9b150a44f
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.cc
```cpp
2138: bool Item_in_optimizer::fix_left(THD *thd, Item **) {
2139:   Item *left = down_cast<Item_in_subselect *>(args[0])->left_expr;
2140:   /*
2141:     Because get_cache() depends on type of left arg, if this arg is a PS param
2142:     we must decide of its type now. We cannot wait until we know the type of
2143:     the subquery's SELECT list.
2144:     @todo: This may actually be changed later, INSPECT.
2145:   */
2146:   if (left->propagate_type(thd, MYSQL_TYPE_VARCHAR)) return true;
2147: 
2148:   assert(cache == nullptr);
2149:   cache = Item_cache::get_cache(left);
2150:   if (cache == nullptr) return true;
2151: 
2152:   cache->setup(left);
2153:   used_tables_cache = left->used_tables();
```
```cpp
2173:   not_null_tables_cache = left->not_null_tables();
2174:   add_accum_properties(left);
2175:   if (const_item()) cache->store(left);
2176: 
2177:   return false;
2178: }
2179: 
2180: bool Item_in_optimizer::fix_fields(THD *thd, Item **) {
2181:   assert(!fixed);
2182:   Item_in_subselect *subqpred = down_cast<Item_in_subselect *>(args[0]);
2183: 
2184:   if (!subqpred->fixed && subqpred->fix_fields(thd, nullptr)) return true;
2185:   if (subqpred->left_expr->cols() != subqpred->unit_cols()) {
2186:     assert(false);
2187:     my_error(ER_OPERAND_COLUMNS, MYF(0), subqpred->left_expr->cols());
2188:     return true;
2189:   }
2190:   if (subqpred->is_nullable()) set_nullable(true);
2191:   add_accum_properties(subqpred);
2192:   used_tables_cache |= subqpred->used_tables();
2193:   not_null_tables_cache |= subqpred->not_null_tables();
```
```cpp
2410: void Item_in_optimizer::update_used_tables() {
2411:   Item_func::update_used_tables();
2412: 
2413:   // See explanation for this logic in Item_in_optimizer::fix_fields
2414:   Item_in_subselect *subqpred = down_cast<Item_in_subselect *>(args[0]);
2415:   if (subqpred->abort_on_null && subqpred->value_transform == BOOL_IS_TRUE) {
2416:   } else {
2417:     not_null_tables_cache &= subqpred->left_expr->not_null_tables();
2418:   }
2419: }
```

# Code: sql/item_subselect.cc
Blob: b27476a5311102df1d1f622d6b09a465be1b6551
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_subselect.cc
```cpp
2537: void Item_in_subselect::update_used_tables() {
2538:   Item_subselect::update_used_tables();
2539:   left_expr->update_used_tables();
2540:   used_tables_cache |= left_expr->used_tables();
2541: }
```

# Code: sql/sql_select.cc
Blob: b04854d625d68959c1d0a19e09e9ccbfff692f7e
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/sql_select.cc
```cpp
4106:   // Don't include temporary fields that originally came from
4107:   // a window function (or an expression containing a window function).
4108:   // Window functions are not relevant to store in the framebuffer,
4109:   // and in fact, trying to restore them would often overwrite
4110:   // good data we shouldn't.
4111:   //
4112:   // Not that the regular filtering in create_tmp_table() cannot do this
4113:   // for us, as it only sees the Item_field, not where it came from.
4114:   mem_root_deque<Item *> fb_fields(window_output_fields);
4115:   for (size_t i = 0; i < fb_fields.size(); ++i) {
4116:     Item *orig_item = source_fields[i];
4117:     if (orig_item->has_wf()) {
4118:       fb_fields[i] = nullptr;
4119:     }
4120:   }
4121:   fb_fields.erase(std::remove(fb_fields.begin(), fb_fields.end(), nullptr),
4122:                   fb_fields.end());
4123:   count_field_types(&query_block, par, fb_fields, false, false);
4124: 
4125:   TABLE *table =
4126:       create_tmp_table(thd, par, fb_fields, nullptr, false, false,
4127:                        query_block.active_options(), HA_POS_ERROR, "");
4128:   if (table == nullptr) return true;
4129: 
4130:   window->set_frame_buffer_param(par);
4131:   window->set_frame_buffer(table);
4132: 
4133:   // For window function expressions we are to evaluate after
4134:   // framebuffering, we need to replace their arguments to point to the
4135:   // output table instead of the input table (we could probably also have
4136:   // used the framebuffer if we wanted). E.g., if our input is t1 and our
4137:   // output is <temporary>, we need to rewrite 1 + SUM(t1.x) OVER w into
4138:   // 1 + SUM(<temporary>.x) OVER w.
4139:   for (Func_ptr &ptr : *mapping_from_source_to_window_output) {
4140:     if (ptr.func()->has_wf()) {
4141:       ReplaceMaterializedItems(thd, ptr.func(),
4142:                                *mapping_from_source_to_window_output,
4143:                                /*need_exact_match=*/false);
4144:     }
4145:   }
4146:   return false;
4147: }
```
```cpp
4654:       const uint widx = REF_SLICE_WIN_1 + wno;
4655: 
4656:       QEP_TAB *tab = &qep_tab[curr_tmp_table];
4657:       mem_root_deque<Item *> *orig_fields = curr_fields;
4658:       {
4659:         Opt_trace_object trace_this_tbl(trace);
4660:         trace_this_tbl
4661:             .add("adding_tmp_table_in_plan_at_position", curr_tmp_table)
4662:             .add_alnum("cause", "output_for_window_functions")
4663:             .add("with_buffer", m_windows[wno]->needs_buffering());
4664: 
4665:         if (create_intermediate_table(tab, *curr_fields, dummy, false))
4666:           return true;
4667: 
4668:         if (alloc_ref_item_slice(thd, widx)) return true;
4669: 
4670:         if (change_to_use_tmp_fields(curr_fields, thd, ref_items[widx],
4671:                                      &tmp_fields[widx],
4672:                                      query_block->m_added_non_hidden_fields))
4673:           return true;
4674: 
4675:         curr_fields = &tmp_fields[widx];
4676:         set_ref_item_slice(widx);
4677:         tab->ref_item_slice = widx;
4678:         setup_tmptable_write_func(tab, &trace_this_tbl);
4679:       }
4680: 
4681:       if (m_windows[wno]->needs_buffering()) {
4682:         if (CreateFramebufferTable(
4683:                 thd, tmp_table_param, *query_block, *orig_fields, *curr_fields,
4684:                 tab->tmp_table_param->items_to_copy, m_windows[wno])) {
4685:           return true;
4686:         }
4687:       }
```
````

### 共同的完整 Stage 1 提示词（含示例及当前源码）

原件：[item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/src2req/item_property_recalculation_248c7f7c227e.txt)

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
Target: item_property_recalculation_248c7f7c227e
Target observation: Accumulated Item property recalculation across ordinary arguments, references and IN-subquery wrappers, and its use by window materialization
Revision: 248c7f7c227e76f3422378ca3b9e10d141dcfc86
Parent revision: 15980860ac2639f41dfbda2f7fffb7aeeab32921
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/item_func.cc
Blob: 31b9dfba5f1fc85c2383f49175759daad498d990
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_func.cc
```cpp
708: void Item_func::update_used_tables() {
709:   used_tables_cache = get_initial_pseudo_tables();
710:   not_null_tables_cache = 0;
711:   m_accum_properties = 0;
712: 
713:   for (uint i = 0; i < arg_count; i++) {
714:     args[i]->update_used_tables();
715:     used_tables_cache |= args[i]->used_tables();
716:     if (null_on_null) not_null_tables_cache |= args[i]->not_null_tables();
717:     add_accum_properties(args[i]);
718:   }
719: }
```
```cpp
8410: void Item_func_sp::update_used_tables() {
8411:   Item_func::update_used_tables();
8412: 
8413:   /* This is reset by Item_func::update_used_tables(). */
8414:   set_stored_program();
8415: }
```

# Code: sql/item.h
Blob: 314cef5c0d21116ee66b303ed55fb3eb6ef115b2
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item.h
```cpp
3179:  protected:
3180:   /// Set accumulated properties for an Item
3181:   void set_accum_properties(const Item *item) {
3182:     m_accum_properties = item->m_accum_properties;
3183:   }
3184: 
3185:   /// Add more accumulated properties to an Item
3186:   void add_accum_properties(const Item *item) {
3187:     m_accum_properties |= item->m_accum_properties;
3188:   }
3189: 
3190:   /// Set the "has subquery" property
3191:   void set_subquery() { m_accum_properties |= PROP_SUBQUERY; }
3192: 
3193:   /// Set the "has stored program" property
3194:   void set_stored_program() { m_accum_properties |= PROP_STORED_PROGRAM; }
3195: 
3196:  public:
3197:   /// @return true if this item or any of its descendants contains a subquery.
3198:   bool has_subquery() const { return m_accum_properties & PROP_SUBQUERY; }
3199: 
3200:   /// @return true if this item or any of its descendants refers a stored func.
3201:   bool has_stored_program() const {
3202:     return m_accum_properties & PROP_STORED_PROGRAM;
3203:   }
3204: 
3205:   /// @return true if this item or any of its descendants is an aggregated func.
3206:   bool has_aggregation() const { return m_accum_properties & PROP_AGGREGATION; }
3207: 
3208:   /// Set the "has aggregation" property
3209:   void set_aggregation() { m_accum_properties |= PROP_AGGREGATION; }
3210: 
3211:   /// Reset the "has aggregation" property
3212:   void reset_aggregation() { m_accum_properties &= ~PROP_AGGREGATION; }
3213: 
3214:   /// @return true if this item or any of its descendants is a window func.
3215:   bool has_wf() const { return m_accum_properties & PROP_WINDOW_FUNCTION; }
3216: 
3217:   /// Set the "has window function" property
3218:   void set_wf() { m_accum_properties |= PROP_WINDOW_FUNCTION; }
```
```cpp
3443:  protected:
3444:   /**
3445:     Set of properties that are calculated by accumulation from underlying items.
3446:     Computed by constructors and fix_fields() and updated by
3447:     update_used_tables(). The properties are accumulated up to the root of the
3448:     current item tree, except they are not accumulated across subqueries and
3449:     functions.
3450:   */
3451:   static constexpr uint8 PROP_SUBQUERY = 0x01;
3452:   static constexpr uint8 PROP_STORED_PROGRAM = 0x02;
3453:   static constexpr uint8 PROP_AGGREGATION = 0x04;
3454:   static constexpr uint8 PROP_WINDOW_FUNCTION = 0x08;
3455:   /**
3456:     Set if the item or one or more of the underlying items contains a
3457:     ROLLUP expression. The rolled up expression itself is not so marked.
3458:   */
3459:   static constexpr uint8 PROP_ROLLUP_EXPR = 0x10;
3460:   /**
3461:     Set if the item or one or more of the underlying items is a GROUPING
3462:     function.
3463:   */
3464:   static constexpr uint8 PROP_GROUPING_FUNC = 0x20;
3465:   uint8 m_accum_properties;
```
```cpp
5738:   Item *get_tmp_table_item(THD *thd) override;
5739:   table_map used_tables() const override {
5740:     if (depended_from != nullptr) return OUTER_REF_TABLE_BIT;
5741:     const table_map map = ref_item()->used_tables();
5742:     if (map != 0) return map;
5743:     // rollup constant: ensure it is non-constant by returning RAND_TABLE_BIT
5744:     if (has_rollup_expr()) return RAND_TABLE_BIT;
5745:     return 0;
5746:   }
5747:   void update_used_tables() override {
5748:     if (depended_from == nullptr) ref_item()->update_used_tables();
5749:     /*
5750:       Reset all flags except rollup, since we do not mark the rollup expression
5751:       itself.
5752:     */
5753:     m_accum_properties &= PROP_ROLLUP_EXPR;
5754:     add_accum_properties(ref_item());
5755:   }
```

# Code: sql/item_cmpfunc.h
Blob: 2630dac95545351e0a578c4ee70f728e7604a1bd
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.h
```cpp
472: /*
473:   Item_in_optimizer(Item_in_subselect(...))
474: 
475:   Item_in_optimizer is used to wrap an instance of Item_in_subselect. This
476:   class does the following:
477:    - Evaluate the left expression and store it in Item_cache_* object (to
478:      avoid re-evaluating it many times during subquery execution)
479:    - Shortcut the evaluation of "NULL IN (...)" to NULL in the cases where we
480:      don't care if the result is NULL or FALSE.
481: 
482:    args[0] keeps a reference to the Item_in_subselect object.
483: 
484:   NOTE
485:     It is not quite clear why the above listed functionality should be
486:     placed into a separate class called 'Item_in_optimizer'.
487: */
488: 
489: class Item_in_optimizer final : public Item_bool_func {
490:  private:
491:   Item_cache *cache{nullptr};
492:   /**
493:     Stores the value of "NULL IN (SELECT ...)" for uncorrelated subqueries:
494:       UNKNOWN - "NULL in (SELECT ...)" has not yet been evaluated
495:       FALSE   - result is FALSE
496:       TRUE    - result is NULL
497:   */
498:   int result_for_null_param{UNKNOWN};
499: 
500:  public:
501:   Item_in_optimizer(Item_in_subselect *item)
502:       : Item_bool_func(pointer_cast<Item *>(item)) {
503:     set_subquery();
504:   }
```

# Code: sql/item_cmpfunc.cc
Blob: 57c367f4470d918ab9f3ed89899c6cb9b150a44f
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_cmpfunc.cc
```cpp
2138: bool Item_in_optimizer::fix_left(THD *thd, Item **) {
2139:   Item *left = down_cast<Item_in_subselect *>(args[0])->left_expr;
2140:   /*
2141:     Because get_cache() depends on type of left arg, if this arg is a PS param
2142:     we must decide of its type now. We cannot wait until we know the type of
2143:     the subquery's SELECT list.
2144:     @todo: This may actually be changed later, INSPECT.
2145:   */
2146:   if (left->propagate_type(thd, MYSQL_TYPE_VARCHAR)) return true;
2147: 
2148:   assert(cache == nullptr);
2149:   cache = Item_cache::get_cache(left);
2150:   if (cache == nullptr) return true;
2151: 
2152:   cache->setup(left);
2153:   used_tables_cache = left->used_tables();
```
```cpp
2173:   not_null_tables_cache = left->not_null_tables();
2174:   add_accum_properties(left);
2175:   if (const_item()) cache->store(left);
2176: 
2177:   return false;
2178: }
2179: 
2180: bool Item_in_optimizer::fix_fields(THD *thd, Item **) {
2181:   assert(!fixed);
2182:   Item_in_subselect *subqpred = down_cast<Item_in_subselect *>(args[0]);
2183: 
2184:   if (!subqpred->fixed && subqpred->fix_fields(thd, nullptr)) return true;
2185:   if (subqpred->left_expr->cols() != subqpred->unit_cols()) {
2186:     assert(false);
2187:     my_error(ER_OPERAND_COLUMNS, MYF(0), subqpred->left_expr->cols());
2188:     return true;
2189:   }
2190:   if (subqpred->is_nullable()) set_nullable(true);
2191:   add_accum_properties(subqpred);
2192:   used_tables_cache |= subqpred->used_tables();
2193:   not_null_tables_cache |= subqpred->not_null_tables();
```
```cpp
2410: void Item_in_optimizer::update_used_tables() {
2411:   Item_func::update_used_tables();
2412: 
2413:   // See explanation for this logic in Item_in_optimizer::fix_fields
2414:   Item_in_subselect *subqpred = down_cast<Item_in_subselect *>(args[0]);
2415:   if (subqpred->abort_on_null && subqpred->value_transform == BOOL_IS_TRUE) {
2416:   } else {
2417:     not_null_tables_cache &= subqpred->left_expr->not_null_tables();
2418:   }
2419: }
```

# Code: sql/item_subselect.cc
Blob: b27476a5311102df1d1f622d6b09a465be1b6551
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/item_subselect.cc
```cpp
2537: void Item_in_subselect::update_used_tables() {
2538:   Item_subselect::update_used_tables();
2539:   left_expr->update_used_tables();
2540:   used_tables_cache |= left_expr->used_tables();
2541: }
```

# Code: sql/sql_select.cc
Blob: b04854d625d68959c1d0a19e09e9ccbfff692f7e
Source: https://github.com/mysql/mysql-server/blob/248c7f7c227e76f3422378ca3b9e10d141dcfc86/sql/sql_select.cc
```cpp
4106:   // Don't include temporary fields that originally came from
4107:   // a window function (or an expression containing a window function).
4108:   // Window functions are not relevant to store in the framebuffer,
4109:   // and in fact, trying to restore them would often overwrite
4110:   // good data we shouldn't.
4111:   //
4112:   // Not that the regular filtering in create_tmp_table() cannot do this
4113:   // for us, as it only sees the Item_field, not where it came from.
4114:   mem_root_deque<Item *> fb_fields(window_output_fields);
4115:   for (size_t i = 0; i < fb_fields.size(); ++i) {
4116:     Item *orig_item = source_fields[i];
4117:     if (orig_item->has_wf()) {
4118:       fb_fields[i] = nullptr;
4119:     }
4120:   }
4121:   fb_fields.erase(std::remove(fb_fields.begin(), fb_fields.end(), nullptr),
4122:                   fb_fields.end());
4123:   count_field_types(&query_block, par, fb_fields, false, false);
4124: 
4125:   TABLE *table =
4126:       create_tmp_table(thd, par, fb_fields, nullptr, false, false,
4127:                        query_block.active_options(), HA_POS_ERROR, "");
4128:   if (table == nullptr) return true;
4129: 
4130:   window->set_frame_buffer_param(par);
4131:   window->set_frame_buffer(table);
4132: 
4133:   // For window function expressions we are to evaluate after
4134:   // framebuffering, we need to replace their arguments to point to the
4135:   // output table instead of the input table (we could probably also have
4136:   // used the framebuffer if we wanted). E.g., if our input is t1 and our
4137:   // output is <temporary>, we need to rewrite 1 + SUM(t1.x) OVER w into
4138:   // 1 + SUM(<temporary>.x) OVER w.
4139:   for (Func_ptr &ptr : *mapping_from_source_to_window_output) {
4140:     if (ptr.func()->has_wf()) {
4141:       ReplaceMaterializedItems(thd, ptr.func(),
4142:                                *mapping_from_source_to_window_output,
4143:                                /*need_exact_match=*/false);
4144:     }
4145:   }
4146:   return false;
4147: }
```
```cpp
4654:       const uint widx = REF_SLICE_WIN_1 + wno;
4655: 
4656:       QEP_TAB *tab = &qep_tab[curr_tmp_table];
4657:       mem_root_deque<Item *> *orig_fields = curr_fields;
4658:       {
4659:         Opt_trace_object trace_this_tbl(trace);
4660:         trace_this_tbl
4661:             .add("adding_tmp_table_in_plan_at_position", curr_tmp_table)
4662:             .add_alnum("cause", "output_for_window_functions")
4663:             .add("with_buffer", m_windows[wno]->needs_buffering());
4664: 
4665:         if (create_intermediate_table(tab, *curr_fields, dummy, false))
4666:           return true;
4667: 
4668:         if (alloc_ref_item_slice(thd, widx)) return true;
4669: 
4670:         if (change_to_use_tmp_fields(curr_fields, thd, ref_items[widx],
4671:                                      &tmp_fields[widx],
4672:                                      query_block->m_added_non_hidden_fields))
4673:           return true;
4674: 
4675:         curr_fields = &tmp_fields[widx];
4676:         set_ref_item_slice(widx);
4677:         tab->ref_item_slice = widx;
4678:         setup_tmptable_write_func(tab, &trace_this_tbl);
4679:       }
4680: 
4681:       if (m_windows[wno]->needs_buffering()) {
4682:         if (CreateFramebufferTable(
4683:                 thd, tmp_table_param, *query_block, *orig_fields, *curr_fields,
4684:                 tab->tmp_table_param->items_to_copy, m_windows[wno])) {
4685:           return true;
4686:         }
4687:       }
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
- [Requirements/mysql/req/item_property_recalculation_248c7f7c227e/item_property_recalculation_248c7f7c227e_1.txt](../prompt_pipeline_20261104/generation/input_bundle/Requirements/mysql/req/item_property_recalculation_248c7f7c227e/item_property_recalculation_248c7f7c227e_1.txt)
- [Prompts/mysql/req2test/item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/req2test/item_property_recalculation_248c7f7c227e.txt)

## 1. 首次 Codex

上下文：同一助手共享对话，无独立 API 信封；[生成清单](../prompt_pipeline_20261104/generation/generation_manifest.json)，[上下文审查](../prompt_pipeline_20261104/contamination_review.md)。生成清单中的未执行状态为历史快照，后续执行见本节运行证据。

### Stage 1 输出：测试偏好与需求原文

原件：[item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/stage1_src2req/item_property_recalculation_248c7f7c227e.txt)

````text
Target
Revision 248c7f7c227e76f3422378ca3b9e10d141dcfc86; parent 15980860ac2639f41dfbda2f7fffb7aeeab32921. Test two separate candidate mechanisms: accumulated window properties across expression reuse/materialization, and properties of a window expression used as the left operand of IN (SELECT ...). Do not assume they represent the same defect.

Source-required conditions
The analysis stage extracted these conditions from the target-revision source:
1. Item_func::update_used_tables resets m_accum_properties to zero and recomputes it from ordinary arguments (sql/item_func.cc:708-719). An expression with a window-function descendant supplies an observable PROP_WINDOW_FUNCTION; constant arithmetic alone does not.
2. Item_ref::update_used_tables preserves PROP_ROLLUP_EXPR, then incorporates its referred Item's properties (sql/item.h:5747-5755). Trace the reference identity and actual call; a SQL alias is only a candidate way to introduce a reference, not proof that this override is used.
3. For buffered windows, CreateFramebufferTable uses orig_item->has_wf() to exclude window-derived output fields from the framebuffer and uses has_wf() again for replacement of materialized arguments (sql/sql_select.cc:4106-4144). The caller checks needs_buffering (4681-4687).
4. Item_in_optimizer wraps Item_in_subselect as args[0] (sql/item_cmpfunc.h:472-504). fix_left accumulates left_expr properties (sql/item_cmpfunc.cc:2173-2175), while update_used_tables calls the generic reset/reaccumulation (2410-2419). Item_in_subselect::update_used_tables explicitly updates the left expression and its used-table bits (sql/item_subselect.cc:2537-2541). This excerpt does not itself prove how the inherited base preserves every accumulated flag; inspect that missing base code before asserting a lost flag.
5. The property bits include subquery, stored program, aggregation, window, rollup and grouping (sql/item.h:3443-3465). This SQL batch targets window properties and IN wrapping; it does not claim coverage of stored-function restoration or all other bits.

Candidate construction
Case family A: make one small temporary table with (g,id,v), unique ordering within each partition, integer values and NULLs. Select an arithmetic wrapper around SUM(v) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING), together with ROW_NUMBER over descending id. The two orders and buffered SUM are candidates for intermediate-table/reference processing. Use a prepared statement with a bound numeric offset: execute twice with the same data/offset, then again with a changed offset, and compare with an ordinary direct query. Do not deallocate/reprepare between repeats. Select order by g,id. Repeated execution is a reuse candidate; a trace must show which Item objects and update calls actually recur.
Case family B: in the SELECT list, put the wrapped SUM window expression directly on the left of IN (SELECT k FROM a separate small lookup table). Also return the wrapped value and order by g,id. Keep the expression in the same query block as the window; moving it to an outer derived-table field would weaken the intended property-propagation target. Use a nonempty lookup table containing both a matching integer and NULL. Capture repeated prepared executions and a direct-query control separately. An IN predicate in the projection avoids intentionally filtering away UNKNOWN. Record whether an Item_in_optimizer was actually selected; textual IN syntax alone is insufficient.

Correctness oracle
For the first partition, use v=[10,NULL,30,40] ordered by id=[1,2,3,4]. CURRENT ROW through 1 FOLLOWING gives SUM=[10,30,70,40]. Adding offset 1 yields [11,31,71,41]; offset 11 yields [21,41,81,51]. Descending row numbers in ascending output order are [4,3,2,1]. A second partition with two NULL values yields NULL wrapped sums and descending row numbers [2,1]. Repeated identical executions must yield the same ordered rows.
For family B, with lookup values [11,71,NULL], left values [11,31,71,41,NULL,NULL] produce IN results [1,NULL,1,NULL,NULL,NULL]. Unmatched non-NULL values yield UNKNOWN because the lookup contains NULL; they must not be judged as zero. After removing the lookup NULL, the same left values yield [1,0,1,0,NULL,NULL]. These truth tables and frame sums are independent semantic expectations, not outputs copied from another server version.

Coverage observation
At sql/item_func.cc:708-717 record Item identity, accumulated properties before reset and after accumulation, argument identities and their property bits. At Item_ref::update_used_tables record referred objects and retained/added flags. For family A, correlate those identities with CreateFramebufferTable orig_item->has_wf() decisions and materialized-item replacement across executions. For family B, capture the Item_in_optimizer wrapper, Item_in_subselect and left_expr property masks during fix_left, fix_fields and update_used_tables. Keep each family's execution/coverage result separate.

Uncertainty
The supplied snippets do not provide every optimizer caller, base Item_subselect implementation, prepared-statement lifetime transition or window-expression placement rule. SQL validity, wrapper selection, actual repeated calls and object reuse require runtime checks on the target build. A SQL error is not automatically a wrong-result finding. If the desired wrapper/property path is absent, return its trace and missing base/caller questions to source analysis. The generated batch does not test stored programs, ROLLUP or every affected property. These requirements were generated by this assistant from the src2req prompt, without executing SQL.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/stage2_req2test/prompts/item_property_recalculation_248c7f7c227e.txt)

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
Revision 248c7f7c227e76f3422378ca3b9e10d141dcfc86; parent 15980860ac2639f41dfbda2f7fffb7aeeab32921. Test two separate candidate mechanisms: accumulated window properties across expression reuse/materialization, and properties of a window expression used as the left operand of IN (SELECT ...). Do not assume they represent the same defect.

Source-required conditions
The analysis stage extracted these conditions from the target-revision source:
1. Item_func::update_used_tables resets m_accum_properties to zero and recomputes it from ordinary arguments (sql/item_func.cc:708-719). An expression with a window-function descendant supplies an observable PROP_WINDOW_FUNCTION; constant arithmetic alone does not.
2. Item_ref::update_used_tables preserves PROP_ROLLUP_EXPR, then incorporates its referred Item's properties (sql/item.h:5747-5755). Trace the reference identity and actual call; a SQL alias is only a candidate way to introduce a reference, not proof that this override is used.
3. For buffered windows, CreateFramebufferTable uses orig_item->has_wf() to exclude window-derived output fields from the framebuffer and uses has_wf() again for replacement of materialized arguments (sql/sql_select.cc:4106-4144). The caller checks needs_buffering (4681-4687).
4. Item_in_optimizer wraps Item_in_subselect as args[0] (sql/item_cmpfunc.h:472-504). fix_left accumulates left_expr properties (sql/item_cmpfunc.cc:2173-2175), while update_used_tables calls the generic reset/reaccumulation (2410-2419). Item_in_subselect::update_used_tables explicitly updates the left expression and its used-table bits (sql/item_subselect.cc:2537-2541). This excerpt does not itself prove how the inherited base preserves every accumulated flag; inspect that missing base code before asserting a lost flag.
5. The property bits include subquery, stored program, aggregation, window, rollup and grouping (sql/item.h:3443-3465). This SQL batch targets window properties and IN wrapping; it does not claim coverage of stored-function restoration or all other bits.

Candidate construction
Case family A: make one small temporary table with (g,id,v), unique ordering within each partition, integer values and NULLs. Select an arithmetic wrapper around SUM(v) OVER (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING), together with ROW_NUMBER over descending id. The two orders and buffered SUM are candidates for intermediate-table/reference processing. Use a prepared statement with a bound numeric offset: execute twice with the same data/offset, then again with a changed offset, and compare with an ordinary direct query. Do not deallocate/reprepare between repeats. Select order by g,id. Repeated execution is a reuse candidate; a trace must show which Item objects and update calls actually recur.
Case family B: in the SELECT list, put the wrapped SUM window expression directly on the left of IN (SELECT k FROM a separate small lookup table). Also return the wrapped value and order by g,id. Keep the expression in the same query block as the window; moving it to an outer derived-table field would weaken the intended property-propagation target. Use a nonempty lookup table containing both a matching integer and NULL. Capture repeated prepared executions and a direct-query control separately. An IN predicate in the projection avoids intentionally filtering away UNKNOWN. Record whether an Item_in_optimizer was actually selected; textual IN syntax alone is insufficient.

Correctness oracle
For the first partition, use v=[10,NULL,30,40] ordered by id=[1,2,3,4]. CURRENT ROW through 1 FOLLOWING gives SUM=[10,30,70,40]. Adding offset 1 yields [11,31,71,41]; offset 11 yields [21,41,81,51]. Descending row numbers in ascending output order are [4,3,2,1]. A second partition with two NULL values yields NULL wrapped sums and descending row numbers [2,1]. Repeated identical executions must yield the same ordered rows.
For family B, with lookup values [11,71,NULL], left values [11,31,71,41,NULL,NULL] produce IN results [1,NULL,1,NULL,NULL,NULL]. Unmatched non-NULL values yield UNKNOWN because the lookup contains NULL; they must not be judged as zero. After removing the lookup NULL, the same left values yield [1,0,1,0,NULL,NULL]. These truth tables and frame sums are independent semantic expectations, not outputs copied from another server version.

Coverage observation
At sql/item_func.cc:708-717 record Item identity, accumulated properties before reset and after accumulation, argument identities and their property bits. At Item_ref::update_used_tables record referred objects and retained/added flags. For family A, correlate those identities with CreateFramebufferTable orig_item->has_wf() decisions and materialized-item replacement across executions. For family B, capture the Item_in_optimizer wrapper, Item_in_subselect and left_expr property masks during fix_left, fix_fields and update_used_tables. Keep each family's execution/coverage result separate.

Uncertainty
The supplied snippets do not provide every optimizer caller, base Item_subselect implementation, prepared-statement lifetime transition or window-expression placement rule. SQL validity, wrapper selection, actual repeated calls and object reuse require runtime checks on the target build. A SQL error is not automatically a wrong-result finding. If the desired wrapper/property path is absent, return its trace and missing base/caller questions to source analysis. The generated batch does not test stored programs, ROLLUP or every affected property. These requirements were generated by this assistant from the src2req prompt, without executing SQL.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[item_property_recalculation_248c7f7c227e.txt](../prompt_pipeline_20261104/generation/stage2_req2test/responses/item_property_recalculation_248c7f7c227e.txt)

````text
Prerequisites
Use a target-revision MySQL build with window functions and SQL prepared statements, a fresh session, and a selected disposable schema. No existing wf_248_* temporary table or prepared statement may share these names. Execute the entire file in one connection; the question mark is a real bound prepared-statement parameter, supplied by each EXECUTE USING. Do not split PREPARE/EXECUTE into separate connections. Temporary tables and prepared statements disappear when the session closes after an error. The IN expression is a SQL candidate whose acceptance and chosen internal wrapper still need verification on the target server.

SQL
```sql
-- Target: 248c7f7c227e76f3422378ca3b9e10d141dcfc86.
-- Fresh session, selected disposable schema, unique temporary-table/statement names.
SELECT VERSION() AS server_version, DATABASE() AS test_schema;
CREATE TEMPORARY TABLE wf_248_values (g INT, id INT, v INT, PRIMARY KEY (g,id));
CREATE TEMPORARY TABLE wf_248_lookup (k INT);
INSERT INTO wf_248_values VALUES
 (1,1,10),(1,2,NULL),(1,3,30),(1,4,40),(2,1,NULL),(2,2,NULL);
INSERT INTO wf_248_lookup VALUES (11),(71),(NULL);

PREPARE wf_248_a FROM 'SELECT g, id, ? + SUM(v) OVER w AS wrapped,
       ROW_NUMBER() OVER (PARTITION BY g ORDER BY id DESC) AS rn_rev
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id';

SET @wf_248_offset = 1;

-- CASE PROP_A1_PREPARED
SELECT 'PROP_A1_PREPARED' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

SET @wf_248_offset = 1;

-- CASE PROP_A2_REPEAT
SELECT 'PROP_A2_REPEAT' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

SET @wf_248_offset = 11;

-- CASE PROP_A3_OFFSET
SELECT 'PROP_A3_OFFSET' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

-- CASE PROP_A4_DIRECT
SELECT 'PROP_A4_DIRECT' AS case_id;
SELECT g, id, 11 + SUM(v) OVER w AS wrapped,
       ROW_NUMBER() OVER (PARTITION BY g ORDER BY id DESC) AS rn_rev
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id;

DEALLOCATE PREPARE wf_248_a;

PREPARE wf_248_b FROM 'SELECT g, id, 1 + SUM(v) OVER w AS wrapped,
       (1 + SUM(v) OVER w) IN (SELECT k FROM wf_248_lookup) AS in_result
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id';

-- CASE PROP_B1_PREPARED
SELECT 'PROP_B1_PREPARED' AS case_id;
EXECUTE wf_248_b;

-- CASE PROP_B2_REPEAT
SELECT 'PROP_B2_REPEAT' AS case_id;
EXECUTE wf_248_b;

-- CASE PROP_B3_DIRECT
SELECT 'PROP_B3_DIRECT' AS case_id;
SELECT g, id, 1 + SUM(v) OVER w AS wrapped,
       (1 + SUM(v) OVER w) IN (SELECT k FROM wf_248_lookup) AS in_result
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id;

DELETE FROM wf_248_lookup WHERE k IS NULL;

-- CASE PROP_B4_NO_NULL
SELECT 'PROP_B4_NO_NULL' AS case_id;
EXECUTE wf_248_b;

DEALLOCATE PREPARE wf_248_b;
DROP TEMPORARY TABLE wf_248_lookup;
DROP TEMPORARY TABLE wf_248_values;
```

Expected results and oracle
Family A's two-row frames yield SUM 10,30,70,40 for group 1 and NULL,NULL for group 2; add the supplied offset only to non-NULL sums. Descending row numbers are 4,3,2,1 and 2,1. A1 and A2 repeat the identical prepared object and parameter. A3 changes the offset without reprepare; A4 checks the corresponding direct form. Family B starts with lookup [11,71,NULL]: unmatched 31 and 41 yield NULL, not 0. After deleting the lookup NULL, they yield 0. A NULL left operand yields NULL against the remaining nonempty lookup. All expectations are independently computed; repeated/direct query agreement alone is not sufficient.

PROP_A1_PREPARED: columns=['g', 'id', 'wrapped', 'rn_rev']; expected=[[1, 1, 11, 4], [1, 2, 31, 3], [1, 3, 71, 2], [1, 4, 41, 1], [2, 1, null, 2], [2, 2, null, 1]]
PROP_A2_REPEAT: columns=['g', 'id', 'wrapped', 'rn_rev']; expected=[[1, 1, 11, 4], [1, 2, 31, 3], [1, 3, 71, 2], [1, 4, 41, 1], [2, 1, null, 2], [2, 2, null, 1]]
PROP_A3_OFFSET: columns=['g', 'id', 'wrapped', 'rn_rev']; expected=[[1, 1, 21, 4], [1, 2, 41, 3], [1, 3, 81, 2], [1, 4, 51, 1], [2, 1, null, 2], [2, 2, null, 1]]
PROP_A4_DIRECT: columns=['g', 'id', 'wrapped', 'rn_rev']; expected=[[1, 1, 21, 4], [1, 2, 41, 3], [1, 3, 81, 2], [1, 4, 51, 1], [2, 1, null, 2], [2, 2, null, 1]]
PROP_B1_PREPARED: columns=['g', 'id', 'wrapped', 'in_result']; expected=[[1, 1, 11, 1], [1, 2, 31, null], [1, 3, 71, 1], [1, 4, 41, null], [2, 1, null, null], [2, 2, null, null]]
PROP_B2_REPEAT: columns=['g', 'id', 'wrapped', 'in_result']; expected=[[1, 1, 11, 1], [1, 2, 31, null], [1, 3, 71, 1], [1, 4, 41, null], [2, 1, null, null], [2, 2, null, null]]
PROP_B3_DIRECT: columns=['g', 'id', 'wrapped', 'in_result']; expected=[[1, 1, 11, 1], [1, 2, 31, null], [1, 3, 71, 1], [1, 4, 41, null], [2, 1, null, null], [2, 2, null, null]]
PROP_B4_NO_NULL: columns=['g', 'id', 'wrapped', 'in_result']; expected=[[1, 1, 11, 1], [1, 2, 31, 0], [1, 3, 71, 1], [1, 4, 41, 0], [2, 1, null, null], [2, 2, null, null]]

Coverage observation
Keep family A and B results separate. Record masks/Item identities before and after Item_func::update_used_tables (sql/item_func.cc:708-719), and referenced identities at sql/item.h:5747-5755. In A, correlate PROP_WINDOW_FUNCTION and has_wf() with sql/sql_select.cc:4115-4119 and 4139-4143 across executions. In B, verify Item_in_optimizer actually wraps Item_in_subselect; record left_expr flags at sql/item_cmpfunc.cc:2173-2175 and after 2410-2419 / sql/item_subselect.cc:2537-2541. An IN keyword or a repeated EXECUTE does not establish those paths. Stored-program and rollup branches are outside this batch.

Execution status
Generated by the current assistant from the saved req2test prompt and its new src2req requirements. No database was connected, SQL executed, or source coverage measured. Expected rows are semantic calculations, not observed results. Retain SQL errors/crashes/missing results as separate observations; do not silently treat them as correct or as confirmed bugs.
````

### 提取后实际执行的完整 SQL

原件：[item_property_recalculation_248c7f7c227e.sql](../prompt_pipeline_20261104/generation/sql/item_property_recalculation_248c7f7c227e.sql)

````sql
-- Target: 248c7f7c227e76f3422378ca3b9e10d141dcfc86.
-- Fresh session, selected disposable schema, unique temporary-table/statement names.
SELECT VERSION() AS server_version, DATABASE() AS test_schema;
CREATE TEMPORARY TABLE wf_248_values (g INT, id INT, v INT, PRIMARY KEY (g,id));
CREATE TEMPORARY TABLE wf_248_lookup (k INT);
INSERT INTO wf_248_values VALUES
 (1,1,10),(1,2,NULL),(1,3,30),(1,4,40),(2,1,NULL),(2,2,NULL);
INSERT INTO wf_248_lookup VALUES (11),(71),(NULL);

PREPARE wf_248_a FROM 'SELECT g, id, ? + SUM(v) OVER w AS wrapped,
       ROW_NUMBER() OVER (PARTITION BY g ORDER BY id DESC) AS rn_rev
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id';

SET @wf_248_offset = 1;

-- CASE PROP_A1_PREPARED
SELECT 'PROP_A1_PREPARED' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

SET @wf_248_offset = 1;

-- CASE PROP_A2_REPEAT
SELECT 'PROP_A2_REPEAT' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

SET @wf_248_offset = 11;

-- CASE PROP_A3_OFFSET
SELECT 'PROP_A3_OFFSET' AS case_id;
EXECUTE wf_248_a USING @wf_248_offset;

-- CASE PROP_A4_DIRECT
SELECT 'PROP_A4_DIRECT' AS case_id;
SELECT g, id, 11 + SUM(v) OVER w AS wrapped,
       ROW_NUMBER() OVER (PARTITION BY g ORDER BY id DESC) AS rn_rev
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id;

DEALLOCATE PREPARE wf_248_a;

PREPARE wf_248_b FROM 'SELECT g, id, 1 + SUM(v) OVER w AS wrapped,
       (1 + SUM(v) OVER w) IN (SELECT k FROM wf_248_lookup) AS in_result
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id';

-- CASE PROP_B1_PREPARED
SELECT 'PROP_B1_PREPARED' AS case_id;
EXECUTE wf_248_b;

-- CASE PROP_B2_REPEAT
SELECT 'PROP_B2_REPEAT' AS case_id;
EXECUTE wf_248_b;

-- CASE PROP_B3_DIRECT
SELECT 'PROP_B3_DIRECT' AS case_id;
SELECT g, id, 1 + SUM(v) OVER w AS wrapped,
       (1 + SUM(v) OVER w) IN (SELECT k FROM wf_248_lookup) AS in_result
FROM wf_248_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING)
ORDER BY g,id;

DELETE FROM wf_248_lookup WHERE k IS NULL;

-- CASE PROP_B4_NO_NULL
SELECT 'PROP_B4_NO_NULL' AS case_id;
EXECUTE wf_248_b;

DEALLOCATE PREPARE wf_248_b;
DROP TEMPORARY TABLE wf_248_lookup;
DROP TEMPORARY TABLE wf_248_values;
````

### 独立保存的预期结果与 oracle

原件：[item_property_recalculation_248c7f7c227e.json](../prompt_pipeline_20261104/generation/expected/item_property_recalculation_248c7f7c227e.json)

````json
{
  "target": "item_property_recalculation_248c7f7c227e",
  "row_order": "significant; each data SELECT orders by stable keys",
  "result_protocol": "A one-row case_id result identifies the next data result set. Environment metadata is not a test result. Case labels must be present in the specified order; omitted/error results cannot pass.",
  "null_encoding": "JSON null means SQL NULL, never zero or an empty string",
  "cases": [
    {
      "case_id": "PROP_A1_PREPARED",
      "family": "wrapped_window_reuse",
      "offset": 1,
      "columns": [
        "g",
        "id",
        "wrapped",
        "rn_rev"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          4
        ],
        [
          1,
          2,
          31,
          3
        ],
        [
          1,
          3,
          71,
          2
        ],
        [
          1,
          4,
          41,
          1
        ],
        [
          2,
          1,
          null,
          2
        ],
        [
          2,
          2,
          null,
          1
        ]
      ]
    },
    {
      "case_id": "PROP_A2_REPEAT",
      "family": "wrapped_window_reuse",
      "offset": 1,
      "columns": [
        "g",
        "id",
        "wrapped",
        "rn_rev"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          4
        ],
        [
          1,
          2,
          31,
          3
        ],
        [
          1,
          3,
          71,
          2
        ],
        [
          1,
          4,
          41,
          1
        ],
        [
          2,
          1,
          null,
          2
        ],
        [
          2,
          2,
          null,
          1
        ]
      ]
    },
    {
      "case_id": "PROP_A3_OFFSET",
      "family": "wrapped_window_reuse",
      "offset": 11,
      "columns": [
        "g",
        "id",
        "wrapped",
        "rn_rev"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          21,
          4
        ],
        [
          1,
          2,
          41,
          3
        ],
        [
          1,
          3,
          81,
          2
        ],
        [
          1,
          4,
          51,
          1
        ],
        [
          2,
          1,
          null,
          2
        ],
        [
          2,
          2,
          null,
          1
        ]
      ]
    },
    {
      "case_id": "PROP_A4_DIRECT",
      "family": "wrapped_window_reuse",
      "offset": 11,
      "columns": [
        "g",
        "id",
        "wrapped",
        "rn_rev"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          21,
          4
        ],
        [
          1,
          2,
          41,
          3
        ],
        [
          1,
          3,
          81,
          2
        ],
        [
          1,
          4,
          51,
          1
        ],
        [
          2,
          1,
          null,
          2
        ],
        [
          2,
          2,
          null,
          1
        ]
      ]
    },
    {
      "case_id": "PROP_B1_PREPARED",
      "family": "in_left_window_property",
      "lookup_contains_null": true,
      "columns": [
        "g",
        "id",
        "wrapped",
        "in_result"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          1
        ],
        [
          1,
          2,
          31,
          null
        ],
        [
          1,
          3,
          71,
          1
        ],
        [
          1,
          4,
          41,
          null
        ],
        [
          2,
          1,
          null,
          null
        ],
        [
          2,
          2,
          null,
          null
        ]
      ]
    },
    {
      "case_id": "PROP_B2_REPEAT",
      "family": "in_left_window_property",
      "lookup_contains_null": true,
      "columns": [
        "g",
        "id",
        "wrapped",
        "in_result"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          1
        ],
        [
          1,
          2,
          31,
          null
        ],
        [
          1,
          3,
          71,
          1
        ],
        [
          1,
          4,
          41,
          null
        ],
        [
          2,
          1,
          null,
          null
        ],
        [
          2,
          2,
          null,
          null
        ]
      ]
    },
    {
      "case_id": "PROP_B3_DIRECT",
      "family": "in_left_window_property",
      "lookup_contains_null": true,
      "columns": [
        "g",
        "id",
        "wrapped",
        "in_result"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          1
        ],
        [
          1,
          2,
          31,
          null
        ],
        [
          1,
          3,
          71,
          1
        ],
        [
          1,
          4,
          41,
          null
        ],
        [
          2,
          1,
          null,
          null
        ],
        [
          2,
          2,
          null,
          null
        ]
      ]
    },
    {
      "case_id": "PROP_B4_NO_NULL",
      "family": "in_left_window_property",
      "lookup_contains_null": false,
      "columns": [
        "g",
        "id",
        "wrapped",
        "in_result"
      ],
      "comparison": "numeric_exact",
      "rows": [
        [
          1,
          1,
          11,
          1
        ],
        [
          1,
          2,
          31,
          0
        ],
        [
          1,
          3,
          71,
          1
        ],
        [
          1,
          4,
          41,
          0
        ],
        [
          2,
          1,
          null,
          null
        ],
        [
          2,
          2,
          null,
          null
        ]
      ]
    }
  ]
}
````

### 执行环境、命令与三轮结果

#### 父提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/result.json)。精确 revision：`15980860ac2639f41dfbda2f7fffb7aeeab32921`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "item_property_recalculation_248c7f7c227e",
  "revision": "15980860ac2639f41dfbda2f7fffb7aeeab32921",
  "role": "parent",
  "run_id": "15980860ac26-e158c564",
  "started": "2026-11-04T03:51:17.067182+00:00",
  "sql_sha256": "6ee8f1f560ebbefd7a0f482f097488bec2dcf072146fa557c1c49a1490e1502f",
  "expected_sha256": "664745c5fe429016de668465500ca3b110c8afde8d9f74da20e9cacc9761f2bf",
  "runtime_path": "/CACHE_ROOT/mysql-intro-bisect-20261103/runtime/15980860ac26",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-15980860ac26-e158c564",
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
    "/CACHE_ROOT/mysql-intro-bisect-20261103/runtime/15980860ac26:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "15980860ac26-e158c564"
  ],
  "container_id": "adb60a4198301216db442f022d71b3a09bc4df2a21d34993439f12a7588fb0b1",
  "server_metadata_tsv": "8.0.33\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "73597157061e301fc34c01c4fa312f207d9b193c6c2b60dbbb31b354972d3966",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 4123269,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T03:51:20.397918455Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T03:51:35.184541+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T03:51:33.028839+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-15980860ac26-e158c564",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/15980860ac26-e158c564/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_15980860ac26_1"
      ],
      "schema": "wf_three_15980860ac26_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4123269,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:20.397918455Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:33.151668+00:00",
      "stdout_sha256": "18350a4c412a79be003be45520f48d777ffe3a5ede038a8095597352fbb65d36",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T03:51:33.247237+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-15980860ac26-e158c564",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/15980860ac26-e158c564/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_15980860ac26_2"
      ],
      "schema": "wf_three_15980860ac26_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4123269,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:20.397918455Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:33.383082+00:00",
      "stdout_sha256": "14f7293ed91317fc3ff0db0568ad8496d18cb357118791672ca6d3b040f428d2",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T03:51:33.481364+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-15980860ac26-e158c564",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/15980860ac26-e158c564/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_15980860ac26_3"
      ],
      "schema": "wf_three_15980860ac26_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4123269,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:20.397918455Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:33.611908+00:00",
      "stdout_sha256": "633f8a2ef1ff9bface1c3b90d0a914bb28fc76e9b48f505b30301ecc1b865d8e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema |
| --- | --- |
| 8.0.33 | wf_three_15980860ac26_1 |

结果集 2：

| case_id |
| --- |
| PROP_A1_PREPARED |

结果集 3：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 11.000000000000000000000000000000 | 4 |
| 1 | 2 | 31.000000000000000000000000000000 | 3 |
| 1 | 3 | 71.000000000000000000000000000000 | 2 |
| 1 | 4 | 41.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 4：

| case_id |
| --- |
| PROP_A2_REPEAT |

结果集 5：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 11.000000000000000000000000000000 | 4 |
| 1 | 2 | 31.000000000000000000000000000000 | 3 |
| 1 | 3 | 71.000000000000000000000000000000 | 2 |
| 1 | 4 | 41.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 6：

| case_id |
| --- |
| PROP_A3_OFFSET |

结果集 7：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 21.000000000000000000000000000000 | 4 |
| 1 | 2 | 41.000000000000000000000000000000 | 3 |
| 1 | 3 | 81.000000000000000000000000000000 | 2 |
| 1 | 4 | 51.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 8：

| case_id |
| --- |
| PROP_A4_DIRECT |

结果集 9：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 21 | 4 |
| 1 | 2 | 41 | 3 |
| 1 | 3 | 81 | 2 |
| 1 | 4 | 51 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 10：

| case_id |
| --- |
| PROP_B1_PREPARED |

结果集 11：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | NULL |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

结果集 12：

| case_id |
| --- |
| PROP_B2_REPEAT |

结果集 13：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | NULL |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

结果集 14：

| case_id |
| --- |
| PROP_B3_DIRECT |

结果集 15：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | NULL |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

结果集 16：

| case_id |
| --- |
| PROP_B4_NO_NULL |

结果集 17：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | 0 |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | 0 |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/result.json)。精确 revision：`248c7f7c227e76f3422378ca3b9e10d141dcfc86`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "item_property_recalculation_248c7f7c227e",
  "revision": "248c7f7c227e76f3422378ca3b9e10d141dcfc86",
  "role": "target",
  "run_id": "248c7f7c227e-d56f3694",
  "started": "2026-11-04T03:51:35.428647+00:00",
  "sql_sha256": "6ee8f1f560ebbefd7a0f482f097488bec2dcf072146fa557c1c49a1490e1502f",
  "expected_sha256": "664745c5fe429016de668465500ca3b110c8afde8d9f74da20e9cacc9761f2bf",
  "runtime_path": "/CACHE_ROOT/mysql-intro-bisect-20261103/runtime/248c7f7c227e",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-248c7f7c227e-d56f3694",
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
    "/CACHE_ROOT/mysql-intro-bisect-20261103/runtime/248c7f7c227e:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "248c7f7c227e-d56f3694"
  ],
  "container_id": "6a0c5838c25ae4e6344c403a23ca12e0ce614655bf194def2227a8e27996ed85",
  "server_metadata_tsv": "8.0.33\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "4e692b40d470773b14ba7adb77e3964e50aa423bb04ed826db39a6b538e86416",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 4127948,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T03:51:35.86738906Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T03:51:49.393184+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T03:51:47.844507+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-248c7f7c227e-d56f3694",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/248c7f7c227e-d56f3694/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_248c7f7c227e_1"
      ],
      "schema": "wf_three_248c7f7c227e_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4127948,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:35.86738906Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:47.995452+00:00",
      "stdout_sha256": "d0fb7efbbeda6e765f0a83728ae186b63ee14dbd133d98667c34add65240a467",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T03:51:48.097109+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-248c7f7c227e-d56f3694",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/248c7f7c227e-d56f3694/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_248c7f7c227e_2"
      ],
      "schema": "wf_three_248c7f7c227e_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4127948,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:35.86738906Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:48.224643+00:00",
      "stdout_sha256": "36725648e636d58834cfd2aad08a00ac122d867c4943e9e275019d6c39690e3a",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T03:51:48.324646+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-248c7f7c227e-d56f3694",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/248c7f7c227e-d56f3694/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_248c7f7c227e_3"
      ],
      "schema": "wf_three_248c7f7c227e_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 4127948,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T03:51:35.86738906Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T03:51:48.461084+00:00",
      "stdout_sha256": "e83bc3e720258a15aa1992096991e3a0455405b1353626fa45888fc8f81f516b",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/item_property_recalculation_248c7f7c227e/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema |
| --- | --- |
| 8.0.33 | wf_three_248c7f7c227e_1 |

结果集 2：

| case_id |
| --- |
| PROP_A1_PREPARED |

结果集 3：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 11.000000000000000000000000000000 | 4 |
| 1 | 2 | 31.000000000000000000000000000000 | 3 |
| 1 | 3 | 71.000000000000000000000000000000 | 2 |
| 1 | 4 | 41.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 4：

| case_id |
| --- |
| PROP_A2_REPEAT |

结果集 5：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 11.000000000000000000000000000000 | 4 |
| 1 | 2 | 31.000000000000000000000000000000 | 3 |
| 1 | 3 | 71.000000000000000000000000000000 | 2 |
| 1 | 4 | 41.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 6：

| case_id |
| --- |
| PROP_A3_OFFSET |

结果集 7：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 21.000000000000000000000000000000 | 4 |
| 1 | 2 | 41.000000000000000000000000000000 | 3 |
| 1 | 3 | 81.000000000000000000000000000000 | 2 |
| 1 | 4 | 51.000000000000000000000000000000 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 8：

| case_id |
| --- |
| PROP_A4_DIRECT |

结果集 9：

| g | id | wrapped | rn_rev |
| --- | --- | --- | --- |
| 1 | 1 | 21 | 4 |
| 1 | 2 | 41 | 3 |
| 1 | 3 | 81 | 2 |
| 1 | 4 | 51 | 1 |
| 2 | 1 | NULL | 2 |
| 2 | 2 | NULL | 1 |

结果集 10：

| case_id |
| --- |
| PROP_B1_PREPARED |

结果集 11：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | NULL |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

结果集 12：

| case_id |
| --- |
| PROP_B2_REPEAT |

结果集 13：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | NULL | 1 |
| 1 | 2 | 11 | NULL |
| 1 | 3 | 21 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | 111 | NULL |
| 2 | 2 | 81 | NULL |

结果集 14：

| case_id |
| --- |
| PROP_B3_DIRECT |

结果集 15：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | 11 | 1 |
| 1 | 2 | 31 | NULL |
| 1 | 3 | 71 | 1 |
| 1 | 4 | 41 | NULL |
| 2 | 1 | NULL | NULL |
| 2 | 2 | NULL | NULL |

结果集 16：

| case_id |
| --- |
| PROP_B4_NO_NULL |

结果集 17：

| g | id | wrapped | in_result |
| --- | --- | --- | --- |
| 1 | 1 | NULL | 1 |
| 1 | 2 | 11 | 0 |
| 1 | 3 | 21 | 1 |
| 1 | 4 | 41 | 0 |
| 2 | 1 | 111 | NULL |
| 2 | 2 | 81 | NULL |

判定与环境补充：[逐检查点比较](../prompt_pipeline_20261104/runtime/comparison.json)、[完整执行报告](../prompt_pipeline_20261104/runtime/final_report.txt)、[输入构建执行关联](../prompt_pipeline_20261104/lineage.json)。

## 2. DeepSeek 重跑

Stage 1 实际请求 [stage1_request.json](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage1_request.json)；原始响应 [stage1_response_raw.json](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage1_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

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
      "content_characters": 17878
    }
  ]
}
```

Stage 2 实际请求 [stage2_request.json](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage2_request.json)；原始响应 [stage2_response_raw.json](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage2_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

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
      "content_characters": 10077
    }
  ]
}
```

### Stage 1 输出：测试偏好与需求原文

原件：[stage1_output.txt](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage1_output.txt)

````text
Target: item_property_recalculation_248c7f7c227e

Target observation: Accumulated Item property recalculation across ordinary arguments, references and IN-subquery wrappers, and its use by window materialization.

Revision: 248c7f7c227e76f3422378ca3b9e10d141dcfc86
Parent revision: 15980860ac2639f41dfbda2f7fffb7aeeab32921
Source repository: https://github.com/mysql/mysql-server

Source-required conditions
- Item_func::update_used_tables() is invoked on an Item_func with one or more arguments (sql/item_func.cc:708-719). It resets m_accum_properties to 0 (line 711), then for each argument calls args[i]->update_used_tables() (line 714), ORs used_tables_cache and not_null_tables_cache from the argument (lines 715-716), and calls add_accum_properties(args[i]) (line 717).
- Item_func_sp::update_used_tables() is invoked on a stored-program Item (sql/item_func.cc:8410-8415). It calls Item_func::update_used_tables() (line 8411), then set_stored_program() (line 8414) to re-add PROP_STORED_PROGRAM after the reset at line 711.
- Item_ref::update_used_tables() is invoked on an Item_ref whose depended_from is nullptr (sql/item.h:5747-5755). It calls ref_item()->update_used_tables() (line 5748), preserves only PROP_ROLLUP_EXPR from m_accum_properties (line 5753), and calls add_accum_properties(ref_item()) (line 5754).
- Item_in_optimizer::update_used_tables() is invoked on an IN-subquery wrapper (sql/item_cmpfunc.cc:2410-2419). It calls Item_func::update_used_tables() (line 2411), which resets and re-accumulates from args[0] (the Item_in_subselect). Afterward, unless abort_on_null is set and value_transform is BOOL_IS_TRUE, it re-applies not_null_tables_cache &= subqpred->left_expr->not_null_tables() (lines 2415-2418).
- Item_in_subselect::update_used_tables() is invoked on an IN-subquery predicate (sql/item_subselect.cc:2537-2541). It calls Item_subselect::update_used_tables() (line 2538), then left_expr->update_used_tables() (line 2539), and ORs left_expr->used_tables() into used_tables_cache (line 2540).
- In CreateFramebufferTable (sql/sql_select.cc:4106-4127), for each output field, if the original source item has_wf() returns true (line 4117), the corresponding framebuffer field is set to nullptr (line 4118) and later removed (lines 4121-4122). This depends on has_wf() reflecting PROP_WINDOW_FUNCTION accumulated from descendants (sql/item.h:3215, 3454).
- In the window output materialization path (sql/sql_select.cc:4654-4687), when m_windows[wno]->needs_buffering() is true (line 4681), CreateFramebufferTable is called (lines 4682-4685). The decision to buffer and the filtering of window-function fields both rely on the accumulated has_wf() property.

Candidate construction
Create a query with a window function whose argument or expression tree contains a subquery or stored function, so that m_accum_properties must include both PROP_WINDOW_FUNCTION and PROP_SUBQUERY or PROP_STORED_PROGRAM after update_used_tables(). For example, use an IN-subquery inside a window function expression, or a stored function call inside a window function, with the window function requiring buffering (e.g., a frame that is not ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW). The window function output should be materialized through the window output temporary table path at sql/sql_select.cc:4654-4687. An ordinary aggregate or non-window expression with a subquery can exercise the Item_func and Item_ref accumulation paths, but only a buffering window function exercises the has_wf() filtering in CreateFramebufferTable.

Correctness oracle
The correctness oracle is not about query output alone. Verify that after fix_fields() and update_used_tables(), the relevant Item tree has the expected accumulated properties: has_wf() is true for expressions containing a window function, has_subquery() is true for expressions containing a subquery, and has_stored_program() is true for stored-program calls. For the window materialization case, verify that the framebuffer table does not include columns whose source item has_wf() is true. Query results should match the expected window function semantics; any discrepancy in accumulated properties may cause incorrect framebuffer column filtering or replacement behavior.

Coverage observation
Instrument or break at Item_func::update_used_tables() (sql/item_func.cc:708), Item_ref::update_used_tables() (sql/item.h:5747), Item_in_optimizer::update_used_tables() (sql/item_cmpfunc.cc:2410), and CreateFramebufferTable (sql/sql_select.cc:4106). Confirm that the target Item tree reaches these methods, that m_accum_properties is reset and re-accumulated as expected, and that has_wf() is true for the source item whose framebuffer field is filtered at line 4117. EXPLAIN alone does not confirm property recalculation; it is only a plan clue.

Uncertainty
The local excerpts do not establish the full SQL-to-Item-tree construction path for window functions with subqueries or stored functions. The callers of update_used_tables() are not shown, so it is not proven that a given SQL query reaches these methods after fix_fields(). The exact conditions under which a window function needs_buffering() and thus reaches CreateFramebufferTable are not fully specified in the supplied excerpts. If the candidate does not reach the target, inspect the window materialization and Item construction callers before revising the candidate. Coverage and correct output are separate observations.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[stage2_prompt.txt](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage2_prompt.txt)

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
Target: item_property_recalculation_248c7f7c227e

Target observation: Accumulated Item property recalculation across ordinary arguments, references and IN-subquery wrappers, and its use by window materialization.

Revision: 248c7f7c227e76f3422378ca3b9e10d141dcfc86
Parent revision: 15980860ac2639f41dfbda2f7fffb7aeeab32921
Source repository: https://github.com/mysql/mysql-server

Source-required conditions
- Item_func::update_used_tables() is invoked on an Item_func with one or more arguments (sql/item_func.cc:708-719). It resets m_accum_properties to 0 (line 711), then for each argument calls args[i]->update_used_tables() (line 714), ORs used_tables_cache and not_null_tables_cache from the argument (lines 715-716), and calls add_accum_properties(args[i]) (line 717).
- Item_func_sp::update_used_tables() is invoked on a stored-program Item (sql/item_func.cc:8410-8415). It calls Item_func::update_used_tables() (line 8411), then set_stored_program() (line 8414) to re-add PROP_STORED_PROGRAM after the reset at line 711.
- Item_ref::update_used_tables() is invoked on an Item_ref whose depended_from is nullptr (sql/item.h:5747-5755). It calls ref_item()->update_used_tables() (line 5748), preserves only PROP_ROLLUP_EXPR from m_accum_properties (line 5753), and calls add_accum_properties(ref_item()) (line 5754).
- Item_in_optimizer::update_used_tables() is invoked on an IN-subquery wrapper (sql/item_cmpfunc.cc:2410-2419). It calls Item_func::update_used_tables() (line 2411), which resets and re-accumulates from args[0] (the Item_in_subselect). Afterward, unless abort_on_null is set and value_transform is BOOL_IS_TRUE, it re-applies not_null_tables_cache &= subqpred->left_expr->not_null_tables() (lines 2415-2418).
- Item_in_subselect::update_used_tables() is invoked on an IN-subquery predicate (sql/item_subselect.cc:2537-2541). It calls Item_subselect::update_used_tables() (line 2538), then left_expr->update_used_tables() (line 2539), and ORs left_expr->used_tables() into used_tables_cache (line 2540).
- In CreateFramebufferTable (sql/sql_select.cc:4106-4127), for each output field, if the original source item has_wf() returns true (line 4117), the corresponding framebuffer field is set to nullptr (line 4118) and later removed (lines 4121-4122). This depends on has_wf() reflecting PROP_WINDOW_FUNCTION accumulated from descendants (sql/item.h:3215, 3454).
- In the window output materialization path (sql/sql_select.cc:4654-4687), when m_windows[wno]->needs_buffering() is true (line 4681), CreateFramebufferTable is called (lines 4682-4685). The decision to buffer and the filtering of window-function fields both rely on the accumulated has_wf() property.

Candidate construction
Create a query with a window function whose argument or expression tree contains a subquery or stored function, so that m_accum_properties must include both PROP_WINDOW_FUNCTION and PROP_SUBQUERY or PROP_STORED_PROGRAM after update_used_tables(). For example, use an IN-subquery inside a window function expression, or a stored function call inside a window function, with the window function requiring buffering (e.g., a frame that is not ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW). The window function output should be materialized through the window output temporary table path at sql/sql_select.cc:4654-4687. An ordinary aggregate or non-window expression with a subquery can exercise the Item_func and Item_ref accumulation paths, but only a buffering window function exercises the has_wf() filtering in CreateFramebufferTable.

Correctness oracle
The correctness oracle is not about query output alone. Verify that after fix_fields() and update_used_tables(), the relevant Item tree has the expected accumulated properties: has_wf() is true for expressions containing a window function, has_subquery() is true for expressions containing a subquery, and has_stored_program() is true for stored-program calls. For the window materialization case, verify that the framebuffer table does not include columns whose source item has_wf() is true. Query results should match the expected window function semantics; any discrepancy in accumulated properties may cause incorrect framebuffer column filtering or replacement behavior.

Coverage observation
Instrument or break at Item_func::update_used_tables() (sql/item_func.cc:708), Item_ref::update_used_tables() (sql/item.h:5747), Item_in_optimizer::update_used_tables() (sql/item_cmpfunc.cc:2410), and CreateFramebufferTable (sql/sql_select.cc:4106). Confirm that the target Item tree reaches these methods, that m_accum_properties is reset and re-accumulated as expected, and that has_wf() is true for the source item whose framebuffer field is filtered at line 4117. EXPLAIN alone does not confirm property recalculation; it is only a plan clue.

Uncertainty
The local excerpts do not establish the full SQL-to-Item-tree construction path for window functions with subqueries or stored functions. The callers of update_used_tables() are not shown, so it is not proven that a given SQL query reaches these methods after fix_fields(). The exact conditions under which a window function needs_buffering() and thus reaches CreateFramebufferTable are not fully specified in the supplied excerpts. If the candidate does not reach the target, inspect the window materialization and Item construction callers before revising the candidate. Coverage and correct output are separate observations.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[stage2_output.txt](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/stage2_output.txt)

````text
Prerequisites
Use a disposable, already selected schema on a MySQL build at revision 248c7f7c227e76f3422378ca3b9e10d141dcfc86 (or a build whose sql/item_func.cc, sql/item.h, sql/item_cmpfunc.cc, sql/item_subselect.cc, and sql/sql_select.cc match the cited line ranges). The build must support window functions (MySQL 8.0+) and INTERSECT ALL is not required. Use a fresh session with no existing objects named wf_prop_src, wf_prop_sub, or wf_prop_fn. Because the coverage target is a source-level property-recalculation observation, the SQL alone cannot prove branch coverage; the coverage plan below describes the instrumentation needed. If the build does not expose CREATE FUNCTION or window functions, stop and record the precondition as unresolved rather than claiming coverage.

SQL
```sql
CREATE TEMPORARY TABLE wf_prop_src (k INT NOT NULL, v INT NOT NULL);
CREATE TEMPORARY TABLE wf_prop_sub (k INT NOT NULL);
INSERT INTO wf_prop_src VALUES (1,10),(1,20),(2,30),(2,40),(3,50);
INSERT INTO wf_prop_sub VALUES (1),(3);

-- Buffering window function (RANGE frame, not the ROWS UNBOUNDED PRECEDING..CURRENT ROW
-- default) whose argument tree contains an IN-subquery. This forces
-- Item_in_optimizer / Item_in_subselect / Item_ref accumulation inside a
-- window function argument, and forces window output materialization through
-- CreateFramebufferTable.
SELECT
  s.k,
  s.v,
  SUM(CASE WHEN s.k IN (SELECT k FROM wf_prop_sub) THEN s.v ELSE 0 END)
    OVER (PARTITION BY s.k ORDER BY s.v RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS win_sum
FROM wf_prop_src AS s
ORDER BY s.k, s.v;

-- Buffering window function whose argument is a stored function call, to
-- exercise Item_func_sp::update_used_tables() re-adding PROP_STORED_PROGRAM
-- after the reset in Item_func::update_used_tables().
DROP FUNCTION IF EXISTS wf_prop_fn;
CREATE FUNCTION wf_prop_fn(x INT) RETURNS INT DETERMINISTIC NO SQL RETURN x * 2;

SELECT
  s.k,
  s.v,
  SUM(wf_prop_fn(s.v))
    OVER (PARTITION BY s.k ORDER BY s.v RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS win_fn_sum
FROM wf_prop_src AS s
ORDER BY s.k, s.v;

DROP FUNCTION wf_prop_fn;
DROP TEMPORARY TABLE wf_prop_sub;
DROP TEMPORARY TABLE wf_prop_src;
```

Expected results and oracle
First SELECT (IN-subquery inside a buffering window argument). Derive from the inserted data:
- wf_prop_src rows: (1,10),(1,20),(2,30),(2,40),(3,50). wf_prop_sub = {1,3}.
- CASE yields s.v when s.k ∈ {1,3}, else 0. Per row: (1,10)→10, (1,20)→20, (2,30)→0, (2,40)→0, (3,50)→50.
- RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING over PARTITION BY k ORDER BY v sums the whole partition. Partitions: k=1 → 10+20=30; k=2 → 0+0=0; k=3 → 50.
- Expected rows in ORDER BY k, v:
  (1,10,30), (1,20,30), (2,30,0), (2,40,0), (3,50,50).

Second SELECT (stored-function call inside a buffering window argument). wf_prop_fn(v)=2v.
- Per-row doubled values: (1,10)→20, (1,20)→40, (2,30)→60, (2,40)→80, (3,50)→100.
- Whole-partition sums: k=1 → 60; k=2 → 140; k=3 → 100.
- Expected rows in ORDER BY k, v:
  (1,10,60), (1,20,60), (2,30,140), (2,40,140), (3,50,100).

The query-output oracle checks window semantics only. It does not by itself demonstrate that m_accum_properties was reset and re-accumulated, nor that has_wf() was true for the source item filtered at sql/sql_select.cc:4117. Those are the separate coverage observations below. If either SELECT fails, retain the failure separately; close the session to release remaining temporary tables and drop wf_prop_fn if the session is reused.

Coverage observation
At revision 248c7f7c227e76f3422378ca3b9e10d141dcfc86, instrument or break at:
- sql/item_func.cc:708 (Item_func::update_used_tables), lines 711 (m_accum_properties reset) and 714–717 (per-argument update and add_accum_properties);
- sql/item_func.cc:8410 (Item_func_sp::update_used_tables), confirming line 8411 delegates to Item_func::update_used_tables and line 8414 re-adds PROP_STORED_PROGRAM;
- sql/item.h:5747 (Item_ref::update_used_tables), confirming line 5753 preserves only PROP_ROLLUP_EXPR and line 5754 re-adds ref_item() properties;
- sql/item_cmpfunc.cc:2410 (Item_in_optimizer::update_used_tables), confirming line 2411 delegates and lines 2415–2418 re-apply the not_null_tables_cache intersection;
- sql/item_subselect.cc:2537 (Item_in_subselect::update_used_tables), confirming line 2538 delegates and lines 2539–2540 update and OR in left_expr used_tables;
- sql/sql_select.cc:4106 (CreateFramebufferTable), line 4117 has_wf() check and line 4118 nulling of the framebuffer field, and the call site at sql/sql_select.cc:4681–4685 guarded by needs_buffering().

For each SELECT, identify the window-function Item whose argument contains the IN-subquery (first query) or the stored-function call (second query). After fix_fields() and update_used_tables(), record m_accum_properties on that Item and its ancestors; confirm has_wf() is true on the window-function source item and that has_subquery() (first query) or has_stored_program() (second query) is also true after the reset. Confirm the framebuffer table built at CreateFramebufferTable omits the column whose source item has_wf() is true, and that the buffering window path (needs_buffering() true at line 4681) is the one taken. EXPLAIN alone is only a plan clue and does not confirm property recalculation or framebuffer filtering.

Execution status
Authored one-shot demonstration. SQL and branch coverage have not been executed or measured. The mapping from these SQL queries to the exact update_used_tables() call sites and to CreateFramebufferTable depends on planner and window-materialization callers not shown in the supplied excerpts; if instrumentation shows the candidate does not reach those sites, revise the query (e.g., add a second buffering window, change the frame, or wrap the subquery/stored function deeper in the argument tree) before claiming coverage.
````

### 提取后实际执行的完整 SQL

原件：[generated.sql](../prompt_pipeline_deepseek_20261105/item_property_recalculation_248c7f7c227e/generated.sql)

````sql
CREATE TEMPORARY TABLE wf_prop_src (k INT NOT NULL, v INT NOT NULL);
CREATE TEMPORARY TABLE wf_prop_sub (k INT NOT NULL);
INSERT INTO wf_prop_src VALUES (1,10),(1,20),(2,30),(2,40),(3,50);
INSERT INTO wf_prop_sub VALUES (1),(3);

-- Buffering window function (RANGE frame, not the ROWS UNBOUNDED PRECEDING..CURRENT ROW
-- default) whose argument tree contains an IN-subquery. This forces
-- Item_in_optimizer / Item_in_subselect / Item_ref accumulation inside a
-- window function argument, and forces window output materialization through
-- CreateFramebufferTable.
SELECT
  s.k,
  s.v,
  SUM(CASE WHEN s.k IN (SELECT k FROM wf_prop_sub) THEN s.v ELSE 0 END)
    OVER (PARTITION BY s.k ORDER BY s.v RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS win_sum
FROM wf_prop_src AS s
ORDER BY s.k, s.v;

-- Buffering window function whose argument is a stored function call, to
-- exercise Item_func_sp::update_used_tables() re-adding PROP_STORED_PROGRAM
-- after the reset in Item_func::update_used_tables().
DROP FUNCTION IF EXISTS wf_prop_fn;
CREATE FUNCTION wf_prop_fn(x INT) RETURNS INT DETERMINISTIC NO SQL RETURN x * 2;

SELECT
  s.k,
  s.v,
  SUM(wf_prop_fn(s.v))
    OVER (PARTITION BY s.k ORDER BY s.v RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS win_fn_sum
FROM wf_prop_src AS s
ORDER BY s.k, s.v;

DROP FUNCTION wf_prop_fn;
DROP TEMPORARY TABLE wf_prop_sub;
DROP TEMPORARY TABLE wf_prop_src;
````

本批没有独立 expected JSON；预期行在上方 Stage 2 响应。自动汇总主要判断父/目标结果、错误与退出码是否相同，不能等同于首次逐检查点 oracle 审计。

### 执行环境、命令与三轮结果

#### 父提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/result.json)。精确 revision：`15980860ac2639f41dfbda2f7fffb7aeeab32921`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "15980860ac2639f41dfbda2f7fffb7aeeab32921",
  "runtime": "[redacted]",
  "mysqld_sha256": "73597157061e301fc34c01c4fa312f207d9b193c6c2b60dbbb31b354972d3966",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_item_pro_p_1",
      "started_at_epoch": 1793890867.6601236,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890867.8041964
    },
    {
      "repeat": 2,
      "schema": "ds_item_pro_p_2",
      "started_at_epoch": 1793890867.9061997,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890868.0458279
    },
    {
      "repeat": 3,
      "schema": "ds_item_pro_p_3",
      "started_at_epoch": 1793890868.1436493,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890868.281638
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| k | v | win_sum |
| --- | --- | --- |
| 1 | 10 | 30 |
| 1 | 20 | 30 |
| 2 | 30 | 0 |
| 2 | 40 | 0 |
| 3 | 50 | 50 |

结果集 2：

| k | v | win_fn_sum |
| --- | --- | --- |
| 1 | 10 | 60 |
| 1 | 20 | 60 |
| 2 | 30 | 140 |
| 2 | 40 | 140 |
| 3 | 50 | 100 |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/result.json)。精确 revision：`248c7f7c227e76f3422378ca3b9e10d141dcfc86`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "248c7f7c227e76f3422378ca3b9e10d141dcfc86",
  "runtime": "[redacted]",
  "mysqld_sha256": "4e692b40d470773b14ba7adb77e3964e50aa423bb04ed826db39a6b538e86416",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_item_pro_t_1",
      "started_at_epoch": 1793890887.6633997,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890887.8032222
    },
    {
      "repeat": 2,
      "schema": "ds_item_pro_t_2",
      "started_at_epoch": 1793890887.9017756,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890888.0398064
    },
    {
      "repeat": 3,
      "schema": "ds_item_pro_t_3",
      "started_at_epoch": 1793890888.1402035,
      "returncode": 0,
      "stdout_sha256": "0c52d289349fe9904be50b5daa65e097f77b5d9956c8c65b6be1a5f0170cce47",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 2122,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890888.280739
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/item_property_recalculation_248c7f7c227e/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| k | v | win_sum |
| --- | --- | --- |
| 1 | 10 | 30 |
| 1 | 20 | 30 |
| 2 | 30 | 0 |
| 2 | 40 | 0 |
| 3 | 50 | 50 |

结果集 2：

| k | v | win_fn_sum |
| --- | --- | --- |
| 1 | 10 | 60 |
| 1 | 20 | 60 |
| 2 | 30 | 140 |
| 2 | 40 | 140 |
| 3 | 50 | 100 |

判定与环境补充：[逐轮配对与二进制身份](../prompt_pipeline_deepseek_20261105/server_evidence/summary.json)、[参数及 run_id](../prompt_pipeline_deepseek_20261105/run_manifest.json)、[执行报告](../prompt_pipeline_deepseek_20261105/verification_report.md)。原始远端 runner 未公开，公开包不能还原其完整启动命令；其 SHA256 见导出清单。

