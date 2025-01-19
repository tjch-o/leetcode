import heapq


def smallest_range(nums):
    n = len(nums)
    heap = []
    heapq.heapify(heap)

    max_val = float("-inf")

    for i in range(n):
        heapq.heappush(heap, (nums[i][0], i, 0))
        max_val = max(max_val, nums[i][0])

    res = [float("-inf"), max_val]

    while len(heap) == n:
        min_val, i, j = heapq.heappop(heap)

        if max_val - min_val < res[1] - res[0]:
            res = [min_val, max_val]

        if j + 1 < len(nums[i]):
            heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
            max_val = max(max_val, nums[i][j + 1])
    return res
