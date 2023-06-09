from math import floor

def diagonalSum(mat):
  # we know the matrix given is square
  # case 1 is mat is order n where n is odd that is when we remove the middle
  # else can ignore middle guy add everything together
  num_rows = len(mat)
  num_cols = len(mat[0])
  odd_indicator = True if num_rows % 2 != 0 else False

  def first_diagonal(i,j, accumulate):
    if i >= num_rows or j >= num_cols:
      return accumulate
    else:
      return first_diagonal(i + 1, j + 1, mat[i][j] + accumulate)

  def second_diagonal(i,j, accumulate):
    if i >= num_rows or j < 0:
      return accumulate
    else:
      return second_diagonal(i + 1, j - 1, mat[i][j] + accumulate)

  total_sum = first_diagonal(0,0,0) + second_diagonal(0, num_cols - 1, 0)

  if odd_indicator:
    middle = floor(num_rows / 2)
    # same middle for both row and column
    return total_sum - mat[middle][middle]
  else:
    return total_sum
    

