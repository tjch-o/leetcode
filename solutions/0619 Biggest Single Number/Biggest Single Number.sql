select ifnull(
        (
            select num
            from (
                    select num,
                        count(num) as counter
                    from MyNumbers
                    group by num
                    order by num desc
                ) as result
            where counter = 1
            limit 1
        ), null
    ) as num;