def subsets(nums):
    result = [[]]

    for num in nums:
        prev = result
        new = [elem + [num] for elem in prev]
        result.extend(new)
    return result
