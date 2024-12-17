def min_cost_to_move_chips(position):
    odds = 0
    evens = 0

    for pos in position:
        if pos % 2 == 0:
            evens += 1
        else:
            odds += 1
    return min(odds, evens)
