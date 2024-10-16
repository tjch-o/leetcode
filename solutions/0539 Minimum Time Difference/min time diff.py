def convert_to_mins(h, m):
    return h * 60 + m


def get_difference(t1, t2):
    d = abs(t1 - t2)
    return min(d, 24 * 60 - d)


def find_min_difference(time_points):
    n = len(time_points)
    min_diff = float("inf")
    mins = []

    for t in time_points:
        h, m = t.split(":")
        mins.append(convert_to_mins(int(h), int(m)))

    for i in range(n):
        for j in range(i):
            d = get_difference(mins[i], mins[j])
            if d == 0:
                return d
            min_diff = min(min_diff, d)
    return min_diff
