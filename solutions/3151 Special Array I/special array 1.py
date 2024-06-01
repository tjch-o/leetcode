def is_array_special(nums):
    n = len(nums)

    for i in range(1, n):
        val_1, val_2 = nums[i - 1], nums[i]
        if val_1 & 1 == val_2 & 1:
            return False
    return True
