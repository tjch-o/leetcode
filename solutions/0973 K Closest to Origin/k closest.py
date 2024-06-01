from math import sqrt
import heapq


def euclid_dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def k_closest(points, k):
    if not points or len(points) == k:
        return points

    dists = []

    for x, y in points:
        dists.append((euclid_dist(0, 0, x, y), (x, y)))

    heapq.heapify(dists)
    closest = []

    for _ in range(k):
        closest.append(heapq.heappop(dists)[1])
    return closest
