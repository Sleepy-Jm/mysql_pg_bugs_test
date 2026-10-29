-- MySQL report #82308; source anchors: cmain, c448466
-- Prepared offline; NOT EXECUTED. Run only in a disposable isolated environment.
CREATE TABLE bit_test(
       attr_bit BIT,
       attr_text LONGTEXT
) ENGINE=MyISAM;

INSERT INTO bit_test
VALUES
(0, 't1'),
(1, 't2'),
(1, 't3'),
(1, 't3'),
(0, 't3');

SELECT CAST(attr_bit AS UNSIGNED), attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test
) a;

#expected:
#0, t1
#1, t2
#1, t3
#0, t3

#actual:
#+----------------------------+-----------+
#| CAST(attr_bit AS UNSIGNED) | attr_text |
#+----------------------------+-----------+
#|                          1 | t1        |
#|                          1 | t2        |
#|                          1 | t3        |
#|                          1 | t3        |
#+----------------------------+-----------+

####################################
#     some additional interesting observations   #
####################################

#selection on attr_bit in the outer query fails:
SELECT CAST(attr_bit AS UNSIGNED), attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test
) a
WHERE a.attr_bit = 0; #alternatively a.attr_bit = (0) OR a.attr_bit = b'0'
#returns the four rows as the query above

SELECT CAST(attr_bit AS UNSIGNED), attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test
) a
WHERE a.attr_bit = 1;
#empty result set

####################
#selection issue was also observed on a similar table table with VARCHAR(255) instead of LONGTEXT
CREATE TABLE bit_test_varchar(
       attr_bit BIT,
       attr_text VARCHAR(255)
) ENGINE=MyISAM;

INSERT INTO bit_test_varchar
VALUES
(0, 't1'),
(1, 't2'),
(1, 't3'),
(1, 't3'),
(0, 't3');

#works
SELECT CAST(attr_bit AS UNSIGNED), attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test_varchar
) a;

#+----------------------------+-----------+
#| CAST(attr_bit AS UNSIGNED) | attr_text |
#+----------------------------+-----------+
#|                          0 | t1        |
#|                          1 | t2        |
#|                          1 | t3        |
#|                          0 | t3        |
#+----------------------------+-----------+

#however selection on attr_bit in outer select still produces unexpected result
SELECT CAST(attr_bit AS UNSIGNED), attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test_varchar
) a
WHERE a.attr_bit = b'0';

#+----------------------------+-----------+
#| CAST(attr_bit AS UNSIGNED) | attr_text |
#+----------------------------+-----------+
#|                          0 | t1        |
#+----------------------------+-----------+

#even though
SELECT a.attr_bit = b'0', attr_text
FROM(
	SELECT DISTINCT *
	FROM bit_test_varchar
) a;

#+-------------------+-----------+
#| a.attr_bit = b'0' | attr_text |
#+-------------------+-----------+
#|                 1 | t1        |
#|                 0 | t2        |
#|                 0 | t3        |
#|                 1 | t3        |
#+-------------------+-----------+
