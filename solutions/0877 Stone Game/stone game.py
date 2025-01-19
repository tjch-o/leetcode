def stone_game(piles):
    left, right = 0, len(piles) - 1
    left_count, right_count = 0, 0
    turn = 0

    while left <= right:
        left_pile, right_pile = piles[left], piles[right]

        if turn == 0:
            if left_pile < right_pile:
                left_count += left_pile
                left += 1
            else:
                left_count += right_pile
                right -= 1
        else:
            if left_pile < right_pile:
                right_count += left_pile
                left += 1
            else:
                right_count += right_pile
                right -= 1
        turn = 1 if 0 else 0
    return left_count > right_count
