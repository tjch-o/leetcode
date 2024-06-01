def fully_before_interval(intervals, i, new_interval):
    return intervals[i][1] < new_interval[0]


def insert(intervals, new_interval):
    i = 0
    n = len(intervals)
    result = []

    while i < n and fully_before_interval(intervals, i, new_interval):
        result.append(intervals[i])
        i += 1

    curr = new_interval

    while i < n and intervals[i][0] <= curr[1]:
        low = min(intervals[i][0], curr[0])
        high = max(intervals[i][1], curr[1])
        curr = [low, high]
        i += 1

    result.append(curr)

    for j in range(i, n):
        result.append(intervals[j])
    return result
