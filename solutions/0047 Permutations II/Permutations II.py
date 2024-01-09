def permuteUnique(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums]
    else:
        result = []

        for i in range(len(nums)):
            current_element = nums[i]
            remaining_lst = nums[:i] + nums[i + 1 :]
            for p in permuteUnique(remaining_lst):
                if [current_element] + p not in result:
                    result.append([current_element] + p)

        return result
