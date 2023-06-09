def uniqueOccurences(arr):
    table = {}
    for num in arr:
        if num not in table:
            table[num] = arr.count(num)
            
    seen = {}
    for count in table.values():
        if count not in seen:
            seen[count] = True
        else:
            return False
    return True