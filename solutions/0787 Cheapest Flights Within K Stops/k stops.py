import heapq
from collections import defaultdict


def find_cheapest_prices(n, flights, src, dst, k):
    if src == dst:
        return 0

    cheapest_prices = defaultdict(lambda: float("inf"))
    cheapest_prices[(src, 0)] = 0

    adj_list = defaultdict(list)
    for x, y, price in flights:
        adj_list[x].append((y, price))

    pq = [(0, src, 0)]
    heapq.heapify(pq)

    while pq:
        acc, curr, steps = heapq.heappop(pq)

        if curr == dst:
            return acc

        if steps > k:
            continue

        for neighbour, price in adj_list[curr]:
            new_cost = acc + price

            if new_cost < cheapest_prices[(neighbour, steps + 1)]:
                cheapest_prices[(neighbour, steps + 1)] = new_cost
                heapq.heappush(pq, (new_cost, neighbour, steps + 1))
    return -1
