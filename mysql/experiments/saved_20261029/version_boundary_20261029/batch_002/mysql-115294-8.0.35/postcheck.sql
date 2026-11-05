-- Read-only evidence after the unchanged source SQL, same session.
SELECT @@performance_schema;
SELECT NAME,ENABLED FROM performance_schema.setup_consumers WHERE NAME IN('global_instrumentation','thread_instrumentation');
SELECT OBJECT_TYPE,OBJECT_SCHEMA,OBJECT_NAME,ENABLED,TIMED FROM performance_schema.setup_objects WHERE OBJECT_TYPE='TABLE';
