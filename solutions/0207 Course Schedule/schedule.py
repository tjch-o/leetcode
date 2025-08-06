from collections import defaultdict, deque


def can_finish(num_courses, prerequisites):
    courses = defaultdict(list)
    in_degrees = [0 for _ in range(num_courses)]

    for course, prereq in prerequisites:
        courses[prereq].append(course)
        in_degrees[course] += 1

    queue = deque()
    count = 0

    for i in range(num_courses):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        course = queue.popleft()
        count += 1

        for neighbour in courses[course]:
            in_degrees[neighbour] -= 1

            if in_degrees[neighbour] == 0:
                queue.append(neighbour)
    return count == num_courses
