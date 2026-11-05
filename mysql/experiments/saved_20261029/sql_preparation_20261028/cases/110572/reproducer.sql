-- MySQL report #110572; source anchors: cmain, c531341
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SET SESSIONoptimizer_switch ='hypergraph_optimizer=on';
SELECT min(1) WHERE sysdate() = (ROW(2, 5) = ROW(1, 3));
SELECT 1 AS server_alive;
