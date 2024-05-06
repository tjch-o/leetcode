def length_of_LIS(nums):
    if not nums:
        return 0

    # table stores length of LIS ending at the index, not the highest value seen
    table = [1 for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)
