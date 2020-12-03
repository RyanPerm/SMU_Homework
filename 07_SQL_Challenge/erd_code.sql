-- ERD CODE

Departments
----
dept_no VARCHAR PK
dept_name VARCHAR

Titles
----
title_id VARCHAR(15) PK
title VARCHAR(50)

Employees
----
emp_no INT PK
emp_title_id VARCHAR(15) FK >- Titles.title_id
birth_date DATE
first_name VARCHAR(40)
last_name VARCHAR(50)
sex VARCHAR(2)
hire_date DATE

Dept_managers
----
dept_no VARCHAR PK FK >- Departments.dept_no
emp_no INT PK FK >- Employees.emp_no

Dept_emps
----
emp_no INT PK FK >- Employees.emp_no
dept_no VARCHAR PK FK >- Departments.dept_no


Salaries
----
emp_no INT PK
salary INT FK >- Employees.emp_no