-- 准备：无表
-- 目标：观察大/小 double 经 sqlite3FpDecode 缩放后的文本输出
-- 对照：同一 double 用 %e 与 %f 两种格式，观察末位是否一致
SELECT
  printf('%.17e', 1.0e+300)                    AS big_e,
  printf('%.17e', 1.0e-300)                    AS small_e,
  printf('%.17e', 9.223372036854775808e+18)    AS near_2p63_e,
  printf('%.17e', 1.2345678901234567e+200)     AS mid_e,
  printf('%.17f', 1.0e-300)                    AS small_f;
-- 清理：无对象
