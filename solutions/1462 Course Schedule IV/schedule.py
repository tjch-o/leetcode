from collections import defaultdict, deque


def check_if_prerequisite(num_courses, prerequisites, queries):
    graph = defaultdict(list)

    for prereq, course in prerequisites:
        graph[course].append(prereq)

    prereq_map = defaultdict(set)

    for i in range(num_courses):
        queue = deque()
        queue.append(i)

        while queue:
            curr = queue.popleft()

            for neighbour in graph[curr]:
                if neighbour not in prereq_map[i]:
                    prereq_map[i].add(neighbour)
                    queue.append(neighbour)

    res = []
    for u, v in queries:
        res.append(True if u in prereq_map[v] else False)
    return res
