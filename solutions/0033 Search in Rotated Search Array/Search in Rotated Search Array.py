def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = start + (end - start) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] >= nums[start]:
            if nums[start] <= target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if nums[middle] < target <= nums[end]:
                start = middle + 1
            else:
                end = middle - 1

    return -1
