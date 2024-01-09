def romanToInt(s):
    table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    
    for i in range(len(s)):
        key = s[i]
        value = table.get(s[i])
        if i < len(s) - 1:
            if key == "I" and (s[i + 1] == "V" or s[i + 1] == "X") and i < len(s) - 1:
                sum -= value
            elif key == "X" and (s[i + 1] == "L" or s[i + 1] == "C") and i < len(s) - 1:
                sum -= value
            elif key == "C" and (s[i + 1] == "D" or s[i + 1] == "M") and i < len(s) - 1:
                sum -= value
            else:
                sum += value
        else:
            sum += value
    return sum
