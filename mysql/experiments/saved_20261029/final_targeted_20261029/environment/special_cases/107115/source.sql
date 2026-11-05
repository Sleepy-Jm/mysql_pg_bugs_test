-- MySQL report #107115; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
SET NAMES utf8mb4;
SELECT @@global.ft_boolean_syntax;
SET GLOBAL ft_boolean_syntax=REPEAT('中',99);
SHOW WARNINGS;
SELECT 1 AS connection_alive;
