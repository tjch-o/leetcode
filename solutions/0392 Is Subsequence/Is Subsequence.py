def is_subsequence(s, t):
    if not s:
        return True
    else:
        ptr = 0
        for char in t:
            if s[ptr] == char:
                ptr += 1
                if ptr == len(s):
                    return True
        return False
