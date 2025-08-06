from collections import Counter
import heapq


def top_k_frequent(nums, k):
    counts = Counter(nums)
    heap = []
    heapq.heapify(heap)
    res = []

    for elem, v in counts.items():
        heapq.heappush(heap, (-v, elem))

    while len(res) < k:
        _, elem = heapq.heappop(heap)
        res.append(elem)
    return res
