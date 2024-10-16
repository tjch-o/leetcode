def longest_palindrome(s):
    if not s or len(s) == 1:
        return s
    
    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]
    max_l = 1
    longest = s[0]

    for i in range(n):
        table[i][i] = True

    for j in range(n):
        for i in range(j):
            if s[i] == s[j] and (table[i + 1][j - 1] or j - i <= 1):
                table[i][j] = True
                if j - i + 1 > max_l:
                    max_l = j - i + 1
                    longest = s[i: j + 1]
    return longest
