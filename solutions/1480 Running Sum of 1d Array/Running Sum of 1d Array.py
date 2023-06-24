def runningSum(nums):
    n = len(nums)
    table = [0 for _ in range(n)]
    table[0] = nums[0]
    
    for i in range(1, n):
        table[i] = table[i - 1] + nums[i]
    return table