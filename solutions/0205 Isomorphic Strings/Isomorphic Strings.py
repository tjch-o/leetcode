def isIsomorphic(s, t):
    n = len(s)
    table = {}

    for i in range(n):
        x = s[i]
        y = t[i]
        if x not in table and y not in table.values():
            table[x] = y
        elif x not in table and y in table.values():
            return False
        else:
            if table[x] != y:
                return False
    return True
