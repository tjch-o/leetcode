def countMatches(items, ruleKey, ruleValue):
   if ruleKey == "type":
      i = 0
   elif ruleKey == "color":
      i = 1
   elif ruleKey == "name":
      i = 2

   items = list(filter(lambda x: x[i] == ruleValue, items))
   return len(items)