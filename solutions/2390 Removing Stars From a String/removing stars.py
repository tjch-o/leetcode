def remove_stars(s):
    lst = []
    for char in s:
        if char != "*":
            lst.append(char)
        else:
            lst.pop()
    return "".join(lst)
