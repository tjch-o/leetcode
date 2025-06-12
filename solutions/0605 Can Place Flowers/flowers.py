def can_place_flowers(flowerbed, n):
    m = len(flowerbed)
    count = n

    for i in range(m):
        if count == 0:
            return True

        if flowerbed[i] == 0:
            is_left_empty = i == 0 or flowerbed[i - 1] == 0
            is_right_empty = i == m - 1 or flowerbed[i + 1] == 0

            if is_left_empty and is_right_empty:
                flowerbed[i] = 1
                count -= 1
                i += 1
    return count == 0
