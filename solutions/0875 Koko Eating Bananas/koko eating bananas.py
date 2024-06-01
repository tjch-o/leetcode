def min_eating_speed(piles, h):
    def hours_for_one_pile(num, speed):
        remainder = num % speed
        return num // speed + 1 if remainder != 0 else num // speed

    def hours_for_whole_pile(piles, speed):
        count = 0
        for pile in piles:
            count += hours_for_one_pile(pile, speed)
        return count

    start = 1
    end = max(piles)

    while start <= end:
        middle = start + (end - start) // 2
        if hours_for_whole_pile(piles, middle) <= h:
            end = middle - 1
        else:
            start = middle + 1
    return start
