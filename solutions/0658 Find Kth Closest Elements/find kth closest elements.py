def find_closest_elements(nums, k, x):
    left = 0
    right = len(nums) - 1

    while right - left >= k:
        if abs(nums[left] - x) <= abs(nums[right] - x):
            right -= 1
        else:
            left += 1
    return nums[left : left + k]
