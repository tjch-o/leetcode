def backtrack(nums, curr, start, res):
    res.append(curr[:])

    for i in range(start, len(nums)):
        while i > start and nums[i] == nums[i - 1]:
            i += 1

        curr.append(nums[i])
        backtrack(nums, curr, i + 1, res)
        curr.pop()


def subsets(nums):
    nums.sort()
    res = []
    backtrack(nums, [], 0, res)
    return res
