def sorted_squares(nums):
    left, right, pos = 0, len(nums) - 1, len(nums) - 1
    result = [0 for _ in range(len(nums))]

    while left <= right:
        if nums[left] ** 2 < nums[right] ** 2:
            result[pos] = nums[right] ** 2
            right -= 1
        else:
            result[pos] = nums[left] ** 2
            left += 1
        pos -= 1
    return result
