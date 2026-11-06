# 窗口帧状态：两批实验完整读本

[返回总览](README.md)

首次从 lower_limit=current_row+1 推导前向缩小帧，要求 1 FOLLOWING..UNBOUNDED FOLLOWING、DECIMAL/DOUBLE、高精度开关及其他帧对照；DeepSeek Stage 1 选择 1 PRECEDING..CURRENT ROW，Stage 2 沿用整数列和后向两行帧。

首次：父提交每轮 9/9、目标 4/9；5 个检查点错误。DeepSeek：两侧每轮均为相同的 8 行结果。

整理新增勘误：DeepSeek Stage 1 将 (1,NULL,3) 的第三行后向两行帧 AVG 写成 3/2=1.5；实际帧为 (NULL,3)，非 NULL 计数为 1，正确值为 3。Stage 2 已写成 3.0000，父/目标 XML 也均为 3.0000。此处保留两阶段原文，不静默修正历史回答。

## 0. 共同源码与 Stage 1 正式输入

两批以下文件逐字节一致。源码节选已含精确提交、父提交、源文件、行号、blob、Target observation 与局部范围说明。

DeepSeek 对应副本：[源码](../prompt_pipeline_deepseek_20261105/input_bundle/source-code-data/mysql/window_frame_state_c296cddb93ff.txt)、[Stage 1 提示词](../prompt_pipeline_deepseek_20261105/input_bundle/Prompts/mysql/src2req/window_frame_state_c296cddb93ff.txt)。

### 目标源码片段与上下文

原件：[window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/input_bundle/source-code-data/mysql/window_frame_state_c296cddb93ff.txt)

````text
Target: window_frame_state_c296cddb93ff
Target observation: Buffered window-frame row-position state during optimized ROWS-frame evaluation and its consumption by AVG
Revision: c296cddb93ffc631f9b43d3b1ff769604e7469d7
Parent revision: 74c7ccfa27f482576412300e5f92fd3dbeb54cfa
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/window.h
Blob: 6e596de81b2696471b703f0c63ea034b060ed558
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/window.h
```cpp
477:   /**
478:     Execution state: The number of the row being visited for its contribution
479:     to a window function, relative to the start of the partition. Note that
480:     this will often be different from the current row for which we are
481:     processing the window function, reading it for output. That is given by
482:     m_rowno_in_partition, q.v.
483:   */
484:   int64 m_rowno_being_visited;
485: 
486:   /**
487:     Execution state: the row number of the current row within a frame, cf.
488:     m_is_last_row_in_frame, relative to start of the frame. 1-based.
489:   */
490:   int64 m_rowno_in_frame;
```
```cpp
1299:   /**
1300:     See #m_rowno_in_frame
1301:   */
1302:   int64 rowno_in_frame() const { return m_rowno_in_frame; }
1303: 
1304:   /**
1305:     See #m_rowno_in_frame
1306:   */
1307:   Window &set_rowno_in_frame(int64 rowno) {
1308:     m_rowno_in_frame = rowno;
1309:     return *this;
1310:   }
1311: 
```

# Code: sql/item_sum.cc
Blob: d90a92a5a47d9ac79d556d9aa52858c3c744eb77
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc
```cpp
410: bool Item_sum::check_wf_semantics1(THD *, Query_block *,
411:                                    Window_evaluation_requirements *r) {
412:   const PT_frame *frame = m_window->frame();
413: 
414:   /*
415:     If we have ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, we can just
416:     accumulate as we see rows, never need to invert old rows or to look at
417:     future rows, so don't need a frame buffer.
418:   */
419:   r->needs_buffer = !(frame->m_query_expression == WFU_ROWS &&
420:                       frame->m_from->m_border_type == WBT_UNBOUNDED_PRECEDING &&
421:                       frame->m_to->m_border_type == WBT_CURRENT_ROW);
422: 
423:   if (with_distinct) {
424:     my_error(ER_NOT_SUPPORTED_YET, MYF(0), "<window function>(DISTINCT ..)");
425:     return true;
426:   }
```
```cpp
1913: bool Item_sum_sum::check_wf_semantics1(THD *thd, Query_block *select,
1914:                                        Window_evaluation_requirements *r) {
1915:   bool result = Item_sum::check_wf_semantics1(thd, select, r);
1916:   if (hybrid_type == REAL_RESULT) {
1917:     /*
1918:       If the frame's start moves we will consider inversion, to remove the
1919:       start rows. But, as we're using REAL_RESULT, and floating point
1920:       arithmetic isn't mathematically exact, inversion may give different
1921:       results from that of the non-optimized path. So, we use it only if the
1922:       user allowed it:
1923:     */
1924:     const PT_frame *f = m_window->frame();
1925:     if (f->m_from->m_border_type == WBT_VALUE_PRECEDING ||
1926:         f->m_from->m_border_type == WBT_VALUE_FOLLOWING ||
1927:         f->m_from->m_border_type == WBT_CURRENT_ROW) {
1928:       r->row_optimizable &= !thd->variables.windowing_use_high_precision;
1929:       r->range_optimizable &= !thd->variables.windowing_use_high_precision;
1930:     }
1931:   }
1932:   return result;
1933: }
```
```cpp
2279: double Item_sum_avg::val_real() {
2280:   assert(fixed == 1);
2281:   if (m_is_window_function) {
2282:     if (wf_common_init()) return 0.0;
2283: 
2284:     double sum = Item_sum_sum::val_real();
2285: 
2286:     if (m_window->is_last_row_in_frame()) {
2287:       int64 divisor = (m_window->needs_buffering()
2288:                            ? m_window->rowno_in_frame() - m_frame_null_count
2289:                            : m_count - m_frame_null_count);
2290:       if (divisor > 0) sum = sum / ulonglong2double(divisor);
2291:     }
2292:     m_avg = sum;  // save
2293:     return sum;
2294:   } else {
2295:     if (aggr) aggr->endup();
2296:     if (!m_count) {
2297:       null_value = true;
2298:       return 0.0;
2299:     }
2300:     return Item_sum_sum::val_real() / ulonglong2double(m_count);
2301:   }
2302: }
2303: 
2304: my_decimal *Item_sum_avg::val_decimal(my_decimal *val) {
2305:   DBUG_TRACE;
2306:   my_decimal sum_buff, cnt;
2307:   const my_decimal *sum_dec;
2308:   assert(fixed == 1);
2309: 
2310:   if (m_is_window_function) {
2311:     if (hybrid_type != DECIMAL_RESULT) {
2312:       my_decimal *result = val_decimal_from_real(val);
2313:       return result;
2314:     }
2315: 
2316:     if (wf_common_init()) {
2317:       return error_decimal(val);
2318:     }
2319: 
2320:     /*
2321:       dec_buff[0]:   the current value
2322:       dec_buff[1]:   holds sum so far
2323:     */
2324:     my_decimal *argd = args[0]->val_decimal(&dec_buffs[0]);
2325: 
2326:     if (!args[0]->null_value) {
2327:       my_decimal tmp;
2328:       if (m_window->do_inverse()) {
2329:         assert(m_count > 0 && m_count > m_frame_null_count);
2330:         my_decimal_sub(E_DEC_FATAL_ERROR, &tmp, &dec_buffs[1], argd);
2331:         tmp.swap(dec_buffs[1]);
2332:         m_count--;
2333:       } else {
2334:         my_decimal_add(E_DEC_FATAL_ERROR, &tmp, &dec_buffs[1], argd);
2335:         tmp.swap(dec_buffs[1]);
2336:         m_count++;
2337:       }
2338:     } else {
2339:       if (m_window->do_inverse()) {
2340:         assert(m_count >= m_frame_null_count && m_frame_null_count > 0);
2341:         m_frame_null_count--;
2342:         m_count--;
2343:         // else no need to inverse if we only saw nulls
2344:       } else {
2345:         m_frame_null_count++;
2346:         m_count++;
2347:       }
2348:     }
2349: 
2350:     int64 divisor = (m_window->needs_buffering()
2351:                          ? m_window->rowno_in_frame() - m_frame_null_count
2352:                          : m_count - m_frame_null_count);
2353: 
2354:     if (m_window->is_last_row_in_frame() && divisor > 0) {
2355:       int2my_decimal(E_DEC_FATAL_ERROR, divisor, false, &cnt);
2356:       my_decimal_div(E_DEC_FATAL_ERROR, &dec_buffs[0], &dec_buffs[1], &cnt,
2357:                      prec_increment);
2358:       val->swap(dec_buffs[0]);
2359:     } else
2360:       my_decimal2decimal(&dec_buffs[1], val);
2361: 
2362:     null_value = (m_count == m_frame_null_count);
2363:     my_decimal tmp(*val);
2364:     m_avg_dec.swap(tmp);  // save result
2365:     return val;
```

# Code: sql/iterators/window_iterators.cc
Blob: 51280850597891900190341a47516b6752377243
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/iterators/window_iterators.cc
```cpp
683:   /**
684:     If true, use code path for static aggregates
685:   */
686:   const bool static_aggregate = w.static_aggregates();
687: 
688:   /**
689:     If true, use code path for ROW bounds with optimized strategy
690:   */
691:   const bool row_optimizable = w.optimizable_row_aggregates();
692: 
693:   /**
694:     If true, use code path for RANGE bounds with optimized strategy
695:   */
696:   const bool range_optimizable = w.optimizable_range_aggregates();
697: 
698:   // These three strategies are mutually exclusive:
699:   assert((static_aggregate + row_optimizable + range_optimizable) <= 1);
```
```cpp
789:     switch (f->m_from->m_border_type) {
790:       case WBT_CURRENT_ROW:
791:         lower_limit = current_row;
792:         break;
793:       case WBT_VALUE_PRECEDING:
794:         /*
795:           Example: 1 PRECEDING and current row== 2 => 1
796:                                    current row== 1 => 1
797:                                    current row== 3 => 2
798:         */
799:         lower_limit = std::max<int64>(current_row - border, 1);
800:         break;
801:       case WBT_VALUE_FOLLOWING:
802:         /*
803:           Example: 1 FOLLOWING and current row== 2 => 3
804:                                    current row== 1 => 2
805:                                    current row== 3 => 4
806:         */
807:         if (border <= (std::numeric_limits<int64>::max() - current_row))
808:           lower_limit = current_row + border;
809:         else {
810:           lower_within_limits = false;
811:           lower_limit = INT64_MAX;
812:         }
813:         break;
814:       case WBT_UNBOUNDED_PRECEDING:
815:         lower_limit = 1;
816:         break;
817:       case WBT_UNBOUNDED_FOLLOWING:
818:         assert(false);
819:         break;
820:     }
```
```cpp
1084:   if (static_aggregate && current_row != 1) {
1085:     /* Set up the correct non-wf fields for copying to the output row */
1086:     if (bring_back_frame_row(thd, &w, current_row,
1087:                              Window_retrieve_cached_row_reason::CURRENT))
1088:       return true;
1089: 
1090:     /* E.g. ROW_NUMBER, RANK, DENSE_RANK */
1091:     if (copy_funcs(param, thd, CFT_WF_NON_FRAMING)) return true;
1092:   } else if (row_optimizable && w.aggregates_primed()) {
1093:     /*
1094:       Rows 2..N in partition: we still have state from previous current row's
1095:       frame computation, now adjust by subtracting row 1 in frame (lower_limit)
1096:       and adding new, if any, final frame row
1097:     */
1098:     const bool remove_previous_first_row =
1099:         (lower_limit > 1 && lower_limit - 1 <= last_rowno_in_cache);
1100:     const bool new_last_row =
1101:         (upper_limit <= upper &&
1102:          !unbounded_following /* all added when primed */);
1103:     const int64 rows_in_frame = upper - lower_limit + 1;
1104:     w.set_first_rowno_in_rows_frame(lower_limit);
1105: 
1106:     /* possibly subtract: early in partition there may not be any */
1107:     if (remove_previous_first_row) {
```
```cpp
1145:       if (bring_back_frame_row(
1146:               thd, &w, lower_limit - 1,
1147:               Window_retrieve_cached_row_reason::FIRST_IN_FRAME))
1148:         return true;
1149: 
1150:       w.set_inverse(true);
1151:       if (!new_last_row) {
1152:         w.set_rowno_in_frame(current_row - lower_limit + 1);
1153:         if (rows_in_frame > 0)
1154:           w.set_is_last_row_in_frame(true);  // do final comp., e.g. div in AVG
1155: 
1156:         if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1157: 
1158:         w.set_is_last_row_in_frame(false);  // undo temporary states
1159:       } else {
1160:         if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1161:       }
1162: 
1163:       w.set_is_last_row_in_peerset_within_frame(false);
1164:       w.set_inverse(false);
1165:     }
1166: 
1167:     if (have_first_value && (lower_limit <= last_rowno_in_cache)) {
1168:       // We have seen first row of frame, FIRST_VALUE can be computed:
1169:       if (bring_back_frame_row(
1170:               thd, &w, lower_limit,
1171:               Window_retrieve_cached_row_reason::FIRST_IN_FRAME))
1172:         return true;
1173: 
1174:       w.set_rowno_in_frame(1);
1175: 
1176:       /*
1177:         Framing WFs which accumulate (SUM, COUNT, AVG) shouldn't accumulate
1178:         this row again as they have done so already. Evaluate only
1179:         X_VALUE/MIN/MAX.
1180:       */
1181:       if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1182:     }
1183: 
1184:     if (have_last_value && !new_last_row) {
1185:       // We have seen last row of frame, LAST_VALUE can be computed:
1186:       if (bring_back_frame_row(
1187:               thd, &w, upper, Window_retrieve_cached_row_reason::LAST_IN_FRAME))
1188:         return true;
1189: 
1190:       w.set_rowno_in_frame(current_row - lower_limit + 1);
1191:       if (rows_in_frame > 0) w.set_is_last_row_in_frame(true);
1192: 
1193:       if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1194: 
1195:       w.set_is_last_row_in_frame(false);
1196:     }
1197: 
1198:     if (!have_nth_value.m_offsets.empty()) {
1199:       int fno = 0;
1200:       for (Window::st_offset nth : have_nth_value.m_offsets) {
1201:         if (lower_limit + nth.m_rowno - 1 <= upper) {
1202:           if (bring_back_frame_row(
1203:                   thd, &w, lower_limit + nth.m_rowno - 1,
1204:                   Window_retrieve_cached_row_reason::MISC_POSITIONS, fno++))
1205:             return true;
1206: 
1207:           w.set_rowno_in_frame(nth.m_rowno);
1208: 
1209:           if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1210:         }
1211:       }
1212:     }
1213: 
1214:     if (new_last_row)  // Add new last row to framing WF's value
1215:     {
1216:       if (bring_back_frame_row(
1217:               thd, &w, upper, Window_retrieve_cached_row_reason::LAST_IN_FRAME))
1218:         return true;
1219: 
1220:       w.set_rowno_in_frame(upper - lower_limit + 1)
1221:           .set_is_last_row_in_frame(true);  // temporary states for next copy
1222: 
1223:       if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1224: 
1225:       w.set_is_last_row_in_frame(false);  // undo temporary states
1226:     }
```
````

### 共同的完整 Stage 1 提示词（含示例及当前源码）

原件：[window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/src2req/window_frame_state_c296cddb93ff.txt)

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
Target: window_frame_state_c296cddb93ff
Target observation: Buffered window-frame row-position state during optimized ROWS-frame evaluation and its consumption by AVG
Revision: c296cddb93ffc631f9b43d3b1ff769604e7469d7
Parent revision: 74c7ccfa27f482576412300e5f92fd3dbeb54cfa
Source repository: https://github.com/mysql/mysql-server
Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.
Line numbers below refer to the upstream file at this revision.

# Code: sql/window.h
Blob: 6e596de81b2696471b703f0c63ea034b060ed558
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/window.h
```cpp
477:   /**
478:     Execution state: The number of the row being visited for its contribution
479:     to a window function, relative to the start of the partition. Note that
480:     this will often be different from the current row for which we are
481:     processing the window function, reading it for output. That is given by
482:     m_rowno_in_partition, q.v.
483:   */
484:   int64 m_rowno_being_visited;
485: 
486:   /**
487:     Execution state: the row number of the current row within a frame, cf.
488:     m_is_last_row_in_frame, relative to start of the frame. 1-based.
489:   */
490:   int64 m_rowno_in_frame;
```
```cpp
1299:   /**
1300:     See #m_rowno_in_frame
1301:   */
1302:   int64 rowno_in_frame() const { return m_rowno_in_frame; }
1303: 
1304:   /**
1305:     See #m_rowno_in_frame
1306:   */
1307:   Window &set_rowno_in_frame(int64 rowno) {
1308:     m_rowno_in_frame = rowno;
1309:     return *this;
1310:   }
1311: 
```

# Code: sql/item_sum.cc
Blob: d90a92a5a47d9ac79d556d9aa52858c3c744eb77
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/item_sum.cc
```cpp
410: bool Item_sum::check_wf_semantics1(THD *, Query_block *,
411:                                    Window_evaluation_requirements *r) {
412:   const PT_frame *frame = m_window->frame();
413: 
414:   /*
415:     If we have ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, we can just
416:     accumulate as we see rows, never need to invert old rows or to look at
417:     future rows, so don't need a frame buffer.
418:   */
419:   r->needs_buffer = !(frame->m_query_expression == WFU_ROWS &&
420:                       frame->m_from->m_border_type == WBT_UNBOUNDED_PRECEDING &&
421:                       frame->m_to->m_border_type == WBT_CURRENT_ROW);
422: 
423:   if (with_distinct) {
424:     my_error(ER_NOT_SUPPORTED_YET, MYF(0), "<window function>(DISTINCT ..)");
425:     return true;
426:   }
```
```cpp
1913: bool Item_sum_sum::check_wf_semantics1(THD *thd, Query_block *select,
1914:                                        Window_evaluation_requirements *r) {
1915:   bool result = Item_sum::check_wf_semantics1(thd, select, r);
1916:   if (hybrid_type == REAL_RESULT) {
1917:     /*
1918:       If the frame's start moves we will consider inversion, to remove the
1919:       start rows. But, as we're using REAL_RESULT, and floating point
1920:       arithmetic isn't mathematically exact, inversion may give different
1921:       results from that of the non-optimized path. So, we use it only if the
1922:       user allowed it:
1923:     */
1924:     const PT_frame *f = m_window->frame();
1925:     if (f->m_from->m_border_type == WBT_VALUE_PRECEDING ||
1926:         f->m_from->m_border_type == WBT_VALUE_FOLLOWING ||
1927:         f->m_from->m_border_type == WBT_CURRENT_ROW) {
1928:       r->row_optimizable &= !thd->variables.windowing_use_high_precision;
1929:       r->range_optimizable &= !thd->variables.windowing_use_high_precision;
1930:     }
1931:   }
1932:   return result;
1933: }
```
```cpp
2279: double Item_sum_avg::val_real() {
2280:   assert(fixed == 1);
2281:   if (m_is_window_function) {
2282:     if (wf_common_init()) return 0.0;
2283: 
2284:     double sum = Item_sum_sum::val_real();
2285: 
2286:     if (m_window->is_last_row_in_frame()) {
2287:       int64 divisor = (m_window->needs_buffering()
2288:                            ? m_window->rowno_in_frame() - m_frame_null_count
2289:                            : m_count - m_frame_null_count);
2290:       if (divisor > 0) sum = sum / ulonglong2double(divisor);
2291:     }
2292:     m_avg = sum;  // save
2293:     return sum;
2294:   } else {
2295:     if (aggr) aggr->endup();
2296:     if (!m_count) {
2297:       null_value = true;
2298:       return 0.0;
2299:     }
2300:     return Item_sum_sum::val_real() / ulonglong2double(m_count);
2301:   }
2302: }
2303: 
2304: my_decimal *Item_sum_avg::val_decimal(my_decimal *val) {
2305:   DBUG_TRACE;
2306:   my_decimal sum_buff, cnt;
2307:   const my_decimal *sum_dec;
2308:   assert(fixed == 1);
2309: 
2310:   if (m_is_window_function) {
2311:     if (hybrid_type != DECIMAL_RESULT) {
2312:       my_decimal *result = val_decimal_from_real(val);
2313:       return result;
2314:     }
2315: 
2316:     if (wf_common_init()) {
2317:       return error_decimal(val);
2318:     }
2319: 
2320:     /*
2321:       dec_buff[0]:   the current value
2322:       dec_buff[1]:   holds sum so far
2323:     */
2324:     my_decimal *argd = args[0]->val_decimal(&dec_buffs[0]);
2325: 
2326:     if (!args[0]->null_value) {
2327:       my_decimal tmp;
2328:       if (m_window->do_inverse()) {
2329:         assert(m_count > 0 && m_count > m_frame_null_count);
2330:         my_decimal_sub(E_DEC_FATAL_ERROR, &tmp, &dec_buffs[1], argd);
2331:         tmp.swap(dec_buffs[1]);
2332:         m_count--;
2333:       } else {
2334:         my_decimal_add(E_DEC_FATAL_ERROR, &tmp, &dec_buffs[1], argd);
2335:         tmp.swap(dec_buffs[1]);
2336:         m_count++;
2337:       }
2338:     } else {
2339:       if (m_window->do_inverse()) {
2340:         assert(m_count >= m_frame_null_count && m_frame_null_count > 0);
2341:         m_frame_null_count--;
2342:         m_count--;
2343:         // else no need to inverse if we only saw nulls
2344:       } else {
2345:         m_frame_null_count++;
2346:         m_count++;
2347:       }
2348:     }
2349: 
2350:     int64 divisor = (m_window->needs_buffering()
2351:                          ? m_window->rowno_in_frame() - m_frame_null_count
2352:                          : m_count - m_frame_null_count);
2353: 
2354:     if (m_window->is_last_row_in_frame() && divisor > 0) {
2355:       int2my_decimal(E_DEC_FATAL_ERROR, divisor, false, &cnt);
2356:       my_decimal_div(E_DEC_FATAL_ERROR, &dec_buffs[0], &dec_buffs[1], &cnt,
2357:                      prec_increment);
2358:       val->swap(dec_buffs[0]);
2359:     } else
2360:       my_decimal2decimal(&dec_buffs[1], val);
2361: 
2362:     null_value = (m_count == m_frame_null_count);
2363:     my_decimal tmp(*val);
2364:     m_avg_dec.swap(tmp);  // save result
2365:     return val;
```

# Code: sql/iterators/window_iterators.cc
Blob: 51280850597891900190341a47516b6752377243
Source: https://github.com/mysql/mysql-server/blob/c296cddb93ffc631f9b43d3b1ff769604e7469d7/sql/iterators/window_iterators.cc
```cpp
683:   /**
684:     If true, use code path for static aggregates
685:   */
686:   const bool static_aggregate = w.static_aggregates();
687: 
688:   /**
689:     If true, use code path for ROW bounds with optimized strategy
690:   */
691:   const bool row_optimizable = w.optimizable_row_aggregates();
692: 
693:   /**
694:     If true, use code path for RANGE bounds with optimized strategy
695:   */
696:   const bool range_optimizable = w.optimizable_range_aggregates();
697: 
698:   // These three strategies are mutually exclusive:
699:   assert((static_aggregate + row_optimizable + range_optimizable) <= 1);
```
```cpp
789:     switch (f->m_from->m_border_type) {
790:       case WBT_CURRENT_ROW:
791:         lower_limit = current_row;
792:         break;
793:       case WBT_VALUE_PRECEDING:
794:         /*
795:           Example: 1 PRECEDING and current row== 2 => 1
796:                                    current row== 1 => 1
797:                                    current row== 3 => 2
798:         */
799:         lower_limit = std::max<int64>(current_row - border, 1);
800:         break;
801:       case WBT_VALUE_FOLLOWING:
802:         /*
803:           Example: 1 FOLLOWING and current row== 2 => 3
804:                                    current row== 1 => 2
805:                                    current row== 3 => 4
806:         */
807:         if (border <= (std::numeric_limits<int64>::max() - current_row))
808:           lower_limit = current_row + border;
809:         else {
810:           lower_within_limits = false;
811:           lower_limit = INT64_MAX;
812:         }
813:         break;
814:       case WBT_UNBOUNDED_PRECEDING:
815:         lower_limit = 1;
816:         break;
817:       case WBT_UNBOUNDED_FOLLOWING:
818:         assert(false);
819:         break;
820:     }
```
```cpp
1084:   if (static_aggregate && current_row != 1) {
1085:     /* Set up the correct non-wf fields for copying to the output row */
1086:     if (bring_back_frame_row(thd, &w, current_row,
1087:                              Window_retrieve_cached_row_reason::CURRENT))
1088:       return true;
1089: 
1090:     /* E.g. ROW_NUMBER, RANK, DENSE_RANK */
1091:     if (copy_funcs(param, thd, CFT_WF_NON_FRAMING)) return true;
1092:   } else if (row_optimizable && w.aggregates_primed()) {
1093:     /*
1094:       Rows 2..N in partition: we still have state from previous current row's
1095:       frame computation, now adjust by subtracting row 1 in frame (lower_limit)
1096:       and adding new, if any, final frame row
1097:     */
1098:     const bool remove_previous_first_row =
1099:         (lower_limit > 1 && lower_limit - 1 <= last_rowno_in_cache);
1100:     const bool new_last_row =
1101:         (upper_limit <= upper &&
1102:          !unbounded_following /* all added when primed */);
1103:     const int64 rows_in_frame = upper - lower_limit + 1;
1104:     w.set_first_rowno_in_rows_frame(lower_limit);
1105: 
1106:     /* possibly subtract: early in partition there may not be any */
1107:     if (remove_previous_first_row) {
```
```cpp
1145:       if (bring_back_frame_row(
1146:               thd, &w, lower_limit - 1,
1147:               Window_retrieve_cached_row_reason::FIRST_IN_FRAME))
1148:         return true;
1149: 
1150:       w.set_inverse(true);
1151:       if (!new_last_row) {
1152:         w.set_rowno_in_frame(current_row - lower_limit + 1);
1153:         if (rows_in_frame > 0)
1154:           w.set_is_last_row_in_frame(true);  // do final comp., e.g. div in AVG
1155: 
1156:         if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1157: 
1158:         w.set_is_last_row_in_frame(false);  // undo temporary states
1159:       } else {
1160:         if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1161:       }
1162: 
1163:       w.set_is_last_row_in_peerset_within_frame(false);
1164:       w.set_inverse(false);
1165:     }
1166: 
1167:     if (have_first_value && (lower_limit <= last_rowno_in_cache)) {
1168:       // We have seen first row of frame, FIRST_VALUE can be computed:
1169:       if (bring_back_frame_row(
1170:               thd, &w, lower_limit,
1171:               Window_retrieve_cached_row_reason::FIRST_IN_FRAME))
1172:         return true;
1173: 
1174:       w.set_rowno_in_frame(1);
1175: 
1176:       /*
1177:         Framing WFs which accumulate (SUM, COUNT, AVG) shouldn't accumulate
1178:         this row again as they have done so already. Evaluate only
1179:         X_VALUE/MIN/MAX.
1180:       */
1181:       if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1182:     }
1183: 
1184:     if (have_last_value && !new_last_row) {
1185:       // We have seen last row of frame, LAST_VALUE can be computed:
1186:       if (bring_back_frame_row(
1187:               thd, &w, upper, Window_retrieve_cached_row_reason::LAST_IN_FRAME))
1188:         return true;
1189: 
1190:       w.set_rowno_in_frame(current_row - lower_limit + 1);
1191:       if (rows_in_frame > 0) w.set_is_last_row_in_frame(true);
1192: 
1193:       if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1194: 
1195:       w.set_is_last_row_in_frame(false);
1196:     }
1197: 
1198:     if (!have_nth_value.m_offsets.empty()) {
1199:       int fno = 0;
1200:       for (Window::st_offset nth : have_nth_value.m_offsets) {
1201:         if (lower_limit + nth.m_rowno - 1 <= upper) {
1202:           if (bring_back_frame_row(
1203:                   thd, &w, lower_limit + nth.m_rowno - 1,
1204:                   Window_retrieve_cached_row_reason::MISC_POSITIONS, fno++))
1205:             return true;
1206: 
1207:           w.set_rowno_in_frame(nth.m_rowno);
1208: 
1209:           if (copy_funcs(param, thd, CFT_WF_USES_ONLY_ONE_ROW)) return true;
1210:         }
1211:       }
1212:     }
1213: 
1214:     if (new_last_row)  // Add new last row to framing WF's value
1215:     {
1216:       if (bring_back_frame_row(
1217:               thd, &w, upper, Window_retrieve_cached_row_reason::LAST_IN_FRAME))
1218:         return true;
1219: 
1220:       w.set_rowno_in_frame(upper - lower_limit + 1)
1221:           .set_is_last_row_in_frame(true);  // temporary states for next copy
1222: 
1223:       if (copy_funcs(param, thd, CFT_WF_FRAMING)) return true;
1224: 
1225:       w.set_is_last_row_in_frame(false);  // undo temporary states
1226:     }
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
- [Requirements/mysql/req/window_frame_state_c296cddb93ff/window_frame_state_c296cddb93ff_1.txt](../prompt_pipeline_20261104/generation/input_bundle/Requirements/mysql/req/window_frame_state_c296cddb93ff/window_frame_state_c296cddb93ff_1.txt)
- [Prompts/mysql/req2test/window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/input_bundle/Prompts/mysql/req2test/window_frame_state_c296cddb93ff.txt)

## 1. 首次 Codex

上下文：同一助手共享对话，无独立 API 信封；[生成清单](../prompt_pipeline_20261104/generation/generation_manifest.json)，[上下文审查](../prompt_pipeline_20261104/contamination_review.md)。生成清单中的未执行状态为历史快照，后续执行见本节运行证据。

### Stage 1 输出：测试偏好与需求原文

原件：[window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/stage1_src2req/window_frame_state_c296cddb93ff.txt)

````text
Target
Revision c296cddb93ffc631f9b43d3b1ff769604e7469d7; parent 74c7ccfa27f482576412300e5f92fd3dbeb54cfa. Observe optimized ROWS-frame state assignments and the buffered AVG denominator that consumes rowno_in_frame. This revision uses rowno_in_frame for buffered averages; do not substitute the later m_count-only implementation from another prompt's example target.

Source-required conditions
The analysis stage extracted these constraints from the source in this prompt:
1. AVG must be a window function, not an ordinary grouped aggregate, and reach its final-row calculation after initialization. The buffered REAL denominator is rowno_in_frame()-m_frame_null_count (sql/item_sum.cc:2279-2293); DECIMAL uses the same buffered expression at 2350-2357. Positive divisor and is_last_row_in_frame gate division.
2. ROWS UNBOUNDED PRECEDING through CURRENT ROW is explicitly a nonbuffered case (sql/item_sum.cc:410-421). Use other ROWS frames for the buffered target and reserve that frame as a control.
3. The optimized-row strategy requires row_optimizable and aggregates_primed (sql/iterators/window_iterators.cc:683-699,1092). Moving-frame REAL aggregation additionally requires windowing_use_high_precision=false to permit inversion; the excerpt does not impose that gate on DECIMAL (sql/item_sum.cc:1913-1931).
4. The subtraction branch requires remove_previous_first_row: lower_limit>1 and lower_limit-1<=last_rowno_in_cache (window_iterators.cc:1098-1107). With no new last row, it sets inverse=true, sets rowno_in_frame to current_row-lower_limit+1, temporarily marks a nonempty frame's final row, and calls the framing functions (1145-1164).
5. A lower border of 1 FOLLOWING gives lower_limit=current_row+1 (789-812). Thus the displayed assignment can produce rowno_in_frame=0 even when a remaining forward frame is nonempty. This is an algebraic observation about a conditional branch; all runtime guards still need confirmation. With an unbounded-following upper border, new_last_row is false according to 1100-1102.
6. FIRST_VALUE, LAST_VALUE and NTH_VALUE have additional setters/copy calls (1167-1209). A bounded moving frame can use the add-new-last-row setter upper-lower_limit+1 (1214-1225). Their reachability should be observed separately.

Candidate construction
Use a small temporary table with (g,id,v_dec,v_real), a unique (g,id) key, DECIMAL and DOUBLE columns holding identical small exactly representable input values. Include a normal partition [10,20,30,40], a mixed-NULL partition [NULL,20,NULL,60], an all-NULL partition [NULL,NULL], and a single-row partition [7]. Order every window by id and the result by g,id.
Primary frame: ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING. It combines a moving lower bound, a fixed upper end, shrinking positive frames and an empty final frame. Run DECIMAL AVG independently, then DOUBLE AVG with windowing_use_high_precision OFF and ON. Save and restore this session variable. OFF is the intended REAL inversion candidate; ON is a numerical/strategy control, not a known-correct oracle.
Secondary frames: ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING, and ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING. Run both numeric types with high precision OFF; they exercise a different lower position and bounded add/remove opportunities. Add a nonbuffered cumulative AVG control. Add a separate forward-frame query combining DECIMAL AVG, FIRST_VALUE, LAST_VALUE and NTH_VALUE(v_dec,2) over one named window to explore the extra state setters. Keep it separate from the primary AVG-only query so added functions do not define primary coverage.

Correctness oracle
For each output row, enumerate the frame's rows in its partition and average only non-NULL values. Empty frames and all-NULL frames return NULL. In [10,20,30,40], the forward-to-end means are [30,35,40,NULL]; current-to-end means are [25,30,35,40]; one-preceding/one-following means are [15,20,30,35]. In [NULL,20,NULL,60], forward-to-end means are [40,60,60,NULL]. Include remaining frames/partitions by the same enumeration, not by asking another window AVG query for the answer.
Choose an explicit six-decimal output cast for stable presentation. Quantize mathematical rational means to six decimals for DECIMAL comparison; permit at most 0.000001 absolute difference in the cast DOUBLE output. NULL must match exactly. FIRST_VALUE/LAST_VALUE use actual first/last frame rows, including NULLs; NTH_VALUE uses the second frame row and returns NULL if absent. These functions do not skip NULLs in this test. A positive-row-count all-NULL frame differs from an empty frame even though both AVG results are NULL.

Coverage observation
Record the window identity, partition/output-row identity, row_optimizable, aggregates_primed, needs_buffering, lower_limit, upper, last_rowno_in_cache, remove_previous_first_row, new_last_row, rows_in_frame and inverse state. At window_iterators.cc:1152 and 1190 capture the assigned rowno_in_frame, and correlate with the AVG call's m_count, m_frame_null_count, divisor and is_last_row_in_frame. Record whether division occurred or was skipped. Trace 1174,1207,1220 separately for auxiliary value functions and bounded frames. An empty final row alone is not evidence that the positive-divisor branch was tested.

Uncertainty
The snippets omit initial priming, all frame-limit calculations, executor scheduling and some null-result handling. The SQL shapes are candidates for the guarded branches; source algebra is not a runtime reproduction. High-precision ON/OFF equality cannot replace the independent frame oracle. Later release builds may already contain subsequent fixes; bind attribution to the given target and parent commits. This is this assistant's src2req output; SQL execution and measured source coverage have not occurred.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/stage2_req2test/prompts/window_frame_state_c296cddb93ff.txt)

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
Revision c296cddb93ffc631f9b43d3b1ff769604e7469d7; parent 74c7ccfa27f482576412300e5f92fd3dbeb54cfa. Observe optimized ROWS-frame state assignments and the buffered AVG denominator that consumes rowno_in_frame. This revision uses rowno_in_frame for buffered averages; do not substitute the later m_count-only implementation from another prompt's example target.

Source-required conditions
The analysis stage extracted these constraints from the source in this prompt:
1. AVG must be a window function, not an ordinary grouped aggregate, and reach its final-row calculation after initialization. The buffered REAL denominator is rowno_in_frame()-m_frame_null_count (sql/item_sum.cc:2279-2293); DECIMAL uses the same buffered expression at 2350-2357. Positive divisor and is_last_row_in_frame gate division.
2. ROWS UNBOUNDED PRECEDING through CURRENT ROW is explicitly a nonbuffered case (sql/item_sum.cc:410-421). Use other ROWS frames for the buffered target and reserve that frame as a control.
3. The optimized-row strategy requires row_optimizable and aggregates_primed (sql/iterators/window_iterators.cc:683-699,1092). Moving-frame REAL aggregation additionally requires windowing_use_high_precision=false to permit inversion; the excerpt does not impose that gate on DECIMAL (sql/item_sum.cc:1913-1931).
4. The subtraction branch requires remove_previous_first_row: lower_limit>1 and lower_limit-1<=last_rowno_in_cache (window_iterators.cc:1098-1107). With no new last row, it sets inverse=true, sets rowno_in_frame to current_row-lower_limit+1, temporarily marks a nonempty frame's final row, and calls the framing functions (1145-1164).
5. A lower border of 1 FOLLOWING gives lower_limit=current_row+1 (789-812). Thus the displayed assignment can produce rowno_in_frame=0 even when a remaining forward frame is nonempty. This is an algebraic observation about a conditional branch; all runtime guards still need confirmation. With an unbounded-following upper border, new_last_row is false according to 1100-1102.
6. FIRST_VALUE, LAST_VALUE and NTH_VALUE have additional setters/copy calls (1167-1209). A bounded moving frame can use the add-new-last-row setter upper-lower_limit+1 (1214-1225). Their reachability should be observed separately.

Candidate construction
Use a small temporary table with (g,id,v_dec,v_real), a unique (g,id) key, DECIMAL and DOUBLE columns holding identical small exactly representable input values. Include a normal partition [10,20,30,40], a mixed-NULL partition [NULL,20,NULL,60], an all-NULL partition [NULL,NULL], and a single-row partition [7]. Order every window by id and the result by g,id.
Primary frame: ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING. It combines a moving lower bound, a fixed upper end, shrinking positive frames and an empty final frame. Run DECIMAL AVG independently, then DOUBLE AVG with windowing_use_high_precision OFF and ON. Save and restore this session variable. OFF is the intended REAL inversion candidate; ON is a numerical/strategy control, not a known-correct oracle.
Secondary frames: ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING, and ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING. Run both numeric types with high precision OFF; they exercise a different lower position and bounded add/remove opportunities. Add a nonbuffered cumulative AVG control. Add a separate forward-frame query combining DECIMAL AVG, FIRST_VALUE, LAST_VALUE and NTH_VALUE(v_dec,2) over one named window to explore the extra state setters. Keep it separate from the primary AVG-only query so added functions do not define primary coverage.

Correctness oracle
For each output row, enumerate the frame's rows in its partition and average only non-NULL values. Empty frames and all-NULL frames return NULL. In [10,20,30,40], the forward-to-end means are [30,35,40,NULL]; current-to-end means are [25,30,35,40]; one-preceding/one-following means are [15,20,30,35]. In [NULL,20,NULL,60], forward-to-end means are [40,60,60,NULL]. Include remaining frames/partitions by the same enumeration, not by asking another window AVG query for the answer.
Choose an explicit six-decimal output cast for stable presentation. Quantize mathematical rational means to six decimals for DECIMAL comparison; permit at most 0.000001 absolute difference in the cast DOUBLE output. NULL must match exactly. FIRST_VALUE/LAST_VALUE use actual first/last frame rows, including NULLs; NTH_VALUE uses the second frame row and returns NULL if absent. These functions do not skip NULLs in this test. A positive-row-count all-NULL frame differs from an empty frame even though both AVG results are NULL.

Coverage observation
Record the window identity, partition/output-row identity, row_optimizable, aggregates_primed, needs_buffering, lower_limit, upper, last_rowno_in_cache, remove_previous_first_row, new_last_row, rows_in_frame and inverse state. At window_iterators.cc:1152 and 1190 capture the assigned rowno_in_frame, and correlate with the AVG call's m_count, m_frame_null_count, divisor and is_last_row_in_frame. Record whether division occurred or was skipped. Trace 1174,1207,1220 separately for auxiliary value functions and bounded frames. An empty final row alone is not evidence that the positive-divisor branch was tested.

Uncertainty
The snippets omit initial priming, all frame-limit calculations, executor scheduling and some null-result handling. The SQL shapes are candidates for the guarded branches; source algebra is not a runtime reproduction. High-precision ON/OFF equality cannot replace the independent frame oracle. Later release builds may already contain subsequent fixes; bind attribution to the given target and parent commits. This is this assistant's src2req output; SQL execution and measured source coverage have not occurred.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[window_frame_state_c296cddb93ff.txt](../prompt_pipeline_20261104/generation/stage2_req2test/responses/window_frame_state_c296cddb93ff.txt)

````text
Prerequisites
Use a MySQL build supporting the named window syntax, window AVG/FIRST_VALUE/LAST_VALUE/NTH_VALUE and windowing_use_high_precision. Bind coverage to c296cddb93ffc631f9b43d3b1ff769604e7469d7 and the saved parent if attribution is later attempted. Use one fresh session and a selected disposable schema; wf_c296_values must not exist. All values are small exactly representable integer inputs; decimal and real columns contain the same values. The script restores the precision setting on normal completion; close the session on an abort after saving diagnostics.

SQL
```sql
-- Target: c296cddb93ffc631f9b43d3b1ff769604e7469d7.
-- Source coverage is tied to this SHA; later releases may contain fixes.
SELECT VERSION() AS server_version, DATABASE() AS test_schema,
       @@SESSION.windowing_use_high_precision AS initial_high_precision;
SET @wf_c296_precision = @@SESSION.windowing_use_high_precision;
CREATE TEMPORARY TABLE wf_c296_values (
  g INT, id INT, v_dec DECIMAL(12,2), v_real DOUBLE, PRIMARY KEY (g,id)
);
INSERT INTO wf_c296_values VALUES
 (1,1,10,10),
 (1,2,20,20),
 (1,3,30,30),
 (1,4,40,40),
 (2,1,NULL,NULL),
 (2,2,20,20),
 (2,3,NULL,NULL),
 (2,4,60,60),
 (3,1,NULL,NULL),
 (3,2,NULL,NULL),
 (4,1,7,7);

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN01_DEC_FORWARD
SELECT 'WIN01_DEC_FORWARD' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN02_REAL_FORWARD_INVERSE
SELECT 'WIN02_REAL_FORWARD_INVERSE' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = ON;

-- CASE WIN03_REAL_FORWARD_PRECISE
SELECT 'WIN03_REAL_FORWARD_PRECISE' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN04_DEC_CURRENT
SELECT 'WIN04_DEC_CURRENT' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN05_REAL_CURRENT
SELECT 'WIN05_REAL_CURRENT' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN06_DEC_BOUNDED
SELECT 'WIN06_DEC_BOUNDED' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN07_REAL_BOUNDED
SELECT 'WIN07_REAL_BOUNDED' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN08_DEC_CUMULATIVE_CONTROL
SELECT 'WIN08_DEC_CUMULATIVE_CONTROL' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN09_VALUE_FUNCTIONS
SELECT 'WIN09_VALUE_FUNCTIONS' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v,
       FIRST_VALUE(v_dec) OVER w AS first_v,
       LAST_VALUE(v_dec) OVER w AS last_v,
       NTH_VALUE(v_dec,2) OVER w AS second_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

DROP TEMPORARY TABLE wf_c296_values;
SET SESSION windowing_use_high_precision = @wf_c296_precision;
```

Expected results and oracle
Enumerate the frame for each (g,id), discard NULL only for AVG, and divide sum by the count of remaining values. Format AVG through the explicit DECIMAL(20,6) output cast. Decimal expected strings are exact six-place rounded semantic results; compare numeric values rather than textual trailing-zero formatting. For REAL only, permit absolute error <=0.000001 after the cast. All NULL positions must match exactly. FIRST/LAST/NTH use frame-row positions and retain NULLs. For group 1, forward means are 30,35,40,NULL; current means 25,30,35,40; bounded means 15,20,30,35. The all-NULL and singleton groups test different boundaries. The ON query and cumulative query are controls, not trusted-answer generators.

WIN01_DEC_FORWARD: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "30.000000"], [1, 2, "35.000000"], [1, 3, "40.000000"], [1, 4, null], [2, 1, "40.000000"], [2, 2, "60.000000"], [2, 3, "60.000000"], [2, 4, null], [3, 1, null], [3, 2, null], [4, 1, null]]
WIN02_REAL_FORWARD_INVERSE: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "30.000000"], [1, 2, "35.000000"], [1, 3, "40.000000"], [1, 4, null], [2, 1, "40.000000"], [2, 2, "60.000000"], [2, 3, "60.000000"], [2, 4, null], [3, 1, null], [3, 2, null], [4, 1, null]]
WIN03_REAL_FORWARD_PRECISE: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "30.000000"], [1, 2, "35.000000"], [1, 3, "40.000000"], [1, 4, null], [2, 1, "40.000000"], [2, 2, "60.000000"], [2, 3, "60.000000"], [2, 4, null], [3, 1, null], [3, 2, null], [4, 1, null]]
WIN04_DEC_CURRENT: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "25.000000"], [1, 2, "30.000000"], [1, 3, "35.000000"], [1, 4, "40.000000"], [2, 1, "40.000000"], [2, 2, "40.000000"], [2, 3, "60.000000"], [2, 4, "60.000000"], [3, 1, null], [3, 2, null], [4, 1, "7.000000"]]
WIN05_REAL_CURRENT: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "25.000000"], [1, 2, "30.000000"], [1, 3, "35.000000"], [1, 4, "40.000000"], [2, 1, "40.000000"], [2, 2, "40.000000"], [2, 3, "60.000000"], [2, 4, "60.000000"], [3, 1, null], [3, 2, null], [4, 1, "7.000000"]]
WIN06_DEC_BOUNDED: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "15.000000"], [1, 2, "20.000000"], [1, 3, "30.000000"], [1, 4, "35.000000"], [2, 1, "20.000000"], [2, 2, "20.000000"], [2, 3, "40.000000"], [2, 4, "60.000000"], [3, 1, null], [3, 2, null], [4, 1, "7.000000"]]
WIN07_REAL_BOUNDED: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "15.000000"], [1, 2, "20.000000"], [1, 3, "30.000000"], [1, 4, "35.000000"], [2, 1, "20.000000"], [2, 2, "20.000000"], [2, 3, "40.000000"], [2, 4, "60.000000"], [3, 1, null], [3, 2, null], [4, 1, "7.000000"]]
WIN08_DEC_CUMULATIVE_CONTROL: columns=['g', 'id', 'avg_v']; expected=[[1, 1, "10.000000"], [1, 2, "15.000000"], [1, 3, "20.000000"], [1, 4, "25.000000"], [2, 1, null], [2, 2, "20.000000"], [2, 3, "20.000000"], [2, 4, "40.000000"], [3, 1, null], [3, 2, null], [4, 1, "7.000000"]]
WIN09_VALUE_FUNCTIONS: columns=['g', 'id', 'avg_v', 'first_v', 'last_v', 'second_v']; expected=[[1, 1, "30.000000", 20, 40, 30], [1, 2, "35.000000", 30, 40, 40], [1, 3, "40.000000", 40, 40, null], [1, 4, null, null, null, null], [2, 1, "40.000000", 20, 60, null], [2, 2, "60.000000", null, 60, 60], [2, 3, "60.000000", 60, 60, null], [2, 4, null, null, null, null], [3, 1, null, null, null, null], [3, 2, null, null, null, null], [4, 1, null, null, null, null]]

Coverage observation
Observe optimized ROWS strategy and priming at sql/iterators/window_iterators.cc:1092, the removal/no-new-last-row guards at 1098-1107, inverse and position state at 1150-1156, and the AVG buffered divisors at sql/item_sum.cc:2286-2290,2350-2357. Correlate window/object/output-row identity, lower_limit, current_row, rows_in_frame, rowno_in_frame, m_count, m_frame_null_count and is_last_row_in_frame. Trace the additional 1174/1190/1207 setters in WIN09 and 1220 for bounded frames separately. WIN02 is the intended REAL inverse candidate; WIN03 enables high precision. The displayed source formula can assign zero with a 1 FOLLOWING lower border, but these scripts do not claim the runtime guards were reached.

Execution status
Generated by the current assistant from the saved req2test prompt and its new src2req requirements. No database was connected, SQL executed, or source coverage measured. Expected rows are semantic calculations, not observed results. Retain SQL errors/crashes/missing results as separate observations; do not silently treat them as correct or as confirmed bugs.
````

### 提取后实际执行的完整 SQL

原件：[window_frame_state_c296cddb93ff.sql](../prompt_pipeline_20261104/generation/sql/window_frame_state_c296cddb93ff.sql)

````sql
-- Target: c296cddb93ffc631f9b43d3b1ff769604e7469d7.
-- Source coverage is tied to this SHA; later releases may contain fixes.
SELECT VERSION() AS server_version, DATABASE() AS test_schema,
       @@SESSION.windowing_use_high_precision AS initial_high_precision;
SET @wf_c296_precision = @@SESSION.windowing_use_high_precision;
CREATE TEMPORARY TABLE wf_c296_values (
  g INT, id INT, v_dec DECIMAL(12,2), v_real DOUBLE, PRIMARY KEY (g,id)
);
INSERT INTO wf_c296_values VALUES
 (1,1,10,10),
 (1,2,20,20),
 (1,3,30,30),
 (1,4,40,40),
 (2,1,NULL,NULL),
 (2,2,20,20),
 (2,3,NULL,NULL),
 (2,4,60,60),
 (3,1,NULL,NULL),
 (3,2,NULL,NULL),
 (4,1,7,7);

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN01_DEC_FORWARD
SELECT 'WIN01_DEC_FORWARD' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN02_REAL_FORWARD_INVERSE
SELECT 'WIN02_REAL_FORWARD_INVERSE' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = ON;

-- CASE WIN03_REAL_FORWARD_PRECISE
SELECT 'WIN03_REAL_FORWARD_PRECISE' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN04_DEC_CURRENT
SELECT 'WIN04_DEC_CURRENT' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN05_REAL_CURRENT
SELECT 'WIN05_REAL_CURRENT' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN06_DEC_BOUNDED
SELECT 'WIN06_DEC_BOUNDED' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN07_REAL_BOUNDED
SELECT 'WIN07_REAL_BOUNDED' AS case_id;
SELECT g,id,CAST(AVG(v_real) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN08_DEC_CUMULATIVE_CONTROL
SELECT 'WIN08_DEC_CUMULATIVE_CONTROL' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
ORDER BY g,id;

SET SESSION windowing_use_high_precision = OFF;

-- CASE WIN09_VALUE_FUNCTIONS
SELECT 'WIN09_VALUE_FUNCTIONS' AS case_id;
SELECT g,id,CAST(AVG(v_dec) OVER w AS DECIMAL(20,6)) AS avg_v,
       FIRST_VALUE(v_dec) OVER w AS first_v,
       LAST_VALUE(v_dec) OVER w AS last_v,
       NTH_VALUE(v_dec,2) OVER w AS second_v
FROM wf_c296_values
WINDOW w AS (PARTITION BY g ORDER BY id ROWS BETWEEN 1 FOLLOWING AND UNBOUNDED FOLLOWING)
ORDER BY g,id;

DROP TEMPORARY TABLE wf_c296_values;
SET SESSION windowing_use_high_precision = @wf_c296_precision;
````

### 独立保存的预期结果与 oracle

原件：[window_frame_state_c296cddb93ff.json](../prompt_pipeline_20261104/generation/expected/window_frame_state_c296cddb93ff.json)

````json
{
  "target": "window_frame_state_c296cddb93ff",
  "row_order": "significant; each data SELECT orders by stable keys",
  "result_protocol": "A one-row case_id result identifies the next data result set. Environment metadata is not a test result. Case labels must be present in the specified order; omitted/error results cannot pass.",
  "null_encoding": "JSON null means SQL NULL, never zero or an empty string",
  "cases": [
    {
      "case_id": "WIN01_DEC_FORWARD",
      "family": "following",
      "input_type": "v_dec",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_exact",
      "absolute_tolerance": "0",
      "rows": [
        [
          1,
          1,
          "30.000000"
        ],
        [
          1,
          2,
          "35.000000"
        ],
        [
          1,
          3,
          "40.000000"
        ],
        [
          1,
          4,
          null
        ],
        [
          2,
          1,
          "40.000000"
        ],
        [
          2,
          2,
          "60.000000"
        ],
        [
          2,
          3,
          "60.000000"
        ],
        [
          2,
          4,
          null
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          null
        ]
      ]
    },
    {
      "case_id": "WIN02_REAL_FORWARD_INVERSE",
      "family": "following",
      "input_type": "v_real",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_absolute_tolerance",
      "absolute_tolerance": "0.000001",
      "rows": [
        [
          1,
          1,
          "30.000000"
        ],
        [
          1,
          2,
          "35.000000"
        ],
        [
          1,
          3,
          "40.000000"
        ],
        [
          1,
          4,
          null
        ],
        [
          2,
          1,
          "40.000000"
        ],
        [
          2,
          2,
          "60.000000"
        ],
        [
          2,
          3,
          "60.000000"
        ],
        [
          2,
          4,
          null
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          null
        ]
      ]
    },
    {
      "case_id": "WIN03_REAL_FORWARD_PRECISE",
      "family": "following",
      "input_type": "v_real",
      "high_precision": "ON",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_absolute_tolerance",
      "absolute_tolerance": "0.000001",
      "rows": [
        [
          1,
          1,
          "30.000000"
        ],
        [
          1,
          2,
          "35.000000"
        ],
        [
          1,
          3,
          "40.000000"
        ],
        [
          1,
          4,
          null
        ],
        [
          2,
          1,
          "40.000000"
        ],
        [
          2,
          2,
          "60.000000"
        ],
        [
          2,
          3,
          "60.000000"
        ],
        [
          2,
          4,
          null
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          null
        ]
      ]
    },
    {
      "case_id": "WIN04_DEC_CURRENT",
      "family": "current",
      "input_type": "v_dec",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_exact",
      "absolute_tolerance": "0",
      "rows": [
        [
          1,
          1,
          "25.000000"
        ],
        [
          1,
          2,
          "30.000000"
        ],
        [
          1,
          3,
          "35.000000"
        ],
        [
          1,
          4,
          "40.000000"
        ],
        [
          2,
          1,
          "40.000000"
        ],
        [
          2,
          2,
          "40.000000"
        ],
        [
          2,
          3,
          "60.000000"
        ],
        [
          2,
          4,
          "60.000000"
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          "7.000000"
        ]
      ]
    },
    {
      "case_id": "WIN05_REAL_CURRENT",
      "family": "current",
      "input_type": "v_real",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_absolute_tolerance",
      "absolute_tolerance": "0.000001",
      "rows": [
        [
          1,
          1,
          "25.000000"
        ],
        [
          1,
          2,
          "30.000000"
        ],
        [
          1,
          3,
          "35.000000"
        ],
        [
          1,
          4,
          "40.000000"
        ],
        [
          2,
          1,
          "40.000000"
        ],
        [
          2,
          2,
          "40.000000"
        ],
        [
          2,
          3,
          "60.000000"
        ],
        [
          2,
          4,
          "60.000000"
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          "7.000000"
        ]
      ]
    },
    {
      "case_id": "WIN06_DEC_BOUNDED",
      "family": "bounded",
      "input_type": "v_dec",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_exact",
      "absolute_tolerance": "0",
      "rows": [
        [
          1,
          1,
          "15.000000"
        ],
        [
          1,
          2,
          "20.000000"
        ],
        [
          1,
          3,
          "30.000000"
        ],
        [
          1,
          4,
          "35.000000"
        ],
        [
          2,
          1,
          "20.000000"
        ],
        [
          2,
          2,
          "20.000000"
        ],
        [
          2,
          3,
          "40.000000"
        ],
        [
          2,
          4,
          "60.000000"
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          "7.000000"
        ]
      ]
    },
    {
      "case_id": "WIN07_REAL_BOUNDED",
      "family": "bounded",
      "input_type": "v_real",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_absolute_tolerance",
      "absolute_tolerance": "0.000001",
      "rows": [
        [
          1,
          1,
          "15.000000"
        ],
        [
          1,
          2,
          "20.000000"
        ],
        [
          1,
          3,
          "30.000000"
        ],
        [
          1,
          4,
          "35.000000"
        ],
        [
          2,
          1,
          "20.000000"
        ],
        [
          2,
          2,
          "20.000000"
        ],
        [
          2,
          3,
          "40.000000"
        ],
        [
          2,
          4,
          "60.000000"
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          "7.000000"
        ]
      ]
    },
    {
      "case_id": "WIN08_DEC_CUMULATIVE_CONTROL",
      "family": "cumulative",
      "input_type": "v_dec",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v"
      ],
      "comparison": "numeric_exact",
      "absolute_tolerance": "0",
      "rows": [
        [
          1,
          1,
          "10.000000"
        ],
        [
          1,
          2,
          "15.000000"
        ],
        [
          1,
          3,
          "20.000000"
        ],
        [
          1,
          4,
          "25.000000"
        ],
        [
          2,
          1,
          null
        ],
        [
          2,
          2,
          "20.000000"
        ],
        [
          2,
          3,
          "20.000000"
        ],
        [
          2,
          4,
          "40.000000"
        ],
        [
          3,
          1,
          null
        ],
        [
          3,
          2,
          null
        ],
        [
          4,
          1,
          "7.000000"
        ]
      ]
    },
    {
      "case_id": "WIN09_VALUE_FUNCTIONS",
      "family": "following",
      "input_type": "v_dec",
      "high_precision": "OFF",
      "columns": [
        "g",
        "id",
        "avg_v",
        "first_v",
        "last_v",
        "second_v"
      ],
      "comparison": "numeric_exact",
      "absolute_tolerance": "0",
      "rows": [
        [
          1,
          1,
          "30.000000",
          20,
          40,
          30
        ],
        [
          1,
          2,
          "35.000000",
          30,
          40,
          40
        ],
        [
          1,
          3,
          "40.000000",
          40,
          40,
          null
        ],
        [
          1,
          4,
          null,
          null,
          null,
          null
        ],
        [
          2,
          1,
          "40.000000",
          20,
          60,
          null
        ],
        [
          2,
          2,
          "60.000000",
          null,
          60,
          60
        ],
        [
          2,
          3,
          "60.000000",
          60,
          60,
          null
        ],
        [
          2,
          4,
          null,
          null,
          null,
          null
        ],
        [
          3,
          1,
          null,
          null,
          null,
          null
        ],
        [
          3,
          2,
          null,
          null,
          null,
          null
        ],
        [
          4,
          1,
          null,
          null,
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

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/result.json)。精确 revision：`74c7ccfa27f482576412300e5f92fd3dbeb54cfa`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "window_frame_state_c296cddb93ff",
  "revision": "74c7ccfa27f482576412300e5f92fd3dbeb54cfa",
  "role": "parent",
  "run_id": "74c7ccfa27f4-bf59ce57",
  "started": "2026-11-04T04:12:26.167614+00:00",
  "sql_sha256": "87b2231315cf8993a546525c367335c81534371f9006e7592b21de96d7e8d4f6",
  "expected_sha256": "a22fbd1fcb4f9dad9377dc2b8c700dcd4c729a32fd60f54c482f7156c7bfd24d",
  "runtime_path": "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/74c7ccfa27f4",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-74c7ccfa27f4-bf59ce57",
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
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/74c7ccfa27f4:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "74c7ccfa27f4-bf59ce57"
  ],
  "container_id": "ebe8b4da38f8fb3eb19494054a6bbc2c330f1dbe6b2a8b0505862ae0bf685523",
  "server_metadata_tsv": "8.0.32\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "9b1c7a6f60cd796f52d4462f05348f42ae4f35252d5a57d9073f819b0b4d4c0a",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 287275,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T04:12:26.912238254Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T04:12:42.628068+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T04:12:40.795701+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-74c7ccfa27f4-bf59ce57",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/74c7ccfa27f4-bf59ce57/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_74c7ccfa27f4_1"
      ],
      "schema": "wf_three_74c7ccfa27f4_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 287275,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:12:26.912238254Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:12:40.934333+00:00",
      "stdout_sha256": "bc0e1153e9cf220a1deec376d52a121c18ac90a5e5d850953be6ad032caabc20",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T04:12:41.032439+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-74c7ccfa27f4-bf59ce57",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/74c7ccfa27f4-bf59ce57/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_74c7ccfa27f4_2"
      ],
      "schema": "wf_three_74c7ccfa27f4_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 287275,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:12:26.912238254Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:12:41.168613+00:00",
      "stdout_sha256": "27bee05c182c7f29a16270b7ed79cc4ace861ef9bb43ac3adcde50d0fb4d05c5",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T04:12:41.277954+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-74c7ccfa27f4-bf59ce57",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/74c7ccfa27f4-bf59ce57/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_74c7ccfa27f4_3"
      ],
      "schema": "wf_three_74c7ccfa27f4_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 287275,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:12:26.912238254Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:12:41.409494+00:00",
      "stdout_sha256": "c3d2b7c5d0bc3324e06b552fb0eb8b90e00e309bc15b5c9bcdfd8f661e621f01",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema | initial_high_precision |
| --- | --- | --- |
| 8.0.32 | wf_three_74c7ccfa27f4_1 | 1 |

结果集 2：

| case_id |
| --- |
| WIN01_DEC_FORWARD |

结果集 3：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 35.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 4：

| case_id |
| --- |
| WIN02_REAL_FORWARD_INVERSE |

结果集 5：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 35.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 6：

| case_id |
| --- |
| WIN03_REAL_FORWARD_PRECISE |

结果集 7：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 35.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 8：

| case_id |
| --- |
| WIN04_DEC_CURRENT |

结果集 9：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 25.000000 |
| 1 | 2 | 30.000000 |
| 1 | 3 | 35.000000 |
| 1 | 4 | 40.000000 |
| 2 | 1 | 40.000000 |
| 2 | 2 | 40.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 10：

| case_id |
| --- |
| WIN05_REAL_CURRENT |

结果集 11：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 25.000000 |
| 1 | 2 | 30.000000 |
| 1 | 3 | 35.000000 |
| 1 | 4 | 40.000000 |
| 2 | 1 | 40.000000 |
| 2 | 2 | 40.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 12：

| case_id |
| --- |
| WIN06_DEC_BOUNDED |

结果集 13：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 15.000000 |
| 1 | 2 | 20.000000 |
| 1 | 3 | 30.000000 |
| 1 | 4 | 35.000000 |
| 2 | 1 | 20.000000 |
| 2 | 2 | 20.000000 |
| 2 | 3 | 40.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 14：

| case_id |
| --- |
| WIN07_REAL_BOUNDED |

结果集 15：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 15.000000 |
| 1 | 2 | 20.000000 |
| 1 | 3 | 30.000000 |
| 1 | 4 | 35.000000 |
| 2 | 1 | 20.000000 |
| 2 | 2 | 20.000000 |
| 2 | 3 | 40.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 16：

| case_id |
| --- |
| WIN08_DEC_CUMULATIVE_CONTROL |

结果集 17：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 10.000000 |
| 1 | 2 | 15.000000 |
| 1 | 3 | 20.000000 |
| 1 | 4 | 25.000000 |
| 2 | 1 | NULL |
| 2 | 2 | 20.000000 |
| 2 | 3 | 20.000000 |
| 2 | 4 | 40.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 18：

| case_id |
| --- |
| WIN09_VALUE_FUNCTIONS |

结果集 19：

| g | id | avg_v | first_v | last_v | second_v |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 30.000000 | 20.00 | 40.00 | 30.00 |
| 1 | 2 | 35.000000 | 30.00 | 40.00 | 40.00 |
| 1 | 3 | 40.000000 | 40.00 | 40.00 | NULL |
| 1 | 4 | NULL | NULL | NULL | NULL |
| 2 | 1 | 40.000000 | 20.00 | 60.00 | NULL |
| 2 | 2 | 60.000000 | NULL | 60.00 | 60.00 |
| 2 | 3 | 60.000000 | 60.00 | 60.00 | NULL |
| 2 | 4 | NULL | NULL | NULL | NULL |
| 3 | 1 | NULL | NULL | NULL | NULL |
| 3 | 2 | NULL | NULL | NULL | NULL |
| 4 | 1 | NULL | NULL | NULL | NULL |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/result.json)。精确 revision：`c296cddb93ffc631f9b43d3b1ff769604e7469d7`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "target": "window_frame_state_c296cddb93ff",
  "revision": "c296cddb93ffc631f9b43d3b1ff769604e7469d7",
  "role": "target",
  "run_id": "c296cddb93ff-7fb4727f",
  "started": "2026-11-04T04:13:35.136309+00:00",
  "sql_sha256": "87b2231315cf8993a546525c367335c81534371f9006e7592b21de96d7e8d4f6",
  "expected_sha256": "a22fbd1fcb4f9dad9377dc2b8c700dcd4c729a32fd60f54c482f7156c7bfd24d",
  "runtime_path": "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/c296cddb93ff",
  "builder_image": "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
  "runtime_error": null,
  "runner_sha256": "96fc34f225a5fa1f1f0212992f4cf40ab7605c0a424eb54364234de78847d040",
  "source_branch_coverage": "not_instrumented",
  "launch_command": [
    "docker",
    "run",
    "-d",
    "--name",
    "codex-three-c296cddb93ff-7fb4727f",
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
    "/EXPERIMENT_ROOT/mysql-three-prompts-20261104-a/runtime/c296cddb93ff:/runtime:ro",
    "sha256:b2f51e7795136616ef1b1a35c529fb290dfdfe8e5f7fdd348248b5991f38674d",
    "bash",
    "/work/server.sh",
    "c296cddb93ff-7fb4727f"
  ],
  "container_id": "7230776eeb38fc99dd9704ca01de39c6356f0c3154e1503871763cf2fefca0f7",
  "server_metadata_tsv": "8.0.32\tLinux\tx86_64\tONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION\tindex_merge=on,index_merge_union=on,index_merge_sort_union=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_pushdown=on,mrr=on,mrr_cost_based=on,block_nested_loop=on,batched_key_access=off,materialization=on,semijoin=on,loosescan=on,firstmatch=on,duplicateweedout=on,subquery_materialization_cost_based=on,use_index_extensions=on,condition_fanout_filter=on,derived_merge=on,use_invisible_indexes=off,skip_scan=on,hash_join=on,subquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=off,derived_condition_pushdown=on\t1\tutf8mb4\tutf8mb4_0900_ai_ci",
  "mysqld_sha256": "083a9cd4a3939ff10e3929804368397dd1e9997928f61e06be1f83041502de49",
  "state_before_cleanup": {
    "Status": "running",
    "Running": true,
    "Paused": false,
    "Restarting": false,
    "OOMKilled": false,
    "Dead": false,
    "Pid": 306307,
    "ExitCode": 0,
    "Error": "",
    "StartedAt": "2026-11-04T04:13:35.875246078Z",
    "FinishedAt": "0001-01-01T00:00:00Z"
  },
  "container_removed": true,
  "finished": "2026-11-04T04:13:47.364900+00:00",
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "started": "2026-11-04T04:13:45.822185+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-c296cddb93ff-7fb4727f",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/c296cddb93ff-7fb4727f/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_c296cddb93ff_1"
      ],
      "schema": "wf_three_c296cddb93ff_1",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 306307,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:13:35.875246078Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:13:45.965067+00:00",
      "stdout_sha256": "70f4b907240ea98b38cfb3210651e085e2a7385e11adda47a7e90de37e20fb7a",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 2,
      "started": "2026-11-04T04:13:46.076221+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-c296cddb93ff-7fb4727f",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/c296cddb93ff-7fb4727f/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_c296cddb93ff_2"
      ],
      "schema": "wf_three_c296cddb93ff_2",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 306307,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:13:35.875246078Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:13:46.220170+00:00",
      "stdout_sha256": "0680198ddb2a46783c86d0ec0666fece6eb08a69ddf5ae33ac969e1b75523efe",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    {
      "repeat": 3,
      "started": "2026-11-04T04:13:46.324074+00:00",
      "command": [
        "docker",
        "exec",
        "-i",
        "codex-three-c296cddb93ff-7fb4727f",
        "/runtime/bin/mysql",
        "--no-defaults",
        "--protocol=socket",
        "--socket=/work/data/c296cddb93ff-7fb4727f/mysql.sock",
        "-uroot",
        "--default-character-set=utf8mb4",
        "--xml",
        "--force",
        "--binary-mode",
        "--database=wf_three_c296cddb93ff_3"
      ],
      "schema": "wf_three_c296cddb93ff_3",
      "timeout": false,
      "returncode": 0,
      "server_state": {
        "Status": "running",
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "Dead": false,
        "Pid": 306307,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2026-11-04T04:13:35.875246078Z",
        "FinishedAt": "0001-01-01T00:00:00Z"
      },
      "finished": "2026-11-04T04:13:46.457403+00:00",
      "stdout_sha256": "2f05bb4f582ce1ac5d98baa976ed4050e4512763778921a56860755280800063",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_20261104/runtime/results/window_frame_state_c296cddb93ff/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| server_version | test_schema | initial_high_precision |
| --- | --- | --- |
| 8.0.32 | wf_three_c296cddb93ff_1 | 1 |

结果集 2：

| case_id |
| --- |
| WIN01_DEC_FORWARD |

结果集 3：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 70.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 4：

| case_id |
| --- |
| WIN02_REAL_FORWARD_INVERSE |

结果集 5：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 70.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 6：

| case_id |
| --- |
| WIN03_REAL_FORWARD_PRECISE |

结果集 7：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 30.000000 |
| 1 | 2 | 35.000000 |
| 1 | 3 | 40.000000 |
| 1 | 4 | NULL |
| 2 | 1 | 40.000000 |
| 2 | 2 | 60.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | NULL |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | NULL |

结果集 8：

| case_id |
| --- |
| WIN04_DEC_CURRENT |

结果集 9：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 25.000000 |
| 1 | 2 | 90.000000 |
| 1 | 3 | 70.000000 |
| 1 | 4 | 40.000000 |
| 2 | 1 | 40.000000 |
| 2 | 2 | 80.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 10：

| case_id |
| --- |
| WIN05_REAL_CURRENT |

结果集 11：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 25.000000 |
| 1 | 2 | 90.000000 |
| 1 | 3 | 70.000000 |
| 1 | 4 | 40.000000 |
| 2 | 1 | 40.000000 |
| 2 | 2 | 80.000000 |
| 2 | 3 | 60.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 12：

| case_id |
| --- |
| WIN06_DEC_BOUNDED |

结果集 13：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 15.000000 |
| 1 | 2 | 20.000000 |
| 1 | 3 | 30.000000 |
| 1 | 4 | 35.000000 |
| 2 | 1 | 20.000000 |
| 2 | 2 | 20.000000 |
| 2 | 3 | 40.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 14：

| case_id |
| --- |
| WIN07_REAL_BOUNDED |

结果集 15：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 15.000000 |
| 1 | 2 | 20.000000 |
| 1 | 3 | 30.000000 |
| 1 | 4 | 35.000000 |
| 2 | 1 | 20.000000 |
| 2 | 2 | 20.000000 |
| 2 | 3 | 40.000000 |
| 2 | 4 | 60.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 16：

| case_id |
| --- |
| WIN08_DEC_CUMULATIVE_CONTROL |

结果集 17：

| g | id | avg_v |
| --- | --- | --- |
| 1 | 1 | 10.000000 |
| 1 | 2 | 15.000000 |
| 1 | 3 | 20.000000 |
| 1 | 4 | 25.000000 |
| 2 | 1 | NULL |
| 2 | 2 | 20.000000 |
| 2 | 3 | 20.000000 |
| 2 | 4 | 40.000000 |
| 3 | 1 | NULL |
| 3 | 2 | NULL |
| 4 | 1 | 7.000000 |

结果集 18：

| case_id |
| --- |
| WIN09_VALUE_FUNCTIONS |

结果集 19：

| g | id | avg_v | first_v | last_v | second_v |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 30.000000 | 20.00 | 40.00 | 30.00 |
| 1 | 2 | 70.000000 | 30.00 | 40.00 | 40.00 |
| 1 | 3 | 40.000000 | 40.00 | 40.00 | NULL |
| 1 | 4 | NULL | NULL | NULL | NULL |
| 2 | 1 | 40.000000 | 20.00 | 60.00 | NULL |
| 2 | 2 | 60.000000 | NULL | 60.00 | 60.00 |
| 2 | 3 | 60.000000 | 60.00 | 60.00 | NULL |
| 2 | 4 | NULL | NULL | NULL | NULL |
| 3 | 1 | NULL | NULL | NULL | NULL |
| 3 | 2 | NULL | NULL | NULL | NULL |
| 4 | 1 | NULL | NULL | NULL | NULL |

判定与环境补充：[逐检查点比较](../prompt_pipeline_20261104/runtime/comparison.json)、[完整执行报告](../prompt_pipeline_20261104/runtime/final_report.txt)、[输入构建执行关联](../prompt_pipeline_20261104/lineage.json)。

## 2. DeepSeek 重跑

Stage 1 实际请求 [stage1_request.json](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage1_request.json)；原始响应 [stage1_response_raw.json](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage1_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

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
      "content_characters": 18262
    }
  ]
}
```

Stage 2 实际请求 [stage2_request.json](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage2_request.json)；原始响应 [stage2_response_raw.json](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage2_response_raw.json)。messages 为一个 user 消息，正文与本读本展示的对应完整提示词一致。

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
      "content_characters": 8759
    }
  ]
}
```

### Stage 1 输出：测试偏好与需求原文

原件：[stage1_output.txt](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage1_output.txt)

````text
Target: window_frame_state_c296cddb93ff

Target observation: Buffered window-frame row-position state during optimized ROWS-frame evaluation and its consumption by AVG

Revision: c296cddb93ffc631f9b43d3b1ff769604e7469d7

Parent revision: 74c7ccfa27f482576412300e5f92fd3dbeb54cfa

Source repository: https://github.com/mysql/mysql-server

Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.

Line numbers below refer to the upstream file at this revision.

Source-required conditions

The window function is an AVG (Item_sum_avg) over a window frame that requires buffering (sql/item_sum.cc:2287-2289, 2350-2352). The frame uses ROWS bounds with an optimized strategy (sql/iterators/window_iterators.cc:691, 1092). During evaluation of rows 2..N in a partition, the optimizer adjusts the frame by removing the previous first row and/or adding a new last row (sql/iterators/window_iterators.cc:1092-1103). The execution state m_rowno_in_frame is set before evaluating framing functions, either when removing the previous first row (sql/iterators/window_iterators.cc:1152), when evaluating first/last value (sql/iterators/window_iterators.cc:1174, 1190), when evaluating NTH_VALUE (sql/iterators/window_iterators.cc:1207), or when adding a new last row (sql/iterators/window_iterators.cc:1220). AVG consumes this state in val_real() or val_decimal() to compute the divisor as rowno_in_frame() minus null count (sql/item_sum.cc:2288, 2351).

Candidate construction

Create a table with a partition key and an integer value column. Insert multiple rows per partition to ensure at least three rows in a partition, so the optimized ROWS-frame path executes for current rows 2..N (sql/iterators/window_iterators.cc:1092). Use a window specification with ROWS BETWEEN 1 PRECEDING AND CURRENT ROW or similar ROWS bounds that trigger row_optimizable evaluation (sql/iterators/window_iterators.cc:691). Apply AVG over the integer column. Include null values in some frame rows to exercise the null-count adjustment in the divisor (sql/item_sum.cc:2288, 2351). For example, a partition with values (1, NULL, 3) and a frame of ROWS BETWEEN 1 PRECEDING AND CURRENT ROW produces frames of size 1 or 2 as the current row advances, with varying rowno_in_frame and null counts.

Correctness oracle

For each current row, the AVG result is the sum of non-null values in the frame divided by the number of non-null rows in the frame. The divisor is rowno_in_frame() minus m_frame_null_count when buffering is used (sql/item_sum.cc:2288, 2351). For a frame with ROWS BETWEEN 1 PRECEDING AND CURRENT ROW, the frame includes the current row and the immediately preceding row (if any). With values (1, NULL, 3) in a partition, the expected results are: row 1 → 1/1 = 1, row 2 → 1/1 = 1 (NULL excluded from divisor), row 3 → 3/2 = 1.5. Derive expected values from the inserted data and the frame definition, not from another server version's output.

Coverage observation

On the specified revision, use a breakpoint or instrumentation at sql/item_sum.cc:2286-2291 or sql/item_sum.cc:2350-2358, and at sql/iterators/window_iterators.cc:1152, 1174, 1190, 1207, or 1220, to observe the values of rowno_in_frame(), m_frame_null_count, and the computed divisor for each current row in the optimized ROWS-frame path. Confirm that set_rowno_in_frame() is called before Item_sum_avg::val_real() or val_decimal() consumes it. EXPLAIN alone does not confirm the internal frame-state values.

Uncertainty

The local excerpts do not establish the complete path from SQL window specification to the selection of row_optimizable versus static_aggregate or range_optimizable. The conditions under which w.optimizable_row_aggregates() returns true are not shown, and the helper functions that prime aggregates and manage the frame cache are omitted. If the candidate query does not reach the optimized ROWS-frame branch, inspect Window::optimizable_row_aggregates() and the window iterator initialization to confirm the frame bounds and aggregate types. Coverage of the state-setting lines and correct AVG output are separate observations.
````

### Stage 2 实际输入：填入本次 Stage 1 后的完整提示词

原件：[stage2_prompt.txt](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage2_prompt.txt)

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
Target: window_frame_state_c296cddb93ff

Target observation: Buffered window-frame row-position state during optimized ROWS-frame evaluation and its consumption by AVG

Revision: c296cddb93ffc631f9b43d3b1ff769604e7469d7

Parent revision: 74c7ccfa27f482576412300e5f92fd3dbeb54cfa

Source repository: https://github.com/mysql/mysql-server

Scope: local excerpts of the target revision; omitted callers/helpers are not assumed known.

Line numbers below refer to the upstream file at this revision.

Source-required conditions

The window function is an AVG (Item_sum_avg) over a window frame that requires buffering (sql/item_sum.cc:2287-2289, 2350-2352). The frame uses ROWS bounds with an optimized strategy (sql/iterators/window_iterators.cc:691, 1092). During evaluation of rows 2..N in a partition, the optimizer adjusts the frame by removing the previous first row and/or adding a new last row (sql/iterators/window_iterators.cc:1092-1103). The execution state m_rowno_in_frame is set before evaluating framing functions, either when removing the previous first row (sql/iterators/window_iterators.cc:1152), when evaluating first/last value (sql/iterators/window_iterators.cc:1174, 1190), when evaluating NTH_VALUE (sql/iterators/window_iterators.cc:1207), or when adding a new last row (sql/iterators/window_iterators.cc:1220). AVG consumes this state in val_real() or val_decimal() to compute the divisor as rowno_in_frame() minus null count (sql/item_sum.cc:2288, 2351).

Candidate construction

Create a table with a partition key and an integer value column. Insert multiple rows per partition to ensure at least three rows in a partition, so the optimized ROWS-frame path executes for current rows 2..N (sql/iterators/window_iterators.cc:1092). Use a window specification with ROWS BETWEEN 1 PRECEDING AND CURRENT ROW or similar ROWS bounds that trigger row_optimizable evaluation (sql/iterators/window_iterators.cc:691). Apply AVG over the integer column. Include null values in some frame rows to exercise the null-count adjustment in the divisor (sql/item_sum.cc:2288, 2351). For example, a partition with values (1, NULL, 3) and a frame of ROWS BETWEEN 1 PRECEDING AND CURRENT ROW produces frames of size 1 or 2 as the current row advances, with varying rowno_in_frame and null counts.

Correctness oracle

For each current row, the AVG result is the sum of non-null values in the frame divided by the number of non-null rows in the frame. The divisor is rowno_in_frame() minus m_frame_null_count when buffering is used (sql/item_sum.cc:2288, 2351). For a frame with ROWS BETWEEN 1 PRECEDING AND CURRENT ROW, the frame includes the current row and the immediately preceding row (if any). With values (1, NULL, 3) in a partition, the expected results are: row 1 → 1/1 = 1, row 2 → 1/1 = 1 (NULL excluded from divisor), row 3 → 3/2 = 1.5. Derive expected values from the inserted data and the frame definition, not from another server version's output.

Coverage observation

On the specified revision, use a breakpoint or instrumentation at sql/item_sum.cc:2286-2291 or sql/item_sum.cc:2350-2358, and at sql/iterators/window_iterators.cc:1152, 1174, 1190, 1207, or 1220, to observe the values of rowno_in_frame(), m_frame_null_count, and the computed divisor for each current row in the optimized ROWS-frame path. Confirm that set_rowno_in_frame() is called before Item_sum_avg::val_real() or val_decimal() consumes it. EXPLAIN alone does not confirm the internal frame-state values.

Uncertainty

The local excerpts do not establish the complete path from SQL window specification to the selection of row_optimizable versus static_aggregate or range_optimizable. The conditions under which w.optimizable_row_aggregates() returns true are not shown, and the helper functions that prime aggregates and manage the frame cache are omitted. If the candidate query does not reach the optimized ROWS-frame branch, inspect Window::optimizable_row_aggregates() and the window iterator initialization to confirm the frame bounds and aggregate types. Coverage of the state-setting lines and correct AVG output are separate observations.

# Test
````

### Stage 2 完整输出：SQL、预期结果与覆盖建议

原件：[stage2_output.txt](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/stage2_output.txt)

````text
Prerequisites
Use a disposable, already selected schema on a MySQL build at revision c296cddb93ffc631f9b43d3b1ff769604e7469d7 (or a build where the window-iterator and Item_sum_avg paths match the cited source lines). Use a fresh session with no existing objects named wf_avg_p, wf_avg_v, or wf_avg_out. The test relies on window functions being available and on the optimizer selecting the row-optimizable ROWS-frame path; this selection is not guaranteed by the SQL alone (see Coverage observation). Do not run on a version whose window-frame internals differ from the cited revision if source-line coverage is required.

SQL
```sql
CREATE TEMPORARY TABLE wf_avg_p (p INT NOT NULL, ord INT NOT NULL, v INT NULL);
INSERT INTO wf_avg_p VALUES
  (1, 1, 1),
  (1, 2, NULL),
  (1, 3, 3),
  (1, 4, 5),
  (2, 1, 10),
  (2, 2, NULL),
  (2, 3, NULL),
  (2, 4, 8);

SELECT
  p,
  ord,
  v,
  AVG(v) OVER (
    PARTITION BY p
    ORDER BY ord
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
  ) AS avg_v
FROM wf_avg_p
ORDER BY p, ord;

DROP TEMPORARY TABLE wf_avg_p;
```

Expected results and oracle
For each row, the frame is the current row plus the immediately preceding row within the partition (or just the current row for the first row of a partition). AVG is the sum of non-null values in the frame divided by the count of non-null values in the frame; the divisor is rowno_in_frame() minus m_frame_null_count when buffering is active (sql/item_sum.cc:2288, 2351). Expected rows, derived from the inserted data and the frame definition:

Partition 1, values (1, NULL, 3, 5) at ord 1..4:
- ord=1, v=1: frame {1}; sum=1, non-null count=1; avg=1.0000
- ord=2, v=NULL: frame {1, NULL}; sum=1, non-null count=1; avg=1.0000
- ord=3, v=3: frame {NULL, 3}; sum=3, non-null count=1; avg=3.0000
- ord=4, v=5: frame {3, 5}; sum=8, non-null count=2; avg=4.0000

Partition 2, values (10, NULL, NULL, 8) at ord 1..4:
- ord=1, v=10: frame {10}; sum=10, non-null count=1; avg=10.0000
- ord=2, v=NULL: frame {10, NULL}; sum=10, non-null count=1; avg=10.0000
- ord=3, v=NULL: frame {NULL, NULL}; sum=NULL, non-null count=0; avg=NULL
- ord=4, v=8: frame {NULL, 8}; sum=8, non-null count=1; avg=8.0000

So the SELECT must return exactly 8 rows in the order (p, ord) = (1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(2,4) with avg_v = 1.0000, 1.0000, 3.0000, 4.0000, 10.0000, 10.0000, NULL, 8.0000. Note that the ord=2 case in each partition specifically exercises the null-count adjustment: the frame size is 2 but the divisor must be 1, not 2. Compare values and row ordering; do not accept distinct-only or row-count-only matches. If the SELECT fails or the row set differs, record that separately; close the session to release remaining temporary tables.

Coverage observation
Separately from the result check, attach a breakpoint or instrumentation at sql/item_sum.cc:2286-2291 (val_real) and/or sql/item_sum.cc:2350-2358 (val_decimal), and at sql/iterators/window_iterators.cc:1152, 1174, 1190, 1207, or 1220. For each current row in partition 1 (ord 1..4) and partition 2 (ord 1..4), record rowno_in_frame(), m_frame_null_count, and the computed divisor (rowno_in_frame() - m_frame_null_count) at the moment Item_sum_avg consumes the state. Confirm that set_rowno_in_frame() was called before the AVG consumption for rows 2..N in each partition. Expected observations consistent with the oracle: for partition 1 ord=2, rowno_in_frame()=2, m_frame_null_count=1, divisor=1; for partition 1 ord=3, rowno_in_frame()=2, m_frame_null_count=1, divisor=1; for partition 2 ord=3, rowno_in_frame()=2, m_frame_null_count=2, divisor=0 (AVG returns NULL). Also confirm the query actually reaches the optimized ROWS-frame branch (sql/iterators/window_iterators.cc:691, 1092) rather than static_aggregate or range_optimizable; if it does not, inspect Window::optimizable_row_aggregates() and the window iterator initialization before revising the candidate. EXPLAIN alone does not confirm these internal values, and a correct result does not by itself prove the target lines were reached.

Execution status
Authored one-shot demonstration. The SQL, expected results, and source-line coverage have not been executed or measured. Branch selection into the optimized ROWS-frame path is not guaranteed by the SQL alone and must be confirmed via the coverage observation.
````

### 提取后实际执行的完整 SQL

原件：[generated.sql](../prompt_pipeline_deepseek_20261105/window_frame_state_c296cddb93ff/generated.sql)

````sql
CREATE TEMPORARY TABLE wf_avg_p (p INT NOT NULL, ord INT NOT NULL, v INT NULL);
INSERT INTO wf_avg_p VALUES
  (1, 1, 1),
  (1, 2, NULL),
  (1, 3, 3),
  (1, 4, 5),
  (2, 1, 10),
  (2, 2, NULL),
  (2, 3, NULL),
  (2, 4, 8);

SELECT
  p,
  ord,
  v,
  AVG(v) OVER (
    PARTITION BY p
    ORDER BY ord
    ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
  ) AS avg_v
FROM wf_avg_p
ORDER BY p, ord;

DROP TEMPORARY TABLE wf_avg_p;
````

本批没有独立 expected JSON；预期行在上方 Stage 2 响应。自动汇总主要判断父/目标结果、错误与退出码是否相同，不能等同于首次逐检查点 oracle 审计。

### 执行环境、命令与三轮结果

#### 父提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/result.json)。精确 revision：`74c7ccfa27f482576412300e5f92fd3dbeb54cfa`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "74c7ccfa27f482576412300e5f92fd3dbeb54cfa",
  "runtime": "[redacted]",
  "mysqld_sha256": "9b1c7a6f60cd796f52d4462f05348f42ae4f35252d5a57d9073f819b0b4d4c0a",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_window_f_p_1",
      "started_at_epoch": 1793890909.491718,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890909.6229565
    },
    {
      "repeat": 2,
      "schema": "ds_window_f_p_2",
      "started_at_epoch": 1793890909.7234533,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890909.8506148
    },
    {
      "repeat": 3,
      "schema": "ds_window_f_p_3",
      "started_at_epoch": 1793890909.9478805,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890910.0670931
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/parent/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| p | ord | v | avg_v |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1.0000 |
| 1 | 2 | NULL | 1.0000 |
| 1 | 3 | 3 | 3.0000 |
| 1 | 4 | 5 | 4.0000 |
| 2 | 1 | 10 | 10.0000 |
| 2 | 2 | NULL | 10.0000 |
| 2 | 3 | NULL | NULL |
| 2 | 4 | 8 | 8.0000 |

#### 目标提交

执行元数据、完整命令（归档中有记录时）、schema、返回码及哈希：[result.json](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/result.json)。精确 revision：`c296cddb93ffc631f9b43d3b1ff769604e7469d7`。

以下为原件中的运行环境和逐轮命令/状态字段；不补造归档未提供的命令。

```json
{
  "revision": "c296cddb93ffc631f9b43d3b1ff769604e7469d7",
  "runtime": "[redacted]",
  "mysqld_sha256": "083a9cd4a3939ff10e3929804368397dd1e9997928f61e06be1f83041502de49",
  "startup_error": null,
  "container_removed": true,
  "trial_execution_metadata": [
    {
      "repeat": 1,
      "schema": "ds_window_f_t_1",
      "started_at_epoch": 1793890927.363939,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890927.4856834
    },
    {
      "repeat": 2,
      "schema": "ds_window_f_t_2",
      "started_at_epoch": 1793890927.643112,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890927.7788484
    },
    {
      "repeat": 3,
      "schema": "ds_window_f_t_3",
      "started_at_epoch": 1793890927.8775275,
      "returncode": 0,
      "stdout_sha256": "ce8dc91eaa18bdb7f6dd7b98d58afcd2cd8c5dd778155d50aa4d930c9e79e81e",
      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "stdout_bytes": 1416,
      "stderr_bytes": 0,
      "sql_errors": [],
      "xml_parse": "ok",
      "finished_at_epoch": 1793890928.0153866
    }
  ]
}
```

| 轮次 | 返回码 | XML 原件 | stderr 原件 |
|---|---|---|---|
| 1 | 0 | [trial-1.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-1.stdout.xml) | [trial-1.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-1.stderr.txt) |
| 2 | 0 | [trial-2.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-2.stdout.xml) | [trial-2.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-2.stderr.txt) |
| 3 | 0 | [trial-3.stdout.xml](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-3.stdout.xml) | [trial-3.stderr.txt](../prompt_pipeline_deepseek_20261105/server_evidence/results/window_frame_state_c296cddb93ff/target/trial-3.stderr.txt) |

第一轮完整结果集如下；第二、三轮原件见上表。首次包含检查点标签结果集，紧随其后的结果集为对应查询值。

结果集 1：

| p | ord | v | avg_v |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1.0000 |
| 1 | 2 | NULL | 1.0000 |
| 1 | 3 | 3 | 3.0000 |
| 1 | 4 | 5 | 4.0000 |
| 2 | 1 | 10 | 10.0000 |
| 2 | 2 | NULL | 10.0000 |
| 2 | 3 | NULL | NULL |
| 2 | 4 | 8 | 8.0000 |

判定与环境补充：[逐轮配对与二进制身份](../prompt_pipeline_deepseek_20261105/server_evidence/summary.json)、[参数及 run_id](../prompt_pipeline_deepseek_20261105/run_manifest.json)、[执行报告](../prompt_pipeline_deepseek_20261105/verification_report.md)。原始远端 runner 未公开，公开包不能还原其完整启动命令；其 SHA256 见导出清单。

