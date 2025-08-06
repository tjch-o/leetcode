from collections import defaultdict, deque


def find_order(num_courses, prerequisites):
    courses = defaultdict(list)
    in_degrees = [0 for _ in range(num_courses)]

    for course, prereq in prerequisites:
        courses[prereq].append(course)
        in_degrees[course] += 1

    res = []
    queue = deque([])

    for i in range(num_courses):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        res.append(curr)

        for neighbour in courses[curr]:
            in_degrees[neighbour] -= 1

            if in_degrees[neighbour] == 0:
                queue.append(neighbour)

    if len(res) != num_courses:
        return []
    return res
