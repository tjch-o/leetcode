def count_substrings(s):
    n = len(s)
    table = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        # j is the start index while i is the end index of the substring
        for j in range(i, -1, -1):
            # check if first character is same as last
            if s[j] == s[i]:
                # check if the substring without first or last character is the same
                if i - j <= 1 or table[j + 1][i - 1]:
                    table[j][i] = True
                    count += 1

    return count
