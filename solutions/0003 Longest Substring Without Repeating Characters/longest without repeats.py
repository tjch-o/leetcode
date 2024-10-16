def length_of_longest_substring(s):
    n = len(s)
    curr = ""
    max_l = 0

    for i in range(n):
        if s[i] in curr:
            j = curr.index(s[i])
            curr = curr[j + 1 :]

        curr += s[i]
        max_l = max(max_l, len(curr))
    return max_l
