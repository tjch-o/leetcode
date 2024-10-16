import heapq


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def min_cost_connect_points(points):
    n = len(points)
    pq = [(0, 0)]
    heapq.heapify(pq)
    tc = 0
    visited = set()

    while len(visited) < n:
        cost, curr = heapq.heappop(pq)

        if curr in visited:
            continue

        visited.add(curr)
        tc += cost

        for i in range(n):
            if i not in visited:
                md = manhattan_dist(points[curr], points[i])
                heapq.heappush(pq, (md, i))
    return tc
