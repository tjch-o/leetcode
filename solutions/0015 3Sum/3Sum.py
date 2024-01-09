def threeSum(nums):
    nums.sort()
    # no need to check equality of triplets
    result = set()

    for i in range(len(nums)):
        current = nums[i]
        # they want left, right and i to be all different values
        left = i + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[left] + nums[right] + current
            if currentSum == 0:
                result.add((nums[left], nums[right], current))
                left += 1
                right -= 1
            elif currentSum > 0:
                right -= 1
            else:
                left += 1
    return list(result)
