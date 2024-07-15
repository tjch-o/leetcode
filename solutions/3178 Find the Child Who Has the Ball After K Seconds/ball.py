def number_of_child(n, k):
    pos = 0
    count = 0
    forward = True

    while count < k:
        if forward:
            pos += 1

            if pos == n - 1:
                forward = False
        else:
            pos -= 1

            if pos == 0:
                forward = True

        count += 1

    return pos
