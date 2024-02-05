def insert(intervals, new_interval):
    result = []
    inserted_flag = False

    for interval in intervals:
        # new interval is completely before current interval
        if interval[0] > new_interval[1]:
            if not inserted_flag:
                result.append(new_interval)
                inserted_flag = True
            result.append(interval)

        # new interval is completely after current interval
        elif interval[1] < new_interval[0]:
            result.append(interval)

        else:
            # dont insert after updating the new interval to handle the overlap because of double counting
            min_start = min(interval[0], new_interval[0])
            max_end = max(interval[1], new_interval[1])
            new_interval = [min_start, max_end]

    # new interval is all the way at the end and is not inserted yet
    if not inserted_flag:
        result.append(new_interval)
    return result
