def find_min(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2

        # second half is sorted
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid + 1
    return nums[start]
