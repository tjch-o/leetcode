def longest_palindrome(s):
    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]
    longest = ""

    for i in range(n):
        table[i][i] = True
        longest = s[i]

    for end in range(n):
        for start in range(end):
            if s[start] == s[end]:
                if table[start + 1][end - 1] or end - start <= 1:
                    table[start][end] = True
                    if end - start >= len(longest):
                        longest = s[start : end + 1]

    return longest
