select first_name as 'First Name', last_name as 'Last Name'
from employees;

select department_id from employees;

select * from employees
order by first_name DESC;

select first_name, last_name,
       salary * 12 / 100 as 'PF'
from employees;

select first_name, last_name, max(salary) from employees;

select first_name, last_name, min(salary) from  employees;

select * from employees;