select email
from (
        select email,
            count(*) as count
        from Person
        group by email
    ) as result
where count > 1;