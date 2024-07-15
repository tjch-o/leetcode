def rob(nums):
    if not nums:
        return 0

    n = len(nums)
    if n == 1:
        return nums[0]

    table = [0 for _ in range(n)]
    table[0] = nums[0]
    table[1] = max(nums[0], nums[1])

    for i in range(2, n):
        table[i] = max(table[i - 2] + nums[i], table[i - 1])
    return table[n - 1]
