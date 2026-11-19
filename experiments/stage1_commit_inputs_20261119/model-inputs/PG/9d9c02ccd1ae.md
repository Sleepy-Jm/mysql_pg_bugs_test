# PostgreSQL 提交分析 · Stage 1

仅使用本文提供的代码和提交说明，为下一阶段的 PostgreSQL 查询正确性测试建立候选思路。请用中文交付以下内容。

1. 哪些 SQL 构造可能进入改动路径？从代码说明入口和分支条件，标出文件、函数或行号。
2. 到达后，哪些输入性质可能影响查询的可观察结果？区分源码直接支持的关系、尚待验证的推断，以及能够区分两者的对照。
3. 给出独立验证结果正确性的方法和仍缺少的证据。候选数量以证据为准，把完整可执行 SQL 留给下一阶段。路径被执行或两版结果不同，本身不足以认定查询结果有错。

## 提交身份与原始说明节选

数据库：PostgreSQL

第一父版本：2f4d0d67994b32320487784afab7ab997d331bb5

目标版本：9d9c02ccd1aea8e9131d8f4edb21bf1687e40782

~~~text
Teach planner and executor about monotonic window funcs

Window functions such as row_number() always return a value higher than
the previously returned value for tuples in any given window partition.

This is done by way of adding a pg_proc.prosupport function to various of
the built-in window functions and adding supporting code to allow the
support function to inform the planner if the window function is
monotonically increasing, monotonically decreasing, both or neither.  The
planner is then able to make use of that information and possibly allow
the executor to short-circuit execution by way of adding a "run condition"
to the WindowAgg to allow it to determine if some of its execution work
can be skipped.

This "run condition" is not like a normal filter.  These run conditions
are only built using quals comparing values to monotonic window functions.
For monotonic increasing functions, quals making use of the btree
operators for <, <= and = can be used (assuming the window function column
is on the left). You can see here that once such a condition becomes false
that a monotonic increasing function could never make it subsequently true
again.  For monotonically decreasing functions the >, >= and = btree
operators for the given type can be used for run conditions.

Here we add prosupport functions to allow the above to work for;
row_number(), rank(), dense_rank(), count(*) and count(expr).  It appears
technically possible to do the same for min() and max(), however, it seems
unlikely to be useful enough, so that's not done here.
~~~

## 相对第一父版本的生产差异

~~~diff
diff --git a/src/backend/commands/explain.c b/src/backend/commands/explain.c
index 1e5701b8eba8e..512b41dc3a2da 100644
--- a/src/backend/commands/explain.c
+++ b/src/backend/commands/explain.c
@@ -1988,6 +1988,14 @@ ExplainNode(PlanState *planstate, List *ancestors,
 				show_instrumentation_count("Rows Removed by Filter", 1,
 										   planstate, es);
 			break;
+		case T_WindowAgg:
+			show_upper_qual(plan->qual, "Filter", planstate, ancestors, es);
+			if (plan->qual)
+				show_instrumentation_count("Rows Removed by Filter", 1,
+										   planstate, es);
+			show_upper_qual(((WindowAgg *) plan)->runConditionOrig,
+							"Run Condition", planstate, ancestors, es);
+			break;
 		case T_Group:
 			show_group_keys(castNode(GroupState, planstate), ancestors, es);
 			show_upper_qual(plan->qual, "Filter", planstate, ancestors, es);
diff --git a/src/backend/executor/nodeWindowAgg.c b/src/backend/executor/nodeWindowAgg.c
index 08ce05ca5a6b5..4b104c4d98a61 100644
--- a/src/backend/executor/nodeWindowAgg.c
+++ b/src/backend/executor/nodeWindowAgg.c
@@ -1248,6 +1248,20 @@ spool_tuples(WindowAggState *winstate, int64 pos)
 	if (winstate->partition_spooled)
 		return;					/* whole partition done already */
 
+	/*
+	 * When in pass-through mode we can just exhaust all tuples in the current
+	 * partition.  We don't need these tuples for any further window function
+	 * evaluation, however, we do need to keep them around if we're not the
+	 * top-level window as another WindowAgg node above must see these.
+	 */
+	if (winstate->status != WINDOWAGG_RUN)
+	{
+		Assert(winstate->status == WINDOWAGG_PASSTHROUGH ||
+			   winstate->status == WINDOWAGG_PASSTHROUGH_STRICT);
+
+		pos = -1;
+	}
+
 	/*
 	 * If the tuplestore has spilled to disk, alternate reading and writing
 	 * becomes quite expensive due to frequent buffer flushes.  It's cheaper
@@ -1256,7 +1270,7 @@ spool_tuples(WindowAggState *winstate, int64 pos)
 	 * XXX this is a horrid kluge --- it'd be better to fix the performance
 	 * problem inside tuplestore.  FIXME
 	 */
-	if (!tuplestore_in_memory(winstate->buffer))
+	else if (!tuplestore_in_memory(winstate->buffer))
 		pos = -1;
 
 	outerPlan = outerPlanState(winstate);
@@ -1295,9 +1309,16 @@ spool_tuples(WindowAggState *winstate, int64 pos)
 			}
 		}
 
-		/* Still in partition, so save it into the tuplestore */
-		tuplestore_puttupleslot(winstate->buffer, outerslot);
-		winstate->spooled_rows++;
+		/*
+		 * Remember the tuple unless we're the top-level window and we're in
+		 * pass-through mode.
+		 */
+		if (winstate->status != WINDOWAGG_PASSTHROUGH_STRICT)
+		{
+			/* Still in partition, so save it into the tuplestore */
+			tuplestore_puttupleslot(winstate->buffer, outerslot);
+			winstate->spooled_rows++;
+		}
 	}
 
 	MemoryContextSwitchTo(oldcontext);
@@ -2023,13 +2044,14 @@ static TupleTableSlot *
 ExecWindowAgg(PlanState *pstate)
 {
 	WindowAggState *winstate = castNode(WindowAggState, pstate);
+	TupleTableSlot *slot;
 	ExprContext *econtext;
 	int			i;
 	int			numfuncs;
 
 	CHECK_FOR_INTERRUPTS();
 
-	if (winstate->all_done)
+	if (winstate->status == WINDOWAGG_DONE)
 		return NULL;
 
 	/*
@@ -2099,143 +2121,224 @@ ExecWindowAgg(PlanState *pstate)
 		winstate->all_first = false;
 	}
 
-	if (winstate->buffer == NULL)
-	{
-		/* Initialize for first partition and set current row = 0 */
-		begin_partition(winstate);
-		/* If there are no input rows, we'll detect that and exit below */
-	}
-	else
+	/* We need to loop as the runCondition or qual may filter out tuples */
+	for (;;)
 	{
-		/* Advance current row within partition */
-		winstate->currentpos++;
-		/* This might mean that the frame moves, too */
-		winstate->framehead_valid = false;
-		winstate->frametail_valid = false;
-		/* we don't need to invalidate grouptail here; see below */
-	}
+		if (winstate->buffer == NULL)
+		{
+			/* Initialize for first partition and set current row = 0 */
+			begin_partition(winstate);
+			/* If there are no input rows, we'll detect that and exit below */
+		}
+		else
+		{
+			/* Advance current row within partition */
+			winstate->currentpos++;
+			/* This might mean that the frame moves, too */
+			winstate->framehead_valid = false;
+			winstate->frametail_valid = false;
+			/* we don't need to invalidate grouptail here; see below */
+		}
 
-	/*
-	 * Spool all tuples up to and including the current row, if we haven't
-	 * already
-	 */
-	spool_tuples(winstate, winstate->currentpos);
+		/*
+		 * Spool all tuples up to and including the current row, if we haven't
+		 * already
+		 */
+		spool_tuples(winstate, winstate->currentpos);
 
-	/* Move to the next partition if we reached the end of this partition */
-	if (winstate->partition_spooled &&
-		winstate->currentpos >= winstate->spooled_rows)
-	{
-		release_partition(winstate);
+		/* Move to the next partition if we reached the end of this partition */
+		if (winstate->partition_spooled &&
+			winstate->currentpos >= winstate->spooled_rows)
+		{
+			release_partition(winstate);
+
+			if (winstate->more_partitions)
+			{
+				begin_partition(winstate);
+				Assert(winstate->spooled_rows > 0);
+
+				/* Come out of pass-through mode when changing partition */
+				winstate->status = WINDOWAGG_RUN;
+			}
+			else
+			{
+				/* No further partitions?  We're done */
+				winstate->status = WINDOWAGG_DONE;
+				return NULL;
+			}
+		}
+
+		/* final output execution is in ps_ExprContext */
+		econtext = winstate->ss.ps.ps_ExprContext;
+
+		/* Clear the per-output-tuple context for current row */
+		ResetExprContext(econtext);
 
-		if (winstate->more_partitions)
+		/*
+		 * Read the current row from the tuplestore, and save in
+		 * ScanTupleSlot. (We can't rely on the outerplan's output slot
+		 * because we may have to read beyond the current row.  Also, we have
+		 * to actually copy the row out of the tuplestore, since window
+		 * function evaluation might cause the tuplestore to dump its state to
+		 * disk.)
+		 *
+		 * In GROUPS mode, or when tracking a group-oriented exclusion clause,
+		 * we must also detect entering a new peer group and update associated
+		 * state when that happens.  We use temp_slot_2 to temporarily hold
+		 * the previous row for this purpose.
+		 *
+		 * Current row must be in the tuplestore, since we spooled it above.
+		 */
+		tuplestore_select_read_pointer(winstate->buffer, winstate->current_ptr);
+		if ((winstate->frameOptions & (FRAMEOPTION_GROUPS |
+									   FRAMEOPTION_EXCLUDE_GROUP |
+									   FRAMEOPTION_EXCLUDE_TIES)) &&
+			winstate->currentpos > 0)
 		{
-			begin_partition(winstate);
-			Assert(winstate->spooled_rows > 0);
+			ExecCopySlot(winstate->temp_slot_2, winstate->ss.ss_ScanTupleSlot);
+			if (!tuplestore_gettupleslot(winstate->buffer, true, true,
+										 winstate->ss.ss_ScanTupleSlot))
+				elog(ERROR, "unexpected end of tuplestore");
+			if (!are_peers(winstate, winstate->temp_slot_2,
+						   winstate->ss.ss_ScanTupleSlot))
+			{
+				winstate->currentgroup++;
+				winstate->groupheadpos = winstate->currentpos;
+				winstate->grouptail_valid = false;
+			}
+			ExecClearTuple(winstate->temp_slot_2);
 		}
 		else
 		{
-			winstate->all_done = true;
-			return NULL;
+			if (!tuplestore_gettupleslot(winstate->buffer, true, true,
+										 winstate->ss.ss_ScanTupleSlot))
+				elog(ERROR, "unexpected end of tuplestore");
 		}
-	}
 
-	/* final output execution is in ps_ExprContext */
-	econtext = winstate->ss.ps.ps_ExprContext;
+		/* don't evaluate the window functions when we're in pass-through mode */
+		if (winstate->status == WINDOWAGG_RUN)
+		{
+			/*
+			 * Evaluate true window functions
+			 */
+			numfuncs = winstate->numfuncs;
+			for (i = 0; i < numfuncs; i++)
+			{
+				WindowStatePerFunc perfuncstate = &(winstate->perfunc[i]);
 
-	/* Clear the per-output-tuple context for current row */
-	ResetExprContext(econtext);
+				if (perfuncstate->plain_agg)
+					continue;
+				eval_windowfunction(winstate, perfuncstate,
+									&(econtext->ecxt_aggvalues[perfuncstate->wfuncstate->wfuncno]),
+									&(econtext->ecxt_aggnulls[perfuncstate->wfuncstate->wfuncno]));
+			}
 
-	/*
-	 * Read the current row from the tuplestore, and save in ScanTupleSlot.
-	 * (We can't rely on the outerplan's output slot because we may have to
-	 * read beyond the current row.  Also, we have to actually copy the row
-	 * out of the tuplestore, since window function evaluation might cause the
-	 * tuplestore to dump its state to disk.)
-	 *
-	 * In GROUPS mode, or when tracking a group-oriented exclusion clause, we
-	 * must also detect entering a new peer group and update associated state
-	 * when that happens.  We use temp_slot_2 to temporarily hold the previous
-	 * row for this purpose.
-	 *
-	 * Current row must be in the tuplestore, since we spooled it above.
-	 */
-	tuplestore_select_read_pointer(winstate->buffer, winstate->current_ptr);
-	if ((winstate->frameOptions & (FRAMEOPTION_GROUPS |
-								   FRAMEOPTION_EXCLUDE_GROUP |
-								   FRAMEOPTION_EXCLUDE_TIES)) &&
-		winstate->currentpos > 0)
-	{
-		ExecCopySlot(winstate->temp_slot_2, winstate->ss.ss_ScanTupleSlot);
-		if (!tuplestore_gettupleslot(winstate->buffer, true, true,
-									 winstate->ss.ss_ScanTupleSlot))
-			elog(ERROR, "unexpected end of tuplestore");
-		if (!are_peers(winstate, winstate->temp_slot_2,
-					   winstate->ss.ss_ScanTupleSlot))
-		{
-			winstate->currentgroup++;
-			winstate->groupheadpos = winstate->currentpos;
-			winstate->grouptail_valid = false;
+			/*
+			 * Evaluate aggregates
+			 */
+			if (winstate->numaggs > 0)
+				eval_windowaggregates(winstate);
 		}
-		ExecClearTuple(winstate->temp_slot_2);
-	}
-	else
-	{
-		if (!tuplestore_gettupleslot(winstate->buffer, true, true,
-									 winstate->ss.ss_ScanTupleSlot))
-			elog(ERROR, "unexpected end of tuplestore");
-	}
 
-	/*
-	 * Evaluate true window functions
-	 */
-	numfuncs = winstate->numfuncs;
-	for (i = 0; i < numfuncs; i++)
-	{
-		WindowStatePerFunc perfuncstate = &(winstate->perfunc[i]);
+		/*
+		 * If we have created auxiliary read pointers for the frame or group
+		 * boundaries, force them to be kept up-to-date, because we don't know
+		 * whether the window function(s) will do anything that requires that.
+		 * Failing to advance the pointers would result in being unable to
+		 * trim data from the tuplestore, which is bad.  (If we could know in
+		 * advance whether the window functions will use frame boundary info,
+		 * we could skip creating these pointers in the first place ... but
+		 * unfortunately the window function API doesn't require that.)
+		 */
+		if (winstate->framehead_ptr >= 0)
+			update_frameheadpos(winstate);
+		if (winstate->frametail_ptr >= 0)
+			update_frametailpos(winstate);
+		if (winstate->grouptail_ptr >= 0)
+			update_grouptailpos(winstate);
 
-		if (perfuncstate->plain_agg)
-			continue;
-		eval_windowfunction(winstate, perfuncstate,
-							&(econtext->ecxt_aggvalues[perfuncstate->wfuncstate->wfuncno]),
-							&(econtext->ecxt_aggnulls[perfuncstate->wfuncstate->wfuncno]));
-	}
+		/*
+		 * Truncate any no-longer-needed rows from the tuplestore.
+		 */
+		tuplestore_trim(winstate->buffer);
 
-	/*
-	 * Evaluate aggregates
-	 */
-	if (winstate->numaggs > 0)
-		eval_windowaggregates(winstate);
+		/*
+		 * Form and return a projection tuple using the windowfunc results and
+		 * the current row.  Setting ecxt_outertuple arranges that any Vars
+		 * will be evaluated with respect to that row.
+		 */
+		econtext->ecxt_outertuple = winstate->ss.ss_ScanTupleSlot;
 
-	/*
-	 * If we have created auxiliary read pointers for the frame or group
-	 * boundaries, force them to be kept up-to-date, because we don't know
-	 * whether the window function(s) will do anything that requires that.
-	 * Failing to advance the pointers would result in being unable to trim
-	 * data from the tuplestore, which is bad.  (If we could know in advance
-	 * whether the window functions will use frame boundary info, we could
-	 * skip creating these pointers in the first place ... but unfortunately
-	 * the window function API doesn't require that.)
-	 */
-	if (winstate->framehead_ptr >= 0)
-		update_frameheadpos(winstate);
-	if (winstate->frametail_ptr >= 0)
-		update_frametailpos(winstate);
-	if (winstate->grouptail_ptr >= 0)
-		update_grouptailpos(winstate);
+		slot = ExecProject(winstate->ss.ps.ps_ProjInfo);
 
-	/*
-	 * Truncate any no-longer-needed rows from the tuplestore.
-	 */
-	tuplestore_trim(winstate->buffer);
+		if (winstate->status == WINDOWAGG_RUN)
+		{
+			econtext->ecxt_scantuple = slot;
 
-	/*
-	 * Form and return a projection tuple using the windowfunc results and the
-	 * current row.  Setting ecxt_outertuple arranges that any Vars will be
-	 * evaluated with respect to that row.
-	 */
-	econtext->ecxt_outertuple = winstate->ss.ss_ScanTupleSlot;
+			/*
+			 * Now evaluate the run condition to see if we need to go into
+			 * pass-through mode, or maybe stop completely.
+			 */
+			if (!ExecQual(winstate->runcondition, econtext))
+			{
+				/*
+				 * Determine which mode to move into.  If there is no
+				 * PARTITION BY clause and we're the top-level WindowAgg then
+				 * we're done.  This tuple and any future tuples cannot
+				 * possibly match the runcondition.  However, when there is a
+				 * PARTITION BY clause or we're not the top-level window we
+				 * can't just stop as we need to either process other
+				 * partitions or ensure WindowAgg nodes above us receive all
+				 * of the tuples they need to process their WindowFuncs.
+				 */
+				if (winstate->use_pass_through)
+				{
+					/*
+					 * STRICT pass-through mode is required for the top window
+					 * when there is a PARTITION BY clause.  Otherwise we must
+					 * ensure we store tuples that don't match the
+					 * runcondition so they're available to WindowAggs above.
+					 */
+					if (winstate->top_window)
+					{
+						winstate->status = WINDOWAGG_PASSTHROUGH_STRICT;
+						continue;
+					}
+					else
+						winstate->status = WINDOWAGG_PASSTHROUGH;
+				}
+				else
+				{
+					/*
+					 * Pass-through not required.  We can just return NULL.
+					 * Nothing else will match the runcondition.
+					 */
+					winstate->status = WINDOWAGG_DONE;
+					return NULL;
+				}
+			}
 
-	return ExecProject(winstate->ss.ps.ps_ProjInfo);
+			/*
+			 * Filter out any tuples we don't need in the top-level WindowAgg.
+			 */
+			if (!ExecQual(winstate->ss.ps.qual, econtext))
+			{
+				InstrCountFiltered1(winstate, 1);
+				continue;
+			}
+
+			break;
+		}
+
+		/*
+		 * When not in WINDOWAGG_RUN mode, we must still return this tuple if
+		 * we're anything apart from the top window.
+		 */
+		else if (!winstate->top_window)
+			break;
+	}
+
+	return slot;
 }
 
 /* -----------------
@@ -2300,12 +2403,32 @@ ExecInitWindowAgg(WindowAgg *node, EState *estate, int eflags)
 							  "WindowAgg Aggregates",
 							  ALLOCSET_DEFAULT_SIZES);
 
+	/* Only the top-level WindowAgg may have a qual */
+	Assert(node->plan.qual == NIL || node->topWindow);
+
+	/* Initialize the qual */
+	winstate->ss.ps.qual = ExecInitQual(node->plan.qual,
+										(PlanState *) winstate);
+
+	/*
+	 * Setup the run condition, if we received one from the query planner.
+	 * When set, this may allow us to move into pass-through mode so that we
+	 * don't have to perform any further evaluation of WindowFuncs in the
+	 * current partition or possibly stop returning tuples altogether when all
+	 * tuples are in the same partition.
+	 */
+	winstate->runcondition = ExecInitQual(node->runCondition,
+										  (PlanState *) winstate);
+
 	/*
-	 * WindowAgg nodes never have quals, since they can only occur at the
-	 * logical top level of a query (ie, after any WHERE or HAVING filters)
+	 * When we're not the top-level WindowAgg node or we are but have a
+	 * PARTITION BY clause we must move into one of the WINDOWAGG_PASSTHROUGH*
+	 * modes when the runCondition becomes false.
 	 */
-	Assert(node->plan.qual == NIL);
-	winstate->ss.ps.qual = NULL;
+	winstate->use_pass_through = !node->topWindow || node->partNumCols > 0;
+
+	/* remember if we're the top-window or we are below the top-window */
+	winstate->top_window = node->topWindow;
 
 	/*
 	 * initialize child nodes
@@ -2500,6 +2623,9 @@ ExecInitWindowAgg(WindowAgg *node, EState *estate, int eflags)
 		winstate->agg_winobj = agg_winobj;
 	}
 
+	/* Set the status to running */
+	winstate->status = WINDOWAGG_RUN;
+
 	/* copy frame options to state node for easy access */
 	winstate->frameOptions = frameOptions;
 
@@ -2579,7 +2705,7 @@ ExecReScanWindowAgg(WindowAggState *node)
 	PlanState  *outerPlan = outerPlanState(node);
 	ExprContext *econtext = node->ss.ps.ps_ExprContext;
 
-	node->all_done = false;
+	node->status = WINDOWAGG_RUN;
 	node->all_first = true;
 
 	/* release tuplestore et al */
diff --git a/src/backend/nodes/copyfuncs.c b/src/backend/nodes/copyfuncs.c
index 1585cf2d58ceb..836f427ea8f68 100644
--- a/src/backend/nodes/copyfuncs.c
+++ b/src/backend/nodes/copyfuncs.c
@@ -1104,11 +1104,14 @@ _copyWindowAgg(const WindowAgg *from)
 	COPY_SCALAR_FIELD(frameOptions);
 	COPY_NODE_FIELD(startOffset);
 	COPY_NODE_FIELD(endOffset);
+	COPY_NODE_FIELD(runCondition);
+	COPY_NODE_FIELD(runConditionOrig);
 	COPY_SCALAR_FIELD(startInRangeFunc);
 	COPY_SCALAR_FIELD(endInRangeFunc);
 	COPY_SCALAR_FIELD(inRangeColl);
 	COPY_SCALAR_FIELD(inRangeAsc);
 	COPY_SCALAR_FIELD(inRangeNullsFirst);
+	COPY_SCALAR_FIELD(topWindow);
 
 	return newnode;
 }
@@ -3061,6 +3064,7 @@ _copyWindowClause(const WindowClause *from)
 	COPY_SCALAR_FIELD(frameOptions);
 	COPY_NODE_FIELD(startOffset);
 	COPY_NODE_FIELD(endOffset);
+	COPY_NODE_FIELD(runCondition);
 	COPY_SCALAR_FIELD(startInRangeFunc);
 	COPY_SCALAR_FIELD(endInRangeFunc);
 	COPY_SCALAR_FIELD(inRangeColl);
diff --git a/src/backend/nodes/equalfuncs.c b/src/backend/nodes/equalfuncs.c
index caad20e047816..e013c1bbfed01 100644
--- a/src/backend/nodes/equalfuncs.c
+++ b/src/backend/nodes/equalfuncs.c
@@ -3234,6 +3234,7 @@ _equalWindowClause(const WindowClause *a, const WindowClause *b)
 	COMPARE_SCALAR_FIELD(frameOptions);
 	COMPARE_NODE_FIELD(startOffset);
 	COMPARE_NODE_FIELD(endOffset);
+	COMPARE_NODE_FIELD(runCondition);
 	COMPARE_SCALAR_FIELD(startInRangeFunc);
 	COMPARE_SCALAR_FIELD(endInRangeFunc);
 	COMPARE_SCALAR_FIELD(inRangeColl);
diff --git a/src/backend/nodes/outfuncs.c b/src/backend/nodes/outfuncs.c
index 13e16435303cb..d5f5e76c5593e 100644
--- a/src/backend/nodes/outfuncs.c
+++ b/src/backend/nodes/outfuncs.c
@@ -829,11 +829,14 @@ _outWindowAgg(StringInfo str, const WindowAgg *node)
 	WRITE_INT_FIELD(frameOptions);
 	WRITE_NODE_FIELD(startOffset);
 	WRITE_NODE_FIELD(endOffset);
+	WRITE_NODE_FIELD(runCondition);
+	WRITE_NODE_FIELD(runConditionOrig);
 	WRITE_OID_FIELD(startInRangeFunc);
 	WRITE_OID_FIELD(endInRangeFunc);
 	WRITE_OID_FIELD(inRangeColl);
 	WRITE_BOOL_FIELD(inRangeAsc);
 	WRITE_BOOL_FIELD(inRangeNullsFirst);
+	WRITE_BOOL_FIELD(topWindow);
 }
 
 static void
@@ -2283,6 +2286,8 @@ _outWindowAggPath(StringInfo str, const WindowAggPath *node)
 
 	WRITE_NODE_FIELD(subpath);
 	WRITE_NODE_FIELD(winclause);
+	WRITE_NODE_FIELD(qual);
+	WRITE_BOOL_FIELD(topwindow);
 }
 
 static void
@@ -3293,6 +3298,7 @@ _outWindowClause(StringInfo str, const WindowClause *node)
 	WRITE_INT_FIELD(frameOptions);
 	WRITE_NODE_FIELD(startOffset);
 	WRITE_NODE_FIELD(endOffset);
+	WRITE_NODE_FIELD(runCondition);
 	WRITE_OID_FIELD(startInRangeFunc);
 	WRITE_OID_FIELD(endInRangeFunc);
 	WRITE_OID_FIELD(inRangeColl);
diff --git a/src/backend/nodes/readfuncs.c b/src/backend/nodes/readfuncs.c
index 48f7216c9eda3..3d150cb25db6b 100644
--- a/src/backend/nodes/readfuncs.c
+++ b/src/backend/nodes/readfuncs.c
@@ -384,6 +384,7 @@ _readWindowClause(void)
 	READ_INT_FIELD(frameOptions);
 	READ_NODE_FIELD(startOffset);
 	READ_NODE_FIELD(endOffset);
+	READ_NODE_FIELD(runCondition);
 	READ_OID_FIELD(startInRangeFunc);
 	READ_OID_FIELD(endInRangeFunc);
 	READ_OID_FIELD(inRangeColl);
@@ -2576,11 +2577,14 @@ _readWindowAgg(void)
 	READ_INT_FIELD(frameOptions);
 	READ_NODE_FIELD(startOffset);
 	READ_NODE_FIELD(endOffset);
+	READ_NODE_FIELD(runCondition);
+	READ_NODE_FIELD(runConditionOrig);
 	READ_OID_FIELD(startInRangeFunc);
 	READ_OID_FIELD(endInRangeFunc);
 	READ_OID_FIELD(inRangeColl);
 	READ_BOOL_FIELD(inRangeAsc);
 	READ_BOOL_FIELD(inRangeNullsFirst);
+	READ_BOOL_FIELD(topWindow);
 
 	READ_DONE();
 }
diff --git a/src/backend/optimizer/path/allpaths.c b/src/backend/optimizer/path/allpaths.c
index 169b1d53fc845..998212dda8f16 100644
--- a/src/backend/optimizer/path/allpaths.c
+++ b/src/backend/optimizer/path/allpaths.c
@@ -27,6 +27,7 @@
 #include "miscadmin.h"
 #include "nodes/makefuncs.h"
 #include "nodes/nodeFuncs.h"
+#include "nodes/supportnodes.h"
 #ifdef OPTIMIZER_DEBUG
 #include "nodes/print.h"
 #endif
@@ -2157,6 +2158,269 @@ has_multiple_baserels(PlannerInfo *root)
 	return false;
 }
 
+/*
+ * find_window_run_conditions
+ *		Determine if 'wfunc' is really a WindowFunc and call its prosupport
+ *		function to determine the function's monotonic properties.  We then
+ *		see if 'opexpr' can be used to short-circuit execution.
+ *
+ * For example row_number() over (order by ...) always produces a value one
+ * higher than the previous.  If someone has a window function in a subquery
+ * and has a WHERE clause in the outer query to filter rows <= 10, then we may
+ * as well stop processing the windowagg once the row number reaches 11.  Here
+ * we check if 'opexpr' might help us to stop doing needless extra processing
+ * in WindowAgg nodes.
+ *
+ * '*keep_original' is set to true if the caller should also use 'opexpr' for
+ * its original purpose.  This is set to false if the caller can assume that
+ * the run condition will handle all of the required filtering.
+ *
+ * Returns true if 'opexpr' was found to be useful and was added to the
+ * WindowClauses runCondition. We also set *keep_original accordingly.
+ * If the 'opexpr' cannot be used then we set *keep_original to true and
+ * return false.
+ */
+static bool
+find_window_run_conditions(Query *subquery, RangeTblEntry *rte, Index rti,
+						   AttrNumber attno, WindowFunc *wfunc, OpExpr *opexpr,
+						   bool wfunc_left, bool *keep_original)
+{
+	Oid			prosupport;
+	Expr	   *otherexpr;
+	SupportRequestWFuncMonotonic req;
+	SupportRequestWFuncMonotonic *res;
+	WindowClause *wclause;
+	List	   *opinfos;
+	OpExpr	   *runopexpr;
+	Oid			runoperator;
+	ListCell   *lc;
+
+	*keep_original = true;
+
+	while (IsA(wfunc, RelabelType))
+		wfunc = (WindowFunc *) ((RelabelType *) wfunc)->arg;
+
+	/* we can only work with window functions */
+	if (!IsA(wfunc, WindowFunc))
+		return false;
+
+	prosupport = get_func_support(wfunc->winfnoid);
+
+	/* Check if there's a support function for 'wfunc' */
+	if (!OidIsValid(prosupport))
+		return false;
+
+	/* get the Expr from the other side of the OpExpr */
+	if (wfunc_left)
+		otherexpr = lsecond(opexpr->args);
+	else
+		otherexpr = linitial(opexpr->args);
+
+	/*
+	 * The value being compared must not change during the evaluation of the
+	 * window partition.
+	 */
+	if (!is_pseudo_constant_clause((Node *) otherexpr))
+		return false;
+
+	/* find the window clause belonging to the window function */
+	wclause = (WindowClause *) list_nth(subquery->windowClause,
+										wfunc->winref - 1);
+
+	req.type = T_SupportRequestWFuncMonotonic;
+	req.window_func = wfunc;
+	req.window_clause = wclause;
+
+	/* call the support function */
+	res = (SupportRequestWFuncMonotonic *)
+		DatumGetPointer(OidFunctionCall1(prosupport,
+										 PointerGetDatum(&req)));
+
+	/*
+	 * Nothing to do if the function is neither monotonically increasing nor
+	 * monotonically decreasing.
+	 */
+	if (res == NULL || res->monotonic == MONOTONICFUNC_NONE)
+		return false;
+
+	runopexpr = NULL;
+	runoperator = InvalidOid;
+	opinfos = get_op_btree_interpretation(opexpr->opno);
+
+	foreach(lc, opinfos)
+	{
+		OpBtreeInterpretation *opinfo = (OpBtreeInterpretation *) lfirst(lc);
+		int			strategy = opinfo->strategy;
+
+		/* handle < / <= */
+		if (strategy == BTLessStrategyNumber ||
+			strategy == BTLessEqualStrategyNumber)
+		{
+			/*
+			 * < / <= is supported for monotonically increasing functions in
+			 * the form <wfunc> op <pseudoconst> and <pseudoconst> op <wfunc>
+			 * for monotonically decreasing functions.
+			 */
+			if ((wfunc_left && (res->monotonic & MONOTONICFUNC_INCREASING)) ||
+				(!wfunc_left && (res->monotonic & MONOTONICFUNC_DECREASING)))
+			{
+				*keep_original = false;
+				runopexpr = opexpr;
+				runoperator = opexpr->opno;
+			}
+			break;
+		}
+		/* handle > / >= */
+		else if (strategy == BTGreaterStrategyNumber ||
+				 strategy == BTGreaterEqualStrategyNumber)
+		{
+			/*
+			 * > / >= is supported for monotonically decreasing functions in
+			 * the form <wfunc> op <pseudoconst> and <pseudoconst> op <wfunc>
+			 * for monotonically increasing functions.
+			 */
+			if ((wfunc_left && (res->monotonic & MONOTONICFUNC_DECREASING)) ||
+				(!wfunc_left && (res->monotonic & MONOTONICFUNC_INCREASING)))
+			{
+				*keep_original = false;
+				runopexpr = opexpr;
+				runoperator = opexpr->opno;
+			}
+			break;
+		}
+		/* handle = */
+		else if (strategy == BTEqualStrategyNumber)
+		{
+			int16		newstrategy;
+
+			/*
+			 * When both monotonically increasing and decreasing then the
+			 * return value of the window function will be the same each time.
+			 * We can simply use 'opexpr' as the run condition without
+			 * modifying it.
+			 */
+			if ((res->monotonic & MONOTONICFUNC_BOTH) == MONOTONICFUNC_BOTH)
+			{
+				*keep_original = false;
+				runopexpr = opexpr;
+				break;
+			}
+
+			/*
+			 * When monotonically increasing we make a qual with <wfunc> <=
+			 * <value> or <value> >= <wfunc> in order to filter out values
+			 * which are above the value in the equality condition.  For
+			 * monotonically decreasing functions we want to filter values
+			 * below the value in the equality condition.
+			 */
+			if (res->monotonic & MONOTONICFUNC_INCREASING)
+				newstrategy = wfunc_left ? BTLessEqualStrategyNumber : BTGreaterEqualStrategyNumber;
+			else
+				newstrategy = wfunc_left ? BTGreaterEqualStrategyNumber : BTLessEqualStrategyNumber;
+
+			/* We must keep the original equality qual */
+			*keep_original = true;
+			runopexpr = opexpr;
+
+			/* determine the operator to use for the runCondition qual */
+			runoperator = get_opfamily_member(opinfo->opfamily_id,
+											  opinfo->oplefttype,
+											  opinfo->oprighttype,
+											  newstrategy);
+			break;
+		}
+	}
+
+	if (runopexpr != NULL)
+	{
+		Expr	   *newexpr;
+
+		/*
+		 * Build the qual required for the run condition keeping the
+		 * WindowFunc on the same side as it was originally.
+		 */
+		if (wfunc_left)
+			newexpr = make_opclause(runoperator,
+									runopexpr->opresulttype,
+									runopexpr->opretset, (Expr *) wfunc,
+									otherexpr, runopexpr->opcollid,
+									runopexpr->inputcollid);
+		else
+			newexpr = make_opclause(runoperator,
+									runopexpr->opresulttype,
+									runopexpr->opretset,
+									otherexpr, (Expr *) wfunc,
+									runopexpr->opcollid,
+									runopexpr->inputcollid);
+
+		wclause->runCondition = lappend(wclause->runCondition, newexpr);
+
+		return true;
+	}
+
+	/* unsupported OpExpr */
+	return false;
+}
+
+/*
+ * check_and_push_window_quals
+ *		Check if 'clause' is a qual that can be pushed into a WindowFunc's
+ *		WindowClause as a 'runCondition' qual.  These, when present, allow
+ *		some unnecessary work to be skipped during execution.
+ *
+ * Returns true if the caller still must keep the original qual or false if
+ * the caller can safely ignore the original qual because the WindowAgg node
+ * will use the runCondition to stop returning tuples.
+ */
+static bool
+check_and_push_window_quals(Query *subquery, RangeTblEntry *rte, Index rti,
+							Node *clause)
+{
+	OpExpr	   *opexpr = (OpExpr *) clause;
+	bool		keep_original = true;
+	Var		   *var1;
+	Var		   *var2;
+
+	/* We're only able to use OpExprs with 2 operands */
+	if (!IsA(opexpr, OpExpr))
+		return true;
+
+	if (list_length(opexpr->args) != 2)
+		return true;
+
+	/*
+	 * Check for plain Vars that reference window functions in the subquery.
+	 * If we find any, we'll ask find_window_run_conditions() if 'opexpr' can
+	 * be used as part of the run condition.
+	 */
+
+	/* Check the left side of the OpExpr */
+	var1 = linitial(opexpr->args);
+	if (IsA(var1, Var) && var1->varattno > 0)
+	{
+		TargetEntry *tle = list_nth(subquery->targetList, var1->varattno - 1);
+		WindowFunc *wfunc = (WindowFunc *) tle->expr;
+
+		if (find_window_run_conditions(subquery, rte, rti, tle->resno, wfunc,
+									   opexpr, true, &keep_original))
+			return keep_original;
+	}
+
+	/* and check the right side */
+	var2 = lsecond(opexpr->args);
+	if (IsA(var2, Var) && var2->varattno > 0)
+	{
+		TargetEntry *tle = list_nth(subquery->targetList, var2->varattno - 1);
+		WindowFunc *wfunc = (WindowFunc *) tle->expr;
+
+		if (find_window_run_conditions(subquery, rte, rti, tle->resno, wfunc,
+									   opexpr, false, &keep_original))
+			return keep_original;
+	}
+
+	return true;
+}
+
 /*
  * set_subquery_pathlist
  *		Generate SubqueryScan access paths for a subquery RTE
@@ -2245,19 +2509,31 @@ set_subquery_pathlist(PlannerInfo *root, RelOptInfo *rel,
 		foreach(l, rel->baserestrictinfo)
 		{
 			RestrictInfo *rinfo = (RestrictInfo *) lfirst(l);
+			Node	   *clause = (Node *) rinfo->clause;
 
 			if (!rinfo->pseudoconstant &&
 				qual_is_pushdown_safe(subquery, rti, rinfo, &safetyInfo))
 			{
-				Node	   *clause = (Node *) rinfo->clause;
-
 				/* Push it down */
 				subquery_push_qual(subquery, rte, rti, clause);
 			}
 			else
 			{
-				/* Keep it in the upper query */
-				upperrestrictlist = lappend(upperrestrictlist, rinfo);
+				/*
+				 * Since we can't push the qual down into the subquery, check
+				 * if it happens to reference a window function.  If so then
+				 * it might be useful to use for the WindowAgg's runCondition.
+				 */
+				if (!subquery->hasWindowFuncs ||
+					check_and_push_window_quals(subquery, rte, rti, clause))
+				{
+					/*
+					 * subquery has no window funcs or the clause is not a
+					 * suitable window run condition qual or it is, but the
+					 * original must also be kept in the upper query.
+					 */
+					upperrestrictlist = lappend(upperrestrictlist, rinfo);
+				}
 			}
 		}
 		rel->baserestrictinfo = upperrestrictlist;
diff --git a/src/backend/optimizer/plan/createplan.c b/src/backend/optimizer/plan/createplan.c
index 51591bb8128ac..95476ada0ba69 100644
--- a/src/backend/optimizer/plan/createplan.c
+++ b/src/backend/optimizer/plan/createplan.c
@@ -288,6 +288,7 @@ static WindowAgg *make_windowagg(List *tlist, Index winref,
 								 int frameOptions, Node *startOffset, Node *endOffset,
 								 Oid startInRangeFunc, Oid endInRangeFunc,
 								 Oid inRangeColl, bool inRangeAsc, bool inRangeNullsFirst,
+								 List *runCondition, List *qual, bool topWindow,
 								 Plan *lefttree);
 static Group *make_group(List *tlist, List *qual, int numGroupCols,
 						 AttrNumber *grpColIdx, Oid *grpOperators, Oid *grpCollations,
@@ -2672,6 +2673,9 @@ create_windowagg_plan(PlannerInfo *root, WindowAggPath *best_path)
 						  wc->inRangeColl,
 						  wc->inRangeAsc,
 						  wc->inRangeNullsFirst,
+						  wc->runCondition,
+						  best_path->qual,
+						  best_path->topwindow,
 						  subplan);
 
 	copy_generic_path_info(&plan->plan, (Path *) best_path);
@@ -6558,7 +6562,7 @@ make_windowagg(List *tlist, Index winref,
 			   int frameOptions, Node *startOffset, Node *endOffset,
 			   Oid startInRangeFunc, Oid endInRangeFunc,
 			   Oid inRangeColl, bool inRangeAsc, bool inRangeNullsFirst,
-			   Plan *lefttree)
+			   List *runCondition, List *qual, bool topWindow, Plan *lefttree)
 {
 	WindowAgg  *node = makeNode(WindowAgg);
 	Plan	   *plan = &node->plan;
@@ -6575,17 +6579,20 @@ make_windowagg(List *tlist, Index winref,
 	node->frameOptions = frameOptions;
 	node->startOffset = startOffset;
 	node->endOffset = endOffset;
+	node->runCondition = runCondition;
+	/* a duplicate of the above for EXPLAIN */
+	node->runConditionOrig = runCondition;
 	node->startInRangeFunc = startInRangeFunc;
 	node->endInRangeFunc = endInRangeFunc;
 	node->inRangeColl = inRangeColl;
 	node->inRangeAsc = inRangeAsc;
 	node->inRangeNullsFirst = inRangeNullsFirst;
+	node->topWindow = topWindow;
 
 	plan->targetlist = tlist;
 	plan->lefttree = lefttree;
 	plan->righttree = NULL;
-	/* WindowAgg nodes never have a qual clause */
-	plan->qual = NIL;
+	plan->qual = qual;
 
 	return node;
 }
diff --git a/src/backend/optimizer/plan/planner.c b/src/backend/optimizer/plan/planner.c
index b2569c5d0c7dd..b090b087e9550 100644
--- a/src/backend/optimizer/plan/planner.c
+++ b/src/backend/optimizer/plan/planner.c
@@ -4190,6 +4190,7 @@ create_one_window_path(PlannerInfo *root,
 {
 	PathTarget *window_target;
 	ListCell   *l;
+	List	   *topqual = NIL;
 
 	/*
 	 * Since each window clause could require a different sort order, we stack
@@ -4214,6 +4215,7 @@ create_one_window_path(PlannerInfo *root,
 		List	   *window_pathkeys;
 		int			presorted_keys;
 		bool		is_sorted;
+		bool		topwindow;
 
 		window_pathkeys = make_pathkeys_for_window(root,
 												   wc,
@@ -4277,10 +4279,21 @@ create_one_window_path(PlannerInfo *root,
 			window_target = output_target;
 		}
 
+		/* mark the final item in the list as the top-level window */
+		topwindow = foreach_current_index(l) == list_length(activeWindows) - 1;
+
+		/*
+		 * Accumulate all of the runConditions from each intermediate
+		 * WindowClause.  The top-level WindowAgg must pass these as a qual so
+		 * that it filters out unwanted tuples correctly.
+		 */
+		if (!topwindow)
+			topqual = list_concat(topqual, wc->runCondition);
+
 		path = (Path *)
 			create_windowagg_path(root, window_rel, path, window_target,
 								  wflists->windowFuncs[wc->winref],
-								  wc);
+								  wc, topwindow ? topqual : NIL, topwindow);
 	}
 
 	add_path(window_rel, path);
diff --git a/src/backend/optimizer/plan/setrefs.c b/src/backend/optimizer/plan/setrefs.c
index 7519723081da2..6ea35056465c9 100644
--- a/src/backend/optimizer/plan/setrefs.c
+++ b/src/backend/optimizer/plan/setrefs.c
@@ -71,6 +71,13 @@ typedef struct
 	double		num_exec;
 } fix_upper_expr_context;
 
+typedef struct
+{
+	PlannerInfo *root;
+	indexed_tlist *subplan_itlist;
+	int			newvarno;
+} fix_windowagg_cond_context;
+
 /*
  * Selecting the best alternative in an AlternativeSubPlan expression requires
  * estimating how many times that expression will be evaluated.  For an
@@ -171,6 +178,9 @@ static List *set_returning_clause_references(PlannerInfo *root,
 											 Plan *topplan,
 											 Index resultRelation,
 											 int rtoffset);
+static List *set_windowagg_runcondition_references(PlannerInfo *root,
+												   List *runcondition,
+												   Plan *plan);
 
 
 /*****************************************************************************
@@ -885,6 +895,18 @@ set_plan_refs(PlannerInfo *root, Plan *plan, int rtoffset)
 			{
 				WindowAgg  *wplan = (WindowAgg *) plan;
 
+				/*
+				 * Adjust the WindowAgg's run conditions by swapping the
+				 * WindowFuncs references out to instead reference the Var in
+				 * the scan slot so that when the executor evaluates the
+				 * runCondition, it receives the WindowFunc's value from the
+				 * slot that the result has just been stored into rather than
+				 * evaluating the WindowFunc all over again.
+				 */
+				wplan->runCondition = set_windowagg_runcondition_references(root,
+																			wplan->runCondition,
+																			(Plan *) wplan);
+
 				set_upper_references(root, plan, rtoffset);
 
 				/*
@@ -896,6 +918,14 @@ set_plan_refs(PlannerInfo *root, Plan *plan, int rtoffset)
 					fix_scan_expr(root, wplan->startOffset, rtoffset, 1);
 				wplan->endOffset =
 					fix_scan_expr(root, wplan->endOffset, rtoffset, 1);
+				wplan->runCondition = fix_scan_list(root,
+													wplan->runCondition,
+													rtoffset,
+													NUM_EXEC_TLIST(plan));
+				wplan->runConditionOrig = fix_scan_list(root,
+														wplan->runConditionOrig,
+														rtoffset,
+														NUM_EXEC_TLIST(plan));
 			}
 			break;
 		case T_Result:
@@ -3064,6 +3094,78 @@ set_returning_clause_references(PlannerInfo *root,
 	return rlist;
 }
 
+/*
+ * fix_windowagg_condition_expr_mutator
+ *		Mutator function for replacing WindowFuncs with the corresponding Var
+ *		in the targetlist which references that WindowFunc.
+ */
+static Node *
+fix_windowagg_condition_expr_mutator(Node *node,
+									 fix_windowagg_cond_context *context)
+{
+	if (node == NULL)
+		return NULL;
+
+	if (IsA(node, WindowFunc))
+	{
+		Var		   *newvar;
+
+		newvar = search_indexed_tlist_for_non_var((Expr *) node,
+												  context->subplan_itlist,
+												  context->newvarno);
+		if (newvar)
+			return (Node *) newvar;
+		elog(ERROR, "WindowFunc not found in subplan target lists");
+	}
+
+	return expression_tree_mutator(node,
+								   fix_windowagg_condition_expr_mutator,
+								   (void *) context);
+}
+
+/*
+ * fix_windowagg_condition_expr
+ *		Converts references in 'runcondition' so that any WindowFunc
+ *		references are swapped out for a Var which references the matching
+ *		WindowFunc in 'subplan_itlist'.
+ */
+static List *
+fix_windowagg_condition_expr(PlannerInfo *root,
+							 List *runcondition,
+							 indexed_tlist *subplan_itlist)
+{
+	fix_windowagg_cond_context context;
+
+	context.root = root;
+	context.subplan_itlist = subplan_itlist;
+	context.newvarno = 0;
+
+	return (List *) fix_windowagg_condition_expr_mutator((Node *) runcondition,
+														 &context);
+}
+
+/*
+ * set_windowagg_runcondition_references
+ *		Converts references in 'runcondition' so that any WindowFunc
+ *		references are swapped out for a Var which references the matching
+ *		WindowFunc in 'plan' targetlist.
+ */
+static List *
+set_windowagg_runcondition_references(PlannerInfo *root,
+									  List *runcondition,
+									  Plan *plan)
+{
+	List	   *newlist;
+	indexed_tlist *itlist;
+
+	itlist = build_tlist_index(plan->targetlist);
+
+	newlist = fix_windowagg_condition_expr(root, runcondition, itlist);
+
+	pfree(itlist);
+
+	return newlist;
+}
 
 /*****************************************************************************
  *					QUERY DEPENDENCY MANAGEMENT
diff --git a/src/backend/optimizer/util/pathnode.c b/src/backend/optimizer/util/pathnode.c
index 1670e5464406b..e2a3c110ce7ec 100644
--- a/src/backend/optimizer/util/pathnode.c
+++ b/src/backend/optimizer/util/pathnode.c
@@ -3388,6 +3388,10 @@ create_minmaxagg_path(PlannerInfo *root,
  * 'target' is the PathTarget to be computed
  * 'windowFuncs' is a list of WindowFunc structs
  * 'winclause' is a WindowClause that is common to all the WindowFuncs
+ * 'qual' WindowClause.runconditions from lower-level WindowAggPaths.
+ *		Must always be NIL when topwindow == false
+ * 'topwindow' pass as true only for the top-level WindowAgg. False for all
+ *		intermediate WindowAggs.
  *
  * The input must be sorted according to the WindowClause's PARTITION keys
  * plus ORDER BY keys.
@@ -3398,10 +3402,15 @@ create_windowagg_path(PlannerInfo *root,
 					  Path *subpath,
 					  PathTarget *target,
 					  List *windowFuncs,
-					  WindowClause *winclause)
+					  WindowClause *winclause,
+					  List *qual,
+					  bool topwindow)
 {
 	WindowAggPath *pathnode = makeNode(WindowAggPath);
 
+	/* qual can only be set for the topwindow */
+	Assert(qual == NIL || topwindow);
+
 	pathnode->path.pathtype = T_WindowAgg;
 	pathnode->path.parent = rel;
 	pathnode->path.pathtarget = target;
@@ -3416,6 +3425,8 @@ create_windowagg_path(PlannerInfo *root,
 
 	pathnode->subpath = subpath;
 	pathnode->winclause = winclause;
+	pathnode->qual = qual;
+	pathnode->topwindow = topwindow;
 
 	/*
 	 * For costing purposes, assume that there are no redundant partitioning
diff --git a/src/backend/utils/adt/int8.c b/src/backend/utils/adt/int8.c
index 4a87114a4f48e..98d432375566b 100644
--- a/src/backend/utils/adt/int8.c
+++ b/src/backend/utils/adt/int8.c
@@ -24,6 +24,7 @@
 #include "nodes/supportnodes.h"
 #include "optimizer/optimizer.h"
 #include "utils/builtins.h"
+#include "utils/lsyscache.h"
 
 
 typedef struct
@@ -818,6 +819,49 @@ int8dec_any(PG_FUNCTION_ARGS)
 	return int8dec(fcinfo);
 }
 
+/*
+ * int8inc_support
+ *		prosupport function for int8inc() and int8inc_any()
+ */
+Datum
+int8inc_support(PG_FUNCTION_ARGS)
+{
+	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);
+
+	if (IsA(rawreq, SupportRequestWFuncMonotonic))
+	{
+		SupportRequestWFuncMonotonic *req = (SupportRequestWFuncMonotonic *) rawreq;
+		MonotonicFunction monotonic = MONOTONICFUNC_NONE;
+		int			frameOptions = req->window_clause->frameOptions;
+
+		/* No ORDER BY clause then all rows are peers */
+		if (req->window_clause->orderClause == NIL)
+			monotonic = MONOTONICFUNC_BOTH;
+		else
+		{
+			/*
+			 * Otherwise take into account the frame options.  When the frame
+			 * bound is the start of the window then the resulting value can
+			 * never decrease, therefore is monotonically increasing
+			 */
+			if (frameOptions & FRAMEOPTION_START_UNBOUNDED_PRECEDING)
+				monotonic |= MONOTONICFUNC_INCREASING;
+
+			/*
+			 * Likewise, if the frame bound is the end of the window then the
+			 * resulting value can never decrease.
+			 */
+			if (frameOptions & FRAMEOPTION_END_UNBOUNDED_FOLLOWING)
+				monotonic |= MONOTONICFUNC_DECREASING;
+		}
+
+		req->monotonic = monotonic;
+		PG_RETURN_POINTER(req);
+	}
+
+	PG_RETURN_POINTER(NULL);
+}
+
 
 Datum
 int8larger(PG_FUNCTION_ARGS)
diff --git a/src/backend/utils/adt/windowfuncs.c b/src/backend/utils/adt/windowfuncs.c
index 3e0cc9be1aff6..596564fa15c54 100644
--- a/src/backend/utils/adt/windowfuncs.c
+++ b/src/backend/utils/adt/windowfuncs.c
@@ -13,6 +13,7 @@
  */
 #include "postgres.h"
 
+#include "nodes/supportnodes.h"
 #include "utils/builtins.h"
 #include "windowapi.h"
 
@@ -88,6 +89,26 @@ window_row_number(PG_FUNCTION_ARGS)
 	PG_RETURN_INT64(curpos + 1);
 }
 
+/*
+ * window_row_number_support
+ *		prosupport function for window_row_number()
+ */
+Datum
+window_row_number_support(PG_FUNCTION_ARGS)
+{
+	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);
+
+	if (IsA(rawreq, SupportRequestWFuncMonotonic))
+	{
+		SupportRequestWFuncMonotonic *req = (SupportRequestWFuncMonotonic *) rawreq;
+
+		/* row_number() is monotonically increasing */
+		req->monotonic = MONOTONICFUNC_INCREASING;
+		PG_RETURN_POINTER(req);
+	}
+
+	PG_RETURN_POINTER(NULL);
+}
 
 /*
  * rank
@@ -110,6 +131,27 @@ window_rank(PG_FUNCTION_ARGS)
 	PG_RETURN_INT64(context->rank);
 }
 
+/*
+ * window_rank_support
+ *		prosupport function for window_rank()
+ */
+Datum
+window_rank_support(PG_FUNCTION_ARGS)
+{
+	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);
+
+	if (IsA(rawreq, SupportRequestWFuncMonotonic))
+	{
+		SupportRequestWFuncMonotonic *req = (SupportRequestWFuncMonotonic *) rawreq;
+
+		/* rank() is monotonically increasing */
+		req->monotonic = MONOTONICFUNC_INCREASING;
+		PG_RETURN_POINTER(req);
+	}
+
+	PG_RETURN_POINTER(NULL);
+}
+
 /*
  * dense_rank
  * Rank increases by 1 when key columns change.
@@ -130,6 +172,27 @@ window_dense_rank(PG_FUNCTION_ARGS)
 	PG_RETURN_INT64(context->rank);
 }
 
+/*
+ * window_dense_rank_support
+ *		prosupport function for window_dense_rank()
+ */
+Datum
+window_dense_rank_support(PG_FUNCTION_ARGS)
+{
+	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);
+
+	if (IsA(rawreq, SupportRequestWFuncMonotonic))
+	{
+		SupportRequestWFuncMonotonic *req = (SupportRequestWFuncMonotonic *) rawreq;
+
+		/* dense_rank() is monotonically increasing */
+		req->monotonic = MONOTONICFUNC_INCREASING;
+		PG_RETURN_POINTER(req);
+	}
+
+	PG_RETURN_POINTER(NULL);
+}
+
 /*
  * percent_rank
  * return fraction between 0 and 1 inclusive,
diff --git a/src/include/catalog/catversion.h b/src/include/catalog/catversion.h
index cec70caae1fa3..5757f3baa1235 100644
--- a/src/include/catalog/catversion.h
+++ b/src/include/catalog/catversion.h
@@ -53,6 +53,6 @@
  */
 
 /*							yyyymmddN */
-#define CATALOG_VERSION_NO	202204075
+#define CATALOG_VERSION_NO	202204076
 
 #endif
diff --git a/src/include/catalog/pg_proc.dat b/src/include/catalog/pg_proc.dat
index 52f56cf5b1b93..6d378ff785948 100644
--- a/src/include/catalog/pg_proc.dat
+++ b/src/include/catalog/pg_proc.dat
@@ -6662,11 +6662,16 @@
 # count has two forms: count(any) and count(*)
 { oid => '2147',
   descr => 'number of input rows for which the input expression is not null',
-  proname => 'count', prokind => 'a', proisstrict => 'f', prorettype => 'int8',
-  proargtypes => 'any', prosrc => 'aggregate_dummy' },
+  proname => 'count', prosupport => 'int8inc_support', prokind => 'a',
+  proisstrict => 'f', prorettype => 'int8', proargtypes => 'any',
+  prosrc => 'aggregate_dummy' },
 { oid => '2803', descr => 'number of input rows',
-  proname => 'count', prokind => 'a', proisstrict => 'f', prorettype => 'int8',
-  proargtypes => '', prosrc => 'aggregate_dummy' },
+  proname => 'count', prosupport => 'int8inc_support', prokind => 'a',
+  proisstrict => 'f', prorettype => 'int8', proargtypes => '',
+  prosrc => 'aggregate_dummy' },
+{ oid => '8802', descr => 'planner support for count run condition',
+  proname => 'int8inc_support', prorettype => 'internal',
+  proargtypes => 'internal', prosrc => 'int8inc_support' },
 
 { oid => '2718',
   descr => 'population variance of bigint input values (square of the population standard deviation)',
@@ -10186,14 +10191,26 @@
 
 # SQL-spec window functions
 { oid => '3100', descr => 'row number within partition',
-  proname => 'row_number', prokind => 'w', proisstrict => 'f',
-  prorettype => 'int8', proargtypes => '', prosrc => 'window_row_number' },
+  proname => 'row_number', prosupport => 'window_row_number_support',
+  prokind => 'w', proisstrict => 'f',  prorettype => 'int8',
+  proargtypes => '', prosrc => 'window_row_number' },
+{ oid => '8799', descr => 'planner support for row_number run condition',
+  proname => 'window_row_number_support', prorettype => 'internal',
+  proargtypes => 'internal', prosrc => 'window_row_number_support' },
 { oid => '3101', descr => 'integer rank with gaps',
-  proname => 'rank', prokind => 'w', proisstrict => 'f', prorettype => 'int8',
+  proname => 'rank', prosupport => 'window_rank_support',
+  prokind => 'w', proisstrict => 'f', prorettype => 'int8',
   proargtypes => '', prosrc => 'window_rank' },
+{ oid => '8800', descr => 'planner support for rank run condition',
+  proname => 'window_rank_support', prorettype => 'internal',
+  proargtypes => 'internal', prosrc => 'window_rank_support' },
 { oid => '3102', descr => 'integer rank without gaps',
-  proname => 'dense_rank', prokind => 'w', proisstrict => 'f',
-  prorettype => 'int8', proargtypes => '', prosrc => 'window_dense_rank' },
+  proname => 'dense_rank', prosupport => 'window_dense_rank_support',
+  prokind => 'w', proisstrict => 'f', prorettype => 'int8', proargtypes => '',
+  prosrc => 'window_dense_rank' },
+{ oid => '8801', descr => 'planner support for dense rank run condition',
+  proname => 'window_dense_rank_support', prorettype => 'internal',
+  proargtypes => 'internal', prosrc => 'window_dense_rank_support' },
 { oid => '3103', descr => 'fractional rank within partition',
   proname => 'percent_rank', prokind => 'w', proisstrict => 'f',
   prorettype => 'float8', proargtypes => '', prosrc => 'window_percent_rank' },
diff --git a/src/include/nodes/execnodes.h b/src/include/nodes/execnodes.h
index cbbcff81d2e7c..94b191f8ae05d 100644
--- a/src/include/nodes/execnodes.h
+++ b/src/include/nodes/execnodes.h
@@ -2406,6 +2406,18 @@ typedef struct AggState
 typedef struct WindowStatePerFuncData *WindowStatePerFunc;
 typedef struct WindowStatePerAggData *WindowStatePerAgg;
 
+/*
+ * WindowAggStatus -- Used to track the status of WindowAggState
+ */
+typedef enum WindowAggStatus
+{
+	WINDOWAGG_DONE,				/* No more processing to do */
+	WINDOWAGG_RUN,				/* Normal processing of window funcs */
+	WINDOWAGG_PASSTHROUGH,		/* Don't eval window funcs */
+	WINDOWAGG_PASSTHROUGH_STRICT	/* Pass-through plus don't store new
+									 * tuples during spool */
+} WindowAggStatus;
+
 typedef struct WindowAggState
 {
 	ScanState	ss;				/* its first field is NodeTag */
@@ -2432,6 +2444,7 @@ typedef struct WindowAggState
 	struct WindowObjectData *agg_winobj;	/* winobj for aggregate fetches */
 	int64		aggregatedbase; /* start row for current aggregates */
 	int64		aggregatedupto; /* rows before this one are aggregated */
+	WindowAggStatus status;		/* run status of WindowAggState */
 
 	int			frameOptions;	/* frame_clause options, see WindowDef */
 	ExprState  *startOffset;	/* expression for starting bound offset */
@@ -2458,8 +2471,17 @@ typedef struct WindowAggState
 	MemoryContext curaggcontext;	/* current aggregate's working data */
 	ExprContext *tmpcontext;	/* short-term evaluation context */
 
+	ExprState  *runcondition;	/* Condition which must remain true otherwise
+								 * execution of the WindowAgg will finish or
+								 * go into pass-through mode.  NULL when there
+								 * is no such condition. */
+
+	bool		use_pass_through;	/* When false, stop execution when
+									 * runcondition is no longer true.  Else
+									 * just stop evaluating window funcs. */
+	bool		top_window;		/* true if this is the top-most WindowAgg or
+								 * the only WindowAgg in this query level */
 	bool		all_first;		/* true if the scan is starting */
-	bool		all_done;		/* true if the scan is finished */
 	bool		partition_spooled;	/* true if all tuples in current partition
 									 * have been spooled into tuplestore */
 	bool		more_partitions;	/* true if there's more partitions after
diff --git a/src/include/nodes/nodes.h b/src/include/nodes/nodes.h
index 300824258ed82..340d28f4e1a98 100644
--- a/src/include/nodes/nodes.h
+++ b/src/include/nodes/nodes.h
@@ -560,7 +560,8 @@ typedef enum NodeTag
 	T_SupportRequestSelectivity,	/* in nodes/supportnodes.h */
 	T_SupportRequestCost,		/* in nodes/supportnodes.h */
 	T_SupportRequestRows,		/* in nodes/supportnodes.h */
-	T_SupportRequestIndexCondition	/* in nodes/supportnodes.h */
+	T_SupportRequestIndexCondition, /* in nodes/supportnodes.h */
+	T_SupportRequestWFuncMonotonic	/* in nodes/supportnodes.h */
 } NodeTag;
 
 /*
diff --git a/src/include/nodes/parsenodes.h b/src/include/nodes/parsenodes.h
index 1bdeb9eb3d308..da02658c815d0 100644
--- a/src/include/nodes/parsenodes.h
+++ b/src/include/nodes/parsenodes.h
@@ -1402,6 +1402,7 @@ typedef struct WindowClause
 	int			frameOptions;	/* frame_clause options, see WindowDef */
 	Node	   *startOffset;	/* expression for starting bound, if any */
 	Node	   *endOffset;		/* expression for ending bound, if any */
+	List	   *runCondition;	/* qual to help short-circuit execution */
 	Oid			startInRangeFunc;	/* in_range function for startOffset */
 	Oid			endInRangeFunc; /* in_range function for endOffset */
 	Oid			inRangeColl;	/* collation for in_range tests */
diff --git a/src/include/nodes/pathnodes.h b/src/include/nodes/pathnodes.h
index 6cbcb67bdf1de..c5ab53e05cb91 100644
--- a/src/include/nodes/pathnodes.h
+++ b/src/include/nodes/pathnodes.h
@@ -1843,6 +1843,9 @@ typedef struct WindowAggPath
 	Path		path;
 	Path	   *subpath;		/* path representing input source */
 	WindowClause *winclause;	/* WindowClause we'll be using */
+	List	   *qual;			/* lower-level WindowAgg runconditions */
+	bool		topwindow;		/* false for all apart from the WindowAgg
+								 * that's closest to the root of the plan */
 } WindowAggPath;
 
 /*
diff --git a/src/include/nodes/plannodes.h b/src/include/nodes/plannodes.h
index 10dd35f011299..e43e360d9be1d 100644
--- a/src/include/nodes/plannodes.h
+++ b/src/include/nodes/plannodes.h
@@ -926,12 +926,16 @@ typedef struct WindowAgg
 	int			frameOptions;	/* frame_clause options, see WindowDef */
 	Node	   *startOffset;	/* expression for starting bound, if any */
 	Node	   *endOffset;		/* expression for ending bound, if any */
+	List	   *runCondition;	/* qual to help short-circuit execution */
+	List	   *runConditionOrig;	/* runCondition for display in EXPLAIN */
 	/* these fields are used with RANGE offset PRECEDING/FOLLOWING: */
 	Oid			startInRangeFunc;	/* in_range function for startOffset */
 	Oid			endInRangeFunc; /* in_range function for endOffset */
 	Oid			inRangeColl;	/* collation for in_range tests */
 	bool		inRangeAsc;		/* use ASC sort order for in_range tests? */
 	bool		inRangeNullsFirst;	/* nulls sort first for in_range tests? */
+	bool		topWindow;		/* false for all apart from the WindowAgg
+								 * that's closest to the root of the plan */
 } WindowAgg;
 
 /* ----------------
@@ -1324,4 +1328,21 @@ typedef struct PlanInvalItem
 	uint32		hashValue;		/* hash value of object's cache lookup key */
 } PlanInvalItem;
 
+/*
+ * MonotonicFunction
+ *
+ * Allows the planner to track monotonic properties of functions.  A function
+ * is monotonically increasing if a subsequent call cannot yield a lower value
+ * than the previous call.  A monotonically decreasing function cannot yield a
+ * higher value on subsequent calls, and a function which is both must return
+ * the same value on each call.
+ */
+typedef enum MonotonicFunction
+{
+	MONOTONICFUNC_NONE = 0,
+	MONOTONICFUNC_INCREASING = (1 << 0),
+	MONOTONICFUNC_DECREASING = (1 << 1),
+	MONOTONICFUNC_BOTH = MONOTONICFUNC_INCREASING | MONOTONICFUNC_DECREASING
+} MonotonicFunction;
+
 #endif							/* PLANNODES_H */
diff --git a/src/include/nodes/supportnodes.h b/src/include/nodes/supportnodes.h
index 88b61b3ab3642..9fcbc399495d1 100644
--- a/src/include/nodes/supportnodes.h
+++ b/src/include/nodes/supportnodes.h
@@ -33,12 +33,12 @@
 #ifndef SUPPORTNODES_H
 #define SUPPORTNODES_H
 
-#include "nodes/primnodes.h"
+#include "nodes/plannodes.h"
 
 struct PlannerInfo;				/* avoid including pathnodes.h here */
 struct IndexOptInfo;
 struct SpecialJoinInfo;
-
+struct WindowClause;
 
 /*
  * The Simplify request allows the support function to perform plan-time
@@ -239,4 +239,64 @@ typedef struct SupportRequestIndexCondition
 								 * equivalent of the function call */
 } SupportRequestIndexCondition;
 
+/* ----------
+ * To support more efficient query execution of any monotonically increasing
+ * and/or monotonically decreasing window functions, we support calling the
+ * window function's prosupport function passing along this struct whenever
+ * the planner sees an OpExpr qual directly reference a window function in a
+ * subquery.  When the planner encounters this, we populate this struct and
+ * pass it along to the window function's prosupport function so that it can
+ * evaluate if the given WindowFunc is;
+ *
+ * a) monotonically increasing, or
+ * b) monotonically decreasing, or
+ * c) both monotonically increasing and decreasing, or
+ * d) none of the above.
+ *
+ * A function that is monotonically increasing can never return a value that
+ * is lower than a value returned in a "previous call".  A monotonically
+ * decreasing function can never return a value higher than a value returned
+ * in a previous call.  A function that is both must return the same value
+ * each time.
+ *
+ * We define "previous call" to mean a previous call to the same WindowFunc
+ * struct in the same window partition.
+ *
+ * row_number() is an example of a monotonically increasing function.  The
+ * return value will be reset back to 1 in each new partition.  An example of
+ * a monotonically increasing and decreasing function is COUNT(*) OVER ().
+ * Since there is no ORDER BY clause in this example, all rows in the
+ * partition are peers and all rows within the partition will be within the
+ * frame bound.  Likewise for COUNT(*) OVER(ORDER BY a ROWS BETWEEN UNBOUNDED
+ * PRECEDING AND UNBOUNDED FOLLOWING).
+ *
+ * COUNT(*) OVER (ORDER BY a ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING)
+ * is an example of a monotonically decreasing function.
+ *
+ * Implementations must only concern themselves with the given WindowFunc
+ * being monotonic in a single partition.
+ *
+ * Inputs:
+ *	'window_func' is the pointer to the window function being called.
+ *
+ *	'window_clause' pointer to the WindowClause data.  Support functions can
+ *	use this to check frame bounds, etc.
+ *
+ * Outputs:
+ *	'monotonic' the resulting MonotonicFunction value for the given input
+ *	window function and window clause.
+ * ----------
+ */
+typedef struct SupportRequestWFuncMonotonic
+{
+	NodeTag		type;
+
+	/* Input fields: */
+	WindowFunc *window_func;	/* Pointer to the window function data */
+	struct WindowClause *window_clause; /* Pointer to the window clause data */
+
+	/* Output fields: */
+	MonotonicFunction monotonic;
+} SupportRequestWFuncMonotonic;
+
 #endif							/* SUPPORTNODES_H */
diff --git a/src/include/optimizer/pathnode.h b/src/include/optimizer/pathnode.h
index 6eca547af80e7..d2d46b15df591 100644
--- a/src/include/optimizer/pathnode.h
+++ b/src/include/optimizer/pathnode.h
@@ -245,7 +245,9 @@ extern WindowAggPath *create_windowagg_path(PlannerInfo *root,
 											Path *subpath,
 											PathTarget *target,
 											List *windowFuncs,
-											WindowClause *winclause);
+											WindowClause *winclause,
+											List *qual,
+											bool topwindow);
 extern SetOpPath *create_setop_path(PlannerInfo *root,
 									RelOptInfo *rel,
 									Path *subpath,
~~~

## 修改位置的版本上下文

### ExecWindowAgg · 投影与返回

第一父版本 · src/backend/executor/nodeWindowAgg.c · L2231–L2239

~~~c
	/*
	 * Form and return a projection tuple using the windowfunc results and the
	 * current row.  Setting ecxt_outertuple arranges that any Vars will be
	 * evaluated with respect to that row.
	 */
	econtext->ecxt_outertuple = winstate->ss.ss_ScanTupleSlot;

	return ExecProject(winstate->ss.ps.ps_ProjInfo);
}
~~~

### ExecWindowAgg · 投影与返回

目标版本 · src/backend/executor/nodeWindowAgg.c · L2265–L2342

~~~c
		/*
		 * Form and return a projection tuple using the windowfunc results and
		 * the current row.  Setting ecxt_outertuple arranges that any Vars
		 * will be evaluated with respect to that row.
		 */
		econtext->ecxt_outertuple = winstate->ss.ss_ScanTupleSlot;

		slot = ExecProject(winstate->ss.ps.ps_ProjInfo);

		if (winstate->status == WINDOWAGG_RUN)
		{
			econtext->ecxt_scantuple = slot;

			/*
			 * Now evaluate the run condition to see if we need to go into
			 * pass-through mode, or maybe stop completely.
			 */
			if (!ExecQual(winstate->runcondition, econtext))
			{
				/*
				 * Determine which mode to move into.  If there is no
				 * PARTITION BY clause and we're the top-level WindowAgg then
				 * we're done.  This tuple and any future tuples cannot
				 * possibly match the runcondition.  However, when there is a
				 * PARTITION BY clause or we're not the top-level window we
				 * can't just stop as we need to either process other
				 * partitions or ensure WindowAgg nodes above us receive all
				 * of the tuples they need to process their WindowFuncs.
				 */
				if (winstate->use_pass_through)
				{
					/*
					 * STRICT pass-through mode is required for the top window
					 * when there is a PARTITION BY clause.  Otherwise we must
					 * ensure we store tuples that don't match the
					 * runcondition so they're available to WindowAggs above.
					 */
					if (winstate->top_window)
					{
						winstate->status = WINDOWAGG_PASSTHROUGH_STRICT;
						continue;
					}
					else
						winstate->status = WINDOWAGG_PASSTHROUGH;
				}
				else
				{
					/*
					 * Pass-through not required.  We can just return NULL.
					 * Nothing else will match the runcondition.
					 */
					winstate->status = WINDOWAGG_DONE;
					return NULL;
				}
			}

			/*
			 * Filter out any tuples we don't need in the top-level WindowAgg.
			 */
			if (!ExecQual(winstate->ss.ps.qual, econtext))
			{
				InstrCountFiltered1(winstate, 1);
				continue;
			}

			break;
		}

		/*
		 * When not in WINDOWAGG_RUN mode, we must still return this tuple if
		 * we're anything apart from the top window.
		 */
		else if (!winstate->top_window)
			break;
	}

	return slot;
}
~~~

## 相关源码摘录

### find_window_run_conditions

目标版本 · src/backend/optimizer/path/allpaths.c · L2183–L2363

~~~c
static bool
find_window_run_conditions(Query *subquery, RangeTblEntry *rte, Index rti,
						   AttrNumber attno, WindowFunc *wfunc, OpExpr *opexpr,
						   bool wfunc_left, bool *keep_original)
{
	Oid			prosupport;
	Expr	   *otherexpr;
	SupportRequestWFuncMonotonic req;
	SupportRequestWFuncMonotonic *res;
	WindowClause *wclause;
	List	   *opinfos;
	OpExpr	   *runopexpr;
	Oid			runoperator;
	ListCell   *lc;

	*keep_original = true;

	while (IsA(wfunc, RelabelType))
		wfunc = (WindowFunc *) ((RelabelType *) wfunc)->arg;

	/* we can only work with window functions */
	if (!IsA(wfunc, WindowFunc))
		return false;

	prosupport = get_func_support(wfunc->winfnoid);

	/* Check if there's a support function for 'wfunc' */
	if (!OidIsValid(prosupport))
		return false;

	/* get the Expr from the other side of the OpExpr */
	if (wfunc_left)
		otherexpr = lsecond(opexpr->args);
	else
		otherexpr = linitial(opexpr->args);

	/*
	 * The value being compared must not change during the evaluation of the
	 * window partition.
	 */
	if (!is_pseudo_constant_clause((Node *) otherexpr))
		return false;

	/* find the window clause belonging to the window function */
	wclause = (WindowClause *) list_nth(subquery->windowClause,
										wfunc->winref - 1);

	req.type = T_SupportRequestWFuncMonotonic;
	req.window_func = wfunc;
	req.window_clause = wclause;

	/* call the support function */
	res = (SupportRequestWFuncMonotonic *)
		DatumGetPointer(OidFunctionCall1(prosupport,
										 PointerGetDatum(&req)));

	/*
	 * Nothing to do if the function is neither monotonically increasing nor
	 * monotonically decreasing.
	 */
	if (res == NULL || res->monotonic == MONOTONICFUNC_NONE)
		return false;

	runopexpr = NULL;
	runoperator = InvalidOid;
	opinfos = get_op_btree_interpretation(opexpr->opno);

	foreach(lc, opinfos)
	{
		OpBtreeInterpretation *opinfo = (OpBtreeInterpretation *) lfirst(lc);
		int			strategy = opinfo->strategy;

		/* handle < / <= */
		if (strategy == BTLessStrategyNumber ||
			strategy == BTLessEqualStrategyNumber)
		{
			/*
			 * < / <= is supported for monotonically increasing functions in
			 * the form <wfunc> op <pseudoconst> and <pseudoconst> op <wfunc>
			 * for monotonically decreasing functions.
			 */
			if ((wfunc_left && (res->monotonic & MONOTONICFUNC_INCREASING)) ||
				(!wfunc_left && (res->monotonic & MONOTONICFUNC_DECREASING)))
			{
				*keep_original = false;
				runopexpr = opexpr;
				runoperator = opexpr->opno;
			}
			break;
		}
		/* handle > / >= */
		else if (strategy == BTGreaterStrategyNumber ||
				 strategy == BTGreaterEqualStrategyNumber)
		{
			/*
			 * > / >= is supported for monotonically decreasing functions in
			 * the form <wfunc> op <pseudoconst> and <pseudoconst> op <wfunc>
			 * for monotonically increasing functions.
			 */
			if ((wfunc_left && (res->monotonic & MONOTONICFUNC_DECREASING)) ||
				(!wfunc_left && (res->monotonic & MONOTONICFUNC_INCREASING)))
			{
				*keep_original = false;
				runopexpr = opexpr;
				runoperator = opexpr->opno;
			}
			break;
		}
		/* handle = */
		else if (strategy == BTEqualStrategyNumber)
		{
			int16		newstrategy;

			/*
			 * When both monotonically increasing and decreasing then the
			 * return value of the window function will be the same each time.
			 * We can simply use 'opexpr' as the run condition without
			 * modifying it.
			 */
			if ((res->monotonic & MONOTONICFUNC_BOTH) == MONOTONICFUNC_BOTH)
			{
				*keep_original = false;
				runopexpr = opexpr;
				break;
			}

			/*
			 * When monotonically increasing we make a qual with <wfunc> <=
			 * <value> or <value> >= <wfunc> in order to filter out values
			 * which are above the value in the equality condition.  For
			 * monotonically decreasing functions we want to filter values
			 * below the value in the equality condition.
			 */
			if (res->monotonic & MONOTONICFUNC_INCREASING)
				newstrategy = wfunc_left ? BTLessEqualStrategyNumber : BTGreaterEqualStrategyNumber;
			else
				newstrategy = wfunc_left ? BTGreaterEqualStrategyNumber : BTLessEqualStrategyNumber;

			/* We must keep the original equality qual */
			*keep_original = true;
			runopexpr = opexpr;

			/* determine the operator to use for the runCondition qual */
			runoperator = get_opfamily_member(opinfo->opfamily_id,
											  opinfo->oplefttype,
											  opinfo->oprighttype,
											  newstrategy);
			break;
		}
	}

	if (runopexpr != NULL)
	{
		Expr	   *newexpr;

		/*
		 * Build the qual required for the run condition keeping the
		 * WindowFunc on the same side as it was originally.
		 */
		if (wfunc_left)
			newexpr = make_opclause(runoperator,
									runopexpr->opresulttype,
									runopexpr->opretset, (Expr *) wfunc,
									otherexpr, runopexpr->opcollid,
									runopexpr->inputcollid);
		else
			newexpr = make_opclause(runoperator,
									runopexpr->opresulttype,
									runopexpr->opretset,
									otherexpr, (Expr *) wfunc,
									runopexpr->opcollid,
									runopexpr->inputcollid);

		wclause->runCondition = lappend(wclause->runCondition, newexpr);

		return true;
	}

	/* unsupported OpExpr */
	return false;
}
~~~

### window_row_number_support

目标版本 · src/backend/utils/adt/windowfuncs.c · L92–L111

~~~c
/*
 * window_row_number_support
 *		prosupport function for window_row_number()
 */
Datum
window_row_number_support(PG_FUNCTION_ARGS)
{
	Node	   *rawreq = (Node *) PG_GETARG_POINTER(0);

	if (IsA(rawreq, SupportRequestWFuncMonotonic))
	{
		SupportRequestWFuncMonotonic *req = (SupportRequestWFuncMonotonic *) rawreq;

		/* row_number() is monotonically increasing */
		req->monotonic = MONOTONICFUNC_INCREASING;
		PG_RETURN_POINTER(req);
	}

	PG_RETURN_POINTER(NULL);
}
~~~

### create_one_window_path

目标版本 · src/backend/optimizer/plan/planner.c · L4282–L4300

~~~c
		/* mark the final item in the list as the top-level window */
		topwindow = foreach_current_index(l) == list_length(activeWindows) - 1;

		/*
		 * Accumulate all of the runConditions from each intermediate
		 * WindowClause.  The top-level WindowAgg must pass these as a qual so
		 * that it filters out unwanted tuples correctly.
		 */
		if (!topwindow)
			topqual = list_concat(topqual, wc->runCondition);

		path = (Path *)
			create_windowagg_path(root, window_rel, path, window_target,
								  wflists->windowFuncs[wc->winref],
								  wc, topwindow ? topqual : NIL, topwindow);
	}

	add_path(window_rel, path);
}
~~~
