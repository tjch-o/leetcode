def three_sum_smaller(nums, target):
    n = len(nums)
    nums.sort()
    count = 0

    for i in range(n):
        start, end = i + 1, n - 1

        while start < end:
            curr_sum = nums[i] + nums[start] + nums[end]

            if curr_sum >= target:
                end -= 1
            else:
                count += end - start
                start += 1
    return count
