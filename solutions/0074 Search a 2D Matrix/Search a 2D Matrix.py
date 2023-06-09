def searchMatrix(matrix, target):
   # can unnest this matrix using extend
   x = []
   for element in matrix:
      x.extend(element)

   if target in x:
      return True
   return False