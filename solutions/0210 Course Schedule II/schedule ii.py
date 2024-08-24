from collections import defaultdict, deque


def find_order(num_courses, prerequisites):
    courses = defaultdict(list)
    degrees = [0 for _ in range(num_courses)]
    path = []

    for course, prereq in prerequisites:
        courses[prereq].append(course)
        degrees[course] += 1

    queue = deque()

    for i in range(num_courses):
        if degrees[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        path.append(curr)

        for neighbour in courses[curr]:
            degrees[neighbour] -= 1
            if degrees[neighbour] == 0:
                queue.append(neighbour)

    if len(path) != num_courses:
        return []
    return path
