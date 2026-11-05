-- Report #111474; source anchors: cmain, c533720, c533721, c536550
-- Static preparation only; not executed. See case.json before any future isolated run.
SET @case_optimizer=@@session.optimizer_switch;
CREATE TABLE t0 (c0 INT);
INSERT INTO t0 (c0) (VALUES ROW(2));
SET @@SESSION.OPTIMIZER_SWITCH = 'hypergraph_optimizer=on';
INSERT INTO t0 (c0) ((VALUES ROW(1),ROW(row_count())) EXCEPT (VALUES ROW(row_count()),ROW(3)));
