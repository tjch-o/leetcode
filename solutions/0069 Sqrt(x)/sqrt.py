def sqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid
        elif square > x:
            right = mid - 1
        else:
            left = mid + 1
    return right
