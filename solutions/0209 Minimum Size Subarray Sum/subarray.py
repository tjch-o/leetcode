def min_subarray_len(target, nums):
    if sum(nums) < target:
        return 0

    left, right = 0, 0
    curr = 0
    min_length = float("inf")

    for right in range(len(nums)):
        curr += nums[right]

        while curr >= target:
            min_length = min(min_length, right - left + 1)
            curr -= nums[left]
            left += 1
    return min_length
