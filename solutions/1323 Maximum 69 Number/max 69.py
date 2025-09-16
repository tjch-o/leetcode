def max_69_number(num):
    s = list(str(num))

    for i in range(len(s)):
        if s[i] == "6":
            s[i] = "9"
            break
    return int("".join(s))
