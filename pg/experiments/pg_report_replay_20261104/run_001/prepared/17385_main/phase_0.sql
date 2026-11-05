CREATE TABLE abc (a int);
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
        SELECT * FROM abc;
        RESET transaction_isolation;
END;
