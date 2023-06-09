def removeStars(s):
    lst = []
    for char in s:
        if char != "*":
            lst.append(char)
        else:
            lst.pop()
    return "".join(lst)