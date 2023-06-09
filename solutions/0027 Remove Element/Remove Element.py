def removeElement(nums,val):
    # they want O(1) extra memory that means no creating new arrays
    # how im going to weed out the elements removed without using strings to indicate
    if not nums:
        return 0 # nothing to remove
    
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