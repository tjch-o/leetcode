def simplify_path(path):
    parts = path.split("/")
    stack = []

    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)

    res = "/"
    res += "/".join(stack)
    return res
