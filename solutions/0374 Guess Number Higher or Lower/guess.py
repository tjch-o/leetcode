def guess_number(n):
    start = 1
    end = n

    while True:
        middle = start + (end - start) // 2
        if guess(middle) == 0:
            return middle
        elif guess(middle) == 1:
            start = middle + 1
        else:
            end = middle - 1
