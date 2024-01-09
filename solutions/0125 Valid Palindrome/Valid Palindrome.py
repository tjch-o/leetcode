def isPalindrome(s):
    def isAlphanumeric(char):
        numbers = [str(i) for i in range(10)]
        alphabets = list(map(lambda x: chr(x), [i for i in range(97,123)]))
        return char in numbers or char in alphabets
    
    def createAlphanumericString(s):
        result = ""
        for char in s:
            if isAlphanumeric(char):
                result += char  
        return result
    
    lowercase_s = s.lower()
    result = createAlphanumericString(lowercase_s)
    return result == result[::-1]
