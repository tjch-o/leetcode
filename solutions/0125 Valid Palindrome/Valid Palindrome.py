def isPalindrome(s):
    def is_alphanumeric(char):
        numbers = [str(i) for i in range(10)]
        alphabets = list(map(lambda x: chr(x), [i for i in range(97,123)]))
        return char in numbers or char in alphabets
    
    def create_alphanumeric_string(s):
        result = ""
        for char in s:
            if is_alphanumeric(char):
                result += char  
        return result
    
    lowercase_s = s.lower()
    result = create_alphanumeric_string(lowercase_s)
    return result == result[::-1]
