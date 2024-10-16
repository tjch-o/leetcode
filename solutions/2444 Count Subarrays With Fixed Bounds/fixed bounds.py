def is_outside_range(x, min_k, max_k):
    return x < min_k or x > max_k


def count_subarrays(nums, min_k, max_k):
    count = 0
    last_seen_invalid = -1
    last_seen_max = -1
    last_seen_min = -1

    for i, curr in enumerate(nums):
        if is_outside_range(curr, min_k, max_k):
            last_seen_invalid = i

        if curr == min_k:
            last_seen_min = i

        if curr == max_k:
            last_seen_max = i

        if last_seen_min != -1 and last_seen_max != -1:
            valid_subarr_start = min(last_seen_min, last_seen_max)
            count += max(0, valid_subarr_start - last_seen_invalid)
    return count
