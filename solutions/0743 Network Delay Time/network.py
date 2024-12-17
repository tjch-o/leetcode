from collections import defaultdict
import heapq


def network_delay_time(times, n, k):
    graph = defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))

    dists = [float("inf") for _ in range(n + 1)]
    dists[k] = 0
    pq = [(0, k)]
    heapq.heapify(pq)

    while pq:
        curr_t, node = heapq.heappop(pq)

        if curr_t > dists[node]:
            continue

        for neighbour, weight in graph[node]:
            t = curr_t + weight

            if t < dists[neighbour]:
                dists[neighbour] = t
                heapq.heappush(pq, (t, neighbour))

    s = max(dists[1:])
    return s if s < float("inf") else -1
