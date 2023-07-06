def reverseVowels(s):
    def replaceString(s, i, char):
        return s[:i] + char + s[i + 1:]
 
    vowels = "aeiouAEIOU"
    n = len(s)
    vowels_in_str = []
    output = s
    
    if n == 1: return s
    
    for char in s:
        if char in vowels:
            vowels_in_str.append(char)
            
    for i in range(n):
        if s[i] in vowels:
            current_vowel = vowels_in_str[-1]
            output = replaceString(output, i, current_vowel)
            vowels_in_str = vowels_in_str[:-1]
            
    return output