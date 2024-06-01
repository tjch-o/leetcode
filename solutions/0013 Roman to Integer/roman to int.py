def roman_to_int(s):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    special_rules = ["IV", "IX", "XL", "XC", "CD", "CM"]
    n = len(s)
    start = 0
    result = 0

    while start < n:
        window = s[start : start + 2]

        if window in special_rules:
            result += values[window[1]] - values[window[0]]
            start += 2
        else:
            result += values[window[0]]
            start += 1
    return result
