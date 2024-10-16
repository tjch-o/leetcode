def subset_xor_sum(nums):
    n = len(nums)
    acc = 0

    for num in nums:
        acc |= num

    return acc * 2 ** (n - 1)
