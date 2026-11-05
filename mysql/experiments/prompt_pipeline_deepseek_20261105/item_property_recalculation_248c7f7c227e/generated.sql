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
