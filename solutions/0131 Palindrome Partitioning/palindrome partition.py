def is_palindrome(s):
    return s == s[::-1]


def backtrack(s, res, acc, start):
    if start == len(s):
        res.append(acc[:])
        return

    for i in range(start, len(s)):
        if is_palindrome(s[start : i + 1]):
            acc.append(s[start : i + 1])
            backtrack(s, res, acc, i + 1)
            acc.pop()


def partition(s):
    res = []
    backtrack(s, res, [], 0)
    return res
