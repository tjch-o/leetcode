def permute(nums):
    if not nums:
        return [[]]

    result = []
    for i in range(len(nums)):
        curr = nums[i]
        complement = nums[:i] + nums[i + 1 :]

        for elem in permute(complement):
            result.append(elem + [curr])
    return result
