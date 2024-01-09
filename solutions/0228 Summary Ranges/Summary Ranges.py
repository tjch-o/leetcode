def summaryRanges(nums):
    def range_string(start, end):
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
            output.append(range_string(start, end))
            start = nums[i + 1]
            end = nums[i + 1]

    output.append(range_string(start, end))
    return output
