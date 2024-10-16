def min_bit_flips(start, goal):
    res = start ^ goal

    count = 0
    while res != 0:
        if res & 0x1 == 1:
            count += 1
        res = res >> 1
    return count
