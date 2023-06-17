def isSubsequence(s, t):
    if not s:
        return True
    else:
        pointer = 0
        for char in t:
            if s[pointer] == char:
                pointer += 1
                if pointer == len(s):
                    return True
        return False