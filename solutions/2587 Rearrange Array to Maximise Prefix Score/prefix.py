def max_score(nums):
    nums.sort(reverse=True)
    count = 0
    curr_score = 0

    for i in range(len(nums)):
        curr_score += nums[i]

        if curr_score <= 0:
            break

        count += 1
    return count
