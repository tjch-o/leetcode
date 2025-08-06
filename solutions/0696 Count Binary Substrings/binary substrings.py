def count_binary_substrings(s):
    counts = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            counts.append(count)
            count = 1
    counts.append(count)

    total = 0
    for i in range(1, len(counts)):
        total += min(counts[i - 1], counts[i])
    return total
