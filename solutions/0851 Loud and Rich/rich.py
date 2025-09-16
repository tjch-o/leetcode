from collections import defaultdict, deque


def loud_and_rich(richer, quiet):
    n = len(quiet)
    graph = defaultdict(list)
    in_degrees = [0 for _ in range(n)]

    for a, b in richer:
        graph[a].append(b)
        in_degrees[b] += 1

    res = [i for i in range(n)]
    queue = deque()

    for i in range(n):
        if in_degrees[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()

        for neighbour in graph[curr]:
            if quiet[res[neighbour]] > quiet[res[curr]]:
                res[neighbour] = res[curr]

            in_degrees[neighbour] -= 1
            if in_degrees[neighbour] == 0:
                queue.append(neighbour)
    return res
