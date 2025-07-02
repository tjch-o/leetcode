def min_extra_char(s, dictionary):
    n = len(s)
    table = [float("inf") for _ in range(n + 1)]
    table[0] = 0

    for i in range(1, n + 1):
        table[i] = table[i - 1] + 1

        for word in dictionary:
            if i >= len(word) and s[i - len(word) : i] == word:
                table[i] = min(table[i], table[i - len(word)])
    return table[n]
