def longest_consecutive(nums):
    if not nums:
        return 0

    curr_length = 0
    max_length = 0
    num_set = set(nums)

    for number in num_set:
        curr_number = number
        
        # find values that have no left neighbour on the number line
        if curr_number - 1 not in num_set:
            curr_length = 1

            while curr_number + 1 in num_set:
                curr_length += 1
                curr_number += 1

        max_length = max(max_length, curr_length)
    return max_length
