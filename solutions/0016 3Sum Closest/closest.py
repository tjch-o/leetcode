def three_sum_closest(nums, target):
    n = len(nums)
    nums.sort()
    closest = float("inf")
    result = 0

    for i in range(n):
        curr = nums[i]
        left, right = i + 1, n -1

        while left < right:
            curr_sum = nums[left] + nums[right] + curr

            if curr_sum == target:
                return target
            
            x = curr_sum - target

            if abs(x) < closest:
                closest = abs(x)
                result = curr_sum
            
            if curr_sum > target:
                right -= 1
            else:
                left += 1
    return result
