from math import floor

def diagonal_sum(mat):
    # we know the matrix given is square
    # case 1 is mat is order n where n is odd that is when we remove the middle
    # else can ignore middle guy add everything together
    m = len(mat)
    n = len(mat[0])
    odd_indicator = True if m % 2 != 0 else False

    def first_diagonal(i, j, accumulate):
        if i >= m or j >= n:
            return accumulate
        else:
            return first_diagonal(i + 1, j + 1, mat[i][j] + accumulate)

    def second_diagonal(i, j, accumulate):
        if i >= m or j < 0:
            return accumulate
        else:
            return second_diagonal(i + 1, j - 1, mat[i][j] + accumulate)

    total_sum = first_diagonal(0, 0, 0) + second_diagonal(0, n - 1, 0)

    if odd_indicator:
        middle = floor(m / 2)
        # same middle for both row and column
        return total_sum - mat[middle][middle]
    else:
        return total_sum
