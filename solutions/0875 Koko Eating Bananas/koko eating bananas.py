def can_finish(piles, h, k):
    if k == 0:
        return False

    count = 0
    for pile in piles:
        if pile % k == 0:
            count += pile // k
        else:
            count += pile // k + 1
    return count <= h


def min_eating_speed(piles, h):
    left = 0
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(piles, h, mid):
            right = mid
        else:
            left = mid + 1
    return right
