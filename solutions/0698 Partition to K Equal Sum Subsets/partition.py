def backtrack(nums, used, start, curr_sum, target, remaining_subsets):
    if remaining_subsets == 1:
        return True

    if curr_sum == target:
        return backtrack(nums, used, 0, 0, target, remaining_subsets - 1)

    for i in range(start, len(nums)):
        if not used[i] and curr_sum + nums[i] <= target:
            used[i] = True

            if backtrack(
                nums, used, i + 1, curr_sum + nums[i], target, remaining_subsets
            ):
                return True

            used[i] = False

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            if curr_sum == 0:
                break
    return False


def can_partition_k_subsets(nums, k):
    n = len(nums)
    total_sum = sum(nums)
    target = total_sum // k

    if target * k != total_sum:
        return False

    used = [False for _ in range(n)]
    nums.sort(reverse=True)
    return backtrack(nums, used, 0, 0, target, k)
