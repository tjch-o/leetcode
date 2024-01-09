select e1.employee_id,
    e1.department_id
from employee e1
group by e1.employee_id
having count(e1.employee_id) = 1
union
select e2.employee_id,
    e2.department_id
from employee e2
where e2.primary_flag = 'Y';