def min_taps(n, ranges):
    intervals = []

    for i, r in enumerate(ranges):
        start = max(0, i - r)
        end = i + r
        intervals.append([start, end])

    intervals.sort()

    i = 0
    curr_end = 0
    taps = 0

    while curr_end < n:
        max_end = curr_end

        while i < len(intervals) and intervals[i][0] <= curr_end:
            max_end = max(max_end, intervals[i][1])
            i += 1

        if max_end == curr_end:
            return -1

        curr_end = max_end
        taps += 1
    return taps
