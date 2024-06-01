def is_palindrome(s):
    s = s.lower()
    nums = [str(i) for i in range(10)]
    alphabets = [chr(i) for i in range(97, 123)]

    x = ""
    for c in s:
        if c in nums or c in alphabets:
            x += c
    return x == x[::-1]
