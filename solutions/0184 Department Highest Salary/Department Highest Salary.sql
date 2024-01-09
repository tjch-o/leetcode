select d.name as Department,
    e.name as Employee,
    e.salary as Salary
from employee e
    join department d on e.departmentId = d.id
where e.salary in (
        select max(e1.salary)
        from employee e1
        /* where clause is needed in the case where salary matches the highest salary in another 
        department but not highest in own department */
        where e.departmentId = e1.departmentId
        group by e1.departmentId
    );