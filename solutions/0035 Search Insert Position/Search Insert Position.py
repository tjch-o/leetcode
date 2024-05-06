def search_insert(nums, target):
    def helper(lower, upper):
        middle = lower + (upper - lower) // 2  
        
        if lower > upper:
            return middle + 1
        elif target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return helper(lower, middle - 1)  
        else:
            return helper(middle + 1, upper)
        
    return helper(0, len(nums) - 1) 