-- Read-only evidence after the unchanged source SQL, same session.
SELECT COUNT(*) AS main_rows FROM t_main;
SELECT COUNT(*) AS ref_rows FROM t_ref;
SELECT * FROM v_test;
