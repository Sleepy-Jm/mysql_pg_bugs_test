-- MySQL report #110857; source anchors: cmain, c532041
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
CREATE TABLE sbtest1(id INT NOT NULL AUTO_INCREMENT,k INT NOT NULL DEFAULT 0,c CHAR(120) NOT NULL DEFAULT '',pad CHAR(60) NOT NULL DEFAULT '',PRIMARY KEY(id),KEY k_1(k));
INSERT INTO sbtest1 VALUES(1,2521302,'test1','test1'),(2,2521301,'test12','test2'),(4,2541301,'test111','test11');
SELECT id,k FROM sbtest1 WHERE id=1;
SELECT id,k FROM sbtest1 WHERE k=2521302;
SELECT id,k FROM sbtest1 WHERE id=1 UNION SELECT id,k FROM sbtest1 WHERE k=2;
SELECT esh.EVENT_ID,esh.SQL_TEXT,esh.NO_INDEX_USED FROM performance_schema.events_statements_history esh JOIN performance_schema.threads th USING(THREAD_ID) WHERE th.PROCESSLIST_ID=CONNECTION_ID() ORDER BY esh.EVENT_ID;
EXPLAIN SELECT id,k FROM sbtest1 WHERE id=1 UNION SELECT id,k FROM sbtest1 WHERE k=2;
