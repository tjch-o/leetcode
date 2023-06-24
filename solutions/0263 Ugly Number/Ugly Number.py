def isUgly(n):
   if n == 0:
      return False
   
   for factor in [2, 3, 5]:
      while n % factor == 0:
         n = n // factor
   return n == 1