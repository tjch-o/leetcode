def num_decodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    table = [0 for _ in range(n + 1)]
    table[0] = 1

    for i in range(1, n + 1):
        if s[i - 1] != '0':
            table[i] += table[i - 1]
        
        if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
            table[i] += table[i - 2]
    return table[n]
