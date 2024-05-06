def longest_palindrome(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    curr_longest = ""
    
    for i in range(n):
        for j in range(i, -1, -1):
            if s[j] == s[i] and (i - j <= 1 or dp[j + 1][i - 1]):
                dp[j][i] = True
                # equal is for length = 1
                if i - j >= len(curr_longest):
                    curr_longest = s[j:i + 1]
    
    return curr_longest
