def check_row(matrix,i,j):
   row = matrix[i]
   if matrix[i][j] == min(row):
      return True
   return False

def check_col(matrix, i,j):
   col = list(map(lambda x: x[j], matrix))  
   if matrix[i][j] == max(col):
      return True
   return False

def luckyNumbers(matrix):
   lucky_nums = [] 
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if check_row(matrix, i, j) and check_col(matrix, i, j):
            lucky_nums.append(matrix[i][j])
   return lucky_nums