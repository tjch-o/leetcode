def my_atoi(s):
    s = s.strip()
    n = len(s)
    result = ""
    positive = True
    sign_set = False
    lower = -(2**31)
    upper = 2**31 - 1

    for i in range(n):
        if not result and not sign_set and s[i] == "-":
            positive = False
            sign_set = True
            continue
        elif not result and not sign_set and s[i] == "+":
            sign_set = True
            continue

        if not s[i].isdigit():
            break
        result += s[i]

    if not result:
        return 0
    elif not positive:
        result = int("-" + result)
    else:
        result = int(result)

    if result < lower:
        result = lower
    elif result > upper:
        result = upper
    return result
