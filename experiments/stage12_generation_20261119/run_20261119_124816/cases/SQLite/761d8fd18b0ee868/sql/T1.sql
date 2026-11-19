-- 准备：无表，仅用字面量
-- 目标：观察实数文本字面量经 sqlite3AtoF 解析后的 double 值
-- 对照：typeof() 确认是 REAL；printf('%!.17g') 给出可区分位模式的最短/精确表示
SELECT
  typeof(1.234567890123456789e+100)            AS t1_type,
  printf('%!.17g', 1.234567890123456789e+100)  AS t1_val,
  typeof(9.999999999999999999e+18)             AS t2_type,
  printf('%!.17g', 9.999999999999999999e+18)   AS t2_val,
  typeof(1.000000000000000111e+00)             AS t3_type,
  printf('%!.17g', 1.000000000000000111e+00)   AS t3_val;
-- 清理：无对象
