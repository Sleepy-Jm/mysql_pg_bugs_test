SET enable_seqscan=off; SELECT f1 <-> point '(0,0)' AS dist FROM point_tbl
ORDER BY dist;
