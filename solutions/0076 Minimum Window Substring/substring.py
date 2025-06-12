from collections import Counter, defaultdict


def min_window(s, t):
    if not s or not t or len(s) < len(t):
        return ""

    substring_counts = Counter(t)
    window_counts = defaultdict(int)
    left, right = 0, 0
    formed = 0
    required = len(substring_counts)
    min_length_left = 0
    min_length = float("inf")

    while right < len(s):
        curr = s[right]
        window_counts[curr] += 1

        if curr in substring_counts and window_counts[curr] == substring_counts[curr]:
            formed += 1

        while left <= right and formed == required:
            curr_window_length = right - left + 1

            if curr_window_length < min_length:
                min_length = curr_window_length
                min_length_left = left

            left_c = s[left]
            window_counts[left_c] -= 1

            if (
                left_c in substring_counts
                and window_counts[left_c] < substring_counts[left_c]
            ):
                formed -= 1

            left += 1

        right += 1

    if min_length == float("inf"):
        return ""
    return s[min_length_left : min_length_left + min_length]
