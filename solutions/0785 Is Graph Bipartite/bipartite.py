from collections import deque


def is_bipartite(graph):
    n = len(graph)
    colours = [-1 for _ in range(n)]

    for i in range(n):
        if colours[i] == -1:
            queue = deque()
            queue.append(i)

            colours[i] = 0

            while queue:
                curr = queue.popleft()

                for neighbour in graph[curr]:
                    if colours[neighbour] == -1:
                        colours[neighbour] = 1 - colours[curr]
                        queue.append(neighbour)
                    elif colours[neighbour] == colours[curr]:
                        return False
    return True
