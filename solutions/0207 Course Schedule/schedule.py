from collections import deque, defaultdict


def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    num_prereqs = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        num_prereqs[course] += 1

    queue = deque()

    # do topological sort by adding all courses with no prerequisites into the queue
    for i in range(num_courses):
        if num_prereqs[i] == 0:
            queue.append(i)

    processed = 0

    while queue:
        curr = queue.popleft()
        processed += 1

        for course in graph[curr]:
            num_prereqs[course] -= 1

            if num_prereqs[course] == 0:
                queue.append(course)

    return processed == num_courses
