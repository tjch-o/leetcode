def count_row(lst):
    return len(list(filter(lambda x: x < 0, lst)))


def count_negatives(grid):
    count = 0
    for row in grid:
        count += count_row(row)
    return count
