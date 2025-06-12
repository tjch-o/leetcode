def can_ship_within_n_days(weights, limit, n):
    curr = 0
    days = 1

    for w in weights:
        if curr + w > limit:
            days += 1
            curr = 0

        curr += w
    return days <= n


def ship_within_days(weights, n):
    left, right = max(weights), sum(weights)

    while left < right:
        mid = left + (right - left) // 2

        if can_ship_within_n_days(weights, mid, n):
            right = mid
        else:
            left = mid + 1
    return left
