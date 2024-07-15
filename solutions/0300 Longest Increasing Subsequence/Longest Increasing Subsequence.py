def length_of_LIS(nums):
    n = len(nums)
    # table stores length of LIS ending at the index, not the highest value seen
    table = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)
