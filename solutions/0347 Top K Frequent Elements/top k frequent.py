from collections import Counter
import heapq


def top_k_frequent(nums, k):
    counts = Counter(nums)
    heap = []
    result = []

    for key, count in counts.items():
        heap.append((-count, key))

    heapq.heapify(heap)

    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result
