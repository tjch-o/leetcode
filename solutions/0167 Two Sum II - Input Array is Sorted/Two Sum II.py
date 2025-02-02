def two_sum(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        curr = nums[start] + nums[end]
        if curr == target:
            return [start + 1, end + 1]
        elif curr < target:
            start += 1
        else:
            end -= 1
