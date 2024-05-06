import heapq

def last_stone_weight(stones):
    # invert values for max heap
    stones = list(map(lambda x: -x, stones))
    heapq.heapify(stones)

    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)

        if x != y:
            y -= x
            heapq.heappush(stones, y)

    if len(stones) == 0:
        return 0
    return -heapq.heappop(stones)
