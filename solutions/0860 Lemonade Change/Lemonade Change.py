def lemonadeChange(bills):
   sum5, sum10, sum20 = 0, 0, 0

   for bill in bills:
      if bill == 5:
         sum5 += 1
         
      elif bill == 10: 
         # return 5
         sum10 += 1
         sum5 -= 1
         if sum5 < 0:
            return False
         
      elif bill == 20:
         # change is 15; either return 10 + 5 or 5 + 5 + 5
         sum20 += 1
         if sum10 >= 0:
            sum10 -= 1
            sum5 -= 1
            if sum5 < 0: 
               return False

         # check for equals because you can have 0 $5 bills
         elif sum5 >= 0: 
            sum5 -= 3
            if sum5 < 0: 
               return False
            
   return True