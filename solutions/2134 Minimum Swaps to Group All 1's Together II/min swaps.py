def min_swaps(nums):
    n = len(nums)
    total_ones = sum(nums)

    if total_ones == 0 or total_ones == n:
        return 0

    curr_ones, max_ones = 0, 0
    arr = nums + nums

    for i in range(total_ones):
        if arr[i] == 1:
            curr_ones += 1
    max_ones = curr_ones

    for i in range(total_ones, 2 * n):
        start = i - total_ones

        if arr[start] == 1:
            curr_ones -= 1
        if arr[i] == 1:
            curr_ones += 1
        if curr_ones > max_ones:
            max_ones = curr_ones
    return total_ones - max_ones
