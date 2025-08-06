def gradient(p1, p2):
    rise = p2[1] - p1[1]
    run = p2[0] - p1[0]
    return rise / run if run != 0 else float("inf")


def check_straight_line(coordinates):
    curr = None

    for i in range(len(coordinates) - 1):
        p1, p2 = coordinates[i], coordinates[i + 1]

        if not curr:
            curr = gradient(p1, p2)
        elif curr and curr != gradient(p1, p2):
            return False
    return True
