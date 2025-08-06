def backtrack(nums, curr, res, used):
    if len(curr) == len(nums):
        res.append(curr[:])
        return

    for i in range(len(nums)):
        if i in used:
            continue

        used.add(i)
        curr.append(nums[i])
        backtrack(nums, curr, res, used)
        curr.pop()
        used.remove(i)


def permute(nums):
    res = []
    used = set()
    backtrack(nums, [], res, used)
    return res
