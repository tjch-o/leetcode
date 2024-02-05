def generate(num_rows):
   if num_rows == 1:
      return [[1]]
   elif num_rows == 2:
      return [[1], [1, 1]]
   else:
      result = generate(num_rows - 1)
      previous_row = result[-1]
      new_row = [1] 
      
      for i in range(1, len(previous_row)):
         new_row.append(previous_row[i - 1] + previous_row[i])
         
      new_row.append(1)
      result.append(new_row)
      return result