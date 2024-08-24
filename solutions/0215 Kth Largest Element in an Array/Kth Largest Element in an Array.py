import heapq


def kth_largest_element(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    return heapq.heappop(nums)
