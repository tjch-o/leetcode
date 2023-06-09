def isHappy(n):
   def sumDigitSquares(number):
      str_num = str(number)
      sum = 0
      for digit in str_num:
         sum += int(digit)**2
      return sum

   x = n
   seen = set()
   while sumDigitSquares(x) != 1:
      if (x not in seen):
         seen.add(x)
         x = sumDigitSquares(x)
      else:
         # there will be a cycle where the sequence of numbers repeat without reaching 1
         return False
   return True
