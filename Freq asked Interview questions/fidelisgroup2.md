employee table
employee_name
employee_id


department table 
department_name
department_id
employee_id


salary table
employee_id
salary

list the 3rd highest salary in every dept

with rankedSalaries as (

select employee_name,department_id, s.salary, dense_rank() over(partition by department_name order by salary desc) as rnk
 from employee e
 join department d on e.employee_id=d.employee_id
 join salary s on e.employee_id=s.employee_id
) 
select employee_name,department_id, s.salary
from rankedSalaries
where rnk=3

dept 1 
abc 8000 1
def 8000 1
