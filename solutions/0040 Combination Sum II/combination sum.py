def backtrack(nums, target, start, curr, res):
    if target == 0:
        res.append(curr[:])
        return

    for i in range(start, len(nums)):
        if nums[i] > target:
            break

        if i > start and nums[i] == nums[i - 1]:
            continue

        curr.append(nums[i])
        backtrack(nums, target - nums[i], i + 1, curr, res)
        curr.pop()


def combination_sum(nums, target):
    nums.sort()
    res = []
    backtrack(nums, target, 0, [], res)
    return res
