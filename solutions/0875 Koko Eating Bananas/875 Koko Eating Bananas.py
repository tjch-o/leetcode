def minEatingSpeed(piles, h):
    def hoursToFinishPile(num, speed):
        remainder = num % speed
        return num // speed + 1 if remainder != 0 else num // speed

    def hoursToFinishWholePile(piles, speed):
        count = 0
        for pile in piles:
            count += hoursToFinishPile(pile, speed)
        return count

    start = 1
    end = max(piles)

    while start <= end:
        middle = start + (end - start) // 2
        if hoursToFinishWholePile(piles, middle) <= h:
            end = middle - 1
        else:
            start = middle + 1
    return start
