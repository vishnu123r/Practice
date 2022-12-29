## The following employee details were extracted using SQL. The tables were created using the attached SQL script and the csv files.

### Q1: Execute a failing query (i.e. one which gives an error) to retrieve all employees records whose salary is lower than the average salary.
SELECT * FROM employees WHERE salary < AVG(salary);

### Q2: Execute a working query using a sub-select to retrieve all employees records whose salary is lower than the average salary.
SELECT * FROM employees WHERE salary < (SELECT AVG(salary) FROM employees);

### Q3:Execute a failing query (i.e. one which gives an error) to retrieve all employees records with EMP_ID, SALARY and maximum salary as MAX_SALARY in every row.
SELECT emp_id, salary, max(salary) as MAX_SALARY FROM employees;

### Q4:Execute a Column Expression that retrieves all employees records with EMP_ID, SALARY and maximum salary as MAX_SALARY in every row.
SELECT emp_id, salary, (select MAX(salary) from employees) as MAX_SALARY FROM employees;

### Q5: Execute a Table Expression for the EMPLOYEES table that excludes columns with sensitive employee data (i.e. does not include columns: SSN, B_DATE, SEX, ADDRESS, SALARY).
SELECT * FROM ( SELECT emp_id, f_name, l_name, dep_id FROM employees) AS emp4all;

