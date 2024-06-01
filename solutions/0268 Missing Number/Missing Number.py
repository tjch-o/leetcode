def missing_number(nums):
    n = len(nums)
    range_sum = 0
    arr_sum = 0

    for i in range(n + 1):
        range_sum += i

    for i in range(n):
        arr_sum += nums[i]

    return range_sum - arr_sum
