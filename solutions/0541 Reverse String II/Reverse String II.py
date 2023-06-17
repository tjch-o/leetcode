def reverseStr(s,k):
   if k == 0:
      return s
   if len(s) < k:
      # reverse all of them
      return s[::-1]
   else: 
      # reverse first k characters of every 2k
      return s[:k][::-1] + s[k:2 * k] + reverseStr(s[2 * k:], k)