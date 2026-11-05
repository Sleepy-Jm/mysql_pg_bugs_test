-- Report #107139; source anchors: cmain, c521910, c521911, c521912, c545749, c545995
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE account (acct_num INT, amount DECIMAL(10,2));
CREATE DEFINER="testinguser"@"localhost" TRIGGER ins_sum BEFORE INSERT ON account FOR EACH ROW SET @sum = @sum + NEW.amount;
