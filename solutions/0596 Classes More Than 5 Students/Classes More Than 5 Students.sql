select class
from (
        select class,
            count(class) as num
        from Courses
        group by class
    ) as result
where num >= 5;