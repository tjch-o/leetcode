def maximum_swap(num):
    digits = list(str(num))
    last_seen = {}

    for i in range(len(digits)):
        last_seen[int(digits[i])] = i

    for j in range(len(digits)):
        curr = int(digits[j])
        for i in range(9, curr, -1):
            if i in last_seen and last_seen[i] > j:
                digits[j], digits[last_seen[i]] = digits[last_seen[i]], digits[j]
                return int("".join(digits))
    return num
