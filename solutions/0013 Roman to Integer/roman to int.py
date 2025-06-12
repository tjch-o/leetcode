def roman_to_int(s):
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    subtraction_mapping = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    n = len(s)
    res = 0
    i = 0

    while i < n:
        if s[i : i + 2] in subtraction_mapping:
            res += subtraction_mapping[s[i : i + 2]]
            i += 2
        else:
            res += mapping[s[i]]
            i += 1
    return res
