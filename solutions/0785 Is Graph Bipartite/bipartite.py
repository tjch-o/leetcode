from collections import deque


def is_bipartite(graph):
    n = len(graph)
    colours = [-1 for _ in range(n)]
    queue = deque()

    for u in range(n):
        if colours[u] != -1:
            continue

        queue.append((u, 0))

        while queue:
            curr, colour = queue.popleft()

            if colours[curr] == -1:
                colours[curr] = colour
            elif colours[curr] != colour:
                return False

            for neighbour in graph[curr]:
                opp_colour = 1 if colour == 0 else 0

                if colours[neighbour] == -1:
                    queue.append((neighbour, opp_colour))
                elif colours[neighbour] == colours[curr]:
                    return False
    return True
