def longest_consecutive(nums):
    seen = set(nums)
    curr = 0
    curr_l = 0
    longest = 0

    for num in seen:
        if num - 1 not in seen:
            curr = num
            curr_l = 1

            while curr + 1 in seen:
                curr_l += 1
                curr += 1
            longest = max(longest, curr_l)
    return longest
