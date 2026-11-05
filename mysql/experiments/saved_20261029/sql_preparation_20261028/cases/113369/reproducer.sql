-- Report #113369; source anchors: cmain, c539471
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE `tt` (
  `id_col` int NOT NULL,
  `bigint_col` bigint NOT NULL,
  `year_col` year DEFAULT NULL,
  KEY `ndx_year_col` (`year_col` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
/*!50100 PARTITION BY HASH (`bigint_col`)
(PARTITION p0,
 PARTITION p1,
 PARTITION p2) */;
 
INSERT into tt values (61,-9223372036854775808,'1913');


SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col AND A.id_col = 61 GROUP BY 1, 2;
SELECT A.year_col,A.id_col FROM tt A WHERE A.id_col<A.year_col;
SELECT A.year_col,A.id_col FROM tt A WHERE A.id_col<CAST(A.year_col AS SIGNED) AND A.id_col=61;
