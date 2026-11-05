-- MySQL report #113433; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `tt` (
  `id_col` int NOT NULL,
  `bigint_col` bigint NOT NULL,
  `year_col` year DEFAULT NULL,
  KEY `ndx_year_col` (`year_col` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT into tt values (61,-9223372036854775808,'1913');

SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col;
SELECT A.year_col, A.id_col FROM tt A WHERE A.id_col < A.year_col AND A.id_col = 61;
SELECT A.year_col, A.id_col FROM tt A WHERE 61 < A.year_col;
