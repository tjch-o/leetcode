select t.teacher_id,
    count(distinct t.subject_id) as cnt
from teacher t
group by t.teacher_id;