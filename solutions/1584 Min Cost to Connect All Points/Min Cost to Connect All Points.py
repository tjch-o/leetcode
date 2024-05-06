import heapq

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def min_cost_connect_points(points):
    n = len(points)
    visited = set()
    cost = 0
    # can just start from 0 since we need to visit all the points anyway
    pq = [(0, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:
        curr = heapq.heappop(pq)
        curr_cost = curr[0]
        curr_i = curr[1]
        curr_p = points[curr_i]

        if curr_i in visited:
            continue

        cost += curr_cost
        visited.add(curr_i)

        for i in range(n):
            if i not in visited:
                p = points[i]
                d = manhattan(curr_p, p)
                heapq.heappush(pq, (d, i))

    return cost
