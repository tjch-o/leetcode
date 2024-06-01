def reverse_string(s):
    # cannot just use s[::-1] as that creates an extra array when requirement is O(1) space
    i = 0
    j = len(s) - 1
    
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s