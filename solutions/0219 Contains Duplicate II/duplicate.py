def contains_nearby_duplicate(nums, k):
    seen = set()

    for i in range(len(nums)):
        if nums[i] in seen:
            return True

        seen.add(nums[i])

        if len(seen) > k:
            seen.remove(nums[i - k])
    return False
