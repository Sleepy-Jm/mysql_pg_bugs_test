-- Report #112194; source anchors: cmain, c535766, c535821, c535822, c535885
-- Static preparation only; not executed. See case.json before any future isolated run.
CREATE TABLE emp(emp_id INT,emp_name VARCHAR(100),salary INT,dept_id INT);
INSERT INTO emp VALUES(1,'emp_A',1000,10),(2,'emp_B',2000,20),(3,'emp_C',3000,30),(4,'emp_D',2000,10),(5,'emp_E',3000,20);
CREATE VIEW vw_emp AS SELECT emp_id,emp_name,salary,dept_id FROM emp;
CREATE TABLE dept(dept_id INT,dept_name VARCHAR(100));
INSERT INTO dept VALUES(10,'dept_A'),(20,'dept_B'),(30,'dept_C'),(40,'dept_D'),(50,'dept_E'),(60,'dept_F');
SET @case_optimizer=@@session.optimizer_switch;
SET SESSION optimizer_switch='derived_merge=off';
# SQL-1 [ SELECT FROM VIEW ]
# Result => Correct

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from vw_emp where a.dept_id=b.dept_id and a.salary > 2000))
where a.emp_id=3
order by emp_id
;

# SQL-2 [ SELECT FROM VIEW and adding "OR (FALSE)" in the INNER JOIN ]
# Result => Wrong

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from vw_emp where a.dept_id=b.dept_id and a.salary > 2000) OR (FALSE))
where a.emp_id=3
order by emp_id
;

# SQL-3 [ SELECT FROM TABLE and adding "OR (FALSE)" in the INNER JOIN ]
# Result => Correct

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from emp where a.dept_id=b.dept_id and a.salary > 2000) OR (FALSE))
where a.emp_id=3
order by emp_id
;


SET SESSION optimizer_switch='derived_merge=on';
# SQL-1 [ SELECT FROM VIEW ]
# Result => Correct

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from vw_emp where a.dept_id=b.dept_id and a.salary > 2000))
where a.emp_id=3
order by emp_id
;

# SQL-2 [ SELECT FROM VIEW and adding "OR (FALSE)" in the INNER JOIN ]
# Result => Wrong

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from vw_emp where a.dept_id=b.dept_id and a.salary > 2000) OR (FALSE))
where a.emp_id=3
order by emp_id
;

# SQL-3 [ SELECT FROM TABLE and adding "OR (FALSE)" in the INNER JOIN ]
# Result => Correct

select a.emp_id, a.emp_name, a.salary, b.dept_name
from emp a
inner join dept b on (b.dept_id in (select dept_id from emp where a.dept_id=b.dept_id and a.salary > 2000) OR (FALSE))
where a.emp_id=3
order by emp_id
;
