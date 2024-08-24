def erase_overlap_intervals(intervals):
    count = 0

    intervals.sort(key=lambda x: x[1])

    prev = (intervals[0][0], intervals[0][1])
    ptr = 1
    n = len(intervals)

    while ptr < n:
        start, end = intervals[ptr]
        _, prev_y = prev

        if prev_y <= start:
            prev = (start, end)
        else:
            count += 1

        ptr += 1
    return count
