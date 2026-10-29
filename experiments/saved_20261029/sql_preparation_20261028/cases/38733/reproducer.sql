-- MySQL report #38733; source anchors: c180702, c185118
-- Static preparation only; NOT EXECUTED. Run only in a fresh isolated schema/instance.
CREATE TABLE entContact(id INT UNSIGNED NOT NULL AUTO_INCREMENT,person VARCHAR(32) NOT NULL,PRIMARY KEY(id));
INSERT INTO entContact(person) VALUES ('Joe'),('Jessica'),('Alan');
DELIMITER $$
CREATE PROCEDURE lstContacts(pPersonMatch VARCHAR(64))
BEGIN SELECT * FROM entContact WHERE pPersonMatch IS NULL OR person RLIKE pPersonMatch; END$$
DELIMITER ;
CALL lstContacts('Joe(seph)?');
CALL lstContacts('Sarah?');
SELECT * FROM entContact WHERE NULL IS NULL OR person RLIKE NULL;
CALL lstContacts(NULL);
