def longest_palindrome(s):
    if len(s) == 1:
        return 1
    else:
        table = {}
        longest_length = 0   
        odd_flag = False 
        
        for char in s:
            if char not in table:
                table[char] = s.count(char)
            
        for count in table.values():
            if count % 2 == 0:
                longest_length += count
            else:
                odd_flag = True
                longest_length += (count - 1)
        
        return longest_length + 1 if odd_flag else longest_length