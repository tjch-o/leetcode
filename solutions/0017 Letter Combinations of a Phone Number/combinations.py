def backtrack(digits, mapping, i, curr, res):
    if i == len(digits):
        res.append(curr)
        return

    digit = digits[i]
    for c in mapping[digit]:
        backtrack(digits, mapping, i + 1, curr + c, res)


def letter_combinations(digits):
    if not digits:
        return []

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = []
    backtrack(digits, mapping, 0, "", res)
    return res
