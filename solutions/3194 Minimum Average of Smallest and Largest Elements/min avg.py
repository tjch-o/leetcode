import heapq


def minimum_average(nums):
    max_heap = list(map(lambda x: -x, nums))
    heapq.heapify(max_heap)

    min_heap = nums
    heapq.heapify(min_heap)

    n = len(nums)
    min_avg = float("inf")
    for _ in range(n // 2):
        low, high = heapq.heappop(min_heap), -1 * heapq.heappop(max_heap)
        avg = (low + high) / 2

        if avg < min_avg:
            min_avg = avg
    return min_avg
