def word_break(s, word_dict):
    n = len(s)
    table = [False for _ in range(n + 1)]
    table[0] = True

    for end in range(1, n + 1):
        for start in range(end):
            if table[start] and s[start:end] in word_dict:
                table[end] = True
                break
    return table[n]
