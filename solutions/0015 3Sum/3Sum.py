def three_sum(nums):
    n = len(nums)
    result = set()
    nums.sort()

    for i in range(n):
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1

        while left < right:
            curr_sum = nums[left] + nums[right] + nums[i]

            if curr_sum == 0:
                result.add((nums[left], nums[right], nums[i]))
                left += 1
                right -= 1
            elif curr_sum > 0:
                right -= 1
            else:
                left += 1
    return list(result)
