def isPalindrome(x):
    str_x = str(x)

    if str_x == str_x[::-1]:
        return True
    return False