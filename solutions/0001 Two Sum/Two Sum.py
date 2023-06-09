def twoSum(nums, target):
    ref_nums = [x for x in nums]
    nums.sort()
    
    left = 0
    right = len(nums) - 1
    while (left < right):
        if nums[left] + nums[right] == target:
            break
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
            
    true_left = ref_nums.index(nums[left])
    if nums[left] == nums[right]:
        ref_nums.remove(nums[left])
        true_right = ref_nums.index(nums[right])
        return [true_left, true_right + 1]
    else:
        true_right = ref_nums.index(nums[right])
        return [true_left, true_right]