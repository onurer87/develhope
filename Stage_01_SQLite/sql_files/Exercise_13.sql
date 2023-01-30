--Deletes the table if exists
DROP TABLE IF EXISTS emp_department;

--Creates the table
CREATE TABLE emp_department(
"dpt_code" INTEGER NOT NULL,
"dpt_name" TEXT NOT NULL,
"dpt_allotment" INTEGER NOT NULL);


--Insert values into the table
INSERT INTO emp_department
VALUES	(57,"IT",65000),
(63,"Finance",15000),
(47,"HR",240000),
(27,"RD",55000),
(89,"QC",75000);

--Show table
Select * FROM emp_department;


--EX13.1
SELECT SUM(dpt_allotment) as "Sum of the Allotment Amount" FROM emp_department;