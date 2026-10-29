-- Read-only postcheck appended after unchanged source SQL.
SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb1; SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb2; SELECT COUNT(*),SUM(double_col IS NULL),GROUP_CONCAT(HEX(bit_col) ORDER BY bit_col) FROM tb3;
