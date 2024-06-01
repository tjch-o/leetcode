def move_zeroes(nums):
    leftmost_zero = 0

    for i, num in enumerate(nums):
        if num != 0:
            if i != leftmost_zero:
                nums[leftmost_zero], nums[i] = nums[i], nums[leftmost_zero]
            leftmost_zero += 1
    return nums
