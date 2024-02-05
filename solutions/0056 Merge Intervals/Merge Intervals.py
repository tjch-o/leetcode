def is_not_overlapping(interval1, interval2):
    return interval1[1] < interval2[0] or interval2[1] < interval1[0]


def merge_overlapping_intervals(interval1, interval2):
    lower = min(interval1[0], interval2[0])
    higher = max(interval1[1], interval2[1])
    return [lower, higher]


def merge(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for i in range(len(intervals)):
        if is_not_overlapping(result[-1], intervals[i]):
            result.append(intervals[i])
        else:
            result[-1] = merge_overlapping_intervals(result[-1], intervals[i])
    return result
