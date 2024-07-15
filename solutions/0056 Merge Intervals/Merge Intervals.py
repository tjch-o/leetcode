def does_not_overlap(i1, i2):
    return i1[1] < i2[0] or i2[1] < i1[0]


def merge_interval(i1, i2):
    return [min(i1[0], i2[0]), max(i1[1], i2[1])]


def merge(intervals):
    result = []

    intervals.sort(key=lambda x: x[0])

    for interval in intervals:
        if not result or does_not_overlap(result[-1], interval):
            result.append(interval)
        else:
            result[-1] = merge_interval(result[-1], interval)
    return result
