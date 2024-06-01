def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [i, seen[target - nums[i]]]
        else:
            if nums[i] not in seen:
                seen[nums[i]] = i
