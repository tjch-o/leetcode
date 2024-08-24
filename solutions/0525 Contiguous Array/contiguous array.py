def find_max_length(nums):
    ones = 0
    zeroes = 0
    diff_to_index = {}
    max_len = 0

    for i, num in enumerate(nums):
        if num == 0:
            zeroes += 1
        else:
            ones += 1
        
        diff = ones - zeroes

        if diff not in diff_to_index:
            diff_to_index[diff] = i

        if diff == 0:
            max_len = ones + zeroes
        else:
            # find first index where this difference appeared so that everything after will be balanced
            earliest = diff_to_index[diff]
            max_len = max(max_len, i - earliest)
    return max_len
