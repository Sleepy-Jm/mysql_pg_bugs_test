-- 准备：无表
-- 目标：观察接近 DBL_MAX 与次正规边界的实数文本字面量解析
-- 对照：typeof() 与 printf('%!.17g') 观察是否得到 Inf/0/次正规
SELECT
  typeof(1.7976931348623157e+308)              AS a_type,
  printf('%!.17g', 1.7976931348623157e+308)    AS a_val,
  typeof(1.7976931348623159e+308)              AS b_type,
  printf('%!.17g', 1.7976931348623159e+308)    AS b_val,
  typeof(4.9406564584124654e-324)              AS c_type,
  printf('%!.17g', 4.9406564584124654e-324)    AS c_val,
  typeof(2.4703282292062327e-324)              AS d_type,
  printf('%!.17g', 2.4703282292062327e-324)    AS d_val;
-- 清理：无对象
