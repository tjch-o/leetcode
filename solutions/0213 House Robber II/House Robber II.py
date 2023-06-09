def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    table1 = [0 for _ in range(len(nums) - 1)]
    table2 = [0 for _ in range(len(nums) - 1)]
    
    # Case 1: we rob the first house and not the last since first house is adjacent to last
    table1[0] = nums[0]
    if len(table1) > 1:
        table1[1] = max(nums[0], nums[1])
    for i in range(2, len(nums) - 1):
        table1[i] = max(table1[i - 1], table1[i - 2] + nums[i])
    max1 = table1[len(nums) - 2]
    
    # Case 2: we rob the last house and not the first 
    table2[0] = nums[1]
    if len(table2) > 1:
        table2[1] = max(nums[1], nums[2])
    for i in range(2, len(nums) - 1):
        # because we excluded the first house so must + 1
        table2[i] = max(table2[i - 1], table2[i - 2] + nums[i + 1])
    max2 = table2[len(nums) - 2]
    
    return max(max1, max2)