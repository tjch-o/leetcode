select r.contest_id,
    round((count(u.user_id) / total_users_count) * 100, 2) as percentage
from users u,
    register r
    join (
        select count(u.user_id) as total_users_count
        from users u
    ) as total_users
where u.user_id = r.user_id
group by r.contest_id
order by percentage desc,
    r.contest_id asc;