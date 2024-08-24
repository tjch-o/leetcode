def longest_consecutive(nums):
    if len(nums) <= 1:
        return len(nums)

    curr_streak = 0
    curr = float("-inf")
    longest = 0
    seen = set(nums)

    for num in seen:
        # check if start of sequence
        if num - 1 not in seen:
            curr = num
            curr_streak = 1

            while curr + 1 in seen:
                curr += 1
                curr_streak += 1

            longest = max(longest, curr_streak)
    return longest
