def reverse_string(s):
    if len(s) <= 1:
        return s

    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
