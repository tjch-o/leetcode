def rotateString(s, goal):
    def shift(s):
        return s[1:] + s[0]

    max_shifts = len(s)

    shift_count = 0
    output = s
    while shift_count < max_shifts:
        output = shift(output)
        if output == goal:
            return True
        else:
            shift_count += 1

    return False
