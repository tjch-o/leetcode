def backtrack(nums, i, curr, res):
    res.append(curr[:])

    for j in range(i, len(nums)):
        if j > i and nums[j] == nums[j - 1]:
            continue

        curr.append(nums[j])
        backtrack(nums, j + 1, curr, res)
        curr.pop()


def subsets_with_duplicates(nums):
    nums.sort()
    res = []
    backtrack(nums, 0, [], res)
    return res
