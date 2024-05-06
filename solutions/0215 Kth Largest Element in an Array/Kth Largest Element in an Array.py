import heapq

def find_kth_largest(nums, k):
    heapq.heapify(nums)
    
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    
    return heapq.heappop(nums)
