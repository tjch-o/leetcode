def wordBreak(s, wordDict):
    n = len(s)
    table = [False for _ in range(n + 1)]
    table[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            current_substring = s[j:i]
            if table[j] and current_substring in wordDict:
                table[i] = True
                break
    
    return table[n]