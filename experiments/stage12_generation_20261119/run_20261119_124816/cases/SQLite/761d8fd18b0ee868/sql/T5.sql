-- 准备：无表
-- 目标：观察无指数实数文本字面量（e == 0 路径）的解析
-- 对照：typeof() 与 printf('%!.17g') 观察 s 接近 2^53/2^63 时的 residual
SELECT
  typeof(9007199254740993.0)                   AS a_type,
  printf('%!.17g', 9007199254740993.0)         AS a_val,
  typeof(9223372036854775807.0)                AS b_type,
  printf('%!.17g', 9223372036854775807.0)      AS b_val,
  typeof(18446744073709551615.0)               AS c_type,
  printf('%!.17g', 18446744073709551615.0)     AS c_val;
-- 清理：无对象
