def memoised_find_target_sum_ways(seen, i, curr, nums, target):
    if i == len(nums):
        return 1 if curr == target else 0

    if (i, curr) in seen:
        return seen[(i, curr)]

    add = memoised_find_target_sum_ways(seen, i + 1, curr + nums[i], nums, target)
    subtract = memoised_find_target_sum_ways(seen, i + 1, curr - nums[i], nums, target)
    seen[(i, curr)] = add + subtract
    return seen[(i, curr)]


def find_target_sum_ways(nums, target):
    return memoised_find_target_sum_ways({}, 0, 0, nums, target)
