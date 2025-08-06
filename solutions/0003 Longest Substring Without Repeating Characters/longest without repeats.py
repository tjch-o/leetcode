def length_of_longest_substring(s):
    last_seen = {}
    start = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] in last_seen:
            start = max(start, last_seen[s[i]] + 1)

        last_seen[s[i]] = i
        max_length = max(max_length, i - start + 1)
    return max_length
