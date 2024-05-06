def permute_unique(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums]
    else:
        result = []

        for i in range(len(nums)):
            curr = nums[i]
            remaining_lst = nums[:i] + nums[i + 1 :]
            for p in permute_unique(remaining_lst):
                if [curr] + p not in result:
                    result.append([curr] + p)

        return result
