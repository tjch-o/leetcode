select e1.name
from Employee e1 as Employee
    join Employee e2 on e1.managerId = e2.id
where e1.salary > e2.salary;