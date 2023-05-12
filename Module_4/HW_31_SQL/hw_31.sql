-- write a query in SQL to display the first name, last name, department number,
-- and department name for each employee

select first_name, last_name, employees.department_id, department_name
from employees
inner join department on employees.department_id = department.department_id
order by last_name;

-- write a query in SQL to display the first and last name, department, city,
-- and state province for each employee

select first_name, last_name, department_name, city, state_province
from employees
inner join department on employees.department_id = department.department_id
inner join locations on department.location_id = locations.location_id
order by last_name;

-- write a query in SQL to display the first name, last name, department number,
-- and department name, for all employees for departments 80 or 40

select first_name, last_name, employees.department_id, department_name
from employees
inner join department d on employees.department_id = d.department_id
where employees.department_id = 80 or employees.department_id = 40
order by last_name;

-- write a query in SQL to display all departments including those where does
-- not have any employee

select department.department_id, department_name, first_name, last_name
from department
left join employees e on department.department_id = e.department_id
order by last_name;

-- write a query in SQL to display the first name of all employees including
-- the first name of their manager

-- don't know how to do this query

-- select employees.first_name, first_name
-- from employees
-- inner join employees on employees.manager_id = employees.employee_id;

-- write a query in SQL to display the job title, full name (first and last name )
-- of the employee, and the difference between the maximum salary for the job and
-- the salary of the employee

select first_name, last_name, jobs.max_salary - employees.salary as sallary_difference
from employees
inner join jobs on employees.job_id = jobs.job_id;

-- write a query in SQL to display the job title and the average salary of employees

select job_title, (max_salary-min_salary)/2 as avarage_salary
from jobs
order by job_title;

-- write a query in SQL to display the full name (first and last name),
-- and salary of those employees who work in any department located in London

select first_name, last_name, salary
from employees
inner join department on employees.department_id = department.department_id
inner join locations on locations.location_id = department.location_id
where locations.city = 'London';

-- write a query in SQL to display
-- the department name and the number of employees in each department

select d.depart_name, count(*) as number_of_employees
from employees
inner join departments d on employees.department_id = d.department_id
group by d.department_id;
