-- Read-only evidence after the unchanged source SQL, same session.
SELECT * FROM testa FORCE INDEX(PRIMARY) ORDER BY id;
SELECT * FROM testb FORCE INDEX(PRIMARY) ORDER BY id;
EXPLAIN SELECT /*+ JOIN_PREFIX(ord, bat) */ bat.id AS batchPkId,bat.batch_no,ord.id,ord.history_order_batch_no AS orderLevelHistoryBatchNo FROM testa bat INNER JOIN testb ord ON ord.current_order_batch_no=bat.batch_no WHERE bat.company_id=48005 AND ord.company_id=48005 AND bat.batch_no=101;
EXPLAIN SELECT bat.id AS batchPkId,bat.batch_no,ord.id,ord.history_order_batch_no AS orderLevelHistoryBatchNo FROM testa bat INNER JOIN testb ord ON ord.current_order_batch_no=bat.batch_no WHERE bat.company_id=48005 AND ord.company_id=48005 AND bat.batch_no=101;
