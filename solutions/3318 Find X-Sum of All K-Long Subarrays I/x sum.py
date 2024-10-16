from collections import Counter
import heapq


def get_x_sum(nums, start, end, x):
    counts = Counter(nums[start : end + 1])
    value_counts = list(counts.items())
    heap = list(map(lambda x: (-x[1], -x[0]), value_counts))

    heapq.heapify(heap)
    x_sum = 0

    while heap and x > 0:
        count, val = heapq.heappop(heap)
        x_sum += -val * -count
        x -= 1
    return x_sum


def find_x_sum(nums, k, x):
    n = len(nums)

    if n < x:
        return [sum(nums)]

    res = []
    for i in range(n - k + 1):
        res.append(get_x_sum(nums, i, i + k - 1, x))
    return res
