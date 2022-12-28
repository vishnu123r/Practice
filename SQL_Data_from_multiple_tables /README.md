## The following employee details were extracted using SQL. The tables were created using the attached SQL script and the csv files.

### Q1: Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table.
select * from employees where job_id in (select job_ident from jobs);

### Q2: Retrieve only the list of employees whose JOB_TITLE is Jr. Designer.
select * from employees where job_id in (select job_ident from jobs where job_title = 'Jr. Designer');

### Q3:Retrieve JOB information and list of employees who earn more than $70,000.
select * from jobs where job_ident in (select job_id from employees where salary > 70000);

### Q4:Retrieve JOB information and list of employees whose birth year is after 1976.
select * from jobs where job_ident in (select job_id from employees where YEAR(B_DATE)>1976);

### Q5: Retrieve JOB information and list of female employees whose birth year is after 1976.
select * from jobs where job_ident in (select job_id from employees where YEAR(B_DATE) > 1976 and sex = 'F');

### Q6:Perform an implicit cartesian/cross join between EMPLOYEES and JOBS tables.
select * from EMPLOYEES E, JOBS J;

### Q7:Retrieve only the EMPLOYEES records that correspond to jobs in the JOBS table.
select * from EMPLOYEES E, JOBS J where E.job_id = J.job_ident;

### Q8:Redo the previous query, using shorter aliases for table names.
select * from EMPLOYEES E, JOBS J where E.job_id = J.job_ident;

### Q9:Redo the previous query, but retrieve only the Employee ID, Employee Name and Job Title.
select EMP_ID,F_NAME,L_NAME, JOB_TITLE  from EMPLOYEES E, JOBS J where E.job_id = J.job_ident;

### Q10:Redo the previous query, but specify the fully qualified column names with aliases in the SELECT clause.
select E.EMP_ID,E.F_NAME,E.L_NAME, J.JOB_TITLE  from EMPLOYEES E, JOBS J where E.job_id = J.job_ident;
