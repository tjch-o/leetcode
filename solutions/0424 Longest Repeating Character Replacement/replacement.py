def character_replacement(s, k):
    n = len(s)
    left = 0
    right = 0
    counts = {}
    result = 0

    for i in range(65, 91):
        counts[chr(i)] = 0

    while right < n:
        curr = s[right]
        counts[curr] += 1

        window_size = right - left + 1
        max_freq = max(counts.values())
        num_chars_to_replace = window_size - max_freq

        if num_chars_to_replace <= k:
            result = max(result, window_size)
        else:
            # shift the window
            counts[s[left]] -= 1
            left += 1
        
        right += 1
    return result
