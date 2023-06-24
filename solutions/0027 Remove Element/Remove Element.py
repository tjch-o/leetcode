def removeElement(nums, val):
    if not nums:
        return 0 
    
    dont_count = max(nums) + 1
    
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = dont_count

    nums.sort()

    number_left = 0
    for x in nums:
        if x == dont_count:
            break
        else:
            number_left += 1

    return number_left