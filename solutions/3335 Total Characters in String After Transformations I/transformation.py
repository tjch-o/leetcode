def length_after_transformation(s, t):
    counts = [0 for _ in range(26)]
    mod = 10**9 + 7

    for c in s:
        counts[ord(c) - ord("a")] += 1

    for _ in range(t):
        new_counts = [0 for _ in range(26)]

        for i in range(26):
            if i == 25:
                new_counts[0] = (new_counts[0] + counts[i]) % mod
                new_counts[1] = (new_counts[1] + counts[i]) % mod
            else:
                new_counts[i + 1] = (new_counts[i + 1] + counts[i]) % mod

        counts = new_counts
    return sum(counts) % mod
