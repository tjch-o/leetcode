def reverse(x):
    numstring = str(x)
    reverse_num = numstring[::-1]

    if numstring[0] == "-": 
        reverse_num = reverse_num[-1] + reverse_num[:-1]

    reverse_num = int(reverse_num)
    if reverse_num < -2**31 or reverse_num >= 2**31: 
        return 0 
    return reverse_num