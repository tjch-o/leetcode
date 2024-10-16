def longest_arithmetic_sequence(nums):
    n = len(nums)
    table = [{} for i in range(n)]
    longest = 0

    for j in range(n):
        for i in range(j):
            d = nums[j] - nums[i]

            if d in table[i]:
                table[j][d] = table[i][d] + 1
            else:
                table[j][d] = 2

            longest = max(longest, table[j][d])
    return longest
