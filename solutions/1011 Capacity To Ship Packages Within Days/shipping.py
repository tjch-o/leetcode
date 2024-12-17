def can_ship(weights, x, days):
    count = 1
    curr = 0

    for w in weights:
        if curr + w > x:
            count += 1
            curr = 0

            if count > days:
                return False
        curr += w
    return True


def ship_within_days(weights, days):
    start = max(weights)
    end = sum(weights)

    while start < end:
        mid = start + (end - start) // 2
        if can_ship(weights, mid, days):
            end = mid
        else:
            start = mid + 1
    return start
