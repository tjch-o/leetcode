def summaryRanges(nums):
    def rangeString(start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)
    
    if not nums:
        return []
    
    start = nums[0]
    end = nums[0]
    output = []
    
    for i in range(0, len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            end = nums[i + 1]
        else:
            output.append(rangeString(start, end))
            start = nums[i + 1]
            end = nums[i + 1]
    
    output.append(rangeString(start, end))        
    return output 