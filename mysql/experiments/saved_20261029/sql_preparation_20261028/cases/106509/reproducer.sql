-- MySQL report #106509; source anchors: cmain
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE `tasks` (
  `TaskID` int NOT NULL,
  `TaskAccess` json DEFAULT NULL,
  PRIMARY KEY (`TaskID`),
  KEY `access` ((cast(json_extract(`TaskAccess`,_utf8mb4'$.access') as unsigned array)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=COMPRESSED;

INSERT INTO `tasks` VALUES (20959,'{\"access\": [3584, 89698, 89906, 89972, 86422, 3583, 89662] }'),(21050,'{\"access\": [89698, 89906, 89972, 86422, 3752, 3583, 89662]}'),(21966,'{\"access\": [3584, 89698, 89906, 89972, 86422, 3583, 89662]}');


SELECT TaskID FROM tasks WHERE 3584 MEMBER OF(TaskAccess->'$.access') ORDER BY TaskID;
SELECT TaskID FROM tasks WHERE 3584 MEMBER OF(TaskAccess->'$.access') ORDER BY TaskID DESC;
EXPLAIN SELECT TaskID FROM tasks WHERE 3584 MEMBER OF(TaskAccess->'$.access') ORDER BY TaskID DESC;
