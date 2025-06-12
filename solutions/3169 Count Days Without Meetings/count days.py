def count_days(days, meetings):
    meetings.sort(key=lambda x: x[0])
    non_overlapping_meetings = []

    for start, end in meetings:
        if non_overlapping_meetings and non_overlapping_meetings[-1][1] >= start:
            non_overlapping_meetings[-1][1] = max(non_overlapping_meetings[-1][1], end)
        else:
            non_overlapping_meetings.append([start, end])

    free_days = days
    for start, end in non_overlapping_meetings:
        free_days -= end - start + 1
    return free_days
