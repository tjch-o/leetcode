import heapq


def k_smallest_pairs(n1, n2, k):
    heap = []
    heapq.heapify(heap)
    res = []

    for i, num in enumerate(n2[:k]):
        heapq.heappush(heap, (n1[0] + num, 0, i))

    while len(res) < k:
        _, i1, i2 = heapq.heappop(heap)
        res.append((n1[i1], n2[i2]))

        if i1 + 1 < len(n1):
            heapq.heappush(heap, (n1[i1 + 1] + n2[i2], i1 + 1, i2))
    return res
