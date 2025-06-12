def single_number(nums):
    res = 0

    for num in nums:
        res ^= num
    return res
