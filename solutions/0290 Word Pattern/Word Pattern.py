def wordPattern(pattern, s):
    table = {}
    words_list = s.split(" ")
    
    if len(pattern) != len(words_list):
        return False
    else:
        n = len(words_list)
        for i in range(n):
            if pattern[i] not in table:
                # check to ensure bijection 
                if words_list[i] not in table.values():
                    table[pattern[i]] = words_list[i]
                else:
                    return False
            else:
                value = table[pattern[i]]
                if value != words_list[i]:
                    return False
        return True