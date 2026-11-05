conn1 = psycopg2.connect(**dbconfig)
conn2 = psycopg2.connect(**dbconfig)
cur1 = conn1.cursor()
cur2 = conn2.cursor()
try:
    cur1.execute("SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;")
    cur1.execute("START TRANSACTION;")


    cur2.execute("SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL SERIALIZABLE;")
    cur2.execute("START TRANSACTION;")


    cur1.execute("SELECT * FROM tJ6mtoSl WHERE ( tJ6mtoSl.c1 < 1646 AND tJ6mtoSl.c1 >= 1061 ) AND (tJ6mtoSl.c0 >= 100) ORDER BY tJ6mtoSl.ID;")
    print(cur1.fetchall())


    cur2.execute("SELECT * FROM tEJybmqs WHERE ( tEJybmqs.c1 = FALSE ) ORDER BY tEJybmqs.ID;")
    print(cur2.fetchall())
    cur2.execute("UPDATE tJ6mtoSl SET VAL = 16732 WHERE ( tJ6mtoSl.c1 < 1646 AND tJ6mtoSl.c1 >= 1061 ) AND (tJ6mtoSl.c0 >= 100);")
    cur2.execute("COMMIT;")


    cur1.execute("DELETE FROM tEJybmqs WHERE ( tEJybmqs.c1 = FALSE );")
    cur1.execute("COMMIT;")
except Exception as e:
    print(e)
cur1.close()
cur2.close();
