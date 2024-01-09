def getRow(rowIndex):
   if rowIndex == 0:
      return [1]
   elif rowIndex == 1:
      return [1, 1]
   else:
      previous_row = getRow(rowIndex - 1)
      result = [1]
      
      for i in range(1, len(previous_row)):
         result.append(previous_row[i - 1] +  previous_row[i])
         
      result.append(1)
      return result