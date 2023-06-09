def check_row(matrix,i,j):
   # if given the coordinates check min in row
   row = matrix[i]
   if matrix[i][j] == min(row):
      return True
   return False

def check_col(matrix, i,j):
   # if given the coordinates check max in col
   col = list(map(lambda x: x[j], matrix))  # given the indexes we use the col number and extract the column to check 
   if matrix[i][j] == max(col):
      return True
   return False

def luckyNumbers(matrix):
   lucky_nums = [] # return numbers in any order
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if check_row(matrix,i,j) and check_col(matrix, i,j):
            lucky_nums.append(matrix[i][j])
   return lucky_nums

matrix = [[3,7,8],[9,11,13],[15,16,17]]

# i realised i saved a lot of runtime by just leaving the loop to the actual function and we check each element to see if it matches but we also use their indexes
# if we for loop in the check row and check col function the runtime will be insane
# similar idea to re-PE the concentric matrix question where we checked each point when given the matrix and their coordinates to see what is the shortest distance to the edge
