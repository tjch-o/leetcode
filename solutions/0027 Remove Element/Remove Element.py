def removeElement(nums, val):
    count = len(nums)

    for i in range(len(nums)):
        if nums[i] == val:
            count -= 1

    start = 0
    end = len(nums) - 1

    # order of elements do not matter
    while start < end:
        if nums[start] != val:
            start += 1
        else:
            if nums[end] != val:
                nums[start], nums[end] = nums[end], nums[start]
            end -= 1
    return count
