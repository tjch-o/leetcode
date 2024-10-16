def is_interleaving(s1, s2, s3):
    m, n, o = len(s1), len(s2), len(s3)

    if m + n != o:
        return False
    
    table = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    table[0][0] = True

    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and table[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                table[i][j] = True
            
            if j > 0 and table[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                table[i][j] = True
    return table[m][n]